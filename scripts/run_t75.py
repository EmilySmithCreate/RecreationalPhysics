"""T75: does a disturbance in the toy's open space spread, and at what speed? Usage:

    python scripts/run_t75.py configs/t75_n512_beside_g1p5.json [out_dir]

Implements PREREGISTRATION.md section T75 with its Amendments 1 to 5. Not exploratory once its couplings are fixed
by amendment; nothing here chooses them.

The space (Amendment 2, item 1). The saved end states of a T51 run (`<states_dir>/<states>_NN_adj/N*_rep*_tc*.npz`,
written by scripts/run_scrap_freeze.py: `adj`, `part`, `lam`, `t_cool`, `replica`), taken in order of their replica
number. Each is checked to be a valid state (cqg.is_valid, no cap) and bipartite with side_u = the points with
part == 0. A state in more than one piece is skipped (Amendment 3, item 3); the run's meta lists which.

The flaw (Amendment 3, item 1): graphity.coupled.cheapest_switch_at, the cheapest valid switch of an edge at the chosen
point with an edge within `flaw_reach` (3) steps, priced exactly at `lambda` (1.25) against the unflawed state, ties
broken in a fixed sorted order. Beside a knot (Amendment 4) it is the cheapest among the switches that touch no knot
point. Only switches costing strictly more than zero count, beside or far (Amendment 5): a cost-free rewiring is
never a flaw. Its cost is written in every row of its replica.

The placement (Amendment 3, item 2, and Amendment 4). The knots are read from the wiring as T55 read them
(analyse_t55.pieces_of: the connected pieces of points not at d = 2); their points are the knot points. "beside":
the starting point is 1 or 2 steps from a knot point and the flaw touches no knot point, so its nearest point is 1 or
2 steps from one; "far": every point of the flaw is at least 6 steps from
every knot point. The points that could start such a flaw are tried in an order drawn from the replica's own placement
stream, and the first whose flaw meets the rule is taken. A state with no knot has no "beside" placement.

Replicas (Amendment 3, item 3): `replicas` (32) per cell. The connected states are taken in replica order; when they
are used up before every replica has a flaw, they are used again in the same order, each new replica with its own
placement and chain streams and a placement different from every earlier one in that state. The row's `use` says
which pass over the states it came from (0 for the first); the meta lists every replica's state, pass, flaw and cost.
The run refuses to start if a whole pass adds no replica.

The run. Copy A is the state as saved, copy B the same state with the flaw. The two are advanced together by
graphity.coupled.run_coupled (Metropolis, no cap, the coupling of Amendment 2, item 3) at coupling `g` and `lambda`,
for `fair_sweeps` fair sweeps (one fair sweep is N^2 * 2 / n_ref attempts; O90), read every `record_every` fair
sweeps, the remainder carried from record to record so that after k fair sweeps exactly floor(2 N^2 k / n_ref)
attempts have been made. A first reading is taken before any attempt.

Readings (Amendment 2, item 4), each on the shared starting graph (the state as saved): `damaged`, the points whose
neighbours differ between the copies; `R`, the distance of the farthest damaged point from the nearest of the flaw's
four points (-1 when nothing is damaged; a point the flaw's piece cannot reach counts at distance N); `joined_R`, the
same for the damaged region joined to the flaw through damaged points at most `step` (2) steps apart (-1 if empty);
`jump`, damage with none joined to the flaw, or some farther than twice joined_R. `D` is the diameter of the starting
graph. One row per reading. The verdicts are read by scripts/analyse_t75.py.

Config keys: name, section, states_dir, states, N, lambda, g, placement ("beside" or "far"), replicas, fair_sweeps,
record_every, n_ref, step, flaw_reach, seed.
"""
import json
import platform
import re
import sys
from pathlib import Path

import numba
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
sys.path.insert(0, str(Path(__file__).resolve().parent))
from graphity import __version__                                                  # noqa: E402
from graphity.coupled import (cheapest_switch_at, diameter, fair_sweep_schedule, graph_distances,  # noqa: E402
                              read_records, run_coupled)
from graphity.cqg import NO_CAP, is_valid                                         # noqa: E402
from graphity.results import ResultWriter, provenance                             # noqa: E402
from analyse_t55 import pieces_of                                                 # noqa: E402

BESIDE, FAR = (1, 2), 6              # Amendment 3, item 2: beside at 1 or 2 steps, far at 6 or more
PLACE, CHAIN = 1, 2                  # stage words for the random streams


def stream_seed(seed, n, rep, stage):
    return int(np.random.SeedSequence([int(seed), int(n), int(rep), int(stage)]).generate_state(1)[0])


def load_states(states_dir, run):
    """[(path, adj, part, replica)] for every saved end state of `run`, in order of replica number."""
    dirs = [d for d in Path(states_dir).iterdir() if d.is_dir() and re.fullmatch(re.escape(run) + r"_\d+_adj", d.name)]
    found = []
    for d in dirs:
        for p in d.glob("N*_rep*_tc*.npz"):
            z = np.load(p)
            adj = np.ascontiguousarray(z["adj"], dtype=np.int64)
            part = np.asarray(z["part"], dtype=np.int64)
            if not is_valid(adj, NO_CAP):
                raise ValueError("%s is not a valid state" % p)
            if not np.all(part[:, None] != part[adj]):
                raise ValueError("%s: a link joins two points of one side" % p)
            found.append((p, adj, part, int(z["replica"])))
    found.sort(key=lambda t: t[3])
    if not found:
        raise FileNotFoundError("no saved states of %s in %s" % (run, states_dir))
    if len({t[3] for t in found}) != len(found):
        raise ValueError("two saved states of %s share a replica number" % run)
    return found


def knot_points(adj):
    """The points of every knot, read as T55 read them (pieces of points not at d = 2)."""
    pieces, _ = pieces_of(adj)
    return np.array(sorted(v for piece in pieces for v in piece), dtype=np.int64)


def is_connected(adj):
    return bool((graph_distances(adj, np.array([0], dtype=np.int64)) >= 0).all())


def place_flaw(adj, knots, placement, seed, lam, reach, exclude=()):
    """(flawed copy, four points, its cost, distance of the flaw's nearest point from a knot point or -1 if there are
    no knots), or None if the placement does not exist in this state. A flaw whose four points, as a set, are in
    `exclude` is passed over (a reused state gets a different placement)."""
    n = adj.shape[0]
    if knots.size:
        to_knot = graph_distances(adj, knots)
        to_knot[to_knot < 0] = n
    else:
        to_knot = np.full(n, n, dtype=np.int64)
    if placement == "beside":
        if not knots.size:
            return None
        starts = np.flatnonzero((to_knot >= BESIDE[0]) & (to_knot <= BESIDE[1]))
    elif placement == "far":
        starts = np.flatnonzero(to_knot >= FAR)
    else:
        raise ValueError("placement must be 'beside' or 'far'")
    for p in np.random.default_rng(seed).permutation(starts):
        try:
            flawed, four, cost = cheapest_switch_at(adj, int(p), lam, reach, NO_CAP,
                                                    avoid=knots if placement == "beside" else None, above=0.0)
        except ValueError:
            continue
        if frozenset(four) in exclude:
            continue
        near = int(to_knot[list(four)].min())
        if (placement == "beside" and BESIDE[0] <= near <= BESIDE[1]) or (placement == "far" and near >= FAR):
            return flawed, four, cost, (near if knots.size else -1)
    return None


def assign(states, cfg):
    """[(state index, pass, flawed copy, four points, cost, knot distance)] for each replica, fixed before any chain
    runs (Amendment 3, item 3)."""
    n_rep = int(cfg["replicas"])
    usable = [i for i, (_, adj, _, _) in enumerate(states) if is_connected(adj)]
    knots = {i: knot_points(states[i][1]) for i in usable}
    used = {i: set() for i in usable}
    out, n_pass = [], 0
    while len(out) < n_rep:
        before = len(out)
        for i in usable:
            if len(out) == n_rep:
                break
            adj = states[i][1]
            got = place_flaw(adj, knots[i], cfg["placement"], stream_seed(cfg["seed"], adj.shape[0], len(out), PLACE),
                             float(cfg["lambda"]), int(cfg["flaw_reach"]), used[i])
            if got is not None:
                used[i].add(frozenset(got[1]))
                out.append((i, n_pass) + got)
        if len(out) == before:
            raise ValueError("a whole pass over the %d connected states added no '%s' placement; %d of %d replicas"
                             % (len(usable), cfg["placement"], len(out), n_rep))
        n_pass += 1
    return out


def piece_diameter(adj, members):
    """The diameter of the connected piece made of `members` (the whole graph when it is connected)."""
    if members.all():
        return int(diameter(adj))
    best = 0
    for s in np.flatnonzero(members):
        best = max(best, int(graph_distances(adj, np.array([s], dtype=np.int64)).max()))
    return best


def main(path, out_dir="results"):
    cfg = json.loads(Path(path).read_text())
    if cfg.get("section") != "T75":
        raise ValueError("not a T75 config")
    for p in (Path(out_dir) / (cfg["name"] + ".csv"), Path(out_dir) / (cfg["name"] + ".meta.json")):
        if p.exists():
            raise FileExistsError("results are append-only; %s exists" % p)
    lam, g = float(cfg["lambda"]), float(cfg["g"])
    states = load_states(cfg["states_dir"], cfg["states"])
    n = states[0][1].shape[0]
    if n != int(cfg["N"]) or any(s[1].shape[0] != n for s in states):
        raise ValueError("the saved states are not all of N = %s" % cfg["N"])
    sched, fair = fair_sweep_schedule(n, int(cfg["fair_sweeps"]), int(cfg["record_every"]), int(cfg["n_ref"]))
    plan = assign(states, cfg)
    meta = dict(config=cfg, config_path=str(path), package=__version__, python=platform.python_version(),
                numpy=np.__version__, numba=numba.__version__, **provenance(),
                replicas_plan=[dict(replica=rep, state=str(states[k][0]), use=use, flaw=[int(v) for v in four],
                                    flaw_cost=cost, knot_distance=near)
                               for rep, (k, use, _, four, cost, near) in enumerate(plan)],
                skipped_disconnected=[str(s[0]) for s in states if not is_connected(s[1])],
                preregistration="PREREGISTRATION.md section T75, with its Amendments 1 to 5")
    with ResultWriter(cfg["name"], meta, out_dir) as out:
        for rep, (k, use, flawed, four, cost, near) in enumerate(plan):
            file, start, part, state_rep = states[k]
            side_u = np.flatnonzero(part == 0)
            anchors = np.array(four, dtype=np.int64)
            piece = graph_distances(start, anchors) >= 0
            d_start = piece_diameter(start, piece)
            a, b = start.copy(), flawed.copy()
            res = run_coupled(a, b, side_u, 1.0 / g, len(sched), sched, stream_seed(cfg["seed"], n, rep, CHAIN),
                              lam, NO_CAP)
            damaged, radius, joined, jump = read_records(start, res["mask"], anchors, int(cfg["step"]))
            done = np.cumsum(sched)
            base = dict(N=n, g=g, lam=lam, placement=cfg["placement"], replica=rep, state=file.name,
                        state_replica=state_rep, use=use, flaw=" ".join(str(v) for v in four), flaw_cost=cost,
                        knot_distance=near, D=d_start,
                        acceptance_a=res["acceptance_a"], acceptance_b=res["acceptance_b"])
            for r in range(len(sched)):
                out.write(dict(**base, fair_sweep=int(fair[r]), attempts=int(done[r]), damaged=int(damaged[r]),
                               R=int(radius[r]), joined_R=int(joined[r]), jump=bool(jump[r])))
            print("%s rep %d (%s): damaged %d -> %d, R max %d, D %d, jumps %d"
                  % (cfg["name"], rep, file.name, damaged[0], damaged[-1], radius.max(), d_start, int(jump.sum())),
                  flush=True)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else "results")

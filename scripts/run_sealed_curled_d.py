"""T30 and T32: a curled six-link torus in a sealed box, given a spark. Usage:

    python scripts/run_sealed_curled_d.py configs/t30_cascade_lam110_n288_c2n.json

Implements PREREGISTRATION.md sections T30 (does one push open both curled directions: the cascade and the room)
and T32 (is the activation fixed with size) on the six-link model (graphity.cqg_d, graphity.sealed_d; VISION
Update 22; ASSUMPTIONS O41). The torus C_4 x C_4 x C_L has two directions curled and one open, 8(lambda - 1) per
vertex above the flat 3-torus; the run puts a spark of E units in one store of a bath of C stores, all else empty,
and follows it for `n_sweeps` sweeps in blocks of `record_every`. Recorded every block: S, X, H per vertex, the
census of the local dimension read at six links (d = 3 flat, 2 one curled, 1 two curled, 0 all curled, above 3
melted), the bath temperature and the conservation check; at the end, the pieces of the flat region and whether
the arrangement ever left its start (T32's question). The final graph is saved when `save_adjacency` is set.

Config keys: name, section, dims (e.g. [4, 4, 18]) or gas ({"dims": [4, 4, 4], "copies": 8}: that many separate
tori, the literal form of the owner's fully curled X), lambda, capacities (expressions in N, as T18), sparks (a
list of E), replicas, n_sweeps, record_every, seed, save_adjacency, and "local_heat" (T34): true puts the spark in
the store of the first side-0 vertex under the per-vertex bath (sealed_d.run_sealed_bath_d with by_vertex), so only a
move made from that vertex can spend it and released energy stays where it is released; capacities are then ignored
and C is recorded as N.
"""
import json
import platform
import sys
from pathlib import Path

import numba
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from graphity import __version__                                          # noqa: E402
from graphity.cqg_d import surplus, torus, total_squares                  # noqa: E402
from graphity.dimension import local_dimension_d, pieces_of               # noqa: E402
from graphity.results import ResultWriter                                 # noqa: E402
from graphity import interchangeable_d                                  # noqa: E402
from graphity.sealed_d import energy_d, run_sealed_bath_d                 # noqa: E402

D_BINS = 8       # d = 0 .. 6 and "7 or more"


def census(adj, lam):
    d = local_dimension_d(adj)
    hist = np.bincount(np.minimum(d, D_BINS - 1), minlength=D_BINS)[:D_BINS]
    flat = pieces_of(adj, d == 3)
    return dict(h_per_vertex=float(energy_d(adj, lam)) / adj.shape[0],
                **{"d%d" % i: int(hist[i]) for i in range(D_BINS)},
                melted=int((d > 3).sum()), pieces_flat=len(flat), largest_flat=(flat[0] if flat else 0))


def gas(dims, copies):
    """`copies` separate tori C_dims, one after another in the vertex numbering."""
    a, p = torus(dims)
    n = a.shape[0]
    return np.concatenate([a + k * n for k in range(copies)]), np.concatenate([p] * copies)


def start_of(cfg):
    if "gas" in cfg:
        g = cfg["gas"]
        adj, part = gas([int(x) for x in g["dims"]], int(g["copies"]))
        return adj, part, "%dx(%s)" % (int(g["copies"]), " ".join(map(str, g["dims"])))
    dims = [int(x) for x in cfg["dims"]]
    adj, part = torus(dims)
    return adj, part, " ".join(map(str, dims))


def main(path, out_dir="results"):
    cfg = json.loads(Path(path).read_text())
    lam = float(cfg["lambda"])
    adj0, part0, label = start_of(cfg)
    n = adj0.shape[0]
    every, n_sweeps = int(cfg.get("record_every", 100)), int(cfg["n_sweeps"])
    local_heat = bool(cfg.get("local_heat", False))
    # T42 (2026-09-25): interchangeable points through graphity.interchangeable_d (the bath only); "weighted": false
    # runs the same chain with named points, as a control. Absent, the runner is what it was.
    interchangeable = bool(cfg.get("interchangeable", False))
    weighted = bool(cfg.get("weighted", True))
    if interchangeable and local_heat:
        raise ValueError("interchangeable points are run with the shared bath only")
    baths = [n] if local_heat else [int(round(eval(str(c), {"N": n}))) for c in cfg["capacities"]]
    meta = dict(config=cfg, config_path=str(path), package=__version__, python=platform.python_version(),
                numpy=np.__version__, numba=numba.__version__,
                preregistration="PREREGISTRATION.md section %s, written 2026-09-25" % cfg.get("section", "T30"))
    adj_dir = Path(out_dir) / (cfg["name"] + "_adj")
    with ResultWriter(cfg["name"], meta, out_dir) as out:
        for c_bath in baths:
            for spark in cfg["sparks"]:
                for rep in range(int(cfg["replicas"])):
                    adj, part = adj0.copy(), part0.copy()
                    side_u = np.flatnonzero(part == 0)
                    stores = np.zeros(c_bath)
                    stores[int(side_u[0]) if local_heat else 0] = float(spark)
                    h0 = energy_d(adj, lam)
                    e0 = h0 + stores.sum()
                    s_start, x_start = int(total_squares(adj)), int(surplus(adj))
                    seed = int(np.random.SeedSequence([int(cfg["seed"]), n, c_bath, int(round(float(spark) * 100)), rep]).generate_state(1)[0])
                    left = False
                    left_at = ""
                    base = dict(N=n, dims=label, C=c_bath, spark=float(spark), replica=rep, lam=lam, local_heat=local_heat)
                    if interchangeable:                                   # T42; absent from earlier files
                        base.update(interchangeable=True, weighted=weighted)
                    c0 = census(adj, lam)
                    out.write(dict(**base, sweep=0, **c0, bath_T=float(stores.mean()), total=float(stores.sum()),
                                   drift=0.0, left=False, final=False))
                    blocks = n_sweeps // every
                    rng = np.random.default_rng(seed) if interchangeable else None
                    for b in range(1, blocks + 1):
                        if interchangeable:
                            s, x, _, tot = interchangeable_d.run(adj, part, every, seed, lam, demons=stores,
                                                                 weighted=weighted, rng=rng)
                            mean = tot / len(stores)
                        else:
                            s, x, mean, tot, _ = run_sealed_bath_d(adj, side_u, stores, every, seed if b == 1 else -1, lam,
                                                                   by_vertex=local_heat)
                        if not left and ((s != s_start).any() or (x != x_start).any()):
                            left = True
                            left_at = b * every
                        c = census(adj, lam)
                        drift = abs(c["h_per_vertex"] * n + tot[-1] - e0)
                        out.write(dict(**base, sweep=b * every, **c, bath_T=float(mean[-1]), total=float(tot[-1]),
                                       drift=float(drift), left=left, final=(b == blocks)))
                    if cfg.get("save_adjacency"):
                        adj_dir.mkdir(parents=True, exist_ok=True)
                        np.savez(adj_dir / ("C%d_E%d_rep%d.npz" % (c_bath, int(round(float(spark))), rep)), adj=adj, part=part,
                                 lam=lam, h0=h0, e0=e0)
                    c = census(adj, lam)
                    print("dims=%s C=%d E=%g rep=%-2d left=%s at %s | end: d3 %d d2 %d d1 %d melted %d | H/N %.3f (start %.3f) | T %.2f"
                          % (base["dims"], c_bath, spark, rep, left, left_at, c["d3"], c["d2"], c["d1"], c["melted"],
                             c["h_per_vertex"], h0 / n, stores.mean()), flush=True)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else "results")

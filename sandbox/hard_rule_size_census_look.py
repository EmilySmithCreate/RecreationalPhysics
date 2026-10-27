"""Sandbox look (exploratory; rule 16: it can kill, never crown), 26 October 2026: the four-link size census of the
hard rule with a held-out size (item 3 (c) of `docs/design/next_experiments_2026-10-26.md`; the owner said "proceed"
at 22:41 UTC by the clock; an earlier draft of this line said 22:52). Usage:

    python sandbox/hard_rule_size_census_look.py L [--procs 3]        # the flat L x L torus, four links a point
    python sandbox/hard_rule_size_census_look.py 16,10                # today's 16 x 10 check against 480 / 448 / 32
    python sandbox/hard_rule_size_census_look.py --rescore            # score the saved held-out JSON (no rerun)

THE QUESTION, declared before any run. Does the hard rule (the square count S held at exactly N for four links;
VISION Update 105) freeze the clean flat L x L torus at every size, under (i) single switches, (ii) pairs of switches
with the second within two links of the first's four points (radius 2, as `hard_rule_pairs_look.py`), and (iii)
triples with the second within one link of the first's four points and the third within one link of the eight (radius
1, as `hard_rule_triples_look.py`)? And how does the number of count-keeping moves scale with L?

WHAT IS COUNTED (exact definitions).
  A switch (u1 v1, u2 v2) -> (u1 v2, u2 v1) with u1, u2 on one side of the bipartition; every graph on the way obeys
  the hard-core rule (no two points share more than two neighbours; `cqg_d._new_edge_ok`). The first switch has
  u1 = 0 (every switch has a translate with a side-0 point at 0, so counting from point 0 counts each translation
  class once, up to the written forms below). As in the triples look, a sequence is a WRITTEN FORM: a switch written
  from either side and the later switches in either order are counted separately, so the counts are of written
  forms, not of distinct sequences; the number of DISTINCT END STATES (distinct final edge sets) is printed beside.
  A sequence is RESTORING if its changes in S sum to zero. It LEAVES THE START if the final edge set differs from
  the torus's. Undoing the previous switch is excluded for the second switch in both written forms (as the corrected
  pairs look does); the third may undo the second, and such sequences return the start and are counted as "back".
  Of the restoring sequences that leave the start, each end state is a RENAMING if it is isomorphic to the start
  (networkx `is_isomorphic` on the end state against the torus, run only when the end state has curl 0 and anticurl
  0, since any other end state has a square-per-link histogram the torus does not and is not isomorphic; so the
  split is exact) and a REAL MOVE otherwise.
  Per real move, OPENS / DAMAGES: DAMAGES if the end state has any point whose local dimension d(v) (the number of
  the six link pairs at v that close no square; `graphity.dimension.local_dimension`; 2 at every point of the flat
  L x L torus) exceeds 2, the torus's value, OR any link carries fewer than 1 square (a link in no square at all);
  OPENS otherwise. Both read from the end state, exact.
  Also per sequence: the change in curl (squares above 2 on a link, summed), in anticurl (squares below 2, summed) and
  dH at lambda 1.25 (H = 4 anticurl + 4 (lambda - 1) curl, exact).

WORDS, declared before any run.
  Singles and pairs: FROZEN AT ALL SIZES if the number of REAL count-keeping moves (not renamings) is zero at every
  L run; THAWS AT SMALL L (first L named) otherwise, naming the smallest L with a real move. Renamings are reported
  beside and do not thaw anything (they are the same arrangement with its points renamed, not the space moving).
  Triples: the count of restoring written forms that leave the start, split into renamings and real moves, with the
  OPENS / DAMAGES split of the real moves, per L.

RULE OBEDIENCE (exact, printed at the start of every run): the flat L x L torus has every link in exactly 2 squares,
S = N, curl 0, anticurl 0, so it obeys the four-link form of the hard rule. The 16 x 10 torus likewise (S = 160).

COST, estimated before running: the number of first switches from point 0 grows as N (u2 ranges over the N/2 side
points), while the radius-2 ball (at most 4 x 17 = 68 points) and the radius-1 balls (at most 16 and 32 points) are
bounded, so every stage is linear in N. L = 6 is timed first and the times for L = 8, 10, 12 printed as that time
scaled by N; the measured times are printed beside them when those sizes run. Stage 3 is pruned exactly on the
running change in S (a switch gains at most 2 (deg - 1) = 6 squares with four links, as the triples look shows).

RULE 14 (held-out size). L = 6, 8 and 10 are computed first. The held-out prediction for L = 12 is then written into
HELD_OUT below with a timestamp from `date`, and printed, BEFORE L = 12 runs; the script refuses to run L = 12 while
HELD_OUT is None. L = 12 is then run and each count scored HELD / MISSED against its range.

HELD-OUT PREDICTION FOR L = 12, written Mon Oct 26 18:59:22 EDT 2026 (`date`) after L = 6, 8, 10 were read and
BEFORE L = 12 ran (ours; derived from L = 6, 8, 10 only; the full text is HELD_OUT below): singles 0; pairs 64
renamings and 0 real moves; triples 448 restoring written forms leaving the start, all 448 renamings (28 distinct
end states), 0 real moves (0 OPENS, 0 DAMAGES). Reason: the renamings were 448 / 64 / 0 at every L; every real
move seen was a wrap-around effect, the +4/+4 OPENS move of k switches appearing exactly at side 2k + 4 (singles
at 6, pairs at 8, triples at 10) and the DAMAGES moves only at sides 6 and 8, so side 12 is beyond the reach of
three switches. Each count is scored HELD / MISSED against its range after the run.

REUSE: the numba kernels `try_switch`, `curl_anti`, `same_edges`, `ball1` and the stage-2/3 driver `run_first` are
imported from `sandbox/hard_rule_triples_look.py`, and `second_moves` and `ball_of` from
`sandbox/hard_rule_pairs_look.py` (both guard their runs under __main__, so importing them runs nothing). Neither
file is modified.
"""
import json
import sys
import time
from collections import Counter
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path

import networkx as nx
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "sandbox"))
from graphity.cqg_d import squares_on_edge, torus  # noqa: E402
from graphity.dimension import local_dimension  # noqa: E402
import hard_rule_pairs_look as P  # noqa: E402
import hard_rule_triples_look as T  # noqa: E402

LAM = 1.25
OUT_DIR = ROOT / "sandbox" / "out" / "hard_rule_size_census"   # corrected 27 October (O163 F28): was a Windows scratchpad path

# Rule 14: filled in by hand after L = 6, 8, 10 were read and before L = 12 ran. None = not yet written.
# Each entry is (low, high), inclusive, for the count at L = 12; "formula" says how it was derived.
HELD_OUT = {
    "L": 12,
    "written": "Mon Oct 26 18:59:22 EDT 2026 (`date`), after L = 6, 8, 10 were read and before L = 12 ran",
    "derived_from": "L = 6, 8, 10 only (N = 36, 64, 100); the 16 x 10 count of the triples look read as a check",
    "formula": ("Renamings are CONSTANT in L: triples 448 written forms / 28 end states, pairs 64 / 12, singles 0 "
                "at every L (the renamings are local, so once L exceeds their reach their count is fixed). Real "
                "moves are WRAP-AROUND effects: a +4 curl / +4 anticurl OPENS move of k parallel switches appears "
                "exactly when a side equals 2k + 4 (k = 1 at side 6: 4 singles; k = 2 at side 8: 16 pair forms; "
                "k = 3 at side 10: 64 triple forms, and 32 on 16 x 10 where only one side is 10), and every DAMAGES "
                "move seen is at side 6 or 8 only (none at 10). At side 12 three switches cannot close round the "
                "torus (that needs k = 4), so the prediction is ZERO real moves of every kind, hence FROZEN for "
                "singles and pairs at L = 12 and triples = renamings only. Ranges are the sharp values; a nonzero "
                "real count at L = 12 would MISS and say the wrap reading is wrong."),
    "singles": (0, 0),
    "pairs_real": (0, 0),
    "pairs_renamings": (64, 64),
    "triples_restoring_leave": (448, 448),
    "triples_renamings": (448, 448),
    "triples_real": (0, 0),
    "triples_real_damages": (0, 0),
    "triples_real_opens": (0, 0),
    "triples_distinct_end_states": (28, 28),
}


def edge_key(adj):
    n, deg = adj.shape
    e = np.empty((n * deg, 2), dtype=np.int64)
    k = 0
    for u in range(n):
        for v in adj[u]:
            e[k, 0] = min(u, int(v))
            e[k, 1] = max(u, int(v))
            k += 1
    e = np.unique(e, axis=0)
    return e.tobytes()


def nx_graph(adj):
    g = nx.Graph()
    n = adj.shape[0]
    g.add_nodes_from(range(n))
    for u in range(n):
        for v in adj[u]:
            g.add_edge(u, int(v))
    return g


def min_squares_on_a_link(adj):
    n = adj.shape[0]
    m = 10 ** 9
    for u in range(n):
        for v in adj[u]:
            if u < int(v):
                m = min(m, int(squares_on_edge(adj, u, int(v))))
    return m


def classify_end_states(end_states, adj0, g0, flat):
    """end_states: dict edge_key -> (adj, count of written forms). Returns the per-kind tallies (exact)."""
    c0, a0 = T.curl_anti(adj0, flat)
    tally = Counter()
    kinds = Counter()
    examples = {}
    for key, (adj, cnt) in end_states.items():
        c, a = T.curl_anti(adj, flat)
        dc, da = int(c - c0), int(a - a0)
        dh = round(4 * da + 4 * (LAM - 1) * dc, 2)
        if dc == 0 and da == 0:
            iso = nx.is_isomorphic(g0, nx_graph(adj))
        else:
            iso = False
        if iso:
            tally["renaming_forms"] += cnt
            tally["renaming_states"] += 1
            kinds[("renaming", dc, da, dh)] += cnt
        else:
            d = local_dimension(adj)
            dmax = int(d.max())
            mins = min_squares_on_a_link(adj)
            word = "DAMAGES" if (dmax > 2 or mins < 1) else "OPENS"
            tally["real_forms"] += cnt
            tally["real_states"] += 1
            tally[f"real_{word}_forms"] += cnt
            tally[f"real_{word}_states"] += 1
            k = ("real", word, dc, da, dh, dmax, mins)
            kinds[k] += cnt
            examples.setdefault(k, key)
    return tally, kinds


def first_switches(adj0, part):
    side = np.flatnonzero(part == part[0])
    out = []
    for v1 in adj0[0]:
        for u2 in side:
            for v2 in adj0[u2]:
                adj = adj0.copy()
                ok, ds1 = T.try_switch(adj, 0, int(v1), int(u2), int(v2))
                if ok:
                    out.append((0, int(v1), int(u2), int(v2), int(ds1)))
    return out


def triples_worker(dims, firsts):
    adj0, part = torus(dims)
    adj0 = np.asarray(adj0, dtype=np.int64)
    part = np.asarray(part, dtype=np.int64)
    n, deg = adj0.shape
    flat = deg - 2
    gmax = 2 * (deg - 1)
    mark = np.zeros(n, dtype=np.int64)
    ball = np.empty(n, dtype=np.int64)
    ball2 = np.empty(n, dtype=np.int64)
    hist = np.zeros((33, 33), dtype=np.int64)
    rows = np.zeros((400000, 17), dtype=np.int64)
    stamp = 0
    nrows = 0
    tot = Counter()
    m2 = m3 = -1000
    for (u1, v1, u2, v2, ds1) in firsts:
        r = T.run_first(adj0, part, u1, v1, u2, v2, ds1, gmax, flat, False,
                        mark, stamp, ball, ball2, hist, rows, nrows, adj0)
        n_second, n_kept, est3, n_third, n_rest, n_back, mm2, mm3, nrows, stamp = r
        tot["second"] += n_second
        tot["kept"] += n_kept
        tot["third"] += n_third
        tot["restoring"] += n_rest
        tot["back"] += n_back
        m2 = max(m2, mm2)
        m3 = max(m3, mm3)
    # end states of the recorded restoring sequences (keyed by edge set)
    ends = {}
    for i in range(nrows):
        x = rows[i]
        adj = adj0.copy()
        T._switch(adj, int(x[0]), int(x[1]), int(x[2]), int(x[3]))
        T._switch(adj, int(x[4]), int(x[5]), int(x[6]), int(x[7]))
        T._switch(adj, int(x[8]), int(x[9]), int(x[10]), int(x[11]))
        key = edge_key(adj)
        if key in ends:
            ends[key][1] += 1
        else:
            ends[key] = [adj, 1]
    return dict(tot), nrows, m2, m3, ends


def survey(dims, nproc):
    adj0, part = torus(dims)
    adj0 = np.asarray(adj0, dtype=np.int64)
    part = np.asarray(part, dtype=np.int64)
    n, deg = adj0.shape
    flat = deg - 2
    c0, a0 = T.curl_anti(adj0, flat)
    s0 = sum(int(squares_on_edge(adj0, u, int(v))) for u in range(n) for v in adj0[u] if u < int(v)) // 4
    s_rule = flat * deg * n // 8
    mins = min_squares_on_a_link(adj0)
    obeys = (s0 == s_rule and c0 == 0 and a0 == 0)
    print(f"flat torus {dims}: N = {n}, deg = {deg}, S = {s0} (hard rule: S = {s_rule}), curl {c0}, anticurl {a0}, "
          f"fewest squares on a link {mins}, max d(v) {int(local_dimension(adj0).max())}; "
          f"OBEYS THE FOUR-LINK HARD RULE: {obeys}")
    g0 = nx_graph(adj0)
    times = {}
    result = {"dims": list(dims), "N": n}

    # (i) singles
    t0 = time.time()
    firsts = first_switches(adj0, part)
    singles_ends = {}
    for (u1, v1, u2, v2, ds1) in firsts:
        if ds1 == 0:
            adj = adj0.copy()
            T._switch(adj, u1, v1, u2, v2)
            key = edge_key(adj)
            if key in singles_ends:
                singles_ends[key][1] += 1
            else:
                singles_ends[key] = [adj, 1]
    tally1, kinds1 = classify_end_states(singles_ends, adj0, g0, flat)
    times["singles"] = time.time() - t0
    by_ds = Counter(f[4] for f in firsts)
    print(f"stage 1: {len(firsts)} legal first switches from point 0, by dS: {dict(sorted(by_ds.items()))}")
    print(f"(i) SINGLES keeping S: {sum(c for _, c in singles_ends.values())} written forms, "
          f"{len(singles_ends)} distinct end states; renamings {tally1['renaming_forms']} forms / "
          f"{tally1['renaming_states']} states; REAL MOVES {tally1['real_forms']} forms / {tally1['real_states']} "
          f"states (OPENS {tally1['real_OPENS_forms']}, DAMAGES {tally1['real_DAMAGES_forms']}); {times['singles']:.1f} s")
    for k, c in sorted(kinds1.items(), key=str):
        print(f"    {k}: {c}")
    result["singles"] = dict(tally1)
    result["singles"]["forms"] = sum(c for _, c in singles_ends.values())

    # (ii) pairs at radius 2
    t0 = time.time()
    out = np.empty((400000, 4), dtype=np.int64)
    pair_ends = {}
    n_pairs = 0
    n_back2 = 0
    for (u1, v1, u2, v2, ds1) in firsts:
        adj = adj0.copy()
        T._switch(adj, u1, v1, u2, v2)
        ball = P.ball_of(adj, [u1, v1, u2, v2], 2)
        m = P.second_moves(adj, ball, part, -ds1, u1, v1, u2, v2, out)
        for r in range(m):
            b = adj.copy()
            T._switch(b, int(out[r, 0]), int(out[r, 1]), int(out[r, 2]), int(out[r, 3]))
            if T.same_edges(b, adj0):
                n_back2 += 1
                continue
            n_pairs += 1
            key = edge_key(b)
            if key in pair_ends:
                pair_ends[key][1] += 1
            else:
                pair_ends[key] = [b, 1]
    tally2, kinds2 = classify_end_states(pair_ends, adj0, g0, flat)
    times["pairs"] = time.time() - t0
    print(f"(ii) PAIRS (radius 2) restoring S and leaving the start: {n_pairs} written forms, {len(pair_ends)} distinct "
          f"end states (plus {n_back2} that return the start exactly); renamings {tally2['renaming_forms']} forms / "
          f"{tally2['renaming_states']} states; REAL MOVES {tally2['real_forms']} forms / {tally2['real_states']} states "
          f"(OPENS {tally2['real_OPENS_forms']}, DAMAGES {tally2['real_DAMAGES_forms']}); {times['pairs']:.1f} s")
    for k, c in sorted(kinds2.items(), key=str):
        print(f"    {k}: {c}")
    result["pairs"] = dict(tally2)
    result["pairs"].update({"forms": n_pairs, "back": n_back2})

    # (iii) triples at radius 1
    t0 = time.time()
    chunks = [firsts[i::nproc] for i in range(nproc)] if nproc > 1 else [firsts]
    tot = Counter()
    nrows = 0
    m2 = m3 = -1000
    ends = {}
    if nproc > 1:
        with ProcessPoolExecutor(max_workers=nproc) as ex:
            parts = list(ex.map(triples_worker, [list(dims)] * len(chunks), chunks))
    else:
        parts = [triples_worker(list(dims), chunks[0])]
    for (t, nr, mm2, mm3, e) in parts:
        tot.update(t)
        nrows += nr
        m2 = max(m2, mm2)
        m3 = max(m3, mm3)
        for key, (adj, c) in e.items():
            if key in ends:
                ends[key][1] += c
            else:
                ends[key] = [adj, c]
    tally3, kinds3 = classify_end_states(ends, adj0, g0, flat)
    times["triples"] = time.time() - t0
    recorded_all = (nrows == tot["restoring"])
    print(f"(iii) TRIPLES (radius 1): {tot['second']} legal non-undo second switches (max dS2 {m2}, bound {2 * (deg - 1)}); "
          f"{tot['kept']} pairs kept for stage 3; {tot['third']} third switches tried (max dS3 {m3}); "
          f"back to the start {tot['back']}")
    print(f"    RESTORING WRITTEN FORMS THAT LEAVE THE START: {tot['restoring']} (recorded {nrows}; all recorded: "
          f"{recorded_all}), {len(ends)} distinct end states; RENAMINGS {tally3['renaming_forms']} forms / "
          f"{tally3['renaming_states']} states; REAL MOVES {tally3['real_forms']} forms / {tally3['real_states']} states "
          f"(OPENS {tally3['real_OPENS_forms']}, DAMAGES {tally3['real_DAMAGES_forms']}); {times['triples']:.1f} s")
    for k, c in sorted(kinds3.items(), key=str):
        print(f"    {k}: {c}")
    result["triples"] = dict(tally3)
    result["triples"].update({"restoring_leave": int(tot["restoring"]), "back": int(tot["back"]),
                              "second": int(tot["second"]), "kept": int(tot["kept"]), "third": int(tot["third"]),
                              "distinct_end_states": len(ends), "max_ds2": int(m2), "max_ds3": int(m3)})
    result["times_s"] = times
    total = sum(times.values())
    print(f"TIME at N = {n}: {total:.1f} s ({', '.join(f'{k} {v:.1f}' for k, v in times.items())}); "
          f"scaled by N: L = 8 {total * 64 / n:.0f} s, L = 10 {total * 100 / n:.0f} s, L = 12 {total * 144 / n:.0f} s, "
          f"16 x 10 {total * 160 / n:.0f} s")
    return result


def score(result):
    """Rule 14: score the saved counts at the held-out size against HELD_OUT. Counts absent from the tallies are 0
    (a Counter records no zero entries; the first scoring crashed on that and was rescored from the saved JSON)."""
    h = HELD_OUT
    t = result["triples"]
    s1 = result["singles"]
    p2 = result["pairs"]
    got = {
        "singles": s1.get("real_forms", 0) + s1.get("renaming_forms", 0),
        "pairs_real": p2.get("real_forms", 0),
        "pairs_renamings": p2.get("renaming_forms", 0),
        "triples_restoring_leave": t["restoring_leave"],
        "triples_renamings": t.get("renaming_forms", 0),
        "triples_real": t.get("real_forms", 0),
        "triples_real_damages": t.get("real_DAMAGES_forms", 0),
        "triples_real_opens": t.get("real_OPENS_forms", 0),
        "triples_distinct_end_states": t["distinct_end_states"],
    }
    print(f"RULE 14 SCORE at L = {h['L']} (prediction written {h['written']}, from {h['derived_from']}):")
    words = []
    for k, v in got.items():
        lo, hi = h[k]
        w = "HELD" if lo <= v <= hi else "MISSED"
        words.append(w)
        print(f"    {k}: predicted [{lo}, {hi}], got {v}: {w}")
    print(f"  OVERALL: {'HELD' if all(w == 'HELD' for w in words) else 'MISSED'} "
          f"({words.count('HELD')} of {len(words)} counts held)")


if __name__ == "__main__":
    argv = sys.argv[1:]
    nproc = 1
    if "--procs" in argv:
        i = argv.index("--procs")
        nproc = int(argv[i + 1])
        del argv[i:i + 2]
    if "--rescore" in argv:
        # score the saved JSON of the held-out size without rerunning it
        with open(OUT_DIR / f"hard_rule_size_census_{HELD_OUT['L']}x{HELD_OUT['L']}.json") as f:
            score(json.load(f))
        raise SystemExit(0)
    dims = [int(x) for x in argv[0].split(",")] if argv else [6, 6]
    if len(dims) == 1:
        dims = [dims[0], dims[0]]
    held = (HELD_OUT is not None and list(dims) == [HELD_OUT["L"]] * 2)
    if list(dims) == [12, 12] and HELD_OUT is None:
        raise SystemExit("rule 14: L = 12 is the held-out size; write HELD_OUT (with a `date` timestamp) before running it")
    if held:
        print(f"HELD-OUT PREDICTION for L = {HELD_OUT['L']}, written {HELD_OUT['written']} from {HELD_OUT['derived_from']}, "
              f"printed BEFORE the run:")
        for k, v in HELD_OUT.items():
            if isinstance(v, tuple):
                print(f"    {k}: [{v[0]}, {v[1]}]")
        print(f"    formula: {HELD_OUT['formula']}")
    res = survey(dims, nproc)
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    tag = "x".join(str(d) for d in dims)
    with open(OUT_DIR / f"hard_rule_size_census_{tag}.json", "w") as f:
        json.dump(res, f, indent=1, default=int)
    if held:
        score(res)

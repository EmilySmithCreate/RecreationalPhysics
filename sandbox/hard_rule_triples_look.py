"""Sandbox look (exploratory; rule 16), 26 October 2026: triples of switches under the owner's hard rule. Usage:

    python sandbox/hard_rule_triples_look.py [dims, e.g. 6,6,8 or 16,10] [--estimate] [--slice k/m]

`--slice k/m` runs only the first switches whose running index is k mod m (for running m processes side by side; the
totals are summed by hand). The estimate of 26 October, 17:52 ET: stages 1 and 2 take 17 s; stage 3 needs
1,589,468,544 try_switch calls over 197,712 kept pairs, about 800 s in one process at the measured rate of about
2 x 10^6 calls a second, so it is run as eight slices in parallel on a 16-core laptop.

Extends `hard_rule_pairs_look.py` (not modified) from two switches to three. A first switch from point 0 (every legal
one), a second switch whose u's lie within one link of the first's four points, a third whose u's lie within one link
of the eight points of the first two; each graph on the way obeys the hard-core rule (codegree at most 2); the second
is not the first undone (both written forms excluded, as the corrected pairs look does). Kept: sequences whose three
changes in the square count sum to zero AND whose final edge set is not the starting one (compared edge by edge).
For each kept sequence: the change in curl, in anticurl, and dH at lambda = 1.25 (H = 4 anticurl + 4 (lambda - 1)
curl, exact), as the pairs look reports.

Words, declared before the run. The question: can a sequence of three nearby switches move clean space at all under
the hard rule (squares held at exactly 3N for six links)? The expected answer, from the [Swap17] reading of today
(`docs/reading/notes/2026-10-26_constrained_moves_kcm.md`): ZERO restoring triples that leave the start. Any nonzero
count is reported with the first sequences listed. This look can kill the claim "three switches never suffice"; it
cannot crown anything.

Starting state against the owner's rules (TASKS, the O159 section, item 1): the flat 6 x 6 x 8 torus OBEYS the hard
rule (every link carries exactly 4 squares, S = 3N = 864; checked at the start of the run and printed). The rod
4 x 4 x 18 does not (S > 3N) and is not used here. The four-link fallback, the flat 16 x 10 torus, has S = N, the
four-link form of the same rule, and obeys it.

Cost, estimated before running (the pairs look's numbers; D = 3, 6 x 6 x 8, N = 288):
  stage 1: 3,514 legal first switches from point 0 (every switch has a translate with a side-0 point at 0).
  stage 2: the radius-1 ball of 4 points holds at most 28 points, 14 a side; 2 sides x C(14,2) x 36 = about 6,500
           try_switch calls per first, about 2.3 x 10^7 in all: seconds.
  stage 3 (naive): per surviving pair the radius-1 ball of 8 points holds at most 56 points; 2 x C(28,2) x 36 = about
           27,000 try_switch calls per pair; with of order 10^6 to 10^7 pairs that is 10^10 to 10^11 calls, which is
           hours. Pruning on the running change in squares is therefore required.
  the prune (exact): under the hard-core rule every link carries at most deg - 1 squares (for a fixed neighbour a of v
           other than u, u and a share v and at most one other neighbour b, so at most one square per a), so a switch
           gains at most 2 (deg - 1): 10 with six links, 6 with four. A pair whose running change is below -2 (deg - 1)
           cannot be restored by any third switch and is dropped before stage 3. The script measures the true maximum
           gain of a second switch (over all pairs) and of a third switch (over all pairs it tries) and prints both,
           so the bound can be checked against what was seen.
  `--estimate` runs stages 1 and 2 only and prints the stage-3 call count from the surviving pairs' ball sizes, with
           the measured try_switch rate, so the run is sized before it is made. If six links will not finish in about
           12 minutes, the same count is made on the four-link flat 16 x 10 torus and the six-link estimate recorded.
"""
import sys
import time
from collections import Counter
from pathlib import Path

import numpy as np
from numba import njit

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from graphity.cqg_d import _new_edge_ok, _replace, _switch, has_edge, squares_on_edge, torus  # noqa: E402

LAM = 1.25


@njit(cache=True)
def try_switch(adj, u1, v1, u2, v2):
    """As in the pairs look: apply the switch if legal; return (applied, dS). adj unchanged when not applied."""
    if u1 == u2 or v1 == v2 or not has_edge(adj, u1, v1) or not has_edge(adj, u2, v2):
        return False, 0
    if has_edge(adj, u1, v2) or has_edge(adj, u2, v1):
        return False, 0
    lost = squares_on_edge(adj, u1, v1)
    _replace(adj, u1, v1, -1)
    _replace(adj, v1, u1, -1)
    lost += squares_on_edge(adj, u2, v2)
    _replace(adj, u2, v2, -1)
    _replace(adj, v2, u2, -1)
    _replace(adj, u1, -1, v2)
    _replace(adj, v2, -1, u1)
    gained = squares_on_edge(adj, u1, v2)
    _replace(adj, u2, -1, v1)
    _replace(adj, v1, -1, u2)
    gained += squares_on_edge(adj, u2, v1)
    if not (_new_edge_ok(adj, u1, v2) and _new_edge_ok(adj, u2, v1)):
        _switch(adj, u1, v2, u2, v1)
        return False, 0
    return True, gained - lost


@njit(cache=True)
def curl_anti(adj, flat):
    n = adj.shape[0]
    c = 0
    a = 0
    for u in range(n):
        for k in range(adj.shape[1]):
            v = adj[u, k]
            if u < v:
                s = squares_on_edge(adj, u, v)
                if s > flat:
                    c += s - flat
                elif s < flat:
                    a += flat - s
    return c, a


@njit(cache=True)
def same_edges(adj, adj0):
    for u in range(adj.shape[0]):
        for k in range(adj.shape[1]):
            if not has_edge(adj0, u, adj[u, k]):
                return False
    return True


@njit(cache=True)
def ball1(adj, seeds, nseeds, mark, stamp, out):
    """Radius-1 ball of the first nseeds entries of seeds; written to out, count returned."""
    m = 0
    for i in range(nseeds):
        s = seeds[i]
        if mark[s] != stamp:
            mark[s] = stamp
            out[m] = s
            m += 1
        for k in range(adj.shape[1]):
            w = adj[s, k]
            if mark[w] != stamp:
                mark[w] = stamp
                out[m] = w
                m += 1
    return m


@njit(cache=True)
def run_first(adj0, part, f_u1, f_v1, f_u2, f_v2, ds1, gmax, flat, estimate_only,
              mark, stamp, ball, ball2, hist, rows, nrows, e0):
    """Stages 2 and 3 for one first switch (already applied in adj0 is NOT assumed: adj0 is the start graph).

    Returns (n_second_legal, n_pairs_kept, stage3_calls_estimate, n_third_tried, n_restoring, n_back, max_ds2,
    max_ds3, nrows, stamp). hist[ds1 + 16, ds2 + 16] counts second switches by (ds1, ds2).
    """
    deg = adj0.shape[1]
    adj = adj0.copy()
    _switch(adj, f_u1, f_v1, f_u2, f_v2)
    seeds = np.empty(8, dtype=np.int64)
    seeds[0] = f_u1
    seeds[1] = f_v1
    seeds[2] = f_u2
    seeds[3] = f_v2
    stamp += 1
    nb = ball1(adj, seeds, 4, mark, stamp, ball)
    n_second = 0
    n_kept = 0
    est3 = 0
    n_third = 0
    n_rest = 0
    n_back = 0
    max_ds2 = -1000
    max_ds3 = -1000
    for i in range(nb):
        a1 = ball[i]
        for j in range(i + 1, nb):
            a2 = ball[j]
            if part[a1] != part[a2]:
                continue
            for k1 in range(deg):
                b1 = adj[a1, k1]
                for k2 in range(deg):
                    b2 = adj[a2, k2]
                    ok, ds2 = try_switch(adj, a1, b1, a2, b2)
                    if not ok:
                        continue
                    undo = ((a1 == f_u1 and b1 == f_v2 and a2 == f_u2 and b2 == f_v1) or
                            (a1 == f_u2 and b1 == f_v1 and a2 == f_u1 and b2 == f_v2) or
                            (a1 == f_v2 and b1 == f_u1 and a2 == f_v1 and b2 == f_u2) or
                            (a1 == f_v1 and b1 == f_u2 and a2 == f_v2 and b2 == f_u1))
                    if not undo:
                        n_second += 1
                        hist[ds1 + 16, ds2 + 16] += 1
                        if ds2 > max_ds2:
                            max_ds2 = ds2
                        need = -(ds1 + ds2)
                        if need <= gmax:
                            n_kept += 1
                            seeds[4] = a1
                            seeds[5] = b1
                            seeds[6] = a2
                            seeds[7] = b2
                            stamp += 1
                            nb2 = ball1(adj, seeds, 8, mark, stamp, ball2)
                            # count same-side pairs for the estimate
                            n0 = 0
                            for q in range(nb2):
                                if part[ball2[q]] == 0:
                                    n0 += 1
                            n1 = nb2 - n0
                            est3 += (n0 * (n0 - 1) // 2 + n1 * (n1 - 1) // 2) * deg * deg
                            if not estimate_only:
                                for p in range(nb2):
                                    c1 = ball2[p]
                                    for q in range(p + 1, nb2):
                                        c2 = ball2[q]
                                        if part[c1] != part[c2]:
                                            continue
                                        for k3 in range(deg):
                                            d1 = adj[c1, k3]
                                            for k4 in range(deg):
                                                d2 = adj[c2, k4]
                                                ok3, ds3 = try_switch(adj, c1, d1, c2, d2)
                                                if not ok3:
                                                    continue
                                                n_third += 1
                                                if ds3 > max_ds3:
                                                    max_ds3 = ds3
                                                if ds3 == need:
                                                    if same_edges(adj, e0):
                                                        n_back += 1
                                                    else:
                                                        n_rest += 1
                                                        if nrows < rows.shape[0]:
                                                            cc, aa = curl_anti(adj, flat)
                                                            rows[nrows, 0] = f_u1
                                                            rows[nrows, 1] = f_v1
                                                            rows[nrows, 2] = f_u2
                                                            rows[nrows, 3] = f_v2
                                                            rows[nrows, 4] = a1
                                                            rows[nrows, 5] = b1
                                                            rows[nrows, 6] = a2
                                                            rows[nrows, 7] = b2
                                                            rows[nrows, 8] = c1
                                                            rows[nrows, 9] = d1
                                                            rows[nrows, 10] = c2
                                                            rows[nrows, 11] = d2
                                                            rows[nrows, 12] = ds1
                                                            rows[nrows, 13] = ds2
                                                            rows[nrows, 14] = ds3
                                                            rows[nrows, 15] = cc
                                                            rows[nrows, 16] = aa
                                                            nrows += 1
                                                _switch(adj, c1, d2, c2, d1)
                    _switch(adj, a1, b2, a2, b1)
    return n_second, n_kept, est3, n_third, n_rest, n_back, max_ds2, max_ds3, nrows, stamp


def survey(dims, estimate_only, sl=(0, 1)):
    adj0, part = torus(dims)
    adj0 = np.asarray(adj0, dtype=np.int64)
    part = np.asarray(part, dtype=np.int64)
    n, deg = adj0.shape
    flat = deg - 2                      # squares per link in flat space: 4 with six links, 2 with four
    gmax = 2 * (deg - 1)                # exact upper bound on the gain of one switch (docstring)
    c0, a0 = curl_anti(adj0, flat)
    s0 = sum(squares_on_edge(adj0, u, int(v)) for u in range(n) for v in adj0[u] if u < v) // 4
    s_rule = flat * deg * n // 8          # flat squares per link x links / 4: 3N with six links, N with four
    print(f"flat torus {dims}: N = {n}, deg = {deg}, S = {s0} (hard rule: S = {s_rule}), "
          f"curl {c0}, anticurl {a0}; starting state obeys the hard rule: {s0 == s_rule and c0 == 0 and a0 == 0}")
    side = np.flatnonzero(part == part[0])
    mark = np.zeros(n, dtype=np.int64)
    ball = np.empty(n, dtype=np.int64)
    ball2 = np.empty(n, dtype=np.int64)
    hist = np.zeros((33, 33), dtype=np.int64)
    rows = np.zeros((5000, 17), dtype=np.int64)
    stamp = 0
    nrows = 0
    tot = Counter()
    firsts = Counter()
    max_ds2 = max_ds3 = -1000
    t0 = time.time()
    n_first = 0
    for v1 in adj0[0]:
        for u2 in side:
            for v2 in adj0[u2]:
                adj = adj0.copy()
                ok, ds1 = try_switch(adj, 0, int(v1), int(u2), int(v2))
                if not ok:
                    continue
                n_first += 1
                if n_first % sl[1] != sl[0]:
                    continue
                firsts[ds1] += 1
                r = run_first(adj0, part, 0, int(v1), int(u2), int(v2), ds1, gmax, flat, estimate_only,
                              mark, stamp, ball, ball2, hist, rows, nrows, adj0)
                n_second, n_kept, est3, n_third, n_rest, n_back, m2, m3, nrows, stamp = r
                tot["second"] += n_second
                tot["kept"] += n_kept
                tot["est3"] += est3
                tot["third"] += n_third
                tot["restoring"] += n_rest
                tot["back"] += n_back
                max_ds2 = max(max_ds2, m2)
                max_ds3 = max(max_ds3, m3)
    dt = time.time() - t0
    print(f"stage 1: {n_first} legal first switches from point 0, by dS: {dict(sorted(firsts.items()))}")
    print(f"stage 2: {tot['second']} legal non-undo second switches (u's within one link of the first's points); "
          f"max dS2 seen {max_ds2} (bound {gmax})")
    print("  (dS1, dS2) histogram:")
    for i in range(33):
        for j in range(33):
            if hist[i, j]:
                print(f"    dS1 {i - 16:+d}, dS2 {j - 16:+d}: {hist[i, j]}")
    print(f"  pairs kept for stage 3 (running change >= -{gmax}): {tot['kept']}; "
          f"stage-3 try_switch calls needed: {tot['est3']:,}")
    print(f"  wall time so far {dt:.1f} s")
    if estimate_only:
        calls2 = tot["second"]  # legal ones only; the rate below is per legal call, conservative
        rate = max(calls2, 1) / max(dt, 1e-9)
        print(f"  estimate: at {rate:,.0f} legal stage-2 calls per second, stage 3 needs about "
              f"{tot['est3'] / rate:,.0f} s (upper bound on the time: stage-3 candidates mostly fail fast)")
        return
    print(f"stage 3: {tot['third']} legal third switches tried; max dS3 seen {max_ds3} (bound {gmax})")
    print(f"  RESTORING TRIPLES THAT LEAVE THE START: {tot['restoring']}; triples that return the start edge set: "
          f"{tot['back']}")
    kinds = Counter()
    for r in range(nrows):
        cc, aa = int(rows[r, 15]), int(rows[r, 16])
        kinds[(cc - c0, aa - a0, round(4 * (aa - a0) + 4 * (LAM - 1) * (cc - c0), 2))] += 1
    for k, cnt in sorted(kinds.items(), key=lambda kv: kv[0][2])[:25]:
        print(f"    (change in curl, change in anticurl, dH at lambda 1.25) {k}: {cnt} sequences (of those recorded)")
    shown = Counter()
    for r in range(nrows):
        x = rows[r]
        kind = (int(x[15]) - c0, int(x[16]) - a0)
        shown[kind] += 1
        if shown[kind] > 6:
            continue
        print(f"    switches ({x[0]},{x[1]},{x[2]},{x[3]}) ({x[4]},{x[5]},{x[6]},{x[7]}) ({x[8]},{x[9]},{x[10]},{x[11]}) "
              f"dS {x[12]:+d},{x[13]:+d},{x[14]:+d}; curl {x[15]}, anticurl {x[16]}")
    print(f"  wall time {time.time() - t0:.1f} s")


if __name__ == "__main__":
    argv = sys.argv[1:]
    sl = (0, 1)
    if "--slice" in argv:
        i = argv.index("--slice")
        k, m = argv[i + 1].split("/")
        sl = (int(k), int(m))
        del argv[i:i + 2]
    args = [a for a in argv if not a.startswith("--")]
    dims = [int(x) for x in args[0].split(",")] if args else [6, 6, 8]
    survey(dims, "--estimate" in argv, sl)

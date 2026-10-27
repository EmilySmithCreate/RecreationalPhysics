"""Sandbox look (exploratory; rule 16), 26 October 2026: four switches under the owner's hard rule. Usage:

CORRECTED 27 October 2026 (ASSUMPTIONS O163, the fifth Codex audit, F11 and F14; two defects of the 26 October version,
both the assistant's). (1) The stage-2 prune kept a pair of switches only if dS1 + dS2 >= -gmax (gmax = 10, the exact
bound on ONE switch's gain), copied from the triples look, where one switch remained. Here two remain, so the exact
bound is 2 gmax = 20, and the 26 October counts (restricted mode: FOUND 9,216, all transpositions, "ZERO REAL MOVES
within the restricted word") searched only the pairs with dS1 + dS2 >= -10, about 4 % of the legal pairs in the
radius-1 ball (a scratch count over 60 first switches: 4,925 kept, 126,476 discarded with need3 in 11..20, none beyond
20); a legal sequence in the discarded region exists (6 x 6 x 8: (0,48,2,50), (1,49,3,51), (0,50,2,48), (1,51,3,49),
dS -6, -5, +5, +6, back to the start). So those counts are NOT a complete count of the restricted word and certify no
ZERO; they stand as counts of the pairs they searched. The stage-2 bound is now 2 gmax for the four-switch stages
(`--estimate`, `--full`, `--restricted`); the stage-3 bound (one switch left) stays gmax; the triples look is untouched.
(2) Part 1 (iii) lifted the 16 x 10 seam move into the 8 x 8 x 8 torus with `idx`, which has no range check, so rows
y = 8 and 9 were silently mapped to (x + 1, y - 8): the printed "-6, -7, -4, total -17" is for a sequence that is not
the lifted move. The lift now goes into the 16 x 10 x 8 torus, which holds every 2D coordinate. The window searches
(i), (ii), (iv) did not use the lift and are unchanged.

    python sandbox/hard_rule_quads_look.py --seam                     # part 1: the seam move by hand, 2D then 3D liftings
    python sandbox/hard_rule_quads_look.py --estimate --slice k/m     # part 2: stages 1-3, count what stage 4 would cost
    python sandbox/hard_rule_quads_look.py --full --slice k/m [--prune 8]        # stage 4 over the radius-1 ball of 12
    python sandbox/hard_rule_quads_look.py --restricted --slice k/m [--prune 8]  # stage 4, every u within one link of the FIRST
    python sandbox/hard_rule_quads_look.py --sum sandbox/out/hard_rule_quads/full   # add up the slices' JSON lines
    ... --restricted --slice k/12 --rows <file.npy>   # also save every recorded FOUND row (the 22-column rows: 16 switch ends, 4 dS, curl, anticurl), 2,000 at most per slice

Extends `hard_rule_triples_look.py` (not modified; its 26 October run: 0 restoring triples out of the flat 6 x 6 x 8 torus,
715,453,184 third switches tried in 8 slices of about 280 s, max gain seen +2 for a second and +8 for a third switch,
exact bound 2(deg - 1) = 10) from three switches to four.

THE QUESTION, declared before any run: can four nearby switches move clean six-link space under the hard rule, the square
count held at exactly 3N? The words: ZERO (no sequence of four switches, each legal under the hard-core rule, with the four
changes in S summing to zero and a final edge set that is not the start's), or FOUND, with the sequences listed, their
change in curl and anticurl and dH at lambda = 1.25 (H = 4 anticurl + 4 (lambda - 1) curl, exact).

THE OWNER'S EXPECTATION, recorded 26 October 22:37 UTC: she agrees with Fable's hypothesis that the cheapest move out of
clean space is a four-switch seam move, the three-direction cousin of the two-direction three-switch seam move (LOG,
26 October: three parallel switches across one seam of the flat 16 x 10 torus that turn six seam links into six chords,
S kept at N, curl +4, anticurl +4, dH 20 at lambda 1.25), and that ZERO at four switches means the hard rule forbids any
local opening of clean space. This look can kill that hypothesis (ZERO in the exhaustive count kills "a four-switch seam
move exists"; a FOUND in part 1 kills "zero at four") and cannot crown anything.

RULE OBEDIENCE: the flat 6 x 6 x 8 torus obeys the hard rule (every link carries exactly 4 squares, S = 3N = 864, curl 0,
anticurl 0; checked and printed at the start). The flat 8 x 8 x 8 torus (S = 3N = 1536) obeys it too and is used where the
two-direction move's row span (rows r and 7 - r) needs eight rows in a plane. The four-link flat 16 x 10 torus (S = N) is
the two-direction control.

PART 1, constructive (minutes). A "seam" is the sheet of links between the planes x = a and x = a + 1; a seam switch pairs
two seam links: when their x = a ends lie on the same side of the bipartition the switch turns them into two chords
across the seam; when they lie on opposite sides it pairs the x = a end of one with the x = a + 1 end of the other and
makes one chord along each side of the seam (rows of opposite parity, the "r and 7 - r" of the LOG).
(i) On the four-link 16 x 10 torus, every ordered sequence of up to three seam switches (no immediate undo, pruned exactly
on the running change in S) is listed: the two-direction seam move should reappear, which fixes its geometry from the code
rather than from memory. (ii) On the six-link 8 x 8 x 8 torus, the same search over seam switches within a window of
seam links (all 8 rows y, planes z in {0, 1}) up to depth 4: this covers the two-direction move lifted into one plane
(three switches), every four-switch seam move inside the window, and their mixtures across two planes. (iii) The
two-direction move applied explicitly in one plane and in two parallel planes (six switches) of the 8 x 8 x 8 torus, with
the change in S at each step, the final S against 3N, curl, anticurl, dH and whether the start is returned. (iv) The same
window search on the 6 x 6 x 8 torus (rows y all 6, z in {0, 1, 2}), depth 4. Each candidate is reported exactly.

PART 2, exhaustive, estimate first. The triples look's stages 1 to 3, then a fourth switch whose u's lie within one link
of the twelve points of the first three, pruned on the running change after three switches: dS1 + dS2 + dS3 >= -10 (the
exact bound; a switch gains at most 2(deg - 1)) and, reported separately as a tighter prune on a seen number, >= -8 (the
largest third-switch gain seen on 26 October). After two switches the prune is dS1 + dS2 >= -20 (corrected 27 October;
two switches remain). `--estimate` counts the triples that survive each prune and the fourth-stage
try_switch calls they imply (same-side pairs of the radius-1 ball of 12 points, times 36; and the same for the restricted
ball of the FIRST switch's four points), with the measured rate.

COST, estimated before running. Stages 1 to 3 cost what the triples look cost: about 1.6 x 10^9 trials, 8 slices of about
280 s, so the estimate itself is a 5-minute job on 12 cores. For stage 4: the kept pairs were 2.4 % of the legal second
switches; if a similar share of the 7.2 x 10^8 third switches survives the -10 prune, that is of order 10^7 triples, each
with a ball of 12 seeds holding up to 84 points (42 a side) and so up to 2 x C(42,2) x 36 = 62,000 calls: of order 10^12
calls, days on 12 cores. The restricted count (every u within one link of the first switch's four points: at most 28 points,
14 a side, 2 x C(14,2) x 36 = 6,552 calls a stage) is about ten times cheaper per triple and smaller in triples, since its
stage 3 is restricted too. Whether either is bought is decided from the measured estimate, not from this paragraph.

RESTRICTION, as a limit on the words: if only the restricted count runs, ZERO there means "no four-switch sequence with
every switch's u's within one link of the first switch's four points", not "no four-switch sequence within one link of the
previous switches' points"; a seam move whose four switches all touch the first's neighbourhood is covered, one that walks
away is not.
"""
import glob
import json
import os
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
    """As in the triples look: apply the switch if legal; return (applied, dS). adj unchanged when not applied."""
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
def total_squares(adj):
    n = adj.shape[0]
    t = 0
    for u in range(n):
        for k in range(adj.shape[1]):
            v = adj[u, k]
            if u < v:
                t += squares_on_edge(adj, u, v)
    return t // 4


@njit(cache=True)
def same_edges(adj, adj0):
    for u in range(adj.shape[0]):
        for k in range(adj.shape[1]):
            if not has_edge(adj0, u, adj[u, k]):
                return False
    return True


@njit(cache=True)
def ball1(adj, seeds, nseeds, mark, stamp, out):
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
def side_pairs(part, ball, nb):
    n0 = 0
    for q in range(nb):
        if part[ball[q]] == 0:
            n0 += 1
    n1 = nb - n0
    return n0 * (n0 - 1) // 2 + n1 * (n1 - 1) // 2


# ----------------------------------------------------------------------------------------------------------------------
# Part 2: the exhaustive stages
# ----------------------------------------------------------------------------------------------------------------------

@njit(cache=True)
def run_first_q(adj0, part, f_u1, f_v1, f_u2, f_v2, ds1, gmax, gmax2, prune4, flat, mode,
                mark, stamp, ball, ball2, ball3, rows, nrows, e0, out):
    """Stages 2 to 4 for one first switch. mode 0: estimate (stages 2, 3; stage-4 cost counted); mode 1: full stage 4
    over the ball of the twelve points; mode 2: restricted (stages 3 and 4 over the ball of the FIRST switch's points).

    out counters: 0 second, 1 kept pairs, 2 third tried, 3 restoring triples (leave start), 4 back triples,
    5 surviving triples (need4 <= gmax), 6 surviving triples (need4 <= 8), 7 est4 full calls (<= gmax),
    8 est4 full calls (<= 8), 9 est4 restricted calls (<= gmax), 10 est4 restricted calls (<= 8), 11 fourth tried,
    12 FOUND quads, 13 back quads, 14 max ds2, 15 max ds3, 16 max ds4.
    """
    deg = adj0.shape[1]
    adj = adj0.copy()
    _switch(adj, f_u1, f_v1, f_u2, f_v2)
    seeds = np.empty(12, dtype=np.int64)
    seeds[0] = f_u1
    seeds[1] = f_v1
    seeds[2] = f_u2
    seeds[3] = f_v2
    stamp += 1
    nb = ball1(adj, seeds, 4, mark, stamp, ball)
    pairs_restr = side_pairs(part, ball, nb)
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
                        out[0] += 1
                        if ds2 > out[14]:
                            out[14] = ds2
                        need3 = -(ds1 + ds2)
                        if need3 <= gmax2:
                            out[1] += 1
                            seeds[4] = a1
                            seeds[5] = b1
                            seeds[6] = a2
                            seeds[7] = b2
                            if mode == 2:
                                cand = ball
                                nc = nb
                            else:
                                stamp += 1
                                nc = ball1(adj, seeds, 8, mark, stamp, ball2)
                                cand = ball2
                            for p in range(nc):
                                c1 = cand[p]
                                for q in range(p + 1, nc):
                                    c2 = cand[q]
                                    if part[c1] != part[c2]:
                                        continue
                                    for k3 in range(deg):
                                        d1 = adj[c1, k3]
                                        for k4 in range(deg):
                                            d2 = adj[c2, k4]
                                            ok3, ds3 = try_switch(adj, c1, d1, c2, d2)
                                            if not ok3:
                                                continue
                                            out[2] += 1
                                            if ds3 > out[15]:
                                                out[15] = ds3
                                            if ds3 == need3:
                                                if same_edges(adj, e0):
                                                    out[4] += 1
                                                else:
                                                    out[3] += 1
                                            need4 = need3 - ds3
                                            if need4 <= gmax:
                                                out[5] += 1
                                                if need4 <= 8:
                                                    out[6] += 1
                                                seeds[8] = c1
                                                seeds[9] = d1
                                                seeds[10] = c2
                                                seeds[11] = d2
                                                if mode == 0:
                                                    stamp += 1
                                                    nb3 = ball1(adj, seeds, 12, mark, stamp, ball3)
                                                    pf = side_pairs(part, ball3, nb3) * deg * deg
                                                    pr = pairs_restr * deg * deg
                                                    out[7] += pf
                                                    out[9] += pr
                                                    if need4 <= 8:
                                                        out[8] += pf
                                                        out[10] += pr
                                                elif need4 <= prune4:
                                                    if mode == 2:
                                                        cand4 = ball
                                                        nc4 = nb
                                                    else:
                                                        stamp += 1
                                                        nc4 = ball1(adj, seeds, 12, mark, stamp, ball3)
                                                        cand4 = ball3
                                                    for p4 in range(nc4):
                                                        g1 = cand4[p4]
                                                        for q4 in range(p4 + 1, nc4):
                                                            g2 = cand4[q4]
                                                            if part[g1] != part[g2]:
                                                                continue
                                                            for k5 in range(deg):
                                                                h1 = adj[g1, k5]
                                                                for k6 in range(deg):
                                                                    h2 = adj[g2, k6]
                                                                    ok4, ds4 = try_switch(adj, g1, h1, g2, h2)
                                                                    if not ok4:
                                                                        continue
                                                                    out[11] += 1
                                                                    if ds4 > out[16]:
                                                                        out[16] = ds4
                                                                    if ds4 == need4:
                                                                        if same_edges(adj, e0):
                                                                            out[13] += 1
                                                                        else:
                                                                            out[12] += 1
                                                                            if nrows < rows.shape[0]:
                                                                                cc, aa = curl_anti(adj, flat)
                                                                                r = rows[nrows]
                                                                                r[0] = f_u1; r[1] = f_v1; r[2] = f_u2; r[3] = f_v2
                                                                                r[4] = a1; r[5] = b1; r[6] = a2; r[7] = b2
                                                                                r[8] = c1; r[9] = d1; r[10] = c2; r[11] = d2
                                                                                r[12] = g1; r[13] = h1; r[14] = g2; r[15] = h2
                                                                                r[16] = ds1; r[17] = ds2; r[18] = ds3; r[19] = ds4
                                                                                r[20] = cc; r[21] = aa
                                                                                nrows += 1
                                                                    _switch(adj, g1, h2, g2, h1)
                                            _switch(adj, c1, d2, c2, d1)
                    _switch(adj, a1, b2, a2, b1)
    return nrows, stamp


KEYS = ["second", "kept_pairs", "third", "restoring_triples", "back_triples", "surv3_10", "surv3_8",
        "est4_full_10", "est4_full_8", "est4_restr_10", "est4_restr_8", "fourth", "FOUND", "back_quads",
        "max_ds2", "max_ds3", "max_ds4"]


def exhaustive(dims, mode, sl, prune4, rows_path=None):
    adj0, part = torus(dims)
    adj0 = np.asarray(adj0, dtype=np.int64)
    part = np.asarray(part, dtype=np.int64)
    n, deg = adj0.shape
    flat = deg - 2
    gmax = 2 * (deg - 1)
    c0, a0 = curl_anti(adj0, flat)
    s0 = int(total_squares(adj0))
    s_rule = flat * deg * n // 8
    print(f"flat torus {dims}: N = {n}, deg = {deg}, S = {s0} (hard rule: S = {s_rule}), curl {c0}, anticurl {a0}; "
          f"starting state obeys the hard rule: {s0 == s_rule and c0 == 0 and a0 == 0}")
    print(f"mode {['estimate', 'full', 'restricted'][mode]}, slice {sl[0]}/{sl[1]}, stage-4 prune need4 <= {prune4} "
          f"(exact bound {gmax})")
    side = np.flatnonzero(part == part[0])
    mark = np.zeros(n, dtype=np.int64)
    ball = np.empty(n, dtype=np.int64)
    ball2 = np.empty(n, dtype=np.int64)
    ball3 = np.empty(n, dtype=np.int64)
    rows = np.zeros((2000, 22), dtype=np.int64)
    out = np.zeros(17, dtype=np.int64)
    out[14] = out[15] = out[16] = -1000
    stamp = 0
    nrows = 0
    firsts = Counter()
    t0 = time.time()
    n_first = 0
    n_mine = 0
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
                n_mine += 1
                firsts[ds1] += 1
                nrows, stamp = run_first_q(adj0, part, 0, int(v1), int(u2), int(v2), ds1, gmax, 2 * gmax, prune4, flat, mode,
                                           mark, stamp, ball, ball2, ball3, rows, nrows, adj0, out)
    dt = time.time() - t0
    res = {k: int(out[i]) for i, k in enumerate(KEYS)}
    res.update(first=n_first, first_in_slice=n_mine, wall_s=round(dt, 1), mode=mode, prune4=prune4, dims=list(dims))
    print(f"stage 1: {n_first} legal first switches from point 0 ({n_mine} in this slice), by dS: "
          f"{dict(sorted(firsts.items()))}")
    print(f"stage 2: {res['second']} legal non-undo second switches; max dS2 {res['max_ds2']} (bound {gmax}); "
          f"pairs kept {res['kept_pairs']} (dS1 + dS2 >= -{2 * gmax}, two switches left; corrected 27 October)")
    print(f"stage 3: {res['third']} third switches tried; max dS3 {res['max_ds3']}; restoring triples that leave the "
          f"start {res['restoring_triples']}; back {res['back_triples']}")
    print(f"  triples surviving for stage 4: {res['surv3_10']} (need4 <= {gmax}), {res['surv3_8']} (need4 <= 8)")
    if mode == 0:
        rate = max(res["third"], 1) / max(dt, 1e-9)
        print(f"  stage-4 calls implied, full ball of 12: {res['est4_full_10']:,} (<= {gmax}), "
              f"{res['est4_full_8']:,} (<= 8); restricted ball of the first's 4 points: {res['est4_restr_10']:,}, "
              f"{res['est4_restr_8']:,}")
        print(f"  measured rate this slice {rate:,.0f} legal third-switch trials/s over {dt:.0f} s "
              f"(upper bound on stage-4 time: candidates mostly fail before being counted)")
    else:
        print(f"stage 4: {res['fourth']} fourth switches tried; max dS4 {res['max_ds4']}")
        print(f"  FOUND QUADS THAT LEAVE THE START: {res['FOUND']}; quads that return the start edge set: "
              f"{res['back_quads']}")
        kinds = Counter()
        for r in range(nrows):
            cc, aa = int(rows[r, 20]), int(rows[r, 21])
            kinds[(cc - c0, aa - a0, round(4 * (aa - a0) + 4 * (LAM - 1) * (cc - c0), 2))] += 1
        for k, cnt in sorted(kinds.items(), key=lambda kv: kv[0][2])[:25]:
            print(f"    (change in curl, change in anticurl, dH at lambda 1.25) {k}: {cnt} sequences (of those recorded)")
        shown = Counter()
        for r in range(nrows):
            x = [int(t) for t in rows[r]]
            kind = (x[20] - c0, x[21] - a0)
            shown[kind] += 1
            if shown[kind] > 6:
                continue
            print(f"SEQ switches ({x[0]},{x[1]},{x[2]},{x[3]}) ({x[4]},{x[5]},{x[6]},{x[7]}) ({x[8]},{x[9]},{x[10]},{x[11]}) "
                  f"({x[12]},{x[13]},{x[14]},{x[15]}) dS {x[16]:+d},{x[17]:+d},{x[18]:+d},{x[19]:+d}; "
                  f"curl {x[20]}, anticurl {x[21]}")
    print(f"  wall time {dt:.1f} s")
    if rows_path is not None:
        np.save(rows_path, rows[:nrows])
        print(f"rows saved: {nrows} of {res['FOUND']} FOUND forms to {rows_path}")
    print("JSON " + json.dumps(res))


def sum_slices(folder):
    tot = Counter()
    seqs = []
    files = sorted(glob.glob(os.path.join(folder, "slice_*.txt")))
    done = 0
    for f in files:
        txt = open(f, encoding="utf-8", errors="replace").read().splitlines()
        js = [l for l in txt if l.startswith("JSON ")]
        if not js:
            print(f"{f}: not finished")
            continue
        done += 1
        res = json.loads(js[-1][5:])
        for k in KEYS:
            if k.startswith("max_"):
                tot[k] = max(tot.get(k, -1000), res[k])
            else:
                tot[k] += res[k]
        tot["first_in_slice"] += res["first_in_slice"]
        tot["wall_s"] += res["wall_s"]
        seqs += [l for l in txt if l.startswith("SEQ ")]
    print(f"{done} of {len(files)} slices finished")
    for k in KEYS + ["first_in_slice", "wall_s"]:
        print(f"  {k}: {tot[k]:,}")
    for s in seqs[:40]:
        print("  " + s)


# ----------------------------------------------------------------------------------------------------------------------
# Part 1: the seam move by hand
# ----------------------------------------------------------------------------------------------------------------------

def idx(coords, dims):
    strides = [int(np.prod(dims[a + 1:])) for a in range(len(dims))]
    return int(sum(c * s for c, s in zip(coords, strides)))


def coords_of(i, dims):
    return tuple(int(x) for x in np.unravel_index(i, dims))


def report_sequence(adj0, part, dims, seq, label):
    """Apply the switches in seq (as (u1, v1, u2, v2) point indices) in order; print each step exactly."""
    adj = adj0.copy()
    deg = adj.shape[1]
    flat = deg - 2
    s_rule = flat * deg * adj.shape[0] // 8
    c0, a0 = curl_anti(adj0, flat)
    steps = []
    for (u1, v1, u2, v2) in seq:
        ok, ds = try_switch(adj, u1, v1, u2, v2)
        steps.append(ds if ok else None)
        if not ok:
            print(f"  {label}: switch ({coords_of(u1, dims)},{coords_of(v1, dims)})x({coords_of(u2, dims)},"
                  f"{coords_of(v2, dims)}) is ILLEGAL at step {len(steps)} (edge missing, chord present, or hard-core)")
            return None
    s = int(total_squares(adj))
    c, a = curl_anti(adj, flat)
    back = same_edges(adj, adj0)
    dH = 4 * (a - a0) + 4 * (LAM - 1) * (c - c0)
    print(f"  {label}: legal at every step; dS per step {steps}; final S = {s} against rule {s_rule} "
          f"({'kept' if s == s_rule else 'NOT kept'}); curl {c - c0:+d}, anticurl {a - a0:+d}, dH(1.25) {dH:+.1f}; "
          f"returns the start: {back}")
    return steps, s, c - c0, a - a0, back


def seam_dfs(dims, a, window, maxdepth, label):
    """Ordered sequences of seam switches across the seam x = a | x = a + 1, over the seam links in `window` (a list of
    coordinate tuples for the x = a ends), no immediate undo, pruned on the running dS >= -gmax x (switches left)."""
    adj0, part = torus(dims)
    adj0 = np.asarray(adj0, dtype=np.int64)
    part = np.asarray(part, dtype=np.int64)
    n, deg = adj0.shape
    flat = deg - 2
    gmax = 2 * (deg - 1)
    s_rule = flat * deg * n // 8
    c0, a0 = curl_anti(adj0, flat)
    print(f"\n{label}: torus {dims}, seam x = {a} | {a + 1}, {len(window)} seam links in the window, depth <= {maxdepth}; "
          f"start S = {int(total_squares(adj0))} (rule {s_rule}), obeys the rule: "
          f"{int(total_squares(adj0)) == s_rule and c0 == 0 and a0 == 0}")
    links = []
    for w in window:
        p = idx(w, dims)
        q = idx((w[0] + 1,) + tuple(w[1:]), dims)
        links.append((p, q))
    cands = []
    for i in range(len(links)):
        for j in range(i + 1, len(links)):
            (p1, q1), (p2, q2) = links[i], links[j]
            if part[p1] == part[p2]:
                cands.append((p1, q1, p2, q2))      # same ends paired: chords across the seam
            else:
                cands.append((p1, q1, q2, p2))      # opposite ends paired: chords along each side of the seam
    print(f"  {len(cands)} seam switches (same-side pairs of seam links)")
    found = []
    counts = Counter()
    adj = adj0.copy()
    t0 = time.time()

    def rec(depth, running, seq, last):
        for c in cands:
            if last is not None and c == last:
                continue  # the same pair again would undo it
            ok, ds = try_switch(adj, *c)
            if not ok:
                continue
            counts[depth] += 1
            r = running + ds
            if r == 0 and not same_edges(adj, adj0):
                cc, aa = curl_anti(adj, flat)
                found.append((tuple(seq + [c]), None, cc - c0, aa - a0))
                found_ds.append(list(ds_stack + [ds]))
            if depth < maxdepth and r >= -gmax * (maxdepth - depth):
                ds_stack.append(ds)
                rec(depth + 1, r, seq + [c], c)
                ds_stack.pop()
            _switch(adj, c[0], c[3], c[2], c[1])


    ds_stack = []
    found_ds = []
    rec(1, 0, [], None)
    print(f"  legal switches tried by depth: {dict(sorted(counts.items()))}; {time.time() - t0:.1f} s")
    print(f"  count-keeping sequences that leave the start (written forms, ordered): {len(found)}")
    kinds = Counter()
    bylen = Counter()
    for (seq, _, dc, da), dss in zip(found, found_ds):
        kinds[(len(seq), dc, da, round(4 * da + 4 * (LAM - 1) * dc, 2))] += 1
        bylen[len(seq)] += 1
    print(f"  by number of switches: {dict(sorted(bylen.items()))}")
    for k, cnt in sorted(kinds.items()):
        print(f"    (switches, change in curl, change in anticurl, dH at lambda 1.25) {k}: {cnt} written forms")
    shown = Counter()
    for (seq, _, dc, da), dss in zip(found, found_ds):
        key = (len(seq), dc, da)
        shown[key] += 1
        if shown[key] > 2:
            continue
        pretty = " ".join(f"[{coords_of(u1, dims)}-{coords_of(v1, dims)} x {coords_of(u2, dims)}-{coords_of(v2, dims)}]"
                          for (u1, v1, u2, v2) in seq)
        print(f"    example: {pretty}; dS per step {dss}")
    return found


def part1():
    # (i) the two-direction move, from the code
    found2d = seam_dfs((16, 10), 0, [(0, y) for y in range(10)], 3, "(i) four links, 16 x 10, all 10 rows")
    # (ii) the six-link 8 x 8 x 8 window: all 8 rows, planes z in {0, 1}
    seam_dfs((8, 8, 8), 0, [(0, y, z) for y in range(8) for z in (0, 1)], 4,
             "(ii) six links, 8 x 8 x 8, rows y all 8, planes z in {0, 1}")
    # (iii) the two-direction move lifted explicitly, into a torus that holds every 16 x 10 coordinate (corrected 27 October)
    dims3 = (16, 10, 8)
    adj3, part3 = torus(dims3)
    adj3 = np.asarray(adj3, dtype=np.int64)
    part3 = np.asarray(part3, dtype=np.int64)
    print("\n(iii) the two-direction seam move lifted into the 16 x 10 x 8 torus (corrected 27 October; the 26 October run lifted\n"
          "      into 8 x 8 x 8 with rows 8 and 9 silently aliased, O163 F14)")
    done = set()
    for (seq, _, dc, da) in found2d:
        if len(seq) != 3 or (dc, da) == (0, 0):
            continue
        rows_used = tuple(sorted(coords_of(u1, (16, 10))[1] for (u1, v1, u2, v2) in seq for _ in (0,)))
        key = tuple(sorted((coords_of(u1, (16, 10))[1], coords_of(u2, (16, 10))[1]) for (u1, v1, u2, v2) in seq))
        if key in done:
            continue
        done.add(key)
        if len(done) > 3:
            break
        print(f"  2D move with row pairs {key} (curl {dc:+d}, anticurl {da:+d}):")
        for planes in ([0], [0, 1], [0, 2], [0, 4]):
            lifted = []
            for z in planes:
                for (u1, v1, u2, v2) in seq:
                    cu1, cv1, cu2, cv2 = (coords_of(t, (16, 10)) for t in (u1, v1, u2, v2))
                    lifted.append((idx((cu1[0], cu1[1], z), dims3), idx((cv1[0], cv1[1], z), dims3),
                                   idx((cu2[0], cu2[1], z), dims3), idx((cv2[0], cv2[1], z), dims3)))
            report_sequence(adj3, part3, dims3, lifted, f"planes z = {planes} ({len(lifted)} switches)")
    # (iv) the 6 x 6 x 8 window: all 6 rows, z in {0, 1, 2}
    seam_dfs((6, 6, 8), 0, [(0, y, z) for y in range(6) for z in (0, 1, 2)], 4,
             "(iv) six links, 6 x 6 x 8, rows y all 6, planes z in {0, 1, 2}")


if __name__ == "__main__":
    argv = sys.argv[1:]
    if "--sum" in argv:
        sum_slices(argv[argv.index("--sum") + 1])
        sys.exit(0)
    if "--seam" in argv:
        part1()
        sys.exit(0)
    sl = (0, 1)
    if "--slice" in argv:
        i = argv.index("--slice")
        k, m = argv[i + 1].split("/")
        sl = (int(k), int(m))
    prune4 = 10
    if "--prune" in argv:
        prune4 = int(argv[argv.index("--prune") + 1])
    mode = 0 if "--estimate" in argv else (2 if "--restricted" in argv else 1)
    rows_path = argv[argv.index("--rows") + 1] if "--rows" in argv else None
    args = [a for a in argv if not a.startswith("--") and not a.replace("/", "").isdigit() and a != rows_path]
    dims = [int(x) for x in args[0].split(",")] if args else [6, 6, 8]
    exhaustive(dims, mode, sl, prune4, rows_path)

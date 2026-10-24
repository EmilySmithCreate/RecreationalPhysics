"""Sandbox look, 20 October 2026: when a linked pair of points is added in one place in the toy's flat two-direction
space, does it leave a curl and an uncurl behind (the owner's idea of the same day: adding space makes one curl knot and
one uncurl knot, which merge at once when cold and stay apart only when hot)?

The insertion is the one of sandbox/pair_insertion_2d.py (cut three links, add two linked points, one of each kind, joined
to the cut ends). For every valid choice within R steps of one point of a flat L x L torus it is read exactly: the
surplus X = sum over links of max(0, S_e - 2) (curl: links on more than two squares), the deficit D = sum over links of
max(0, 2 - S_e) (missing squares), and the energy added at lambda = 1.25, H = 4 D + 4 (lambda - 1) X (Q1 written link by link).
Reported: how many valid insertions leave curl only, missing squares only, or both, and the cheapest of each. Exact for
what it tries; a look, not a result.
"""
import itertools
import sys
from collections import Counter

import numpy as np

sys.path.insert(0, "src")
from graphity.cqg import NO_CAP, hamiltonian, is_valid, torus  # noqa: E402
from graphity.row_growth import edge_census  # noqa: E402
from graphity.cqg import surplus  # noqa: E402

LAM = 1.25


def insert_pair(adj, part, links):
    n = adj.shape[0]
    a = [p if part[p] == 0 else q for p, q in links]     # kind 0 ends
    b = [q if part[p] == 0 else p for p, q in links]     # kind 1 ends
    if len(set(a)) < 3 or len(set(b)) < 3:
        return None
    nb = [set(int(x) for x in adj[i]) for i in range(n)] + [set(), set()]
    u, v = n, n + 1                                     # u kind 0 (joins b's), v kind 1 (joins a's)
    for ai, bi in zip(a, b):
        if bi not in nb[ai]:
            return None
        nb[ai].discard(bi); nb[bi].discard(ai)
    for bi in b:
        nb[u].add(bi); nb[bi].add(u)
    for ai in a:
        nb[v].add(ai); nb[ai].add(v)
    nb[u].add(v); nb[v].add(u)
    if any(len(s) != 4 for s in nb):
        return None
    new = np.array([sorted(s) for s in nb], dtype=np.int64)
    return new, np.concatenate([part, [0, 1]])

for L, R in ((10, 2), (10, 3), (12, 4)):
    adj, part = torus(L, cap=NO_CAP)
    h0 = hamiltonian(adj, LAM)
    dist = {0: 0}
    frontier = [0]
    for step in range(1, R + 1):
        nxt = []
        for p in frontier:
            for q in adj[p]:
                q = int(q)
                if q not in dist:
                    dist[q] = step
                    nxt.append(q)
        frontier = nxt
    near = sorted({tuple(sorted((p, int(q)))) for p in dist for q in adj[p] if int(q) in dist})
    kinds = Counter()
    best = {}
    for links in itertools.combinations(near, 3):
        out = insert_pair(adj, part, links)
        if out is None:
            continue
        new, _ = out
        if not is_valid(new, NO_CAP):
            continue
        d, _, _ = edge_census(new)
        x = int(surplus(new))
        dh = hamiltonian(new, LAM) - h0
        assert abs(dh - (4 * d + 4 * (LAM - 1) * x)) < 1e-9
        kind = "both" if d and x else ("missing only" if d else ("curl only" if x else "flat"))
        kinds[kind] += 1
        if kind not in best or dh < best[kind][0]:
            best[kind] = (dh, int(d), x)
    print("L = %d, R = %d: %s; cheapest per kind (energy, missing D, curl X): %s"
          % (L, R, dict(kinds), {k: best[k] for k in sorted(best)}))

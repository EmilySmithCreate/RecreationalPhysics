"""Sandbox look, 20 October 2026: can points be added to the toy's flat two-direction space in one small place without
leaving flaws? (The owner's growth rule of the same night: add points only where the surrounding links are flat or short
a square, never next to curled ones.)

The smallest addition that keeps every point on four links and the two kinds equal is a linked pair, one point of each
kind: remove three links (a_i, b_i), a_i of one kind and b_i of the other, add new points u (kind of the a's) and v (kind
of the b's), link u to the three b's, v to the three a's, and u to v. That is the pair compaction of 18 October run
backwards, in two directions. Every choice of three links with both ends within R steps of one point of a flat L x L torus is tried
exhaustively; reported: how many choices give a valid graph (simple, hard-core rule), the least energy added at
lambda = 1.25, and how many points then sit at a local dimension other than 2. Exact for what it tries; a look.
"""
import itertools
import sys

import numpy as np

sys.path.insert(0, "src")
from graphity.cqg import NO_CAP, hamiltonian, is_valid, torus  # noqa: E402
from graphity.dimension import local_dimension  # noqa: E402

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
    centre = 0
    # links within R steps of the centre point
    dist = {centre: 0}
    frontier = [centre]
    for step in range(1, R + 1):
        nxt = []
        for p in frontier:
            for q in adj[p]:
                q = int(q)
                if q not in dist:
                    dist[q] = step; nxt.append(q)
        frontier = nxt
    near = sorted({tuple(sorted((p, int(q)))) for p in dist for q in adj[p] if int(q) in dist})
    n_try = n_valid = n_struct = 0
    best = None
    for links in itertools.combinations(near, 3):
        n_try += 1
        out = insert_pair(adj, part, links)
        if out is None:
            continue
        new, newpart = out
        n_struct += 1
        if not is_valid(new, NO_CAP):
            continue
        n_valid += 1
        dh = hamiltonian(new, LAM) - h0
        off = int((local_dimension(new) != 2).sum())
        if best is None or (dh, off) < best[:2]:
            best = (dh, off, links)
    print(f"L = {L}, R = {R}: {len(near)} links, {n_try} choices of three, {n_struct} simple and four-linked, {n_valid} valid; "
          f"least energy added {best[0] if best else None}, with {best[1] if best else None} points not at d = 2")

"""Step 1, part b (sandbox lane): the first run of regge_step1_stiffness.py at L = 6 found, against the prediction written
in its header, a single-link response dH = 12 delta^2 / (1 + delta) (even, quadratic to leading order) and a mixed term
of -4 delta^2 for the two collinear and four side-by-side parallel neighbours, 0 for perpendicular links and for parallel
links two or more steps away. Row sum 24 - 6 x 4 = 0: the stiffness looks like 4 x (the cubic-lattice Laplacian acting
on each axis family of links separately), gapless, with the uniform scaling as its zero mode.

WRITTEN BEFORE COMPUTING (ours, revised): (a) the mixed term is -4 delta^2 (to the 1/(1 + delta) factor) at every
parallel offset of one step and 0 at every other offset within three steps, in every direction; (b) scaling every
length by the same factor leaves H_curv exactly 0 (kappa is scale-free); (c) the same numbers at L = 8, since the
coupling has range one; (d) a perturbation along one axis never changes the lengths' energy through links of another
axis (M = 0 for every perpendicular pair). If (a) to (d) hold, the stiffness is K = 4 (6 I - A) per family, A the
cubic adjacency of link positions, and the halo of a point source is the lattice Green's function of
`sandbox/gravity_carrier_isotropy.py`'s point-scalar row (1/r at long range, isotropic to 0.993 at r = 12).
"""
import heapq
import sys
from itertools import product
from pathlib import Path

import numpy as np
from scipy.optimize import linprog

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from graphity.cqg_d import torus  # noqa: E402

L = int(sys.argv[1]) if len(sys.argv) > 1 else 6
D = 3
adj, part = torus((L, L, L))
N = adj.shape[0]
EDGES = sorted({(min(u, v), max(u, v)) for u in range(N) for v in adj[u]})
length = {e: 1.0 for e in EDGES}
NB = {u: list(adj[u]) for u in range(N)}
coords = np.array(np.unravel_index(np.arange(N), (L, L, L))).T
idx = {tuple(c): i for i, c in enumerate(coords)}


def dijkstra(src, radius):
    dist = {src: 0.0}
    heap = [(0.0, src)]
    while heap:
        d, p = heapq.heappop(heap)
        if d > dist[p] or d > radius:
            continue
        for q in NB[p]:
            nd = d + length[(min(p, q), max(p, q))]
            if nd < dist.get(q, np.inf):
                dist[q] = nd
                heapq.heappush(heap, (nd, q))
    return dist


def kappa(x, y):
    A, B = NB[x], NB[y]
    k = len(A)
    cost = np.empty((k, k))
    for i, a in enumerate(A):
        da = dijkstra(a, 6.0)
        for j, b in enumerate(B):
            cost[i, j] = da[b]
    Aeq = np.zeros((2 * k, k * k))
    for i in range(k):
        Aeq[i, i * k:(i + 1) * k] = 1
        Aeq[k + i, i::k] = 1
    res = linprog(cost.ravel(), A_eq=Aeq, b_eq=np.full(2 * k, 1.0 / k), bounds=(0, None), method="highs")
    assert res.success
    return 1.0 - res.fun / length[(min(x, y), max(x, y))]


def hops(src, r):
    seen = {src}; frontier = [src]
    for _ in range(r):
        frontier = [q for p in frontier for q in NB[p] if q not in seen]
        seen.update(frontier)
    return seen


KAP = {e: kappa(*e) for e in EDGES}
K0 = dict(KAP)
H0 = -4 * D * sum(KAP.values())


def energy_after(changed):
    near = set()
    for e in changed:
        near |= hops(e[0], 3) | hops(e[1], 3)
    for e in EDGES:
        if e[0] in near or e[1] in near:
            KAP[e] = kappa(*e)
    H = -4 * D * sum(KAP.values())
    KAP.update(K0)
    return H


def link(c, axis):
    a = idx[tuple(np.mod(c, L))]
    cc = list(np.mod(c, L)); cc[axis] = (cc[axis] + 1) % L
    return (min(a, idx[tuple(cc)]), max(a, idx[tuple(cc)]))


delta = 0.05
e0 = link((0, 0, 0), 0)
length[e0] = 1 + delta; He = energy_after([e0]); length[e0] = 1.0
print("L = %d: flat H %.2e; one link +0.05: dH = %.6f (12 d^2/(1+d) = %.6f)" % (L, H0, He - H0, 12 * delta ** 2 / (1 + delta)), flush=True)

print("(a),(d) mixed term M by offset of the second link (axis 0 = parallel to e0), all offsets within 2 steps:")
nonzero = []
for axis in (0, 1, 2):
    for off in product(range(-2, 3), repeat=3):
        f = link(np.array(off), axis)
        if f == e0:
            continue
        length[f] = 1 + delta; Hf = energy_after([f])
        length[e0] = 1 + delta; Hef = energy_after([e0, f])
        length[e0] = 1.0; length[f] = 1.0
        M = Hef - He - Hf + H0
        if abs(M) > 1e-9:
            nonzero.append((axis, off, M))
print("   non-zero mixed terms:", len(nonzero))
for axis, off, M in sorted(nonzero):
    print("   second link axis %d at offset %s: M = %+.6f  (-4 d^2/(1+d) = %+.6f)" % (axis, off, M, -4 * delta ** 2 / (1 + delta)))

print("(b) every length x 1.05:")
for e in EDGES:
    length[e] = 1.05
H = -4 * D * sum(kappa(*e) for e in EDGES)
for e in EDGES:
    length[e] = 1.0
print("   H_curv = %.2e" % H)

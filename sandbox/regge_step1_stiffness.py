"""Step 1 of the gravity link brief (docs/design/gravity_link_brief.md, section 4), a look in the sandbox lane: with the
published curvature written over link lengths, how does the energy of the flat six-link torus change when lengths are
perturbed, link by link? Exact arithmetic (shortest paths by Dijkstra, the transport cost by a linear programme).

Definitions ([T25] Sec. II.2, read by fetch on 28 October): m_x is the uniform measure on the k neighbours of x (no
mass at x); W(m_x, m_y) = min over couplings of sum xi(a, b) d(a, b) with d the shortest-path distance; kappa(x, y) =
1 - W / d(x, y); H_curv = -2D sum_i sum_{j ~ i} kappa(i, j) = -4D sum_edges kappa. With every length 1 the hand check
reproduces Eq. (8) at S = 0, 1, 2 in two dimensions and kappa = 0 on the flat lattice. Here d is the shortest path over
the link lengths l_e, and d(x, y) = l_xy for the edge itself.

WRITTEN BEFORE COMPUTING (ours): at the flat point the transport plans do not use the edge xy itself, so lengthening a
link changes its own kappa through 1 - 1/l and its neighbours' kappas through W, both LINEARLY in the perturbation, with
no quadratic restoring part: H_curv has no stationary point in the lengths and "Regge's step" (relax the lengths) runs
away rather than giving a halo. If so, the stiffness matrix of section 4 does not exist and the route "reach emerges from
the toy's own curvature" is closed as the toy's curvature stands; the published Regge action (deficit angle times hinge
measure) is a different functional, for which flat space is stationary. What would refute this: a single-link response
that is even in the perturbation (quadratic), with a mixed term between links that decays with their distance.

Measured here: (1) kappa on the flat torus (must be 0); (2) the energy change for one link lengthened or shortened by
delta = 0.01 ... 0.2 (odd or even in delta?); (3) the mixed change for two links perturbed together, against their
separation along and across the axis.
"""
import heapq
import sys
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
assert len(EDGES) == 3 * N
length = {e: 1.0 for e in EDGES}
NB = {u: list(adj[u]) for u in range(N)}


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
    # transport LP: xi >= 0, row sums 1/k, column sums 1/k
    c = cost.ravel()
    Aeq = np.zeros((2 * k, k * k))
    for i in range(k):
        Aeq[i, i * k:(i + 1) * k] = 1
        Aeq[k + i, i::k] = 1
    res = linprog(c, A_eq=Aeq, b_eq=np.full(2 * k, 1.0 / k), bounds=(0, None), method="highs")
    assert res.success
    return 1.0 - res.fun / length[(min(x, y), max(x, y))]


def hops(src, r):
    """Points within r hops of src."""
    seen = {src}
    frontier = [src]
    for _ in range(r):
        frontier = [q for p in frontier for q in NB[p] if q not in seen]
        seen.update(frontier)
    return seen


KAP = {}


def energy_full():
    for e in EDGES:
        KAP[e] = kappa(*e)
    return -4 * D * sum(KAP.values())


def energy_after(changed):
    """Recompute kappa only for edges with an end within 4 hops of a changed link; return H."""
    near = set()
    for e in changed:
        near |= hops(e[0], 4) | hops(e[1], 4)
    for e in EDGES:
        if e[0] in near or e[1] in near:
            KAP[e] = kappa(*e)
    return -4 * D * sum(KAP.values())


H0 = energy_full()
print("L = %d, N = %d, edges %d; flat energy %.6f; max |kappa| on the flat torus %.2e" % (
    L, N, len(EDGES), H0, max(abs(v) for v in KAP.values())), flush=True)
K0 = dict(KAP)

# a reference link along the first axis
x0 = 0
y0 = [v for v in NB[0] if (v // (L * L)) % L == 1 and v % (L * L) == 0][0]      # +axis-0 neighbour of the origin
e0 = (min(x0, y0), max(x0, y0))

print("\n(2) one link, length 1 + delta: change in H_curv")
for delta in (-0.2, -0.1, -0.05, -0.02, -0.01, 0.01, 0.02, 0.05, 0.1, 0.2):
    length[e0] = 1.0 + delta
    H = energy_after([e0])
    length[e0] = 1.0
    KAP.update(K0)
    print("   delta = %+.2f   dH = %+.6f   dH/delta = %+.4f" % (delta, H - H0, (H - H0) / delta), flush=True)

# locality check once: full recompute at delta = 0.05 must agree with the local one
length[e0] = 1.05
Hloc = energy_after([e0]); KAP.update(K0)
Hfull = energy_full()
length[e0] = 1.0; KAP.update(K0)
print("   locality check at delta = 0.05: local %.6f full %.6f" % (Hloc - H0, Hfull - H0), flush=True)

print("\n(3) two links at delta = 0.05 each: mixed term M = H(e,f) - H(e) - H(f) + H0, by separation")
coords = np.array(np.unravel_index(np.arange(N), (L, L, L))).T
idx = {tuple(c): i for i, c in enumerate(coords)}


def link(c, axis):
    a = idx[tuple(c)]
    cc = list(c); cc[axis] = (cc[axis] + 1) % L
    b = idx[tuple(cc)]
    return (min(a, b), max(a, b))


delta = 0.05
length[e0] = 1 + delta
He = energy_after([e0]); KAP.update(K0); length[e0] = 1.0
cases = [("same axis, +1 along", (1, 0, 0), 0), ("same axis, +2 along", (2, 0, 0), 0), ("same axis, +3 along", (3, 0, 0), 0),
         ("parallel, 1 across", (0, 1, 0), 0), ("parallel, 2 across", (0, 2, 0), 0), ("parallel, 3 across", (0, 3, 0), 0),
         ("perpendicular at origin", (0, 0, 0), 1), ("perpendicular at far end", (1, 0, 0), 1),
         ("perpendicular, 2 away", (0, 2, 0), 1)]
for name, c, axis in cases:
    f = link(c, axis)
    if f == e0:
        continue
    length[f] = 1 + delta
    Hf = energy_after([f]); KAP.update(K0)
    length[e0] = 1 + delta
    Hef = energy_after([e0, f]); KAP.update(K0)
    length[e0] = 1.0; length[f] = 1.0
    print("   %-26s  dH(e) %+.5f  dH(f) %+.5f  mixed M %+.6f" % (name, He - H0, Hf - H0, Hef - He - Hf + H0), flush=True)

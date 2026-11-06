"""A look (sandbox lane): one source on the cubic lattice; does the pull depend on direction under each carrier?

The owner's decision of 28 October (sandbox/NOTEBOOK.md, 13:03 UTC): gravity's carrier is on the links, in 3D only, the
diagonals making the lattice rigid being a feature; "the count of links is distance". Her inferred prediction for this
check: DIRECTION-DEPENDENT, the pace along the root-2 (diagonal) direction differing from the axis direction.
Ours: a count of links is the Manhattan distance, which differs by root 2 along a face diagonal and root 3 along a body
diagonal at every range; Regge's lengths (the diagonals at their Euclidean sizes) leave a smaller difference that does not
shrink with range; a smooth quantity on the points (Update 40, O61) is isotropic at long range.

Exact, no toy energy. Three carriers for the potential of one source at the origin:
  P  point scalar: the Green's function of the cubic-lattice Laplacian (FFT on a periodic box, mean removed).
  LC link count: potential 1/d, d the shortest path counted in links, with diagonals allowed at the owner's weights
     (face = 2 links, body = 3 links, box = 4 links): every diagonal ties with its edge path, so d is Manhattan.
  LR link lengths: potential 1/d, d the shortest path with every link and diagonal at its Euclidean length (Regge).
For each, the ratio of the potential along the face diagonal (r, r, 0)/root 2 and the body diagonal (r, r, r)/root 3 to
the potential along the axis (r, 0, 0), at the same Euclidean distance r. Isotropic means ratio 1.
"""
import heapq
from itertools import product

import numpy as np

L = 64
R = 24

# P: lattice Green's function on a periodic L^3 box
k = 2 * np.pi * np.fft.fftfreq(L)
KX, KY, KZ = np.meshgrid(k, k, k, indexing="ij")
lap = 2 * (3 - np.cos(KX) - np.cos(KY) - np.cos(KZ))
lap[0, 0, 0] = np.inf                     # zero mode removed (periodic box: a uniform background)
src = np.zeros((L, L, L)); src[0, 0, 0] = 1.0
G = np.real(np.fft.ifftn(np.fft.fftn(src) / lap))
G -= G[L // 2, L // 2, L // 2]            # potential relative to the far corner


def P(x, y, z):
    return G[x % L, y % L, z % L]


# link carriers: Dijkstra from the origin on a (2R+1)^3 block with the 26 lattice steps
STEPS = [s for s in product((-1, 0, 1), repeat=3) if any(s)]
STEPS += [s for s in product((-1, 0, 1), (-1, 0, 1), (-2, 2))] + \
         [s for s in product((-1, 0, 1), (-2, 2), (-1, 0, 1))] + [s for s in product((-2, 2), (-1, 0, 1), (-1, 0, 1))]
STEPS = [s for s in STEPS if sorted(map(abs, s)) in ([0, 0, 1], [0, 1, 1], [1, 1, 1], [1, 1, 2])]
COUNT = {(0, 0, 1): 1, (0, 1, 1): 2, (1, 1, 1): 3, (1, 1, 2): 4}
LENGTH = {(0, 0, 1): 1.0, (0, 1, 1): 2 ** .5, (1, 1, 1): 3 ** .5, (1, 1, 2): 6 ** .5}


def dijkstra(weight):
    dist = {(0, 0, 0): 0.0}
    heap = [(0.0, (0, 0, 0))]
    while heap:
        d, p = heapq.heappop(heap)
        if d > dist[p]:
            continue
        for s in STEPS:
            q = (p[0] + s[0], p[1] + s[1], p[2] + s[2])
            if max(map(abs, q)) > R:
                continue
            nd = d + weight[tuple(sorted(map(abs, s)))]
            if nd < dist.get(q, np.inf):
                dist[q] = nd
                heapq.heappush(heap, (nd, q))
    return dist


DC = dijkstra(COUNT)
DL = dijkstra(LENGTH)
print("steps per point:", len(STEPS), "(6 axis, 12 face, 8 body, 24 box)")
print("link count: Manhattan at every checked point:",
      all(abs(DC[p] - sum(map(abs, p))) < 1e-9 for p in DC))
print()
print("ratio of the potential along the face diagonal and the body diagonal to the potential along the axis,")
print("at equal Euclidean distance r (1 = no direction dependence)")
print("   r   point scalar face/axis body/axis | link count face body | link lengths face body")
for r in (4, 6, 8, 12, 16, 24):
    a = r
    f = int(round(r / 2 ** .5)); b = int(round(r / 3 ** .5))
    rf = f * 2 ** .5; rb = b * 3 ** .5          # the lattice points nearest to distance r on each diagonal
    # point scalar: interpolate the axis potential to the exact diagonal distances rf and rb
    ax = np.array([P(i, 0, 0) for i in range(1, 2 * R)])
    pa_f = np.interp(rf, np.arange(1, 2 * R), ax); pa_b = np.interp(rb, np.arange(1, 2 * R), ax)
    pf = P(f, f, 0) / pa_f; pb = P(b, b, b) / pa_b
    cf = (1 / DC[(f, f, 0)]) / (1 / rf); cb = (1 / DC[(b, b, b)]) / (1 / rb)
    lf = (1 / DL[(f, f, 0)]) / (1 / rf); lb = (1 / DL[(b, b, b)]) / (1 / rb)
    print("  %2d      %.4f   %.4f           |   %.4f %.4f       |   %.4f %.4f" % (r, pf, pb, cf, cb, lf, lb))
print()
print("link count, exact: face/axis = 1/sqrt2 = %.4f, body/axis = 1/sqrt3 = %.4f at every range" % (2 ** -.5, 3 ** -.5))
# worst direction for link lengths: scan the sphere at r = 20
worst = min((rr / DL[p], p) for p in DL if 19.5 < (rr := (p[0] ** 2 + p[1] ** 2 + p[2] ** 2) ** .5) < 20.5)
print("link lengths, worst direction near r = 20: ratio %.4f at %s" % worst)

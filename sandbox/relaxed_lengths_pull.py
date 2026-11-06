"""A look (sandbox lane), exact: with the link lengths relaxed from the relics' curl by step 1's stiffness, what is the
energy of two relics against their separation, and is light through the halo delayed?

Step 1 (regge_step1_stiffness.py): at flat the published curvature over link lengths is 1/2 delta^T K delta with
K = 4 (6 I - A) on each axis family of links (A the cubic adjacency of link positions), gapless. The brief's source term
couples a relic's curl to the length of its own links: alpha sum_e |c_e| delta_e, c_e = S_e - 4. Minimising over the
lengths exactly gives delta = -alpha K^+ |c| per family and the relaxed energy

    E_relax = -(alpha^2 / 2) |c|^T K^+ |c|,

so the energy of two relics is lower than the sum of their own by  alpha^2 |c_1|^T K^+ |c_2|  (per family, summed):
an attraction of Newton's shape for EITHER sign of alpha, since |c| >= 0; the sign of alpha sets only whether links near
matter are longer (alpha < 0, light delayed) or shorter (alpha > 0, light early). This is the owner's response rule
("a loop shifts toward a longer path") made exact: with alpha < 0 the relic's energy falls where links are long, and
links are long where the other relic's curl is.

WRITTEN BEFORE COMPUTING (ours): E_int(r) negative at every separation, falling in size roughly as 1/r at r >= 4, the same
for alpha = +a and -a, and with the axis and face-diagonal separations agreeing to within the point-scalar row of
gravity_carrier_isotropy.py (0.93 to 0.99); the light path through the halo longer than flat for alpha < 0 and shorter
for alpha > 0, by an amount proportional to |alpha|.

Relic here: the defect left by ONE random valid switch on the flat torus (not a dip; a look at the shape only), copied by
translation. L = 16, alpha = +-0.5.
"""
import heapq
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from graphity.cqg_d import torus, is_valid, squares_on_edge  # noqa: E402

L = 16
D = 3
adj0, part = torus((L, L, L))
N = adj0.shape[0]
coords = np.array(np.unravel_index(np.arange(N), (L, L, L))).T
idx = {tuple(c): i for i, c in enumerate(coords)}
rng = np.random.default_rng(3)


def switch_at(adj, u1, v1, u2, v2):
    # (u1,v1),(u2,v2) -> (u1,v2),(u2,v1)
    adj[u1, list(adj[u1]).index(v1)] = v2
    adj[v1, list(adj[v1]).index(u1)] = u2
    adj[u2, list(adj[u2]).index(v2)] = v1
    adj[v2, list(adj[v2]).index(u2)] = u1


def make_relic(adj, origin):
    """One valid switch among links near `origin`; returns the four points (for translation)."""
    o = idx[tuple(origin)]
    cand = [p for p in range(N) if np.all(np.abs((coords[p] - coords[o] + L // 2) % L - L // 2) <= 1)]
    for _ in range(10000):
        u1, u2 = rng.choice(cand, 2, replace=False)
        v1 = adj[u1, rng.integers(6)]; v2 = adj[u2, rng.integers(6)]
        if len({u1, v1, u2, v2}) < 4 or v1 in adj[u2] or v2 in adj[u1]:
            continue
        switch_at(adj, u1, v1, u2, v2)
        if is_valid(adj):
            return (u1, v1, u2, v2)
        switch_at(adj, u1, v2, u2, v1)
    raise RuntimeError


def translate(p, shift):
    return idx[tuple((coords[p] + shift) % L)]


def curl_fields(adj):
    """|c_e| on the three axis families as (3, L, L, L) arrays indexed by the link's lower point and axis;
    links that are not axis links (rewired by the switch) are assigned to the family of their nearest axis."""
    f = np.zeros((3, L, L, L))
    seen = set()
    for u in range(N):
        for v in adj[u]:
            e = (min(u, v), max(u, v))
            if e in seen:
                continue
            seen.add(e)
            c = abs(squares_on_edge(adj, u, v) - 4)
            if c == 0:
                continue
            d = (coords[v] - coords[u] + L // 2) % L - L // 2
            axis = int(np.argmax(np.abs(d)))
            lower = coords[u] if d[axis] > 0 else coords[v]
            f[axis][tuple(lower % L)] += c
    return f


k = 2 * np.pi * np.fft.fftfreq(L)
KX, KY, KZ = np.meshgrid(k, k, k, indexing="ij")
lam = 4 * (2 * (3 - np.cos(KX) - np.cos(KY) - np.cos(KZ)))      # eigenvalues of K = 4 (6I - A)
lam[0, 0, 0] = np.inf


def relax(f, alpha):
    """delta = -alpha K^+ f per family, and the relaxed energy -(alpha^2/2) f^T K^+ f (the zero mode set to zero mean)."""
    delta = np.empty_like(f)
    E = 0.0
    for a in range(3):
        F = np.fft.fftn(f[a])
        delta[a] = -alpha * np.real(np.fft.ifftn(F / lam))
        E += -(alpha ** 2 / 2) * np.sum(f[a] * np.real(np.fft.ifftn(F / lam)))
    return delta, E


def light_path(delta, src, dst):
    """Shortest path over lengths 1 + delta between two points, on the axis links only."""
    dist = {src: 0.0}; heap = [(0.0, src)]
    while heap:
        d, p = heapq.heappop(heap)
        if p == dst:
            return d
        if d > dist[p]:
            continue
        c = coords[p]
        for axis in range(3):
            for s in (1, -1):
                q = idx[tuple((c + s * np.eye(3, dtype=int)[axis]) % L)]
                lower = c if s > 0 else coords[q]
                nd = d + 1 + delta[axis][tuple(lower % L)]
                if nd < dist.get(q, np.inf):
                    dist[q] = nd; heapq.heappush(heap, (nd, q))


# relic A at the origin
adjA = adj0.copy()
quad = make_relic(adjA, np.array([0, 0, 0]))
fA = curl_fields(adjA)
print("relic A: a switch of four points, |c| total %.0f on families %s" % (fA.sum(), fA.sum(axis=(1, 2, 3))))

for alpha in (0.5, -0.5):
    _, EA = relax(fA, alpha)
    print("\nalpha = %+.2f: one relic's relaxed energy %.5f" % (alpha, EA))
    # reference shape: two unit point sources on family 0 with the same solver, the torus's own Green's function
    def ref(shift):
        f1 = np.zeros((3, L, L, L)); f1[0, 0, 0, 0] = 1.0
        f2 = f1.copy(); f2[0][tuple(shift % L)] += 1.0
        return relax(f2, alpha)[1] - 2 * relax(f1, alpha)[1]
    print("   separation   E_int (axis)   E_int (face diagonal)   | ratio to two point sources: axis, diagonal")
    for r in (2, 3, 4, 5, 6, 8):
        out = []
        for shift in (np.array([r, 0, 0]), np.array([r, r, 0])):
            adjB = adjA.copy()
            # relic B: the same switch translated
            u1, v1, u2, v2 = (translate(p, shift) for p in quad)
            # B's links as they were before its switch: in adjB (flat there) do the same switch
            switch_at(adjB, u1, v1, u2, v2)
            assert is_valid(adjB)
            fAB = curl_fields(adjB)
            _, EAB = relax(fAB, alpha)
            out.append(EAB - 2 * EA)
        ra, rd = ref(np.array([r, 0, 0])), ref(np.array([r, r, 0]))
        print("   %-10s   %+.5f        %+.5f (at r = %.2f)   |   %.3f   %.3f" % (
            r, out[0], out[1], r * 2 ** .5, out[0] / ra, out[1] / rd))
    # light delay: path from (-6,0,0) to (+6,0,0) past relic A at the origin, and across flat space
    deltaA, _ = relax(fA, alpha)
    src, dst = idx[((-3) % L, 0, 0)], idx[(3, 0, 0)]
    near = light_path(deltaA, src, dst)
    far = light_path(deltaA, idx[((-3) % L, 8, 8)], idx[(3, 8, 8)])
    print("   light: 6 links past the relic %.5f, the same far from it %.5f, flat 6 -> %s" % (
        near, far, "DELAYED" if near > far else "ADVANCED"))

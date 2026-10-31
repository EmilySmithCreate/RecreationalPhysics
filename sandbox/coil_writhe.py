"""A look (sandbox lane), exact geometry: does the fold (writhe) of a closed coil of box diagonals grow with its length, and
how much fold does one diagonal buy at best? Set by the owner's unit of 28 October (VISION Update 139): if fold weighs as
twist does, a proton must hold 1,835 units of fold, and the loops counted so far (proton_loop_fold.py) hold at most
0.26 per diagonal.

WRITTEN BEFORE COMPUTING (ours): the writhe of a closed coil grows in proportion to its turns, about 0.5 to 0.6 per turn
for the tightest lattice helix (four box diagonals a turn, rising 4 a turn), so about 0.13 to 0.15 per diagonal, and
1,835 units need roughly 3,000 to 3,700 turns, 12,000 to 15,000 diagonals; a wider helix (eight diagonals a turn) buys
more per turn but less per diagonal. If the writhe per turn instead saturates or falls with the number of turns, a
proton of fold is impossible on this lattice.

The coil: m turns of the helix (2,1,1), (-1,2,1), (-2,-1,1), (1,-2,1) from the origin (each turn rises 4 and returns
above its start), a bridge (2,1,1), (2,1,-1) to the offset (4,2,0), m turns of the same helix traversed backwards (the
negated steps in reverse order, which keeps the handedness, so the two halves' writhe add), and the bridge back,
(-2,-1,-1), (-2,-1,1) (the first order touched the helix's first point). Closed, 8m + 4 diagonals. Checked simple (no two non-adjacent segments touching). Writhe by the
Gauss double integral over non-adjacent segment pairs, each segment split into 8 pieces with 16-point Gauss-Legendre.
"""
import sys

import numpy as np

PIECES = 8
gx, gw = np.polynomial.legendre.leggauss(16)
GX = np.concatenate([(k + (gx + 1) / 2) / PIECES for k in range(PIECES)])
GW = np.concatenate([gw / 2 / PIECES for _ in range(PIECES)])


def writhe(V):
    n = len(V)
    total = 0.0
    T = np.roll(V, -1, axis=0) - V                         # segment vectors
    R = V[:, None, :] + GX[None, :, None] * T[:, None, :]  # (n, Q, 3) sample points
    for i in range(n):
        js = [j for j in range(n) if j != i and (i + 1) % n != j and (j + 1) % n != i]
        if not js:
            continue
        cr = np.cross(T[i], T[js])                          # (J, 3)
        d = R[i][:, None, None, :] - R[js][None, :, :, :]   # (Q, J, Q, 3)
        num = np.einsum("qjpk,jk->qjp", d, cr)
        den = np.linalg.norm(d, axis=3) ** 3
        total += np.einsum("q,p,qjp->", GW, GW, num / den)
    return total / (4 * np.pi)


def seg_dist(a0, a1, b0, b1):
    u, v, w = a1 - a0, b1 - b0, a0 - b0
    A, B, C, D, E = u @ u, u @ v, v @ v, u @ w, v @ w
    den = A * C - B * B
    if den < 1e-12:
        s = 0.0; tt = np.clip(E / C, 0, 1)
    else:
        s = np.clip((B * E - C * D) / den, 0, 1)
        tt = (B * s + E) / C
        if tt < 0:
            tt = 0.0; s = np.clip(-D / A, 0, 1)
        elif tt > 1:
            tt = 1.0; s = np.clip((B - D) / A, 0, 1)
    return np.linalg.norm(w + s * u - tt * v)


def min_gap(V):
    n = len(V)
    return min(seg_dist(V[i], V[(i + 1) % n], V[j], V[(j + 1) % n])
               for i in range(n) for j in range(i + 2, n) if not (i == 0 and j == n - 1))


TURN = [(2, 1, 1), (-1, 2, 1), (-2, -1, 1), (1, -2, 1)]
WIDE = [(2, 1, 1), (1, 2, 1), (-1, 2, 1), (-2, 1, 1), (-2, -1, 1), (-1, -2, 1), (1, -2, 1), (2, -1, 1)]   # 8 a turn, rises 8


def coil(m, turn, bridge_out, bridge_back):
    steps = turn * m + bridge_out + [tuple(-np.array(s)) for s in reversed(turn)] * m + bridge_back
    V = [np.zeros(3)]
    for s in steps:
        V.append(V[-1] + np.array(s, dtype=float))
    assert np.allclose(V[-1], 0), "not closed"
    V = np.array(V[:-1])
    assert len({tuple(p) for p in V}) == len(V), "a point repeats"
    return V


if __name__ == "__main__":   # guarded 30 October so that anchor_muon_tau.py can import coil and writhe
    ms = [int(a) for a in sys.argv[1:]] or [1, 2, 3, 4, 6, 8, 12, 16]
    for name, turn, out, back in (    ("tight (4 diagonals a turn, rise 4)", TURN, [(2, 1, 1), (2, 1, -1)], [(-2, -1, -1), (-2, -1, 1)]),
                                  ("wide (8 diagonals a turn, rise 8)", WIDE, [(2, 1, 1), (2, 1, -1), (2, 1, 1), (2, 1, -1)],
                                   [(-2, -1, -1), (-2, -1, 1), (-2, -1, -1), (-2, -1, 1)])):
        print(name)
        prev = None
        for m in ms:
            V = coil(m, turn, out, back)
            gap = min_gap(V)
            w = writhe(V)
            n = len(V)
            inc = "" if prev is None else "  (+%.3f per added turn)" % ((w - prev[0]) / (m - prev[1]))
            print("  m = %2d turns, %3d diagonals: writhe %+.3f, per turn %.3f, per diagonal %.4f, min gap %.2f%s" % (
                m, n, w, w / (2 * m), w / n, gap, inc), flush=True)
            prev = (w, m)

"""Sandbox look (kill but not crown), 3 November 2026: is the gamma reader itself sound? T85 and T100 found alpha* drifting
across impact parameters for wiring knots. Here the halo is put in by hand and isotropic: every axis link is lengthened by
delta = a0 / r (r the torus-minimal distance from the center to the link's midpoint, floored at 1), the body diagonals are
derived as in graphity.diagonals, and the "potential" is the same field, U(x) = a0 / r. D(b) is the zigzag path's ticks
with the halo minus without it; P(b) is the sum of U over the path's points times sqrt 3 (T100's definitions). The
reader's ratio D / (2 P) is reported against b.

WRITTEN BEFORE COMPUTING (ours): if the reader is sound, D / (2 P) is the same number at every b within +-10 % for
b <= L/2 - 4 (the diagonals lengthen to first order by the mean of their cube's edges over sqrt 3, so D is the path integral
of the same field P integrates), and the ratio is unchanged when a0 is halved (linearity). If it drifts here, the drift in
T85 and T100 is the reader's, not the halo's.
"""
import sys
import numpy as np
sys.path.insert(0, "src"); sys.path.insert(0, "scripts")
from graphity import diagonals
from t100_gamma_consistent import zigzag_points, path_ticks

L = int(sys.argv[1]) if len(sys.argv) > 1 else 24
R = L // 4
idx = np.indices((L, L, L)).astype(float)


def torus_r(x, y, z):
    d = np.stack([x, y, z]); d = (d + L / 2) % L - L / 2
    return np.sqrt((d ** 2).sum(axis=0))


def halo(a0):
    delta = np.zeros((3, L, L, L))
    for a in range(3):
        mid = idx.copy(); mid[a] += 0.5
        delta[a] = a0 / np.maximum(torus_r(*mid), 1.0)
    return delta


flat = diagonals.diagonal_lengths(np.zeros((3, L, L, L)))
for a0 in (0.1, 0.05):
    diag = diagonals.diagonal_lengths(halo(a0))
    print(f"L = {L}, a0 = {a0}:   b    D        P        D/(2P)")
    for b in range(2, L // 2 - 1, 2):
        pts = zigzag_points((-R, b, 0), 2 * R)
        D = path_ticks(diag, pts, L) - path_ticks(flat, pts, L)
        P = sum(a0 / max(torus_r(*np.array(p, float)), 1.0) for p in pts) * np.sqrt(3)
        print(f"                         {b:2d}   {D:.5f}  {P:.5f}  {D / (2 * P):.4f}")

"""Sandbox look, 23 October 2026 (rule 16: a look; it can kill, not crown). The owner's idea of the same evening:
"without movement space has just 2 degrees of freedom, and that is what happens in the cold flat end." What do the
toy's still, cold, perfect lattices read as a random-walk dimension, scale by scale? Built graphs only (perfect shapes,
no saved state; nothing T80 scores). Discrete walk, `graphity.dimension.spectral_dimension`, readings while the
finite-size floor holds less than 0.3 of the return probability (T80's draft window), first step excluded.

Shapes: a wide flat sheet (24 x 24), a narrow flat torus like the burp's product (6 x 96; O116: the tube opens into a
tube six around), the tube (4 x 96), and a six-link cubic lattice (12 x 12 x 12, built here as a 6-regular torus).

Usage: python3 sandbox/cold_flat_dimension_look.py
"""
import os
import sys

import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "src"))
from graphity import cqg  # noqa: E402
from graphity.dimension import spectral_dimension  # noqa: E402


def cubic_torus(n):
    """The n x n x n cubic lattice torus as an (N, 6) neighbour array."""
    idx = lambda x, y, z: ((x % n) * n + (y % n)) * n + (z % n)
    adj = np.zeros((n ** 3, 6), dtype=np.int64)
    for x in range(n):
        for y in range(n):
            for z in range(n):
                adj[idx(x, y, z)] = [idx(x + 1, y, z), idx(x - 1, y, z), idx(x, y + 1, z),
                                     idx(x, y - 1, z), idx(x, y, z + 1), idx(x, y, z - 1)]
    return adj


SHAPES = [
    ("wide flat sheet 24 x 24", cqg.torus(24, 24, cap=cqg.NO_CAP)[0]),
    ("narrow flat torus 6 x 96 (like the burp's product)", cqg.torus(6, 96, cap=cqg.NO_CAP)[0]),
    ("tube 4 x 96 (one direction curled)", cqg.torus(4, 96, cap=cqg.NO_CAP)[0]),
    ("six-link cubic lattice 12 x 12 x 12", cubic_torus(12)),
]

for name, adj in SHAPES:
    out = spectral_dimension(adj, 4000)
    t_mid, ds, p, floor = out["t_mid"], out["D_s"], out["P"], out["floor"]
    share = floor / p[:-1]                         # floor's share at the earlier t of each pair
    keep = (share < 0.3) & (t_mid > 3.0)           # inside the window; first step excluded
    marks = [8, 16, 32, 64, 128, 256, 512, 1024]
    line = []
    for m in marks:
        sel = np.flatnonzero(keep & (t_mid >= m))
        if sel.size:
            i = sel[0]
            line.append("t~%d: %.2f" % (m, ds[i]))
    print("%-52s N = %5d | %s" % (name, adj.shape[0], "  ".join(line)))

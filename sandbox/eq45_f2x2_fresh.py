"""Sandbox look, 23 October 2026 (rule 16: a look; it can kill, not crown). On fresh warm chains with NEW seeds (not
T78's; no saved state is opened), the 2 x 2 grid count per point and the free energy -g ln(n/N) it gives, at g = 3.3 and
3.697, N = 196, lambda = 1: the F convention of the Eq. (45) ratio brief (docs/design/eq45_ratio_brief.md, handoff item
2.3). Written by an assistant agent while correcting the brief; kept here so the look can be rerun.

Usage: python3 sandbox/eq45_f2x2_fresh.py
"""
import math
import os
import sys

import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "src"))
from graphity.cqg import NO_CAP, torus, run_chain, total_squares, surplus  # noqa: E402
from graphity.objects import count_grid  # noqa: E402

for g in (3.3, 3.697):
    vals = []
    for rep in range(2):
        adj, part = torus(14, 14, NO_CAP)
        su = np.flatnonzero(part == 0)
        run_chain(adj, su, 0.0, 200, 1, 880000 + rep + int(g * 1000), 1.0, NO_CAP, False)
        run_chain(adj, su, 1.0 / g, 20000, 1, -1, 1.0, NO_CAP, False)
        for s in range(10):
            run_chain(adj, su, 1.0 / g, 0, 500, -1, 1.0, NO_CAP, False)
            vals.append((count_grid(adj, 2, 2, True) / 196.0, total_squares(adj) / 196.0, surplus(adj) / 196.0))
    v = np.array(vals).mean(axis=0)
    print("g=%.3f  n_2x2/N %.3f  S/N %.3f  X/N %.3f  -> -g ln(n/N) = %+.2f" % (g, v[0], v[1], v[2], -g * math.log(v[0])))

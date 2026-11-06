"""A look (sandbox lane): is there a stationary warm six-link flat space with many defects, between "nothing moves" and
"melts"? The audit of 28 October (O166 (11)) asks this before any correlation or clustering test; T83 found no such window
in two dimensions in 4,000 sweeps (frozen at g <= 3, melting at g >= 4). In three dimensions the flat wall is 64, so the
window, if any, sits at a larger coupling.

WRITTEN BEFORE RUNNING (ours): no window. Below the coupling where the first move is accepted in 2,000 sweeps, nothing
moves; at and above it the flat share falls through the run without levelling (a nucleating melt), as in two dimensions.
A window would show as a cell whose flat share in the second half of the run is within 0.01 of the first half's and
below 0.99 (so at least a few dozen defective links).

Protocol: flat L^3 torus (L = 8), lambda = 1.25, cqg_d.run_chain (the published move, Metropolis), g from 4 to 24,
2,000 sweeps of warm-up then 2,000 measured in blocks of 200; per block the flat share (links with 4 squares) and the
total squares; one replica a coupling. Takes minutes.
"""
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from graphity.cqg_d import run_chain, torus, squares_on_edge  # noqa: E402

L = int(sys.argv[1]) if len(sys.argv) > 1 else 8
LAM = 1.25
dims = (L, L, L)


def flat_share(adj):
    n = adj.shape[0]
    tot = flat = 0
    for u in range(n):
        for v in adj[u]:
            if v > u:
                tot += 1
                flat += squares_on_edge(adj, u, v) == 4
    return flat / tot


print("L = %d, lambda = %.2f; flat share per block of 200 sweeps after 2,000 of warm-up" % (L, LAM))
for g in (4, 6, 8, 10, 12, 16, 20, 24):
    adj, part = torus(dims)
    side = np.flatnonzero(part == 0)
    run_chain(adj, side, 1.0 / g, 2000, 0, 20268400 + g, LAM)
    shares, phis, acc = [], [], []
    for _ in range(10):
        s, x, a = run_chain(adj, side, 1.0 / g, 0, 200, -1, LAM)
        shares.append(flat_share(adj)); phis.append(s[-1] / adj.shape[0]); acc.append(a)
    first, second = np.mean(shares[:5]), np.mean(shares[5:])
    word = ("FROZEN" if second > 0.999 else "WINDOW" if abs(first - second) < 0.01 and second < 0.99 else "MELTING")
    print("  g = %4.1f  flat share %s  halves %.3f %.3f  phi %.3f  acc %.4f  -> %s" % (
        g, " ".join("%.3f" % v for v in shares), first, second, phis[-1], np.mean(acc), word), flush=True)

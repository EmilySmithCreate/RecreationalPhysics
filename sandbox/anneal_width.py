"""Sandbox: warm a flat torus six around until it is disordered, cool it slowly, and see how wide it re-forms. Usage:

    python sandbox/anneal_width.py LENGTH HOT COOL_SWEEPS [REPLICAS] [LAMBDA] [START]

START is "twist" (the tube with its seam shifted by two; the default) or "tube" (the curled tube itself).
Holds at coupling HOT for 4,000 sweeps, cools in 40 equal steps of coupling down to 1.0 over COOL_SWEEPS, then
sits at g = 0.05. Reads the end: exactly flat or not, its width if flat, and in any case the largest number of
points at one distance from a point (8 for a tube, about sqrt(2N) for a torus as wide as it is long).
"""
import statistics
import sys
from collections import Counter
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "scripts"))
from graphity.cqg import NO_CAP, hamiltonian, run_chain              # noqa: E402
from read_endpoint_width import is_flat, twisted_tube, width         # noqa: E402
from read_open_shells import shells                                  # noqa: E402


def main(length, hot, cool_sweeps, replicas=8, lam=1.25, start="twist", seed=2026101200):
    n = 4 * length
    side = np.array([x * length + y for x in range(4) for y in range(length) if (x + y) % 2 == 0], dtype=np.int64)
    steps = 40
    print("N = %d, lambda = %.2f, start %s, hot g = %.2f for 4000 sweeps, cooled to 1.0 over %d sweeps"
          % (n, lam, start, hot, cool_sweeps))
    widths, wide = Counter(), []
    for rep in range(replicas):
        adj = twisted_tube(length, 2 if start == "twist" else 0)
        s, _x, _a = run_chain(adj, side, 1.0 / hot, 3999, 1, seed + 7919 * rep + int(100 * hot) + cool_sweeps, lam, NO_CAP)
        hot_phi = s[-1] / n
        for i in range(steps):
            g = hot + (1.0 - hot) * (i + 1) / steps
            run_chain(adj, side, 1.0 / g, max(1, cool_sweeps // steps) - 1, 1, -1, lam, NO_CAP)
        run_chain(adj, side, 1.0 / 0.05, 1999, 1, -1, lam, NO_CAP)
        flat = is_flat(adj)
        w = width(adj) if flat else 0
        largest = statistics.median(max(shells(adj, int(v))) for v in np.linspace(0, n - 1, 8).astype(int))
        widths[w] += 1
        wide.append(largest)
        print("  replica %d: squares per point when hot %.2f | end energy %6.1f | %s | largest shell %g"
              % (rep, hot_phi, hamiltonian(adj, lam), ("flat, width %d" % w) if flat else "not flat", largest))
    print("  ends: %s (0 = not exactly flat) | largest shell, median %g, range %g to %g"
          % (dict(sorted(widths.items())), statistics.median(wide), min(wide), max(wide)))


if __name__ == "__main__":
    a = sys.argv[1:]
    main(int(a[0]), float(a[1]), int(a[2]), int(a[3]) if len(a) > 3 else 8, float(a[4]) if len(a) > 4 else 1.25,
         a[5] if len(a) > 5 else "twist")

"""Sandbox: does a flat torus six around get wider if it is kept warm? Usage:

    python sandbox/warm_width.py LENGTH G [REPLICAS] [ROUNDS] [WARM_SWEEPS] [LAMBDA]

Starts from the tube with its seam shifted by two (4 x LENGTH points, flat, six around). Each round: run the chain
warm at coupling G, then copy the graph, cool the copy (the chain at g = 0.05, which takes no uphill move) and read
it: is it exactly flat, and if so how wide? The warm graph carries on. Prints one line per replica.
"""
import sys
from collections import Counter
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "scripts"))
from graphity.cqg import NO_CAP, run_chain, total_squares           # noqa: E402
from read_endpoint_width import is_flat, twisted_tube, width        # noqa: E402

COLD = 1.0 / 0.05


def main(length, g, replicas=4, rounds=20, warm=2000, lam=1.25, quench=3000, seed=2026101100):
    n = 4 * length
    side = np.array([x * length + y for x in range(4) for y in range(length) if (x + y) % 2 == 0], dtype=np.int64)
    print("N = %d, lambda = %.2f, warm at g = %.2f, %d rounds of %d sweeps" % (n, lam, g, rounds, warm))
    summary = Counter()
    for rep in range(replicas):
        adj = twisted_tube(length, 2)
        assert is_flat(adj) and width(adj) == 6
        run_chain(adj, side, 1.0 / g, 0, 1, seed + 1000 * rep + int(100 * g), lam, NO_CAP)
        seen, phi = [], []
        for _ in range(rounds):
            s, _x, _acc = run_chain(adj, side, 1.0 / g, warm - 1, 1, -1, lam, NO_CAP)
            phi.append(s[-1] / n)
            cold = adj.copy()
            run_chain(cold, side, COLD, quench - 1, 1, -1, lam, NO_CAP)
            seen.append(width(cold) if is_flat(cold) else 0)
        flat = [w for w in seen if w]
        summary.update(flat)
        print("  replica %d: squares per point while warm %.2f to %.2f | cooled copies flat in %d of %d | widths %s"
              % (rep, min(phi), max(phi), len(flat), rounds, " ".join(str(w) if w else "." for w in seen)))
    print("  widths of the cooled flat copies, all replicas:", dict(sorted(summary.items())))


if __name__ == "__main__":
    a = sys.argv[1:]
    main(int(a[0]), float(a[1]), *(int(x) for x in a[2:5]), *(float(x) for x in a[5:6]))

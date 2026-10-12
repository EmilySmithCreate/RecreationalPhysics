"""Sandbox: the same price on loops of six, but starting from the curled tube itself (four around). Usage:

    python sandbox/six_loop_from_tube.py LENGTH MU G [HOLD] [COOL] [REPLICAS] [LAMBDA]

T62 starts from the tube six around. This look asks what the curled tube does in one go: with the price it sits
1 + 18 mu per point above a wide flat torus at lambda = 1.25, and 1 + 3 mu above the tube six around. Warm for
HOLD sweeps at G, cooled to 0.5 over COOL sweeps, then cold, as in T62. A look for designing the next test.
"""
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "scripts"))
sys.path.insert(0, str(ROOT / "sandbox"))
from graphity.sixloop import excess6, run_chain6                    # noqa: E402
from read_endpoint_width import twisted_tube                        # noqa: E402
from read_flat_kind import describe                                 # noqa: E402
from shape_tools import read                                        # noqa: E402


def main(length, mu, g, hold=30000, cool=60000, replicas=6, lam=1.25):
    n = 4 * length
    side = np.array([x * length + y for x in range(4) for y in range(length) if (x + y) % 2 == 0], dtype=np.int64)
    print("from the curled tube: N=%d lambda=%.2f mu=%.2f g=%.2f, %d warm sweeps, cooled over %d" % (n, lam, mu, g, hold, cool),
          flush=True)
    for rep in range(replicas):
        adj = twisted_tube(length, 0)
        e0 = int(excess6(adj, side))
        s, x, e, _a = run_chain6(adj, side, 1.0 / g, 0, hold, 20261015 + 7919 * rep + int(1000 * mu) + int(100 * g), lam, mu)
        low = s.min() / n
        gone = np.flatnonzero(x == 0)                                 # the first sweep with no surplus square left
        warm = (s[-1] / n, x[-1] / n, e[-1] / e0)
        for step in range(40):
            s, x, e, _a = run_chain6(adj, side, 1.0 / (g + (0.5 - g) * (step + 1) / 40), 0, max(1, cool // 40), -1, lam, mu)
            low = min(low, s.min() / n)
        run_chain6(adj, side, 1.0 / 0.05, 0, 1000, -1, lam, mu)
        end = read(adj, lam)
        e_end = int(excess6(adj, side))
        what = "; ".join("%s %s around (%d)" % (k, w, size) for size, k, w in describe(adj)) if end["flat"] else "flaws left"
        print("  %d: curl gone at sweep %s | after the warm spell: squares %.2f, surplus %.2f, six-loop excess %.2f of the "
              "start | fewest squares %.2f | end: energy %5.1f, excess %4d, sees3 %.2f | %s"
              % (rep, gone[0] if gone.size else "never", warm[0], warm[1], warm[2], low, end["energy"], e_end, end["sees3"],
                 what), flush=True)


if __name__ == "__main__":
    a = sys.argv[1:]
    main(int(a[0]), float(a[1]), float(a[2]), int(a[3]) if len(a) > 3 else 30000, int(a[4]) if len(a) > 4 else 60000,
         int(a[5]) if len(a) > 5 else 6, float(a[6]) if len(a) > 6 else 1.25)

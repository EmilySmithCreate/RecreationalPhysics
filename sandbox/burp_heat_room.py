"""Sandbox: the same sealed-then-drained tubes as burp_heat_width.py, read by a measure that flaws disturb less:
for each point, the number of points within 3, 4 and 5 steps (25, 41, 61 on an endless sheet; 22, 30, 38 on the
tube with its seam shifted by two). Usage: python sandbox/burp_heat_room.py LENGTH STORES [REPLICAS] [LAMBDA]"""
import statistics
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src")); sys.path.insert(0, str(ROOT / "scripts")); sys.path.insert(0, str(ROOT / "sandbox"))
from graphity.cqg import NO_CAP, hamiltonian, run_chain, torus       # noqa: E402
from graphity.dimension import local_dimension                       # noqa: E402
from graphity.sealed import run_sealed_bath                          # noqa: E402
from read_open_shells import shells                                  # noqa: E402


def end_state(length, stores, lam, seed, leak=0.02, hold=20000):
    adj, part = torus(length, 4, NO_CAP)
    side = np.flatnonzero(part == 0).astype(np.int64)
    demons = np.zeros(stores, dtype=np.float64)
    demons[0] = min(32.0 - 16.0 * lam, 64.0 - 40.0 * lam)
    run_sealed_bath(adj, side, demons, hold, seed, lam, NO_CAP, None, False)
    blocks = 0
    while demons.sum() > 0.5 and blocks < 4000:
        demons *= (1.0 - leak)
        run_sealed_bath(adj, side, demons, 100, -1, lam, NO_CAP, None, False)
        blocks += 1
    run_chain(adj, side, 1.0 / 0.05, 1999, 1, -1, lam, NO_CAP)
    return adj


def main(length, stores, replicas=8, lam=1.25):
    n = 4 * length
    print("N=%d lambda=%.2f stores=%d: per replica: energy left | points at d=2 | mean points within 3, 4, 5 steps | "
          "share of points that see the endless sheet out to 3 steps, to 4 steps" % (n, lam, stores))
    for rep in range(replicas):
        adj = end_state(length, stores, lam, 2026101300 + 104729 * rep + 31 * stores + length)
        d = local_dimension(adj)
        balls = np.array([np.cumsum(shells(adj, v)[:6] + [0] * 6)[:6] for v in range(n)])
        print("  %d: %6.1f | %3d of %d | %.1f %.1f %.1f | %.2f %.2f"
              % (rep, hamiltonian(adj, lam), int((d == 2).sum()), n, balls[:, 3].mean(), balls[:, 4].mean(),
                 balls[:, 5].mean(), (balls[:, 3] == 25).mean(), (balls[:, 4] == 41).mean()))


if __name__ == "__main__":
    a = sys.argv[1:]
    main(int(a[0]), int(a[1]), int(a[2]) if len(a) > 2 else 8, float(a[3]) if len(a) > 3 else 1.25)

"""Sandbox: energy comes in and cannot leave. Usage:

    python sandbox/feed_energy.py LENGTH RATE [FEED_SWEEPS] [REPLICAS] [LAMBDA] [MODE]

A sealed tube (4 x LENGTH points) with one store per point, shared, and the wall's spark in one. Every 100 sweeps
RATE units are added to one store chosen at random, for FEED_SWEEPS sweeps; nothing is taken out. Then the feed
stops, the stores are drained by 2 % every 100 sweeps and the graph is left cold and read.

MODE "all" (default): energy may pay for any move. MODE "curl": energy may only pay for moves that add or remove
surplus squares (curl or uncurl); a move that only breaks squares is refused. The second is the owner's question
of 11 October: what if the available energy can do nothing but curl and uncurl?
"""
import inspect
import sys
from pathlib import Path

import numpy as np
from numba import njit

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "sandbox"))
from graphity import sealed                                         # noqa: E402
from graphity.cqg import NO_CAP, hamiltonian, run_chain, torus      # noqa: E402
from shape_tools import line, read                                  # noqa: E402

_src = inspect.getsource(sealed.run_sealed_bath.py_func).replace("@njit(cache=True)\n", "")
_old = "if d_h > demons[k]:"
assert _src.count(_old) == 1
_src = _src.replace(_old, "if d_h > demons[k] or (d_s < 0 and d_x >= 0):").replace("def run_sealed_bath(", "def run_curl_only(")
_ns = dict(vars(sealed))
exec(_src, _ns)
run_curl_only = njit(_ns["run_curl_only"])


def one(length, rate, feed, lam, mode, seed):
    chain = sealed.run_sealed_bath if mode == "all" else run_curl_only
    adj, part = torus(length, 4, NO_CAP)
    n = adj.shape[0]
    side = np.flatnonzero(part == 0).astype(np.int64)
    demons = np.zeros(n, dtype=np.float64)
    demons[0] = min(32.0 - 16.0 * lam, 64.0 - 40.0 * lam)
    rng = np.random.default_rng(seed)
    chain(adj, side, demons, 1, seed, lam, NO_CAP, None, False)
    low, fed = 9.9, 0.0
    for _ in range(feed // 100):
        demons[rng.integers(0, n)] += rate
        fed += rate
        s, _x, mean, _sum, _acc = chain(adj, side, demons, 100, -1, lam, NO_CAP, None, False)
        low = min(low, s.min() / n)
    hot = dict(phi=s[-1] / n, low=low, store=float(demons.mean()), energy=float(hamiltonian(adj, lam)))
    blocks = 0
    while demons.sum() > 0.5 and blocks < 6000:
        demons *= 0.98
        chain(adj, side, demons, 100, -1, lam, NO_CAP, None, False)
        blocks += 1
    if mode == "all":
        run_chain(adj, side, 1.0 / 0.05, 1999, 1, -1, lam, NO_CAP)
    return fed, hot, read(adj, lam)


def main(length, rate, feed=40000, replicas=4, lam=1.25, mode="all"):
    print("N=%d lambda=%.2f mode=%s: %.2f units every 100 sweeps for %d sweeps (%.1f per point in all)"
          % (4 * length, lam, mode, rate, feed, rate * feed / 100 / (4 * length)))
    for rep in range(replicas):
        fed, hot, end = one(length, rate, feed, lam, mode, 2026101400 + 7919 * rep + int(1000 * rate))
        print("  when the feed stops: squares per point %.2f (lowest %.2f), graph energy %.0f, per store %.2f | at the end: %s"
              % (hot["phi"], hot["low"], hot["energy"], hot["store"], line(end)))


if __name__ == "__main__":
    a = sys.argv[1:]
    main(int(a[0]), float(a[1]), int(a[2]) if len(a) > 2 else 40000, int(a[3]) if len(a) > 3 else 4,
         float(a[4]) if len(a) > 4 else 1.25, a[5] if len(a) > 5 else "all")

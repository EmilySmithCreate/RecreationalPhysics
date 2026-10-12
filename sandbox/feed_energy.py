"""Sandbox: energy comes in and cannot leave. Usage:

    python sandbox/feed_energy.py LENGTH RATE [FEED_SWEEPS] [REPLICAS] [LAMBDA] [MODE] [START]

A sealed tube (4 x LENGTH points) with one store per point, shared, and the wall's spark in one. Every 100 sweeps
RATE units are added to one store chosen at random, for FEED_SWEEPS sweeps; nothing is taken out. Then the feed
stops, the stores are drained by 2 % every 100 sweeps and the graph is left cold and read.

MODE "all" (default): energy may pay for any move. MODE "curl": energy may only pay for moves that add or remove
surplus squares (curl or uncurl); a move that only breaks squares is refused. The second is the owner's question
of 11 October: what if the available energy can do nothing but curl and uncurl?

START "tube" (default) or "twist": the tube already re-glued, flat and six around, with no spark. The second asks
the reverse of the burp: does energy that is supplied curl flat fabric back up? Surplus squares per point are 1 on
the curled tube and 0 on flat fabric.
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
from graphity.cqg import NO_CAP, hamiltonian, run_chain, surplus, torus      # noqa: E402
sys.path.insert(0, str(ROOT / "scripts"))
from read_endpoint_width import twisted_tube                      # noqa: E402
from shape_tools import line, read                                  # noqa: E402

_src = inspect.getsource(sealed.run_sealed_bath.py_func).replace("@njit(cache=True)\n", "")
_old = "if d_h > demons[k]:"
assert _src.count(_old) == 1
_src = _src.replace(_old, "if d_h > demons[k] or (d_s < 0 and d_x >= 0):").replace("def run_sealed_bath(", "def run_curl_only(")
_ns = dict(vars(sealed))
exec(_src, _ns)
run_curl_only = njit(_ns["run_curl_only"])


def one(length, rate, feed, lam, mode, seed, start="tube"):
    chain = sealed.run_sealed_bath if mode == "all" else run_curl_only
    if start == "tube":
        adj, part = torus(length, 4, NO_CAP)
        side = np.flatnonzero(part == 0).astype(np.int64)
    else:
        adj = twisted_tube(length, 2)
        side = np.array([x * length + y for x in range(4) for y in range(length) if (x + y) % 2 == 0], dtype=np.int64)
    n = adj.shape[0]
    demons = np.zeros(n, dtype=np.float64)
    if start == "tube":
        demons[0] = min(32.0 - 16.0 * lam, 64.0 - 40.0 * lam)
    rng = np.random.default_rng(seed)
    chain(adj, side, demons, 1, seed, lam, NO_CAP, None, False)
    low, fed = 9.9, 0.0
    for _ in range(feed // 100):
        demons[rng.integers(0, n)] += rate
        fed += rate
        s, _x, mean, _sum, _acc = chain(adj, side, demons, 100, -1, lam, NO_CAP, None, False)
        low = min(low, s.min() / n)
    hot = dict(phi=s[-1] / n, low=low, store=float(demons.mean()), energy=float(hamiltonian(adj, lam)),
               curl=surplus(adj) / n)
    blocks = 0
    while demons.sum() > 0.5 and blocks < 6000:
        demons *= 0.98
        chain(adj, side, demons, 100, -1, lam, NO_CAP, None, False)
        blocks += 1
    if mode == "all":
        run_chain(adj, side, 1.0 / 0.05, 1999, 1, -1, lam, NO_CAP)
    return fed, hot, read(adj, lam), surplus(adj) / n


def main(length, rate, feed=40000, replicas=4, lam=1.25, mode="all", start="tube"):
    print("N=%d lambda=%.2f mode=%s start=%s: %.2f units every 100 sweeps for %d sweeps (%.1f per point in all)"
          % (4 * length, lam, mode, start, rate, feed, rate * feed / 100 / (4 * length)))
    for rep in range(replicas):
        fed, hot, end, curl = one(length, rate, feed, lam, mode, 2026101400 + 7919 * rep + int(1000 * rate), start)
        print("  when the feed stops: squares per point %.2f (lowest %.2f), surplus per point %.2f, graph energy %.0f, per store %.2f"
              " | at the end: surplus per point %.2f, %s"
              % (hot["phi"], hot["low"], hot["curl"], hot["energy"], hot["store"], curl, line(end)))


if __name__ == "__main__":
    a = sys.argv[1:]
    main(int(a[0]), float(a[1]), int(a[2]) if len(a) > 2 else 40000, int(a[3]) if len(a) > 3 else 4,
         float(a[4]) if len(a) > 4 else 1.25, a[5] if len(a) > 5 else "all", a[6] if len(a) > 6 else "tube")

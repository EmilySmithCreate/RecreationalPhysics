"""Sandbox: if the burp's heat stays, does the tube come out wider? Usage:

    python sandbox/burp_heat_width.py LENGTH STORES [REPLICAS] [LAMBDA] [LEAK] [HOLD]

A sealed tube (4 x LENGTH points) with STORES stores of energy beside it and a spark of the wall's size in one of
them (energy is conserved, so what the burp releases can only go into the stores, and fewer stores means hotter).
Sealed for HOLD sweeps; then the stores are drained by the fraction LEAK every 100 sweeps until almost nothing is
left; then a short cold spell. Reads the end: exactly flat or not, its width if flat, and the most points at one
distance from a point (8 for a tube). STORES = 0 means one store per point, energy kept where it is released.
"""
import statistics
import sys
from collections import Counter
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "scripts"))
from graphity.cqg import NO_CAP, hamiltonian, run_chain, torus       # noqa: E402
from graphity.sealed import run_sealed_bath                          # noqa: E402
from read_endpoint_width import is_flat, width                       # noqa: E402
from read_open_shells import shells                                  # noqa: E402


def one(length, stores, lam, leak, hold, seed):
    adj, part = torus(length, 4, NO_CAP)
    n = adj.shape[0]
    side = np.flatnonzero(part == 0).astype(np.int64)
    by_vertex = stores == 0
    demons = np.zeros(n if by_vertex else stores, dtype=np.float64)
    spark = min(32.0 - 16.0 * lam, 64.0 - 40.0 * lam)
    demons[side[0] if by_vertex else 0] = spark
    start = hamiltonian(adj, lam) + spark
    s, _x, mean, _sum, _acc = run_sealed_bath(adj, side, demons, hold, seed, lam, NO_CAP, None, by_vertex)
    hot_phi, hot_mean, low_phi = s[-1] / n, mean[-1], s.min() / n
    drift = abs(hamiltonian(adj, lam) + demons.sum() - start)
    blocks = 0
    while demons.sum() > 0.5 and blocks < 4000:
        demons *= (1.0 - leak)
        run_sealed_bath(adj, side, demons, 100, -1, lam, NO_CAP, None, by_vertex)
        blocks += 1
    run_chain(adj, side, 1.0 / 0.05, 1999, 1, -1, lam, NO_CAP)
    flat = is_flat(adj)
    largest = statistics.median(max(shells(adj, int(v))) for v in np.linspace(0, n - 1, 8).astype(int))
    return dict(hot_phi=hot_phi, low_phi=low_phi, hot_mean=hot_mean, drift=drift, flat=flat,
                width=width(adj) if flat else 0, left=hamiltonian(adj, lam), largest=largest, drain=100 * blocks)


def main(length, stores, replicas=8, lam=1.25, leak=0.02, hold=20000, seed=2026101300):
    n = 4 * length
    rows = [one(length, stores, lam, leak, hold, seed + 104729 * r + 31 * stores + length) for r in range(replicas)]
    widths = Counter(r["width"] for r in rows)
    print("N=%d lambda=%.2f stores=%s (N/%.3g) leak=%.2f | squares per point at the end of the sealed spell %.2f to %.2f "
          "(lowest seen %.2f) | store mean %.2f | widths %s (0 = not exactly flat) | energy left %s | largest shell %s | "
          "max drift %.1e"
          % (n, lam, stores or "one per point", n / (stores or n / 2), leak, min(r["hot_phi"] for r in rows),
             max(r["hot_phi"] for r in rows), min(r["low_phi"] for r in rows),
             statistics.mean(r["hot_mean"] for r in rows), dict(sorted(widths.items())),
             " ".join("%g" % r["left"] for r in rows), " ".join("%g" % r["largest"] for r in rows),
             max(r["drift"] for r in rows)))


if __name__ == "__main__":
    a = sys.argv[1:]
    main(int(a[0]), int(a[1]), int(a[2]) if len(a) > 2 else 8, float(a[3]) if len(a) > 3 else 1.25,
         float(a[4]) if len(a) > 4 else 0.02, int(a[5]) if len(a) > 5 else 20000)

"""Sandbox look (exploratory; rule 16), 25 October 2026: the true barrier under the owner's pair tie, by T54's patch method.

The owner's decision (VISION Update 124): the tie returns for the twin pair, f = (0, 0, a, 0) per point by the number
of open directions d (a = 4 (lambda - 1); a broken point costs 0). The single-move walls (out/pair_tie_walls.txt) said
that from lambda of about 1.2 up the slab's wall (the second opening) is below the rod's (the first). Single moves are
not the barrier (T54); this computes the energy of a growing opened patch, exactly, for both openings:

  the second opening: the slab 4 x L x L with its curled direction opened over a k x k patch (T54's helix patch,
  scripts/exact_t54_patch.py, imported, unchanged);
  the first opening: the rod 4 x 4 x L with one curled direction (axis 0) opened in k whole rows along the open axis
  (every pair of neighbouring rings round axis 1 re-threaded by the same helix switch, in rows z = 0 .. k - 1).

dH(k) = E(patch) - E(start), E = H + the tie's total, under three tables: none, "all at the last" (0, a, 2a, 0), and the
pair tie (0, 0, a, 0). Read: whether dH rises then falls (a critical patch, its peak the barrier), and the peak.
"""
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "scripts"))
from graphity.cqg_d import _switch, hamiltonian, is_valid, torus      # noqa: E402
from graphity.dimension import local_dimension_d                       # noqa: E402
from graphity.sealed_tie_d import table_total                          # noqa: E402
from exact_t54_patch import patch, verdict                             # noqa: E402


def tables(lam):
    a = 4.0 * (lam - 1.0)
    return {"none": np.zeros(4), "last": np.array([0.0, a, 2 * a, 0.0]), "pair": np.array([0.0, 0.0, a, 0.0])}


def energy(adj, lam, tab):
    return float(hamiltonian(adj, lam)) + float(table_total(adj, tab))


def rod_index(length, a, x, z):
    return ((a % 4) * 4 + (x % 4)) * length + (z % length)


def rod_patch(adj0, length, k):
    adj = adj0.copy()
    for z in range(k):
        for x in range(4):
            u1, v1 = rod_index(length, 0, x + 1, z), rod_index(length, 1, x + 1, z)
            u2, v2 = rod_index(length, 3, x, z), rod_index(length, 2, x, z)
            _switch(adj, u1, v1, u2, v2)
    return adj


def report(name, start, states, lam):
    for tname, tab in tables(lam).items():
        e0 = energy(start, lam, tab)
        dhs = [energy(s, lam, tab) - e0 for s in states]
        peak = max(dhs)
        print(f"  {name:4s} lam {lam:.2f} {tname:4s}: {verdict(dhs):15s} peak {peak:7.1f} at k = {int(np.argmax(dhs)) + 1:2d}; "
              f"dH(k) = {', '.join(f'{x:.0f}' for x in dhs)}")


def main():
    L = 12
    slab0, _ = torus([4, L, L])
    rod0, _ = torus([4, 4, 3 * L // 2])
    slabs = [patch(slab0, L, k)[0] for k in range(1, L)]
    rods = [rod_patch(rod0, 3 * L // 2, k) for k in range(1, 3 * L // 2 + 1)]
    full = rods[-1]
    d = local_dimension_d(full)
    print(f"check: rod with every row opened: valid {is_valid(full)}, points at d = 0..3 {np.bincount(d, minlength=4)[:4].tolist()}, "
          f"broken {int((d > 3).sum())}; slab patches valid {all(is_valid(s) for s in slabs)}; rod patches valid "
          f"{all(is_valid(s) for s in rods)}")
    for lam in (1.15, 1.20, 1.25, 1.40):
        print(f"lambda = {lam}")
        report("rod", rod0, rods, lam)
        report("slab", slab0, slabs, lam)


if __name__ == "__main__":
    main()

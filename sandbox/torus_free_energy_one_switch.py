"""Sandbox look, 23 October 2026 (rule 16: a look; it can kill, not crown). At lambda = 1 every lattice torus at one N
ties in energy and (the look of the same afternoon) in its count of renamings. What can still tell them apart at
finite coupling is the free energy, through the excitations each torus admits. This enumerates every single switch
of the chain's move set out of each torus (the kernel's proposal: edges (u1,v1), (u2,v2) with u1, u2 on side 0,
switched to (u1,v2), (u2,v1); kept only if the graph stays valid under the hard-core rule, no cap), records its
energy cost dH at lambda = 1, and compares the low-temperature free energies

    F(g) = -g ln ( 1 + sum over distinct switches of exp(-dH / g) ),

the ground state plus its one-switch neighbours. This is the first term of the expansion, not the full free energy:
a torus's two-switch and deeper excitations are not counted, and it says nothing about whether the chain can move
between tori. Reported per torus: the number of valid switches by cost, and F(g) at several g; per N: F(tube) minus
F(each other torus), negative where the tube is favored. Sizes 144, 160, 192 (the N with several lattice tori).

The owner's prediction, recorded in sandbox/NOTEBOOK.md before this ran: the tube wins at every finite coupling at
lambda = 1.

Usage: python3 sandbox/torus_free_energy_one_switch.py > sandbox/out/torus_free_energy_one_switch_2026-10-23.txt
"""
import math
import os
import sys
from collections import Counter

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(HERE), "src"))
from graphity import cqg  # noqa: E402
from graphity.cqg import _switch, has_edge, hamiltonian, is_valid  # noqa: E402

SIZES = (144, 160, 192)
LAM = 1.0
COUPLINGS = (0.5, 1.0, 1.5, 2.0, 3.0, 5.0, 10.0)


def tori_of(n):
    out = []
    for a in range(4, int(math.isqrt(n)) + 1, 2):
        if n % a == 0 and (n // a) % 2 == 0 and n // a >= 4:
            out.append((a, n // a))
    return out


def switches(adj, part):
    """Every distinct valid single switch out of `adj` with its energy cost at LAM."""
    n = adj.shape[0]
    side0 = [u for u in range(n) if part[u] == 0]
    h0 = hamiltonian(adj, LAM)
    edges = [(u, int(v)) for u in side0 for v in adj[u]]          # 2N edges, each once (u on side 0)
    costs = Counter()
    tried = 0
    for i in range(len(edges)):
        u1, v1 = edges[i]
        for j in range(i + 1, len(edges)):
            u2, v2 = edges[j]
            if u1 == u2 or v1 == v2 or has_edge(adj, u1, v2) or has_edge(adj, u2, v1):
                continue
            tried += 1
            _switch(adj, u1, v1, u2, v2)
            if is_valid(adj, cqg.NO_CAP):
                costs[int(round(hamiltonian(adj, LAM) - h0))] += 1
            _switch(adj, u1, v2, u2, v1)                            # exact reverse
    assert hamiltonian(adj, LAM) == h0
    return costs, tried


def free_energy(costs, g):
    z = 1.0 + sum(k * math.exp(-dh / g) for dh, k in costs.items())
    return -g * math.log(z)


def main():
    print("Low-temperature free energy of the lattice tori at one N, lambda = %.1f, from every single switch (exact; sandbox)" % LAM)
    for n in SIZES:
        results = []
        for a, b in tori_of(n):
            adj, part = cqg.torus(a, b, cap=cqg.NO_CAP)
            costs, tried = switches(adj, part)
            results.append(((a, b), costs, tried))
        print("\nN = %d" % n)
        print("  %-9s %8s %8s   %s" % ("torus", "pairs", "valid", "valid switches by cost dH (count at each cost)"))
        for (a, b), costs, tried in results:
            print("  %-9s %8d %8d   %s" % ("%d x %d" % (a, b), tried, sum(costs.values()),
                                           ", ".join("%+d: %d" % (dh, k) for dh, k in sorted(costs.items()))))
        print("  %-9s " % "F(g)" + " ".join("%9s" % ("g=%.1f" % g) for g in COUPLINGS))
        for (a, b), costs, _ in results:
            print("  %-9s " % ("%d x %d" % (a, b)) + " ".join("%9.3f" % free_energy(costs, g) for g in COUPLINGS))
        tube = next(r for r in results if r[0][0] == 4)
        print("  F(tube) - F(other), negative where the tube is favored:")
        for (a, b), costs, _ in results:
            if (a, b) == tube[0]:
                continue
            print("  %-9s " % ("vs %d x %d" % (a, b)) + " ".join("%9.3f" % (free_energy(tube[1], g) - free_energy(costs, g)) for g in COUPLINGS))


if __name__ == "__main__":
    main()

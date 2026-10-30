"""A look (sandbox lane; the owner's rule and picture of 30 October). Two exact checks, expectations first.

(1) Her picture: a whole turn fits the flat lattice when three versions of spacetime combine into one, "3 planes
    intersecting". Check: enumerate every closed loop of three box diagonals from the origin (all ordered triples of the 24
    box steps summing to zero) and ask whether each has exactly one diagonal lying long (the 2) along each axis.
    Expectation (ours, exact by the sum rule: each axis must receive 2 - 1 - 1 or -2 + 1 + 1): every triangle does, so a
    whole turn of three thirds is one third per axis.
(2) Her rule: like twists repel; a charge of 2 or more on one loop breaks into two particles unless bound. Under the
    working term E4 (elastic + mismatch) charge 2 on six diagonals costs exactly two electrons. The simplest repulsion
    piece (ours): a per-loop cost eps_q T^2 in the loop's net twist T, the self-energy of a charge. With it, E(one loop,
    charge 2) - 2 E(electron) = eps_q (4 - 2) = 2 eps_q > 0 for any eps_q > 0, so charge 2 breaks; the electron's own
    cost rises by eps_q. Also the per-loop periodic piece she described (whole charge free, fractions costing),
    eps_p (1 - cos 2 pi T): zero for the electron and for charge 2 alike, so it confines thirds and does not split
    charge 2; the two pieces do different jobs. Expectation: as stated; the table says it in numbers.
Crowns nothing; which pieces to add is hers.
"""
import math
from fractions import Fraction
from itertools import product

import numpy as np

from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from graphity.twist import BOX_STEPS, THIRD, Loop, twist_energy  # noqa: E402

if __name__ == "__main__":
    steps = sorted(BOX_STEPS)
    tri = [(a, b, c) for a in steps for b in steps for c in steps if tuple(np.add(np.add(a, b), c)) == (0, 0, 0)]
    one_per_axis = sum(1 for t in tri if sorted(int(np.argmax(np.abs(s))) for s in t) == [0, 1, 2])
    print("(1) closed triangles of box diagonals from a point: %d ordered; with one diagonal long along each axis: %d" % (len(tri), one_per_axis))
    e = twist_energy(Loop(8, (0, 0, 0), [(1, 1, 2), (1, -2, -1), (-2, 1, -1)], [THIRD] * 3), eps=1.0, eps_w=0.0)
    hexa = [(1, 1, 2), (1, 2, -1), (-2, 1, -1), (-1, -1, -2), (-1, -2, 1), (2, -1, 1)]   # a simple planar hexagon of box diagonals
    two = twist_energy(Loop(8, (0, 0, 0), hexa, [THIRD] * 6), eps=1.0, eps_w=0.0)
    print("(2) E4 alone: electron %.3f; one loop of six thirds (charge 2) %.3f; two electrons %.3f; difference %.3f" % (e, two, 2 * e, two - 2 * e))
    for eq in (0.25, 1.0):
        print("    with eps_q T^2 per loop at eps_q = %.2f: electron %.3f; charge-2 loop %.3f; two electrons %.3f; the loop breaks by %.3f" % (
            eq, e + eq, two + 4 * eq, 2 * (e + eq), (two + 4 * eq) - 2 * (e + eq)))
    for ep in (1.0,):
        pf = lambda T: ep * (1 - math.cos(2 * math.pi * T))
        print("    per-loop periodic at eps_p = %.1f: a lone third costs %.3f, two thirds %.3f, a whole charge %.3f, charge 2 %.3f (confines thirds; does not split)" % (
            ep, pf(1 / 3), pf(2 / 3), pf(1), pf(2)))
    print("Crowns nothing.")

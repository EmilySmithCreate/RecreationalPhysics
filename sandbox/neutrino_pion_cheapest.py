"""A look (sandbox lane; the owner's instruction of 30 October: "predict before computing: the cheapest loop for the neutrino
and for the pion's two loops under the same term"). Predictions first, written before the enumeration ran.

Term: E4 per loop, elastic + mismatch, eps = 1, on a flat loop (writhe 0); twists in thirds on box diagonals, in halves on
face diagonals (the sheet); the loop must hold some twist where spin is needed (the neutrino).

Predictions (ours, arithmetic, written before running):
  neutrino as built (box, net 0, twist present): the triangle (1/3, -1/3, 0) costs 2/9 + 6/9 = 8/9; a square (1/3, 0, -1/3, 0)
    costs 2/9 + 4/9 = 6/9, and every longer loop with the two thirds separated by zeros costs the same 6/9. So the cheapest
    loop is NOT the triangle: it is any loop of four or more, degenerate in length, 6/9. No size is selected.
  her dark neutrino (face diagonals, halves, net 0): triangle (1/2, -1/2, 0) costs 1/2 + 3/2 = 2; square (1/2, 0, -1/2, 0)
    costs 1/2 + 1 = 3/2, and longer loops the same 3/2. Cheapest 3/2 at four or more; dearer than the box one at equal eps.
  pion loop with net 1/3: (1/3, 0, 0) costs 1/9 + 2/9 = 3/9 on the triangle and the same on every longer loop. Degenerate.
  pion loop with net 2/3: (1/3, 1/3, 0) costs 2/9 + 2/9 = 4/9 on the triangle and the same on every longer loop; (2/3, 0, 0)
    costs 12/9. Degenerate in length.
  So only the electron (a whole charge in thirds) has a unique cheapest length; every fractional or zero-net loop is
    indifferent to length above a floor (3 for the pion's loops, 4 for the neutrino).
Also checked: whether a closed triangle of face diagonals exists (one per coordinate plane), for her Mobius-like picture.
Crowns nothing.
"""
from fractions import Fraction as F
from itertools import product

import numpy as np


def cheapest(n, inc, net, need_twist):
    vals = [F(k, inc) for k in range(-inc, inc + 1)]
    best = None
    for taus in product(vals, repeat=n):
        if sum(taus) != net or (need_twist and not any(taus)):
            continue
        e = sum(t * t for t in taus) + sum((taus[(i + 1) % n] - taus[i]) ** 2 for i in range(n))
        if best is None or e < best[0]:
            best = (e, taus)
    return best


if __name__ == "__main__":
    cases = [("neutrino, box thirds, net 0, twist present", 3, F(0), True),
             ("her dark neutrino, face halves, net 0, twist present", 2, F(0), True),
             ("pion loop, box thirds, net 1/3", 3, F(1, 3), False),
             ("pion loop, box thirds, net 2/3", 3, F(2, 3), False)]
    for name, inc, net, need in cases:
        print(name)
        for n in range(3, 8):
            e, taus = cheapest(n, inc, net, need)
            print("  n = %d: min E4 = %s  example %s" % (n, e, tuple(str(t) for t in taus)))
    face = [s for s in product((-1, 0, 1), repeat=3) if sorted(map(abs, s)) == [0, 1, 1]]
    tri = [(a, b, c) for a in face for b in face for c in face if tuple(np.add(np.add(a, b), c)) == (0, 0, 0)]
    per_plane = sum(1 for t in tri if sorted(int(np.argmin(np.abs(s))) for s in t) == [0, 1, 2])
    print("closed triangles of face diagonals from a point: %d ordered; with one diagonal in each coordinate plane: %d" % (len(tri), per_plane))
    print("Crowns nothing.")

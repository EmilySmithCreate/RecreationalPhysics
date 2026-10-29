"""A look (sandbox lane; the owner's stability rule of 29 October, about 12:05 UTC): twists of one direction must be spread
equally round the loop, since they repel each other somewhat; 'two thirds, then a gluon, then a third, then a gluon' is not
symmetrical and is out. For a loop of three thirds (the electron's charge) that means the three twisted short diagonals sit
at equal spacing, so a loop with gluons (long diagonals) between them has the pattern S L^k S L^k S L^k: length 3(k + 1),
by count 3, 6, 9, ...; by length 3 + 3k sqrt 3.

This enumerates the k = 1 pattern, S L S L S L (six steps, short (1,1,2) and long (1,1,4) alternating), with the first
short step fixed to (1,1,2) (every other choice is a rotation or reflection of the lattice), closure required, and
reports how many close, how many are simple, and their coil range. 24^5 = 8 million sequences with pruning.

WRITTEN BEFORE COMPUTING (ours): such loops exist (the three longs sum to minus the three shorts, and there is room in
24^5 choices), in the hundreds, with coils from 0 to about 1. If none closes, her rule leaves the electron alone below
the nine-step pattern, which would be read next. Kills, if it finds loops: nothing of hers; it kills "equal spacing has
no closed loop at six". Crowns nothing: the rule is hers and put in, and the muon's gap is not made by it (6, 9, 12 ...
remain).
"""
from itertools import permutations, product

import numpy as np

from long_diagonal_mass import is_simple, writhe, steps_of

SHORT = steps_of((1, 1, 2))
LONG = steps_of((1, 1, 4))
PATTERN = [SHORT, LONG, SHORT, LONG, SHORT, LONG]
first = (1, 1, 2)
found = []


def rec(seq, pos, depth):
    if depth == 6:
        if pos == (0, 0, 0):
            found.append(list(seq))
        return
    left = 6 - depth
    reach = sum(6 if PATTERN[d] is LONG else 4 for d in range(depth, 6))
    if abs(pos[0]) + abs(pos[1]) + abs(pos[2]) > reach:
        return
    for v in PATTERN[depth]:
        if depth > 0 and v == tuple(-c for c in seq[-1]):
            continue
        rec(seq + [v], (pos[0] + v[0], pos[1] + v[1], pos[2] + v[2]), depth + 1)


rec([first], first, 1)
print("S L S L S L loops closing with the first short fixed to (1,1,2):", len(found))
simple = []
for seq in found:
    V = np.array([np.zeros(3)] + list(np.cumsum(np.array(seq[:-1], dtype=float), axis=0)))
    if is_simple(V):
        simple.append(abs(writhe(V)))
print("simple (no self-crossing):", len(simple))
if simple:
    print("coil: min %.3f, max %.3f; whole coils (within 0.0005 of 1): %d" % (min(simple), max(simple),
          sum(1 for w in simple if abs(w - 1) < 0.0005)))
print("mass by count 6 (1.02 MeV at the electron's unit); by length 3 + 3 sqrt 3 = %.3f (%.2f MeV)" % (3 + 3 * np.sqrt(3), (3 + 3 * np.sqrt(3)) * 0.1703))

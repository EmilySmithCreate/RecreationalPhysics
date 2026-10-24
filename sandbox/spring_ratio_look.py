"""Sandbox look, 22 October 2026 (rule 16: a look; rule 13's "count the arbitrary combinations" step).

The owner's question: could the dark-to-ordinary matter ratio (5.36, Planck 2018, to verify) come out as the ratio of
the energy stored in two loops of different lengths on the lattice (edge loops against diagonal loops), "two springs of
different lengths folded into a circle and a smaller circle"?

Before any such formula is written, rule 13 asks how many arbitrary combinations of the available ingredients would
land on the target anyway. This script counts them. Ingredients, all exact on the cubic lattice: closed loops whose
steps are lattice edges (length 1), face diagonals (sqrt 2) or body diagonals (sqrt 3); a loop's length is a sum of
such steps (even counts of edges and face diagonals close; body diagonals in even counts). Energy laws tried: E
proportional to L, L^2, L^3, 1/L, 1/L^2 (curvature of a circle of circumference L), and L times a small integer count
(several loops per unit). The ratio of two such energies is compared with the target and with ten other targets drawn
at random in the same range, to show the hit rate a number of this kind has by chance.

Usage: python3 sandbox/spring_ratio_look.py
"""
import itertools
import math
import random

TARGET = 5.36
TOL = 0.02                                       # within 2 %

# loop lengths: a edges + b face diagonals + c body diagonals, closed on the lattice (parity), total steps 3 to 12
lengths = {}
for a in range(0, 13):
    for b in range(0, 13):
        for c in range(0, 7):
            n = a + b + c
            if n < 3 or n > 12:
                continue
            if (a % 2) or (c % 2):               # edge steps and body-diagonal steps must pair up to close
                continue
            if a == 0 and b == 0:
                continue
            if b % 2 == 1 and a == 0 and c == 0:
                if b < 3:
                    continue                     # the triangle of three face diagonals is the smallest odd ring
            L = a + b * math.sqrt(2) + c * math.sqrt(3)
            lengths[(a, b, c)] = L
Ls = sorted(set(round(v, 9) for v in lengths.values()))
laws = {"L": lambda L: L, "L^2": lambda L: L ** 2, "L^3": lambda L: L ** 3, "1/L": lambda L: 1 / L, "1/L^2": lambda L: 1 / L ** 2}
counts = (1, 2, 3, 4, 6, 8)                      # several loops per unit, or per cube

def hits(target):
    found = []
    for (n1, f1), (n2, f2) in itertools.product(laws.items(), repeat=2):
        for L1, L2 in itertools.product(Ls, repeat=2):
            for k1, k2 in itertools.product(counts, repeat=2):
                r = (k1 * f1(L1)) / (k2 * f2(L2))
                if abs(r / target - 1) < TOL:
                    found.append((n1, L1, k1, n2, L2, k2, r))
    return found

random.seed(13)
print("distinct loop lengths on the lattice (3 to 12 steps of edges, face and body diagonals):", len(Ls))
h = hits(TARGET)
print("combinations within 2 %% of %.2f: %d" % (TARGET, len(h)))
print("a few of them:")
for row in h[:8]:
    print("   %s(%.3f) x %d  /  %s(%.3f) x %d  = %.3f" % row)
others = [round(random.uniform(2, 12), 2) for _ in range(10)]
print("the same count for ten random targets in the range 2 to 12:")
for t in others:
    print("   target %.2f: %d combinations" % (t, len(hits(t))))

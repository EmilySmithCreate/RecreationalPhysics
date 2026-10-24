"""Sandbox look, 23 October 2026 (rule 16: a look). The owner's picture: one square is a coin whose two diagonals, one
joining each kind's opposite corners, are matter and antimatter, "so energy does both at the same time". Exact
arithmetic on one square with sides of length 1 (stage B's lengths; the stiff toy has none):

  * Euler's quadrilateral theorem: for any four points A, B, C, D, the four sides squared add up to the two diagonals
    squared plus four times the squared distance m between the diagonals' midpoints:
        |AB|^2 + |BC|^2 + |CD|^2 + |DA|^2 = |AC|^2 + |BD|^2 + 4 m^2.
  * So with every side 1: d1^2 + d2^2 = 4 - 4 m^2. Flat (a rhombus, m = 0): d1^2 + d2^2 = 4 exactly, one diagonal
    shortening by as much as the other lengthens (in squared length). Folded out of its plane: m > 0, both shorten.

Checked numerically on random quadrilaterals, flat rhombi and folded squares.

Usage: python3 sandbox/square_diagonals_check.py
"""
import numpy as np

rng = np.random.default_rng(20261023)


def sq(v):
    return float(np.dot(v, v))


worst = 0.0
for _ in range(10000):
    a, b, c, d = rng.normal(size=(4, 3))
    sides = sq(b - a) + sq(c - b) + sq(d - c) + sq(a - d)
    m = (a + c) / 2 - (b + d) / 2
    worst = max(worst, abs(sides - (sq(c - a) + sq(d - b) + 4 * sq(m))))
print("Euler's quadrilateral identity on 10,000 random quadrilaterals: largest error %.1e" % worst)

print("flat rhombus of side 1 (m = 0): angle, short diagonal, long diagonal, d1^2 + d2^2")
for deg in (90, 80, 70, 60):
    t = np.radians(deg)
    a, b = np.array([0.0, 0, 0]), np.array([1.0, 0, 0])
    d = np.array([np.cos(t), np.sin(t), 0])
    c = b + d
    d1, d2 = np.sqrt(sq(c - a)), np.sqrt(sq(d - b))
    print("  %3d deg  %.4f  %.4f  %.4f" % (deg, min(d1, d2), max(d1, d2), d1 * d1 + d2 * d2))

print("square of side 1 folded along a diagonal by angle f: d1 (the fold line), d2 (across), m, d1^2 + d2^2")
for fdeg in (0, 20, 40, 60):
    f = np.radians(fdeg)
    a, c = np.array([0.0, 0, 0]), np.array([np.sqrt(2), 0, 0])
    h = np.sqrt(2) / 2
    b = np.array([h, h * np.cos(f / 2), h * np.sin(f / 2)])
    d = np.array([h, -h * np.cos(f / 2), h * np.sin(f / 2)])
    m = np.sqrt(sq((a + c) / 2 - (b + d) / 2))
    d1, d2 = np.sqrt(sq(c - a)), np.sqrt(sq(d - b))
    print("  %3d deg  %.4f  %.4f  %.4f  %.4f" % (fdeg, d1, d2, m, d1 * d1 + d2 * d2))

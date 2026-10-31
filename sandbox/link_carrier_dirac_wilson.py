"""A look (sandbox lane): Dirac's whole-number rule and Wilson's lattice field on the toy's flat 3D torus.

The owner's decision of 28 October: electromagnetism gets a carrier on the links. The published form is Wilson's
(1974; general knowledge, not read): an angle theta_e on each link, the flux through a square the sum of its four
angles, and charges coupling to a closed loop through exp(i q sum theta). Dirac (1931, read in part): the phase round
a closed loop is 2 pi times a whole number plus the flux through it, so charges must be whole multiples of one unit.

What is checked here, all exact arithmetic on the L x L x L torus of `graphity.cqg_d.torus` (six links a point):
  1. DeGrand-Toussaint: with every square's flux reduced to (-pi, pi], the flux out of each cube is 2 pi x an integer,
     the monopole number. Random angles, several seeds: the integer always appears and the count is reported.
  2. A charge q couples to a loop through exp(i q sum theta). Shifting one link's angle by 2 pi (the same field, named
     differently) leaves the coupling alone only when q is whole. Thirds and halves fail; the proton's three thirds
     (2/3 + 2/3 - 1/3 = 1) pass as one loop.
  3. A carrier that can only hold N angles (2 pi k / N) cannot tell charge q from charge q + N. With N = 2 (the owner's
     180-degree curl per link) charge +1 and -1 are the same: such a carrier cannot tell matter from antimatter, or
     attraction from repulsion.
  4. The owner's lengths: hypotenuse of sqrt 3 and 1 is 2 only at a right angle; on the lattice a cube's body diagonal
     plus one edge is the (1, 1, 2) box diagonal, sqrt 6.

Nothing here runs the toy's chain. The field is put on the links by hand; the toy's curl is not used.
"""
import sys
from fractions import Fraction
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from graphity.cqg_d import torus  # noqa: E402

L = 6
adj, part = torus((L, L, L))
N = L ** 3
coords = np.array(np.unravel_index(np.arange(N), (L, L, L))).T
strides = np.array([L * L, L, 1])


def idx(c):
    return int(np.dot(np.mod(c, L), strides))


# links: one per (point, +axis); angle lives on the oriented link, minus on the reverse
links = {}
for i, c in enumerate(coords):
    for a in range(3):
        step = np.zeros(3, dtype=int); step[a] = 1
        links[(i, a)] = idx(c + step)
assert len(links) == 3 * N == adj.size // 2, "link count must match the toy's wiring"
for (i, a), j in links.items():
    assert j in adj[i], "every link of the field is a link of the toy's torus"


def wrap(x):
    return (x + np.pi) % (2 * np.pi) - np.pi


def plaquette(theta, i, a, b):
    """Flux through the square at point i spanned by +a then +b, reduced to (-pi, pi]."""
    c = coords[i]
    ea = np.zeros(3, dtype=int); ea[a] = 1
    eb = np.zeros(3, dtype=int); eb[b] = 1
    s = theta[(i, a)] + theta[(idx(c + ea), b)] - theta[(idx(c + eb), a)] - theta[(i, b)]
    return wrap(s)


def monopoles(theta):
    """DeGrand-Toussaint monopole number in each cube: flux out over its six faces / 2 pi."""
    out = np.empty(N)
    for i, c in enumerate(coords):
        total = 0.0
        for a, b, n in ((1, 2, 0), (2, 0, 1), (0, 1, 2)):      # faces normal to axis n, right-handed
            en = np.zeros(3, dtype=int); en[n] = 1
            total += plaquette(theta, idx(c + en), a, b) - plaquette(theta, i, a, b)
        out[i] = total / (2 * np.pi)
    return out


print("1. DeGrand-Toussaint on the %d-point torus, random angles" % N)
for seed in range(4):
    rng = np.random.default_rng(seed)
    theta = {k: float(rng.uniform(-np.pi, np.pi)) for k in links}
    m = monopoles(theta)
    assert np.allclose(m, np.round(m), atol=1e-9), "flux out of a cube must be 2 pi x integer"
    mi = np.round(m).astype(int)
    print("   seed %d: monopole numbers %s, total %+d (must be 0 on a torus)" % (
        seed, {int(a): int(b) for a, b in zip(*np.unique(mi, return_counts=True))}, mi.sum()))
    assert mi.sum() == 0

print("\n2. Charge q round a closed loop under a 2 pi renaming of one link")
rng = np.random.default_rng(7)
theta = {k: float(rng.uniform(-np.pi, np.pi)) for k in links}
loop = [(0, 0), (idx(coords[0] + [1, 0, 0]), 1)]           # two links of the square at the origin, used forward
back = [(idx(coords[0] + [0, 1, 0]), 0), (0, 1)]          # the other two, used backward
hol = sum(theta[k] for k in loop) - sum(theta[k] for k in back)
for q in (Fraction(1, 3), Fraction(1, 2), Fraction(2, 3), Fraction(1), Fraction(5, 3), Fraction(2)):
    w0 = np.exp(1j * float(q) * hol)
    w1 = np.exp(1j * float(q) * (hol + 2 * np.pi))
    same = abs(w0 - w1) < 1e-12
    print("   q = %-4s %s" % (q, "same coupling: allowed" if same else "coupling changes by exp(2 pi i q): not allowed alone"))
thirds = [Fraction(2, 3), Fraction(2, 3), Fraction(-1, 3)]
qt = sum(thirds)
print("   three thirds on one loop, %s -> q = %s: %s" % (thirds, qt, "allowed" if qt.denominator == 1 else "not"))

print("\n3. A carrier with N angles: which charges it can tell apart")
for Nang in (2, 3, 6):
    # every holonomy the carrier can produce round a loop is 2 pi k / N; two charges are the same to the carrier
    # when their couplings agree for every k
    classes = {}
    for q in range(-3, 4):
        key = tuple((round(np.cos(2 * np.pi * q * k / Nang), 9), round(np.sin(2 * np.pi * q * k / Nang), 9))
                    for k in range(Nang))
        classes.setdefault(key, []).append(q)
    print("   N = %d (%3d degrees a step): charges the carrier cannot tell apart %s" % (
        Nang, 360 // Nang, sorted(classes.values())))

print("\n4. Lengths")
print("   hypotenuse of sqrt 3 and 1 at a right angle: %.3f" % np.hypot(np.sqrt(3), 1))
print("   on the lattice, body diagonal (1,1,1) plus edge (0,0,1) = (1,1,2): length %.3f, links walked 4" % np.sqrt(6))
print("   face diagonal (1,1,0): %.3f, links walked 2; body diagonal (1,1,1): %.3f, links walked 3" % (np.sqrt(2), np.sqrt(3)))
print("   speed if each takes its link count in ticks: face %.3f, body %.3f, box %.3f of the axis speed" % (
    np.sqrt(2) / 2, np.sqrt(3) / 3, np.sqrt(6) / 4))
print("   if the box diagonal takes 3 ticks: %.3f" % (np.sqrt(6) / 3))

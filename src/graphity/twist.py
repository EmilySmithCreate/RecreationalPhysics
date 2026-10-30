"""The twisted-diagonal state: the owner's particles as loops of diagonals on the cubic torus, with twist, curl and spin,
and the readers of her rules (docs/design/twisted_diagonals_build_2026-10-30.md; the standing sheet
docs/design/twist_curl_rules_current.md). Her Option B: particles are loops of twisted diagonals built as variables; the
wiring's knots are the scrap. Nothing here is derived; the rules are put in and read back exactly.

The lattice: points of an L x L x L torus, coloured by the parity of x + y + z. A box diagonal is a signed permutation of
(1, 1, 2) (24 steps, sqrt 6, same colour); a long diagonal (1, 1, 2m), m >= 2 (holds curl, no twist); a face diagonal a
signed permutation of (1, 1, 0) (12 steps, sqrt 2, dark twist in halves). Body diagonals (1, 1, 1) change colour and are
not part of this state.

A Loop: closed on the torus, one step kind, twist on each diagonal (thirds on box, halves on face, zero on long), an
integer curl >= 1, and a spin in {-1/2, 0, +1/2} that may be non-zero only if some twist is present (her rule of
30 October: spin needs twist present, not net twist). A Particle is a named set of loops. Readers: charge = sum of twist;
spin = |sum of loop spins|; mass_count = number of looped diagonals (a long diagonal counts one); parts = (L, n, tau+, T,
s, C); net_twist over a set of particles, the quantity pair creation conserves.

Twist values are kept as Fractions so that thirds and halves are exact.
"""
from dataclasses import dataclass, field
from fractions import Fraction
from itertools import permutations, product

import numpy as np

THIRD, HALF = Fraction(1, 3), Fraction(1, 2)


def _signed_perms(base):
    out = set()
    for p in permutations(base):
        for s in product((1, -1), repeat=3):
            out.add(tuple(int(a * b) for a, b in zip(p, s)))
    return out


BOX_STEPS = _signed_perms((1, 1, 2))
FACE_STEPS = _signed_perms((1, 1, 0))


def step_kind(delta):
    """'box', 'face', 'long' (a (1, 1, 2m) step with m >= 2) or None."""
    d = tuple(int(x) for x in delta)
    if d in BOX_STEPS:
        return "box"
    if d in FACE_STEPS:
        return "face"
    a = sorted(abs(x) for x in d)
    if a[0] == 1 and a[1] == 1 and a[2] >= 4 and a[2] % 2 == 0:
        return "long"
    return None


def colour(point):
    return "black" if sum(int(x) for x in point) % 2 == 0 else "white"


@dataclass
class Loop:
    """points: the loop's points in order (the step from the last back to the first closes it); steps are given as
    displacements so that the torus wrap is explicit. twists: one Fraction per step. curl: integer >= 1. spin: Fraction."""
    L: int
    start: tuple
    steps: list
    twists: list
    curl: int = 1
    spin: Fraction = Fraction(0)
    kind: str = field(init=False)
    points: list = field(init=False)

    def __post_init__(self):
        kinds = {step_kind(s) for s in self.steps}
        if None in kinds:
            raise ValueError("a step is not a box, face or long diagonal: %s" % [s for s in self.steps if step_kind(s) is None])
        if len(kinds) != 1:
            raise ValueError("a loop uses one kind of diagonal; got %s" % sorted(kinds))
        self.kind = kinds.pop()
        if len(self.twists) != len(self.steps):
            raise ValueError("one twist per diagonal")
        total = np.sum(np.array(self.steps, dtype=int), axis=0)
        if any(int(t) % self.L != 0 for t in total):
            raise ValueError("the loop does not close on the torus: total displacement %s" % (tuple(int(t) for t in total),))
        inc = {"box": THIRD, "face": HALF, "long": None}[self.kind]
        for t in self.twists:
            t = Fraction(t)
            if inc is None and t != 0:
                raise ValueError("a long diagonal holds curl and no twist")
            if inc is not None and (t / inc).denominator != 1:
                raise ValueError("twist %s is not a multiple of %s on a %s diagonal" % (t, inc, self.kind))
        self.twists = [Fraction(t) for t in self.twists]
        if int(self.curl) < 1 or int(self.curl) != self.curl:
            raise ValueError("one curl of energy per loop at least; curl must be a positive integer")
        self.spin = Fraction(self.spin)
        if self.spin not in (Fraction(0), HALF, -HALF):
            raise ValueError("a loop's spin is -1/2, 0 or +1/2")
        if self.spin != 0 and all(t == 0 for t in self.twists):
            raise ValueError("spin needs twist present (her rule of 30 October)")
        p = np.array(self.start, dtype=int)
        pts = [tuple(int(x) % self.L for x in p)]
        for s in self.steps[:-1]:
            p = p + np.array(s, dtype=int)
            pts.append(tuple(int(x) % self.L for x in p))
        self.points = pts

    @property
    def colour(self):
        return colour(self.start)

    @property
    def net_twist(self):
        return sum(self.twists, Fraction(0))

    @property
    def twist_present(self):
        return sum((abs(t) for t in self.twists), Fraction(0))

    @property
    def mass_count(self):
        return len(self.steps)


@dataclass
class Particle:
    name: str
    loops: list

    @property
    def charge(self):
        return sum((lp.net_twist for lp in self.loops), Fraction(0))

    @property
    def spin(self):
        return abs(sum((lp.spin for lp in self.loops), Fraction(0)))

    @property
    def mass_count(self):
        return sum(lp.mass_count for lp in self.loops)

    @property
    def parts(self):
        return dict(L=len(self.loops), n=self.mass_count,
                    tau_plus=sum((lp.twist_present for lp in self.loops), Fraction(0)),
                    T=self.charge, s=sum((lp.spin for lp in self.loops), Fraction(0)),
                    C=sum(lp.curl for lp in self.loops))

    def check_whole_charge(self):
        if self.charge.denominator != 1:
            raise ValueError("%s: a particle on its own has whole charge; got %s" % (self.name, self.charge))
        return True


def net_twist(particles):
    return sum((p.charge for p in particles), Fraction(0))


# ---------------------------------------------------------------- the sheet's hand-built loops

TRIANGLE = [(1, 1, 2), (1, -2, -1), (-2, 1, -1)]          # three box diagonals that close: a flat triangle (exact)


def triangle(L, start=(0, 0, 0), twists=(-THIRD, -THIRD, -THIRD), spin=HALF, curl=1):
    return Loop(L, start, list(TRIANGLE), list(twists), curl=curl, spin=spin)


def mirror(loop):
    """The same loop with every twist and its spin reversed: the anti-particle's loop (pairs: +theta with -theta)."""
    return Loop(loop.L, loop.start, list(loop.steps), [-t for t in loop.twists], curl=loop.curl, spin=-loop.spin)

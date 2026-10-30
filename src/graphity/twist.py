"""The twisted-diagonal state: the owner's particles as loops of diagonals on the cubic torus, with twist, curl and spin,
and the readers of her rules (docs/design/twisted_diagonals_build_2026-10-30.md; the standing sheet
docs/design/twist_curl_rules_current.md). Her Option B: particles are loops of twisted diagonals built as variables; the
wiring's knots are the scrap. Nothing here is derived; the rules are put in and read back exactly.

The lattice: points of an L x L x L torus, coloured by the parity of x + y + z. A box diagonal is a signed permutation of
(1, 1, 2) (24 steps, sqrt 6, same colour); a long diagonal (1, 1, 2m), m >= 2 (holds curl, no twist); a face diagonal a
signed permutation of (1, 1, 0) (12 steps, sqrt 2, dark twist in halves). Body diagonals (1, 1, 1) change colour (8 steps,
sqrt 3) and carry the photon (her first form of 30 October, evening): not a loop but an open path along one body diagonal,
with half a curl, spin 1, no twist, moving one link per sweep, the angle of its curl turning a quarter turn per link so
that it repeats every four links. Its readers: charge 0, net twist 0, curl +1/2 or -1/2, spin +1 or -1.

A Loop: closed on the torus, one step kind, twist on each diagonal (thirds on box, halves on face, zero on long), an
non-zero integer curl (signed from 30 October, evening: the anti-particle's loop has the opposite curl, so that a
particle's curl can net zero, her neutrino), and a spin in {-1/2, 0, +1/2} that may be non-zero only if some twist is
present (her rule of 30 October: spin needs twist present, not net twist). A Particle is a named set of loops. Readers: charge = sum of twist;
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
    displacements so that the torus wrap is explicit. twists: one Fraction per step. curl: non-zero integer. spin: Fraction."""
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
        if int(self.curl) == 0 or int(self.curl) != self.curl:
            raise ValueError("one curl of energy per loop at least; curl must be a non-zero integer (signed from 30 October)")
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
    """The same loop with every twist, its curl and its spin reversed: the anti-particle's loop (pairs: +theta with -theta;
    her ledger of 30 October, evening: the positron is -1 twist, -1 loop)."""
    return Loop(loop.L, loop.start, list(loop.steps), [-t for t in loop.twists], curl=-loop.curl, spin=-loop.spin)


# ---------------------------------------------------------------- the photon, first form (her decision of 30 October, evening)

BODY_STEPS = {tuple(s) for s in product((1, -1), repeat=3)}


@dataclass
class Photon:
    """Her first form of the photon, put in as she stated it: a curve on the two-colour (body) diagonal, half a curl, spin 1,
    no twist, carried one link per sweep by its spin; the angle its curl sits at turns as it moves and repeats every four
    links; on meeting matter it hands on its spin and its curl (not built: the meeting). An open path of `length` body
    diagonals, all the same step `direction`, from `start`, advanced by `position` links. curl is +1/2 or -1/2 (the sign is
    the sense of the curl; her annihilation ledger makes the two photons opposite), spin +1 or -1 (the two photons' spins
    are opposite in direction). Nothing is derived; the values are the rules. The two-colour diagonal has length sqrt 3 (she
    wrote root 2 and corrected it to root 3, 30 October)."""
    L: int
    start: tuple
    direction: tuple
    length: int = 4
    curl: Fraction = HALF
    spin: Fraction = Fraction(1)
    position: int = 0

    def __post_init__(self):
        if tuple(self.direction) not in BODY_STEPS:
            raise ValueError("a photon runs along a body diagonal (1, 1, 1) in some signed form; got %s" % (self.direction,))
        self.curl, self.spin = Fraction(self.curl), Fraction(self.spin)
        if self.curl not in (HALF, -HALF):
            raise ValueError("a photon carries half a curl, +1/2 or -1/2")
        if self.spin not in (Fraction(1), Fraction(-1)):
            raise ValueError("a photon carries spin 1, in one direction or the other")
        if self.length < 1:
            raise ValueError("a photon has at least one link")

    @property
    def charge(self):
        return Fraction(0)

    net_twist = charge

    @property
    def twist_present(self):
        return Fraction(0)

    @property
    def mass_count(self):
        """Zero: a photon's diagonals are two-colour, not matter's one-colour box diagonals, so they are not counted as mass
        (her decision, 30 October, evening); `length` is the path it is drawn on and 4 is its period."""
        return 0

    @property
    def head(self):
        p = np.array(self.start, dtype=int) + self.position * np.array(self.direction, dtype=int)
        return tuple(int(x) % self.L for x in p)

    @property
    def colour(self):
        return colour(self.head)

    @property
    def angle_degrees(self):
        """The angle the half curl sits at: a quarter turn per link, repeating every four (her picture)."""
        return 90 * (self.position % 4)

    @property
    def parts(self):
        return dict(L=0, n=0, tau_plus=Fraction(0), T=Fraction(0), s=self.spin, C=self.curl)

    def advance(self, sweeps=1):
        """One link per sweep, carried by its spin."""
        return Photon(self.L, self.start, self.direction, self.length, self.curl, self.spin, self.position + int(sweeps))


def annihilate(particle, antiparticle, direction=(1, 1, 1), length=4):
    """Her ledger of 30 October, evening: an electron (+1 twist, 1 loop, 1/2 spin) and its anti-particle (-1 twist, -1 loop,
    1/2 spin) make two photons, C (+1/2 loop, spin 1, no twist) and D (-1/2 loop in the opposite direction, spin 1, no
    twist). Built with the photons' spins opposite (+1, -1), the only reading under which the signed spin balances given
    that `mirror` reverses the loop's spin. The photons leave from the particle's first point along `direction` and its
    reverse. Returns (C, D). What is conserved is read by `ledger`."""
    start = particle.loops[0].start
    back = tuple(-x for x in direction)
    return (Photon(particle.loops[0].L, start, direction, length, HALF, Fraction(1)),
            Photon(particle.loops[0].L, start, back, length, -HALF, Fraction(-1)))


def ledger(objects):
    """The sums her ledger balances: net twist, curl and signed spin, over particles and photons alike, and the mass count."""
    tw = cu = sp = Fraction(0)
    n = 0
    for o in objects:
        pr = o.parts
        tw, cu, sp, n = tw + pr["T"], cu + pr["C"], sp + pr["s"], n + pr["n"]
    return dict(T=tw, C=cu, s=sp, n=n)


# ---------------------------------------------------------------- the coil's writhe, and the energy of twist (30 October, her decisions)

_PIECES = 8
_gx, _gw = np.polynomial.legendre.leggauss(16)
_GX = np.concatenate([(k + (_gx + 1) / 2) / _PIECES for k in range(_PIECES)])
_GW = np.concatenate([_gw / 2 / _PIECES for _ in range(_PIECES)])


def unwrapped_points(loop):
    """The loop's corners in the plane's own coordinates, unwrapped (cumulative steps from the start); None if the loop
    winds round the torus, since the writhe of a winding loop is not that of a closed curve in space."""
    total = np.sum(np.array(loop.steps, dtype=int), axis=0)
    if any(int(t) != 0 for t in total):
        return None
    pts = [np.array(loop.start, dtype=float)]
    for s in loop.steps[:-1]:
        pts.append(pts[-1] + np.array(s, dtype=float))
    return np.array(pts)


def writhe(loop):
    """The writhe of the loop as a closed polygon in space: the Gauss double integral over non-adjacent segment pairs,
    each segment split into 8 pieces with 16-point Gauss-Legendre (the routine of sandbox/coil_writhe.py). Exact to the
    quadrature; 0 for a planar loop; its sign flips with the loop's mirror image. None for a loop that winds the torus."""
    V = unwrapped_points(loop)
    if V is None:
        return None
    n = len(V)
    T = np.roll(V, -1, axis=0) - V
    R = V[:, None, :] + _GX[None, :, None] * T[:, None, :]
    total = 0.0
    for i in range(n):
        js = [j for j in range(n) if j != i and (i + 1) % n != j and (j + 1) % n != i]
        if not js:
            continue
        cr = np.cross(T[i], T[js])
        d = R[i][:, None, None, :] - R[js][None, :, :, :]
        num = np.einsum("qjpk,jk->qjp", d, cr)
        den = np.linalg.norm(d, axis=3) ** 3
        total += np.einsum("q,p,qjp->", _GW, _GW, num / den)
    return float(total / (4 * np.pi))


def twist_energy(loop, eps=1.0, eps_w=1.0):
    """E4 plus writhe: eps [sum tau^2 + sum (tau_next - tau)^2] + eps_w Wr^2 (the build document, section 4). A winding
    loop has no writhe and pays eps_w * 0."""
    taus = loop.twists
    n = len(taus)
    elastic = float(sum(t * t for t in taus))
    mismatch = float(sum((taus[(i + 1) % n] - taus[i]) ** 2 for i in range(n)))
    if eps_w == 0.0:
        return eps * (elastic + mismatch)
    wr = writhe(loop)
    return eps * (elastic + mismatch) + eps_w * (0.0 if wr is None else wr * wr)


def particle_energy(particle, eps=1.0, eps_w=1.0):
    return sum(twist_energy(lp, eps, eps_w) for lp in particle.loops)

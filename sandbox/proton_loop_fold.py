"""A look (sandbox lane): closed loops of box diagonals on the cubic lattice, and the fold each needs.

The owner's rules of 27 to 28 October (docs/design/twist_curl_rules_2026-10-27.md): matter twist lives on the centre
diagonals of 1 x 1 x 2 boxes, in thirds, signed by the colour of the diagonal; a closed loop's charge is its total
twist, a whole number; a loop that cannot pay for a twist folds instead, and the fold (the published writhe) carries
mass but no charge. Question: what is the smallest closed loop of box diagonals, what colours can it carry, and how
much fold does it hold?

Exact geometry, no toy energy (the toy's energy does not see diagonals):
  1. A box diagonal is a step (+-1, +-1, +-2) in some order; its family is the axis of the 2. Every step joins two
     points of one colour (parity of x + y + z), so every closed loop of box diagonals is one colour: the proton's
     2 black + 1 white cannot be a chain of diagonals end to end. Where 2 black + 1 white does occur is among the
     four diagonals through one square's centre (2 black, 2 white), which all belong to one box, so one family.
  2. Closed loops of 3 to 6 steps are enumerated up to translation and start; loops whose segments cross or touch
     are dropped (the Gauss integrand is singular there and the fold of a self-crossing loop is not the thing
     asked); each simple loop is checked for being planar; writhe is the Gauss double integral over non-adjacent
     pairs of segments, each segment split into 8 pieces with 16-point Gauss-Legendre on each (a planar loop must
     give 0 to rounding, which is checked and reported). The distribution of |writhe| by length is reported.
     First run (69 minutes, unsplit quadrature, crossing loops kept) gave planar loops up to 1.0: the crossings.
"""
from collections import Counter
from itertools import permutations, product

import numpy as np

STEPS = sorted({tuple(s * v for s, v in zip(signs, perm))
                for perm in set(permutations((1, 1, 2))) for signs in product((1, -1), repeat=3)})
assert len(STEPS) == 24
FAMILY = {s: int(np.argmax(np.abs(s))) for s in STEPS}


def closed_loops(n):
    """Closed walks of n box-diagonal steps from the origin that do not revisit a point, up to rotation of the start."""
    out = set()

    def rec(path, pos, visited):
        if len(path) == n:
            if pos == (0, 0, 0):
                # canonical form: the lexicographically least rotation of the step sequence
                rots = [tuple(path[i:] + path[:i]) for i in range(n)]
                out.add(min(rots))
            return
        for s in STEPS:
            q = (pos[0] + s[0], pos[1] + s[1], pos[2] + s[2])
            remaining = n - len(path) - 1
            if remaining and q in visited:
                continue
            if remaining == 0 and q != (0, 0, 0):
                continue
            if sum(abs(c) for c in q) > 2 * remaining + 2 and remaining:
                continue
            rec(path + [s], q, visited | {q})

    rec([], (0, 0, 0), {(0, 0, 0)})
    return out


def vertices(loop):
    v = [np.zeros(3)]
    for s in loop:
        v.append(v[-1] + np.array(s, dtype=float))
    return np.array(v[:-1])


def is_planar(V):
    """Planar if every vertex lies in the plane of some non-collinear triple (the first run was wrong here: it took
    the first three vertices, which can be collinear when a step repeats, and then called every such loop planar)."""
    if len(V) < 4:
        return True
    for i in range(len(V)):
        for j in range(i + 1, len(V)):
            n = np.cross(V[i] - V[0], V[j] - V[0])
            if np.linalg.norm(n) > 1e-9:
                return all(abs(np.dot(q - V[0], n)) < 1e-9 for q in V)
    return True


PIECES = 8
gx, gw = np.polynomial.legendre.leggauss(16)
gx = (gx + 1) / 2
gw = gw / 2
GX = np.concatenate([(k + gx) / PIECES for k in range(PIECES)])
GW = np.concatenate([gw / PIECES for _ in range(PIECES)])


def writhe(V):
    n = len(V)
    total = 0.0
    for i in range(n):
        a0, a1 = V[i], V[(i + 1) % n]
        ta = a1 - a0
        ra = a0[None, :] + GX[:, None] * ta[None, :]
        for j in range(n):
            if i == j or (i + 1) % n == j or (j + 1) % n == i:
                continue           # adjacent straight segments contribute nothing
            b0, b1 = V[j], V[(j + 1) % n]
            tb = b1 - b0
            rb = b0[None, :] + GX[:, None] * tb[None, :]
            cr = np.cross(ta, tb)
            d = ra[:, None, :] - rb[None, :, :]
            total += np.einsum("i,j,ij->", GW, GW, (d @ cr) / np.linalg.norm(d, axis=2) ** 3)
    return total / (4 * np.pi)


def seg_dist(a0, a1, b0, b1):
    """Shortest distance between two closed segments."""
    u, v, w = a1 - a0, b1 - b0, a0 - b0
    A, B, C, D, E = u @ u, u @ v, v @ v, u @ w, v @ w
    den = A * C - B * B
    if den < 1e-12:
        s = 0.0
        tt = np.clip(E / C, 0, 1)
    else:
        s = np.clip((B * E - C * D) / den, 0, 1)
        tt = (B * s + E) / C
        if tt < 0:
            tt = 0.0; s = np.clip(-D / A, 0, 1)
        elif tt > 1:
            tt = 1.0; s = np.clip((B - D) / A, 0, 1)
    return np.linalg.norm(w + s * u - tt * v)


def is_simple(V):
    n = len(V)
    for i in range(n):
        for j in range(i + 1, n):
            if (i + 1) % n == j or (j + 1) % n == i:
                continue
            if seg_dist(V[i], V[(i + 1) % n], V[j], V[(j + 1) % n]) < 1e-9:
                return False
    return True


print("step families (axis of the 2):", Counter(FAMILY.values()))
print("colour: every step changes x+y+z by an even amount, so a loop of box diagonals is one colour:",
      all(sum(s) % 2 == 0 for s in STEPS))
print("the four centre diagonals through one square: 2 black, 2 white, one box, one family (geometry, Figure 1)")
print()
import sys
lengths = tuple(int(a) for a in sys.argv[1:]) or (3, 4, 5, 6)
for n in lengths:
    loops = closed_loops(n)
    simple = [l for l in loops if is_simple(vertices(l))]
    fams = Counter(tuple(sorted(Counter(FAMILY[s] for s in l).values())) for l in simple)
    wr = Counter()
    worst_planar = 0.0
    planar = 0
    for l in simple:
        V = vertices(l)
        w = writhe(V)
        if is_planar(V):
            planar += 1
            worst_planar = max(worst_planar, abs(w))
            continue
        wr[round(abs(w), 3)] += 1
    print("length %d: %d loops up to translation and start, %d simple (no crossing); %d of those planar (writhe 0 to %.1e); family patterns %s" % (
        n, len(loops), len(simple), planar, worst_planar, dict(fams)), flush=True)
    if wr:
        top = sorted(wr.items())
        print("   non-planar simple loops: |writhe| (count) %s" % [(float(a), b) for a, b in top[:14]], flush=True)
        print("   largest |writhe| at this length: %.3f; loops with |writhe| >= 0.25: %d" % (
            max(wr), sum(c for a, c in wr.items() if a >= 0.25)), flush=True)

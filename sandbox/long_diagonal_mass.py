"""A look (sandbox lane; the owner's question of 29 October, 11:44 UTC and her request of 11:50 UTC): does a long
diagonal count as one looped diagonal of mass, or as its length? Exact geometry on closed loops mixing short box
diagonals, the 24 permutations of (+-1, +-1, +-2), length sqrt 6, and long ones, (+-1, +-1, +-4), length sqrt 18 =
sqrt 3 x sqrt 6 (allowed by colour: every step changes x + y + z by an even number). Only a short diagonal can carry a
third of twist (hers: thirds live on the 1 x 1 x 2 diagonals), so a loop's charge capacity is its short count in thirds,
whole when that count is a multiple of 3; a long diagonal holds curl without twist (her long diagonal, the gluon).

For every closed, simple (non-self-crossing) loop of up to N steps, up to rotation, reversal and translation, this
reports its composition (shorts, longs), its two masses, mass_count = shorts + longs and mass_length = shorts +
sqrt(3) x longs (in units of one short diagonal), its charge capacity, and its writhe (the coil). Then the two mass
ladders, chargeable loops (shorts a multiple of 3) and neutral ones, under each rule.

WRITTEN BEFORE COMPUTING (ours): mixed loops exist at every length from 3 (a long step and two shorts can close, as
(1,1,4) + (-2,1,-1)... needs checking by the enumeration; if none closes at 3 the first mixed loops are at 4). Under
the count rule a mixed loop sits on a rung the short ladder already has (an integer), so the count rule adds no new
masses, only new objects at old masses; under the length rule every long diagonal adds 0.732 to the mass, so mixed loops
insert rungs between the integers, and the ladder below the muon gets denser, not sparser. Neither rule opens a gap
between the electron (3) and the muon (621). Kills, if the enumeration says so: "a long diagonal makes the spectrum
sparser" (ours, declared here). Crowns nothing: which rule is right is hers to decide and no measurement here decides it.
"""
import sys
from collections import Counter, defaultdict
from itertools import permutations, product

import numpy as np

PIECES = 8
gx, gw = np.polynomial.legendre.leggauss(16)
GX = np.concatenate([(k + (gx + 1) / 2) / PIECES for k in range(PIECES)])
GW = np.concatenate([gw / 2 / PIECES for _ in range(PIECES)])


def writhe(V):
    n = len(V)
    total = 0.0
    T = np.roll(V, -1, axis=0) - V
    R = V[:, None, :] + GX[None, :, None] * T[:, None, :]
    for i in range(n):
        js = [j for j in range(n) if j != i and (i + 1) % n != j and (j + 1) % n != i]
        if not js:
            continue
        cr = np.cross(T[i], T[js])
        d = R[i][:, None, None, :] - R[js][None, :, :, :]
        num = np.einsum("qjpk,jk->qjp", d, cr)
        den = np.linalg.norm(d, axis=3) ** 3
        total += np.einsum("q,p,qjp->", GW, GW, num / den)
    return total / (4 * np.pi)


def seg_dist(a0, a1, b0, b1):
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


def steps_of(base):
    out = set()
    for p in permutations(base):
        for sg in product((1, -1), repeat=3):
            out.add(tuple(a * s for a, s in zip(p, sg)))
    return sorted(out)


SHORT = steps_of((1, 1, 2))
LONG = steps_of((1, 1, 4))
STEPS = [(s, 0) for s in SHORT] + [(s, 1) for s in LONG]   # (vector, is_long)
REACH = 6  # the farthest one step moves in L1 (a long step: 1 + 1 + 4)


def canonical(seq):
    """Up to rotation and reversal (reversal: negated steps in reverse order); translation is free already."""
    n = len(seq)
    cands = []
    rev = [((-a, -b, -c), k) for (a, b, c), k in reversed(seq)]
    for s in (seq, rev):
        for r in range(n):
            cands.append(tuple(s[r:] + s[:r]))
    return min(cands)


def closed_loops(n):
    found = set()
    pos0 = (0, 0, 0)

    def rec(seq, pos, depth):
        if depth == n:
            if pos == pos0:
                found.add(canonical(seq))
            return
        left = n - depth
        if abs(pos[0]) + abs(pos[1]) + abs(pos[2]) > left * REACH:
            return
        for v, k in STEPS:
            if depth > 0 and v == tuple(-c for c in seq[-1][0]):
                continue  # an immediate backtrack is never simple
            rec(seq + [(v, k)], (pos[0] + v[0], pos[1] + v[1], pos[2] + v[2]), depth + 1)

    rec([], pos0, 0)
    return found


def vertices(seq):
    V = [np.zeros(3)]
    for v, k in seq[:-1]:
        V.append(V[-1] + np.array(v, dtype=float))
    return np.array(V)


print("short steps:", len(SHORT), " long steps:", len(LONG), " colour-safe:",
      all(sum(s) % 2 == 0 for s in SHORT + LONG))
print("masses in units of one short diagonal: count = shorts + longs; length = shorts + sqrt(3) x longs")
print()
nmax = int(sys.argv[1]) if len(sys.argv) > 1 else 5
ladder_count = defaultdict(set)
ladder_length = defaultdict(set)
for n in range(3, nmax + 1):
    loops = closed_loops(n)
    rows = defaultdict(list)
    for seq in loops:
        V = vertices(list(seq))
        if not is_simple(V):
            continue
        nl = sum(k for _, k in seq)
        ns = n - nl
        rows[(ns, nl)].append(abs(writhe(V)))
    print("length %d: %d closed loops up to symmetry, %d simple" % (n, len(loops), sum(len(r) for r in rows.values())))
    for (ns, nl), ws in sorted(rows.items()):
        mc = ns + nl
        ml = ns + np.sqrt(3) * nl
        charge = "whole charge possible" if ns % 3 == 0 and ns > 0 else ("neutral only" if ns == 0 else "fractional only")
        print("   shorts %d longs %d: %6d simple loops; mass count %d, mass length %.3f; %s; |coil| %.3f to %.3f"
              % (ns, nl, len(ws), mc, ml, charge, min(ws), max(ws)))
        kind = "charged" if ns % 3 == 0 and ns > 0 else ("neutral" if ns == 0 else "fractional")
        ladder_count[kind].add(mc)
        ladder_length[kind].add(round(ml, 3))
    print()
print("mass ladders up to %d steps (units of one short diagonal):" % nmax)
for kind in ("charged", "neutral", "fractional"):
    print("  %-10s count rule:  %s" % (kind, sorted(ladder_count[kind])))
    print("  %-10s length rule: %s" % (kind, [float(x) for x in sorted(ladder_length[kind])]))

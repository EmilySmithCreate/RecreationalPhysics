"""A look (sandbox lane; the owner's instruction of 30 October). Guess 2 (ours): the neutrino lives on the dark carrier:
a closed loop of face diagonals (1, 1, 0) holding dark twist in halves, so it has spin 1/2 (full curl, R5), no electric
charge (no matter twist), and interacts with ordinary matter only through gravity and whatever the dark twist couples to,
which is how a neutrino behaves (general knowledge, to verify: it has no electric charge and feels only the weak force
and gravity). This keeps R9 as written for matter loops.

Two things are exact and can kill it before any rule is added:

(1) Geometry: do closed loops of face diagonals exist, at what lengths, and are they one colour? (A face-diagonal step
    changes x + y + z by 0 or +-2, so every such loop is one colour, as the box-diagonal loops are.) With her stability
    rule, a loop with two opposite halves (+1/2, -1/2, net zero) needs them at equal spacing, so an even length; with one
    half (net +-1/2, a 'dark charge') any length will do.

(2) Mass: if the neutrino is a loop of n_f face diagonals and mass counts looped diagonals at the electron's unit
    u = m_e/3 = 0.170 MeV, its mass is at least 3u = 0.51 MeV, while the measured bound is below 8e-7 MeV: a factor of
    a million. So the guess survives only if face diagonals carry no mass (mass counts box diagonals only, which is how
    the standing rules are worded) and the neutrino's small measured mass comes from something else. Kind: measurement.

WRITTEN BEFORE COMPUTING (ours): face-diagonal loops exist at length 3 (the triangles of a cube's corner tetrahedra,
seen before: LOG, 28 October) and at 4 (squares in a plane); the net-zero two-half form needs length 4 or more; the mass
kill in (2) is arithmetic and stands whatever (1) finds. Kills: "the neutrino is a face-diagonal loop whose diagonals
weigh what box diagonals weigh" (ours, declared). Crowns nothing.
"""
from itertools import permutations, product

import numpy as np

from long_diagonal_mass import is_simple, writhe


def steps():
    out = set()
    for p in permutations((1, 1, 0)):
        for sg in product((1, -1), repeat=3):
            out.add(tuple(a * s for a, s in zip(p, sg)))
    return sorted(v for v in out if any(v))


FACE = steps()  # 12 face diagonals


def loops(n):
    found = set()

    def canon(seq):
        rev = [tuple(-c for c in v) for v in reversed(seq)]
        cands = []
        for s in (seq, rev):
            for r in range(n):
                cands.append(tuple(s[r:] + s[:r]))
        return min(cands)

    def rec(seq, pos, depth):
        if depth == n:
            if pos == (0, 0, 0):
                found.add(canon(seq))
            return
        if sum(abs(c) for c in pos) > 2 * (n - depth):
            return
        for v in FACE:
            if depth > 0 and v == tuple(-c for c in seq[-1]):
                continue
            rec(seq + [v], tuple(p + c for p, c in zip(pos, v)), depth + 1)

    rec([], (0, 0, 0), 0)
    return found


if __name__ == "__main__":
    print("face-diagonal steps:", len(FACE), "; colour-safe (x+y+z changes by an even number):",
          all(sum(v) % 2 == 0 for v in FACE))
    for n in range(3, 7):
        L = loops(n)
        simple, coils = 0, []
        for seq in L:
            V = np.array([np.zeros(3)] + list(np.cumsum(np.array(seq[:-1], dtype=float), axis=0)))
            if is_simple(V):
                simple += 1
                coils.append(abs(writhe(V)))
        print("length %d: %d closed loops up to symmetry, %d simple, |coil| %.3f to %.3f; two opposite halves at equal spacing: %s"
              % (n, len(L), simple, min(coils) if coils else 0, max(coils) if coils else 0, "possible" if n % 2 == 0 else "no (odd length)"))
    u = 0.51099895 / 3
    print()
    print("mass kill: a 3-loop at the electron's unit weighs %.3f MeV; the neutrino bound is < 8e-7 MeV: factor %.0e" % (3 * u, 3 * u / 8e-7))

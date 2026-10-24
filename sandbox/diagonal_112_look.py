"""Exact look for the owner's decision of 24 October: matter strands move from body diagonals (which join the two
colours of point) to 1 x 1 x 2 diagonals (which join one colour to the same colour), to hold the rule of thirds.

1. How many 1 x 1 x 2 diagonals lie in a 2 x 2 x 2 and a 2 x 2 x 3 block of cubes (both ends inside the block),
   with face diagonals and body diagonals counted the same way for comparison; and how many per point in the
   unbounded lattice.
2. Every line of the lattice that joins one colour to the same colour and leaves the coordinate planes: which is
   shortest.
3. Does the lattice turn into itself about a 1 x 1 x 2 line (the check that made thirds natural on body diagonals)?
4. The smallest closed rings of 1 x 1 x 2 diagonals through one point.
"""
import itertools
import os

import numpy as np

OUT = os.path.join(os.path.dirname(__file__), "out")
os.makedirs(OUT, exist_ok=True)
lines = []


def say(s=""):
    print(s)
    lines.append(s)


def directions(pattern):
    out = set()
    for perm in set(itertools.permutations(pattern)):
        for signs in itertools.product((1, -1), repeat=3):
            out.add(tuple(p * s for p, s in zip(perm, signs)))
    return sorted(out)


D112 = directions((1, 1, 2))
FACE = directions((1, 1, 0))
BODY = directions((1, 1, 1))


def count_in_block(cubes, dirs):
    nx, ny, nz = (c + 1 for c in cubes)               # points per side
    pts = set(itertools.product(range(nx), range(ny), range(nz)))
    segs = set()
    for p in pts:
        for d in dirs:
            q = tuple(np.add(p, d))
            if q in pts:
                segs.add(frozenset((p, q)))
    same = sum(1 for s in segs if len({sum(x) % 2 for x in s}) == 1)
    return len(segs), same


say("1. Lines with both ends inside a block of cubes (same-colour count in brackets)")
for cubes in ((2, 2, 2), (2, 2, 3)):
    n112, s112 = count_in_block(cubes, D112)
    nf, sf = count_in_block(cubes, FACE)
    nb, sb = count_in_block(cubes, BODY)
    say(f"   {cubes[0]} x {cubes[1]} x {cubes[2]} block ({(cubes[0]+1)*(cubes[1]+1)*(cubes[2]+1)} points): "
        f"1x1x2 diagonals {n112} ({s112} same colour); face diagonals {nf} ({sf}); body diagonals {nb} ({sb})")
say(f"   unbounded lattice: {len(D112)} directions of 1x1x2 from each point, so {len(D112) // 2} lines per point "
    f"(face diagonals {len(FACE) // 2}, body diagonals {len(BODY) // 2})")

say("\n2. Same-colour lines that leave every coordinate plane, shortest first")
cands = []
for v in itertools.product(range(-3, 4), repeat=3):
    if all(v) and sum(v) % 2 == 0:
        cands.append((sum(x * x for x in v), tuple(sorted(map(abs, v)))))
for length2, pat in sorted(set(cands))[:3]:
    g = np.gcd.reduce(pat)
    say(f"   {pat[0]} x {pat[1]} x {pat[2]}: length sqrt({length2}) = {np.sqrt(length2):.4f}"
        + ("" if g == 1 else f"  (passes through a lattice point: it is {g} steps of a shorter line)"))


def rotation_order(axis):
    a = np.array(axis, float) / np.linalg.norm(axis)
    K = np.array([[0, -a[2], a[1]], [a[2], 0, -a[0]], [-a[1], a[0], 0]])
    for n in range(12, 0, -1):
        t = 2 * np.pi / n
        R = np.eye(3) + np.sin(t) * K + (1 - np.cos(t)) * K @ K
        if np.allclose(R, np.rint(R), atol=1e-9):
            return n
    return None


say("\n3. The smallest turn about each line that maps the lattice onto itself")
for name, ax in (("edge (1,0,0)", (1, 0, 0)), ("face diagonal (1,1,0)", (1, 1, 0)),
                 ("body diagonal (1,1,1)", (1, 1, 1)), ("1x1x2 diagonal (1,1,2)", (1, 1, 2))):
    n = rotation_order(ax)
    say(f"   {name}: every 360/{n} = {360 // n} degrees" + ("  (no turn short of a full one)" if n == 1 else ""))


def rings(steps, max_len):
    counts = {}
    start = (0, 0, 0)

    def walk(path, last):
        for s in steps:
            if last is not None and s == tuple(-x for x in last):
                continue
            q = tuple(np.add(path[-1], s))
            if q == start and len(path) >= 3:
                counts[len(path)] = counts.get(len(path), 0) + 1
                continue
            if q in path or len(path) >= max_len:
                continue
            walk(path + [q], s)

    walk([start], None)
    return {k: v // 2 for k, v in sorted(counts.items())}


say("\n4. Closed rings of 1x1x2 diagonals through one point (no step back, no point twice), by number of segments")
say(f"   {rings(D112, 4)}")

path = os.path.join(OUT, "diagonal_112_look_2026-10-24.txt")
open(path, "w", encoding="utf-8").write("\n".join(lines) + "\n")
print("written", path)

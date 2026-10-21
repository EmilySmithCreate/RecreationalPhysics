"""Sandbox look, 21 October 2026 (exact for what it counts; a look, not a result). The owner's twisted rings are made of
face diagonals, which join points of one kind (VISION Updates 85 to 87). Which closed rings can such diagonals make?

In the six-link toy's flat space (a cubic lattice), the points of one kind are those with an even coordinate sum, and
the face diagonals join each such point to its 12 nearest same-kind neighbours at distance sqrt(2): the points of one
kind form a face-centred cubic lattice. Counted here: (1) inside one cube, the same-kind corners and the face diagonals
among them; (2) the simple closed rings of k face diagonals through one point, k = 3 to 6, counted once per ring (not per
direction or starting point), with their lengths k sqrt(2) in link lengths and whether they lie in one plane; (3) for
comparison, the rings of k edges through one point of the cubic lattice itself.
Usage: python3 sandbox/diagonal_rings.py
"""
import itertools
import math

DIAG = [v for v in itertools.product((-1, 0, 1), repeat=3) if sum(abs(x) for x in v) == 2]   # 12 face diagonals
EDGE = [v for v in itertools.product((-1, 0, 1), repeat=3) if sum(abs(x) for x in v) == 1]   # 6 edges


def add(p, v):
    return tuple(a + b for a, b in zip(p, v))


def rings_through_origin(steps, kmax):
    """Simple cycles through the origin, as frozensets of their points, by length."""
    found = {k: set() for k in range(3, kmax + 1)}
    origin = (0, 0, 0)

    def walk(path):
        k = len(path)
        if k > kmax:
            return
        for v in steps:
            q = add(path[-1], v)
            if q == origin and k >= 3:
                found[k].add(frozenset(path))
            elif q not in path and k < kmax:
                walk(path + [q])

    walk([origin])
    return found


def planar(points):
    pts = list(points)
    p0 = pts[0]
    vecs = [tuple(a - b for a, b in zip(p, p0)) for p in pts[1:]]
    for a, b, c in itertools.combinations(vecs, 3):
        det = (a[0] * (b[1] * c[2] - b[2] * c[1]) - a[1] * (b[0] * c[2] - b[2] * c[0]) + a[2] * (b[0] * c[1] - b[1] * c[0]))
        if det != 0:
            return False
    return True


corners = list(itertools.product((0, 1), repeat=3))
for kind in (0, 1):
    same = [c for c in corners if sum(c) % 2 == kind]
    diag = [(a, b) for a, b in itertools.combinations(same, 2)
            if sum((x - y) ** 2 for x, y in zip(a, b)) == 2]
    print(f"one cube, kind {kind}: {len(same)} corners, {len(diag)} face diagonals among them "
          f"(a regular tetrahedron: every pair of these corners is one face diagonal apart)")
body = [(a, b) for a, b in itertools.combinations(corners, 2) if sum((x - y) ** 2 for x, y in zip(a, b)) == 3]
print(f"one cube: {len(body)} corner-to-corner diagonals; joining two different kinds: "
      f"{sum(1 for a, b in body if sum(a) % 2 != sum(b) % 2)} of {len(body)}")

for name, steps, length in (("face diagonals (one kind of point)", DIAG, math.sqrt(2)), ("edges", EDGE, 1.0)):
    found = rings_through_origin(steps, 6)
    print(f"\nrings through one point made of {name}:")
    for k, rings in found.items():
        flat = sum(1 for r in rings if planar(r))
        print(f"  {k} links: {len(rings):5d} rings ({flat} lying in one plane), length {k * length:.3f} link lengths")

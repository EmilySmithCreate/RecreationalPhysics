"""Sandbox look, 22 October 2026 (exact for what it computes; a look, not a result). The owner asked whether the shape
of a curl is connected to the golden ratio, phi = (1 + sqrt 5)/2 = 1.618... Where could phi enter the toy?

(A) Lengths. The six-link toy's flat space is a cubic lattice: links 1, face diagonals sqrt 2, body diagonals sqrt 3.
(B) Symmetry. phi comes with five-fold symmetry (pentagons, the icosahedron). A rotation that maps a lattice to itself
    has an integer matrix in the lattice's basis, so its trace 1 + 2 cos(theta) is an integer: theta can only be 60,
    90, 120 or 180 degrees (the crystallographic restriction). Listed here by brute force over 2 cos(theta).
(C) Vibrations. The Laplacian frequencies of the toy's objects: rings of n links, the hypercubes (the 4-cube is the
    curled 4 x 4 torus, the 6-cube the fully curled 4 x 4 x 4), and two flat tori. Does any frequency involve phi?
(D) Shadows. The 6-cube's 64 corners projected into three directions two ways: along the toy's own axes (how the
    4 x 4 x 4 torus sits in space) and along the six five-fold axes of an icosahedron (the cut-and-project picture of
    icosahedral quasicrystals). The hull's vertices, faces and the ratio of each face's diagonals.
Usage: python3 sandbox/golden_ratio_look.py
"""
import itertools
import math

import numpy as np
from scipy.spatial import ConvexHull

PHI = (1 + math.sqrt(5)) / 2
GOLDEN_COS = [PHI, -PHI, PHI - 1, 1 - PHI]   # the values of 2 cos(theta) for multiples of 36 degrees


def has_phi(eigs):
    """True if some eigenvalue e has 2 - e equal to one of the golden values of 2 cos(theta) (rings, tori)."""
    return any(abs((2 - e) - g) < 1e-9 or abs((4 - e) - g - 2) < 1e-9 for e in eigs for g in GOLDEN_COS)


def ring(n):
    a = np.zeros((n, n))
    for i in range(n):
        a[i, (i + 1) % n] = a[(i + 1) % n, i] = 1
    return a


def torus(lx, ly):
    n = lx * ly
    a = np.zeros((n, n))
    for x in range(lx):
        for y in range(ly):
            i = x * ly + y
            for j in (((x + 1) % lx) * ly + y, x * ly + (y + 1) % ly):
                a[i, j] = a[j, i] = 1
    return a


def hypercube(d):
    n = 2 ** d
    a = np.zeros((n, n))
    for i in range(n):
        for k in range(d):
            a[i, i ^ (1 << k)] = 1
    return a


def spectrum(a):
    lap = np.diag(a.sum(1)) - a
    return np.round(np.linalg.eigvalsh(lap), 9)


def shadow(axes):
    pts = np.array([sum(v[i] * np.array(axes[i], float) for i in range(6)) for v in itertools.product((0, 1), repeat=6)])
    hull = ConvexHull(pts)
    verts = sorted(set(hull.vertices))
    planes = {}
    for eq, simplex in zip(hull.equations, hull.simplices):
        key = tuple(np.round(eq, 6))
        planes.setdefault(key, set()).update(simplex)
    ratios = []
    for corner_ids in planes.values():
        c = np.unique(np.round(pts[list(corner_ids)], 9), axis=0)
        if len(c) == 4:
            d = sorted(np.linalg.norm(c[i] - c[j]) for i, j in itertools.combinations(range(4), 2))
            ratios.append(d[5] / d[4])   # the two longest distances in a rhombus are its diagonals
    return len(verts), len(planes), ratios


def main():
    print("(A) lengths 1, sqrt2 = %.4f, sqrt3 = %.4f; ratios sqrt3/sqrt2 = %.4f; phi = %.4f"
          % (math.sqrt(2), math.sqrt(3), math.sqrt(1.5), PHI))
    allowed = [round(math.degrees(math.acos(t / 2))) for t in (-2, -1, 0, 1, 2)]
    print("(B) rotations a lattice allows (2cos integer): %s degrees; 72 and 36 (five-fold) are not among them" % allowed)
    print("(C) does a frequency involve phi?")
    for name, a in [("ring 4", ring(4)), ("ring 6", ring(6)), ("ring 8", ring(8)), ("ring 10", ring(10)),
                    ("ring 12", ring(12)), ("ring 20", ring(20)), ("3-cube", hypercube(3)), ("4-cube", hypercube(4)),
                    ("6-cube", hypercube(6)), ("torus 8x8", torus(8, 8)), ("torus 16x10", torus(16, 10))]:
        e = spectrum(a)
        print("    %-12s phi: %-5s distinct frequencies: %s" % (name, has_phi(e),
              ", ".join("%.3f" % x for x in sorted(set(e)))[:90]))
    toy_axes = [(1, 0, 0), (1, 0, 0), (0, 1, 0), (0, 1, 0), (0, 0, 1), (0, 0, 1)]
    ico_axes = [(0, 1, PHI), (0, -1, PHI), (PHI, 0, 1), (-PHI, 0, 1), (1, PHI, 0), (-1, PHI, 0)]
    for name, axes in [("toy's axes", toy_axes), ("icosahedral axes", ico_axes)]:
        nv, nf, r = shadow(axes)
        print("(D) 6-cube along %-16s hull: %d corners, %d faces; diagonal ratios of rhombic faces: %s"
              % (name, nv, nf, sorted(set(float(round(x, 6)) for x in r)) or "none"))


main()

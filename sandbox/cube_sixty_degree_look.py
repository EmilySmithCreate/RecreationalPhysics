"""Sandbox look (exploratory), 25 October 2026: the owner's 60-degree pieces and the 12 squares at a point.

Checks, exactly, on the cubic lattice:
1. how many squares meet at a point (pairs of perpendicular links);
2. whether a 60-degree turn about a body diagonal is a symmetry of the cube by itself, or only with a mirror
   (the rotoreflection S6), and what one, two and three such steps do;
3. whether each step keeps or swaps the two kinds of point (checkerboard colour = parity of x + y + z).
"""
import itertools
import numpy as np

# 1. squares at a point: pairs of the six links that are perpendicular
links = [np.array(v) for v in [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]]
perp = sum(1 for a, b in itertools.combinations(links, 2) if a @ b == 0)
print("squares meeting at a point:", perp, "| straight pairs:", sum(1 for a, b in itertools.combinations(links, 2) if a @ b == -1))

# 2. turns about the body diagonal through the centre of the unit cube
n = np.ones(3) / np.sqrt(3)
K = np.array([[0, -n[2], n[1]], [n[2], 0, -n[0]], [-n[1], n[0], 0]])


def rot(deg):
    t = np.radians(deg)
    return np.eye(3) + np.sin(t) * K + (1 - np.cos(t)) * K @ K


mirror = np.eye(3) - 2 * np.outer(n, n)
corners = [np.array(c, float) for c in itertools.product((0, 1), repeat=3)]
centre = np.full(3, 0.5)


def act(M, p):
    return M @ (p - centre) + centre


def describe(name, M):
    images = [act(M, c) for c in corners]
    is_sym = all(np.allclose(q, np.round(q)) and set(np.round(q)) <= {0, 1} for q in images)
    if not is_sym:
        print(f"{name:32s} symmetry of the cube: no")
        return
    swaps = [int(c.sum()) % 2 != int(np.round(q).sum()) % 2 for c, q in zip(corners, images)]
    kind = "swaps every point's kind" if all(swaps) else ("keeps every kind" if not any(swaps) else "mixed")
    print(f"{name:32s} symmetry of the cube: yes; {kind}")


describe("60 deg turn alone", rot(60))
describe("120 deg turn alone", rot(120))
describe("180 deg turn alone", rot(180))
S6 = mirror @ rot(60)
describe("60 deg turn + mirror (S6), x1", S6)
describe("S6 x2", S6 @ S6)
describe("S6 x3", S6 @ S6 @ S6)
print("S6 x3 equals inversion through the centre:", np.allclose(S6 @ S6 @ S6, -np.eye(3)))

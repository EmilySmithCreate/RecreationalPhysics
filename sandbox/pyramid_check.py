import numpy as np
from itertools import product, combinations
corners = [np.array(c) for c in product((0, 1), repeat=3)]
black = [c for c in corners if sum(c) % 2 == 0]
white = [c for c in corners if sum(c) % 2 == 1]
d = lambda a, b: np.linalg.norm(a - b)
print("black corners:", [tuple(c) for c in black])
print("black pairwise lengths:", sorted(round(d(a, b), 4) for a, b in combinations(black, 2)))
print("white pairwise lengths:", sorted(round(d(a, b), 4) for a, b in combinations(white, 2)))
# faces of the black tetrahedron: each edge is a face diagonal; which cube plane does it lie in?
fam = lambda a, b: "xyz"[int(np.argmin(np.abs(a - b)))] + "-normal"
for face in combinations(black, 3):
    edges = [(a, b) for a, b in combinations(face, 2)]
    fams = [fam(a, b) for a, b in edges]
    apex = [c for c in black if not any((c == f).all() for f in face)][0]
    centroid = sum(face) / 3
    opp_white = 1 - apex                       # the white corner on apex's body diagonal
    on_line = np.linalg.norm(np.cross(centroid - apex, opp_white - apex)) < 1e-12
    perp = all(abs(np.dot(opp_white - apex, b - a)) < 1e-12 for a, b in edges)
    print("face", [tuple(f) for f in face], "edge planes", fams,
          "| body diagonal from", tuple(apex), "to", tuple(opp_white),
          "passes through face centroid:", on_line, "perpendicular to face:", perp)
# body-diagonal steps cannot close in three
steps = [np.array(s) for s in product((1, -1), repeat=3)]
print("closed triangles of body diagonals:", sum(1 for a, b, c in product(steps, repeat=3) if not (a + b + c).any()))
print("closed 4-loops of body diagonals (ordered):", sum(1 for a, b, c, e in product(steps, repeat=4) if not (a + b + c + e).any()))
# angles between body diagonals
bd = [np.array([1, 1, 1]), np.array([1, 1, -1]), np.array([1, -1, 1]), np.array([-1, 1, 1])]
print("angle between body diagonals (deg):", round(np.degrees(np.arccos(abs(bd[0] @ bd[1]) / 3)), 2))
print("tetrahedral angle at a corner between half-diagonals to the centre (deg):", round(np.degrees(np.arccos(-1 / 3)), 2))

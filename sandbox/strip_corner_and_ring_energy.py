"""Two exact looks for the owner's messages of 24 October (evening).

1. "thirds still apply becase the corners are still 3 sides the strip could align to": a flat strip lying along a
   1 x 1 x 2 diagonal, in a plane that also holds one cube edge at the corner. How many such planes, and how far apart?
2. "what is the difference in energy between a loop that wants to be flat length sqrrt 2 and sqrrt5?": a strip that
   would lie straight, closed into a circle of its own length L. Elastic bending (Euler's elastica, textbook, to
   verify): energy = (B/2) * integral of curvature^2 = (B/2) (2 pi / L)^2 L = 2 pi^2 B / L, B the bending stiffness.
   A twist of angle theta spread along the strip: (C/2) theta^2 / L, C the twisting stiffness. Both fall as 1 / L.
   No stiffness is known in the toy (the stiff toy has no lengths; stage B has lengths and no bending energy yet), so
   the answers are in units of B and C. Colour of each line's ends reported too.
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


say("1. Planes through a line that also hold one cube edge at its corner, and the angles between them")
for name, v in (("body diagonal (1,1,1)", (1, 1, 1)), ("1x1x2 diagonal (1,1,2)", (1, 1, 2)),
                ("face diagonal (1,1,0)", (1, 1, 0))):
    v = np.array(v, float)
    normals = []
    for e in np.eye(3):
        n = np.cross(v, e)
        if np.linalg.norm(n) > 1e-12:
            normals.append(n / np.linalg.norm(n))
    angs = sorted(np.degrees(np.arccos(min(1.0, abs(a @ b)))) for a, b in itertools.combinations(normals, 2))
    say(f"   {name}: {len(normals)} planes; angles between them " + ", ".join(f"{x:.2f}" for x in angs) + " degrees")
say("   A 1x1x2 line lies in no coordinate plane, so each of the three edges at its corner gives one plane: three")
say("   positions for the strip, as for the body diagonal, but not equally spaced (the body diagonal's are 60, 60, 60).")

say("\n2. A strip closed into a circle of its own length L: bending 2 pi^2 B / L; twist (C/2) theta^2 / L")
rows = (("face diagonal", np.sqrt(2), (1, 1, 0)), ("1x2 line", np.sqrt(5), (1, 2, 0)),
        ("1x1x2 diagonal", np.sqrt(6), (1, 1, 2)))
for name, L, v in rows:
    colour = "same colour" if sum(v) % 2 == 0 else "two colours"
    say(f"   {name:15s} L = {L:.4f} ({colour}): bending {2 * np.pi ** 2 / L:.3f} B")
e2, e5, e6 = (2 * np.pi ** 2 / L for _, L, _ in rows)
say(f"   difference sqrt2 - sqrt5: {e2 - e5:.3f} B (ratio {e2 / e5:.3f} = sqrt(5/2)); sqrt2 - sqrt6: {e2 - e6:.3f} B "
    f"(ratio {e2 / e6:.3f} = sqrt 3)")
say("   With her twists (Update 97 and 98): a half turn (pi) on the face diagonal, a third of a turn (2 pi / 3) on the")
say(f"   1x1x2 diagonal: twist energy {np.pi ** 2 / (2 * np.sqrt(2)):.3f} C against {(2 * np.pi / 3) ** 2 / (2 * np.sqrt(6)):.3f} C, "
    f"ratio {(np.pi ** 2 / (2 * np.sqrt(2))) / ((2 * np.pi / 3) ** 2 / (2 * np.sqrt(6))):.3f}.")
say("   Under these laws the shorter strip always holds more energy for the same bend or twist. Rule 13: none of these")
say("   ratios is to be set beside a measured number unless a rule fixes B and C first.")

path = os.path.join(OUT, "strip_corner_and_ring_energy_2026-10-24.txt")
open(path, "w", encoding="utf-8").write("\n".join(lines) + "\n")
print("written", path)

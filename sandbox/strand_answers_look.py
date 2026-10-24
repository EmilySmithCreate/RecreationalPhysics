"""Exact looks on the owner's answers of 24 October (comments in docs/design/particle_handoff_brief_2026-10-24.md):
matter and antimatter on body diagonals, dark and antidark matter on face diagonals; an electron is three thirds into
one full twist, a Moebius strip; charge from thirds and handedness. A sandbox look; arithmetic and enumeration only.

1. Closed rings of body diagonals and of face diagonals on the cubic lattice, by length (enumeration).
2. The turn of a flat tape stepping round a body diagonal: angles between the planes through it that hold a cube edge.
3. A charge rule read from her answer, Q = -(signed thirds)/3, against the observed table with quark contents.
"""
import itertools
import os
from fractions import Fraction

import numpy as np

OUT = os.path.join(os.path.dirname(__file__), "out")
os.makedirs(OUT, exist_ok=True)
lines = []


def say(s=""):
    print(s)
    lines.append(s)


BODY = [np.array(v) for v in itertools.product((1, -1), repeat=3)]
FACE = [np.array(v) for v in set(itertools.permutations((1, 1, 0))) | set(itertools.permutations((1, -1, 0)))
        | set(itertools.permutations((-1, -1, 0)))]


def kind(p):
    return int(sum(p)) % 2


def rings(steps, max_len):
    """closed walks from the origin with no backtracking, no repeated point, counted once per cycle and direction"""
    counts = {}
    start = (0, 0, 0)

    def walk(path, last):
        n = len(path)
        for s in steps:
            if last is not None and np.array_equal(s, -last):
                continue
            q = tuple(np.array(path[-1]) + s)
            if q == start and n >= 3:
                counts[n] = counts.get(n, 0) + 1
                continue
            if q in path or n >= max_len:
                continue
            walk(path + [q], s)

    walk([start], None)
    # each cycle through the origin is found twice (two directions); report rings through the origin per length
    return {k: v // 2 for k, v in sorted(counts.items())}


say("1. Closed rings through one point (no step back, no point twice), by number of segments")
say(f"   body diagonals (each joins kind {kind((0, 0, 0))} to kind {kind((1, 1, 1))}): {rings(BODY, 6)}")
say(f"   face diagonals (each joins a point to its own kind): {rings(FACE, 4)}")
say("   A body diagonal always changes the kind of point, so a closed ring of them has an even number of segments:")
say("   no ring of three body diagonals exists. The smallest is four.")

say("\n2. A flat tape lying along the body diagonal (1, 1, 1), in a plane that also holds a cube edge")
d = np.array([1.0, 1.0, 1.0]) / np.sqrt(3)
planes = {"x = y": np.array([1, -1, 0.0]), "y = z": np.array([0, 1, -1.0]), "z = x": np.array([-1, 0, 1.0])}
names = list(planes)
for a, b in itertools.combinations(names, 2):
    na, nb = planes[a] / np.linalg.norm(planes[a]), planes[b] / np.linalg.norm(planes[b])
    ang = np.degrees(np.arccos(abs(na @ nb)))
    say(f"   planes {a} and {b}: {ang:.1f} degrees apart")
say("   One step to the next plane turns the tape 60 degrees; three steps turn it 180 degrees, which brings a flat tape")
say("   back onto itself face down: closed there, it is a Moebius band (one-sided). Six steps, 360 degrees, close a")
say("   two-sided band. So 'three thirds' closing as a Moebius strip is the 60-degree step; 'one full twist' (360) needs six.")

say("\n3. A charge rule read from her answer: Q = -(signed thirds)/3, the electron +3 thirds (Q = -1), its mirror -3")
F = Fraction
quark = {"u": -2, "d": +1, "ubar": +2, "dbar": -1}      # the reading's assignment, to confirm
obs = [("electron", [], 3, F(-1)), ("positron", [], -3, F(1)), ("neutrino", [], 0, F(0)), ("photon", [], 0, F(0)),
       ("up quark", ["u"], 0, F(2, 3)), ("down quark", ["d"], 0, F(-1, 3)),
       ("proton uud", ["u", "u", "d"], 0, F(1)), ("neutron udd", ["u", "d", "d"], 0, F(0)),
       ("pi+ u dbar", ["u", "dbar"], 0, F(1)), ("pi0 (u ubar)", ["u", "ubar"], 0, F(0)),
       ("pi- d ubar", ["d", "ubar"], 0, F(-1))]
ok = True
for name, qs, lepton, q_obs in obs:
    thirds = lepton + sum(quark[x] for x in qs)
    q = F(-thirds, 3)
    ok &= q == q_obs
    say(f"   {name:13s} signed thirds {thirds:+d} -> Q = {str(q):5s} observed {str(q_obs):5s} {'ok' if q == q_obs else 'NO'}")
say(f"   every row agrees: {ok}. Under this reading the up quark is two thirds of the handedness opposite the electron's")
say("   and the down quark one third of the electron's; 3Q + (signed thirds) = 0 holds exactly, not only mod 3.")
say("   Her words 'one third is negative, two thirds is positive' fit if the two thirds are of the opposite handedness;")
say("   'one is neutral' is not placed by this reading (to ask).")

path = os.path.join(OUT, "strand_answers_look_2026-10-24.txt")
open(path, "w", encoding="utf-8").write("\n".join(lines) + "\n")
print("written", path)


def rotation_order(axis):
    """largest n such that the rotation by 360/n degrees about `axis` maps the cubic lattice onto itself"""
    a = np.array(axis, float) / np.linalg.norm(axis)
    K = np.array([[0, -a[2], a[1]], [a[2], 0, -a[0]], [-a[1], a[0], 0]])
    for n in range(12, 0, -1):
        t = 2 * np.pi / n
        R = np.eye(3) + np.sin(t) * K + (1 - np.cos(t)) * K @ K
        if np.allclose(R, np.rint(R), atol=1e-9) and np.allclose(np.abs(np.linalg.det(np.rint(R))), 1):
            return n
    return None


def tape_positions(axis):
    """planes holding the axis and one lattice direction of the cube (edges, face and body diagonals): how many distinct"""
    a = np.array(axis, float) / np.linalg.norm(axis)
    dirs = [np.array(v, float) for v in itertools.product((-1, 0, 1), repeat=3) if any(v)]
    normals = []
    for v in dirs:
        n = np.cross(a, v)
        if np.linalg.norm(n) < 1e-9:
            continue
        n /= np.linalg.norm(n)
        if not any(abs(abs(n @ m) - 1) < 1e-9 for m in normals):
            normals.append(n)
    return len(normals)


say("\n4. The cube's turns about each kind of diagonal (exact, by testing rotations against the lattice)")
for name, ax in (("body diagonal (1,1,1)", (1, 1, 1)), ("face diagonal (1,1,0)", (1, 1, 0)), ("edge (1,0,0)", (1, 0, 0))):
    n = rotation_order(ax)
    say(f"   {name}: the lattice maps onto itself every 360/{n} = {360 // n} degrees; "
        f"distinct lattice planes through it: {tape_positions(ax)}")
orders = {name: rotation_order(ax) for name, ax in (("body", (1, 1, 1)), ("face", (1, 1, 0)))}
say(f"   Read: the smallest symmetric turn about a body diagonal is 1/{orders['body']} of a full turn, about a face")
say(f"   diagonal 1/{orders['face']}. Thirds on body diagonals and halves on face diagonals "
    + ("are the cube's own turns." if orders == {"body": 3, "face": 2} else "are NOT what the cube gives."))

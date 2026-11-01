"""Sandbox look, 1 November 2026 (a look: it can kill, not crown). The entropic route to a pull, at its one-step order.

Question: do two curled relics in flat four-link space change each other's room to move? The hard-core rule forbids
most switches beside a saturated link (sandbox/forbidden_volume.py, 22 October: 12 to 13 % allowed round a curled ring
against 34 to 35 % round its uncurled twin). If that forbidden volume is the mechanism of the entropy penalty on curl
(T78, T79), then the one-step proxy of an ENTROPIC INTERACTION between two relics is: the number of valid switches
available to the surroundings of the pair, minus the sum for each relic alone. Zero beyond contact means no entropic
pull at this order; a dependence on separation means the surroundings feel both.

Relic: a short handle (eq45_geometrize_check.handle_graph with h = 3, its two splices three lattice steps apart), which
holds one curled ring (four links at three squares) and sits as a local object of 12 points in the flat torus. Two of
them are placed on the 20 x 20 torus at separations r = 2 .. 9 along y (r = lattice steps between the splice squares).
Exact per graph: free links within one step of the relics' points, every pair tried as a switch, valid ones counted
(graphity.cqg.is_valid), and the energy H = 16 (N - S) + 4 lam X at lam = 1.25 (O22 predicts exact additivity beyond
contact). Output: sandbox/out/pair_handles_look_2026-11-01.txt
"""
import itertools
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(HERE), "src"))
sys.path.insert(0, HERE)
from graphity.cqg import NO_CAP, is_valid, surplus, torus, total_squares  # noqa: E402
from graphity.objects import count_rings                                   # noqa: E402
from graphity.squares import squares_on_edge                               # noqa: E402

LX = LY = 20
H = 3
LAM = 1.25


def two_handles(sep):
    """Flat torus with handle A spliced at (0,0)-(3,0) and handle B at (0,sep)-(3,sep); None if sep too small."""
    adj0, part0 = torus(LX, LY, NO_CAP)
    n0 = LX * LY
    nb = [list(map(int, adj0[v])) for v in range(n0)]
    side = list(map(int, part0))
    segs = []

    def add_handle(at_a, at_b):
        base = len(nb)
        for t in range(H):
            for j in range(4):
                nb.append([])
                side.append((t + j) % 2)
        seg = lambda t, j: base + 4 * t + (j % 4)  # noqa: E731
        for t in range(H):
            for j in range(4):
                nb[seg(t, j)].extend([seg(t, j + 1), seg(t, j - 1)])
                if t + 1 < H:
                    nb[seg(t, j)].append(seg(t + 1, j))
                    nb[seg(t + 1, j)].append(seg(t, j))

        def splice(x0, y0, layer):
            lab = lambda x, y: (x % LX) * LY + (y % LY)  # noqa: E731
            u1, v1, u2, v2 = lab(x0, y0), lab(x0, y0 + 1), lab(x0 + 1, y0 + 1), lab(x0 + 1, y0)
            for a, b in ((u1, v1), (u2, v2)):
                nb[a].remove(b)
                nb[b].remove(a)
            s = side[u1]
            ends_s = [seg(layer, j) for j in range(4) if side[seg(layer, j)] != s]
            ends_o = [seg(layer, j) for j in range(4) if side[seg(layer, j)] == s]
            for p, q in zip(ends_s, (u1, u2)):
                nb[p].append(q); nb[q].append(p)
            for p, q in zip(ends_o, (v1, v2)):
                nb[p].append(q); nb[q].append(p)

        splice(at_a[0], at_a[1], 0)
        splice(at_b[0], at_b[1], H - 1)
        segs.append([seg(t, j) for t in range(H) for j in range(4)])

    add_handle((0, 0), (3, 0))
    if sep is not None:
        add_handle((0, sep), (3, sep))
    adj = np.array(nb, dtype=np.int64)
    return adj, np.array(side, dtype=np.int64), segs


def energy(adj):
    n = adj.shape[0]
    return 16 * (n - int(total_squares(adj))) + 4 * LAM * int(surplus(adj))


def region(adj, pts):
    near = set(pts)
    for p in pts:
        near |= set(map(int, adj[p]))
    return near


def free_links(adj, part, pts):
    near = region(adj, pts)
    out = set()
    for u in near:
        for v in map(int, adj[u]):
            out.add(frozenset((u, v)))
    return [tuple(sorted(l, key=lambda x: part[x])) for l in out]


def switched(adj, e1, e2):
    (a1, b1), (a2, b2) = e1, e2
    if a1 == a2 or b1 == b2:
        return None
    new = adj.copy()
    ra1, ra2 = list(new[a1]), list(new[a2])
    if b2 in ra1 or b1 in ra2:
        return None
    new[a1][ra1.index(b1)] = b2
    new[a2][ra2.index(b2)] = b1
    rb1, rb2 = list(new[b1]), list(new[b2])
    new[b1][rb1.index(a1)] = a2
    new[b2][rb2.index(a2)] = a1
    return new


def count_valid(adj, part, pts):
    F = free_links(adj, part, pts)
    valid = 0
    for e1, e2 in itertools.combinations(F, 2):
        new = switched(adj, e1, e2)
        if new is not None and is_valid(new, NO_CAP):
            valid += 1
    return len(F), valid


def main():
    out = open(os.path.join(HERE, "out", "pair_handles_look_2026-11-01.txt"), "w", encoding="utf-8")
    def say(s):
        print(s); out.write(s + "\n")
    flat, part0 = torus(LX, LY, NO_CAP)
    say("flat %d x %d torus: H = %.1f" % (LX, LY, energy(flat)))
    adj1, part1, segs1 = two_handles(None)
    assert is_valid(adj1, NO_CAP)
    pts1 = set(segs1[0]) | region(adj1, segs1[0])
    F1, V1 = count_valid(adj1, part1, segs1[0])
    E1 = energy(adj1) - energy(flat)
    say("one handle: N = %d, rings = %d, energy above flat = %.1f, free links within one step = %d, valid switches = %d"
        % (adj1.shape[0], count_rings(adj1), E1, F1, V1))
    say("")
    say("%4s %6s %10s %10s %10s %12s" % ("sep", "rings", "E - 2E1", "free", "valid", "valid - 2V1"))
    for sep in range(2, 10):
        adj, part, segs = two_handles(sep)
        if not is_valid(adj, NO_CAP):
            say("%4d  invalid build" % sep); continue
        pts = segs[0] + segs[1]
        F, V = count_valid(adj, part, pts)
        E = energy(adj) - energy(flat)
        say("%4d %6d %10.1f %10d %10d %12d" % (sep, count_rings(adj), E - 2 * E1, F, V, V - 2 * V1))
    out.close()


if __name__ == "__main__":
    main()

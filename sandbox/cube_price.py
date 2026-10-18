"""Sandbox look, 18 October 2026: what a price on cubes (loops of loops, the 3-cell) would count.

The owner's question: "maybe we should be pricing cubes not squares". This counts 3-cubes on the built ladder and,
for every valid single switch from a slab, the change in squares, surplus squares and cubes, so that the opening
move and the breaking moves can be compared under a cube count. No kernel, no run; a look (rule 16).
"""
import sys
from collections import Counter

import numpy as np

sys.path.insert(0, "src")
sys.path.insert(0, "scripts")
from graphity.cqg_d import _switch, is_valid, surplus, torus, total_squares  # noqa: E402
from exact_walls_d import gas, within  # noqa: E402


def nbrs(adj):
    return [set(int(x) for x in row) for row in adj]


def common(nb, a, b, not_v):
    return [x for x in nb[a] & nb[b] if x != not_v]


def cubes(adj):
    """Number of 3-cubes (eight points wired as Q3). Each is seen once from each of its eight corners."""
    nb = nbrs(adj)
    count = 0
    for v in range(adj.shape[0]):
        row = sorted(nb[v])
        for i in range(len(row)):
            for j in range(i + 1, len(row)):
                ab = common(nb, row[i], row[j], v)
                if not ab:
                    continue
                for k in range(j + 1, len(row)):
                    ac = common(nb, row[i], row[k], v)
                    bc = common(nb, row[j], row[k], v)
                    for p in ab:
                        for q in ac:
                            for r in bc:
                                if len({p, q, r}) < 3:
                                    continue
                                far = nb[p] & nb[q] & nb[r]
                                far.discard(row[i]); far.discard(row[j]); far.discard(row[k])
                                count += len(far)
    assert count % 8 == 0, count
    return count // 8


def ladder():
    print("cubes and squares per point on the built ladder (six links)")
    for spec in ((6, 6, 6), (8, 8, 8), (4, 6, 6), (4, 8, 8), (4, 4, 8), (4, 4, 4)):
        adj, part = torus(spec)
        n = adj.shape[0]
        c, s, x = cubes(adj), total_squares(adj), surplus(adj)
        print("  %-10s N=%-4d squares/N=%.3f surplus/N=%.3f cubes/N=%.3f" % ("x".join(map(str, spec)), n, s / n, x / n, c / n))


def switches(spec, lam, near=4):
    adj, part = torus(spec)
    n = adj.shape[0]
    s0, x0, c0 = total_squares(adj), surplus(adj), cubes(adj)
    side0 = np.flatnonzero(part == 0)
    u1 = int(side0[0])
    close = set(within(adj, u1, near).tolist())
    kinds = Counter()
    nbr1 = set(int(v) for v in adj[u1])
    for u2 in side0:
        u2 = int(u2)
        if u2 == u1 or u2 not in close:
            continue
        nbr2 = set(int(v) for v in adj[u2])
        for v1 in adj[u1]:
            v1 = int(v1)
            if v1 in nbr2:
                continue
            for v2 in adj[u2]:
                v2 = int(v2)
                if v2 == v1 or v2 in nbr1:
                    continue
                t = adj.copy()
                _switch(t, u1, v1, u2, v2)
                if not is_valid(t):
                    continue
                kinds[(int(total_squares(t)) - s0, int(surplus(t)) - x0, cubes(t) - c0)] += 1
    print("\nevery valid single switch from the slab %s (one u1, partners within %d), lambda=%.2f" % ("x".join(map(str, spec)), near, lam))
    print("  cost(squares)  dS  dX  dCubes  ways")
    for (ds, dx, dc), k in sorted(kinds.items(), key=lambda kv: (-16 * kv[0][0] + 4 * lam * kv[0][1], kv[0])):
        print("  %10.1f  %3d %3d  %5d  %4d" % (-16.0 * ds + 4.0 * lam * dx, ds, dx, dc, k))


if __name__ == "__main__":
    ladder()
    switches((4, 6, 6), 1.25)
    switches((6, 6, 6), 1.25)

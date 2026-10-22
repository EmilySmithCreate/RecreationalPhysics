"""Sandbox look, 22 October 2026: how rare are the two objects of the curl-against-flat test in the published model's
warm equilibrium graphs? (Feasibility only, on the already-read T36 graphs; the registered test runs fresh chains.)

Objects, both touching nine squares:
  * the curled ring: a square a-b-c-d whose four links each carry three squares (the column of paper 2, in kind);
  * the flat patch: a 4 x 4 grid of 16 distinct points with its 24 grid links present, i.e. nine squares in a 3 x 3
    block. Built cell by cell: the first row and first column are free walks; every other cell x[i][j] is the unique
    common neighbour of x[i-1][j] and x[i][j-1] other than x[i-1][j-1]. Ordered (corner, two directions) tuples are
    counted and divided by 8, the symmetries of a square grid.
Check: the flat 14 x 14 torus has 196 patches and no ring.

Usage: python3 sandbox/curl_vs_flat_feasibility.py
"""
import glob
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, "src"))
from graphity.cqg import NO_CAP, torus  # noqa: E402
from graphity.squares import squares_on_edge  # noqa: E402

K = 4   # grid side in points: 4 x 4 points = 3 x 3 squares


def nbrs(adj):
    return [set(int(x) for x in row) for row in adj]


def common_other(nb, a, b, *exclude):
    return [x for x in nb[a] & nb[b] if x not in exclude]


def rings(adj, nb):
    """Squares whose four links each carry three squares, each counted once."""
    n = adj.shape[0]
    seen = set()
    for a in range(n):
        for b in nb[a]:
            if squares_on_edge(adj, a, b) < 3:
                continue
            for d in nb[a]:
                if d == b or squares_on_edge(adj, a, d) < 3:
                    continue
                for c in common_other(nb, b, d, a):
                    if squares_on_edge(adj, b, c) == 3 and squares_on_edge(adj, c, d) == 3:
                        seen.add(frozenset((a, b, c, d)))
    return len(seen)


def patches(nb):
    """Number of K x K grids (unordered), from ordered tuples / 8."""
    n = len(nb)
    cells = [(i, j) for i in range(K) for j in range(K)]      # fill order: row by row

    def extend(grid, used, idx):
        if idx == len(cells):
            return 1
        i, j = cells[idx]
        if i == 0 and j == 0:
            raise RuntimeError
        if i == 0:                                           # first row: a free walk
            cands = [v for v in nb[grid[(0, j - 1)]] if v not in used]
        elif j == 0:                                         # first column: a free walk
            cands = [v for v in nb[grid[(i - 1, 0)]] if v not in used]
        else:
            cands = [v for v in common_other(nb, grid[(i - 1, j)], grid[(i, j - 1)], grid[(i - 1, j - 1)])
                     if v not in used]
        total = 0
        for v in cands:
            grid[(i, j)] = v
            used.add(v)
            total += extend(grid, used, idx + 1)
            used.discard(v)
            del grid[(i, j)]
        return total

    tuples = 0
    for x00 in range(n):
        tuples += extend({(0, 0): x00}, {x00}, 1)
    return tuples / 8


def main():
    adj, part = torus(14, 14, NO_CAP)
    nb = nbrs(adj)
    print("flat 14 x 14 torus: rings %d, patches %.1f (expect 0 and 196)" % (rings(adj, nb), patches(nb)))
    adj, part = torus(16, 4, NO_CAP)
    nb = nbrs(adj)
    print("curled 16 x 4 torus: rings %d, patches %.1f (expect 16 rings; patches: 4 x 4 grids that wrap the short side"
          " are not 16 distinct points, so 0)" % (rings(adj, nb), patches(nb)))
    files = sorted(glob.glob(os.path.join(ROOT, "results", "t36_allotropes_n196_adj", "*.npz")))
    picked = [f for f in files if ("snap200" in f or "snap400" in f) and any(("_rep%d_" % r) in f for r in range(4))]
    tot = {}
    for f in picked:
        z = np.load(f)
        adj = z["adj"].astype(np.int64)
        nb = nbrs(adj)
        name = os.path.basename(f)[:-4]
        g = name.split("_")[0]
        r, p = rings(adj, nb), patches(nb)
        tot.setdefault(g, [0, 0.0, 0])
        tot[g][0] += r
        tot[g][1] += p
        tot[g][2] += 1
        print("  %-32s rings %d  patches %.0f" % (name, r, p))
    for g, (r, p, k) in tot.items():
        print("%s: %d graphs, rings %d (%.3f per graph), patches %.0f (%.2f per graph)" % (g, k, r, r / k, p, p / k))


if __name__ == "__main__":
    main()

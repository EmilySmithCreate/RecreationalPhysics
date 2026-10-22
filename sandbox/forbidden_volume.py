"""Sandbox look, 22 October 2026 (rule 16: a look; it can kill, not crown). After T79 (PENALTY ON CURL, O148): is the
curled ring's extra entropy loss the hard-core rule's doing? A link carrying three squares admits no fourth square and
no K_{2,3}, so switches near it that would be valid near a flat link are forbidden. If so, the surroundings of a
curled ring should have fewer valid moves available than the surroundings of a flat object of the same size.

Measure, exact per graph: for an object with point set P, the neighbourhood links are the links with at least one
endpoint within one step of P, less the object's own links ("free links", F). Every unordered pair of free links is
tried as a switch (both orientations that keep sides); counted: valid switches, and valid switches that leave the
object intact (its links present with the same square counts). Reported per free link, per object type, per coupling.
Objects: ring3 (curled), ring2 (its uncurled twin), flat 3 x 4 and 4 x 4 grids (no grid link above two squares).
Graphs: the saved snapshots of T78 (results/t78_curl_vs_flat_n196_g*_adj/, every 100th) and T36.

Usage: python3 sandbox/forbidden_volume.py > sandbox/out/forbidden_volume_2026-10-22.txt
"""
import glob
import itertools
import os
import random
import sys
from collections import defaultdict

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, "src"))
from graphity.cqg import NO_CAP, is_valid  # noqa: E402
from graphity.squares import squares_on_edge  # noqa: E402

MAX_PER_TYPE = 3          # flat objects sampled per graph; rings all
random.seed(2026_10_22)


def nbrs(adj):
    return [set(int(x) for x in row) for row in adj]


def squares_all(adj, nb):
    """Every square as a 4-tuple (a, b, c, d) in cyclic order, each once."""
    out = set()
    n = adj.shape[0]
    for a in range(n):
        for b in nb[a]:
            for d in nb[a]:
                if d <= b:
                    continue
                for c in nb[b] & nb[d]:
                    if c != a:
                        out.add(frozenset(((a, b), (b, c), (c, d), (d, a))) if False else tuple(sorted((a, b, c, d))) + ((a, b, c, d),))
    # dedupe by point set (a square is determined by its four points in a bipartite hard-core graph)
    seen = {}
    for *_, cyc in out:
        seen[frozenset(cyc)] = cyc
    return list(seen.values())


def ring_instances(adj, nb, k):
    """Squares whose four links each carry exactly k squares (k = 3: ring3; k = 2: ring2)."""
    inst = []
    for a, b, c, d in squares_all(adj, nb):
        links = [(a, b), (b, c), (c, d), (d, a)]
        if all(squares_on_edge(adj, u, v) == k for u, v in links):
            inst.append(dict(points=[a, b, c, d], links=links))
    return inst


def grid_instances(adj, nb, a, b):
    """a x b flat grids (no grid link above two squares), as point grids; deduped by point set."""
    found = {}
    n = adj.shape[0]

    def common_other(x, y, z):
        return [w for w in nb[x] & nb[y] if w != z]

    def extend(grid, used, i, j):
        if i == a:
            pts = frozenset(used)
            if pts not in found:
                found[pts] = [row[:] for row in grid]
            return
        ni, nj = (i, j + 1) if j + 1 < b else (i + 1, 0)
        if i == 0 and j > 0:
            cands = [v for v in nb[grid[0][j - 1]] if v not in used]
        elif j == 0 and i > 0:
            cands = [v for v in nb[grid[i - 1][0]] if v not in used]
        else:
            cands = [v for v in common_other(grid[i - 1][j], grid[i][j - 1], grid[i - 1][j - 1]) if v not in used]
        for v in cands:
            grid[i][j] = v
            used.add(v)
            extend(grid, used, ni, nj)
            used.discard(v)

    for x00 in range(n):
        grid = [[-1] * b for _ in range(a)]
        grid[0][0] = x00
        extend(grid, {x00}, 0, 1)
    inst = []
    for pts, grid in found.items():
        links = []
        for i in range(a):
            for j in range(b):
                if j + 1 < b:
                    links.append((grid[i][j], grid[i][j + 1]))
                if i + 1 < a:
                    links.append((grid[i][j], grid[i + 1][j]))
        if all(squares_on_edge(adj, u, v) <= 2 for u, v in links):
            inst.append(dict(points=sorted(pts), links=links))
    return inst


def free_links(adj, nb, part, obj):
    near = set(obj["points"])
    for p in obj["points"]:
        near |= nb[p]
    own = {frozenset(l) for l in obj["links"]}
    out = set()
    for u in near:
        for v in nb[u]:
            l = frozenset((u, v))
            if l not in own:
                out.add(l)
    # orient as (side-0 end, side-1 end)
    return [tuple(sorted(l, key=lambda x: part[x])) for l in out]


def switched(adj, e1, e2):
    (a1, b1), (a2, b2) = e1, e2
    if a1 == a2 or b1 == b2:
        return None
    new = adj.copy()
    row_a1, row_a2 = list(new[a1]), list(new[a2])
    if b2 in row_a1 or b1 in row_a2:
        return None
    new[a1][row_a1.index(b1)] = b2
    new[a2][row_a2.index(b2)] = b1
    rb1, rb2 = list(new[b1]), list(new[b2])
    new[b1][rb1.index(a1)] = a2
    new[b2][rb2.index(a2)] = a1
    return new


def intact(new, obj, counts):
    for (u, v), c in zip(obj["links"], counts):
        if v not in new[u] or squares_on_edge(new, u, v) != c:
            return False
    return True


def measure(adj, nb, part, obj):
    F = free_links(adj, nb, part, obj)
    counts = [squares_on_edge(adj, u, v) for u, v in obj["links"]]
    valid = keep = 0
    pairs = 0
    for e1, e2 in itertools.combinations(F, 2):
        pairs += 1
        new = switched(adj, e1, e2)
        if new is None or not is_valid(new, NO_CAP):
            continue
        valid += 1
        if intact(new, obj, counts):
            keep += 1
    return len(F), pairs, valid, keep


def main():
    files = []
    for g in (3300, 3433, 3550, 3697):
        files += sorted(glob.glob(os.path.join(ROOT, "results", "t78_curl_vs_flat_n196_g%d_adj" % g, "*.npz")))
    files += sorted(glob.glob(os.path.join(ROOT, "results", "t36_allotropes_n196_adj", "*.npz")))
    acc = defaultdict(lambda: defaultdict(list))        # g -> type -> list of (F, pairs, valid, keep)
    for f in files:
        z = np.load(f)
        adj, part = z["adj"].astype(np.int64), z["part"].astype(np.int64)
        nb = nbrs(adj)
        g = int(os.path.basename(f).split("_")[0][1:]) / 1000.0
        objs = {"ring3": ring_instances(adj, nb, 3), "ring2": ring_instances(adj, nb, 2),
                "flat_3x4": grid_instances(adj, nb, 3, 4), "flat_4x4": grid_instances(adj, nb, 4, 4)}
        for t, inst in objs.items():
            if t != "ring3" and len(inst) > MAX_PER_TYPE:
                inst = random.sample(inst, MAX_PER_TYPE)
            for o in inst:
                acc[g][t].append(measure(adj, nb, part, o))
    print("valid switches among the free links round an object, per free link; and the share of those that keep the object")
    print("%6s %-9s %5s %8s %8s %10s %10s %12s" % ("g", "object", "n", "free", "pairs", "valid/F", "keep/F", "keep/valid"))
    for g in sorted(acc):
        for t in ("ring3", "ring2", "flat_3x4", "flat_4x4"):
            rows = acc[g][t]
            if not rows:
                print("%6.3f %-9s %5d" % (g, t, 0))
                continue
            F = np.array([r[0] for r in rows], float); P = np.array([r[1] for r in rows], float)
            V = np.array([r[2] for r in rows], float); K = np.array([r[3] for r in rows], float)
            print("%6.3f %-9s %5d %8.1f %8.1f %10.3f %10.3f %12.3f   (keep/F sd %.3f)"
                  % (g, t, len(rows), F.mean(), P.mean(), (V / F).mean(), (K / F).mean(), (K.sum() / V.sum()), (K / F).std()))


if __name__ == "__main__":
    main()

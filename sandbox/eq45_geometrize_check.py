"""Sandbox check, 23 October 2026 (rule 16: a look, not a result; it can kill, not crown). BUILT GRAPHS ONLY.

Is the operational curvature reading proposed in docs/design/eq45_ratio_brief.md (the Sec. IV.2 geometrization of
[T25] applied point by point) well defined on the toy's built graphs, and what does it read on each?

The reading, as the brief's "current definitions" box states it (PROPOSED, not yet read back to the owner):
  * corner: an unordered pair of a point's four links; its cycle length c is 2 + the shortest path between the two
    neighbours that avoids the point (BFS); no path gives c = infinity.
  * rotation: one of the three ways to pair the four links into two "opposite" pairs; its four corners are the other
    four pairs. The point's rotation is the one whose four corner cycles give the smallest angle sum parameter
    alpha = sum (k - 2) / k ([T25] Eq. (25)); ties are counted and broken by the lexicographically smallest sorted type.
  * vertex type: the sorted four corner lengths (k1, k2, k3, k4) of the chosen rotation.
  * K at the point: -x^2 in units of 1 / l^2, where x = l / R solves [T25] Eq. (27),
        sum_i 2 arcsin( cos(pi / k_i) / cosh(x / 2) ) = 2 pi,
    by bisection (x = 0 when alpha = 2; the k = infinity term uses cos(pi / k) = 1). Euclidean excess angle
    eps = pi (alpha - 2) is reported beside it.
  * face consistency: the share of chosen corners whose shortest cycle is also a chosen corner at every other point of
    that cycle (1.0 means the local rule is a global 2-cell embedding on these graphs).
  * sum of eps / pi over all points (added 23 October, after the adversarial check): on any consistent map,
    sum_v (alpha_v - 2) = sum_f (k_f - 2) - 2V = -2 chi (4-regular, so E = 2V), so the integrated excess angle is
    topological: 0 on a torus, +2 pi for a cross-cap, +4 pi for a handle, whatever the handle's length.

Graphs: the flat 14 x 14 torus; the tube 4 x 36 and 16 x 4; the 4-cube (4 x 4); the finite Fig. 7 tiling of
scripts/build_planted_allotrope.py (240 points, three squares and a hexagon at every point: the text's own homogeneous
hyperbolic case, a positive control); a curled ring built into the flat 14 x 14 torus as a short circumference-4
handle (a tube segment of h layers, h = 3 and 5, spliced into two cut links far apart); and (added 23 October) the
finite Fig. 9 allotropes of build_planted_allotrope.build_all (a fold, i.e. a cross-cap, and a handle in the Fig. 7
tiling; the same handle surgery on the flat torus), a positive control for the sign of Fig. 9's caption ("a higher
absolute curvature"). Nothing is read from results/.

Usage: python3 sandbox/eq45_geometrize_check.py > sandbox/out/eq45_geometrize_check_2026-10-23.txt
"""
import math
import os
import sys
from collections import Counter, deque

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, "src"))
sys.path.insert(0, os.path.join(ROOT, "scripts"))

from graphity.cqg import NO_CAP, is_valid, torus, total_squares, surplus          # noqa: E402
from graphity.objects import count_rings                                          # noqa: E402
from graphity.squares import squares_on_edge                                      # noqa: E402
from build_planted_allotrope import background, build_all, square_counts           # noqa: E402

INF = 10 ** 9
PAIRS = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
# the three rotations, each given by its two opposite pairs; the corners are the other four pairs
ROTATIONS = [((0, 1), (2, 3)), ((0, 2), (1, 3)), ((0, 3), (1, 2))]


def shortest_cycle_through_corner(adj, v, a, b):
    """2 + the shortest path from a to b in the graph with v removed; INF if none."""
    if a == b:
        return INF
    n = adj.shape[0]
    dist = np.full(n, -1, dtype=np.int64)
    dist[a] = 0
    q = deque([a])
    while q:
        x = q.popleft()
        if x == b:
            return int(dist[x]) + 2
        for y in adj[x]:
            y = int(y)
            if y == v or dist[y] >= 0:
                continue
            dist[y] = dist[x] + 1
            q.append(y)
    return INF


def angle_term(k):
    """(k - 2) / k, the share of pi in a regular Euclidean k-gon's interior angle; 1 for k = infinity."""
    return 1.0 if k >= INF else (k - 2.0) / k


def solve_x(ktype):
    """x = l / R solving Eq. (27) for the vertex type; 0 if the Euclidean angle sum is already 2 pi."""
    def total(x):
        s = 0.0
        for k in ktype:
            c = 1.0 if k >= INF else math.cos(math.pi / k)
            s += 2.0 * math.asin(min(1.0, c / math.cosh(x / 2.0)))
        return s
    alpha = sum(angle_term(k) for k in ktype)
    if alpha <= 2.0 + 1e-12:
        return 0.0
    lo, hi = 0.0, 10.0
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        if total(mid) > 2.0 * math.pi:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def geometrize(adj):
    """Per point: vertex type, alpha, eps, K, tie flag, and the chosen corner cycles (for consistency)."""
    n = adj.shape[0]
    corner_len = np.zeros((n, 6), dtype=np.int64)
    for v in range(n):
        for p, (i, j) in enumerate(PAIRS):
            corner_len[v, p] = shortest_cycle_through_corner(adj, v, int(adj[v, i]), int(adj[v, j]))
    types, alphas, epss, ks, ties, chosen = [], [], [], [], [], []
    for v in range(n):
        options = []
        for opp in ROTATIONS:
            corners = [p for p, pr in enumerate(PAIRS) if pr not in opp]
            ktype = tuple(sorted(int(corner_len[v, p]) for p in corners))
            alpha = sum(angle_term(k) for k in ktype)
            options.append((round(alpha, 12), ktype, corners))
        options.sort()
        tie = len(options) > 1 and options[0][0] == options[1][0] and options[0][1] != options[1][1]
        alpha, ktype, corners = options[0]
        x = solve_x(ktype)
        types.append(ktype)
        alphas.append(alpha)
        epss.append(math.pi * (alpha - 2.0))
        ks.append(-x * x)
        ties.append(tie)
        chosen.append(corners)
    return dict(types=types, alpha=np.array(alphas), eps=np.array(epss), K=np.array(ks), ties=np.array(ties),
                chosen=chosen, corner_len=corner_len)


def shortest_cycle_points(adj, v, a, b):
    """The points of one shortest cycle through corner a - v - b (BFS with parents); None if none."""
    n = adj.shape[0]
    parent = np.full(n, -2, dtype=np.int64)
    parent[a] = -1
    q = deque([a])
    while q:
        x = q.popleft()
        if x == b:
            path = [b]
            while parent[path[-1]] >= 0:
                path.append(int(parent[path[-1]]))
            return [v] + path
        for y in adj[x]:
            y = int(y)
            if y == v or parent[y] != -2:
                continue
            parent[y] = x
            q.append(y)
    return None


def face_consistency(adj, geo):
    """Share of chosen finite corners whose shortest cycle is a chosen corner at every other point on it."""
    n = adj.shape[0]
    chosen_pairs = [set() for _ in range(n)]
    for v in range(n):
        for p in geo["chosen"][v]:
            i, j = PAIRS[p]
            chosen_pairs[v].add(frozenset((int(adj[v, i]), int(adj[v, j]))))
    good = total = 0
    for v in range(n):
        for p in geo["chosen"][v]:
            if geo["corner_len"][v, p] >= INF:
                continue
            i, j = PAIRS[p]
            cyc = shortest_cycle_points(adj, v, int(adj[v, i]), int(adj[v, j]))
            total += 1
            ok = True
            m = len(cyc)
            for t in range(m):
                w, prev, nxt = cyc[t], cyc[(t - 1) % m], cyc[(t + 1) % m]
                if frozenset((prev, nxt)) not in chosen_pairs[w]:
                    ok = False
                    break
            good += ok
    return good / total if total else float("nan")


def two_colour(adj):
    n = adj.shape[0]
    col = np.full(n, -1, dtype=np.int64)
    for s in range(n):
        if col[s] >= 0:
            continue
        col[s] = 0
        q = deque([s])
        while q:
            x = q.popleft()
            for y in adj[x]:
                y = int(y)
                if col[y] < 0:
                    col[y] = 1 - col[x]
                    q.append(y)
                elif col[y] == col[x]:
                    return None
    return col


def handle_graph(lx, ly, h, at_a=(0, 0), at_b=None):
    """The flat lx x ly torus with a circumference-4 tube segment of h layers spliced in as a handle.

    At each end two parallel vertical lattice links bounding one lattice square are cut, and the four freed ends are
    joined to the four points of the segment's end layer, side to opposite side. The segment's layers 1 .. h - 2 are
    curled rings (each of their links carries three squares: the ring itself and one square to each neighbouring
    layer). The end layers carry two links with one square each (the splice's uncurl)."""
    adj0, part0 = torus(lx, ly, NO_CAP)
    n0 = lx * ly
    n = n0 + 4 * h
    nb = [list(map(int, adj0[v])) for v in range(n0)] + [[] for _ in range(4 * h)]
    seg = lambda t, j: n0 + 4 * t + (j % 4)                               # noqa: E731
    side = list(map(int, part0)) + [(t + j) % 2 for t in range(h) for j in range(4)]
    for t in range(h):
        for j in range(4):
            nb[seg(t, j)].extend([seg(t, j + 1), seg(t, j - 1)])
            if t + 1 < h:
                nb[seg(t, j)].append(seg(t + 1, j))
                nb[seg(t + 1, j)].append(seg(t, j))
    if at_b is None:
        at_b = (lx // 2, ly // 2)

    def splice(x0, y0, layer):
        lab = lambda x, y: (x % lx) * ly + (y % ly)                          # noqa: E731
        u1, v1, u2, v2 = lab(x0, y0), lab(x0, y0 + 1), lab(x0 + 1, y0 + 1), lab(x0 + 1, y0)
        for a, b in ((u1, v1), (u2, v2)):
            nb[a].remove(b)
            nb[b].remove(a)
        s = side[u1]                                   # u1 and u2 share a side; v1 and v2 the other
        ends_s = [seg(layer, j) for j in range(4) if side[seg(layer, j)] != s]       # must join a side-s point
        ends_o = [seg(layer, j) for j in range(4) if side[seg(layer, j)] == s]
        for p, q in zip(ends_s, (u1, u2)):
            nb[p].append(q)
            nb[q].append(p)
        for p, q in zip(ends_o, (v1, v2)):
            nb[p].append(q)
            nb[q].append(p)

    splice(at_a[0], at_a[1], 0)
    splice(at_b[0], at_b[1], h - 1)
    adj = np.array(nb, dtype=np.int64)
    assert adj.shape == (n, 4), adj.shape
    return adj, np.array(side, dtype=np.int64), [seg(t, j) for t in range(h) for j in range(4)]


def report(name, adj, groups=None):
    n = adj.shape[0]
    ok = bool(is_valid(adj, NO_CAP))
    col = two_colour(adj)
    print("=" * 100)
    print("%s: N = %d, valid (4-regular, simple, hard-core) = %s, bipartite = %s, S = %d, X = %d, rings = %d"
          % (name, n, ok, col is not None, int(total_squares(adj)), int(surplus(adj)), int(count_rings(adj))))
    link_census = Counter()
    for u in range(n):
        for v in adj[u]:
            if int(v) > u:
                link_census[int(squares_on_edge(adj, u, int(v)))] += 1
    print("  links by squares carried:", dict(sorted(link_census.items())))
    geo = geometrize(adj)
    census = Counter(tuple("inf" if k >= INF else k for k in t) for t in geo["types"])
    print("  vertex types (sorted corner cycle lengths) and counts:")
    for t, c in sorted(census.items(), key=lambda kv: -kv[1]):
        k = geo["K"][[i for i, tt in enumerate(geo["types"]) if tuple("inf" if x >= INF else x for x in tt) == t][0]]
        print("    %-24s %5d points   alpha = %.4f   eps = %.4f   K = %+.5f (1/l^2)"
              % (str(t), c, sum(angle_term(INF if x == "inf" else x) for x in t),
                 math.pi * (sum(angle_term(INF if x == "inf" else x) for x in t) - 2.0), k))
    print("  ties in the rotation choice: %d of %d points" % (int(geo["ties"].sum()), n))
    print("  mean K over all points = %+.5f; min %+.5f; max %+.5f" % (geo["K"].mean(), geo["K"].min(), geo["K"].max()))
    print("  face consistency (chosen corners whose cycle is chosen at every point of it) = %.4f" % face_consistency(adj, geo))
    print("  sum of eps / pi over all points (Gauss-Bonnet: -2 chi on a consistent map) = %.4f" % (geo["eps"].sum() / math.pi))
    if groups:
        for gname, pts in groups.items():
            pts = list(pts)
            print("  %-34s %4d points: mean K = %+.5f, mean eps = %.4f, types %s"
                  % (gname, len(pts), geo["K"][pts].mean(), geo["eps"][pts].mean(),
                     dict(Counter(tuple("inf" if k >= INF else k for k in geo["types"][p]) for p in pts))))
    return geo


def main():
    print("eq45_geometrize_check, 23 October 2026: the proposed point-by-point Sec. IV.2 reading on BUILT graphs only.")
    print("K is in units of 1/l^2: -x^2 with x = l/R from [T25] Eq. (27); eps = pi (alpha - 2), alpha from Eq. (25).")
    adj, _ = torus(14, 14, NO_CAP)
    report("flat torus 14 x 14", adj)
    adj, _ = torus(4, 36, NO_CAP)
    report("tube 4 x 36 (one direction curled to circumference 4)", adj)
    adj, _ = torus(16, 4, NO_CAP)
    report("tube 16 x 4", adj)
    adj, _ = torus(4, 4, NO_CAP)
    report("4-cube (4 x 4 torus, both directions curled)", adj)
    adj, _ = background(240)
    report("finite Fig. 7 tiling, 240 points (three squares and a hexagon at every point)", adj)
    for h in (3, 5):
        adj, side, seg = handle_graph(14, 14, h)
        n0 = 14 * 14
        layers = {t: seg[4 * t:4 * t + 4] for t in range(h)}
        ring_layers = [t for t in range(1, h - 1)]
        mid = ring_layers[len(ring_layers) // 2]
        ring_obj = layers[mid - 1] + layers[mid] + layers[mid + 1]            # the ring and the 8 points its squares touch
        touched = set()
        for p in seg:
            touched.update(int(x) for x in adj[p])
        splice_pts = sorted(touched - set(seg))                               # the eight lattice points joined to the segment
        near = set(splice_pts)
        for p in splice_pts:
            near.update(int(x) for x in adj[p])
        far = [v for v in range(n0) if v not in near]
        groups = {"middle ring's 12 points (ring + touched)": ring_obj,
                  "middle ring's own 4 points": layers[mid],
                  "segment end layers (8 points)": layers[0] + layers[h - 1],
                  "spliced lattice points (8)": splice_pts,
                  "lattice points beyond 1 step of splice": far}
        report("flat 14 x 14 torus with a %d-layer circumference-4 handle (curled ring built in)" % h, adj, groups)
    # Fig. 9 positive control (added 23 October): the planted allotropes of build_planted_allotrope.build_all. The
    # region is the points whose square count differs from the background's; the caption says it has "a higher
    # absolute curvature" than the tiling around it.
    for name, (adj, _part, bg_c) in build_all(240, 14).items():
        q = square_counts(adj)
        groups = {}
        reg = [int(v) for v in np.flatnonzero(q != bg_c)]
        rest = [int(v) for v in np.flatnonzero(q == bg_c)]
        if reg:
            groups["allotrope region (square count != %d)" % bg_c] = reg
        groups["background points (square count %d)" % bg_c] = rest
        report("build_planted_allotrope.build_all: %s" % name, adj, groups)
    print("=" * 100)
    print("done")


if __name__ == "__main__":
    main()

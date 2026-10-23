"""Sandbox look, 23 October 2026 (rule 16: a look; it can kill, not crown). Checks made while correcting the Eq. (45)
ratio brief (docs/design/eq45_ratio_brief.md, handoff item 2.3): Eq. (27) curvatures for vertex types, object counts on
the flat 14 x 14 torus, Gauss-Bonnet sums and the Fig. 9 control on built graphs, and, on fresh warm chains with NEW
seeds (not T78's; no saved state is opened), how many points lie at distance >= 2 from every 2 x 2 sighting (the support
of the background the brief's first draft used). Written by an assistant agent; kept here so the look can be rerun.

Usage: python3 sandbox/eq45_background_support.py
"""
import math
import os
import sys
from collections import Counter, deque

import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "src"))
sys.path.insert(0, os.path.join(ROOT, "scripts"))
sys.path.insert(0, os.path.join(ROOT, "sandbox"))

from eq45_geometrize_check import geometrize, face_consistency, solve_x, angle_term, INF   # noqa: E402
from graphity.cqg import NO_CAP, torus, run_chain, total_squares, surplus                 # noqa: E402
from graphity.objects import count_grid, count_ring2, count_rings                        # noqa: E402
from graphity.squares import squares_on_edge                                             # noqa: E402
from build_planted_allotrope import build_all, square_counts                             # noqa: E402

I = INF
print("== Eq. (27) K for types")
for t in [(4, 4, 6, 8), (4, 4, 4, 100), (4, 4, 4, 12), (4, 4, 6, 6), (4, 4, 4, I), (4, 4, 8, 8), (4, 6, 6, 6),
          (4, 4, 6, I), (6, 6, 6, 6), (4, 4, I, I), (4, 4, 4, 6), (4, 4, 4, 8), (I, I, I, I)]:
    a = sum(angle_term(k) for k in t)
    x = solve_x(t)
    print("  %-22s alpha %.4f  K %+.4f" % (str(tuple('inf' if k >= I else k for k in t)), a, -x * x))
print("  -4 ln(1+sqrt2)^2 =", -4 * math.log(1 + math.sqrt(2)) ** 2)

print("== counts on the flat 14 x 14 torus")
adj, part = torus(14, 14, NO_CAP)
for a, b in [(2, 2), (2, 3), (2, 4), (3, 3), (3, 4), (3, 5), (4, 4), (4, 5)]:
    print("  grid %dx%d: %d" % (a, b, count_grid(adj, a, b, True)))
print("  ring2: %d  ring3: %d" % (count_ring2(adj), count_rings(adj)))

print("== interior fractions (a-2)(b-2)/ab")
for a, b in [(2, 2), (2, 3), (2, 4), (3, 3), (3, 4), (3, 5), (4, 4), (4, 5)]:
    print("  %dx%d: %d/%d" % (a, b, (a - 2) * (b - 2), a * b))

print("== build_all: Gauss-Bonnet sums and the Fig. 9 control")
for name, (adj, part, bg_c) in build_all(240, 14).items():
    geo = geometrize(adj)
    q = square_counts(adj)
    reg = np.flatnonzero(q != bg_c)
    rest = np.flatnonzero(q == bg_c)
    print("  %-22s N=%4d ties=%d cons=%.3f sum eps/pi=%.4f | region %d pts q=%s meanK=%s | rest meanK=%+.4f types=%s"
          % (name, adj.shape[0], int(geo["ties"].sum()), face_consistency(adj, geo), geo["eps"].sum() / math.pi,
             len(reg), dict(Counter(q[reg].tolist())), ("%+.4f" % geo["K"][reg].mean()) if len(reg) else "-",
             geo["K"][rest].mean(),
             dict(Counter(tuple('inf' if k >= I else k for k in geo['types'][p]) for p in reg))))

print("== sandbox handle graphs: Gauss-Bonnet")
from eq45_geometrize_check import handle_graph  # noqa: E402
for h in (3, 5):
    adj, side, seg = handle_graph(14, 14, h)
    geo = geometrize(adj)
    print("  h=%d: sum eps/pi = %.4f, X = %d" % (h, geo["eps"].sum() / math.pi, int(surplus(adj))))


def square_points_flat2(adj):
    """Points on at least one square whose four links each carry <= 2 squares (a 2 x 2 flat grid sighting)."""
    n = adj.shape[0]
    on = np.zeros(n, dtype=bool)
    nb = [set(int(x) for x in adj[v]) for v in range(n)]
    for a in range(n):
        for b in nb[a]:
            for d in nb[a]:
                if d <= b:
                    continue
                for c in nb[b] & nb[d]:
                    if c == a:
                        continue
                    sq = (a, b, c, d)
                    links = [(a, b), (b, c), (c, d), (d, a)]
                    if all(squares_on_edge(adj, u, v) <= 2 for u, v in links):
                        on[list(sq)] = True
    return on


def dist_from(adj, mask):
    n = adj.shape[0]
    d = np.full(n, -1)
    q = deque()
    for v in np.flatnonzero(mask):
        d[v] = 0
        q.append(int(v))
    while q:
        x = q.popleft()
        for y in adj[x]:
            y = int(y)
            if d[y] < 0:
                d[y] = d[x] + 1
                q.append(y)
    return d


print("== fresh warm chains (NEW seeds, not T78's), N = 196, lambda = 1: the background support")
for g in (3.3, 3.697):
    sup, onsq, rhos, qs = [], [], [], []
    for rep in range(4):
        adj, part = torus(14, 14, NO_CAP)
        side_u = np.flatnonzero(part == 0)
        run_chain(adj, side_u, 0.0, 200, 1, 990000 + rep + int(g * 1000), 1.0, NO_CAP, False)
        run_chain(adj, side_u, 1.0 / g, 20000, 1, -1, 1.0, NO_CAP, False)
        for s in range(5):
            run_chain(adj, side_u, 1.0 / g, 0, 1000, -1, 1.0, NO_CAP, False)
            n = adj.shape[0]
            S, X = int(total_squares(adj)), int(surplus(adj))
            D = 4 * (n - S) + X
            rhos.append(D / n)
            qs.append(4 * S / n)
            on = square_points_flat2(adj)
            onsq.append(on.mean())
            d = dist_from(adj, on)
            sup.append(int(((d >= 2) | (d < 0)).sum()))
    print("  g=%.3f: rho %.3f, mean squares/point %.3f, share of points on a 2x2 sighting %.3f, points at distance >= 2"
          " from every 2x2 sighting per snapshot: mean %.2f (max %d) of 196"
          % (g, np.mean(rhos), np.mean(qs), np.mean(onsq), np.mean(sup), max(sup)))

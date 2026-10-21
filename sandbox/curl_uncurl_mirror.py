"""Sandbox look, 21 October 2026 (exact for what it tries; a look, not a result). The owner's hypothesis of the same day
(VISION Update 80): curl is matter and uncurl antimatter. Matter and antimatter are measured to have equal masses, so
the question asked here is exact: does the toy's energy treat a curl and an uncurl as mirror images?

Written link by link (VISION Update 5; Q1), the energy above flat is H = 4 D + 4 (lambda - 1) X, with D the missing
squares (sum over links of max(0, 2 - S_e)) and X the surplus (sum of max(0, S_e - 2)).

Part A, the prices per link, from the form alone: what a link costs per square missing and per square extra, how far
each side can go, and at which lambda (if any) the two sides price alike.

Part B, the defects a flat 8 x 8 torus can reach: every valid one switch, and every valid pair of switches near one
point (first switch on links within one step of point 0, second within two steps), read for (D, X). Reported: how many
defects carry curl only, missing squares only, or both; the cheapest of each at lambda = 1.10, 1.25, 1.40; and for each
(D, X) class with curl only and each with missing squares only, the lambda at which a curl-only and a missing-only
class would cost the same.

Usage: python3 sandbox/curl_uncurl_mirror.py > sandbox/out/curl_uncurl_mirror_2026-10-21.txt
"""
import itertools
import sys
from collections import Counter

sys.path.insert(0, "src")
from graphity.cqg import NO_CAP, is_valid, surplus, torus  # noqa: E402
from graphity.row_growth import edge_census  # noqa: E402

L = 8
LAMS = (1.10, 1.25, 1.40)

print("Part A: prices per link (from H = 4 D + 4 (lambda - 1) X)")
print("  a link missing one square: 4; missing two (S_e = 0): 8, the most a link can be missing in two directions")
print("  a link on one extra square (S_e = 3): 4 (lambda - 1); one extra is the most a link can carry (S_e <= 3, [T25])")
print("  equal per square only at lambda = 2; and the ranges differ (two missing against one extra), so no lambda makes")
print("  the per-link energy symmetric under curl <-> uncurl. With six links (flat S_e = 4, at most 5; Q21) the ranges")
print("  differ more: four missing against one extra.")
for lam in LAMS:
    print(f"  lambda = {lam:.2f}: one extra square costs {4*(lam-1):.2f} per link against 4 per missing square, ratio 1 : {1/(lam-1):.1f}")

adj0, part = torus(L)
n = adj0.shape[0]


def links_near(adj, r):
    """Links with an endpoint within r steps of point 0, as (side-0 end, side-1 end)."""
    dist = {0: 0}
    frontier = [0]
    for d in range(1, r + 1):
        nxt = []
        for u in frontier:
            for v in adj[u]:
                v = int(v)
                if v not in dist:
                    dist[v] = d
                    nxt.append(v)
        frontier = nxt
    out = set()
    for u in dist:
        for v in adj[u]:
            v = int(v)
            a, b = (u, v) if part[u] == 0 else (v, u)
            out.add((a, b))
    return sorted(out)


def switched(adj, e1, e2):
    """(a1,b1),(a2,b2) -> (a1,b2),(a2,b1); None if it would repeat a link or join a point to itself."""
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


def classify(adj):
    d, _, _ = edge_census(adj)
    x = int(surplus(adj))
    return int(d), x


singles = Counter()
all_links = links_near(adj0, L)                      # every link
for e1, e2 in itertools.combinations(all_links, 2):
    g = switched(adj0, e1, e2)
    if g is not None and is_valid(g, NO_CAP):
        singles[classify(g)] += 1

doubles = Counter()
first = links_near(adj0, 1)
second = links_near(adj0, 2)
for e1, e2 in itertools.combinations(first, 2):
    g1 = switched(adj0, e1, e2)
    if g1 is None or not is_valid(g1, NO_CAP):
        continue
    near = links_near(g1, 2)
    for f1, f2 in itertools.combinations(near, 2):
        g2 = switched(g1, f1, f2)
        if g2 is not None and is_valid(g2, NO_CAP):
            doubles[classify(g2)] += 1


def report(name, census):
    print(f"\nPart B, {name}: {sum(census.values())} valid defects, by (D missing, X extra) -> count")
    for (d, x), c in sorted(census.items()):
        kind = "flat" if d == x == 0 else ("curl only" if d == 0 else ("missing only" if x == 0 else "both"))
        e = "  ".join(f"H({lam:.2f})={4*d + 4*(lam-1)*x:.1f}" for lam in LAMS)
        print(f"  D={d:2d} X={x:2d}  {c:6d}  {kind:12s} {e}")
    kinds = Counter()
    for (d, x), c in census.items():
        kinds["flat" if d == x == 0 else ("curl only" if d == 0 else ("missing only" if x == 0 else "both"))] += c
    print("  totals:", dict(kinds))
    curl_only = [k for k in census if k[0] == 0 and k[1] > 0]
    miss_only = [k for k in census if k[1] == 0 and k[0] > 0]
    if curl_only and miss_only:
        for (_, xc) in curl_only:
            for (dm, _) in miss_only:
                print(f"  a curl-only class X={xc} and a missing-only class D={dm} cost the same at lambda = {1 + dm / xc:.3f}")
    else:
        print("  no pair of a curl-only class and a missing-only class to compare: "
              + ("no curl-only defect" if not curl_only else "no missing-only defect"))


report("one switch", singles)
report("two switches near one point", doubles)

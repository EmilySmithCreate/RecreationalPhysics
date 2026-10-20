"""Sandbox look, 20 October 2026, follow-up to knot_halo.py: in the first ring round each knot (points one step from a
knot point), is the flat total of squares made of links over and under two that cancel? Per point: the squares on each
of its four links, sorted; counted over T51's states at N = 512 and 1,024 (not the held-out 2,048). Exact; a look.
"""
import sys
from collections import Counter

import numpy as np

sys.path.insert(0, "src")
sys.path.insert(0, "scripts")
from graphity.coupled import graph_distances  # noqa: E402
from graphity.cqg import squares_on_edge  # noqa: E402
from run_t75 import is_connected, knot_points, load_states  # noqa: E402

for run in ("t51_l128_10k", "t51_l256_300k"):
    ring, links_to_knot = Counter(), Counter()
    total_off = 0
    for path, adj, part, rep in load_states("results", run):
        if not is_connected(adj):
            continue
        kp = knot_points(adj)
        if kp.size == 0:
            continue
        ks = set(kp.tolist())
        dist = graph_distances(adj, kp)
        for v in np.flatnonzero(dist == 1):
            s = tuple(sorted(squares_on_edge(adj, int(v), int(w)) for w in adj[v]))
            ring[s] += 1
            if sum(s) != 8:
                total_off += 1
            for w in adj[v]:
                if int(w) in ks:
                    links_to_knot[squares_on_edge(adj, int(v), int(w))] += 1
    print(f"\n{run}: first-ring points by the squares on their four links (sorted), count")
    for s, c in ring.most_common():
        print(f"   {s}: {c}")
    print(f"   points whose four links do not total 8 squares: {total_off}")
    print(f"   squares on the ring's links into the knot: {dict(sorted(links_to_knot.items()))}")

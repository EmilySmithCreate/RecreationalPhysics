"""Sandbox look, 20 October 2026: is there a balancing halo of curvature around the burp's knots? (The owner's gravity
idea of the same night: space curves to balance matter's curling toward neutral.)

On T51's saved end states (the burp's product: spaces opened from several seeds and cooled) at N = 512 (length 128,
10k cooling) and N = 1,024 (length 256, 300k cooling), for every point outside the knots: its distance to the nearest
knot point, its share of H (T55's per-point split e(v), zero for a perfectly flat point), the squares on its links less
the flat 8, and, for a sample, the cheapest positive-cost switch at it (T75's flaw rule). Binned by distance. The
held-out size of T75 (N = 2,048) is not read. Exact for each state; a look, not evidence.
"""
import sys
from collections import defaultdict

import numpy as np

sys.path.insert(0, "src")
sys.path.insert(0, "scripts")
from graphity.coupled import cheapest_switch_at, graph_distances  # noqa: E402
from graphity.cqg import squares_on_edge  # noqa: E402
from analyse_t55 import point_energy  # noqa: E402
from run_t75 import is_connected, knot_points, load_states  # noqa: E402

LAM = 1.25
RUNS = [("t51_l128_10k", 512), ("t51_l256_300k", 1024)]
SAMPLE_PER_BIN = 3          # cheapest-switch samples per distance bin per state
MAX_STATES = 12             # states per run for the cheapest-switch sample

for run, n in RUNS:
    states = [s for s in load_states("results", run) if is_connected(s[1])]
    e_bin, sq_bin, cost_bin = defaultdict(list), defaultdict(list), defaultdict(list)
    n_knotted = 0
    rng = np.random.default_rng(20261020)
    for i, (path, adj, part, rep) in enumerate(states):
        kp = knot_points(adj)
        if kp.size == 0:
            continue
        n_knotted += 1
        dist = graph_distances(adj, kp)
        for v in range(adj.shape[0]):
            dv = int(dist[v])
            if dv <= 0:
                continue
            b = min(dv, 9)
            e_bin[b].append(point_energy(adj, v, LAM))
            sq_bin[b].append(sum(squares_on_edge(adj, v, int(w)) for w in adj[v]) - 8)
        if n_knotted <= MAX_STATES:
            for b in (1, 2, 3, 4, 6, 8):
                cand = np.flatnonzero(dist == b) if b < 9 else np.flatnonzero(dist >= 9)
                for v in rng.choice(cand, size=min(SAMPLE_PER_BIN, cand.size), replace=False):
                    res = cheapest_switch_at(adj, int(v), lam=LAM, reach=3, avoid=kp, above=0.0)
                    if res is not None:
                        cost_bin[b].append(res[2])
    print(f"\n{run} (N = {n}): {len(states)} connected states, {n_knotted} with knots")
    print(" dist | points | mean e(v) | share e(v) != 0 | mean squares - 8 | cheapest flaw: n, mean, min")
    for b in sorted(e_bin):
        e = np.array(e_bin[b]); q = np.array(sq_bin[b]); c = np.array(cost_bin.get(b, []))
        lab = f"{b}" if b < 9 else ">=9"
        cs = f"{c.size:3d} {c.mean():6.1f} {c.min():5.0f}" if c.size else "  -"
        print(f" {lab:>4} | {e.size:6d} | {e.mean():9.3f} | {np.mean(e != 0):15.3f} | {q.mean():16.3f} | {cs}")

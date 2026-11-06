"""A look (sandbox lane), exact, no run: the correlation C(r) of T83's quantity on a flat 32 x 32 sheet holding ONE
defect cluster, made by a single valid switch (or two, far apart). If a lone defect alone gives C(3) of the size the
LONG cells of T83 stage 1 show (0.07 to 0.15), then what those cells measure is the defect's own footprint by graph
distance, not curl felt through flat sheet."""
import numpy as np
from graphity.cqg import NO_CAP, is_valid, torus, _switch, _new_edge_ok
from graphity.correlation import correlation_by_distance, correlation_curve, edge_squares

rng = np.random.default_rng(1)
adj, part = torus(32, 32, NO_CAP)
n = adj.shape[0]

def one_switch(adj, rng, cap=NO_CAP):
    # pick two disjoint edges u1-v1, u2-v2 with u on side 0 and switch to u1-v2, u2-v1 if valid (as the chain does)
    for _ in range(100000):
        u1, u2 = rng.choice(np.flatnonzero(part == 0), 2, replace=False)
        v1 = adj[u1, rng.integers(4)]; v2 = adj[u2, rng.integers(4)]
        if v1 == v2 or v1 in adj[u2] or v2 in adj[u1]:
            continue
        _switch(adj, u1, v1, u2, v2)
        if is_valid(adj, cap):
            return (u1, v1, u2, v2)
        _switch(adj, u1, v2, u2, v1)      # undo
    raise RuntimeError

for k in (1, 2, 4):
    adj, part = torus(32, 32, NO_CAP)
    for _ in range(k):
        one_switch(adj, rng)
    num, count, ev, phi, diam = correlation_by_distance(adj, 16)
    c = correlation_curve(num, count, ev)
    flat = np.mean(edge_squares(adj) == 2)
    print("%d switch(es): flat share %.4f  C(1..6) = %s" % (k, flat, np.round(c[1:7], 3)))

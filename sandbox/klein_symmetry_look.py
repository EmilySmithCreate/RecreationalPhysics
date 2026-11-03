"""Sandbox look: renamings (side-preserving automorphisms) of the flat torus against its Klein-bottle relative (O150), 4 x L. Exact; not a result."""
import sys
sys.path.insert(0, "src"); sys.path.insert(0, "scripts")
import numpy as np
from math import exp
from graphity.cqg import NO_CAP, torus, is_valid
from graphity.small_graphs import log_automorphisms, sides_first
from read_flat_kind import klein_bottle
for L in (8, 12, 16):
    t_adj, t_part = torus(4, L, NO_CAP)
    k = klein_bottle(4, L)
    k_adj, k_part = (k if isinstance(k, tuple) else (k, None))
    if k_part is None:
        import networkx as nx
        g = nx.Graph([(u, int(v)) for u in range(len(k_adj)) for v in k_adj[u] if v >= 0])
        col = nx.bipartite.color(g); k_part = np.array([col[i] for i in range(len(k_adj))])
    print(f"4 x {L}: torus valid {is_valid(t_adj, NO_CAP)} renamings {exp(log_automorphisms(sides_first(t_adj, t_part))):.0f};  klein valid {is_valid(k_adj, NO_CAP)} renamings {exp(log_automorphisms(sides_first(k_adj, k_part))):.0f}")

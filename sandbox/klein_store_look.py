"""Sandbox look (kill but not crown), 4 November 2026: the owner's reflection seam (a two-degree-of-freedom Klein bottle
holding two dark-matter rings) set against the toy's Klein relative (O150, read_flat_kind.klein_bottle). Exact; nothing
here is a result. Expectation written first: the Klein wiring is bipartite, so every square has one black and one white
diagonal (wiring_is_paired True) and it cannot hold a surplus kind in its wiring any more than the torus can; its energy
is a fixed seam cost that does not grow with L, against the tube's 4(lambda - 1) per point."""
import sys
sys.path.insert(0, "src"); sys.path.insert(0, "scripts")
import numpy as np, networkx as nx
from graphity.cqg import NO_CAP, torus, is_valid, hamiltonian
from graphity.curl_pairs import squares, wiring_is_paired
from graphity.dimension import local_dimension
from read_flat_kind import klein_bottle
for L in (8, 12, 16, 24):
    k = klein_bottle(4, L); adj = k[0] if isinstance(k, tuple) else k
    g = nx.Graph([(u, int(v)) for u in range(len(adj)) for v in adj[u] if v >= 0])
    col = nx.bipartite.color(g); part = np.array([col[i] for i in range(len(adj))])
    t_adj, t_part = torus(4, L, NO_CAP)
    d = local_dimension(adj)
    print(f"4 x {L}: klein valid {is_valid(adj, NO_CAP)} bipartite {nx.is_bipartite(g)} squares {len(squares(adj, part))} "
          f"paired {wiring_is_paired(adj, part)} H(1.25) {hamiltonian(adj, 1.25):.0f} H(1.10) {hamiltonian(adj, 1.10):.0f} "
          f"points not flat {int((d != 2).sum())} | tube H(1.25) {hamiltonian(t_adj, 1.25):.0f}")

"""The two exploratory shape readers of 11 October 2026 (scripts/read_open_shells.py, scripts/read_endpoint_width.py):
the shells and the width on tori whose answers are known, and on one saved end state."""
import sys
from pathlib import Path

import networkx as nx
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from read_endpoint_width import is_flat, twisted_tube, width      # noqa: E402
from read_open_shells import profile, shells, torus               # noqa: E402


def graph(adj):
    return nx.Graph((i, int(j)) for i in range(adj.shape[0]) for j in adj[i])


def squares_on_each_edge(adj):
    """Brute force with networkx: for every edge, the number of squares through it."""
    g = graph(adj)
    return {sum(1 for a in g[u] if a != v for b in g[v] if b not in (u, a) and g.has_edge(a, b)) for u, v in g.edges()}


def test_shells_of_known_tori():
    assert shells(torus((4, 4, 18)), 0) == [1, 6, 16, 26, 31, 32, 32, 32, 32, 31, 26, 16, 6, 1]
    assert shells(torus((6, 6, 8)), 0) == [1, 6, 18, 36, 53, 60, 53, 36, 18, 6, 1]
    for dims in ((4, 12), (6, 16), (4, 8, 8)):
        adj = torus(dims)
        counted = shells(adj, 5)
        assert sum(counted) == adj.shape[0]
        by_networkx = nx.single_source_shortest_path_length(graph(adj), 5)
        assert counted == [list(by_networkx.values()).count(r) for r in range(len(counted))]


def test_a_rod_and_flat_space_are_told_apart_by_their_largest_shell():
    rod, flat = profile(torus((4, 4, 18))), profile(torus((6, 6, 8)))
    assert rod[0] == 32 and flat[0] == 60                     # twice the rod's cross-section; flat space's widest shell
    assert rod[1] == 13 and flat[1] == 10                     # the rod's far end is farther away


def test_width_is_the_shortest_way_round():
    for dims, expected in (((4, 12), 4), ((6, 16), 6), ((8, 8), 8), ((8, 12), 8), ((12, 16), 12)):
        adj = torus(dims)
        assert width(adj) == expected
        assert is_flat(adj) == (min(dims) >= 6)


def test_the_tube_with_its_seam_shifted_by_two_is_flat_and_six_round():
    for length in (16, 24, 48):
        tube, twisted = twisted_tube(length, 0), twisted_tube(length, 2)
        assert nx.is_isomorphic(graph(tube), graph(torus((4, length))))
        assert squares_on_each_edge(tube) == {2, 3} and not is_flat(tube) and width(tube) == 4
        assert squares_on_each_edge(twisted) == {2} and is_flat(twisted) and width(twisted) == 6
        assert nx.is_bipartite(graph(twisted)) and set(dict(graph(twisted).degree()).values()) == {4}
        assert shells(twisted, 0)[:6] == [1, 4, 8, 9, 8, 8]   # eight points at each distance: still a tube


def test_a_saved_flat_end_state_is_that_twisted_tube():
    """ASSUMPTIONS O116: one saved end state of T60 (lambda = 1.05, N = 64), read from its wiring."""
    saved = np.load(ROOT / "results" / "t60_lam105_n64_adj" / "N64_rep0.npz")["adj"]
    assert is_flat(saved) and width(saved) == 6
    assert nx.is_isomorphic(graph(saved), graph(twisted_tube(16, 2)))

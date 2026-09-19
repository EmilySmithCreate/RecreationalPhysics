"""Checks on the 2D combinatorial quantum gravity kernel."""
import networkx as nx
import numpy as np
import pytest

from graphity.cqg import is_valid, run_chain, squares_on_edge, torus, total_squares


def to_nx(adj):
    g = nx.Graph()
    for u in range(adj.shape[0]):
        for v in adj[u]:
            g.add_edge(u, int(v))
    return g


def brute_squares(g):
    return sum(1 for c in nx.simple_cycles(g, length_bound=4) if len(c) == 4)


def test_torus_is_the_ground_state():
    adj, part = torus(6)
    assert is_valid(adj)
    assert total_squares(adj) == 36                       # S = N, so H = 16 (N - S) = 0
    assert all(squares_on_edge(adj, u, int(v)) == 2 for u in range(36) for v in adj[u])


def test_four_cube_is_excluded():
    with pytest.raises(ValueError):
        torus(4)                                          # 4x4 torus = Q4, three squares per edge (Q3)


def test_chain_stays_in_configuration_space():
    adj, part = torus(8)
    side_u = np.flatnonzero(part == 0)
    for inv_g, seed in [(0.0, 1), (0.3, 2)]:
        s, acc = run_chain(adj, side_u, inv_g, 20, 20, seed)
        g = to_nx(adj)
        assert is_valid(adj)
        assert all(d == 4 for _, d in g.degree())
        assert nx.is_bipartite(g)
        assert all(part[u] != part[v] for u, v in g.edges())   # bipartition preserved
        assert s[-1] == total_squares(adj) == brute_squares(g)  # incremental count is exact
        assert 0 < acc < 1


def test_melts_at_infinite_temperature():
    adj, part = torus(10)
    s, _ = run_chain(adj, np.flatnonzero(part == 0), 0.0, 300, 50, 3)
    assert s.mean() / 100 < 0.25                           # far from the ordered value S/N = 1


def test_same_seed_same_result():
    runs = []
    for _ in range(2):
        adj, part = torus(6)
        runs.append(run_chain(adj, np.flatnonzero(part == 0), 0.2, 5, 20, 42)[0])
    assert np.array_equal(runs[0], runs[1])

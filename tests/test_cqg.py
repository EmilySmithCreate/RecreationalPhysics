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


def test_rectangular_torus():
    """TASKS T1: the 16 x 10 torus, N = 160 as in [T25] Fig. 3."""
    adj, part = torus(16, 10)
    g = to_nx(adj)
    assert adj.shape == (160, 4)
    assert all(d == 4 for _, d in g.degree())             # 4-regular
    assert nx.is_bipartite(g)
    assert all(part[u] != part[v] for u, v in g.edges())  # and `part` is a valid two-colouring
    assert part.sum() == 80                               # equal halves
    assert total_squares(adj) == brute_squares(g) == 160  # S = N, checked independently
    assert all(squares_on_edge(adj, u, int(v)) == 2 for u in range(160) for v in adj[u])
    assert is_valid(adj)


def test_square_torus_is_unchanged():
    """torus(L) must stay exactly what it was, slot order included, or old seeds stop reproducing."""
    adj, part = torus(10)
    adj2, part2 = torus(10, 10)
    assert np.array_equal(adj, adj2) and np.array_equal(part, part2)
    assert list(adj[0]) == [10, 90, 1, 9]                 # +x, -x, +y, -y


def test_short_or_odd_sides_are_refused():
    for lx, ly in [(16, 4), (4, 16), (7, 10), (10, 7)]:   # a side of 4 wraps into extra squares
        with pytest.raises(ValueError):
            torus(lx, ly)


def test_chain_runs_on_a_rectangle_and_melts_to_the_published_floor():
    """Hot-phase square density at N = 160 against the published 0.126 [T25 Fig. 3].

    This is the floor only. It depends on which graphs are allowed, not on the
    energy, so it is NOT Gate B. Our value is 0.120, about 5 % BELOW the published
    one; the hard-core rule (Q2) causes the deficit, the cap does not (open issue O5).
    """
    adj, part = torus(16, 10)
    s, _ = run_chain(adj, np.flatnonzero(part == 0), 0.0, 300, 700, 5)
    assert is_valid(adj)
    assert s[-1] == total_squares(adj) == brute_squares(to_nx(adj))
    floor = s.mean() / 160
    assert abs(floor - 0.126) < 0.01                      # Gate B's tolerance, met with little room
    assert abs(floor - 0.120) < 0.004                     # our own value: guards the rules and the sampler


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

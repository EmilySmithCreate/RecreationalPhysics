"""Tests of graphity.u1 (ASSUMPTIONS Q29): squares against networkx, gauge invariance, Gauss's law on a closed graph,
the linear waves on flat tori, energy conservation, the Monte Carlo's local update against full recomputation,
same-seed reproducibility, and the reproduction gate against the exact two-direction answer."""
import itertools

import networkx as nx
import numpy as np
import pytest

from graphity import cqg_d, u1


def _graph(adj):
    G = nx.Graph()
    for x in range(len(adj)):
        for y in adj[x]:
            G.add_edge(x, int(y))
    return G


@pytest.mark.parametrize("dims", [(6, 6), (8, 10), (4, 8), (6, 6, 6), (4, 4, 6)])
def test_squares_are_every_four_cycle(dims):
    adj, part = cqg_d.torus(dims)
    f = u1.Field(adj, part)
    brute = {frozenset(c) for c in nx.simple_cycles(_graph(adj), length_bound=4) if len(c) == 4}
    mine = {frozenset(s) for s in f.squares}
    assert mine == brute
    assert f.n_squares == len(brute) == cqg_d.total_squares(adj)
    # every square's four links are links of the graph, and each link's tail is of kind 0
    assert np.all(part[f.tail] == 0) and np.all(part[f.head] == 1)


def test_flat_torus_squares_are_the_plaquettes_and_a_curl_adds_its_own():
    assert u1.Field(*cqg_d.torus((6, 6))).n_squares == 36
    assert u1.Field(*cqg_d.torus((6, 6, 6))).n_squares == 3 * 216
    # a side of 4 is curled: each ring round it is one more square
    assert u1.Field(*cqg_d.torus((4, 8))).n_squares == 32 + 8


def test_holonomy_is_gauge_invariant():
    rng = np.random.default_rng(1)
    f = u1.Field(*cqg_d.torus((6, 8)))
    th = rng.uniform(-np.pi, np.pi, f.n_links)
    alpha = rng.uniform(-10, 10, f.n)
    assert np.allclose(f.holonomy(f.gauge(th, alpha)), f.holonomy(th), atol=1e-12)
    assert f.potential(f.gauge(th, alpha)) == pytest.approx(f.potential(th), abs=1e-9)


@pytest.mark.parametrize("dims", [(6, 6), (6, 6, 6), (4, 8)])
def test_charges_on_a_closed_graph_add_to_zero(dims):
    rng = np.random.default_rng(2)
    f = u1.Field(*cqg_d.torus(dims))
    assert abs(f.charge(rng.normal(size=f.n_links)).sum()) < 1e-10
    z = rng.integers(0, 3, f.n_links)
    assert int(np.rint(f.charge(z)).astype(int).sum()) % 3 == 0


@pytest.mark.parametrize("dims", [(8, 8), (6, 6, 6)])
def test_linear_waves_on_flat_tori(dims):
    f = u1.Field(*cqg_d.torus(dims))
    d = len(dims)
    ev = np.sort(np.linalg.eigvalsh(f.mode_matrix()))
    assert int(np.sum(ev < 1e-9)) == f.n - 1 + d          # gauge modes plus one holonomy per direction
    pred = []
    for k in itertools.product(*[2 * np.pi * np.arange(s) / s for s in dims]):
        w2 = 4 * np.sum(np.sin(np.array(k) / 2) ** 2)
        if w2 > 1e-12:
            pred += [w2] * (d - 1)                        # d - 1 polarisations
    assert np.allclose(np.sort(pred), ev[ev > 1e-9], atol=1e-9)
    assert ev.max() <= 4 * d + 1e-9                        # fastest phase change bounded: omega <= 2 sqrt(d)


def test_evolution_conserves_energy():
    rng = np.random.default_rng(3)
    f = u1.Field(*cqg_d.torus((6, 6, 6)))
    th = rng.uniform(-1, 1, f.n_links)
    ve = rng.normal(scale=0.5, size=f.n_links)
    e0 = f.energy(th, ve)
    th2, ve2 = f.evolve(th, ve, dt=0.02, steps=500)
    assert abs(f.energy(th2, ve2) - e0) / e0 < 1e-3


def test_local_update_matches_full_recomputation():
    rng = np.random.default_rng(4)
    for dims in [(6, 8), (4, 6, 6)]:
        f = u1.Field(*cqg_d.torus(dims))
        th = rng.uniform(-np.pi, np.pi, f.n_links)
        for _ in range(300):
            l = int(rng.integers(f.n_links))
            d = rng.uniform(-2, 2)
            before = np.sum(np.cos(f.holonomy(th)))
            th2 = th.copy()
            th2[l] += d
            after = np.sum(np.cos(f.holonomy(th2)))
            got = u1.delta_action(th, f.sq_links, f.sq_sign, f.link_sq, f.link_sgn, l, d)
            assert got == pytest.approx(after - before, abs=1e-9)


def test_metropolis_keeps_phases_wrapped_and_is_reproducible():
    f = u1.Field(*cqg_d.torus((6, 6)))
    th0 = np.zeros(f.n_links)
    a = f.metropolis(th0, 1.0, 1.5, 20, 30, seed=11)
    b = f.metropolis(th0, 1.0, 1.5, 20, 30, seed=11)
    c = f.metropolis(th0, 1.0, 1.5, 20, 30, seed=12)
    assert np.array_equal(a[0], b[0]) and np.array_equal(a[1], b[1]) and a[2] == b[2]
    assert not np.array_equal(a[1], c[1])
    assert np.all(a[0] > -np.pi - 1e-12) and np.all(a[0] <= np.pi + 1e-12)
    assert np.array_equal(th0, np.zeros(f.n_links))        # the input is not modified


def test_exact_answer_limits():
    from scipy.special import iv
    # many squares: the torus constraint fades and each square is independent, I1/I0
    assert u1.exact_mean_cos_2d(2.0, 10_000) == pytest.approx(iv(1, 2.0) / iv(0, 2.0), abs=1e-12)
    # few squares at large beta: the constraint matters and the answer differs from I1/I0
    assert abs(u1.exact_mean_cos_2d(8.0, 36) - iv(1, 8.0) / iv(0, 8.0)) > 1e-3


def test_gate_u1_short():
    # a short version of Gate U1: the sampler against the exact answer on the flat 6 x 6 torus
    f = u1.Field(*cqg_d.torus((6, 6)))
    for beta, step in ((1.0, 2.5), (4.0, 1.2)):
        _, series, acc = f.metropolis(np.zeros(f.n_links), beta, step, 500, 4000, seed=5)
        blocks = series.reshape(40, -1).mean(axis=1)
        err = blocks.std(ddof=1) / np.sqrt(len(blocks))
        assert abs(series.mean() - u1.exact_mean_cos_2d(beta, f.n_squares)) < 5 * err + 2e-3
        assert 0.2 < acc < 0.9

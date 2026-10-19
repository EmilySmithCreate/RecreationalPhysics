"""The combined protocol (graphity.layer_feed): conservation to 1e-9 at every row under every move set, the clean
guarantee under "model", same-seed reproducibility, the feed stopping at the first split, the gate's timing, and
validity of the end state by brute force."""
import networkx as nx
import numpy as np
import pytest

from graphity import contraction as C
from graphity import layer_feed as LF
from graphity.cqg_d import is_valid


def brute_ok(state):
    g = nx.Graph()
    for u in range(state.n):
        for v in state.adj[u]:
            g.add_edge(u, int(v))
    assert g.number_of_nodes() == state.n and all(d == 6 for _, d in g.degree()) and nx.is_bipartite(g)
    assert is_valid(state.adj)


@pytest.mark.parametrize("move_set", LF.MOVE_SETS)
def test_conservation_and_same_seed_under_every_move_set(move_set):
    st = C.build((4, 6, 6))
    lam = 1.25
    args = dict(rate=0.1, n_sweeps=120, seed=4, gate=0.0, leak=0.02, move_set=move_set, max_width=8, log_every=1)
    a, rows_a, first_a = LF.run_layer_feed(st, lam, **args)
    b, rows_b, first_b = LF.run_layer_feed(st, lam, **args)
    assert rows_a == rows_b and first_a == first_b
    assert np.array_equal(np.sort(a.adj, axis=1), np.sort(b.adj, axis=1)) and np.array_equal(a.stores, b.stores)
    for res, row in zip(LF.conservation_residuals(first_a["f0"], rows_a), rows_a):
        assert abs(res) < 1e-9 * max(1.0, row[5])
    assert rows_a[-1][7] >= 1                                # with no gate the slab split
    if move_set == "model":
        assert all(row[12] == 0 for row in rows_a)           # the clean guarantee: no broken point in any row
    brute_ok(a)


def test_the_feed_stops_at_the_first_split_and_the_gate_sets_its_time():
    st = C.build((4, 6, 6))
    lam = 1.25
    a = 4.0 * (lam - 1.0)
    gate = a * st.n                                           # g1: the slab's whole curling cost
    rate = 1.0 / 16
    final, rows, first = LF.run_layer_feed(st, lam, rate=rate, n_sweeps=200, seed=9, gate=gate, leak=0.0,
                                           feed_stops_at_split=True, move_set="layer", max_width=6)
    # the pool of a split is two layers (2 L^2 = 72 points) filling at `rate` each: the gate is reached at 2a / r
    assert first["first_split"] is not None and first["first_split"] >= 2 * a / rate
    fed_at = {row[0]: row[5] for row in rows}
    t = first["first_split"]
    assert fed_at[t] == pytest.approx(rate * st.n * t)
    assert rows[-1][5] == fed_at[t]                           # nothing fed after the split
    for res, row in zip(LF.conservation_residuals(first["f0"], rows), rows):
        assert abs(res) < 1e-9 * max(1.0, row[5])
    # the release at the split is the slab's whole curling cost, credited to the stores
    row_t = next(r for r in rows if r[0] == t)
    assert row_t[4] == pytest.approx(row_t[5] - row_t[6] + a * st.n, abs=1e-9)


def test_the_lump_leaves_one_way_into_a_daughter_and_the_slab_reforms():
    """VISION Update 66: a release is never credited to the parent's stores; it is counted in a daughter ledger.
    Conservation holds with the ledger included; the slab reforms from the stores and burps again; every daughter
    carries exactly a N_slab."""
    st = C.build((4, 6, 6))
    lam = 1.25
    a = 4.0 * (lam - 1.0)
    rate = 1.0 / 16
    final, rows, first = LF.run_layer_feed(st, lam, rate=rate, n_sweeps=240, seed=3, gate=a * st.n, leak=0.0,
                                           move_set="layer", max_width=8, release_to="daughter")
    for res, row in zip(LF.conservation_residuals(first["f0"], rows), rows):
        assert abs(res) < 1e-9 * max(1.0, row[5])
    last = rows[-1]
    assert last[13] >= 2 and last[8] >= 1                      # two or more daughters, at least one refold between
    assert last[14] == pytest.approx(last[13] * a * st.n)      # each daughter is exactly a N_slab
    # the parent's books never receive a release: stores + F never exceed what was fed plus the slab's own curl
    for row in rows:
        assert row[3] + row[4] <= first["f0"] + row[5] + 1e-9
    brute_ok(final)

"""Checks on the chain that allows triangles and pentagons (ASSUMPTIONS Q10, Q18).

What cannot be checked here, and why it is said out loud: there is no exactly known
distribution to compare the chain with. The hard-core rule leaves no valid 4-regular graph
below 14 vertices (Q8), and enumerating the states of a 14- or 16-vertex general graph is out
of reach, so the sampling has no exact reference the way `cqg` has one at N = 16 and 18 (Q9).
What is checked: the energy and validity reader against the exact reference already tested in
`test_full_curvature`, that the walk never leaves the valid states, that a seed reproduces a
run, and that the two arrangements this module was written to compare both sit still when cold.
"""
import networkx as nx

from graphity import full_curvature as fc
from graphity import general_chain as gc


def census(g):
    counts = [0, 0, 0]
    for cycle in fc.short_cycles(g):
        counts[len(cycle) - 3] += 1
    return tuple(counts)


def test_read_agrees_with_the_exact_reference():
    """One listing of the short cycles gives what `is_valid`, `energy` and a census give separately."""
    starts = [fc.square_sheet(6, 5), gc.icosidodecahedron(), fc.kagome_sheet(3)]
    hot, _, _ = gc.melt(fc.square_sheet(6, 5), 10, seed=7)           # states a run actually reaches
    starts.append(hot)
    for g in starts:
        valid, h, t, s, p = gc.read(g)
        assert valid == fc.is_valid(g)
        assert h == fc.energy(g)
        assert (t, s, p) == census(g)


def test_the_chain_never_leaves_the_valid_states():
    """4-regular, simple, hard-core rule: every recorded state, hot enough to move a lot."""
    end, rows, acceptance = gc.run(fc.square_sheet(6, 5), 40.0, 20, seed=3)
    assert acceptance > 0.01 and len(rows) == 20
    assert fc.is_valid(end) and all(d == 4 for _, d in end.degree())
    assert end.number_of_nodes() == 30 and end.number_of_edges() == 60


def test_the_same_seed_gives_the_same_run():
    a = gc.run(fc.square_sheet(6, 5), 20.0, 8, seed=11)[1]
    b = gc.run(fc.square_sheet(6, 5), 20.0, 8, seed=11)[1]
    c = gc.run(fc.square_sheet(6, 5), 20.0, 8, seed=12)[1]
    assert a == b and a != c


def test_both_zero_energy_arrangements_sit_still_when_cold():
    """The flat sheet and the closed 30-point piece tie at H = 0 and are both dips (Q10), so a cold
    chain should stay in each: this is the control for the runs that ask whether space refolds."""
    for start, expect in [(fc.square_sheet(6, 5), (0, 30, 6)), (gc.icosidodecahedron(), (20, 0, 12))]:
        assert census(start) == expect and fc.energy(start) == 0
        end, rows, _ = gc.run(start, 1.0, 20, seed=5)
        assert all(r["H"] == 0.0 for r in rows)
        assert census(end) == expect                    # nothing moved, in either arrangement
        assert nx.is_connected(end)


def test_a_sheet_that_wraps_in_an_odd_number_of_steps_carries_free_pentagons():
    """The 6 x 5 sheet has a pentagon down each of its 6 columns and they cost nothing: once an edge
    carries two squares both brackets of the curvature are already at zero, so further loops on it are
    free. Worth pinning, because it is why a 30-point sheet can be compared with the 30-point piece."""
    sheet = fc.square_sheet(6, 5)
    assert census(sheet) == (0, 30, 6) and fc.energy(sheet) == 0 == fc.energy(fc.square_sheet(6, 6))
    # still a dip, but the free pentagons halve the wall: 8 to get out, against 16 on an even sheet
    assert fc.way_out(sheet)[0] == 8 and fc.way_out(fc.square_sheet(6, 6))[0] == 16

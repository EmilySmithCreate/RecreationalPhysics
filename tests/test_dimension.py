"""T7 gate 1: the per-vertex local dimension must read 2 / 1 / 0 on the exact sheet, tube and
4-cube, at every vertex, before it is used on anything else."""
import numpy as np

from graphity.cqg import NO_CAP, torus
from graphity.dimension import local_dimension, pieces_of


def test_sheet_tube_cube_at_every_vertex():
    for shape, want in (((6, 6), 2), ((8, 8), 2), ((16, 4), 1), ((24, 4), 1), ((4, 4), 0)):
        adj, _ = torus(shape[0], shape[1], NO_CAP)
        d = local_dimension(adj)
        assert (d == want).all(), (shape, np.bincount(d))


def test_it_agrees_with_the_square_count_ladder():
    """Design brief: curling a side adds a quarter of a square per vertex and removes one large
    direction. So mean d + squares per vertex is constant across the ladder (2 + 1 = 1 + 1.25 =
    0 + 1.5? no -- but 2 - d equals 4 * (squares per vertex - 1)). Check that relation."""
    from graphity.cqg import total_squares
    for shape in ((6, 6), (16, 4), (4, 4)):
        adj, _ = torus(shape[0], shape[1], NO_CAP)
        n = adj.shape[0]
        d = local_dimension(adj).mean()
        sq = total_squares(adj) / n
        assert abs((2 - d) - 4 * (sq - 1)) < 1e-12, (shape, d, sq)


def test_pieces_of_a_subset():
    adj, _ = torus(8, 8, NO_CAP)
    n = adj.shape[0]
    # one connected 2x2 block of the lattice, plus one isolated vertex far away
    members = np.zeros(n, dtype=bool)
    members[[0, 1, 8, 9]] = True
    members[36] = True
    assert pieces_of(adj, members) == [4, 1]
    assert pieces_of(adj, np.ones(n, dtype=bool)) == [n]
    assert pieces_of(adj, np.zeros(n, dtype=bool)) == []


def test_piece_labels_agree_with_pieces_of():
    """T37: the labels number the same pieces pieces_of sizes."""
    from graphity.dimension import piece_labels
    adj, _ = torus(12, 10, NO_CAP)
    rng = np.random.default_rng(3)
    for _ in range(20):
        members = rng.random(adj.shape[0]) < 0.45
        labels = piece_labels(adj, members)
        assert (labels[~members] == -1).all() and (labels[members] >= 0).all()
        sizes = sorted(np.bincount(labels[labels >= 0]).tolist(), reverse=True) if members.any() else []
        assert sizes == pieces_of(adj, members)


def test_new_seeds_counts_only_pieces_touching_nothing_counted():
    """T37: a new piece is a seed; a piece that grew, split or merged is not; small pieces are ignored."""
    from graphity.dimension import new_seeds
    counted = np.zeros(10, dtype=bool)
    labels = np.array([0, 0, 0, -1, 1, 1, 1, -1, 2, -1])          # two pieces of 3, one of 1
    k, counted = new_seeds(labels, counted, 3)
    assert k == 2 and counted.tolist() == [1, 1, 1, 0, 1, 1, 1, 0, 0, 0]
    labels = np.array([0, 0, 0, 0, 0, 0, 0, -1, -1, -1])          # the two merged: no new seed
    k, counted = new_seeds(labels, counted, 3)
    assert k == 0
    labels = np.array([0, -1, 1, 1, -1, -1, -1, 2, 2, 2])         # a split piece (0, 1) and a new one (2)
    k, counted = new_seeds(labels, counted, 1)
    assert k == 1 and counted[7:].all()

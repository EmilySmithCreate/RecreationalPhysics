"""The local dimension of every vertex, and the connected pieces of a set of vertices.

A vertex has four edges and six pairs of edges. A pair that closes a square is a direction that
has curled back on itself within four steps; a pair that closes none is a direction that stays
large. The count of the latter is the vertex's local dimension: 2 on the flat sheet, 1 on a
tube (one side of the torus curled to length 4), 0 in a 4-cube (VISION Update 7, the design
brief's ladder of dimensions, `test_sheet_tube_cube_ladder`). Here it is computed per vertex,
which is what PREREGISTRATION.md T7 needs: while a tube uncurls into a sheet, which vertices are
already sheet and where they are.
"""
import numpy as np
from numba import njit


@njit(cache=True)
def _share_a_neighbour_other_than(adj, a, b, v):
    """Do a and b have a common neighbour that is not v? (That is, does the pair (v-a, v-b)
    close a square v - a - c - b - v.)"""
    for i in range(4):
        c = adj[a, i]
        if c < 0 or c == v:
            continue
        for j in range(4):
            if adj[b, j] == c:
                return True
    return False


@njit(cache=True)
def local_dimension(adj):
    """d[v] = number of the six edge pairs at v that close no square. Sheet 2, tube 1, cube 0."""
    n = adj.shape[0]
    d = np.zeros(n, dtype=np.int64)
    for v in range(n):
        open_pairs = 0
        for i in range(4):
            a = adj[v, i]
            if a < 0:
                continue
            for j in range(i + 1, 4):
                b = adj[v, j]
                if b < 0:
                    continue
                if not _share_a_neighbour_other_than(adj, a, b, v):
                    open_pairs += 1
        d[v] = open_pairs
    return d


@njit(cache=True)
def _share_d(adj, a, b, v):
    """_share_a_neighbour_other_than at any number of links (the slots are read from the array)."""
    deg = adj.shape[1]
    for i in range(deg):
        c = adj[a, i]
        if c < 0 or c == v:
            continue
        for j in range(deg):
            if adj[b, j] == c:
                return True
    return False


@njit(cache=True)
def local_dimension_d(adj):
    """d[v] at any number of links: the edge pairs at v that close no square, counted over all pairs.

    With four links this is local_dimension (tested). With six, on the cubic lattice, the twelve mixed-axis
    pairs each close a square and the three opposite pairs (+x, -x) close one only along a direction curled
    to length 4, so d is 3 on the flat 3-torus, 2 with one direction curled, 1 with two, 0 in the 6-cube
    (VISION Update 22; ASSUMPTIONS O41). A slot holding -1 (an edge removed mid-move) is skipped.
    """
    n, deg = adj.shape
    d = np.zeros(n, dtype=np.int64)
    for v in range(n):
        open_pairs = 0
        for i in range(deg):
            a = adj[v, i]
            if a < 0:
                continue
            for j in range(i + 1, deg):
                b = adj[v, j]
                if b < 0:
                    continue
                if not _share_d(adj, a, b, v):
                    open_pairs += 1
        d[v] = open_pairs
    return d


def piece_labels(adj, members):
    """Label the connected pieces of the subgraph induced on `members` (a boolean mask).

    Returns an int array over vertices: -1 outside `members`, else the piece's index. The pieces are the ones
    `pieces_of` sizes, numbered in order of their lowest vertex. Added 2026-09-25 for T37, which counts separate
    seeds by asking whether a piece touches any vertex already counted.
    """
    members = np.asarray(members, dtype=bool)
    n = adj.shape[0]
    labels = np.full(n, -1, dtype=np.int64)
    k = 0
    for start in range(n):
        if not members[start] or labels[start] >= 0:
            continue
        stack = [start]
        labels[start] = k
        while stack:
            v = stack.pop()
            for j in range(adj.shape[1]):
                w = adj[v, j]
                if w >= 0 and members[w] and labels[w] < 0:
                    labels[w] = k
                    stack.append(w)
        k += 1
    return labels


def new_seeds(labels, counted, min_size):
    """T37's seed count at one look. `labels` from piece_labels; `counted` a boolean mask of the vertices in pieces
    already counted. A piece with at least `min_size` vertices and no vertex in `counted` is a new seed. Returns
    (the number of new seeds, the updated mask: every vertex in a piece of at least `min_size`, plus the old mask).
    A piece that splits, or one that merges with another, touches counted vertices and is not counted again."""
    n_new = 0
    counted = counted.copy()
    if labels.max() < 0:
        return 0, counted
    sizes = np.bincount(labels[labels >= 0])
    big = np.flatnonzero(sizes >= min_size)
    for k in big:
        members = labels == k
        if not counted[members].any():
            n_new += 1
    keep = np.isin(labels, big)
    counted |= keep
    return n_new, counted


def pieces_of(adj, members):
    """Connected pieces of the subgraph induced on `members` (a boolean mask over vertices).

    Returns the sizes of the pieces, largest first. Used for T7 observable 3: the vertices that
    have already become sheet, and whether they form one front or many scattered patches.
    """
    members = np.asarray(members, dtype=bool)
    n = adj.shape[0]
    seen = np.zeros(n, dtype=bool)
    sizes = []
    for start in range(n):
        if not members[start] or seen[start]:
            continue
        stack, count = [start], 0
        seen[start] = True
        while stack:
            v = stack.pop()
            count += 1
            for k in range(adj.shape[1]):              # any number of links (six-link work, 2026-09-25)
                w = adj[v, k]
                if w >= 0 and members[w] and not seen[w]:
                    seen[w] = True
                    stack.append(w)
        sizes.append(count)
    return sorted(sizes, reverse=True)

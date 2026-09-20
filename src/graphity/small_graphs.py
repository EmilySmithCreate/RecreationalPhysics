"""Every state of the CQG model at the smallest sizes, and whether the edge switch connects them (task T4).

WHAT IS CHECKED. A Monte Carlo chain is only right if its moves can reach every
state (ergodicity; ASSUMPTION Q4 left this open). Here the whole configuration
space is listed for the smallest N, independently of the moves, and compared
with what the moves reach.

THE STATES. 4-regular bipartite graphs on n + n labelled vertices obeying the
hard-core rule (Q2), and the cap if asked for (Q3). Write such a graph as an
n x n table of 0s and 1s, rows for one side and columns for the other, four 1s
in every row and column; the hard-core rule says two rows share at most two
columns and two columns share at most two rows.

WHY RELABELLING DOES NOT MATTER (ours). Everything we measure (S, X, the pieces)
is unchanged when vertices are renamed within their side. Call two states the
same CLASS if such a renaming turns one into the other. Renaming also turns moves
into moves. So if the moves join all classes, then every set of states the chain
can get trapped in is a renamed copy of every other, the averages of our
observables are the same in each copy, and the chain gives the right answer.
Joining all classes is therefore what has to be shown. (It is a weaker demand
than joining all labelled states, and at N = 14 the difference is real: the
chain cannot move at all there, yet there is only one class.)

HOW COMPLETENESS IS PROVED: BY COUNTING (ours).
  1. Count the tables directly. To save work only tables that contain the row
     1111000... and whose rows are in increasing order are counted: G of them.
     Every row pattern is as likely as any other (rename the columns), and a
     table has n different rows that can be ordered in n! ways, so the number of
     labelled states is  L = G * C(n,4) * (n-1)! .
  2. Walk outwards from one state by switches, keeping one representative per
     class. A class whose graph has A side-preserving symmetries contains
     (n!)^2 / A labelled states.
  3. If the classes reached add up to L, nothing was missed: the list is complete
     AND the moves join all of it. If they add up to less, some states cannot be
     reached, and the difference says how many.

networkx does the isomorphism tests; sizes here are tiny. Nothing in the
simulation kernel depends on this module.
"""
from collections import defaultdict
from itertools import combinations
from math import comb, factorial

import networkx as nx
import numpy as np
from networkx.algorithms.isomorphism import GraphMatcher, categorical_node_match
from numba import njit

from graphity.connectivity import connectivity
from graphity.cqg import CAP, NO_CAP, _switch, has_edge, is_valid, squares_on_edge, surplus, total_squares

_SAME_SIDE = categorical_node_match("side", 0)


@njit(cache=True)
def _bits(x):
    count = 0
    while x:
        x &= x - 1
        count += 1
    return count


@njit(cache=True)
def _count_tables(n, masks, cols, cap):
    """Depth-first count of the tables described above. Returns (G, rows of the first one found)."""
    n_masks = masks.shape[0]
    used = np.zeros(n, dtype=np.int64)               # which row pattern sits in each row
    colsum = np.zeros(n, dtype=np.int64)
    shared = np.zeros((n, n), dtype=np.int64)        # rows containing both columns
    adj = np.zeros((2 * n, 4), dtype=np.int64)
    example = np.zeros(n, dtype=np.int64)
    for a in range(4):
        colsum[cols[0, a]] += 1
        for b in range(a + 1, 4):
            shared[cols[0, a], cols[0, b]] += 1
    count = 0
    depth = 1                                        # rows placed so far; row 0 is pattern 0 for good
    nxt = 1
    while depth >= 1:
        placed = False
        if depth < n:
            left = n - depth
            i = nxt
            while i < n_masks and not placed:
                ok = True
                for r in range(depth):               # hard-core rule between rows
                    if _bits(masks[i] & masks[used[r]]) > 2:
                        ok = False
                        break
                if ok:
                    for a in range(4):
                        if colsum[cols[i, a]] == 4:
                            ok = False
                        for b in range(a + 1, 4):    # hard-core rule between columns
                            if shared[cols[i, a], cols[i, b]] == 2:
                                ok = False
                if ok:
                    for a in range(4):
                        colsum[cols[i, a]] += 1
                    for c in range(n):               # can every column still reach four?
                        if colsum[c] + left - 1 < 4:
                            ok = False
                    if ok:
                        for a in range(4):
                            for b in range(a + 1, 4):
                                shared[cols[i, a], cols[i, b]] += 1
                        used[depth] = i
                        depth += 1
                        nxt = i + 1
                        placed = True
                    else:
                        for a in range(4):
                            colsum[cols[i, a]] -= 1
                i += 1
        if placed and depth == n:
            good = True
            if cap < NO_CAP:                         # the cap needs the finished graph
                fill = np.zeros(n, dtype=np.int64)
                for r in range(n):
                    for a in range(4):
                        c = cols[used[r], a]
                        adj[r, a] = n + c
                        adj[n + c, fill[c]] = r
                        fill[c] += 1
                good = is_valid(adj, cap)
            if good:
                if count == 0:
                    for r in range(n):
                        example[r] = masks[used[r]]
                count += 1
        if placed:
            continue
        depth -= 1                                   # nothing fits here: take the last row back
        if depth >= 1:
            i = used[depth]
            for a in range(4):
                colsum[cols[i, a]] -= 1
                for b in range(a + 1, 4):
                    shared[cols[i, a], cols[i, b]] -= 1
            nxt = i + 1
    return count, example


def count_labelled_states(n, cap=NO_CAP):
    """(number of labelled states L, one state as an adjacency array or None). Step 1 of the docstring."""
    patterns = sorted(sum(1 << c for c in chosen) for chosen in combinations(range(n), 4))
    masks = np.array(patterns, dtype=np.int64)
    cols = np.array([[c for c in range(n) if m >> c & 1] for m in patterns], dtype=np.int64)
    g, example = _count_tables(n, masks, cols, cap)
    if g == 0:
        return 0, None
    return g * comb(n, 4) * factorial(n - 1), table_to_adj([int(m) for m in example], n)


def table_to_adj(rows, n):
    """Rows given as bit patterns over the columns -> the (2n, 4) neighbour array; side A is 0..n-1."""
    adj = np.empty((2 * n, 4), dtype=np.int64)
    fill = [0] * n
    for r, m in enumerate(rows):
        for a, c in enumerate(c for c in range(n) if m >> c & 1):
            adj[r, a] = n + c
            adj[n + c, fill[c]] = r
            fill[c] += 1
    return adj


def sides_first(adj, part):
    """Renumber a graph from anywhere else in the package (e.g. cqg.torus) so that side 0 is 0..n-1.

    Everything in this module assumes that numbering; a graph in another numbering would be
    switched across its own sides, which is not the kernel's move.
    """
    order = np.concatenate([np.flatnonzero(part == 0), np.flatnonzero(part == 1)])
    new_name = np.empty(len(adj), dtype=np.int64)
    new_name[order] = np.arange(len(adj))
    return new_name[adj[order]]


def circulant(n, offsets=(0, 1, 3, 7)):
    """Vertex i of side 0 joined to i + d (mod n) of side 1 for each offset d: a quick valid state by hand.

    With the default offsets and n = 9 every difference between two offsets occurs at most twice, which is
    the hard-core rule; check other choices with cqg.is_valid.
    """
    adj = np.empty((2 * n, 4), dtype=np.int64)
    for i in range(n):
        adj[i] = [n + (i + d) % n for d in offsets]
        adj[n + i] = [(i - d) % n for d in offsets]
    return adj


def _check_numbering(adj):
    n = len(adj) // 2
    if not ((adj[:n] >= n).all() and (adj[n:] < n).all()):
        raise ValueError("side 0 must be vertices 0..n-1 and side 1 the rest; see sides_first()")


def _graph(adj):
    n = len(adj) // 2
    g = nx.Graph()
    g.add_nodes_from((v, dict(side=int(v >= n))) for v in range(2 * n))
    g.add_edges_from((u, int(v)) for u in range(n) for v in adj[u])
    return g


def _fingerprint(adj):
    """Cheap numbers that renaming cannot change; classes are compared only inside one fingerprint."""
    n = len(adj) // 2
    per_vertex = sorted((int(v >= n), tuple(sorted(squares_on_edge(adj, v, int(w)) for w in adj[v])))
                        for v in range(2 * n))
    return total_squares(adj), tuple(per_vertex), tuple(connectivity(adj))


class ClassList:
    """One representative per class, found by fingerprint first and a true isomorphism test second."""

    def __init__(self):
        self.reps = []                               # (adj, graph)
        self._by_fingerprint = defaultdict(list)

    def index_of(self, adj):
        """Index of the class of `adj`, adding a new class if it is not there yet."""
        g = _graph(adj)
        bucket = self._by_fingerprint[_fingerprint(adj)]
        for k in bucket:
            if GraphMatcher(g, self.reps[k][1], node_match=_SAME_SIDE).is_isomorphic():
                return k
        self.reps.append((adj.copy(), g))
        bucket.append(len(self.reps) - 1)
        return len(self.reps) - 1

    def symmetries(self, k):
        """Number of renamings within sides that leave representative k unchanged."""
        g = self.reps[k][1]
        return sum(1 for _ in GraphMatcher(g, g, node_match=_SAME_SIDE).isomorphisms_iter())


def one_switch_away(adj, cap=NO_CAP):
    """Every valid state one edge switch from `adj` (the kernel's move, Q4), as adjacency arrays."""
    _check_numbering(adj)
    n = len(adj) // 2
    out = []
    work = adj.copy()
    for u1 in range(n):
        for u2 in range(u1 + 1, n):
            for v1 in adj[u1]:
                for v2 in adj[u2]:
                    v1, v2 = int(v1), int(v2)
                    if v1 == v2 or has_edge(work, u1, v2) or has_edge(work, u2, v1):
                        continue
                    _switch(work, u1, v1, u2, v2)
                    if is_valid(work, cap):
                        out.append(work.copy())
                    _switch(work, u1, v2, u2, v1)
    return out


def explore(start, cap=NO_CAP):
    """Walk outwards from `start` by switches. Returns (ClassList, {class: set of neighbouring classes})."""
    classes = ClassList()
    joined = defaultdict(set)
    todo = [classes.index_of(start)]
    seen = set(todo)
    while todo:
        k = todo.pop()
        for other in one_switch_away(classes.reps[k][0], cap):
            j = classes.index_of(other)
            if j != k:
                joined[k].add(j)
                joined[j].add(k)
            if j not in seen:
                seen.add(j)
                todo.append(j)
    return classes, joined


def check(n, cap=NO_CAP):
    """Steps 1 to 3 of the docstring for n vertices a side. Returns a dict for the report."""
    labelled, start = count_labelled_states(n, cap)
    if start is None:
        return dict(n=n, N=2 * n, cap=cap, labelled=0, classes=[], reached=0, ergodic=None)
    classes, joined = explore(start, cap)
    rows, reached = [], 0
    for k, (adj, _) in enumerate(classes.reps):
        a = classes.symmetries(k)
        size = factorial(n) ** 2 // a
        reached += size
        pieces, largest, in_babies, cubes = connectivity(adj)
        rows.append(dict(class_id=k, squares=int(total_squares(adj)), surplus=int(surplus(adj)), pieces=int(pieces),
                         largest=int(largest), in_babies=int(in_babies), cubes=int(cubes), symmetries=a,
                         labelled_states=size, neighbouring_classes=len(joined[k]),
                         valid_under_cap=bool(is_valid(adj, CAP))))
    return dict(n=n, N=2 * n, cap=cap, labelled=labelled, classes=rows, reached=reached, ergodic=reached == labelled)

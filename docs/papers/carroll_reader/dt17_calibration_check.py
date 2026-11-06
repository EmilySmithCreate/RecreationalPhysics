"""Check for the draft in this folder: the [DT17] two-copy state on the 8 x 8 flat torus, read by [CCM16].

Exact (arithmetic on a pure state; no sampling). Run from the repository root:
    PYTHONPATH=src python docs/papers/carroll_reader/dt17_calibration_check.py

The state ([DT17] Eq. 4) is |w> = sum_ij w_ij |i>|j> / ||w||_F on two copies of an N-level register, w the adjacency
matrix, read in its one-excitation form: 2N qubits, one per (copy, vertex). For two qubits the reduced state is
written down directly: across the copies it is diagonal in the product basis; within one copy the only coherence is
(w w^T)_ik / ||w||_F^2 between |10> and |01>. Mutual information in bits; I0 = 2 bits (two maximally entangled
qubits), Phi = -ln ([CCM16] Eq. 13), shortest paths ([CCM16] Eq. 14), classical multidimensional scaling
([CCM16] Eqs. 22 to 25). Prints the mutual information by graph distance and the MDS reading with the uniform
background kept and removed. Not part of the record's code; the numbers are to be entered in the record before the
draft is shared.
"""
from collections import defaultdict

import networkx as nx
import numpy as np

from graphity.cqg import NO_CAP, torus


def h(p):
    p = np.array([x for x in p if x > 1e-15])
    return float(-(p * np.log2(p)).sum())


def mds_spectrum(dist):
    n = len(dist)
    j = np.eye(n) - np.ones((n, n)) / n
    b = -0.5 * j @ (np.asarray(dist, dtype=float) ** 2) @ j
    return np.sort(np.linalg.eigvalsh(b))[::-1]


def main():
    adj = torus(8, 8, NO_CAP)[0]
    n = len(adj)
    w = np.zeros((n, n))
    for u in range(n):
        for v in adj[u]:
            w[u, v] = 1.0
    f = w.sum()
    ww = w @ w.T

    def mi_cross(i, j):
        p11 = w[i, j] / f
        p10 = w[i].sum() / f - p11
        p01 = w[:, j].sum() / f - p11
        p00 = 1 - p11 - p10 - p01
        return h([p11 + p10, p01 + p00]) + h([p11 + p01, p10 + p00]) - h([p11, p10, p01, p00])

    def mi_same(i, k):
        a, b, c = w[i].sum() / f, w[k].sum() / f, ww[i, k] / f
        ev = np.linalg.eigvalsh(np.array([[a, c], [c, b]]))
        return h([a, 1 - a]) + h([b, 1 - b]) - h(list(ev) + [1 - a - b])

    g = nx.Graph()
    for u in range(n):
        for v in adj[u]:
            g.add_edge(u, int(v))
    dist = dict(nx.all_pairs_shortest_path_length(g))
    cross, same = defaultdict(set), defaultdict(set)
    m = 2 * n
    info = np.zeros((m, m))
    for i in range(n):
        for j in range(n):
            info[i, n + j] = info[n + j, i] = mi_cross(i, j)
            cross[dist[i][j]].add(round(info[i, n + j], 7))
            if i != j:
                info[i, j] = info[n + i, n + j] = mi_same(i, j)
                same[(dist[i][j], int(ww[i, j]))].add(round(info[i, j], 7))
    print("across copies, by graph distance:", {k: sorted(v) for k, v in sorted(cross.items())})
    print("within a copy, by (graph distance, common neighbors):", {k: sorted(v) for k, v in sorted(same.items())})
    i0 = 2.0
    for label, cut in (("background kept", 0.0), ("background removed", 4e-4)):
        gi = nx.Graph()
        gi.add_nodes_from(range(m))
        for a in range(m):
            for b in range(a + 1, m):
                if info[a, b] > cut:
                    gi.add_edge(a, b, weight=-np.log(info[a, b] / i0))
        comps = sorted(nx.connected_components(gi), key=len)
        part = sorted(comps[-1])
        d = dict(nx.all_pairs_dijkstra_path_length(gi))
        dm = np.array([[d[p][q] for q in part] for p in part])
        s = mds_spectrum(dm)
        print(label, "| pieces", [len(c) for c in comps], "| largest distance", round(float(dm.max()), 3),
              "| top eigenvalues / largest", np.round(s[:6] / s[0], 3))


if __name__ == "__main__":
    main()

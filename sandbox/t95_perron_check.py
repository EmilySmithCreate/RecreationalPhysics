"""Sandbox look (not a result): is T95's long-path share the Perron (eigenvector-centrality) vector of the move-count matrix? Usage: python sandbox/t95_perron_check.py n"""
import sys
import numpy as np
sys.path.insert(0, "src"); sys.path.insert(0, "scripts")
import multiway_paths as mp
from graphity.small_graphs import circulant, explore
n = int(sys.argv[1])
start = circulant(n); classes, _ = explore(start); m = mp.move_counts(classes); k0 = classes.index_of(start)
shares = mp.path_shares(m, k0, 400)
long_share = (shares[-1] + shares[-2]) / 2
w, v = np.linalg.eig(m.T)                      # left eigenvectors of M
i = np.argmax(w.real); perron = np.abs(v[:, i].real); perron /= perron.sum()
w2, v2 = np.linalg.eig(m.T @ m.T)              # two-step chain, for a period-2 move graph
print("top |eigenvalues| of M:", np.round(np.sort(np.abs(w))[::-1][:3], 3))
print("max |long_share/perron - 1| =", np.max(np.abs(long_share / perron - 1)))
print("max |share_k=400 / share_k=398 - 1| =", np.max(np.abs(shares[-1] / shares[-3] - 1)))

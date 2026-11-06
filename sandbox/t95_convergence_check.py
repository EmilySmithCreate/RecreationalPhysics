"""Sandbox look (not a result): does T95's long-path share approach the labelled target at larger k? Usage: python sandbox/t95_convergence_check.py n"""
import sys
from pathlib import Path
import numpy as np
sys.path.insert(0, "src"); sys.path.insert(0, "scripts")
import multiway_paths as mp
from graphity.small_graphs import circulant, explore
from math import factorial
n = int(sys.argv[1])
start = circulant(n); classes, _ = explore(start); m = mp.move_counts(classes); k0 = classes.index_of(start)
a = np.array([classes.symmetries(j) for j in range(len(classes.reps))], float); deg = m.sum(1)
lab = factorial(n) ** 2 / a; target = lab * deg / (lab * deg).sum()
shares = mp.path_shares(m, k0, 2000)
for k in (40, 100, 200, 400, 1000, 2000):
    s = (shares[k - 1] + shares[k - 2]) / 2
    print(f"n={n} k={k} max|share/labelled-1|={np.max(np.abs(s / target - 1)):.4f}  odd/even gap={np.max(np.abs(shares[k-1]-shares[k-2])):.4f}")
w = np.sort(np.abs(np.linalg.eigvals(m / m.sum(1, keepdims=True))))[::-1]
print("transition eigenvalues (abs, top 4):", np.round(w[:4], 4))

"""Sandbox look (exploratory), 25 October 2026: which sign of curvature does space that opened from a curled start carry?

The owner's question C1 (docs/design/owner_questions_2026-10-24.md): is our universe slightly negative and the parent
slightly positive? In the four-link toy the total of curl minus uncurl over a graph is sum over links of (S_e - 2) =
4(S - N) (VISION Update 105, exact). A tube starts at S = 1.25 N (all curl). For every saved final graph of T51 (tubes
that opened by themselves while cooling, `results/t51_*_adj/*.npz`) this counts, over the whole graph and over the
links that are not flat, the curl (squares above two on a link) and the uncurl (squares below two), and reports the net.
Negative net = net uncurl = "negatively curved" in the reading of C1. A sandbox look: it can kill the reading, not crown it.
"""
import glob
import numpy as np

from graphity.squares import squares_on_edge

rows = []
for path in sorted(glob.glob("results/t51_*_adj/*.npz")):
    z = np.load(path)
    adj = z[z.files[0]] if "adj" not in z.files else z["adj"]
    n = adj.shape[0]
    curl = uncurl = 0
    for v in range(n):
        for w in adj[v]:
            w = int(w)
            if w < 0 or w < v:
                continue
            s = squares_on_edge(adj, v, w)
            if s > 2:
                curl += s - 2
            elif s < 2:
                uncurl += 2 - s
    rows.append((path, n, curl, uncurl, curl - uncurl))

net = np.array([r[4] for r in rows])
cur = np.array([r[2] for r in rows])
unc = np.array([r[3] for r in rows])
print(f"saved final graphs read: {len(rows)}")
print(f"graphs with net uncurl (negative): {int((net < 0).sum())}; net zero: {int((net == 0).sum())}; net curl (positive): {int((net > 0).sum())}")
print(f"curl per graph: mean {cur.mean():.2f}; uncurl per graph: mean {unc.mean():.2f}; net mean {net.mean():.2f} (min {net.min()}, max {net.max()})")
by = {}
for p, n, c, u, d in rows:
    key = p.split("\\")[-2] if "\\" in p else p.split("/")[-2]
    key = "_".join(key.split("_")[:3])
    by.setdefault(key, []).append(d)
for k in sorted(by):
    a = np.array(by[k])
    print(f"  {k:18s} graphs {len(a):3d}  net mean {a.mean():+.2f}  negative {int((a < 0).sum())}  zero {int((a == 0).sum())}  positive {int((a > 0).sum())}")

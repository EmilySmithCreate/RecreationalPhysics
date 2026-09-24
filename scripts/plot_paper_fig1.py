"""Figure 1 of the curled-torus paper (docs/papers/curled_torus/). Usage:

    python scripts/plot_paper_fig1.py docs/papers/curled_torus/fig1.pdf

Reads committed files only.
  (a) mean waiting time of the perfect 4 x L torus at lambda = 1.25 against 1/g
      (results/cqg_tube_arrhenius_lam125.csv, 16 runs per point), with the two predictions that
      use nothing fitted: move A alone, 1/(3 exp(-12/g)), and moves A and B,
      1/(3 exp(-12/g) + 2 exp(-14/g)) (PREREGISTRATION T8, exact move counts).
  (b) the share of vertices at each local dimension d when half the torus has converted
      (results/t7b_lam125_n*.csv, columns d0_50 .. d3_50, every decay that reached 50 %).
"""
import csv
import math
import sys
from collections import defaultdict

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

out = sys.argv[1]
INK, INK2, GRID = "#0b0b0b", "#52514e", "#e6e5e1"
BLUE, ORANGE, AQUA, YELLOW = "#2a78d6", "#eb6834", "#1baf7a", "#eda100"

waits = defaultdict(list)
for r in csv.DictReader(open("results/cqg_tube_arrhenius_lam125.csv", newline="")):
    if r["left"] == "True":
        waits[(int(r["N"]), float(r["g"]))].append(float(r["wait"]))

plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 8.5})
fig, (ax, bx) = plt.subplots(1, 2, figsize=(7.0, 2.6))
for a in (ax, bx):
    a.grid(True, color=GRID, lw=0.8)
    a.tick_params(colors=INK2, length=0)
    for side in ("top", "right"):
        a.spines[side].set_visible(False)

for n, color, marker in ((64, BLUE, "o"), (144, ORANGE, "s")):
    pts = sorted((g, np.mean(w), np.std(w, ddof=1) / math.sqrt(len(w))) for (nn, g), w in waits.items() if nn == n)
    ax.errorbar([1 / g for g, _, _ in pts], [m for _, m, _ in pts], yerr=[e for _, _, e in pts],
                color=color, marker=marker, ms=4, lw=0, elinewidth=1, capsize=2, label="N = %d" % n)
x = np.linspace(0.38, 0.73, 100)
ax.plot(x, 1 / (3 * np.exp(-12 * x)), color=INK, lw=1.2, label="move A only")
ax.plot(x, 1 / (3 * np.exp(-12 * x) + 2 * np.exp(-14 * x)), color=INK2, lw=1.2, ls="--", label="moves A and B")
ax.set_yscale("log")
ax.set_xlabel("1 / g")
ax.set_ylabel("mean waiting time (sweeps)")
ax.set_title("(a) no parameter fitted", fontsize=9, loc="left")
ax.legend(frameon=False, fontsize=7.5)

width = 0.2
for i, (n, color) in enumerate(((64, BLUE), (96, ORANGE), (144, AQUA), (192, YELLOW))):
    shares = np.zeros(4)
    count = 0
    for r in csv.DictReader(open("results/t7b_lam125_n%d.csv" % n, newline="")):
        if r["d2_50"] == "":
            continue
        shares += np.array([int(r["d%d_50" % k]) for k in range(4)]) / n
        count += 1
    shares /= count
    bx.bar(np.arange(4) + (i - 1.5) * width, shares, width=width * 0.9, color=color, label="N = %d (%d decays)" % (n, count))
bx.set_xticks(range(4))
bx.set_xticklabels(["d = 0", "d = 1\n(torus)", "d = 2\n(sheet)", "d = 3"])
bx.set_ylabel("share of vertices")
bx.set_ylim(0, 0.95)
bx.set_title("(b) at half conversion", fontsize=9, loc="left")
bx.legend(frameon=False, fontsize=7, loc="upper center", ncol=2)
fig.tight_layout()
fig.savefig(out)
print("wrote", out)

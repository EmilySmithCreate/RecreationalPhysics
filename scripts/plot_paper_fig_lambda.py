"""Figure 3 of the curled-torus paper: the lambda map (PREREGISTRATION T8). Usage:

    python scripts/plot_paper_fig_lambda.py docs/papers/curled_torus/fig_lambda.pdf

Reads results/t8_lam*.csv (and T7's t7b_lam125_n*.csv for lambda = 1.25, which T8 does not rerun).
(a) mean waiting time against lambda for each size where the tube is stuck (T8's definition), with Eq. (2)
    (moves A and B, nothing fitted) and the 200-sweep resting stretch below which the waiting time cannot fall;
(b) how each decay ended: the share of decays at the flat torus, and the share of vertices at d in {1, 2}
    at half conversion (the two orders side by side), per lambda, pooled over sizes.
"""
import csv
import glob
import math
import sys
from collections import defaultdict

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

out = sys.argv[1]
INK, INK2, GRID = "#1c1e22", "#5d636b", "#e6e5e1"
COLORS = {64: "#2a78d6", 96: "#eb6834", 144: "#1baf7a", 192: "#eda100"}
MARKERS = {64: "o", 96: "s", 144: "D", 192: "^"}


def tau(lam, g=1.5):
    return 1.0 / (3 * math.exp(-(32 - 16 * lam) / g) + 2 * math.exp(-(64 - 40 * lam) / g))


rows = defaultdict(list)
for f in glob.glob("results/t8_lam*.csv") + glob.glob("results/t7b_lam125_n*.csv"):
    for r in csv.DictReader(open(f, newline="")):
        rows[(float(r["lam"]), int(r["N"]))].append(r)

fig, (ax, bx) = plt.subplots(1, 2, figsize=(7.0, 2.7))
for a in (ax, bx):
    a.grid(True, color=GRID, lw=0.8)
    a.tick_params(colors=INK2, length=0)
    for side in ("top", "right"):
        a.spines[side].set_visible(False)

lams = sorted({l for l, _ in rows})
for n in (64, 96, 144, 192):
    xs, ys = [], []
    for l in lams:
        cell = rows.get((l, n), [])
        f200 = [float(r["f_200"]) for r in cell if r.get("f_200", "") not in ("", None)]
        stuck = (not f200) or sum(1 for x in f200 if x < 0.25) > len(f200) / 2   # T8's definition; T7 rows lack f_200
        w = [float(r["waiting"]) for r in cell if r["waiting"] not in ("", None) and r["reached"] and float(r["reached"]) >= 0.75]
        if stuck and len(w) >= 10:
            xs.append(l + (n - 120) / 12000.0)
            ys.append(np.mean(w))
    ax.plot(xs, ys, lw=0, marker=MARKERS[n], ms=4.5, color=COLORS[n], label="N = %d" % n)
lx = np.linspace(1.03, 1.47, 200)
ax.plot(lx, [tau(l) for l in lx], color=INK, lw=1.2, label="Eq. (2), nothing fitted")
ax.axhline(200, color=INK2, lw=0.8, ls=":")
ax.text(1.03, 170, "200-sweep rest", ha="left", va="top", fontsize=7, color=INK2)
ax.set_yscale("log")
ax.set_xlabel("λ")
ax.set_ylabel("mean waiting time (sweeps)")
ax.set_title("(a) how long the curled torus lasts", fontsize=9, loc="left")
ax.legend(frameon=False, fontsize=7, loc="lower left", bbox_to_anchor=(0.28, 0.0))

share_sheet, share_two, xl = [], [], []
for l in lams:
    rs = [r for n in (64, 96, 144, 192) for r in rows.get((l, n), [])]
    if not rs:
        continue
    expect = 4 * (l - 1)
    at_sheet = [abs(float(r["released"]) - expect) <= 0.01 * expect for r in rs]
    two = [(int(r["d1_50"]) + int(r["d2_50"])) / int(r["N"]) for r in rs if r.get("d2_50", "") != ""]
    xl.append(l)
    share_sheet.append(np.mean(at_sheet))
    share_two.append(np.mean(two) if two else float("nan"))
bx.plot(xl, share_two, color="#2a78d6", marker="o", ms=4, lw=1.4, label="vertices in one order or the other at 50%")
bx.plot(xl, share_sheet, color="#eb6834", marker="s", ms=4, lw=1.4, label="decays ending at the flat torus")
bx.axvspan(1.375, 1.47, color="#e6e5e1", zorder=0)
bx.text(1.42, 0.53, "not stuck", ha="center", fontsize=7, color=INK2)
ax.axvspan(1.375, 1.47, color="#e6e5e1", zorder=0)
bx.set_ylim(0.0, 1.03)
bx.set_xlabel("λ")
bx.set_ylabel("share")
bx.set_title("(b) sharpness and completeness", fontsize=9, loc="left")
bx.legend(frameon=False, fontsize=7, loc="lower left")
bx.set_xlim(1.02, 1.47)
ax.set_xlim(1.02, 1.47)
fig.tight_layout()
fig.savefig(out, dpi=220 if out.endswith(".png") else None)
print("wrote", out, "lambdas", xl)

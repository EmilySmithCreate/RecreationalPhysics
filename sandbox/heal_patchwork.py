"""Sandbox: can a patchwork become flat? Usage: python sandbox/heal_patchwork.py [G_HOLD] [HOLD_SWEEPS] [COOL_SWEEPS]

Takes the saved end states of T61 stage 1 at lambda = 1.40, N = 96 that read WIDE (at least half their points see a
sheet out to three steps), holds each warm at G_HOLD, cools it to g = 1 in 40 steps, then leaves it cold, and reads
it again. T61's stage 1 has been read, so this opens nothing unread.
"""
import csv
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "sandbox"))
from graphity.cqg import NO_CAP, run_chain                          # noqa: E402
from shape_tools import line, read                                  # noqa: E402


def main(g_hold=2.0, hold=100000, cool=100000, lam=1.40, name="t61_lam140_n96"):
    rows = [r for r in csv.DictReader(open(ROOT / "results" / (name + ".csv"), newline="", encoding="utf-8"))
            if float(r["sees3"]) >= 0.5]
    print("%d WIDE end states of %s; held at g = %.2f for %d sweeps, cooled over %d" % (len(rows), name, g_hold, hold, cool))
    for i, r in enumerate(rows):
        z = np.load(ROOT / "results" / (name + "_adj") / ("N%s_C%s_rep%s.npz" % (r["N"], r["stores"], r["replica"])))
        adj, part = z["adj"].copy(), z["part"]
        side = np.flatnonzero(part == 0).astype(np.int64)
        before = read(adj, lam)
        run_chain(adj, side, 1.0 / g_hold, hold - 1, 1, 777 + i, lam, NO_CAP)
        for step in range(40):
            g = g_hold + (1.0 - g_hold) * (step + 1) / 40
            run_chain(adj, side, 1.0 / g, max(1, cool // 40) - 1, 1, -1, lam, NO_CAP)
        run_chain(adj, side, 1.0 / 0.05, 1999, 1, -1, lam, NO_CAP)
        print("  before: %s\n   after: %s" % (line(before), line(read(adj, lam))))


if __name__ == "__main__":
    a = sys.argv[1:]
    main(float(a[0]) if a else 2.0, int(a[1]) if len(a) > 1 else 100000, int(a[2]) if len(a) > 2 else 100000)

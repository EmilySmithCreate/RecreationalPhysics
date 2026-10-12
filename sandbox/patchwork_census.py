"""Sandbox: what is a patchwork made of? Usage: python sandbox/patchwork_census.py [NAME] [LAMBDA]

Reads the saved end states of a T61 stage-1 file (already read, so nothing unread is opened). For each end state
that is neither a clean tube nor flat, every point is asked how far it can look before the space stops matching an
endless sheet: the first radius r at which fewer than 2r^2 + 2r + 1 points lie within r steps. "Sees 2r around."
A point that fails at r = 1 or 2 sits on or beside a flaw.
"""
import csv
import sys
from collections import Counter
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "scripts"))
from graphity.cqg import hamiltonian                                # noqa: E402
from graphity.dimension import local_dimension                      # noqa: E402
from read_open_shells import shells                                 # noqa: E402


def look(adj):
    """Per point: the first radius at which the ball is smaller than the plane's (99 if never), and whether the ball
    is ever LARGER than the plane's (a shortcut: something no flat surface has)."""
    n = adj.shape[0]
    first, over = np.zeros(n, dtype=np.int64), np.zeros(n, dtype=bool)
    for v in range(n):
        c = np.cumsum(shells(adj, v))
        first[v] = 99
        for r, reached in enumerate(c):
            plane = 2 * r * r + 2 * r + 1
            if reached > plane:
                over[v] = True
            if reached < plane:
                first[v] = r
                break
    return first, over


def main(name="t61_lam140_n96", lam=1.40, want="WIDE"):
    rows = list(csv.DictReader(open(ROOT / "results" / (name + ".csv"), newline="", encoding="utf-8")))
    for r in rows:
        s3 = float(r["sees3"])
        kind = "WIDE" if s3 >= 0.5 else ("TUBE" if s3 < 0.05 else "PATCHWORK")
        if kind != want:
            continue
        z = np.load(ROOT / "results" / (name + "_adj") / ("N%s_C%s_rep%s.npz" % (r["N"], r["stores"], r["replica"])))
        adj = z["adj"]
        n = adj.shape[0]
        first, over = look(adj)
        d = Counter(int(x) for x in local_dimension(adj))
        around = Counter(int(2 * x) for x in first)
        print("C=%s rep=%s: energy %.1f | points by local count d: %s | sees N around: %s | points with a shortcut: %d"
              % (r["stores"], r["replica"], hamiltonian(adj, lam), dict(sorted(d.items())),
                 ", ".join("%d: %d" % kv for kv in sorted(around.items())), int(over.sum())))


if __name__ == "__main__":
    a = sys.argv[1:]
    main(a[0] if a else "t61_lam140_n96", float(a[1]) if len(a) > 1 else 1.40, a[2] if len(a) > 2 else "WIDE")

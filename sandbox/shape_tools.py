"""Sandbox helpers for reading a four-link graph's shape. Not a registered reader."""
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "scripts"))
from graphity.cqg import hamiltonian                                # noqa: E402
from read_endpoint_width import is_flat                             # noqa: E402
from read_open_shells import shells                                 # noqa: E402


def read(adj, lam):
    """dict: energy, exactly flat or not, the widths seen from every point (if flat), and sees3: the share of points
    with exactly 25 points within three steps, as an endless sheet has."""
    n = adj.shape[0]
    balls = np.zeros((n, 8), dtype=np.int64)
    widths = []
    for v in range(n):
        s = shells(adj, v)
        c = np.cumsum(s)
        balls[v, :min(8, len(c))] = c[:8]
        balls[v, len(c):] = c[-1]
        w = None
        for r, reached in enumerate(c):
            if reached < 2 * r * r + 2 * r + 1:
                w = 2 * r
                break
        widths.append(w)
    flat = bool(is_flat(adj))
    seen = sorted(set(widths), key=lambda x: (x is None, x))
    return dict(energy=float(hamiltonian(adj, lam)), flat=flat, widths=seen if flat else [],
                sees3=float((balls[:, 3] == 25).mean()), sees4=float((balls[:, 4] == 41).mean()),
                near5=float(balls[:, 5].mean()))


def line(r):
    return ("energy %6.1f | %s | sees a sheet to 3 steps %.2f, to 4 steps %.2f | within 5 steps %.1f"
            % (r["energy"], ("flat, width %s" % "/".join(str(w) for w in r["widths"])) if r["flat"] else "not flat",
               r["sees3"], r["sees4"], r["near5"]))

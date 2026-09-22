"""From a given arrangement, how many single moves build order and how many destroy it? Usage:

    python scripts/run_move_census.py configs/move_census.json

EXACT, exploratory (explains O20; TASKS T13 rung 3). O20 found that energy put into a sheet of
space melts it rather than folding it, and explained that by counting ways: more ways to break a
loop than to make one. **That explanation was too weak.** This census enumerates every valid single
switch out of an arrangement and sorts it by whether it adds squares (the only way to curl, since a
curled arrangement carries more squares per point than a flat one) or loses them.

Read the result before quoting the earlier explanation: out of a *perfectly ordered* arrangement, of
either kind, the number of moves that add a square is not small but zero. Order can only be
destroyed in one step. Building happens only out of disorder, which is a different statement and a
stronger one.
"""
import json
import platform
import sys
from pathlib import Path

import numba
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from graphity import __version__                                          # noqa: E402
from graphity.cqg import (NO_CAP, _switch, hamiltonian, is_valid,          # noqa: E402
                          run_chain, torus, total_squares)
from graphity.results import ResultWriter                                 # noqa: E402


def census(adj, lam):
    """Every valid single switch, sorted by what it does to the number of squares."""
    n = adj.shape[0]
    base_s, base_h = total_squares(adj), hamiltonian(adj, lam)
    made = broke = same = 0
    cheapest_make = cheapest_break = None
    for u1 in range(n):
        for v1 in adj[u1]:
            for u2 in range(u1 + 1, n):
                for v2 in adj[u2]:
                    if len({u1, int(v1), u2, int(v2)}) < 4:
                        continue
                    trial = adj.copy()
                    _switch(trial, u1, int(v1), u2, int(v2))
                    if not is_valid(trial, NO_CAP):
                        continue
                    ds = total_squares(trial) - base_s
                    dh = hamiltonian(trial, lam) - base_h
                    if ds > 0:
                        made += 1
                        cheapest_make = dh if cheapest_make is None else min(cheapest_make, dh)
                    elif ds < 0:
                        broke += 1
                        cheapest_break = dh if cheapest_break is None else min(cheapest_break, dh)
                    else:
                        same += 1
    return dict(squares=int(base_s), h=base_h, adds=made, loses=broke, neither=same,
                cheapest_add=cheapest_make, cheapest_lose=cheapest_break)


def arrangements(cfg, lam):
    for lx, ly in cfg["sheets"]:
        adj, _ = torus(lx, ly, NO_CAP)
        yield "flat sheet %dx%d" % (lx, ly), adj
    for long_side in cfg["tubes"]:
        adj, _ = torus(long_side, 4, NO_CAP)
        yield "tube %dx4" % long_side, adj
    for lx, ly in cfg["melted_from"]:
        adj, part = torus(lx, ly, NO_CAP)
        run_chain(adj, np.flatnonzero(part == 0), 1.0 / float(cfg["melt_g"]), 0,
                  int(cfg["melt_sweeps"]), int(cfg["seed"]), lam, NO_CAP, False)
        yield "melted from %dx%d" % (lx, ly), adj


def main(path, out_dir="results"):
    cfg = json.loads(Path(path).read_text())
    lam = float(cfg["lambda"])
    meta = dict(config=cfg, config_path=str(path), package=__version__,
                python=platform.python_version(), numpy=np.__version__,
                numba=numba.__version__, purpose=cfg.get("_purpose", ""))
    with ResultWriter(cfg["name"], meta, out_dir) as out:
        for label, adj in arrangements(cfg, lam):
            row = dict(arrangement=label, n=int(adj.shape[0]), lam=lam, **census(adj, lam))
            out.write(row)
            print("%-22s squares %4d: %6d moves add a square, %6d lose one; cheapest add %s, cheapest lose %s"
                  % (label, row["squares"], row["adds"], row["loses"],
                     row["cheapest_add"], row["cheapest_lose"]), flush=True)


if __name__ == "__main__":
    main(*sys.argv[1:])

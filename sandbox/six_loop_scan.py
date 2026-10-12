"""Sandbox: the pushed six-around tube under a price on loops of six, with the tested kernel (graphity.sixloop).

    python sandbox/six_loop_scan.py LENGTH MU G [SWEEPS] [REPLICAS] [LAMBDA] [SEED] [PUSH] [COOL_SWEEPS]

PUSH is far (default), local94, local24, local103, cheap or none; see `pushed`.

The tube six around (4 x LENGTH points, seam shifted by two), with the first six-loop-removing move made by hand,
is run at coupling G in blocks of 500 sweeps until it has fallen back, or finished (no six-loop excess and no
energy left), or SWEEPS are used up; then it is left cold and read from its wiring. A look for choosing settings,
not a registered run.
"""
import sys
import time
from collections import Counter
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "scripts"))
sys.path.insert(0, str(ROOT / "sandbox"))
from graphity.cqg import NO_CAP, _new_edge_ok, _switch, hamiltonian, surplus, total_squares     # noqa: E402
from graphity.sixloop import excess6, run_chain6                                             # noqa: E402
from read_endpoint_width import is_flat, twisted_tube                                        # noqa: E402
from read_flat_kind import describe, pieces                                                  # noqa: E402
from shape_tools import read                                                                 # noqa: E402

BLOCK = 500


def side_of(length):
    return np.array([x * length + y for x in range(4) for y in range(length) if (x + y) % 2 == 0], dtype=np.int64)


PUSHES = {"far": (-4, 0, -176), "local94": (-2, 2, -94), "local24": (-2, 0, -24), "cheap": (-1, 3, -59),
          "local103": (-3, 1, -103)}


def pushed(length, push="far"):
    """The six-around tube after one switch made by hand, named by what it does to squares, surplus and E6.
    "far" joins places several steps apart (it is the switch that removes the most E6); the others are local,
    their two links two or three steps apart. "none" makes no switch. Returns (graph, side, E6 before, E6 after)."""
    adj = twisted_tube(length, 2)
    side = side_of(length)
    e0 = excess6(adj, side)
    if push == "none":
        return adj, side, e0, e0
    want = PUSHES[push]
    for u1 in side[:8]:
        u1 = int(u1)
        for v1 in adj[u1]:
            for u2 in side:
                if u2 == u1:
                    continue
                for v2 in adj[u2]:
                    if v1 == v2 or v2 in adj[u1] or v1 in adj[u2]:
                        continue
                    trial = adj.copy()
                    _switch(trial, u1, int(v1), int(u2), int(v2))
                    if not (_new_edge_ok(trial, u1, int(v2), NO_CAP) and _new_edge_ok(trial, int(u2), int(v1), NO_CAP)):
                        continue
                    if (total_squares(trial) - 4 * length, surplus(trial)) != want[:2]:
                        continue
                    if excess6(trial, side) - e0 == want[2]:
                        return trial, side, e0, e0 + want[2]
    raise ValueError("no switch of kind %s found" % (want,))


def one(length, mu, g, sweeps, lam, seed, push="far", cool=0):
    adj, side, e_start, _e1 = pushed(length, push)
    n = 4 * length
    low, used, what = 1.0, 0, "unfinished"
    first = True
    while used < sweeps:
        s, x, e, _acc = run_chain6(adj, side, 1.0 / g, 0, BLOCK, seed if first else -1, lam, mu)
        first = False
        used += BLOCK
        low = min(low, s.min() / n)
        if push != "none" and e[-1] == e_start and s[-1] == n and x[-1] == 0:
            what = "fell back"
            break
        if e[-1] == 0 and s[-1] == n and x[-1] == 0:
            what = "finished"
            break
    if what == "unfinished" and cool > 0:                  # then cooled slowly, from g down to 0.5
        for step in range(40):
            g_now = g + (0.5 - g) * (step + 1) / 40
            s, x, e, _acc = run_chain6(adj, side, 1.0 / g_now, 0, max(1, cool // 40), -1, lam, mu)
            low = min(low, s.min() / n)
        used += cool
        if e[-1] == 0 and s[-1] == n and x[-1] == 0:
            what = "finished"
    run_chain6(adj, side, 1.0 / 0.05, 0, 1000, -1, lam, mu)
    end = read(adj, lam)
    e_end = int(excess6(adj, side))
    if end["flat"] and e_end == 0:
        parts = describe(adj)
        label = "; ".join("%s %s around (%d)" % (k, w, size) for size, k, w in parts)
    elif end["flat"]:
        label = "flat, six-loop excess left %d: %s" % (e_end, "; ".join("%s %s (%d)" % (k, w, size) for size, k, w in describe(adj)))
    else:
        label = "flaws left"
    return dict(what=what, used=used, low=low, energy=end["energy"], excess=e_end, sees3=end["sees3"], label=label,
                pieces=len(pieces(adj)))


def main(length, mu, g, sweeps=100000, replicas=16, lam=1.25, seed=20261013, push="far", cool=0):
    t0 = time.time()
    print("N=%d lambda=%.2f mu=%.3f g=%.2f push=%s, up to %d sweeps, then cooled over %d, %d replicas"
          % (4 * length, lam, mu, g, push, sweeps, cool, replicas), flush=True)
    tally = Counter()
    for rep in range(replicas):
        r = one(length, mu, g, sweeps, lam, seed + 7919 * rep + int(1000 * mu) + int(100 * g) + length, push, cool)
        tally[r["label"] if r["what"] != "fell back" else "fell back"] += 1
        print("  %2d: %-10s after %6d sweeps | fewest squares per point %.3f | energy %5.1f, excess %4d, sees3 %.2f, "
              "pieces %d | %s" % (rep, r["what"], r["used"], r["low"], r["energy"], r["excess"], r["sees3"], r["pieces"],
                                  r["label"]), flush=True)
    print("ends:", dict(tally), "| %.0f s" % (time.time() - t0), flush=True)


if __name__ == "__main__":
    a = sys.argv[1:]
    main(int(a[0]), float(a[1]), float(a[2]), int(a[3]) if len(a) > 3 else 100000, int(a[4]) if len(a) > 4 else 16,
         float(a[5]) if len(a) > 5 else 1.25, int(a[6]) if len(a) > 6 else 20261013, a[7] if len(a) > 7 else "far",
         int(a[8]) if len(a) > 8 else 0)

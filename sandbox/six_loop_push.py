"""Sandbox, the NEW RULE of `six_loop_edge.py` (a price mu on a link's loops of six beyond 6): start the change by
hand and see whether it runs. The owner's "if this kept happening", 11 October 2026.

    python sandbox/six_loop_push.py next [LENGTH]                    # after the first move: what the next moves cost
    python sandbox/six_loop_push.py run LENGTH MU G [SWEEPS] [REPLICAS]

With a gentle price the tube six around is stuck: its cheapest move that removes six-loops costs 64 - 176 mu, too
much for warmth to supply. Here that first move is made by hand (a push), and the chain is then left to run at G.
Does a front carry the change along the tube to a tube eight around, or does the move just fall back?
"""
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "scripts"))
sys.path.insert(0, str(ROOT / "sandbox"))
from graphity.cqg import NO_CAP, _new_edge_ok, _switch, surplus, total_squares      # noqa: E402
from read_endpoint_width import twisted_tube                                     # noqa: E402
from read_flat_kind import describe                                              # noqa: E402
from shape_tools import line, read                                               # noqa: E402
from six_loop_cost import side_of                                                # noqa: E402
from six_loop_edge import excess6, run_edge                                      # noqa: E402


def switches(adj, side_u, firsts=None):
    """Every valid switch as ((u1, v1, u2, v2), d_S, d_X, d_excess), by trying it. `firsts` limits the first point."""
    s0, x0, e0 = total_squares(adj), surplus(adj), excess6(adj, side_u)
    out = []
    for u1 in (side_u if firsts is None else firsts):
        for v1 in adj[u1]:
            for u2 in side_u:
                if u2 == u1:
                    continue
                for v2 in adj[u2]:
                    if v1 == v2 or v2 in adj[u1] or v1 in adj[u2]:
                        continue
                    trial = adj.copy()
                    _switch(trial, int(u1), int(v1), int(u2), int(v2))
                    if not (_new_edge_ok(trial, int(u1), int(v2), NO_CAP) and _new_edge_ok(trial, int(u2), int(v1), NO_CAP)):
                        continue
                    out.append(((int(u1), int(v1), int(u2), int(v2)), int(total_squares(trial) - s0),
                                int(surplus(trial) - x0), int(excess6(trial, side_u) - e0)))
    return out


def pushed(length):
    """The tube six around with the first six-loop-removing move made: (graph, side, the move's d_S, d_X, d_excess)."""
    adj = twisted_tube(length, 2)
    side = side_of(length)
    best = min((m for m in switches(adj, side, firsts=side[:1]) if m[1] == -4 and m[2] == 0), key=lambda m: m[3])
    _switch(adj, *best[0])
    return adj, side, best[1:]


def cost(ds, dx, de, mu, lam=1.25):
    return -16.0 * ds + 4.0 * lam * dx + mu * de


def next_moves(length=12):
    adj, side, first = pushed(length)
    print("N = %d. The push: squares %+d, surplus %+d, six-loop excess %+d." % ((4 * length,) + first))
    moves = switches(adj, side)
    kinds = {}
    for _m, ds, dx, de in moves:
        kinds[(ds, dx, de)] = kinds.get((ds, dx, de), 0) + 1
    for mu in (0.05, 0.10, 0.15, 0.20, 0.30):
        ranked = sorted((cost(ds, dx, de, mu), ds, dx, de, k) for (ds, dx, de), k in kinds.items())
        print("  mu = %.2f: the push costs %.1f; cheapest next moves (cost, dS, dX, d excess, how many): %s"
              % (mu, cost(*first, mu), "; ".join("%.1f %d %d %d x%d" % r for r in ranked[:5])))


def run(length, mu, g, sweeps=20000, replicas=8, lam=1.25):
    n = 4 * length
    adj0, side, first = pushed(length)
    start = excess6(twisted_tube(length, 2), side)
    print("N=%d mu=%.2f g=%.2f: the push costs %.1f (excess %d -> %d); six around holds %.2f per point; %d sweeps"
          % (n, mu, g, cost(*first, mu, lam), start, excess6(adj0, side), mu * start / n, sweeps))
    for rep in range(replicas):
        adj = adj0.copy()
        out = run_edge(adj, side, 1.0 / g, sweeps, 2026101700 + 7919 * rep + int(1000 * mu) + int(100 * g), lam, mu)
        back = np.flatnonzero((out[:, 2] == start) & (out[:, 0] == n))
        gone = np.flatnonzero(out[:, 2] == 0)
        end = read(adj, lam)
        what = ("; ".join("%d points, %s, %s around" % p for p in describe(adj)) if end["flat"] else "")
        print("  %d: fell back at sweep %s | excess gone at sweep %s | fewest squares per point %.3f | end: excess %d, %s %s"
              % (rep, back[0] if back.size else "never", gone[0] if gone.size else "never", out[:, 0].min() / n,
                 out[-1, 2], line(end), what), flush=True)


if __name__ == "__main__":
    a = sys.argv[1:]
    if not a or a[0] == "next":
        next_moves(int(a[1]) if len(a) > 1 else 12)
    else:
        run(int(a[1]), float(a[2]), float(a[3]), int(a[4]) if len(a) > 4 else 20000, int(a[5]) if len(a) > 5 else 8)

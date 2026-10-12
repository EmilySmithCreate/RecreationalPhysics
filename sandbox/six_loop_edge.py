"""Sandbox, and a NEW RULE that is not the toy's: the saturating form of the six-loop price, link by link.

    H'' = 16 (N - S) + 4 lambda X + mu * sum over links of (six-loops through the link - 6)+

In a wide flat sheet every link lies on exactly 6 loops of six (the outlines of pairs of neighbouring squares), so
the new term is zero there. A link with more than 6 is "over-full at the next scale", the way a link with more than
two squares is over-full in the toy's own rule. Unlike `six_loop_cost.py`, having FEWER six-loops than a sheet
earns nothing, so breaking squares is not rewarded once the wraps are gone.

Usage:
    python sandbox/six_loop_edge.py walls [LENGTH]
    python sandbox/six_loop_edge.py run LENGTH MU G [SWEEPS] [REPLICAS] [COOL_SWEEPS] [LAMBDA]
"""
import sys
from pathlib import Path

import numpy as np
from numba import njit

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "scripts"))
sys.path.insert(0, str(ROOT / "sandbox"))
from graphity.cqg import (NO_CAP, _new_edge_ok, _note_square_edges, _replace, _surplus_on, _switch,   # noqa: E402
                          has_edge, squares_on_edge, surplus, total_squares)
from read_endpoint_width import twisted_tube                         # noqa: E402
from shape_tools import line, read                                   # noqa: E402
from six_loop_cost import loops6_through, side_of, total_loops6      # noqa: E402

FLAT = 6


@njit(cache=True)
def excess6(adj, side_u):
    """Sum over links of (six-loops through the link - 6)+."""
    total = 0
    for i in range(side_u.shape[0]):
        u = side_u[i]
        for j in range(4):
            c = loops6_through(adj, u, adj[u, j], -1, -1)
            if c > FLAT:
                total += c - FLAT
    return total


@njit(cache=True)
def run_edge(adj, side_u, inv_g, n_sweeps, seed, lam, mu):
    """Thermal chain under H''. Returns S, X, excess per sweep. The six-loop excess is recomputed in full for a
    proposal only when the cheap part of the energy change has not already decided it (the excess can fall by at
    most its present value, so the same random number settles those proposals without the count)."""
    if seed >= 0:
        np.random.seed(seed)
    n = adj.shape[0]
    nu = side_u.shape[0]
    edges = np.empty((64, 2), dtype=np.int64)
    s = total_squares(adj)
    x = surplus(adj)
    e6 = excess6(adj, side_u)
    out = np.zeros((n_sweeps, 3), dtype=np.int64)
    for sweep in range(n_sweeps):
        for _ in range(2 * n):
            u1 = side_u[np.random.randint(0, nu)]
            v1 = adj[u1, np.random.randint(0, 4)]
            u2 = side_u[np.random.randint(0, nu)]
            v2 = adj[u2, np.random.randint(0, 4)]
            if u1 == u2 or v1 == v2 or has_edge(adj, u1, v2) or has_edge(adj, u2, v1):
                continue
            n_edges = 0
            n_edges = _note_square_edges(adj, u1, v1, edges, n_edges)
            n_edges = _note_square_edges(adj, u2, v2, edges, n_edges)
            lost = squares_on_edge(adj, u1, v1)
            _replace(adj, u1, v1, -1)
            _replace(adj, v1, u1, -1)
            lost += squares_on_edge(adj, u2, v2)
            _replace(adj, u2, v2, -1)
            _replace(adj, v2, u2, -1)
            _replace(adj, u1, -1, v2)
            _replace(adj, v2, -1, u1)
            gained = squares_on_edge(adj, u1, v2)
            _replace(adj, u2, -1, v1)
            _replace(adj, v1, -1, u2)
            gained += squares_on_edge(adj, u2, v1)
            d_s = gained - lost
            d_x = 0
            new_e6 = e6
            ok = _new_edge_ok(adj, u1, v2, NO_CAP) and _new_edge_ok(adj, u2, v1, NO_CAP)
            if ok:
                n_edges = _note_square_edges(adj, u1, v2, edges, n_edges)
                n_edges = _note_square_edges(adj, u2, v1, edges, n_edges)
                after = _surplus_on(adj, edges, n_edges)
                _switch(adj, u1, v2, u2, v1)
                before = _surplus_on(adj, edges, n_edges)
                _switch(adj, u1, v1, u2, v2)
                d_x = after - before
                cheap = -16.0 * d_s + 4.0 * lam * d_x
                r = np.random.random()
                least = cheap - mu * e6                              # the excess can fall by at most e6
                if least > 0.0 and r >= np.exp(-least * inv_g):
                    ok = False
                else:
                    new_e6 = excess6(adj, side_u)
                    d_h = cheap + mu * (new_e6 - e6)
                    if d_h > 0.0 and r >= np.exp(-d_h * inv_g):
                        ok = False
            if ok:
                s += d_s
                x += d_x
                e6 = new_e6
            else:
                _switch(adj, u1, v2, u2, v1)
        out[sweep, 0] = s
        out[sweep, 1] = x
        out[sweep, 2] = e6
    return out


def moves_out(adj, side_u):
    """Every switch out of this graph as (d_S, d_X, d_excess), with how many there are; by trying each one."""
    kinds = {}
    s0, x0, e0 = total_squares(adj), surplus(adj), excess6(adj, side_u)
    for u1 in side_u:
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
                    key = (int(total_squares(trial) - s0), int(surplus(trial) - x0), int(excess6(trial, side_u) - e0))
                    kinds[key] = kinds.get(key, 0) + 1
    return kinds


def walls(length=12, lam=1.25):
    for name, shift in (("the tube (four around)", 0), ("six around (seam shifted by two)", 2),
                        ("eight around (seam shifted by four)", 4)):
        adj = twisted_tube(length, shift)
        side = side_of(length)
        n = adj.shape[0]
        e0 = excess6(adj, side)
        print("%s, N = %d: squares %d, surplus %d, six-loops %d (2N = %d), excess over links %d (%.2f per point)"
              % (name, n, total_squares(adj), surplus(adj), total_loops6(adj, side), 2 * n, e0, e0 / n))
        kinds = moves_out(adj, side)
        for mu in (0.0, 0.05, 0.1, 0.2, 0.3, 0.5):
            cost = sorted((-16.0 * ds + 4.0 * lam * dx + mu * de, ds, dx, de, k) for (ds, dx, de), k in kinds.items())
            print("   mu = %.2f (release %.2f per point): cheapest moves out (cost, dS, dX, d excess, how many): %s"
                  % (mu, mu * e0 / n, "; ".join("%.1f %d %d %d x%d" % c for c in cost[:3])))


def run(length, mu, g, sweeps=10000, replicas=3, cool=10000, lam=1.25):
    n = 4 * length
    side = side_of(length)
    print("N=%d lambda=%.2f mu=%.2f g=%.2f from six around, %d sweeps then cooled over %d" % (n, lam, mu, g, sweeps, cool))
    for rep in range(replicas):
        adj = twisted_tube(length, 2)
        out = run_edge(adj, side, 1.0 / g, sweeps, 2026101600 + 7919 * rep + int(1000 * mu) + int(100 * g), lam, mu)
        assert (total_squares(adj), surplus(adj), excess6(adj, side)) == tuple(out[-1])      # the books are exact
        gone = np.flatnonzero(out[:, 2] == 0)
        half = np.flatnonzero(out[:, 2] <= out[0, 2] // 2)
        low = out[:, 0].min() / n
        for step in range(40 if cool else 0):
            run_edge(adj, side, 1.0 / (g + (0.3 - g) * (step + 1) / 40), max(1, cool // 40), -1, lam, mu)
        run_edge(adj, side, 1.0 / 0.05, 500, -1, lam, mu)
        print("  %d: excess %d -> %d (half gone at sweep %s, none at %s) | fewest squares per point %.3f | cold: excess %d, %s"
              % (rep, out[0, 2], out[-1, 2], half[0] if half.size else "never", gone[0] if gone.size else "never",
                 low, excess6(adj, side), line(read(adj, lam))), flush=True)


if __name__ == "__main__":
    a = sys.argv[1:]
    if not a or a[0] == "walls":
        walls(int(a[1]) if len(a) > 1 else 12)
    else:
        run(int(a[1]), float(a[2]), float(a[3]), int(a[4]) if len(a) > 4 else 10000, int(a[5]) if len(a) > 5 else 3,
            int(a[6]) if len(a) > 6 else 10000, float(a[7]) if len(a) > 7 else 1.25)

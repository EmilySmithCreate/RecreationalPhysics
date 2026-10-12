"""Sandbox, and a NEW RULE that is not the toy's: a price on six-loops beyond those a wide flat sheet has.

    H' = 16 (N - S) + 4 lambda X + mu (C6 - 2N)

C6 is the number of closed loops of six links. A flat torus eight or more around has exactly 2N of them (the loops
round two neighbouring squares), so it still costs zero. A flat torus six around has more (its wraps), so under this
rule it is "curled at the next scale" and costs mu per extra loop. The question: does a tube six around then give
way to one eight around, as the tube four around gave way to six?

Usage:
    python sandbox/six_loop_cost.py walls                       # the cheapest moves out of the six-around tube, by mu
    python sandbox/six_loop_cost.py run LENGTH MU G [SWEEPS] [REPLICAS] [START] [LAMBDA] [COOL_SWEEPS]
START is "twist" (the tube with its seam shifted by two; default) or "tube".
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


@njit(cache=True)
def _is(p, q, a, b):
    return (p == a and q == b) or (p == b and q == a)


@njit(cache=True)
def loops6_through(adj, u, v, a, b):
    """Six-loops that use link (u, v) and do not use link (a, b); a = -1 for no such link."""
    count = 0
    for i1 in range(4):
        p1 = adj[v, i1]
        if p1 == u:
            continue
        for i2 in range(4):
            p2 = adj[p1, i2]
            if p2 == v:
                continue
            for i3 in range(4):
                p3 = adj[p2, i3]
                if p3 == p1 or p3 == u:
                    continue
                for i4 in range(4):
                    p4 = adj[p3, i4]
                    if p4 == p2 or p4 == v or not has_edge(adj, p4, u):
                        continue
                    if a >= 0 and (_is(v, p1, a, b) or _is(p1, p2, a, b) or _is(p2, p3, a, b) or _is(p3, p4, a, b)
                                   or _is(p4, u, a, b)):
                        continue
                    count += 1
    return count


@njit(cache=True)
def total_loops6(adj, side_u):
    total = 0
    for i in range(side_u.shape[0]):
        u = side_u[i]
        for j in range(4):
            total += loops6_through(adj, u, adj[u, j], -1, -1)
    return total // 6


@njit(cache=True)
def run_six(adj, side_u, inv_g, n_sweeps, seed, lam, mu):
    """The thermal chain of graphity.cqg.run_chain with mu (C6 - 2N) added to the energy. Returns S, X, C6 per sweep."""
    if seed >= 0:
        np.random.seed(seed)
    n = adj.shape[0]
    nu = side_u.shape[0]
    edges = np.empty((64, 2), dtype=np.int64)
    s = total_squares(adj)
    x = surplus(adj)
    c6 = total_loops6(adj, side_u)
    out = np.zeros((n_sweeps, 3), dtype=np.int64)
    for sweep in range(n_sweeps):
        for _ in range(2 * n):
            u1 = side_u[np.random.randint(0, nu)]
            v1 = adj[u1, np.random.randint(0, 4)]
            u2 = side_u[np.random.randint(0, nu)]
            v2 = adj[u2, np.random.randint(0, 4)]
            if u1 == u2 or v1 == v2 or has_edge(adj, u1, v2) or has_edge(adj, u2, v1):
                continue
            c_before = loops6_through(adj, u1, v1, -1, -1) + loops6_through(adj, u2, v2, u1, v1)
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
            d_c = 0
            ok = _new_edge_ok(adj, u1, v2, NO_CAP) and _new_edge_ok(adj, u2, v1, NO_CAP)
            if ok:
                n_edges = _note_square_edges(adj, u1, v2, edges, n_edges)
                n_edges = _note_square_edges(adj, u2, v1, edges, n_edges)
                after = _surplus_on(adj, edges, n_edges)
                c_after = loops6_through(adj, u1, v2, -1, -1) + loops6_through(adj, u2, v1, u1, v2)
                _switch(adj, u1, v2, u2, v1)
                before = _surplus_on(adj, edges, n_edges)
                _switch(adj, u1, v1, u2, v2)
                d_x = after - before
                d_c = c_after - c_before
                d_h = -16.0 * d_s + 4.0 * lam * d_x + mu * d_c
                if d_h > 0.0 and np.random.random() >= np.exp(-d_h * inv_g):
                    ok = False
            if ok:
                s += d_s
                x += d_x
                c6 += d_c
            else:
                _switch(adj, u1, v2, u2, v1)
        out[sweep, 0] = s
        out[sweep, 1] = x
        out[sweep, 2] = c6
    return out


def side_of(length):
    return np.array([x * length + y for x in range(4) for y in range(length) if (x + y) % 2 == 0], dtype=np.int64)


def moves_out(adj, side_u, lam):
    """Every switch out of this graph as (d_S, d_X, d_C6), with how many there are; by trying each one."""
    kinds = {}
    for u1 in side_u:
        for v1 in adj[u1]:
            for u2 in side_u:
                if u2 == u1:
                    continue
                for v2 in adj[u2]:
                    if v1 == v2 or v2 in adj[u1] or v1 in adj[u2]:
                        continue
                    trial = adj.copy()
                    s0, x0 = total_squares(trial), surplus(trial)
                    c0 = total_loops6(trial, side_u)
                    _switch(trial, int(u1), int(v1), int(u2), int(v2))
                    if not (_new_edge_ok(trial, int(u1), int(v2), NO_CAP) and _new_edge_ok(trial, int(u2), int(v1), NO_CAP)):
                        continue
                    key = (int(total_squares(trial) - s0), int(surplus(trial) - x0), int(total_loops6(trial, side_u) - c0))
                    kinds[key] = kinds.get(key, 0) + 1
    return kinds


def walls(length=12, lam=1.25):
    for name, shift in (("the tube (four around)", 0), ("the tube with its seam shifted by two (six around)", 2)):
        adj = twisted_tube(length, shift)
        side = side_of(length)
        n = adj.shape[0]
        print("%s, N = %d: squares %d, surplus %d, six-loops %d (2N = %d; extra per point %.2f)"
              % (name, n, total_squares(adj), surplus(adj), total_loops6(adj, side), 2 * n,
                 (total_loops6(adj, side) - 2 * n) / n))
        kinds = moves_out(adj, side, lam)
        for mu in (0.0, 0.5, 1.0, 1.5, 2.0, 3.0):
            cost = sorted((-16.0 * ds + 4.0 * lam * dx + mu * dc, ds, dx, dc, k) for (ds, dx, dc), k in kinds.items())
            print("   mu = %.1f: cheapest moves out (cost, dS, dX, dC6, how many): %s"
                  % (mu, "; ".join("%.1f %d %d %d x%d" % c for c in cost[:3])))


def run(length, mu, g, sweeps=20000, replicas=4, start="twist", lam=1.25, cool=0):
    n = 4 * length
    side = side_of(length)
    print("N=%d lambda=%.2f mu=%.2f g=%.2f start=%s, %d sweeps" % (n, lam, mu, g, start, sweeps))
    for rep in range(replicas):
        adj = twisted_tube(length, 2 if start == "twist" else 0)
        out = run_six(adj, side, 1.0 / g, sweeps, 2026101500 + 7919 * rep + int(100 * mu) + int(100 * g), lam, mu)
        assert (total_squares(adj), surplus(adj), total_loops6(adj, side)) == tuple(out[-1])   # the books are exact
        extra = out[:, 2] - 2 * n
        gone = np.flatnonzero(extra <= 0)
        for step in range(40 if cool else 0):                        # optional slow cooling from g down to 0.3
            run_six(adj, side, 1.0 / (g + (0.3 - g) * (step + 1) / 40), max(1, cool // 40), -1, lam, mu)
        run_six(adj, side, 1.0 / 0.05, 1500, -1, lam, mu)
        end = read(adj, lam)
        print("  %d: extra six-loops %d -> %d (first none at sweep %s) | squares per point at the end %.3f | cold: %s"
              % (rep, extra[0], extra[-1], gone[0] if gone.size else "never", out[-1, 0] / n, line(end)))


if __name__ == "__main__":
    a = sys.argv[1:]
    if not a or a[0] == "walls":
        walls()
    else:
        run(int(a[1]), float(a[2]), float(a[3]), int(a[4]) if len(a) > 4 else 20000, int(a[5]) if len(a) > 5 else 4,
            a[6] if len(a) > 6 else "twist", float(a[7]) if len(a) > 7 else 1.25, int(a[8]) if len(a) > 8 else 0)

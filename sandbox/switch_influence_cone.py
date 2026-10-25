"""Sandbox look (exploratory; rule 16: it can kill the idea, never crown it), 25 October 2026: does influence between the
toy's own moves spread at a steady speed?

The owner's idea (VISION Update 116): the number of switches in an area, how many later switches each can influence and how
many earlier ones can influence it, is related to the speed of light. Here an order is defined from the dynamics alone:
a later accepted switch is influenced if any of its four points lies within one link (on the graph as it then is) of a
point already influenced; its four points then join the influenced set. Starting from one accepted switch after
equilibration, the influenced set's reach R(t) (largest graph distance, on the current graph, from the starting switch's
points to an influenced point) is read every sweep.

Declared before the first run (what each outcome would mean):
  STEADY : R grows roughly in proportion to time, with a similar slope across starting switches and couplings that keep
           the sheet flat: a speed nobody put in. (Kills nothing; crowns nothing.)
  JUMPS  : R leaps by many links within a sweep, because the published move can join two distant points: no light cone.
  STALLS : R stops growing well short of the sheet's size: no spread.

The chain is the toy's own (graphity.cqg.run_chain's step, copied with each accepted switch logged; Î» = 1.25, four links,
Metropolis, no cap). A flat L x L torus, L = 32 (N = 1,024). One chain sweep = 2N attempts; one fair sweep (O90) = N/96
chain sweeps, so here 1 chain sweep = 0.094 fair sweeps.
"""
import sys
from collections import deque

import numpy as np
from numba import njit

from graphity.cqg import (torus, NO_CAP, ENERGY_PER_SQUARE, ENERGY_PER_SURPLUS, _replace, _switch, _new_edge_ok,
                          _note_square_edges, _surplus_on)
from graphity.squares import has_edge, squares_on_edge


@njit(cache=True)
def chain_logged(adj, side_u, inv_g, n_sweeps, seed, lam, max_events):
    np.random.seed(seed)
    n = adj.shape[0]
    nu = side_u.shape[0]
    cap = NO_CAP
    edges = np.empty((64, 2), dtype=np.int64)
    ev = np.empty((max_events, 5), dtype=np.int64)   # sweep, u1, v1, u2, v2  (new links (u1,v2), (u2,v1))
    k = 0
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
            ok = _new_edge_ok(adj, u1, v2, cap) and _new_edge_ok(adj, u2, v1, cap)
            if ok:
                n_edges = _note_square_edges(adj, u1, v2, edges, n_edges)
                n_edges = _note_square_edges(adj, u2, v1, edges, n_edges)
                after = _surplus_on(adj, edges, n_edges)
                _switch(adj, u1, v2, u2, v1)
                before = _surplus_on(adj, edges, n_edges)
                _switch(adj, u1, v1, u2, v2)
                d_x = after - before
                d_h = -ENERGY_PER_SQUARE * d_s + ENERGY_PER_SURPLUS * lam * d_x
                if d_h > 0.0 and np.random.random() >= np.exp(-inv_g * d_h):
                    ok = False
            if ok:
                if k < max_events:
                    ev[k, 0] = sweep
                    ev[k, 1] = u1
                    ev[k, 2] = v1
                    ev[k, 3] = u2
                    ev[k, 4] = v2
                k += 1
            else:
                _switch(adj, u1, v2, u2, v1)
    return ev[:min(k, max_events)], k


def apply(adj, u1, v1, u2, v2):
    for a, old, new in ((u1, v1, v2), (v1, u1, u2), (u2, v2, v1), (v2, u2, u1)):
        row = adj[a]
        row[np.where(row == old)[0][0]] = new


def bfs(adj, sources, limit=10**9):
    dist = {s: 0 for s in sources}
    q = deque(sources)
    while q:
        a = q.popleft()
        for b in adj[a]:
            b = int(b)
            if b >= 0 and b not in dist:
                dist[b] = dist[a] + 1
                q.append(b)
    return dist


def cone(adj0, events, start, n_sweeps):
    """Replay events from index `start`; return R per sweep after the start (largest distance from the start's points)."""
    adj = adj0.copy()
    for e in events[:start]:
        apply(adj, *map(int, e[1:]))
    s0 = int(events[start, 0])
    pts0 = [int(x) for x in events[start, 1:]]
    apply(adj, *pts0)
    infected = set(pts0)
    near = set(infected)
    for p in list(infected):
        near.update(int(b) for b in adj[p])
    radii, sizes = [], []
    i = start + 1
    for sweep in range(s0 + 1, s0 + 1 + n_sweeps):
        while i < len(events) and events[i, 0] < sweep:
            pts = [int(x) for x in events[i, 1:]]
            hit = any(p in near for p in pts)
            apply(adj, *pts)
            if hit:
                infected.update(pts)
            if hit or any(p in infected for p in pts):
                near = set(infected)
                for p in infected:
                    near.update(int(b) for b in adj[p])
            i += 1
        d = bfs(adj, pts0)
        radii.append(max(d.get(p, -1) for p in infected))
        sizes.append(len(infected))
    return radii, sizes


def main():
    L, lam, equil, follow = 32, 1.25, 100, 200
    out = []
    for g in (2.0, 4.0, 5.0, 6.0, 7.0, 8.0):
        adj0, part = torus(L, L, cap=NO_CAP)
        side_u = np.where(part == 0)[0].astype(np.int64)
        adj = adj0.copy()
        ev, total = chain_logged(adj, side_u, 1.0 / g, equil + follow + 5, 20261025, lam, 2_000_000)
        long_links = 0
        acc_follow = int(np.sum(ev[:, 0] >= equil))
        print(f"g = {g}: accepted switches {total} over {equil + follow + 5} sweeps ({total / (equil + follow + 5):.1f} per sweep)")
        starts = [int(np.searchsorted(ev[:, 0], equil)) + j * 37 for j in range(5)]
        for st in starts:
            if st >= len(ev):
                continue
            radii, sizes = cone(adj0, ev, st, follow)
            marks = [radii[t] for t in (0, 9, 19, 49, 99, 199) if t < len(radii)]
            jumps = max(b - a for a, b in zip([0] + radii[:-1], radii))
            print(f"   start {st:6d}: R at sweeps 1,10,20,50,100,200 = {marks}; influenced points at 200 = {sizes[-1]}; largest one-sweep jump = {jumps}")
            out.append((g, st, radii, sizes))
    return out


if __name__ == "__main__":
    main()

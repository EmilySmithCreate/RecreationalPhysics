"""Sandbox look (exploratory; rule 16), 26 October 2026: paired switches under the owner's hard rule. Usage:

    python sandbox/hard_rule_pairs_look.py [radius]

`hard_rule_moves_look.py` found that no single switch keeps the square count, out of the flat 6 x 6 x 8 torus or the
rod. The hard rule as decided (VISION Update 105) also allows "moves paired so that S returns". This lists pairs: a first
switch from point 0 (every valid one), then a second switch whose four points lie within `radius` links (default 2) of
the first's four points, that brings the square count back exactly, and is not the first switch undone. Both graphs on
the way must obey the hard-core rule. For each pair: the change in curl, in anticurl, and dH at lambda = 1.25
(H = 4 anticurl + 4 (lambda - 1) curl, exact). Read: does the rule allow any paired move out of flat space, and does
it make curl and anticurl together, as her picture asks.
"""
import sys
from collections import Counter
from pathlib import Path

import numpy as np
from numba import njit

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from graphity.cqg_d import _new_edge_ok, _replace, _switch, has_edge, squares_on_edge, torus  # noqa: E402

LAM = 1.25


@njit(cache=True)
def try_switch(adj, u1, v1, u2, v2):
    """Apply the switch if it is a legal move; return (applied, dS). Leaves adj unchanged when not applied."""
    if u1 == u2 or v1 == v2 or not has_edge(adj, u1, v1) or not has_edge(adj, u2, v2):
        return False, 0
    if has_edge(adj, u1, v2) or has_edge(adj, u2, v1):
        return False, 0
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
    if not (_new_edge_ok(adj, u1, v2) and _new_edge_ok(adj, u2, v1)):
        _switch(adj, u1, v2, u2, v1)
        return False, 0
    return True, gained - lost


@njit(cache=True)
def second_moves(adj, ball, part, need, f_u1, f_v1, f_u2, f_v2, out):
    """Every second switch with its u's in `ball` (one side at a time) and dS = need; writes rows to out."""
    deg = adj.shape[1]
    m = 0
    nb = ball.shape[0]
    for i in range(nb):
        a1 = ball[i]
        for j in range(i + 1, nb):
            a2 = ball[j]
            if part[a1] != part[a2]:
                continue
            for k1 in range(deg):
                b1 = adj[a1, k1]
                for k2 in range(deg):
                    b2 = adj[a2, k2]
                    ok, ds = try_switch(adj, a1, b1, a2, b2)
                    if not ok:
                        continue
                    # undoing the first switch exactly is (u1, v2, u2, v1) in either order
                    undo = ((a1 == f_u1 and b1 == f_v2 and a2 == f_u2 and b2 == f_v1) or
                            (a1 == f_u2 and b1 == f_v1 and a2 == f_u1 and b2 == f_v2))
                    if ds == need and not undo and m < out.shape[0]:
                        out[m, 0] = a1
                        out[m, 1] = b1
                        out[m, 2] = a2
                        out[m, 3] = b2
                        m += 1
                    _switch(adj, a1, b2, a2, b1)
    return m


@njit(cache=True)
def curl_anti(adj):
    n = adj.shape[0]
    c = 0
    a = 0
    for u in range(n):
        for k in range(adj.shape[1]):
            v = adj[u, k]
            if u < v:
                s = squares_on_edge(adj, u, v)
                if s > 4:
                    c += s - 4
                elif s < 4:
                    a += 4 - s
    return c, a


def ball_of(adj, seeds, radius):
    seen = set(seeds)
    frontier = list(seeds)
    for _ in range(radius):
        nxt = []
        for v in frontier:
            for w in adj[v]:
                w = int(w)
                if w not in seen:
                    seen.add(w)
                    nxt.append(w)
        frontier = nxt
    return np.array(sorted(seen), dtype=np.int64)


def survey(name, dims, radius):
    adj0, part = torus(dims)
    part = np.asarray(part, dtype=np.int64)
    c0, a0 = curl_anti(adj0)
    side = np.flatnonzero(part == part[0])
    out = np.empty((200000, 4), dtype=np.int64)
    found = Counter()
    firsts = Counter()
    n_first = 0
    for v1 in adj0[0]:
        for u2 in side:
            for v2 in adj0[u2]:
                adj = adj0.copy()
                ok, ds1 = try_switch(adj, 0, int(v1), int(u2), int(v2))
                if not ok:
                    continue
                n_first += 1
                ball = ball_of(adj, [0, int(v1), int(u2), int(v2)], radius)
                m = second_moves(adj, ball, part, -ds1, 0, int(v1), int(u2), int(v2), out)
                if m:
                    firsts[ds1] += 1
                for r in range(m):
                    b = adj.copy()
                    try_switch(b, *[int(x) for x in out[r]])
                    c, a = curl_anti(b)
                    found[(c - c0, a - a0, round(4 * (a - a0) + 4 * (LAM - 1) * (c - c0), 2))] += 1
    print(f"{name} {dims}, radius {radius}: {n_first} first switches from point 0; "
          f"{sum(firsts.values())} of them have a second switch that restores the count")
    print(f"  first switches with a partner, by their dS: {dict(sorted(firsts.items()))}")
    for k, n in sorted(found.items(), key=lambda kv: kv[0][2])[:25]:
        print(f"    (change in curl, change in anticurl, dH at lambda 1.25) {k}: {n} ordered pairs")


if __name__ == "__main__":
    r = int(sys.argv[1]) if len(sys.argv) > 1 else 2
    survey("flat", [6, 6, 8], r)

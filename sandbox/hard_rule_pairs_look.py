"""Sandbox look (exploratory; rule 16), 26 October 2026: paired switches under the owner's hard rule. Usage:

    python sandbox/hard_rule_pairs_look.py [radius]

`hard_rule_moves_look.py` found that no single switch keeps the square count, out of the flat 6 x 6 x 8 torus or the
rod. The hard rule as decided (VISION Update 105) also allows "moves paired so that S returns". This lists pairs: a first
switch from point 0 (every valid one), then a second switch whose four points lie within `radius` links (default 2) of
the first's four points, that brings the square count back exactly, and is not the first switch undone. Both graphs on
the way must obey the hard-core rule. For each pair: the change in curl, in anticurl, and dH at lambda = 1.25
(H = 4 anticurl + 4 (lambda - 1) curl, exact). Read: does the rule allow any paired move out of flat space, and does
it make curl and anticurl together, as her picture asks.

    python sandbox/hard_rule_pairs_look.py damaged <end-state .npz>

counts the count-keeping single switches in a saved end state of the push look.
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
                    # undoing the first switch removes (u1, v2) and (u2, v1); written from the u side it is
                    # (u1, v2, u2, v1) in either order, from the v side (v2, u1, v1, u2) in either order.
                    # Corrected 26 October (O159; Codex F21): the v-side form was missing, so every "restoring
                    # pair" the first version found was the undo.
                    undo = ((a1 == f_u1 and b1 == f_v2 and a2 == f_u2 and b2 == f_v1) or
                            (a1 == f_u2 and b1 == f_v1 and a2 == f_u1 and b2 == f_v2) or
                            (a1 == f_v2 and b1 == f_u1 and a2 == f_v1 and b2 == f_u2) or
                            (a1 == f_v1 and b1 == f_u2 and a2 == f_v2 and b2 == f_u1))
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


def edge_set(adj):
    return {(min(u, int(v)), max(u, int(v))) for u in range(adj.shape[0]) for v in adj[u]}


def survey(name, dims, radius):
    adj0, part = torus(dims)
    part = np.asarray(part, dtype=np.int64)
    c0, a0 = curl_anti(adj0)
    side = np.flatnonzero(part == part[0])
    out = np.empty((200000, 4), dtype=np.int64)
    found = Counter()
    firsts = Counter()
    e0 = edge_set(adj0)
    back = 0
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
                    back += edge_set(b) == e0
                    c, a = curl_anti(b)
                    found[(c - c0, a - a0, round(4 * (a - a0) + 4 * (LAM - 1) * (c - c0), 2))] += 1
    print(f"{name} {dims}, radius {radius}: {n_first} first switches from point 0; "
          f"{sum(firsts.values())} of them have a second switch that restores the count")
    print(f"  restoring pairs found: {sum(found.values())}, of which {back} return the starting edge set exactly")
    print(f"  first switches with a partner, by their dS: {dict(sorted(firsts.items()))}")
    for k, n in sorted(found.items(), key=lambda kv: kv[0][2])[:25]:
        print(f"    (change in curl, change in anticurl, dH at lambda 1.25) {k}: {n} ordered pairs")


def damaged(path):
    """Count-keeping single switches in a saved end state, each switch counted once (u1 < u2). Added 26 October (O159;
    Codex F22): Update 128's counts of 84, 114 and 28 came from an uncommitted scratch script that counted each switch
    four times (both orders, and both sides of the bipartition)."""
    z = np.load(path)
    adj0 = np.asarray(z["adj"], dtype=np.int64)
    part = np.asarray(z["part"], dtype=np.int64)
    c0, a0 = curl_anti(adj0)
    lam = float(z["lam"]) if "lam" in z else LAM
    legal = keep = 0
    dh = Counter()
    n = adj0.shape[0]
    # a switch written from side 0 is the same switch written from side 1, so side 0 only, u1 < u2
    for u1 in range(n):
        if part[u1] != 0:
            continue
        for u2 in range(u1 + 1, n):
            if part[u2] != 0:
                continue
            for v1 in adj0[u1]:
                for v2 in adj0[u2]:
                    adj = adj0.copy()
                    ok, ds = try_switch(adj, u1, int(v1), u2, int(v2))
                    if not ok:
                        continue
                    legal += 1
                    if ds == 0:
                        keep += 1
                        c, a = curl_anti(adj)
                        dh[round(4 * (a - a0) + 4 * (lam - 1) * (c - c0), 2)] += 1
    print(f"{path}: curl {c0}, anticurl {a0}; {legal} legal switches, {keep} keep the count "
          f"(each counted once); dH at lambda {lam}: {dict(sorted(dh.items()))}")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "damaged":
        damaged(sys.argv[2])
    else:
        r = int(sys.argv[1]) if len(sys.argv) > 1 else 2
        survey("flat", [6, 6, 8], r)

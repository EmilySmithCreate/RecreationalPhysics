"""Sandbox look (exploratory; rule 16), 26 October 2026: what the owner's hard rule allows with six links. Usage:

    python sandbox/hard_rule_moves_look.py

The hard rule (VISION Update 105, the owner's decision of 25 October): curl minus anticurl is held at exactly zero, so
with six links the number of squares stays at 3N, and a move is allowed only if it leaves the count unchanged. Before
any X is built under it (VISION Update 127; her "proceed" of 26 October), this lists every single switch out of two
states, from one point (both are tori, so every point is equivalent; switches are drawn as in `cqg_d`, u1 and u2 on one
side, v1 and v2 among their neighbours):

  the flat torus 6 x 6 x 8 (N = 288, curl = anticurl = 0: it obeys the rule), and
  the rod 4 x 4 x 18 (N = 288, curl 576, anticurl 0: it does not, and is listed for comparison).

For each valid switch: the change in squares dS, and for those with dS = 0 the curl and anticurl it leaves and dH at
lambda = 1.25 (H = 4 anticurl + 4 (lambda - 1) curl, exact, VISION Update 127). Read: does the rule allow any move out
of flat space, what does it make (a curl-anticurl pair, as her picture asks), and at what cost.
"""
import sys
from collections import Counter
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from graphity.cqg_d import _new_edge_ok, _switch, has_edge, is_valid, squares_on_edge, torus, total_squares  # noqa: E402

LAM = 1.25


def curl_anti(adj):
    n = adj.shape[0]
    c = a = 0
    for u in range(n):
        for v in adj[u]:
            if u < v:
                s = squares_on_edge(adj, u, int(v))
                c += max(s - 4, 0)
                a += max(4 - s, 0)
    return c, a


def moves(adj, part):
    u1 = 0
    side = np.flatnonzero(part == part[u1])
    for v1 in adj[u1]:
        for u2 in side:
            if u2 == u1:
                continue
            for v2 in adj[u2]:
                v1, v2 = int(v1), int(v2)
                if v2 == v1 or has_edge(adj, u1, v2) or has_edge(adj, int(u2), v1):
                    continue
                yield u1, v1, int(u2), v2


def survey(name, dims):
    adj0, part = torus(dims)
    s0 = total_squares(adj0)
    c0, a0 = curl_anti(adj0)
    ds_count = Counter()
    kept = Counter()
    for u1, v1, u2, v2 in moves(adj0, part):
        adj = adj0.copy()
        _switch(adj, u1, v1, u2, v2)
        if not is_valid(adj):
            continue
        ds = total_squares(adj) - s0
        ds_count[ds] += 1
        if ds == 0:
            c, a = curl_anti(adj)
            dh = 4 * (a - a0) + 4 * (LAM - 1) * (c - c0)
            kept[(c - c0, a - a0, round(dh, 2))] += 1
    print(f"{name} {dims}: squares {s0} (flat value {3 * adj0.shape[0]}), curl {c0}, anticurl {a0}")
    print(f"  valid single switches from point 0, by change in squares: {dict(sorted(ds_count.items()))}")
    if kept:
        print("  those keeping the count (dS = 0), by (change in curl, change in anticurl, dH at lambda 1.25): count")
        for k, n in sorted(kept.items(), key=lambda kv: kv[0][2]):
            print(f"    {k}: {n}")
    else:
        print("  none keeps the count: the hard rule allows no single switch here")


if __name__ == "__main__":
    survey("flat", [6, 6, 8])
    survey("rod", [4, 4, 18])

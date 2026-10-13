"""Sandbox look, 12 October 2026 (sandbox/LOG.md). Not evidence.

The owner: "what if melting isnt allowed the connections return to connecting locally close points pretty
quick?" One way to say that in the toy with no new length in it: a link whose two ends are not otherwise close
is a link on no square (take it away and its ends are more than three steps apart). Call that a bare link. A
melted network is mostly bare links; a flat one has none.

    hard rule   no bare link is ever allowed (a rule on the arrangements, like the hard-core rule)
    soft rule   a bare link costs kappa on top of the toy's energy, so it is short-lived

Three looks at 96 points and lambda = 1.25, named points:
    A  exact: the ways out of the curled tube, the tube six around and the tube eight around, with and without
       the hard rule
    B  the curled tube in the paper's bath (g = 1.5): does it still burp, and what comes out?
    C  a flat tube put in a hot bath and cooled again: does it melt, and does it come back?

    python sandbox/no_far_links.py [A|B|C]
"""
import sys
from collections import Counter
from pathlib import Path

import numpy as np
from numba import njit

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
sys.path.insert(0, str(ROOT / "src"))
from exact_sixloop_walls import switches                          # noqa: E402
from graphity.cqg import (NO_CAP, _new_edge_ok, _note_square_edges, _replace, _surplus_on, _switch, hamiltonian,  # noqa: E402
                          is_valid, surplus, total_squares)
from graphity.squares import has_edge, squares_on_edge             # noqa: E402
from read_leftover_width import read as read_shape                 # noqa: E402
from run_sixloop_widen import seam_shifted                         # noqa: E402

LAM = 1.25
LENGTH = 24                                                        # 96 points


@njit(cache=True)
def bare_links(adj):
    """Links on no square."""
    k = 0
    for u in range(adj.shape[0]):
        for j in range(4):
            v = adj[u, j]
            if u < v and squares_on_edge(adj, u, v) == 0:
                k += 1
    return k


@njit(cache=True)
def _bare_on(adj, edges, n):
    k = 0
    for i in range(n):
        a, b = edges[i, 0], edges[i, 1]
        if has_edge(adj, a, b) and squares_on_edge(adj, a, b) == 0:
            k += 1
    return k


@njit(cache=True)
def run_local(adj, side_u, inv_g, n_sweeps, seed, lam, kappa, hard):
    """cqg.run_chain with the cap off and one addition: a bare link costs kappa, or, if `hard`, no move that
    leaves one is accepted. Returns (S, X, bare, fewest S on the way, most bare on the way, acceptance).
    A rule on arrangements, or an energy term, with the same symmetric proposals: detailed balance holds."""
    if seed >= 0:
        np.random.seed(seed)
    n = adj.shape[0]
    nu = side_u.shape[0]
    edges = np.empty((64, 2), dtype=np.int64)
    s, x, b = total_squares(adj), surplus(adj), bare_links(adj)
    s_min, b_max = s, b
    accepted = 0
    for _sweep in range(n_sweeps):
        for _ in range(2 * n):
            u1 = side_u[np.random.randint(0, nu)]
            v1 = adj[u1, np.random.randint(0, 4)]
            u2 = side_u[np.random.randint(0, nu)]
            v2 = adj[u2, np.random.randint(0, 4)]
            if u1 == u2 or v1 == v2 or has_edge(adj, u1, v2) or has_edge(adj, u2, v1):
                continue
            n_edges = _note_square_edges(adj, u1, v1, edges, 0)
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
            d_b = 0
            ok = _new_edge_ok(adj, u1, v2, NO_CAP) and _new_edge_ok(adj, u2, v1, NO_CAP)
            if ok:
                n_edges = _note_square_edges(adj, u1, v2, edges, n_edges)
                n_edges = _note_square_edges(adj, u2, v1, edges, n_edges)
                after_x = _surplus_on(adj, edges, n_edges)
                after_b = _bare_on(adj, edges, n_edges)
                _switch(adj, u1, v2, u2, v1)
                d_x = after_x - _surplus_on(adj, edges, n_edges)
                d_b = after_b - _bare_on(adj, edges, n_edges)
                _switch(adj, u1, v1, u2, v2)
                if hard and after_b > 0:
                    ok = False
            if ok:
                d_h = -16.0 * d_s + 4.0 * lam * d_x + kappa * d_b
                if d_h > 0.0 and np.random.random() >= np.exp(-inv_g * d_h):
                    ok = False
            if ok:
                s += d_s
                x += d_x
                b += d_b
                accepted += 1
                if s < s_min:
                    s_min = s
                if b > b_max:
                    b_max = b
            else:
                _switch(adj, u1, v2, u2, v1)
    return s, x, b, s_min, b_max, accepted / max(2 * n * n_sweeps, 1)


RULES = (("none", 0.0, False), ("soft 8", 8.0, False), ("soft 32", 32.0, False), ("hard", 0.0, True))


def look_a():
    print("A. Exact: single switches out of three tubes of 96 points, lambda = %.2f. Cost = -16 dS + 5 dX." % LAM)
    for shift, name in ((0, "curled tube (4 around)"), (2, "six around"), (4, "eight around")):
        adj, side = seam_shifted(LENGTH, shift)
        allowed, banned = [], []
        for (move, d_s, d_x, _d6) in switches(adj, side):
            trial = adj.copy()
            _switch(trial, *move)
            (banned if bare_links(trial) else allowed).append(-16 * d_s + 4 * LAM * d_x)
        both = allowed + banned
        print("  %-24s switches %5d, cheapest %5.1f | leaving a bare link: %5d (cheapest %s) | leaving none: %5d "
              "(cheapest %s, and %d at that cost)" % (
                  name, len(both), min(both), len(banned), "%.1f" % min(banned) if banned else "-", len(allowed),
                  "%.1f" % min(allowed) if allowed else "-", sum(c == min(allowed) for c in allowed) if allowed else 0))


def cool(adj, side, g_from, g_to, sweeps, steps, lam, kappa, hard):
    worst_s, worst_b = total_squares(adj), 0
    for k in range(steps):
        g = g_from + (g_to - g_from) * (k + 1) / steps
        _s, _x, _b, s_min, b_max, _acc = run_local(adj, side, 1.0 / g, sweeps // steps, -1, lam, kappa, hard)
        worst_s, worst_b = min(worst_s, s_min), max(worst_b, b_max)
    return worst_s, worst_b


def finish(adj, n):
    kind, sees3, clear, c25, c22 = read_shape(adj)[:5]
    word = "WIDE" if sees3 >= 0.5 else ("TUBE" if sees3 < 0.05 else "PATCHWORK")
    return dict(h=hamiltonian(adj, LAM), x=int(surplus(adj)), bare=int(bare_links(adj)), kind=kind, word=word,
                sees3=sees3, clear=clear, c25=c25, c22=c22, valid=bool(is_valid(adj, NO_CAP)))


def look_b(replicas=12, hold=30000, cool_sweeps=20000):
    print("B. The curled tube, 96 points, lambda = %.2f, g = 1.5: %d sweeps warm, %d cooling to 0.5, 500 cold."
          % (LAM, hold, cool_sweeps))
    for name, kappa, hard in RULES:
        ends, gone, s_low = [], [], []
        for rep in range(replicas):
            adj, side = seam_shifted(LENGTH, 0)
            np.random.seed(7000 + rep)
            run_local(adj, side, 1.0 / 1.5, 0, 7000 + rep, LAM, kappa, hard)        # seeds the stream
            first, low = -1, int(total_squares(adj))
            for block in range(hold // 500):
                _s, x, _b, s_min, _bm, _acc = run_local(adj, side, 1.0 / 1.5, 500, -1, LAM, kappa, hard)
                low = min(low, s_min)
                if first < 0 and x == 0:
                    first = 500 * (block + 1)
            low = min(low, cool(adj, side, 1.5, 0.5, cool_sweeps, 20, LAM, kappa, hard)[0])
            run_local(adj, side, 1.0 / 0.05, 500, -1, LAM, kappa, hard)
            ends.append(finish(adj, 96))
            gone.append(first)
            s_low.append(low / 96)
        words = Counter(e["word"] for e in ends)
        print("  %-8s curl gone in %2d of %d (median sweep %s) | exactly flat %2d | TUBE %d, PATCHWORK %d, WIDE %d | "
              "energy left: median %.0f, most %.0f | bare links left %d | fewest squares per point %.2f | all valid %s"
              % (name, sum(g >= 0 for g in gone), replicas,
                 int(np.median([g for g in gone if g >= 0])) if any(g >= 0 for g in gone) else "-",
                 sum(e["h"] == 0 for e in ends), words["TUBE"], words["PATCHWORK"], words["WIDE"],
                 float(np.median([e["h"] for e in ends])), max(e["h"] for e in ends), sum(e["bare"] for e in ends),
                 min(s_low), all(e["valid"] for e in ends)))


def look_c(replicas=6, hot=3000, cool_sweeps=12000):
    print("C. A flat tube of 96 points heated and cooled: %d sweeps hot, %d cooling to 0.5, 500 cold." % (hot, cool_sweeps))
    for shift, start in ((2, "six around"), (4, "eight around")):
        for g in (3.0, 5.0, 8.0):
            for name, kappa, hard in RULES:
                ends, low, bare = [], [], []
                for rep in range(replicas):
                    adj, side = seam_shifted(LENGTH, shift)
                    _s, _x, _b, s_min, b_max, acc = run_local(adj, side, 1.0 / g, hot, 9000 + rep, LAM, kappa, hard)
                    s_hot = int(total_squares(adj))
                    cool(adj, side, g, 0.5, cool_sweeps, 24, LAM, kappa, hard)
                    run_local(adj, side, 1.0 / 0.05, 500, -1, LAM, kappa, hard)
                    ends.append(finish(adj, 96))
                    low.append(s_hot / 96)
                    bare.append(b_max)
                words = Counter(e["word"] for e in ends)
                print("  %-12s g = %.0f %-8s | squares per point while hot %.2f to %.2f | most bare links at once %3d | "
                      "after cooling: exactly flat %d of %d; TUBE %d, PATCHWORK %d, WIDE %d; energy left median %.0f; "
                      "clear points seeing 25: %d, seeing 22: %d"
                      % (start, g, name, min(low), max(low), max(bare), sum(e["h"] == 0 for e in ends), replicas,
                         words["TUBE"], words["PATCHWORK"], words["WIDE"], float(np.median([e["h"] for e in ends])),
                         sum(e["c25"] for e in ends), sum(e["c22"] for e in ends)))


if __name__ == "__main__":
    which = sys.argv[1] if len(sys.argv) > 1 else "ABC"
    if "A" in which:
        look_a()
    if "B" in which:
        look_b()
    if "C" in which:
        look_c()

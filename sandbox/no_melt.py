"""Sandbox: "what if melted isn't a thing?" (the owner, 12 October 2026). Usage:

    python sandbox/no_melt.py pieces                       # which pieces of T61's end states are flat on their own
    python sandbox/no_melt.py heal [G] [MARGIN] [SWEEPS] [NAME] [LAMBDA] [WANT]

`heal` takes saved end states of T61 (all read) and runs the toy's own chain with one change: a ceiling on the
energy. A move is refused if it would lift the energy more than MARGIN above the lowest value reached so far. So
flaws can wander and cancel, and the fabric can never melt: there is never room for more than about one flaw
beyond those already there. Does a patchwork then heal, and into what?
"""
import csv
import sys
from collections import Counter
from pathlib import Path

import numpy as np
from numba import njit

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "scripts"))
sys.path.insert(0, str(ROOT / "sandbox"))
from graphity.cqg import (NO_CAP, _new_edge_ok, _note_square_edges, _replace, _surplus_on, _switch,   # noqa: E402
                          has_edge, squares_on_edge, surplus, total_squares)
from read_endpoint_width import is_flat, width                       # noqa: E402
from read_flat_kind import describe, kind, pieces                     # noqa: E402
from shape_tools import line, read                                    # noqa: E402


@njit(cache=True)
def run_ceiling(adj, side_u, inv_g, n_sweeps, seed, lam, margin):
    """graphity.cqg.run_chain's moves and acceptance, with a ceiling: no move may lift the energy more than
    `margin` above the lowest energy reached so far. Returns (lowest energy, highest energy seen, energy at end)."""
    if seed >= 0:
        np.random.seed(seed)
    n = adj.shape[0]
    nu = side_u.shape[0]
    edges = np.empty((64, 2), dtype=np.int64)
    h = 16.0 * (n - total_squares(adj)) + 4.0 * lam * surplus(adj)
    low = h
    high = h
    for _sweep in range(n_sweeps):
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
            d_h = 0.0
            ok = _new_edge_ok(adj, u1, v2, NO_CAP) and _new_edge_ok(adj, u2, v1, NO_CAP)
            if ok:
                n_edges = _note_square_edges(adj, u1, v2, edges, n_edges)
                n_edges = _note_square_edges(adj, u2, v1, edges, n_edges)
                after = _surplus_on(adj, edges, n_edges)
                _switch(adj, u1, v2, u2, v1)
                before = _surplus_on(adj, edges, n_edges)
                _switch(adj, u1, v1, u2, v2)
                d_h = -16.0 * (gained - lost) + 4.0 * lam * (after - before)
                if h + d_h > low + margin + 1e-9:
                    ok = False
                elif d_h > 0.0 and np.random.random() >= np.exp(-d_h * inv_g):
                    ok = False
            if ok:
                h += d_h
                if h < low:
                    low = h
                if h > high:
                    high = h
            else:
                _switch(adj, u1, v2, u2, v1)
    return low, high, h


def saved(name):
    rows = list(csv.DictReader(open(ROOT / "results" / (name + ".csv"), newline="", encoding="utf-8")))
    for r in rows:
        z = np.load(ROOT / "results" / (name + "_adj") / ("N%s_C%s_rep%s.npz" % (r["N"], r["stores"], r["replica"])))
        yield r, z["adj"].copy(), z["part"]


def outcome(r):
    s3 = float(r["sees3"])
    return "WIDE" if s3 >= 0.5 else ("TUBE" if s3 < 0.05 else "PATCHWORK")


def flat_pieces():
    """Among T61's end states that are not flat as a whole: the pieces that are exactly flat on their own."""
    import glob
    names = sorted(Path(f).stem for f in glob.glob(str(ROOT / "results" / "t61_lam*_n*.csv")))
    tally, total, with_flat = Counter(), 0, 0
    for name in names:
        for r, adj, _part in saved(name):
            if is_flat(adj):
                continue
            ps = pieces(adj)
            if len(ps) < 2:
                continue
            total += 1
            flat = [(p.shape[0], kind(p), width(p, 0)) for p in ps if is_flat(p)]
            with_flat += bool(flat)
            for size, k, w in flat:
                tally[(k, w)] += 1
    print("T61 end states that are not flat as a whole and are in two or more pieces: %d" % total)
    print("of those, with at least one piece that is exactly flat on its own: %d" % with_flat)
    for (k, w), count in sorted(tally.items(), key=lambda kv: -kv[1]):
        print("   flat pieces that are a %s, %s around: %d" % (k, w, count))


def heal(g=2.0, margin=32.0, sweeps=200000, name="t61_lam140_n96", lam=1.40, want="WIDE"):
    chosen = [(r, adj, part) for r, adj, part in saved(name) if outcome(r) == want]
    print("%d %s end states of %s; energy ceiling %.0f above the lowest reached; g = %.2f; %d sweeps"
          % (len(chosen), want, name, margin, g, sweeps), flush=True)
    ends = Counter()
    for i, (r, adj, part) in enumerate(chosen):
        side = np.flatnonzero(part == 0).astype(np.int64)
        before = read(adj, lam)
        low, high, end = run_ceiling(adj, side, 1.0 / g, sweeps, 4242 + i, lam, margin)
        run_ceiling(adj, side, 1.0 / 0.05, 2000, -1, lam, 0.0)
        after = read(adj, lam)
        what = "; ".join("%d points, %s, %s around" % p for p in describe(adj)) if after["flat"] else ""
        ends["flat: " + what if after["flat"] else "not flat"] += 1
        print("  before %5.1f, sees3 %.2f | highest on the way %5.1f | after: %s %s"
              % (before["energy"], before["sees3"], high, line(after), what), flush=True)
    print("ends:", dict(ends))


if __name__ == "__main__":
    a = sys.argv[1:]
    if not a or a[0] == "pieces":
        flat_pieces()
    else:
        heal(float(a[1]) if len(a) > 1 else 2.0, float(a[2]) if len(a) > 2 else 32.0,
             int(a[3]) if len(a) > 3 else 200000, a[4] if len(a) > 4 else "t61_lam140_n96",
             float(a[5]) if len(a) > 5 else 1.40, a[6] if len(a) > 6 else "WIDE")

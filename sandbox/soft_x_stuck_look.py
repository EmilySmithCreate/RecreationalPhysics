"""Sandbox look (rule 16: can kill, never crown), 27 October 2026: is the nearest buildable X of the owner's picture stuck
for now under her soft rule? Words declared here before anything ran.

Her picture (VISION Update 133, answers of 17:41 and 17:51 UTC): a rod (two curled directions) with curl toward the north
pole and anticurl toward the south, balanced; lambda the same everywhere that can seed or open; anticurl priced at lambda
as curl is; soft penalty mu0 (S - 3N)^2 / N. Exact (O164 addendum): her energy at lambda is lambda H(lambda') with
lambda' = 2 - 1/lambda, so H_her = lambda (-16 dS + 4 lambda' dX) + mu0 ((S + dS - 3N)^2 - (S - 3N)^2) / N per move.

Starting states, with rule obedience stated: (X) the rod 4 x 4 x L with its south half (z >= L/2) melted by random legal
switches confined to that half, each kept only if S stays >= 3N, until S = 3N exactly: OBEYS the hard rule (S = 3N),
curl in the north half, anticurl in the south; three melt seeds, L = 16 and 24. The toy has no handedness: north and
south are curl and anticurl only. (R) the plain rod 4 x 4 x L, S = 3.5N: BREAKS the rule; control. (F) the flat 6 x 6 x 8
torus, S = 3N: OBEYS; control.

What is read: every legal single switch (u1 < u2 on one side), its dS and dX exactly, and its change in H_her at lambda in
{1.10, 1.25, 1.40} and mu0 in {1, 16, 256}. Words: STUCK (every legal switch raises H_her) / NOT STUCK (some switch lowers
it or leaves it unchanged); for NOT STUCK, the count of downhill or level switches, the lowest change, and where they sit
(all four ends in the north half, all in the south, or across).

Ours, declared before running: X is NOT STUCK at every lambda and mu0, with the downhill switches in the melted south
half (anticurl heals: each unit costs 4 lambda, and one switch changes S by a few squares, so the penalty on one move is
mu0 dS^2 / N, small at these sizes); F STUCK; R STUCK (the rod family is stuck for lambda' below 1.5, and lambda' =
2 - 1/lambda is below 1.5 at every lambda here).
"""
import sys
from pathlib import Path

import numpy as np
from numba import njit

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from graphity import cqg_d  # noqa: E402
from graphity.cqg_d import (_new_edge_ok, _note_square_edges, _replace, _surplus_on, _switch, has_edge,  # noqa: E402
                            squares_on_edge, total_squares)

OUT = ROOT / "sandbox" / "out" / "soft_x_stuck"


@njit(cache=True)
def delta(adj, u1, v1, u2, v2, edges):
    """(legal, dS, dX) of the switch (u1,v1),(u2,v2) -> (u1,v2),(u2,v1); adj is left as it was."""
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
    ok = _new_edge_ok(adj, u1, v2) and _new_edge_ok(adj, u2, v1)
    d_x = 0
    if ok:
        n_edges = _note_square_edges(adj, u1, v2, edges, n_edges)
        n_edges = _note_square_edges(adj, u2, v1, edges, n_edges)
        after = _surplus_on(adj, edges, n_edges)
        _switch(adj, u1, v2, u2, v1)
        before = _surplus_on(adj, edges, n_edges)
        d_x = after - before
    else:
        _switch(adj, u1, v2, u2, v1)
    return ok, gained - lost, d_x


@njit(cache=True)
def all_moves(adj, side):
    """Every legal single switch with u1 < u2 on the given side: rows (u1, v1, u2, v2, dS, dX)."""
    deg = adj.shape[1]
    edges = np.empty((4 * (1 + 3 * (deg - 1)) + 8, 2), dtype=np.int64)
    out = np.empty((side.shape[0] * side.shape[0] * deg * deg // 2 + 1, 6), dtype=np.int64)
    m = 0
    for i in range(side.shape[0]):
        u1 = side[i]
        for j in range(i + 1, side.shape[0]):
            u2 = side[j]
            for k1 in range(deg):
                v1 = adj[u1, k1]
                for k2 in range(deg):
                    v2 = adj[u2, k2]
                    if v1 == v2 or has_edge(adj, u1, v2) or has_edge(adj, u2, v1):
                        continue
                    ok, ds, dx = delta(adj, u1, v1, u2, v2, edges)
                    if ok:
                        out[m, 0] = u1
                        out[m, 1] = v1
                        out[m, 2] = u2
                        out[m, 3] = v2
                        out[m, 4] = ds
                        out[m, 5] = dx
                        m += 1
    return out[:m]


@njit(cache=True)
def melt_south(adj, side, south, s_target, seed, max_tries):
    """Random legal switches with all four ends in the south half, kept only if S stays >= s_target; stop at equality."""
    np.random.seed(seed)
    deg = adj.shape[1]
    edges = np.empty((4 * (1 + 3 * (deg - 1)) + 8, 2), dtype=np.int64)
    s = total_squares(adj)
    for t in range(max_tries):
        if s == s_target:
            return s, t
        u1 = side[np.random.randint(0, side.shape[0])]
        u2 = side[np.random.randint(0, side.shape[0])]
        v1 = adj[u1, np.random.randint(0, deg)]
        v2 = adj[u2, np.random.randint(0, deg)]
        if u1 == u2 or v1 == v2 or not (south[u1] and south[u2] and south[v1] and south[v2]):
            continue
        if has_edge(adj, u1, v2) or has_edge(adj, u2, v1):
            continue
        ok, ds, dx = delta(adj, u1, v1, u2, v2, edges)
        if ok and s + ds >= s_target:
            _switch(adj, u1, v1, u2, v2)
            s += ds
    return s, max_tries


def read(name, adj, part, regions, lines):
    n = adj.shape[0]
    side = np.flatnonzero(part == 0).astype(np.int64)
    s = int(total_squares(adj))
    moves = all_moves(adj, side)
    ds, dx = moves[:, 4].astype(float), moves[:, 5].astype(float)
    lines.append(f"{name}: N = {n}, S = {s} (3N = {3 * n}, S - 3N = {s - 3 * n}), valid {bool(cqg_d.is_valid(adj))}, "
                 f"legal switches {len(moves)}")
    for lam in (1.10, 1.25, 1.40):
        lp = 2 - 1 / lam
        for mu0 in (1.0, 16.0, 256.0):
            dh = lam * (-16 * ds + 4 * lp * dx) + mu0 * ((s - 3 * n + ds) ** 2 - (s - 3 * n) ** 2) / n
            down = dh <= 1e-9
            word = "STUCK" if not down.any() else "NOT STUCK"
            where = ""
            if down.any() and regions is not None:
                ends = moves[down][:, :4]
                north = int((~regions[ends]).all(axis=1).sum())
                south = int(regions[ends].all(axis=1).sum())
                where = f"; north {north}, south {south}, across {int(down.sum()) - north - south}"
            up = dh[~down].min() if (~down).any() else float("nan")
            lines.append(f"  lambda {lam:.2f} (lambda' {lp:.4f}), mu0 {mu0:5.0f}: {word}; downhill or level "
                         f"{int(down.sum())}, lowest dH {dh.min():9.3f}, cheapest uphill {up:8.3f}{where}")


def main():
    lines = []
    for L in (16, 24):
        for seed in (1, 2, 3):
            adj, part = cqg_d.torus((4, 4, L))
            n = adj.shape[0]
            south = (np.arange(n) % L) >= L // 2
            side = np.flatnonzero(part == 0).astype(np.int64)
            s, tries = melt_south(adj, side, south, 3 * n, seed, 50_000_000)
            assert s == 3 * n, (L, seed, s)
            read(f"X (rod 4 x 4 x {L}, south half melted to S = 3N, seed {seed}, {tries} tries)", adj, part, south, lines)
        adj, part = cqg_d.torus((4, 4, L))
        read(f"R (plain rod 4 x 4 x {L}, control, breaks the rule)", adj, part, None, lines)
    adj, part = cqg_d.torus((6, 6, 8))
    read("F (flat 6 x 6 x 8, control)", adj, part, None, lines)
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "soft_x_stuck.txt").write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()

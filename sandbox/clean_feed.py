"""Sandbox look, 18 October 2026: the owner's picture run as a rule (rule 16; a look, not evidence).

Her picture (notebook, 18 October): energy arrives at every point of the slab equally; a point is closed (four
around) or open (six around) and nothing else; breaking is not in the picture. In the toy every single switch from
the slab leaves four broken points, so the picture needs a move the toy lacks: two switches at once that leave no
point broken. This script runs that move set on the untied slab 4 x L x L with a store at every point:

  * the feed adds r/N to every store each sweep (T68's "all" place);
  * a move is two switches, the second anchored within two steps of the first, accepted only if the hard-core rule
    holds and NO point is left broken (every point at d <= 3 after the move; the slab starts clean, so the whole
    graph stays clean);
  * its cost dH is paid from the pooled stores of the moved points (up to eight), each paying in proportion to what
    it holds; a release is credited to them evenly; a move the pool cannot pay is refused. No temperature.
  * a sweep is N attempts.

Written per block: open points (d = 3), curled (d = 2), the largest open region and the number of open regions,
the energy, the stores. Energy is checked conserved at the end (H + stores - fed = H0). With --break the clean check
is skipped, as a control on the same move set. Nothing here is registered.
"""
import sys
import time

import numpy as np
from numba import njit

sys.path.insert(0, "src")
sys.path.insert(0, "scripts")
from graphity.cqg_d import _switch, has_edge, hamiltonian, is_valid, torus          # noqa: E402
from graphity.dimension import _share_d, local_dimension_d, pieces_of               # noqa: E402
from exact_lowest_path import _local_energy, _ok_around, _patch_points             # noqa: E402


@njit(cache=True)
def d_at(adj, v):
    deg = adj.shape[1]
    c = 0
    for i in range(deg):
        a = adj[v, i]
        for j in range(i + 1, deg):
            if not _share_d(adj, a, adj[v, j], v):
                c += 1
    return c


@njit(cache=True)
def _add(out, n, x):
    for t in range(n):
        if out[t] == x:
            return n
    out[n] = x
    return n + 1


@njit(cache=True)
def _near_side0(adj, part, anchor):
    """A side-0 point within two steps of anchor (a neighbour if anchor is side 1; else a neighbour's neighbour)."""
    deg = adj.shape[1]
    if part[anchor] == 1:
        return adj[anchor, np.random.randint(0, deg)]
    a = adj[anchor, np.random.randint(0, deg)]
    return adj[a, np.random.randint(0, deg)]


@njit(cache=True)
def attempt(adj, part, stores, side0, lam, allow_break, pts1, pts2, four, ends, allpts):
    """One compound move. Returns (accepted 0/1, dH)."""
    deg = adj.shape[1]
    nu = side0.shape[0]
    u1 = side0[np.random.randint(0, nu)]
    v1 = adj[u1, np.random.randint(0, deg)]
    u2 = _near_side0(adj, part, u1)
    v2 = adj[u2, np.random.randint(0, deg)]
    if u1 == u2 or v1 == v2 or has_edge(adj, u1, v2) or has_edge(adj, u2, v1):
        return 0, 0.0
    n1 = _patch_points(adj, u1, v1, u2, v2, pts1)
    before = _local_energy(adj, pts1, n1, lam)
    _switch(adj, u1, v1, u2, v2)
    four[0] = u1; four[1] = u2; four[2] = v1; four[3] = v2
    if not _ok_around(adj, four):
        _switch(adj, u1, v2, u2, v1)
        return 0, 0.0
    dh = _local_energy(adj, pts1, n1, lam) - before
    # second switch, anchored at the first's endpoints
    a1 = _near_side0(adj, part, four[np.random.randint(0, 4)])
    b1 = adj[a1, np.random.randint(0, deg)]
    a2 = _near_side0(adj, part, four[np.random.randint(0, 4)])
    b2 = adj[a2, np.random.randint(0, deg)]
    if a1 == a2 or b1 == b2 or has_edge(adj, a1, b2) or has_edge(adj, a2, b1):
        _switch(adj, u1, v2, u2, v1)
        return 0, 0.0
    n2 = _patch_points(adj, a1, b1, a2, b2, pts2)
    before2 = _local_energy(adj, pts2, n2, lam)
    _switch(adj, a1, b1, a2, b2)
    four2 = four.copy()
    four2[0] = a1; four2[1] = a2; four2[2] = b1; four2[3] = b2
    ok = _ok_around(adj, four2)
    if ok:
        dh += _local_energy(adj, pts2, n2, lam) - before2
        if not allow_break:
            na = 0
            for t in range(n1):
                na = _add(allpts, na, pts1[t])
            for t in range(n2):
                na = _add(allpts, na, pts2[t])
            for t in range(na):
                if d_at(adj, allpts[t]) > 3:
                    ok = False
                    break
    if ok:
        ne = 0
        for e in (u1, v1, u2, v2, a1, b1, a2, b2):
            ne = _add(ends, ne, e)
        pool = 0.0
        for t in range(ne):
            pool += stores[ends[t]]
        if dh > pool:
            ok = False
        elif dh >= 0.0:
            if pool > 0.0:
                for t in range(ne):
                    stores[ends[t]] -= dh * stores[ends[t]] / pool
        else:
            for t in range(ne):
                stores[ends[t]] -= dh / ne
    if not ok:
        _switch(adj, a1, b2, a2, b1)
        _switch(adj, u1, v2, u2, v1)
        return 0, 0.0
    return 1, dh


@njit(cache=True)
def run_block(adj, part, stores, side0, lam, allow_break, n_sweeps, rate):
    n, deg = adj.shape
    pts1 = np.empty(4 + 4 * deg, dtype=np.int64)
    pts2 = np.empty(4 + 4 * deg, dtype=np.int64)
    allpts = np.empty(2 * (4 + 4 * deg), dtype=np.int64)
    four = np.empty(4, dtype=np.int64)
    ends = np.empty(8, dtype=np.int64)
    acc = 0
    dh_sum = 0.0
    for _ in range(n_sweeps):
        for i in range(n):
            stores[i] += rate / n
        for _ in range(n):
            a, dh = attempt(adj, part, stores, side0, lam, allow_break, pts1, pts2, four, ends, allpts)
            acc += a
            dh_sum += dh
    return acc, dh_sum


def run(L, lam, rate, seed, max_sweeps, every, allow_break=False, log=print):
    adj, part = torus((4, L, L))
    n = adj.shape[0]
    side0 = np.flatnonzero(part == 0).astype(np.int64)
    stores = np.zeros(n)
    h0 = hamiltonian(adj, lam)
    np.random.seed(seed)
    _seed_numba(seed)
    fed = 0.0
    t0 = time.time()
    rows = []
    for sweep in range(0, max_sweeps, every):
        acc, _ = run_block(adj, part, stores, side0, lam, allow_break, every, rate)
        fed += every * rate
        d = local_dimension_d(adj)
        op = int((d == 3).sum()); cu = int((d == 2).sum()); br = int((d > 3).sum()); lo = int((d < 2).sum())
        regions = pieces_of(adj, d == 3)
        h = hamiltonian(adj, lam)
        row = dict(sweep=sweep + every, open=op, curled=cu, broken=br, low=lo, regions=len(regions),
                   largest=int(regions[0]) if len(regions) else 0, H=h, stores=float(stores.sum()), acc=acc)
        rows.append(row)
        if acc or sweep + every >= max_sweeps or op >= 0.9 * n:
            log("  L=%d lam=%.2f r=%g seed=%d sweep %6d: open %3d curled %3d broken %3d regions %3d largest %3d  H %7.1f stores %8.1f acc %d" %
                (L, lam, rate, seed, sweep + every, op, cu, br, len(regions), row["largest"], h, stores.sum(), acc))
        if op >= 0.9 * n:
            break
    assert is_valid(adj)
    cons = h + stores.sum() - fed - h0
    log("  conservation H + stores - fed - H0 = %.6f; %.0f s" % (cons, time.time() - t0))
    return rows


@njit(cache=True)
def _seed_numba(seed):
    np.random.seed(seed)


if __name__ == "__main__":
    allow_break = "--break" in sys.argv
    L = 8
    lam = 1.25
    for rate in (2.0, 8.0, 32.0):
        for seed in (1, 2):
            run(L, lam, rate, seed, max_sweeps=6000, every=100, allow_break=allow_break)

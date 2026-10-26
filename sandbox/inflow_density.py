"""Sandbox look, 19 October 2026 (rule 16; one line in LOG): inflow rate against density.

The owner's handoff of 19 October (`docs/theory/omega_opening_inflow_density_handoff_2026-10-19.md`) asks whether
energy that keeps arriving while the opening is under way, spread through the curled region, could leave spatial
differences in the new space's energy. Its program: a symmetry control (a uniform inflow must give zero contrast), then
the spatial response to a uniform, a time-varying and a spatially variable inflow at the same total. This script runs
that program on what the toy has.

  A. Arithmetic, no run. A feed that arrives in deposits of size q at random points is a Poisson sprinkle: when the
     stores hold m per point, the contrast per point is sqrt(q / m), averaged over b points sqrt(q / (m b)), and the
     spectrum is flat (white). The RATE never enters; only the grain q and the amount m do.
  B. The layer form (VISION Update 65, gate g1 of Update 69): the slab 4 x L x L fed to the gate under four feeds at the
     same mean rate: uniform (the "all" place of T68 and T71), uniform in space but bursty in time, random deposits of
     q = 1, random deposits of q = 4; and the random feed at four times the rate. At the first sweep at which any cut's
     pool holds a N_slab the split is made with the actual kernel. Read: the stores' field in the parent at that moment
     (the inflow since the gate; under Update 66 the daughter is a ledger and carries exactly a N_slab, uniform), its
     contrast against the arithmetic, and the field under the reference rule f1 (release credited to the two layers
     beside the cut; new layers at zero), whose pattern has the width as its scale.
  C. The front form (the 2D tube, 4 x L, sealed with a store at every side-0 point; `sealed.run_sealed_bath`,
     by_vertex): the same four feeds, the feed stopped when nine tenths of the columns have opened, 5,000 sealed sweeps
     more, then read per column: the sweep at which the column opened, the store energy, the wiring energy above
     flat, their sum. The lump is credited to the store of the point whose move released it, so in this form the
     product has a spatial energy field. Read its contrast, its block-averaged contrast against block size (white:
     1 / sqrt(b)), its power along the ring (white: flat), and the correlation between when a column opened and what
     it ends with.

Nothing here is registered or evidence. Output: `sandbox/out/inflow_density_2026-10-19.txt`.

    PYTHONPATH="src;scripts" python sandbox/inflow_density.py
"""
import sys
import time

import numpy as np
from numba import njit

sys.path.insert(0, "src")
from graphity import contraction as C                                   # noqa: E402
from graphity import sealed                                             # noqa: E402
from graphity.cqg import NO_CAP, hamiltonian, squares_on_edge, surplus, torus   # noqa: E402

RNG0 = 20261019


def contrast_stats(field, blocks=(1, 2, 4, 8, 16), axis_len=None):
    """Per-point contrast of a 1D or flattened field, and the rms after averaging over b consecutive entries."""
    f = np.asarray(field, dtype=float).ravel()
    m = f.mean()
    if m <= 0:
        return dict(mean=m, rms=float("nan"), blocks={})
    d = f / m - 1.0
    out = {}
    for b in blocks:
        if b > len(f) // 2:
            continue
        nb = len(f) // b
        out[b] = float(np.sqrt(np.mean(d[: nb * b].reshape(nb, b).mean(axis=1) ** 2)))
    return dict(mean=float(m), rms=float(np.sqrt(np.mean(d ** 2))), blocks=out)


def ring_power(field):
    """Power per mode of the contrast along a ring, binned by |k| into octaves; returns (bin edges in k index, P)."""
    f = np.asarray(field, dtype=float)
    d = f / f.mean() - 1.0
    p = np.abs(np.fft.rfft(d)) ** 2 / len(d)
    k = np.arange(len(p))
    edges = [1, 2, 4, 8, 16, 32, 64, 128, 256]
    rows = []
    for lo, hi in zip(edges[:-1], edges[1:]):
        sel = (k >= lo) & (k < hi)
        if sel.any():
            rows.append((lo, hi, float(p[sel].mean())))
    return rows


def slope(rows):
    """Fitted slope of log P against log k over the octave bins (white: 0)."""
    if len(rows) < 3:
        return float("nan")
    x = np.log([np.sqrt(lo * hi) for lo, hi, _ in rows])
    y = np.log([max(p, 1e-30) for _, _, p in rows])
    return float(np.polyfit(x, y, 1)[0])


# ---------------------------------------------------------------- A. arithmetic
def part_a(log):
    log("A. Arithmetic (exact; no run). A feed in deposits of size q at random points: when the stores hold m per point,")
    log("   contrast per point = sqrt(q/m); over b points sqrt(q/(m b)); spectrum flat. The rate does not enter.")
    for lam in (1.10, 1.25, 1.40):
        a = 4 * (lam - 1)
        log("   lambda %.2f: gate g1 is reached at m = 2a = %.2f per point (uniform feed); q = 1 gives contrast %.2f, q = 4 gives %.2f,"
            " q = 0.01 gives %.3f" % (lam, 2 * a, np.sqrt(1 / (2 * a)), np.sqrt(4 / (2 * a)), np.sqrt(0.01 / (2 * a))))
    log("   For a contrast of 1e-5 per point at m = 2 the grain must be q = 2e-10 of a unit: the inflow's grain, not its rate, sets it.")
    log("")


# ---------------------------------------------------------------- B. layer form
def feed_once(stores, kind, r, q, sweep, rng):
    n = len(stores)
    if kind == "uniform":
        stores += r
        return r * n
    if kind == "bursty":
        amt = 2 * r if (sweep // 10) % 2 == 0 else 0.0
        stores += amt
        return amt * n
    k = rng.poisson(r * n / q)
    idx = rng.integers(0, n, k)
    np.add.at(stores, idx, q)
    return float(k * q)


def layer_run(L, lam, kind, r, q, seed, log):
    a = 4 * (lam - 1)
    st = C.build((4, L, L))
    n = st.n
    gate = a * n
    rng = np.random.default_rng(seed)
    fed = 0.0
    sweep = 0
    while True:
        sweep += 1
        fed += feed_once(st.stores, kind, r, q, sweep, rng)
        pools = [float(st.stores[C.pool_mask(st, 0, x0, False)].sum()) for x0 in range(st.dims[0])]
        if max(pools) >= gate:
            break
        if sweep > 10_000_000:
            raise RuntimeError("no gate")
    x0 = int(np.argmax(pools))
    before = st.stores.copy()
    f0 = C.energy(st, lam)
    cand = C.split_layers(st, 0, x0, max_width=8)
    release = f0 - C.energy(cand, lam)
    # the parent's field at the burp, read on the (y, z) plane summed over the curled direction
    plane = np.zeros((L, L))
    np.add.at(plane, (st.coords[:, 1], st.coords[:, 2]), before)
    stats = contrast_stats(before)
    stats_plane = contrast_stats(plane.ravel())
    pred = np.sqrt(q / before.mean()) if kind == "random" else 0.0
    # the f1 reference: release credited evenly to the two layers beside the cut; new layers at zero
    rec = C.receiving_mask(cand, 0, x0, False)
    f1 = cand.stores.copy()
    f1[rec] += release / int(rec.sum())
    by_layer = np.array([f1[cand.coords[:, 0] == x].mean() for x in range(cand.dims[0])])
    log("   %-8s r=%-6g q=%-4g seed %d: gate at sweep %6d, fed %8.1f (%.3f per point), release %.1f = a N? %s; parent's field:"
        " mean %.3f, contrast per point %.3f (arithmetic %.3f), per column of 4 %.3f, over 4x4 columns %.3f;"
        " f1 field per layer %s"
        % (kind, r, q, seed, sweep, fed, fed / n, release, abs(release - gate) < 1e-9, stats["mean"], stats["rms"], pred,
           stats_plane["rms"], stats_plane["blocks"].get(16, float("nan")), np.round(by_layer, 2).tolist()))
    return stats["rms"]


def part_b(log):
    L, lam = 16, 1.25
    log("B. Layer form, slab 4 x %d x %d, lambda %.2f, gate g1 = a N_slab, split made with the kernel at the first sweep the gate holds." % (L, L, lam))
    cells = [("uniform", 1 / 16, 1), ("bursty", 1 / 16, 1), ("random", 1 / 16, 1), ("random", 1 / 16, 4), ("random", 1 / 4, 1),
             ("random", 1 / 16, 0.01)]
    for kind, r, q in cells:
        for rep in range(3):
            layer_run(L, lam, kind, r, q, RNG0 + rep, log)
    log("")


# ---------------------------------------------------------------- C. front form (2D tube)
@njit(cache=True)
def column_fields(adj, lam, L):
    """Per column (points 4c..4c+3 of torus(L, 4)): wiring energy above flat and surplus squares, each edge half to
    each end."""
    n = adj.shape[0]
    energy = np.zeros(L)
    surp = np.zeros(L)
    for u in range(n):
        for i in range(4):
            v = adj[u, i]
            if v < u:
                continue
            se = squares_on_edge(adj, u, v)
            e = 4.0 * ((2 - se) + lam * max(se - 2, 0))
            x = max(se - 2, 0)
            energy[u // 4] += e / 2
            energy[v // 4] += e / 2
            surp[u // 4] += x / 2
            surp[v // 4] += x / 2
    return energy, surp


def tube_run(L, lam, kind, r, q, seed, log, block=50, max_sweeps=80_000, settle=5_000):
    adj, part = torus(L, 4, NO_CAP)
    n = adj.shape[0]
    side = np.flatnonzero(part == 0).astype(np.int64)
    assert all(adj[u, 0] // 4 == (u // 4 + 1) % L for u in range(n))
    stores = np.zeros(n)
    active = np.zeros(n, dtype=bool)
    active[side] = True                       # by_vertex: only side-0 stores are ever drawn on
    rng = np.random.default_rng(seed)
    h0 = hamiltonian(adj, lam)
    fed = 0.0
    opened = np.full(L, -1)
    sweep = 0
    first = True
    feeding = True
    settled = 0
    while sweep < max_sweeps:
        if feeding:
            sub = stores[active]
            for s in range(block):
                fed += feed_once(sub, kind, r, q, sweep + s, rng)
            stores[active] = sub
        sealed.run_sealed_bath(adj, side, stores, block, seed if first else -1, lam, NO_CAP, None, True)
        first = False
        sweep += block
        _e, surp = column_fields(adj, lam, L)
        newly = (opened < 0) & (surp == 0)
        opened[newly] = sweep
        if feeding and (opened >= 0).sum() >= 0.9 * L:
            feeding = False
        if not feeding:
            settled += block
            if settled >= settle:
                break
    energy, surp = column_fields(adj, lam, L)
    store_c = np.array([stores[4 * c: 4 * c + 4].sum() for c in range(L)])
    total = energy + store_c
    drift = hamiltonian(adj, lam) + stores.sum() - fed - h0
    st_total = contrast_stats(total, blocks=(1, 2, 4, 8, 16, 32))
    st_store = contrast_stats(store_c, blocks=(1, 4, 16))
    rows = ring_power(total)
    done = opened >= 0
    corr = float(np.corrcoef(opened[done], total[done])[0, 1]) if done.sum() > 3 else float("nan")
    seeds_first = int((opened == opened[done].min()).sum()) if done.any() else 0
    log("   %-8s r=%-6g q=%-4g seed %d: first column open at sweep %6d (%d columns in that block), 90%% open at %6d, read at %6d; fed %.1f"
        " (%.2f per point); knots: wiring above flat %.0f, surplus %.0f; drift %.1e"
        % (kind, r, q, seed, opened[done].min() if done.any() else -1, seeds_first,
           int(np.sort(opened[done])[int(0.9 * L) - 1]) if done.sum() >= 0.9 * L else -1, sweep, fed, fed / n,
           energy.sum(), surp.sum(), drift))
    log("        energy per column (stores + wiring): mean %.2f, contrast %.3f; over 4 columns %.3f, 16 %.3f, 32 %.3f; stores alone %.3f;"
        " power by octave %s, slope %.2f; corr(opening sweep, energy) %.2f"
        % (st_total["mean"], st_total["rms"], st_total["blocks"].get(4, np.nan), st_total["blocks"].get(16, np.nan),
           st_total["blocks"].get(32, np.nan), st_store["rms"], [round(p, 3) for _, _, p in rows], slope(rows), corr))
    return st_total, rows


def part_c(log):
    L, lam = 128, 1.25
    log("C. Front form, 2D tube 4 x %d (N = %d), lambda %.2f, sealed, a store at every side-0 point; feed stopped at 90%% of columns open, then %d sweeps."
        % (L, 4 * L, lam, 5000))
    cells = [("uniform", 0.01, 1), ("bursty", 0.01, 1), ("random", 0.01, 1), ("random", 0.01, 4), ("random", 0.04, 1)]
    for kind, r, q in cells:
        for rep in range(3):
            t0 = time.time()
            tube_run(L, lam, kind, r, q, RNG0 + 100 + rep, log)
            log("        (%.0f s)" % (time.time() - t0))
    log("")


if __name__ == "__main__":
    out = open("sandbox/out/inflow_density_2026-10-19.txt", "w", encoding="utf-8")

    def log(s):
        print(s, flush=True)
        out.write(s + "\n")
        out.flush()

    part_a(log)
    part_b(log)
    part_c(log)
    out.close()

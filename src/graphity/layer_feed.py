"""The layer form's full move set in one driven protocol (VISION Update 65 and its addendum of 18 October 2026).

The move set the author confirmed: the layer moves (`contraction.py`) plus the clean two-switch move (`clean_move.py`);
the single switch is kept only as a control and lives in T68's runner (`scripts/run_slab_feed.py`), not here.

One sweep, in this order:
  1. the feed: `rate` is added to every point's store (the "all" place), unless `feed_stops_at_split` is set and a
     split has already been made;
  2. the leak: a fraction `leak` of every store leaves and is counted;
  3. N attempts of the clean two-switch move (`move_set` "model"), paid from the pooled stores of the moved points;
     none ("layer"); or N attempts of the same compound move with the clean check off ("breaking", a second control,
     NOT the registered single-switch control);
  4. `proposals_per_sweep` layer proposals (an axis, a position, split or contract), paid from the pool of the layers
     the move touches, a release credited to the two layers beside the cut, and the `gate` applied to any move that
     costs nothing: it fires only when its pool already holds `gate`, which is not spent.
Where a release goes is `release_to`: "stores" credits it evenly to the two layers beside the cut (it can then pay the
fold back); "daughter" is the owner's decision of 18 October (VISION Update 66): the lump leaves one way into a
daughter ledger that nothing in the parent can draw on, the parent keeps its geometry and its stores, and the slab
reforms when the stores can pay the contraction. Every downhill move's release is counted there; a release above zero
is one daughter. Energy is conserved exactly: F + sum(stores) + daughter - fed + leaked = F0 with F = H + mu_N N
(tests, 1e-9). The protocol claims no detailed balance; conservation is its invariant. At lambda != 1, and with a varying count of points, this is
our family around the published model, never combinatorial quantum gravity.
"""
import numpy as np

from . import clean_move as CM
from .contraction import contract_layers, energy, pool_mask, receiving_mask, split_layers
from .dimension import local_dimension_d

MOVE_SETS = ("model", "layer", "breaking")
RELEASE_TO = ("stores", "daughter")


def propose_layer_move(st, f, lam, mu_n, rng, axes, max_width, gate, release_to="stores"):
    """One layer proposal on `st` (energy f). Returns (new_state, new_f, kind, released) with kind in {None, "split",
    "contract"}; None when nothing happened. `released` is the energy a downhill move gave off: credited to the
    stores beside the cut under release_to "stores", or handed to the caller's daughter ledger under "daughter"."""
    axis = int(axes[rng.integers(len(axes))])
    x0 = int(rng.integers(st.dims[axis]))
    contract = bool(rng.integers(2))
    cand = contract_layers(st, axis, x0) if contract else split_layers(st, axis, x0, max_width)
    if cand is None:
        return st, f, None, 0.0
    f_new = energy(cand, lam, mu_n)
    df = f_new - f
    mask = pool_mask(st, axis, x0, contract)
    pool = float(st.stores[mask].sum())
    if df > 0:
        if pool + 1e-12 < df:
            return st, f, None, 0.0
        st = st.copy()
        st.stores[mask] -= st.stores[mask] * (df / pool)
        cand = contract_layers(st, axis, x0) if contract else split_layers(st, axis, x0, max_width)
    else:
        if pool + 1e-12 < gate:
            return st, f, None, 0.0
        if release_to == "stores":
            rec = receiving_mask(cand, axis, x0, contract)
            cand.stores[rec] += (-df) / int(rec.sum())
    return cand, f_new, ("contract" if contract else "split"), max(-df, 0.0)


def census(adj):
    d = local_dimension_d(adj)
    return int((d == 3).sum()), int((d == 2).sum()), int((d > 3).sum())


def run_layer_feed(state, lam, rate, n_sweeps, seed, gate=0.0, leak=0.0, feed_stops_at_split=False,
                   move_set="model", max_width=8, axes=(0,), proposals_per_sweep=1, mu_n=0.0, log_every=1,
                   release_to="stores"):
    """The protocol of the module docstring. Returns (final_state, rows, summary).

    rows: one tuple per logged sweep, (sweep, N, dims, F, stores_sum, fed, leaked, n_split, n_contract, n_clean,
    open, curled, broken, daughters, daughter_energy). summary: dict(first_split, first_clean, first_contract) as
    sweeps or None, and f0. Under release_to "stores" the last two columns stay zero.
    """
    assert move_set in MOVE_SETS and release_to in RELEASE_TO
    rng = np.random.default_rng(seed)
    np.random.seed(int(rng.integers(2**31 - 1)))
    CM.seed_numba(int(rng.integers(2**31 - 1)))
    st = state.copy()
    f = energy(st, lam, mu_n)
    f0 = f
    fed = leaked = 0.0
    n_split = n_contract = n_clean = 0
    daughters, daughter_energy = 0, 0.0
    first = dict(first_split=None, first_clean=None, first_contract=None)
    work = CM.work_arrays(st.adj.shape[1])
    side0 = np.flatnonzero(st.part == 0).astype(np.int64)
    rows = []
    for sweep in range(1, n_sweeps + 1):
        if not (feed_stops_at_split and first["first_split"] is not None):
            st.stores += rate
            fed += rate * st.n
        if leak > 0:
            out = leak * st.stores
            st.stores -= out
            leaked += float(out.sum())
        if move_set != "layer":
            acc, dh_sum = CM.run_block(st.adj, st.part, st.stores, side0, lam, move_set == "breaking", 1, 0.0, *work)
            if acc:
                n_clean += acc
                f += dh_sum
                if first["first_clean"] is None:
                    first["first_clean"] = sweep
        for _ in range(proposals_per_sweep):
            st, f, kind, released = propose_layer_move(st, f, lam, mu_n, rng, axes, max_width, gate, release_to)
            if kind is None:
                continue
            if release_to == "daughter" and released > 1e-9:
                daughters += 1
                daughter_energy += released
            side0 = np.flatnonzero(st.part == 0).astype(np.int64)
            if kind == "split":
                n_split += 1
                if first["first_split"] is None:
                    first["first_split"] = sweep
            else:
                n_contract += 1
                if first["first_contract"] is None:
                    first["first_contract"] = sweep
        if sweep % log_every == 0 or sweep == n_sweeps:
            op, cu, br = census(st.adj)
            rows.append((sweep, st.n, tuple(st.dims), float(f), float(st.stores.sum()), fed, leaked, n_split,
                         n_contract, n_clean, op, cu, br, daughters, daughter_energy))
    first["f0"] = f0
    return st, rows, first


def conservation_residuals(f0, rows):
    """F + stores + daughter - fed + leaked - F0 for every logged row."""
    return [r[3] + r[4] + (r[14] if len(r) > 14 else 0.0) - r[5] + r[6] - f0 for r in rows]

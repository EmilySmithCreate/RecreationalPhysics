"""Sandbox look, 15 October 2026 (rule 16; one line in LOG). The owner's picture: the slab (4 x L x L, one direction
curled) is X; under her tie "all at the last" it holds the whole burp, 3a per point (O106); the barrier to opening it
is a patch of a few columns (T54, O118), not one move. Here the patch is opened BY HAND above T54's critical size and
the box is then sealed with empty stores: does the opening spread to the whole slab and release 3a per point into the
stores, or fall back, or break the space? T9's room question in three directions. The tie is the table as the owner
decided it (a damaged point pays nothing); nothing new in the energy. Not registered; nothing here is evidence.

    python3 sandbox/slab_patch_sealed.py  >  sandbox/out/slab_patch_sealed.txt
"""
import sys, time
import numpy as np
sys.path.insert(0, "scripts"); sys.path.insert(0, "src")
from exact_t54_patch import patch, tie_table          # noqa: E402
from graphity.cqg_d import torus                      # noqa: E402
from graphity.dimension import local_dimension_d      # noqa: E402
from graphity.sealed_tie_d import run_sealed_bath_table_d, energy_table_d  # noqa: E402
from run_sealed_curled_d import census_any            # noqa: E402

L = int(sys.argv[1]) if len(sys.argv) > 1 else 8
CELLS = [  # (lam, k, stores per point)
    (1.25, 0, 4), (1.25, 1, 4), (1.25, 2, 1), (1.25, 2, 4), (1.25, 3, 1), (1.25, 3, 4),
    (1.20, 3, 4), (1.20, 4, 4),
]
REPS, SWEEPS, EVERY = 3, 20000, 1000
print("slab 4 x %d x %d, tie all at the last, sealed from a hand-opened patch, empty stores" % (L, L))
print("lam k C/N rep | start: H_tied/N d-census | end: H_tied/N d-census(d0..d3,d>3) store_mean left_at")
for lam, k, cpn in CELLS:
    ftab = tie_table("all_at_the_last", lam)
    for rep in range(REPS):
        adj0, part = torus([4, L, L])
        adj, _ = patch(adj0, L, k)
        n = adj.shape[0]
        side_u = np.flatnonzero(part == 0)
        stores = np.zeros(cpn * n)
        h0 = energy_table_d(adj, lam, ftab)
        d0 = local_dimension_d(adj)
        c0 = [int((d0 == i).sum()) for i in range(4)] + [int((d0 > 3).sum())]
        seed = int(np.random.SeedSequence([20261015, L, int(lam * 100), k, cpn, rep]).generate_state(1)[0])
        t0 = time.time(); left_at = None; s_prev = None
        for b in range(1, SWEEPS // EVERY + 1):
            s, x, t, mean, tot, _ = run_sealed_bath_table_d(adj, side_u, stores, EVERY, seed if b == 1 else -1, lam, ftab, by_vertex=False)
        d = local_dimension_d(adj)
        c = [int((d == i).sum()) for i in range(4)] + [int((d > 3).sum())]
        h1 = energy_table_d(adj, lam, ftab)
        drift = abs(h1 + stores.sum() - h0)
        print(f"{lam} {k} {cpn} {rep} | {h0/n:+.3f} {c0} | {h1/n:+.3f} {c} store {stores.mean():.3f} drift {drift:.1e} ({time.time()-t0:.0f}s)", flush=True)

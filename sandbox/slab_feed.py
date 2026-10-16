"""Sandbox look, 16 October 2026 (rule 16; one line in LOG). The owner: the push is "a flow with various rates based on
what black hole eats and so it's one spot per seed". Untied slab 4 x 8 x 8 (N = 256), lambda 1.25, sealed with 4N
empty stores; each sweep r units are added to the stores: mode "shared", into store 0 of the shared bath (any move may
draw it); mode "spot", per-vertex stores with the feed into one point's store (only moves from that point spend it).
Every 100 sweeps: open (d = 3), curled (d <= 2), damaged (d > 3) points, the number of separate open regions, the store
mean. Stops at 10,000 sweeps or when open >= 0.9 N. Not registered; nothing here is evidence.

    python3 sandbox/slab_feed.py > sandbox/out/slab_feed.txt
"""
import sys, time
import numpy as np
sys.path.insert(0, "src")
from graphity.cqg_d import torus                                              # noqa: E402
from graphity.dimension import local_dimension_d, pieces_of                  # noqa: E402
from graphity.sealed_tie_d import run_sealed_bath_table_d, energy_table_d     # noqa: E402

LAM = 1.25; FTAB = np.zeros(4); L = 8
RATES = [2.0, 8.0, 32.0]; MODES = ["shared", "spot"]; REPS = 3; SWEEPS = 10000; EVERY = 100
print("untied slab 4 x %d x %d, lambda %.2f, feed r units a sweep, sealed, up to %d sweeps" % (L, L, LAM, SWEEPS))
print("mode | r | rep | sweep | open curled damaged | open regions | store mean | first sweep open>N/2 (regions then) | drift")
for mode in MODES:
    for r in RATES:
        for rep in range(REPS):
            adj, part = torus([4, L, L]); n = adj.shape[0]
            side_u = np.flatnonzero(part == 0)
            by_vertex = mode == "spot"
            stores = np.zeros(n if by_vertex else 4 * n)
            feed_idx = int(side_u[0]) if by_vertex else 0
            seed = int(np.random.SeedSequence([20261016, 7, int(r), rep, by_vertex]).generate_state(1)[0])
            fed = 0.0; h0 = energy_table_d(adj, LAM, FTAB); half = None; t0 = time.time()
            for b in range(SWEEPS // EVERY):
                run_sealed_bath_table_d(adj, side_u, stores, EVERY, seed if b == 0 else -1, LAM, FTAB, by_vertex=by_vertex)
                stores[feed_idx] += r * EVERY; fed += r * EVERY
                d = local_dimension_d(adj)
                op, cu, dm = int((d == 3).sum()), int((d <= 2).sum()), int((d > 3).sum())
                regions = len(pieces_of(adj, d == 3)) if op else 0
                if half is None and op > n // 2:
                    half = ((b + 1) * EVERY, regions)
                if op >= 0.9 * n:
                    break
            drift = abs(energy_table_d(adj, LAM, FTAB) + stores.sum() - h0 - fed)
            print(f"{mode} | {r:.0f} | {rep} | {(b+1)*EVERY} | {op} {cu} {dm} | {regions} | {stores.mean():.2f} | {half} | {drift:.1e} ({time.time()-t0:.0f}s)", flush=True)

"""Sandbox look, 16 October 2026 (rule 16; one line in LOG). The owner's prediction: flat three-direction space under
the tie heals damage in fewer sweeps than flat two-direction space untied. Same N = 216 (12 x 18 against 6 x 6 x 6),
lambda 1.25, energy E packed into one store of a bath of 4N empty stores (T9's protocol), sealed. Each sweep: the
number of damaged points (d above the flat value), the mean store energy. Reported per replica: the peak damage and its
sweep, the first sweep after the peak at which damage is at most 2 (the scar of O82) and at which it is 0, the damage
and the store mean at the end. Not registered; nothing here is evidence.

    python3 sandbox/heal_time.py > sandbox/out/heal_time.txt
"""
import sys, time
import numpy as np
sys.path.insert(0, "src")
from graphity.cqg_d import torus                                              # noqa: E402
from graphity.dimension import local_dimension_d                              # noqa: E402
from graphity.sealed_tie_d import run_sealed_bath_table_d, energy_table_d     # noqa: E402

LAM = 1.25
A = 4 * (LAM - 1)
CASES = [  # label, dims, ftab
    ("2D untied 12x18", [12, 18], np.zeros(3)),
    ("3D tied   6x6x6", [6, 6, 6], np.array([0.0, A, 2 * A, 0.0])),
    ("3D untied 6x6x6", [6, 6, 6], np.zeros(4)),
]
ENERGIES = [192.0, 384.0, 768.0]
REPS, SWEEPS, EVERY = 8, 4000, 2
print("N = 216, lambda %.2f, bath of 4N stores, E packed in one store, sealed, %d sweeps, read every %d" % (LAM, SWEEPS, EVERY))
print("case | E | rep | peak damaged @sweep | first <=2 after peak | first 0 after peak | end damaged, store mean | drift")
for label, dims, ftab in CASES:
    D = len(dims)
    for E in ENERGIES:
        rows = []
        for rep in range(REPS):
            adj, part = torus(dims)
            n = adj.shape[0]
            side_u = np.flatnonzero(part == 0)
            stores = np.zeros(4 * n); stores[0] = E
            h0 = energy_table_d(adj, LAM, ftab) + stores.sum()
            seed = int(np.random.SeedSequence([20261016, D, int(E), rep]).generate_state(1)[0])
            dam = []
            for b in range(SWEEPS // EVERY):
                run_sealed_bath_table_d(adj, side_u, stores, EVERY, seed if b == 0 else -1, LAM, ftab, by_vertex=False)
                dam.append(int((local_dimension_d(adj) > D).sum()))
            dam = np.array(dam)
            ip = int(dam.argmax()); peak = int(dam[ip])
            after = dam[ip:]
            t2 = np.flatnonzero(after <= 2); t0 = np.flatnonzero(after == 0)
            t2 = (int(t2[0]) * EVERY) if len(t2) else None
            t0 = (int(t0[0]) * EVERY) if len(t0) else None
            drift = abs(energy_table_d(adj, LAM, ftab) + stores.sum() - h0)
            rows.append((peak, (ip + 1) * EVERY, t2, t0, int(dam[-1]), stores.mean()))
            print(f"{label} | {E:.0f} | {rep} | {peak} @{(ip+1)*EVERY} | {t2} | {t0} | {dam[-1]}, {stores.mean():.3f} | {drift:.1e}", flush=True)
        t2s = [r[2] for r in rows if r[2] is not None]; t0s = [r[3] for r in rows if r[3] is not None]
        print(f"  summary {label} E={E:.0f}: peak median {np.median([r[0] for r in rows]):.0f}; <=2 reached in {len(t2s)}/{REPS}, median {np.median(t2s) if t2s else 'n/a'} sweeps after peak; 0 reached in {len(t0s)}/{REPS}, median {np.median(t0s) if t0s else 'n/a'}; end damaged median {np.median([r[4] for r in rows]):.0f}", flush=True)

"""Sandbox look, 19 October 2026 (rule 16; not evidence). The owner's "curl and uncurl, a little more curl": under
the layer form with her gate (g1 = a N_slab) and the one-way daughter rule (Update 66), how much does the parent
hold beyond what it hands to daughters, and how does that excess compare with the total released?  Also the exact
side count: in a 2D-regular bipartite graph the two kinds of point are equal in number, so the toy cannot hold an
excess of one kind.  Usage: python3 sandbox/curl_uncurl_ledger.py > sandbox/out/curl_uncurl_ledger_2026-10-19.txt"""
import numpy as np
from graphity.contraction import build, energy
from graphity.layer_feed import run_layer_feed

for L, lam, rate, n_sweeps in [(6, 1.25, 1 / 16, 3000), (8, 1.25, 1 / 16, 3000), (6, 1.10, 1 / 16, 3000)]:
    st = build((4, L, L))
    a = 4 * (lam - 1)
    n_slab = 4 * L * L
    f0 = energy(st, lam)
    final, rows, first = run_layer_feed(st, lam, rate, n_sweeps, seed=7, gate=a * n_slab, move_set="layer",
                                        release_to="daughter", log_every=50)
    sweep, n, dims, f, stores, fed, leaked, n_split, n_contract, n_clean, op, cu, br, dau, dau_e = rows[-1]
    print(f"L={L} lam={lam} r={rate:.4f} sweeps={n_sweeps}: a*N_slab={a*n_slab:.1f}, F0={f0:.1f}, F_end={f:.1f}, "
          f"stores_end={stores:.1f}, fed={fed:.1f}, daughters={dau}, daughter_energy={dau_e:.1f}, "
          f"per_daughter={dau_e/max(dau,1):.1f}, parent_excess=F_end+stores-F0={f+stores-f0:.1f}, "
          f"excess/released={(f+stores-f0)/max(dau_e,1e-9):.4f}, 1/daughters={1/max(dau,1):.4f}")
    # the two kinds of point: side counts
    part = np.asarray(final.part)
    print(f"   kinds of point at the end: side0={int((part==0).sum())} side1={int((part==1).sum())} (N={final.n})")
print("Exact: every link joins one point of each kind and every point has the same number of links, so the two kinds "
      "are equal in number in every valid state at every size; an excess of one kind is impossible in the toy.")

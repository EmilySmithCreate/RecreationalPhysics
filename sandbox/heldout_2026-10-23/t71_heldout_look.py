"""Scratch (2026-10-23), for the T71 held-out amendment draft: per-replica details of the stage-1 cells (L = 8, 12)
that the registered analyzer reads only as medians. Reads results/t71_* only (already read and scored, O144).

    PYTHONPATH="src;scripts" python3 sandbox/heldout_2026-10-23/t71_heldout_look.py

Prints, per cell (lam, L, r, move_set, release_to): the gate sweep t_gate (the smallest sweep s with
2 L^2 r s + 1e-12 >= gate, the kernel's own test on a pool of two layers of L^2 points... see note), the offsets
first_split - t_gate (min, median, max), the clean-switch counts, the largest stores per point seen in a logged row,
the end width and end F classes, and the per-replica energy per daughter / a N_slab. Then the control cells by
analyse_t68's rules. Nothing is written anywhere.
"""
import csv
import math
import sys
from collections import Counter, defaultdict
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))
sys.path.insert(0, str(ROOT / "src"))
import analyse_t71 as A  # noqa: E402

FILES = ["t71_model_lam110", "t71_model_lam125", "t71_model_lam140",
         "t71_layer_lam110", "t71_layer_lam125", "t71_layer_lam140",
         "t71_layerref_lam110", "t71_layerref_lam125", "t71_layerref_lam140"]


def t_gate(L, r, gate):
    # the pool of a split is the two layers beside the cut, 2 L^2 points, each fed r a sweep from empty
    s = gate / (2 * L * L * r)
    t = math.floor(s)
    while 2 * L * L * r * t + 1e-12 < gate:
        t += 1
    return t


def main():
    groups = defaultdict(lambda: defaultdict(list))
    for name in FILES:
        for r in csv.DictReader(open(ROOT / "results" / (name + ".csv"), newline="")):
            key = (float(r["lam"]), int(r["L"]), float(r["rate"]), r["move_set"], r["release_to"])
            groups[key][int(r["replica"])].append(r)
    for key in sorted(groups):
        lam, L, rate, ms, rel = key
        reps = groups[key]
        a_n = 4 * (lam - 1) * 4 * L * L
        gate = float(next(iter(reps.values()))[0]["gate"])
        tg = t_gate(L, rate, gate)
        offs, ncl, firstcl, maxstore, endw, endF, perd, broken, nsweeps = [], [], [], [], [], [], [], [], []
        for rep, rows in sorted(reps.items()):
            rows = sorted(rows, key=lambda x: int(x["sweep"]))
            x = A.read_replica(rows)
            offs.append(x["first_split"] - tg)
            ncl.append(int(rows[-1]["n_clean"]))
            if rows[0]["first_clean"] not in ("", "None"):
                firstcl.append(int(rows[0]["first_clean"]))
            maxstore.append(max(float(q["stores"]) / int(q["N"]) for q in rows))
            endw.append(A.width_of(rows[-1]["dims"]))
            endF.append(round(float(rows[-1]["F"]), 3))
            broken.append(int(rows[-1]["broken"]))
            nsweeps.append(int(rows[-1]["sweep"]))
            if x["per_daughter"] is not None:
                perd.append(x["per_daughter"] / a_n)
        print("lam=%.2f L=%2d r=%-8g %-6s %-8s | n_sweeps %s | t_gate %d | first_split - t_gate: min %d median %.1f max %d"
              % (lam, L, rate, ms, rel, sorted(set(nsweeps)), tg, min(offs), float(np.median(offs)), max(offs)))
        print("    clean moves: replicas with any %d/16, total %d, first at %s | max stores per point: median %.2f, max %.2f"
              % (sum(1 for c in ncl if c), sum(ncl), sorted(firstcl) if firstcl else "never", float(np.median(maxstore)), max(maxstore)))
        print("    end width %s | end F %s | end broken %s"
              % (dict(Counter(endw)), dict(Counter(endF)), dict(Counter(broken))))
        if perd:
            print("    per daughter / a N_slab: median %.4f, min %.4f, max %.4f, replicas below 1 - 1e-9: %d"
                  % (float(np.median(perd)), min(perd), max(perd), sum(1 for p in perd if p < 1 - 1e-9)))
    # the control, by analyse_t68's rules (T67's words)
    import analyse_t68 as B
    df = B.load("results", prefix="t71_control_")
    table = B.cells(df)
    print("\ncontrol (T68's runner, mode all): lam | N | rate | word | counts | median stop | median fed | fed per point | max damaged | max open")
    for k in sorted(table):
        c = table[k]
        lam, sched, mode, kk, C, rate, n = k
        g = df[(df.lam == lam) & (df.N == n) & (df.rate == rate)]
        print("%.2f | %d | %g | %s | %s | %d | %.2f | %.4f | %d | %d"
              % (lam, n, rate, c["word"], dict(c["counts"]), c["median_stop"], c["median_fed"], c["median_fed"] / n,
                 int(g["damaged"].max()), int(g["open"].max())))
    for lam in sorted(df["lam"].unique()):
        for n in sorted(df["N"].unique()):
            words = [c["word"] for k, c in table.items() if k[0] == lam and k[6] == n]
            print("control size verdict lam=%.2f N=%d: %s" % (lam, n, B.size_verdict(words)))


if __name__ == "__main__":
    main()

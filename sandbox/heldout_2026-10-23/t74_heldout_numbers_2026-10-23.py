"""Scratch (2026-10-23, sandbox; not a registered reader): the numbers for T74's held-out size L = 16, fitted on the
stage-1 results at L = 8 and 12 only, by `scripts/analyse_t74.py`'s own reading functions. Usage:

    python sandbox/heldout_2026-10-23/t74_heldout_numbers_2026-10-23.py > sandbox/out/t74_heldout_numbers_2026-10-23.txt

Reads the 108 files results/t74_lam{110,125,140}_L{08,12}_*.csv by name (they were read and scored on 21 October,
O145). Opens nothing else in results/. Writes nothing but stdout.

What it prints:
1. the mean period between fed-phase births per (lambda, L, cap, feed), pooled over the three backgrounds as the
   analyzer pools it (48 replicas), with a bootstrap over replicas (2,000 resamples, numpy seed 20261023) for the
   statistical spread, the exact a N_slab / min(c, R), and the change from L = 8 to 12;
2. per cell, the counts behind the fed and unfed words (replicas with a short fed daughter, with a clean switch move
   in the fed phase, meeting each unfed bar, with the common mean above 2a);
3. the timing ratios (mean ratio, cv ratio) per (lambda, L, cap, meals) against steady.
"""
import csv
import sys
from collections import defaultdict
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "scripts"))
import analyse_t74 as A  # noqa: E402

LAMS = (110, 125, 140)
SIZES = (8, 12)
FEEDS = ("steady", "meals16", "meals256")
CAPS = ("c2R", "cRhalf")
BGS = ("cold", "equal", "warm")


def path(lam, L, feed, cap, bg):
    return Path("results") / ("t74_lam%d_L%02d_%s_%s_%s.csv" % (lam, L, feed, cap, bg))


def read_file(p):
    rows = list(csv.DictReader(open(p, newline="")))
    cells = A.read_cells(rows)
    assert len(cells) == 1, p
    (key, cell), = cells.items()
    by_rep = defaultdict(list)
    for r in rows:
        by_rep[int(r["replica"])].append(r)
    clean_fed, clean_any, first_clean = [], [], []
    for rep, rs in sorted(by_rep.items()):
        t_unfed = int(rs[0]["t_unfed"])
        fed_rows = [r for r in rs if int(r["sweep"]) <= t_unfed]
        clean_fed.append(max(int(r["n_clean"]) for r in fed_rows))
        clean_any.append(max(int(r["n_clean"]) for r in rs))
        fc = [r["first_clean"] for r in rs if r["first_clean"] not in ("", None)]
        first_clean.append(int(float(fc[0])) if fc else None)
    cell["clean_fed"] = clean_fed
    cell["clean_any"] = clean_any
    cell["first_clean"] = first_clean
    return key, cell


def pooled_mean(periods_by_rep):
    allp = [p for ps in periods_by_rep for p in ps]
    return float(np.mean(allp)) if allp else float("nan")


def pooled_cv(periods_by_rep):
    allp = [p for ps in periods_by_rep for p in ps]
    return float(np.std(allp) / np.mean(allp)) if allp else float("nan")


def main():
    cells = {}
    for lam in LAMS:
        for L in SIZES:
            for feed in FEEDS:
                for cap in CAPS:
                    for bg in BGS:
                        p = path(lam, L, feed, cap, bg)
                        key, cell = read_file(p)
                        cells[key] = cell
                        sys.stderr.write("read %s\n" % p.name)

    rng = np.random.default_rng(20261023)
    print("== 1. Mean period between fed-phase births, backgrounds pooled (48 replicas) ==")
    print("lam   cap    feed     | L=8 mean (boot sd) cv      | L=12 mean (boot sd) cv     | exact a N/min(c,R) | "
          "change 8->12 | mean of 8,12")
    groups = defaultdict(list)
    for (lam, L, feed, cap, bg), c in cells.items():
        groups[(lam, L, feed, cap)].extend([x["periods"] for x in c["replicas"]])
    period_table = {}
    for lam in (1.10, 1.25, 1.40):
        a = 4.0 * (lam - 1.0)
        for cap in CAPS:
            exact = 16 * a if cap == "c2R" else 32 * a
            for feed in FEEDS:
                out = []
                for L in SIZES:
                    reps = groups[(lam, L, feed, cap)]
                    m = pooled_mean(reps)
                    cv = pooled_cv(reps)
                    boots = []
                    for _ in range(2000):
                        idx = rng.integers(0, len(reps), len(reps))
                        boots.append(pooled_mean([reps[i] for i in idx]))
                    out.append((m, float(np.std(boots)), cv, len(reps)))
                (m8, s8, cv8, n8), (m12, s12, cv12, n12) = out
                center = 0.5 * (m8 + m12)
                period_table[(lam, cap, feed)] = (m8, s8, m12, s12, exact, center)
                print("%.2f  %-6s %-8s | %8.4f (%.4f) %.3f [%d] | %8.4f (%.4f) %.3f [%d] | %7.3f | %+.4f (%+.2f%%) | %.4f"
                      % (lam, cap, feed, m8, s8, cv8, n8, m12, s12, cv12, n12, exact, m12 - m8,
                         100 * (m12 - m8) / m8, center))

    print()
    print("== 1b. Candidate ranges for L = 16 (center = mean of L = 8 and 12) ==")
    print("lam   cap    feed     | center  | +-10%% (registration's SAME TIMING tolerance) | linear-in-L to 16 | "
          "linear-in-1/L to 16 | 3 x max boot sd | center/exact")
    for (lam, cap, feed), (m8, s8, m12, s12, exact, center) in period_table.items():
        lin_L = m12 + (m12 - m8) * (16 - 12) / (12 - 8)
        lin_invL = m12 + (m12 - m8) * (1 / 16 - 1 / 12) / (1 / 12 - 1 / 8)
        print("%.2f  %-6s %-8s | %7.4f | %7.4f to %7.4f | %7.4f | %7.4f | %.4f | %.4f"
              % (lam, cap, feed, center, 0.9 * center, 1.1 * center, lin_L, lin_invL, 3 * max(s8, s12),
                 center / exact))

    print()
    print("== 2. Per cell: fed and unfed counts (of 16 replicas) ==")
    print("lam   L  feed     cap    bg    | fed word  short clean_fed(reps) first_clean | unfed word | wait diss fedby | "
          "above2a | median g_common 2a | digest_bal median_digestion")
    for key in sorted(cells):
        lam, L, feed, cap, bg = key
        c = cells[key]
        short = sum(not x["exact"] for x in c["replicas"])
        nf = sum(1 for k in c["clean_fed"] if k > 0)
        fc = sorted(f for f in c["first_clean"] if f is not None)
        print("%.2f %2d  %-8s %-6s %-5s | %-9s %2d %2d %s | %-50s | %2d %2d %2d | %2d | %.3f %.3f | %2d %.0f"
              % (lam, L, feed, cap, bg, c["fed_word"], short, nf, fc, c["unfed_word"], c["n_wait"],
                 c["n_dissolve"], c["n_fed_by"], c["n_common_above_2a"], c["median_g_common"], c["two_a"],
                 c["n_digest_balanced"], c["median_digestion"]))

    print()
    print("== 3. Timing ratios against steady (backgrounds pooled), as the analyzer computes them ==")
    for (lam, L, cap, feed), (word, ratio, cv_ratio) in sorted(A.timing(cells).items()):
        print("%.2f %2d %-6s %-8s | %-12s mean ratio %.4f cv ratio %.3f" % (lam, L, cap, feed, word, ratio, cv_ratio))


if __name__ == "__main__":
    main()

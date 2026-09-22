"""The T7 verdict table. Usage:

    python scripts/analyse_t7.py lam125        (reads results/t7_lam125_n*.csv)

Applies PREREGISTRATION.md section T7 exactly: gates 2 and 3, the three predictions, and the
three verdicts. Prints and writes nothing.
"""
import csv
import sys
from pathlib import Path

import numpy as np

MIN_DECAYS = 30            # gate 2
ENERGY_TOL = 0.01          # gate 3, fractional
CV_RANGE = (0.7, 1.3)      # prediction (a)
TWO_STATE_FRAC = 0.80      # prediction (b): share of vertices at d in {1, 2} at half conversion
FRONT_FRAC = 0.70          # prediction (c): largest sheet piece's share of converted vertices
CONT_CV, CONT_FRAC = 0.4, 0.5


def main(tag, out_dir="results"):
    files = sorted(Path(out_dir).glob("t7_%s_n*.csv" % tag), key=lambda p: int(p.stem.split("_n")[-1]))
    if not files:
        print("no results for", tag); return
    print("T7, %s. PREREGISTRATION.md section T7.\n" % tag)
    print("%-5s %-7s %-7s %-6s %-9s %-7s %-14s %-12s %-9s  %s"
          % ("N", "decays", "gate2", "gate3", "wait", "CV", "d in {1,2} @50%", "largest @50%", "pieces", "a b c"))
    per_size = []
    for f in files:
        rows = [r for r in csv.DictReader(open(f, newline="")) if r["reached"] and float(r["reached"]) >= 0.75]
        n = int(f.stem.split("_n")[-1])
        if not rows:
            print("%-5d 0" % n); continue
        lam = float(rows[0]["lam"])
        expect = 4.0 * (lam - 1.0)
        rel = np.array([float(r["released"]) for r in rows])
        g2 = len(rows) >= MIN_DECAYS
        g3 = bool(np.all(np.abs(rel - expect) <= ENERGY_TOL * expect))
        waits = np.array([float(r["waiting"]) for r in rows if r["waiting"]])
        cv = waits.std(ddof=1) / waits.mean() if len(waits) > 1 else np.nan
        two = np.array([(int(r["d1_50"]) + int(r["d2_50"])) / n for r in rows if r["d2_50"] != ""])
        largest = np.array([float(r["largest_50"]) for r in rows if r["largest_50"] != ""])
        pieces = np.array([int(r["pieces_50"]) for r in rows if r["pieces_50"] != ""])
        a = CV_RANGE[0] <= cv <= CV_RANGE[1]
        b = two.mean() >= TWO_STATE_FRAC
        c = largest.mean() >= FRONT_FRAC
        print("%-5d %-7d %-7s %-6s %-9.0f %-7.2f %-14s %-12s %-9s  %s %s %s"
              % (n, len(rows), "pass" if g2 else "FAIL", "pass" if g3 else "FAIL", waits.mean(), cv,
                 "%.3f +/- %.3f" % (two.mean(), two.std(ddof=1) if len(two) > 1 else 0),
                 "%.2f +/- %.2f" % (largest.mean(), largest.std(ddof=1) if len(largest) > 1 else 0),
                 "%.1f" % pieces.mean(),
                 "Y" if a else "n", "Y" if b else "n", "Y" if c else "n"))
        if not g3:
            worst = rel[np.argmax(np.abs(rel - expect))]
            print("      gate 3 worst decay released %.4f against %.4f" % (worst, expect))
        per_size.append(dict(N=n, g=g2 and g3, a=a, b=b, c=c, cv=cv, two=two.mean()))

    gated = [p for p in per_size if p["g"]]
    print("\nSizes passing gates 2 and 3: %s of %s" % ([p["N"] for p in gated], [p["N"] for p in per_size]))
    if len(gated) < len(per_size):
        print("The verdict is over the sizes run; a size failing a gate is reported and not interpreted.")
    if not gated:
        print("No verdict."); return
    if all(p["a"] and p["b"] and p["c"] for p in gated):
        verdict = "TWO-STATE CHANGE"
    elif all(p["cv"] < CONT_CV and p["two"] < CONT_FRAC for p in gated):
        verdict = "CONTINUOUS DEFORMATION"
    else:
        verdict = "INCONCLUSIVE"
    print("\n  PRE-REGISTERED VERDICT, %s, sizes %s:  %s" % (tag, [p["N"] for p in gated], verdict))


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "lam125")

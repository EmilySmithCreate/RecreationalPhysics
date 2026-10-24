"""Scratch (2026-10-23): which stage-1 statistics fall outside the band built from the other size alone, under the
first version's band and under the predictive band of t71_heldout_numbers_v2.py, at alpha 0.01 and 0.00123.
Reads results/t71_{model,layer,layerref}_* only (already read and scored, O144). Writes nothing.

    PYTHONPATH="src;scripts" python3 sandbox/heldout_2026-10-23/t71_heldout_crosscheck_misses.py
"""
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
import t71_heldout_numbers_v2 as V  # noqa: E402


def main():
    reps = V.load()
    cells = sorted({k[:4] for k in reps})
    for label, method, alpha, seed in (("first version, 99 %", "first", None, 20261023),
                                       ("predictive, alpha 0.01", "pred", 0.01, 7),
                                       ("predictive, alpha 0.00123", "pred", 0.10 / 81, 7)):
        rng = np.random.default_rng(seed)
        print("\n" + label)
        n = 0
        for c in cells:
            ms, rel = c[0], c[1]
            r8, r12 = reps[c + (8,)], reps[c + (12,)]
            for q in V.quantities(ms, rel):
                if q == "per_daughter":
                    continue
                if V.is_clean_cell(c) and q != "period":
                    continue
                stat = V.stat_of(q)
                v8 = [x[q] for x in r8 if x[q] is not None]
                v12 = [x[q] for x in r12 if x[q] is not None]
                m8, m12 = float(stat(v8)), float(stat(v12))
                if method == "first":
                    b8, b12 = V.one_sample_band(v8, rng, stat), V.one_sample_band(v12, rng, stat)
                else:
                    b8 = V.band(m8, V.diff_draws(v8, 16, 16, rng, stat), alpha)
                    b12 = V.band(m12, V.diff_draws(v12, 16, 16, rng, stat), alpha)
                n += 2
                if not (b8[0] - 1e-12 <= m12 <= b8[1] + 1e-12):
                    print("  %s/%s %.2f 1/%d %-11s: L = 12's %.4f outside L = 8's band %.4f to %.4f" % (ms, rel, c[2], round(1 / c[3]), q, m12, b8[0], b8[1]))
                if not (b12[0] - 1e-12 <= m8 <= b12[1] + 1e-12):
                    print("  %s/%s %.2f 1/%d %-11s: L = 8's %.4f outside L = 12's band %.4f to %.4f" % (ms, rel, c[2], round(1 / c[3]), q, m8, b12[0], b12[1]))
        print("  checks: %d" % n)


if __name__ == "__main__":
    main()

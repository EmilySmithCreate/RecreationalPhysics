"""Scratch (2026-10-23): the numbers for T71's held-out size L = 16, written from L = 8 and 12 alone (CLAUDE.md rule 14).
Reads results/t71_* only (already read and scored, O144). Writes nothing; prints the table the amendment draft quotes.

    PYTHONPATH="src;scripts" python3 sandbox/heldout_2026-10-23/t71_heldout_numbers.py

Rules, declared before L = 16 exists (ours):

  A. Where no clean switch move fires (arm B, the f1 reference, and the model arm in every cell but lambda = 1.10,
     r = 1/16), the layer-move dynamics do not depend on L: the proposal draws (axis, a width position, split or
     contract) do not involve L, the feed is per point, a payment is drawn in proportion over whole layers, a release
     and the gate scale with L^2. So L = 16 is a fresh sample of the same per-replica distribution as L = 8 and 12.
     The number is the median of the 32 pooled stage-1 replicas; the range is the 0.5th to 99.5th percentile of the
     median of 16 replicas drawn with replacement from those 32 (20,000 resamples, seed 20261023), stretched if needed
     to hold both stage-1 medians.
  B. The first split: t_gate (the first sweep at which a pool of two layers, 2 L^2 points each fed r a sweep, holds
     a N_slab; the same at every L) plus a wait of one coin flip a sweep (a contraction is refused at width 4, so each
     sweep after t_gate splits with probability 1/2). The number and range are the median and the 0.5 % and 99.5 %
     quantiles of the median of 16 such waits (exact law, 10^6 simulated sets of 16); the replica range: the earliest
     at t_gate, the latest at most t_gate + 12.
  C. Exact: the release at the first split is a N_slab in every cell (no clean move can be paid before it: until then
     every store holds exactly r t, so a pool of eight ends holds 8 r t, and 8 r t reaches the 64 of the first clean step
     only after 8 / r sweeps, 76 to 460 sweeps after t_gate); every daughter is a N_slab wherever no clean move fires.
  D. Where clean moves fire (the model arm at lambda = 1.10, r = 1/16) the count of clean-move attempts per sweep is N,
     so L can matter. No form is registered; ours: the number is the line in L through the two stage-1 medians,
     2 m12 - m8; the range runs from m12 (the trend stops) to the line in N_slab at 1,024 points,
     m12 + (m12 - m8) 448 / 320, widened on each side by the half-widths of the 99 % band of 16-medians from the L = 12
     replicas alone, clipped to what the quantity can take. The period, which showed no change, takes rule A.
"""
import csv
import math
import sys
from collections import Counter, defaultdict
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))
import analyse_t71 as A  # noqa: E402

FILES = ["t71_model_lam110", "t71_model_lam125", "t71_model_lam140",
         "t71_layer_lam110", "t71_layer_lam125", "t71_layer_lam140",
         "t71_layerref_lam110", "t71_layerref_lam125", "t71_layerref_lam140"]
NBOOT, SEED = 20000, 20261023
BOUNDS = dict(slab_share=(0, 1), open_share=(0, 1), per_daughter=(0, 1), end_F=(0, None), daughters=(0, None),
              period=(0, None), refolds=(0, None), clean_total=(0, None))


def t_gate(L, r, gate):
    t = math.floor(gate / (2 * L * L * r))
    while 2 * L * L * r * t + 1e-12 < gate:
        t += 1
    return t


def band16(vals, rng, stat=np.median, lo=0.5, hi=99.5):
    v = np.asarray(vals, dtype=float)
    draws = rng.choice(v, size=(NBOOT, 16), replace=True)
    s = stat(draws, axis=1)
    return float(np.percentile(s, lo)), float(np.percentile(s, hi))


def clip(x, q):
    lo, hi = BOUNDS.get(q, (None, None))
    if lo is not None:
        x = max(lo, x)
    if hi is not None:
        x = min(hi, x)
    return x


def per_replica(rows):
    rows = sorted(rows, key=lambda x: int(x["sweep"]))
    x = A.read_replica(rows)
    a_n = x["a_n"]
    r9 = lambda v: None if v is None else round(v, 9)   # noqa: E731  (ratios to 1e-9, so rounding noise is not a change)
    return dict(first_split=x["first_split"], release=r9(x["release"] / a_n if x["release"] is not None else None),
                end_F=r9(x["end_F"] / a_n), refolds=x["refolds"], open_share=x["open_share"],
                slab_share=x["slab_share"], daughters=x["daughters"],
                per_daughter=r9(x["per_daughter"] / a_n if x["per_daughter"] is not None else None),
                period=x["period"], clean_total=int(rows[-1]["n_clean"]), spent_first=x["spent_first"], word=x["word"],
                end_slab=A.width_of(rows[-1]["dims"]) == 4, end_broken=int(rows[-1]["broken"]))


def main():
    rng = np.random.default_rng(SEED)
    # the law of the first split's wait: offsets k >= 0 with P = 2^-(k+1); the median of 16
    sim = np.random.default_rng(SEED + 1).geometric(0.5, size=(1_000_000, 16)) - 1
    med16 = np.median(sim, axis=1)
    g_num, g_lo, g_hi = float(np.median(med16)), float(np.percentile(med16, 0.5)), float(np.percentile(med16, 99.5))
    p_late = 1 - (1 - 2.0 ** -13) ** 16
    print("first-split wait, median of 16 replicas: %.1f sweeps, 99 %% band %.1f to %.1f; P(latest replica >= t_gate + 13) = %.4f per cell; P(no replica at t_gate) = %.1e"
          % (g_num, g_lo, g_hi, p_late, 2.0 ** -16))

    groups = defaultdict(lambda: defaultdict(list))
    for name in FILES:
        for r in csv.DictReader(open(ROOT / "results" / (name + ".csv"), newline="")):
            key = (r["move_set"], r["release_to"], float(r["lam"]), float(r["rate"]), int(r["L"]))
            groups[key][int(r["replica"])].append(r)
    reps = {k: [per_replica(rs) for _, rs in sorted(v.items())] for k, v in groups.items()}
    cells = sorted({k[:4] for k in reps})

    calib_n = calib_out = 0
    n_scored = n_rule_a = 0
    offs = []
    for c in cells:
        ms, rel, lam, rate = c
        r8, r12 = reps[c + (8,)], reps[c + (12,)]
        tg = t_gate(8, rate, 4.0 * (lam - 1.0) * 256)
        assert tg == t_gate(12, rate, 4.0 * (lam - 1.0) * 576) == t_gate(16, rate, 4.0 * (lam - 1.0) * 1024)
        offs += [x["first_split"] - tg for x in r8 + r12]
        clean_cell = ms == "model" and abs(lam - 1.1) < 1e-9 and abs(rate - 0.0625) < 1e-12
        words8, words12 = Counter(x["word"] for x in r8), Counter(x["word"] for x in r12)
        word = words8.most_common(1)[0][0]
        assert word == words12.most_common(1)[0][0]
        print("\n%s / %s, lambda = %.2f, r = 1/%d: word at L = 8, 12: %s, %s -> predicted at L = 16: %s (16 of 16); SPENT FIRST %d, %d -> 0 of 16; a N_slab at L = 16 = %.1f"
              % (ms, rel, lam, round(1 / rate), dict(words8), dict(words12), word,
                 sum(x["spent_first"] for x in r8), sum(x["spent_first"] for x in r12), 4.0 * (lam - 1.0) * 1024))
        fs8 = float(np.median([x["first_split"] for x in r8]))
        fs12 = float(np.median([x["first_split"] for x in r12]))
        print("    first split: t_gate %d; medians %.1f, %.1f (ranges %d-%d, %d-%d) -> %.1f, range %.1f to %.1f; replicas from %d to at most %d   [rule B]"
              % (tg, fs8, fs12, min(x["first_split"] for x in r8), max(x["first_split"] for x in r8),
                 min(x["first_split"] for x in r12), max(x["first_split"] for x in r12),
                 tg + g_num, tg + g_lo, tg + g_hi, tg, tg + 12))
        n_scored += 1
        rel8 = sorted({x["release"] for x in r8}); rel12 = sorted({x["release"] for x in r12})
        print("    release / a N_slab: %s, %s -> 1 exactly (to 1e-9)   [rule C]" % (rel8, rel12))
        qs = ["end_F"] + (["daughters", "per_daughter", "period", "slab_share"] if rel == "daughter" else ["open_share", "refolds"])
        if ms == "model":
            qs.append("clean_total")
        for q in qs:
            stat = np.sum if q == "clean_total" else np.median
            v8 = [x[q] for x in r8 if x[q] is not None]
            v12 = [x[q] for x in r12 if x[q] is not None]
            m8, m12 = float(stat(v8)), float(stat(v12))
            b8, b12 = band16(v8, rng, stat), band16(v12, rng, stat)
            if q == "per_daughter" and not clean_cell:
                print("    %-12s: %.4f, %.4f -> 1 exactly (to 1e-9)   [rule C]" % (q, m8, m12))
                n_scored += 1
                continue
            if clean_cell and q in ("daughters", "per_daughter", "slab_share", "end_F", "clean_total"):
                line_L = 2 * m12 - m8
                line_N = m12 + (m12 - m8) * 448 / 320
                lo = min(m12, line_N) - (m12 - b12[0])
                hi = max(m12, line_N) + (b12[1] - m12)
                print("    %-12s: %.4f, %.4f -> %.4f, range %.4f to %.4f (line in N_slab %.4f; L = 12 band %.4f to %.4f)   [rule D]"
                      % (q, m8, m12, clip(line_L, q), clip(lo, q), clip(hi, q), line_N, b12[0], b12[1]))
                if q in ("per_daughter", "end_F"):
                    a16 = 4.0 * (lam - 1.0) * 1024
                    print("                  in energy at L = 16: %.1f, range %.1f to %.1f (stage 1: %.1f, %.1f)"
                          % (clip(line_L, q) * a16, clip(lo, q) * a16, clip(hi, q) * a16, m8 * 4.0 * (lam - 1.0) * 256, m12 * 4.0 * (lam - 1.0) * 576))
                n_scored += 1
                continue
            pooled = v8 + v12
            num = float(stat(np.asarray(pooled))) if q != "clean_total" else 0.0
            lo, hi = band16(pooled, rng, stat)
            lo, hi = min(lo, m8, m12), max(hi, m8, m12)
            # calibration: between two sizes that share one distribution, how often one size's statistic falls outside
            # the 99 % band built from the other size's replicas alone
            calib_n += 2
            calib_out += int(not (b8[0] <= m12 <= b8[1])) + int(not (b12[0] <= m8 <= b12[1]))
            scored = not (rel == "stores" and q in ("open_share", "refolds"))
            if scored:
                n_scored += 1
                n_rule_a += 1
            extra = ""
            if q == "end_F":
                a16 = 4.0 * (lam - 1.0) * 1024
                extra = "   = %.1f, range %.1f to %.1f in energy at L = 16 (stage 1: %.1f, %.1f)" % (num * a16, lo * a16, hi * a16, m8 * 4.0 * (lam - 1.0) * 256, m12 * 4.0 * (lam - 1.0) * 576)
            print("    %-12s: %.4f, %.4f -> %.4f, range %.4f to %.4f   [rule A%s]%s" % (q, m8, m12, num, lo, hi, "" if scored else ", NOT SCORED: not a registered per-cell reading", extra))
        if clean_cell:
            k8 = sum(1 for x in r8 if x["clean_total"]); k12 = sum(1 for x in r12 if x["clean_total"])
            p = (k8 + k12) / 32
            from math import comb
            cdf = lambda k: sum(comb(16, j) * p ** j * (1 - p) ** (16 - j) for j in range(0, k + 1))  # noqa: E731
            print("    replicas with a clean move: %d, %d of 16; pooled share %.3f; P(8 or fewer of 16) = %.4f at that share -> a majority (9 or more of 16)"
                  % (k8, k12, p, cdf(8)))
            print("    end broken points: L = 8 %s; L = 12 %s" % (dict(Counter(x["end_broken"] for x in r8)), dict(Counter(x["end_broken"] for x in r12))))
        else:
            if ms == "model":
                print("    clean moves: 0 in all 32 stage-1 replicas -> 0 at L = 16 (empirical)")
    h = Counter(offs)
    print("\nfirst split minus t_gate over all %d stage-1 replicas, against 576 x 2^-(k+1): %s"
          % (len(offs), ", ".join("%d: %d (%.1f)" % (k, h[k], len(offs) * 2.0 ** -(k + 1)) for k in range(max(h) + 1))))
    print("calibration (rule A's band, between L = 8 and 12): %d of %d stage-1 statistics fall outside the band built from the other size alone (%.1f %%)"
          % (calib_out, calib_n, 100.0 * calib_out / calib_n))
    print("numbers scored in the arm cells at L = 16 (words, release and SPENT FIRST excluded): %d, of which rule A %d"
          % (n_scored, n_rule_a))
    print("expected chance misses among the rule-A numbers if nothing depends on L: %.1f (at the nominal 1 %%) to %.1f (at the stage-1 rate)"
          % (0.01 * n_rule_a, n_rule_a * calib_out / calib_n))
    print("expected chance misses among the 18 rule-B medians and replica ranges: %.2f" % (18 * (0.01 + p_late + 2.0 ** -16)))
    # rule C's margin: a pool of eight ends holds 8 r t before the first split, so the first clean step's 64 needs t = 8 / r
    margins = []
    for lam in (1.10, 1.25, 1.40):
        for rate in (1 / 64, 1 / 16):
            tg = t_gate(16, rate, 4.0 * (lam - 1.0) * 1024)
            margins.append((lam, round(1 / rate), int(round(8 / rate)) - tg))
    print("rule C: sweeps between t_gate and t = 8 / r, per (lambda, 1/r): %s; smallest %d, largest %d"
          % (margins, min(m[2] for m in margins), max(m[2] for m in margins)))
    # the control as configured (T68's runner, mode "all"): the rate is the total per sweep, shared by N points
    print("\ncontrol at L = 16 as configured: last record = (n_sweeps // 50) * 50; fed = r x last record, shared by 1,024 points")
    for lam, n_sweeps in ((1.10, 2000), (1.25, 2560), (1.40, 4096)):
        last = (n_sweeps // 50) * 50
        for rate in (1 / 64, 1 / 16):
            fed = rate * last
            print("  lambda = %.2f, r = 1/%d: median stop %d, median fed %.2f, per point %.4f at N = 1,024 (%.4f at 256, %.4f at 576)"
                  % (lam, round(1 / rate), last, fed, fed / 1024, fed / 256, fed / 576))
    per_pt = [n * r for n, r in ((2000, 1 / 64), (2000, 1 / 16), (2560, 1 / 64), (2000, 1 / 16), (4096, 1 / 64), (2000, 1 / 16))]
    print("  the layer-feed arms, for comparison: r to every point every sweep, %.2f to %.2f per point over the run"
          % (min(per_pt), max(per_pt)))


if __name__ == "__main__":
    main()

"""Scratch (2026-10-23, sandbox; not a registered reader): T74's held-out ranges rebuilt after the check of the draft
amendment, with the fit's own sampling error counted (a two-level draw). Usage:

    python sandbox/heldout_2026-10-23/t74_heldout_twolevel_2026-10-23.py > sandbox/out/t74_heldout_twolevel_2026-10-23.txt

Reads the per-replica cache sandbox/out/t74_stage1_replicas_2026-10-23.json (written by
t74_heldout_resample_2026-10-23.py from the 108 stage-1 files by name) and, for the clean-switch count only, the 18
stage-1 files results/t74_lam110_L{08,12}_*_c2R_*.csv by name. Opens nothing else in results/.

Two-level draw (ours): in each draw, a fresh "stage 1" is drawn with replacement from the stage-1 replicas (as many as
stage 1 had), and a fresh "L = 16" is drawn from the same replicas (as many as L = 16 will have). The range is the
observed stage-1 value plus the central 99.7 % of (fresh L = 16 value - fresh stage-1 value). For a word, the fresh
L = 16 replicas are drawn from the fresh stage 1 (so the rate itself varies from draw to draw).
"""
import csv
import json
import math
import sys
from collections import Counter, defaultdict
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "scripts"))
import analyse_t74 as A  # noqa: E402

LAMS = ("1.10", "1.25", "1.40")
FEEDS = ("steady", "meals16", "meals256")
CAPS = ("c2R", "cRhalf")
BGS = ("cold", "equal", "warm")
CACHE = Path("sandbox/out/t74_stage1_replicas_2026-10-23.json")
D = 10000
LO, HI = 0.15, 99.85


def stats(sample):
    return np.array([[len(x["periods"]), sum(x["periods"]), sum(p * p for p in x["periods"])] for x in sample],
                    dtype=float)


def pmean(st):
    t = st.sum(axis=0)
    return t[1] / t[0]


def pcv(st):
    t = st.sum(axis=0)
    m = t[1] / t[0]
    return math.sqrt(max(t[2] / t[0] - m * m, 0.0)) / m


def draws(st, k, rng, n):
    """Pooled mean and cv of k rows drawn with replacement from st, n times."""
    tot = st[rng.integers(0, len(st), (n, k))].sum(axis=1)
    m = tot[:, 1] / tot[:, 0]
    return m, np.sqrt(np.maximum(tot[:, 2] / tot[:, 0] - m * m, 0.0)) / m


def timing_word(r, c):
    if abs(r - 1) > A.TIMING_TOL:
        return "DIFFERENT TIMING"
    return "SPREAD ONLY" if c >= A.SPREAD_FACTOR else "SAME TIMING"


def fed_ok(x):
    return x["fed_daughters"] >= 1 and x["exact"]


def unfed_word(sample, bg):
    n = len(sample)
    w, _ = A.unfed_word(sum(x["waits"] for x in sample), sum(x["dissolves"] for x in sample),
                        sum(x["fed_by_surroundings"] for x in sample), n)
    return w, A.predicted(bg, sample)


def main():
    reps = json.loads(CACHE.read_text())
    rng = np.random.default_rng(20261023)
    rng_check = np.random.default_rng(4243)

    def get(lam, L, feed, cap, bg):
        return reps["%s|%d|%s|%s|%s" % (lam, L, feed, cap, bg)]

    def pool(lam, feed, cap, sizes=(8, 12)):
        return [x for L in sizes for bg in BGS for x in get(lam, L, feed, cap, bg)]

    # ---------------- periods ----------------
    print("== 1. Period, L = 16: one-level (draft) and two-level ranges; miss rates under the claim ==")
    print("lam  cap    feed     | fit     | one-level range     | two-level range     | width ratio | "
          "max dist from fit %% (two-level) | miss rate of one-level range | of two-level range")
    miss1, miss2 = [], []
    for lam in LAMS:
        for cap in CAPS:
            for feed in FEEDS:
                st = stats(pool(lam, feed, cap))
                fit = pmean(st)
                b48, _ = draws(st, 48, rng, D)
                lo1, hi1 = np.percentile(b48, [LO, HI])
                f96, _ = draws(st, 96, rng, D)
                n48, _ = draws(st, 48, rng, D)
                d = n48 - f96
                dlo, dhi = np.percentile(d, [LO, HI])
                lo2, hi2 = fit + dlo, fit + dhi
                # miss rates under the claim, from an independent two-level draw (40,000)
                cf, _ = draws(st, 96, rng_check, 40000)
                cn, _ = draws(st, 48, rng_check, 40000)
                cd = cn - cf
                m1 = float(((cd < lo1 - fit) | (cd > hi1 - fit)).mean())
                m2 = float(((cd < dlo) | (cd > dhi)).mean())
                miss1.append(m1)
                miss2.append(m2)
                print("%s %-6s %-8s | %.3f | %.3f to %.3f | %.3f to %.3f | %.2f | %.2f | %.4f | %.4f" % (
                    lam, cap, feed, fit, lo1, hi1, lo2, hi2, (hi2 - lo2) / (hi1 - lo1),
                    100 * max(fit - lo2, hi2 - fit) / fit, m1, m2))
    print("P(at least one of 18 misses | claim true): one-level ranges %.3f; two-level ranges %.3f; "
          "1 - 0.997^18 = %.3f" % (1 - np.prod(1 - np.array(miss1)), 1 - np.prod(1 - np.array(miss2)),
                                   1 - 0.997 ** 18))

    # ---------------- back-test ----------------
    print()
    print("== 2. Back-test: rule fitted on L = 8 alone (48 replicas), against L = 12's value ==")
    in1 = in2 = 0
    cov_old = []
    for lam in LAMS:
        for cap in CAPS:
            for feed in FEEDS:
                st8 = stats(pool(lam, feed, cap, (8,)))
                st12 = stats(pool(lam, feed, cap, (12,)))
                fit8, v12 = pmean(st8), pmean(st12)
                b, _ = draws(st8, 48, rng, D)
                lo1, hi1 = np.percentile(b, [LO, HI])
                f, _ = draws(st8, 48, rng, D)
                n, _ = draws(st8, 48, rng, D)
                dlo, dhi = np.percentile(n - f, [LO, HI])
                ok1 = lo1 <= v12 <= hi1
                ok2 = fit8 + dlo <= v12 <= fit8 + dhi
                in1 += ok1
                in2 += ok2
                # coverage of the one-level rule when a fit of 48 predicts 48 (pooled 96 as the population;
                # the rule's half-widths taken from the pooled 96)
                st = stats(pool(lam, feed, cap))
                fitp = pmean(st)
                bb, _ = draws(st, 48, rng_check, 40000)
                hlo, hhi = np.percentile(bb, [LO, HI])
                ff, _ = draws(st, 48, rng_check, 40000)
                nn, _ = draws(st, 48, rng_check, 40000)
                dd = nn - ff
                cov_old.append(float(((dd >= hlo - fitp) & (dd <= hhi - fitp)).mean()))
                print("%s %-6s %-8s | one-level %.3f to %.3f %s | two-level %.3f to %.3f %s | L=12 %.3f | "
                      "one-level coverage for 48 -> 48: %.4f" % (lam, cap, feed, lo1, hi1, "in" if ok1 else "OUT",
                                                                fit8 + dlo, fit8 + dhi, "in" if ok2 else "OUT", v12,
                                                                cov_old[-1]))
    print("one-level rule: %d of 18 inside; two-level rule: %d of 18 inside" % (in1, in2))
    print("one-level rule, 48 -> 48: mean coverage %.4f; P(18 of 18 inside) %.3f; normal approximation "
          "P(|Z| < 2.968/sqrt 2) = %.4f, ^18 = %.3f" % (
              np.mean(cov_old), np.prod(cov_old), math.erf(2.968 / 2), math.erf(2.968 / 2) ** 18))

    # ---------------- timing ----------------
    print()
    print("== 3. Timing, L = 16, two-level: ratios and words ==")
    for lam in LAMS:
        for cap in CAPS:
            sts = stats(pool(lam, "steady", cap))
            for feed in ("meals16", "meals256"):
                stm = stats(pool(lam, feed, cap))
                r0 = pmean(stm) / pmean(sts)
                c0 = pcv(stm) / pcv(sts)
                fm, fmc = draws(stm, 96, rng, D)
                fs, fsc = draws(sts, 96, rng, D)
                nm, nmc = draws(stm, 48, rng, D)
                ns, nsc = draws(sts, 48, rng, D)
                r = r0 + (nm / ns - fm / fs)
                c = c0 + (nmc / nsc - fmc / fsc)
                words = Counter(timing_word(a, b) for a, b in zip(r, c))
                rlo, rhi = np.percentile(r, [LO, HI])
                clo, chi = np.percentile(c, [LO, HI])
                print("%s %-6s %-8s | mean ratio %.5f (%.5f to %.5f) | cv ratio %.4f (%.4f to %.4f) | %s" % (
                    lam, cap, feed, r0, rlo, rhi, c0, clo, chi,
                    ", ".join("%s %.4f" % (w, k / D) for w, k in words.most_common())))

    # ---------------- fed word ----------------
    print()
    print("== 4. Fed word, L = 16, two-level (fresh 96 per (lam, feed, cap), then 16 per cell from it) ==")
    short = {}
    for lam in LAMS:
        for feed in FEEDS:
            for cap in CAPS:
                p = pool(lam, feed, cap)
                short[(lam, feed, cap)] = sum(not fed_ok(x) for x in p)
    certain = [k for k, s in short.items() if s == 0]
    print("settings with no short replica in 96: %d of 18 -> %d cells BURPS in every draw" % (len(certain),
                                                                                         3 * len(certain)))
    unc = [k for k, s in short.items() if s > 0]
    for k in unc:
        print("short replicas %s: %d of 96" % (k, short[k]))
    counts = []
    pb = Counter()
    for _ in range(D):
        n_b = 0
        for k in unc:
            p = pool(*k)
            ok = np.array([fed_ok(x) for x in p])
            stage = ok[rng.integers(0, len(ok), 96)]
            for bg in BGS:
                w = bool(stage[rng.integers(0, 96, 16)].all())
                pb[(k, bg)] += w
                n_b += w
        counts.append(n_b)
    for k in unc:
        print("%s: P(BURPS) two-level %s" % (k, ", ".join("%s %.3f" % (bg, pb[(k, bg)] / D) for bg in BGS)))
    print("BURPS among the six uncertain cells: median %d, 99.7%% range %d to %d; distribution %s" % (
        int(np.median(counts)), int(np.percentile(counts, LO)), int(np.percentile(counts, HI)),
        dict(sorted(Counter(counts).items()))))

    # ---------------- unfed words ----------------
    print()
    print("== 5. Unfed words, L = 16, two-level (fresh 32 per cell, then 16 from it) ==")
    per_cell = defaultdict(Counter)
    tallies = defaultdict(list)
    for _ in range(D):
        t = Counter()
        for lam in LAMS:
            for feed in FEEDS:
                for cap in CAPS:
                    for bg in BGS:
                        p = get(lam, 8, feed, cap, bg) + get(lam, 12, feed, cap, bg)
                        stage = [p[i] for i in rng.integers(0, len(p), len(p))]
                        s16 = [stage[i] for i in rng.integers(0, len(stage), 16)]
                        w, pred = unfed_word(s16, bg)
                        per_cell[(lam, feed, cap, bg)][w] += 1
                        short_w = "MIXED" if w.startswith("MIXED") else w
                        t[(bg, short_w)] += 1
                        if bg == "equal" and not pred.startswith("SPLIT"):
                            t[("equal", "scored")] += 1
                            t[("equal", "holds")] += (pred == w)
        for key in (("cold", "DISSOLVES"), ("warm", "FED BY ITS SURROUNDINGS"), ("equal", "scored"),
                    ("equal", "WAITS"), ("equal", "MIXED"), ("equal", "FED BY ITS SURROUNDINGS"),
                    ("equal", "holds")):
            tallies[key].append(t[key])
    for key, vals in tallies.items():
        print("%-5s %-26s median %d, 99.7%% range %d to %d" % (key[0], key[1], int(np.median(vals)),
                                                            int(np.percentile(vals, LO)),
                                                            int(np.percentile(vals, HI))))
    rows = []
    for lam in LAMS:
        for feed in FEEDS:
            for cap in CAPS:
                for bg in BGS:
                    w8 = unfed_word(get(lam, 8, feed, cap, bg), bg)[0]
                    w12 = unfed_word(get(lam, 12, feed, cap, bg), bg)[0]
                    c = per_cell[(lam, feed, cap, bg)]
                    (wm, nm), = c.most_common(1)
                    p_stage = c[w8] / D if w8 == w12 else None
                    rows.append((lam, feed, cap, bg, w8, w12, wm, nm / D, p_stage))
    print("cells where the two stage-1 words differ or the modal share (two-level) is below 0.997:")
    for r in rows:
        if r[4] != r[5] or r[7] < 0.997:
            print("  %s %-8s %-6s %-5s | L8 %s | L12 %s | modal %s %.3f | P(stage word) %s" % (
                r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7], "%.3f" % r[8] if r[8] is not None else "-"))
    agree = [r for r in rows if r[4] == r[5]]
    print("cells with the same word at both stage-1 sizes: %d of 54" % len(agree))
    for thr in (0.90, 0.93, 0.997):
        must = [r for r in agree if r[8] >= thr]
        rest = [r for r in rows if r not in must]
        print("rule 'must repeat if P(stage word) >= %.3f': %d cells must repeat; P(all repeat | claim) %.3f; "
              "%d cells left over" % (thr, len(must), float(np.prod([r[8] for r in must])), len(rest)))


def clean_switches():
    print()
    print("== 6. Clean switch moves in the fed phase, lam 1.10, c = 2R (stage-1 files by name) ==")
    for L in (8, 12):
        reps_with, moves, short = 0, 0, 0
        for feed in FEEDS:
            for bg in BGS:
                p = Path("results") / ("t74_lam110_L%02d_%s_c2R_%s.csv" % (L, feed, bg))
                last = {}
                with open(p, newline="") as fh:
                    for r in csv.DictReader(fh):
                        if int(r["sweep"]) <= int(r["n_fed"]):
                            rep = int(r["replica"])
                            s = int(r["sweep"])
                            if rep not in last or s >= last[rep][0]:
                                last[rep] = (s, int(r["n_clean"]))
                for rep, (_, n) in last.items():
                    reps_with += n > 0
                    moves += n
        print("L = %d: replicas with a clean switch in the fed phase %d of 144, moves %d" % (L, reps_with, moves))
    p = 256 / (256 + 576)
    tail = sum(math.comb(8, k) * p ** k * (1 - p) ** (8 - k) for k in range(4, 9))
    exact = math.comb(8, 4) * p ** 4 * (1 - p) ** 4
    print("8 short replicas split by points (256 : 576): P(4 at L = 8) %.3f; P(at least 4 at L = 8) %.3f" % (exact,
                                                                                                         tail))


if __name__ == "__main__":
    main()
    if "--no-csv" not in sys.argv[1:]:
        clean_switches()

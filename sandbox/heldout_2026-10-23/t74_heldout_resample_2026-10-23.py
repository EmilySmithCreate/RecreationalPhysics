"""Scratch (2026-10-23, sandbox; not a registered reader): the numbers and ranges for T74's held-out size L = 16, from
the stage-1 results at L = 8 and 12 only. Usage:

    python sandbox/heldout_2026-10-23/t74_heldout_resample_2026-10-23.py > sandbox/out/t74_heldout_resample_2026-10-23.txt

Reads the 108 stage-1 files results/t74_lam{110,125,140}_L{08,12}_*.csv by name (read and scored on 21 October, O145),
with `scripts/analyse_t74.py`'s own `read_replica`, and caches the per-replica reads in
sandbox/out/t74_stage1_replicas_2026-10-23.json (rerun with --cached to skip the CSVs). Opens nothing else in results/.

The fit (ours; T74 names no fitted form): every size claim of T74 says a quantity or a word is the same at every L, so
the fit is a constant, the two stage-1 sizes pooled. The range is what L = 16 would show if that claim holds: L = 16
drawn as fresh replicas from the stage-1 population, 10,000 resamples (numpy seed 20261023), and the central 99.7 %
of the draws (0.15 % to 99.85 %), wide enough that 18 settings read at once miss by chance about one time in twenty.

* period: per (lambda, cap, feed), 48 replicas drawn from the 96 of stage 1 (3 backgrounds x 2 sizes; the reservoir is
  isolated while fed, so the background does not touch the fed phase, as the analyzer's timing pooling says), the
  pooled mean of their fed-phase intervals;
* timing: per (lambda, cap, meals), 48 meals and 48 steady replicas drawn the same way, the analyzer's mean ratio,
  cv ratio and word;
* fed word: per cell, 16 replicas drawn from the 96 of its (lambda, feed, cap) (fed phase and digestion are isolated
  from the background), the analyzer's BURPS / NEVER BURPS / MIXED;
* unfed word: per cell, 16 replicas drawn from the 32 of the same (lambda, feed, cap, background) at L = 8 and 12, the
  analyzer's word and, for the equal background, its SPLIT rule and the shared prediction.
"""
import csv
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "scripts"))
import analyse_t74 as A  # noqa: E402

LAMS = ((1.10, 110), (1.25, 125), (1.40, 140))
SIZES = (8, 12)
FEEDS = ("steady", "meals16", "meals256")
CAPS = ("c2R", "cRhalf")
BGS = ("cold", "equal", "warm")
CACHE = Path("sandbox/out/t74_stage1_replicas_2026-10-23.json")
DRAWS = 10000
LO, HI = 0.15, 99.85
KEEP = ("periods", "fed_daughters", "exact", "waits", "dissolves", "fed_by_surroundings", "common_above_2a")


def load(cached):
    if cached and CACHE.exists():
        return json.loads(CACHE.read_text())
    reps = {}
    for lam, tag in LAMS:
        for L in SIZES:
            for feed in FEEDS:
                for cap in CAPS:
                    for bg in BGS:
                        p = Path("results") / ("t74_lam%d_L%02d_%s_%s_%s.csv" % (tag, L, feed, cap, bg))
                        by_rep = defaultdict(list)
                        for r in csv.DictReader(open(p, newline="")):
                            by_rep[int(r["replica"])].append(r)
                        reads = []
                        for _, rs in sorted(by_rep.items()):
                            x = A.read_replica(rs)
                            reads.append({k: ([int(v) for v in x[k]] if k == "periods" else x[k]) for k in KEEP})
                        reps["%.2f|%d|%s|%s|%s" % (lam, L, feed, cap, bg)] = reads
                        sys.stderr.write("read %s\n" % p.name)
    CACHE.write_text(json.dumps(reps))
    return reps


def stats(sample):
    """Per replica: the count, sum and sum of squares of its fed-phase intervals (so a pooled mean and a pooled
    population standard deviation over any set of replicas follow exactly, as the analyzer pools them)."""
    return np.array([[len(x["periods"]), sum(x["periods"]), sum(p * p for p in x["periods"])] for x in sample],
                    dtype=float)


def pooled_mean(sample):
    n, s, _ = stats(sample).sum(axis=0)
    return s / n if n else float("nan")


def pooled_cv(sample):
    n, s, ss = stats(sample).sum(axis=0)
    if not n:
        return float("nan")
    m = s / n
    return float(np.sqrt(max(ss / n - m * m, 0.0)) / m)


def boot(st, k, rng, draws):
    """Pooled mean and cv of k replicas drawn with replacement from the rows of st, `draws` times."""
    idx = rng.integers(0, len(st), (draws, k))
    tot = st[idx].sum(axis=1)
    m = tot[:, 1] / tot[:, 0]
    sd = np.sqrt(np.maximum(tot[:, 2] / tot[:, 0] - m * m, 0.0))
    return m, sd / m


def fed_word(sample):
    if all(x["fed_daughters"] >= 1 and x["exact"] for x in sample):
        return "BURPS"
    if all(x["fed_daughters"] == 0 for x in sample):
        return "NEVER BURPS"
    return "MIXED"


def unfed(sample, bg):
    n = len(sample)
    word, _ = A.unfed_word(sum(x["waits"] for x in sample), sum(x["dissolves"] for x in sample),
                           sum(x["fed_by_surroundings"] for x in sample), n)
    pred = A.predicted(bg, sample)
    return word, pred


def q(vals):
    return float(np.percentile(vals, LO)), float(np.percentile(vals, HI))


def main(cached):
    reps = load(cached)
    rng = np.random.default_rng(20261023)

    def get(lam, L, feed, cap, bg):
        return reps["%.2f|%d|%s|%s|%s" % (lam, L, feed, cap, bg)]

    def fed_pool(lam, feed, cap):
        return [x for L in SIZES for bg in BGS for x in get(lam, L, feed, cap, bg)]

    def draw(pool, k):
        idx = rng.integers(0, len(pool), k)
        return [pool[i] for i in idx]

    print("== Period between fed-phase births, L = 16 (48 replicas, backgrounds pooled) ==")
    print("lam   cap    feed     | L=8      L=12     | pooled (fit) | 99.7%% range        | half-width %% | exact a N/min(c,R)")
    for lam, _ in LAMS:
        a = 4 * (lam - 1)
        for cap in CAPS:
            exact = (16 if cap == "c2R" else 32) * a
            for feed in FEEDS:
                pool = fed_pool(lam, feed, cap)
                m8 = pooled_mean([x for bg in BGS for x in get(lam, 8, feed, cap, bg)])
                m12 = pooled_mean([x for bg in BGS for x in get(lam, 12, feed, cap, bg)])
                fit = pooled_mean(pool)
                bs, _cv = boot(stats(pool), 48, rng, DRAWS)
                lo, hi = q(bs)
                print("%.2f  %-6s %-8s | %7.3f  %7.3f  | %7.3f      | %7.3f to %7.3f | %.2f | %6.2f"
                      % (lam, cap, feed, m8, m12, fit, lo, hi, 100 * max(fit - lo, hi - fit) / fit, exact))

    print()
    print("== Timing, meals against steady, L = 16 (48 + 48 replicas) ==")
    print("lam   cap    meals    | L=8 word, mean r, cv r | L=12 word, mean r, cv r | pooled mean r, cv r | "
          "99.7%% mean r | 99.7%% cv r | P(word) over draws")
    stage = {k: v for k, v in A.timing(cells_for_timing(reps)).items()}
    for lam, _ in LAMS:
        for cap in CAPS:
            st = fed_pool(lam, "steady", cap)
            for feed in ("meals16", "meals256"):
                me = fed_pool(lam, feed, cap)
                mr = pooled_mean(me) / pooled_mean(st)
                cr = pooled_cv(me) / pooled_cv(st)
                mm, mc = boot(stats(me), 48, rng, DRAWS)
                sm, sc = boot(stats(st), 48, rng, DRAWS)
                rs, cs = mm / sm, mc / sc
                words = Counter()
                for r, c in zip(rs, cs):
                    words["DIFFERENT TIMING" if abs(r - 1) > A.TIMING_TOL else
                          ("SPREAD ONLY" if c >= A.SPREAD_FACTOR else "SAME TIMING")] += 1
                w8, r8, c8 = stage[(lam, 8, cap, feed)]
                w12, r12, c12 = stage[(lam, 12, cap, feed)]
                rlo, rhi = q(rs)
                clo, chi = q(cs)
                print("%.2f  %-6s %-8s | %-11s %.4f %.3f | %-11s %.4f %.3f | %.4f %.3f | %.4f to %.4f | %.3f to %.3f | %s"
                      % (lam, cap, feed, w8, r8, c8, w12, r12, c12, mr, cr, rlo, rhi, clo, chi,
                         ", ".join("%s %.4f" % (w, n / DRAWS) for w, n in words.most_common())))

    print()
    print("== Fed word per cell at L = 16 (16 replicas drawn from the 96 of the cell's lambda, feed, cap) ==")
    burps_counts = []
    per_cell_fed = {}
    pools = {(lam, feed, cap): fed_pool(lam, feed, cap) for lam, _ in LAMS for feed in FEEDS for cap in CAPS}
    for lam, _ in LAMS:
        for feed in FEEDS:
            for cap in CAPS:
                pool = pools[(lam, feed, cap)]
                short = sum(1 for x in pool if not (x["fed_daughters"] >= 1 and x["exact"]))
                per_cell_fed[(lam, feed, cap)] = short
    draws_fed = defaultdict(Counter)
    for _ in range(DRAWS):
        n_burps = 0
        for (lam, feed, cap), pool in pools.items():
            for bg in BGS:
                w = fed_word(draw(pool, 16))
                draws_fed[(lam, feed, cap, bg)][w] += 1
                n_burps += (w == "BURPS")
        burps_counts.append(n_burps)
    for (lam, feed, cap), short in sorted(per_cell_fed.items()):
        if short:
            ps = ["%s: P(BURPS) %.3f" % (bg, draws_fed[(lam, feed, cap, bg)]["BURPS"] / DRAWS) for bg in BGS]
            print("%.2f %-8s %-6s replicas without an exact fed daughter: %d of 96 | %s" % (lam, feed, cap, short,
                                                                                            "; ".join(ps)))
    others = [k for k, s in per_cell_fed.items() if s == 0]
    print("(lambda, feed, cap) settings with every one of 96 replicas exact: %d of 18" % len(others))
    lo, hi = np.percentile(burps_counts, LO), np.percentile(burps_counts, HI)
    print("BURPS cells of 54: stage 1 L=8 %d, L=12 %d | L = 16 median %d, 99.7%% range %d to %d" % (
        stage_fed_count(reps, 8), stage_fed_count(reps, 12), int(np.median(burps_counts)), int(lo), int(hi)))

    print()
    print("== Unfed words per cell at L = 16 (16 replicas drawn from the cell's 32 at L = 8 and 12) ==")
    tallies = defaultdict(list)
    per_cell = defaultdict(Counter)
    per_cell_pred = defaultdict(Counter)
    for _ in range(DRAWS):
        t = Counter()
        for lam, _t in LAMS:
            for feed in FEEDS:
                for cap in CAPS:
                    for bg in BGS:
                        pool = get(lam, 8, feed, cap, bg) + get(lam, 12, feed, cap, bg)
                        word, pred = unfed(draw(pool, 16), bg)
                        short = "MIXED" if word.startswith("MIXED") else word
                        per_cell[(lam, feed, cap, bg)][word] += 1
                        t[(bg, short)] += 1
                        if bg == "equal":
                            split = pred.startswith("SPLIT")
                            per_cell_pred[(lam, feed, cap)]["SPLIT" if split else pred] += 1
                            if not split:
                                t[("equal", "scored")] += 1
                                t[("equal", "scored " + short)] += 1
                                t[("equal", "holds")] += (pred == word)
        for key in (("cold", "DISSOLVES"), ("cold", "MIXED"), ("warm", "FED BY ITS SURROUNDINGS"), ("warm", "MIXED"),
                    ("equal", "scored"), ("equal", "scored WAITS"), ("equal", "scored MIXED"),
                    ("equal", "scored FED BY ITS SURROUNDINGS"), ("equal", "holds"), ("equal", "WAITS"),
                    ("equal", "MIXED"), ("equal", "FED BY ITS SURROUNDINGS")):
            tallies[key].append(t[key])
    for key, vals in tallies.items():
        print("%-5s %-32s of 18: median %d, 99.7%% range %d to %d" % (key[0], key[1], int(np.median(vals)),
                                                                    int(np.percentile(vals, LO)),
                                                                    int(np.percentile(vals, HI))))
    print()
    print("Per cell (modal word at L = 16 and its share of draws; stage-1 words at L = 8 and 12):")
    for lam, _t in LAMS:
        for feed in FEEDS:
            for cap in CAPS:
                for bg in BGS:
                    c = per_cell[(lam, feed, cap, bg)]
                    (w, n), = c.most_common(1)
                    s8 = stage_unfed_word(get(lam, 8, feed, cap, bg), bg)
                    s12 = stage_unfed_word(get(lam, 12, feed, cap, bg), bg)
                    extra = ""
                    if bg == "equal":
                        pc = per_cell_pred[(lam, feed, cap)]
                        extra = " | equal rule: " + ", ".join("%s %.3f" % (k, v / DRAWS) for k, v in pc.most_common())
                    print("%.2f %-8s %-6s %-5s | L16 %-55s %.3f | L8 %-55s | L12 %-55s%s"
                          % (lam, feed, cap, bg, w, n / DRAWS, s8, s12, extra))


def stage_unfed_word(sample, bg):
    return unfed(sample, bg)[0]


def stage_fed_count(reps, L):
    n = 0
    for key, sample in reps.items():
        lam, size, feed, cap, bg = key.split("|")
        if int(size) == L:
            n += fed_word(sample) == "BURPS"
    return n


def cells_for_timing(reps):
    cells = {}
    for key, sample in reps.items():
        lam, size, feed, cap, bg = key.split("|")
        cells[(float(lam), int(size), feed, cap, bg)] = {"periods": [p for x in sample for p in x["periods"]]}
    return cells


if __name__ == "__main__":
    main("--cached" in sys.argv[1:])

"""Scratch (2026-10-23, sandbox): a back-test of the range rule proposed for T74's held-out size. The same rule, fitted
on L = 8 alone, predicts L = 12; how many of L = 12's numbers fall inside? Both sizes were read on 21 October (O145), so
this is a check of the rule, not a prediction. Usage (after t74_heldout_resample_2026-10-23.py has written its cache):

    python sandbox/heldout_2026-10-23/t74_heldout_backtest_2026-10-23.py > sandbox/out/t74_heldout_backtest_2026-10-23.txt
"""
import json
import sys
from collections import Counter
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "scripts"))
sys.path.insert(0, str(Path(__file__).resolve().parent))
import analyse_t74 as A  # noqa: E402
import importlib.util  # noqa: E402
_spec = importlib.util.spec_from_file_location(
    "t74_resample", Path(__file__).resolve().parent / "t74_heldout_resample_2026-10-23.py")
_m = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_m)
boot, fed_word, pooled_cv, pooled_mean, stats, unfed = (_m.boot, _m.fed_word, _m.pooled_cv, _m.pooled_mean,
                                                        _m.stats, _m.unfed)

LAMS = (1.10, 1.25, 1.40)
FEEDS = ("steady", "meals16", "meals256")
CAPS = ("c2R", "cRhalf")
BGS = ("cold", "equal", "warm")
DRAWS = 10000
LO, HI = 0.15, 99.85


def main():
    reps = json.loads(Path("sandbox/out/t74_stage1_replicas_2026-10-23.json").read_text())
    rng = np.random.default_rng(20261023)

    def get(lam, L, feed, cap, bg):
        return reps["%.2f|%d|%s|%s|%s" % (lam, L, feed, cap, bg)]

    def pool(lam, L, feed, cap):
        return [x for bg in BGS for x in get(lam, L, feed, cap, bg)]

    inside = 0
    print("Period: range from L = 8 alone (48 drawn from its 48), against L = 12's value")
    for lam in LAMS:
        for cap in CAPS:
            for feed in FEEDS:
                p8, p12 = pool(lam, 8, feed, cap), pool(lam, 12, feed, cap)
                bs, _ = boot(stats(p8), 48, rng, DRAWS)
                lo, hi = np.percentile(bs, LO), np.percentile(bs, HI)
                v = pooled_mean(p12)
                ok = lo <= v <= hi
                inside += ok
                print("%.2f %-6s %-8s | %.3f to %.3f | L=12 %.3f %s" % (lam, cap, feed, lo, hi, v, "in" if ok else "OUT"))
    print("period: %d of 18 inside" % inside)

    print()
    print("Timing words: L = 8's word against L = 12's, with the share of draws giving L = 8's word")
    same = 0
    for lam in LAMS:
        for cap in CAPS:
            st8, st12 = pool(lam, 8, "steady", cap), pool(lam, 12, "steady", cap)
            for feed in ("meals16", "meals256"):
                me8, me12 = pool(lam, 8, feed, cap), pool(lam, 12, feed, cap)
                mm, mc = boot(stats(me8), 48, rng, DRAWS)
                sm, sc = boot(stats(st8), 48, rng, DRAWS)
                words = Counter("DIFFERENT TIMING" if abs(r - 1) > A.TIMING_TOL else
                                ("SPREAD ONLY" if c >= A.SPREAD_FACTOR else "SAME TIMING")
                                for r, c in zip(mm / sm, mc / sc))
                r12 = pooled_mean(me12) / pooled_mean(st12)
                c12 = pooled_cv(me12) / pooled_cv(st12)
                w12 = ("DIFFERENT TIMING" if abs(r12 - 1) > A.TIMING_TOL else
                       ("SPREAD ONLY" if c12 >= A.SPREAD_FACTOR else "SAME TIMING"))
                (w, n), = words.most_common(1)
                same += (w == w12)
                print("%.2f %-6s %-8s | from L=8: %s %.4f | L=12: %s" % (lam, cap, feed, w, n / DRAWS, w12))
    print("timing: %d of 12 match" % same)

    print()
    print("Counts of cells (fed word of 54; unfed words of 18): range from L = 8 alone against L = 12's count")
    tallies = {k: [] for k in ("BURPS", "cold DISSOLVES", "warm FED BY ITS SURROUNDINGS", "equal scored",
                               "equal WAITS", "equal MIXED", "equal FED BY ITS SURROUNDINGS")}
    for _ in range(DRAWS):
        t = Counter()
        for lam in LAMS:
            for feed in FEEDS:
                for cap in CAPS:
                    fp = pool(lam, 8, feed, cap)
                    for bg in BGS:
                        idx = rng.integers(0, len(fp), 16)
                        t["BURPS"] += fed_word([fp[i] for i in idx]) == "BURPS"
                        up = get(lam, 8, feed, cap, bg)
                        idx = rng.integers(0, len(up), 16)
                        word, pred = unfed([up[i] for i in idx], bg)
                        short = "MIXED" if word.startswith("MIXED") else word
                        t["%s %s" % (bg, short)] += 1
                        if bg == "equal" and not pred.startswith("SPLIT"):
                            t["equal scored"] += 1
        for k in tallies:
            tallies[k].append(t[k])
    actual = Counter()
    for lam in LAMS:
        for feed in FEEDS:
            for cap in CAPS:
                actual["BURPS"] += 0  # filled below per cell
                for bg in BGS:
                    s12 = get(lam, 12, feed, cap, bg)
                    actual["BURPS"] += fed_word(s12) == "BURPS"
                    word, pred = unfed(s12, bg)
                    short = "MIXED" if word.startswith("MIXED") else word
                    actual["%s %s" % (bg, short)] += 1
                    if bg == "equal" and not pred.startswith("SPLIT"):
                        actual["equal scored"] += 1
    n_in = 0
    for k, vals in tallies.items():
        lo, hi = int(np.percentile(vals, LO)), int(np.percentile(vals, HI))
        ok = lo <= actual[k] <= hi
        n_in += ok
        print("%-32s | %d to %d | L=12 %d %s" % (k, lo, hi, actual[k], "in" if ok else "OUT"))
    print("counts: %d of %d inside" % (n_in, len(tallies)))


if __name__ == "__main__":
    main()

"""Scratch (2026-10-23, sandbox; not a registered reader): the cell-by-cell reads for T74's held-out size, after the
check of the draft amendment. Usage:

    python sandbox/heldout_2026-10-23/t74_heldout_cells_2026-10-23.py > sandbox/out/t74_heldout_cells_2026-10-23.txt

Reads only the per-replica cache sandbox/out/t74_stage1_replicas_2026-10-23.json (the 108 stage-1 files, read by name
by t74_heldout_resample_2026-10-23.py). Opens nothing in results/.

(a) Unfed words, two-level draw as in t74_heldout_twolevel_2026-10-23.py (fresh 32 per cell, then 16 from it): the
    cells whose stage-1 word (the same at L = 8 and 12) comes up in at least 99.7 % of the draws, and, for the other
    cells, the number that give their most likely word, with its 99.7 % range.
(b) The same with a one-level draw (16 from the 32), for the joint chance that every cell at or above 93 % repeats.
(c) Back-test, fitted on L = 8 alone, scored on L = 12: fed (settings with no short replica among L = 8's 48 must
    BURPS in every L = 12 cell), unfed (as in (a), from L = 8's 16 per cell), timing words (two-level).
"""
import importlib.util
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
_spec = importlib.util.spec_from_file_location("tl", HERE / "t74_heldout_twolevel_2026-10-23.py")
T = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(T)

LAMS, FEEDS, CAPS, BGS = T.LAMS, T.FEEDS, T.CAPS, T.BGS
D = 10000
THR = 0.997


def per_cell_shares(cells, rng, two_level, n16=16):
    """cells: {key: (pool, bg)}. Returns {key: Counter of words over D draws} and the list of per-draw words."""
    out = defaultdict(Counter)
    per_draw = []
    for _ in range(D):
        row = {}
        for key, (p, bg) in cells.items():
            stage = [p[i] for i in rng.integers(0, len(p), len(p))] if two_level else p
            s16 = [stage[i] for i in rng.integers(0, len(stage), n16)]
            w, _ = T.unfed_word(s16, bg)
            out[key][w] += 1
            row[key] = w
        per_draw.append(row)
    return out, per_draw


def split_rule(cells, shares, stage_words):
    must = [k for k in cells if stage_words[k] is not None and shares[k][stage_words[k]] / D >= THR]
    rest = [k for k in cells if k not in must]
    modal = {k: shares[k].most_common(1)[0][0] for k in rest}
    return must, rest, modal


def main():
    reps = json.loads(T.CACHE.read_text())
    rng = np.random.default_rng(20261023)

    def get(lam, L, feed, cap, bg):
        return reps["%s|%d|%s|%s|%s" % (lam, L, feed, cap, bg)]

    keys = [(lam, feed, cap, bg) for lam in LAMS for feed in FEEDS for cap in CAPS for bg in BGS]

    # (a) two-level, L = 8 and 12 pooled
    cells = {k: (get(k[0], 8, *k[1:]) + get(k[0], 12, *k[1:]), k[3]) for k in keys}
    w8 = {k: T.unfed_word(get(k[0], 8, *k[1:]), k[3])[0] for k in keys}
    w12 = {k: T.unfed_word(get(k[0], 12, *k[1:]), k[3])[0] for k in keys}
    stage_words = {k: (w8[k] if w8[k] == w12[k] else None) for k in keys}
    shares, per_draw = per_cell_shares(cells, rng, True)
    must, rest, modal = split_rule(cells, shares, stage_words)
    print("== (a) Unfed, two-level, L = 16 ==")
    print("cells that must repeat their stage-1 word (share >= %.3f): %d" % (THR, len(must)))
    by_bg = Counter(k[3] for k in must)
    print("  by background: %s" % dict(by_bg))
    p_all = float(np.prod([shares[k][stage_words[k]] / D for k in must]))
    print("  P(all repeat | claim) %.4f" % p_all)
    print("cells left over: %d" % len(rest))
    for k in rest:
        print("  %s %-8s %-6s %-5s | L8 %s | L12 %s | most likely at L = 16: %s (%.3f)" % (
            k[0], k[1], k[2], k[3], w8[k], w12[k], modal[k], shares[k][modal[k]] / D))
    n_modal = [sum(row[k] == modal[k] for k in rest) for row in per_draw]
    lo, hi = np.percentile(n_modal, [T.LO, T.HI])
    print("number of the %d giving their most likely word: median %d, 99.7%% range %d to %d" % (
        len(rest), int(np.median(n_modal)), int(lo), int(hi)))
    joint = np.mean([all(row[k] == stage_words[k] for k in must) and lo <= sum(row[k] == modal[k] for k in rest) <= hi
                     for row in per_draw])
    print("P(the unfed read repeats stage 1 | claim), same draws: %.4f" % joint)

    # (b) one-level, the checker's literal rule (>= 0.93 of the draws, one-level)
    shares1, _ = per_cell_shares(cells, rng, False)
    lit = [k for k in keys if stage_words[k] is not None and shares1[k][stage_words[k]] / D >= 0.93]
    p1 = float(np.prod([shares1[k][stage_words[k]] / D for k in lit]))
    p2 = float(np.prod([shares[k][stage_words[k]] / D for k in lit]))
    print()
    print("== (b) The rule 'every cell at or above 93 %% (one-level) repeats': %d cells; P(all repeat | claim) "
          "one-level %.3f, two-level %.3f ==" % (len(lit), p1, p2))

    # (c) back-test
    print()
    print("== (c) Back-test, fitted on L = 8 alone, scored on L = 12 ==")
    fails = 0
    for lam in LAMS:
        for feed in FEEDS:
            for cap in CAPS:
                p8 = [x for bg in BGS for x in get(lam, 8, feed, cap, bg)]
                s8 = sum(not T.fed_ok(x) for x in p8)
                cells12 = [T.fed_ok(x) for bg in BGS for x in get(lam, 12, feed, cap, bg)]
                words12 = []
                for bg in BGS:
                    s = get(lam, 12, feed, cap, bg)
                    words12.append("BURPS" if all(T.fed_ok(x) for x in s) else
                                   ("NEVER BURPS" if all(x["fed_daughters"] == 0 for x in s) else "MIXED"))
                if s8 == 0:
                    bad = [w for w in words12 if w != "BURPS"]
                    fails += len(bad)
                    if bad:
                        print("  fed: %s %s %s certain from L = 8 (0 short of 48), L = 12 words %s" % (
                            lam, feed, cap, words12))
                else:
                    print("  fed: %s %s %s uncertain from L = 8 (%d short of 48); L = 12 words %s" % (
                        lam, feed, cap, s8, words12))
    print("fed: certain cells from L = 8 that did not BURPS at L = 12: %d" % fails)

    cells8 = {k: (get(k[0], 8, *k[1:]), k[3]) for k in keys}
    sh8, pd8 = per_cell_shares(cells8, rng, True)
    must8 = [k for k in keys if sh8[k][w8[k]] / D >= THR]
    rest8 = [k for k in keys if k not in must8]
    modal8 = {k: sh8[k].most_common(1)[0][0] for k in rest8}
    miss = [k for k in must8 if w12[k] != w8[k]]
    n8 = [sum(row[k] == modal8[k] for k in rest8) for row in pd8]
    lo8, hi8 = np.percentile(n8, [T.LO, T.HI])
    n12 = sum(w12[k] == modal8[k] for k in rest8)
    print("unfed: %d cells must repeat from L = 8; %d did not at L = 12 %s; of the other %d, %d at L = 12 gave "
          "the most likely word, range %d to %d" % (len(must8), len(miss), miss, len(rest8), n12, int(lo8),
                                                     int(hi8)))

    same = 0
    rng2 = np.random.default_rng(20261024)
    for lam in LAMS:
        for cap in CAPS:
            st8 = T.stats([x for bg in BGS for x in get(lam, 8, "steady", cap, bg)])
            st12 = T.stats([x for bg in BGS for x in get(lam, 12, "steady", cap, bg)])
            for feed in ("meals16", "meals256"):
                me8 = T.stats([x for bg in BGS for x in get(lam, 8, feed, cap, bg)])
                me12 = T.stats([x for bg in BGS for x in get(lam, 12, feed, cap, bg)])
                r0, c0 = T.pmean(me8) / T.pmean(st8), T.pcv(me8) / T.pcv(st8)
                fm, fmc = T.draws(me8, 48, rng2, D)
                fs, fsc = T.draws(st8, 48, rng2, D)
                nm, nmc = T.draws(me8, 48, rng2, D)
                ns, nsc = T.draws(st8, 48, rng2, D)
                words = Counter(T.timing_word(a, b) for a, b in zip(r0 + nm / ns - fm / fs,
                                                                    c0 + nmc / nsc - fmc / fsc))
                (w, n), = words.most_common(1)
                w_12 = T.timing_word(T.pmean(me12) / T.pmean(st12), T.pcv(me12) / T.pcv(st12))
                same += (w == w_12 and n == D)
    print("timing: %d of 12 L = 12 words equal to the word every two-level draw from L = 8 gave" % same)


if __name__ == "__main__":
    main()

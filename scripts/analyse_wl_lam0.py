"""The T6 verdict table at lambda = 0 from the one-dimensional walks. Usage:

    python scripts/analyse_wl_lam0.py

Reads every results/wl_lam0_N*<tag>.npz, re-derives the four observables from each walk's
ln g(S) with the current analysis (so a repaired analysis re-reads old walks rather than needing
them re-run), applies gates 3 and 4 of PREREGISTRATION.md T6, and fits what passes. Under
amendment 2 only multiples of 16 enter the lambda = 0 fit; other sizes are shown and marked.

Gate 3: at each size the seeds must agree on the barrier to 20 % and on the latent heat to 10 %,
measured as (max - min) / mean. Gate 4: every walk must have made at least 20 round trips.
"""
import re
import sys
from collections import defaultdict
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
import run_wl_lam0 as W                          # noqa: E402

GATE3_BARRIER, GATE3_LATENT, GATE4_TRIPS = 0.20, 0.10, 20


def main(out_dir="results"):
    runs = defaultdict(list)
    for f in sorted(Path(out_dir).glob("wl_lam0_N*.npz")):
        m = re.match(r"wl_lam0_N(\d+)(.*)\.npz", f.name)
        n, tag = int(m.group(1)), m.group(2) or "(untagged)"
        d = np.load(f)
        got = W.observables(d["lng"], d["seen"], int(d["s_min"]), n)
        runs[n].append(dict(tag=tag, trips=int(d["round_trips"]), got=got))

    print("T6 at lambda = 0 by one-dimensional Wang-Landau in S. PREREGISTRATION.md T6, amendments 1-3.\n")
    print("%-5s %-6s %-11s %-6s %-8s %-15s %-9s %-9s  %s"
          % ("N", "knots", "tag", "trips", "g_c", "phi hot|cold", "latent", "barrier", "gate 4"))
    passing = []
    for n in sorted(runs):
        clean = (n % 16 == 0)
        rows = runs[n]
        for r in rows:
            g = r["got"]
            ok4 = r["trips"] >= GATE4_TRIPS
            if g:
                print("%-5d %-6s %-11s %-6d %-8.3f %-7.3f|%-7.3f %-9.3f %-9.3f  %s"
                      % (n, ("%d" % (n // 16)) if clean else "ribbon", r["tag"], r["trips"], g["g_c"],
                         g["phi_lo"], g["phi_hi"], g["latent"], g["barrier"], "pass" if ok4 else "FAIL"))
            else:
                print("%-5d %-6s %-11s %-6d %-8s %-15s %-9s %-9s  %s"
                      % (n, ("%d" % (n // 16)) if clean else "ribbon", r["tag"], r["trips"], "-", "no two humps",
                         "-", "-", "pass" if ok4 else "FAIL"))
        good = [r for r in rows if r["got"] and r["trips"] >= GATE4_TRIPS]
        if len(good) < 2:
            print("      -> %d seed(s) pass gate 4 with a fit; gate 3 needs at least two. Not fitted.\n" % len(good))
            continue
        bar = np.array([r["got"]["barrier"] for r in good])
        lat = np.array([r["got"]["latent"] for r in good])
        gc = np.array([r["got"]["g_c"] for r in good])
        sb = (bar.max() - bar.min()) / bar.mean()
        sl = (lat.max() - lat.min()) / lat.mean()
        ok3 = sb <= GATE3_BARRIER and sl <= GATE3_LATENT
        print("      -> %d seeds: barrier %.3f +/- %.3f (spread %.1f%%), latent %.3f +/- %.3f (spread %.1f%%), "
              "g_c %.3f +/- %.3f   gate 3 %s%s\n"
              % (len(good), bar.mean(), bar.std(ddof=1), 100 * sb, lat.mean(), lat.std(ddof=1), 100 * sl,
                 gc.mean(), gc.std(ddof=1), "pass" if ok3 else "FAIL",
                 "" if clean else "   [not a multiple of 16: shown, not fitted]"))
        if ok3 and clean:
            passing.append(dict(N=n, L=np.sqrt(n), barrier=bar.mean(), b_err=bar.std(ddof=1) / np.sqrt(len(bar)),
                                latent=lat.mean(), l_err=lat.std(ddof=1) / np.sqrt(len(lat)), g_c=gc.mean()))

    print("Sizes passing both gates and entering the fit: %s" % [p["N"] for p in passing])
    if len(passing) < 3:
        print("The pre-registered verdict needs at least three. No verdict from this table.")
        return
    L = np.array([p["L"] for p in passing]); b = np.array([p["barrier"] for p in passing])
    lat = np.array([p["latent"] for p in passing]); n = np.array([p["N"] for p in passing], float)
    # barrier against L (interface picture, 2D: dF = 2 sigma L) and against N (no interface)
    sL = np.linalg.lstsq(np.vstack([L, np.ones_like(L)]).T, b, rcond=None)[0]
    sN = np.linalg.lstsq(np.vstack([n, np.ones_like(n)]).T, b, rcond=None)[0]
    resL = b - (sL[0] * L + sL[1]); resN = b - (sN[0] * n + sN[1])
    lat0 = np.linalg.lstsq(np.vstack([1 / L, np.ones_like(L)]).T, lat, rcond=None)[0][1]
    print("\n  barrier = %.3f * L %+.3f   (rms residual %.3f)" % (sL[0], sL[1], np.sqrt((resL ** 2).mean())))
    print("  barrier = %.4f * N %+.3f  (rms residual %.3f)" % (sN[0], sN[1], np.sqrt((resN ** 2).mean())))
    print("  latent heat extrapolated to infinite size (against 1/L): %.3f per point" % lat0)
    print("\n  A barrier that grows with size, and a latent heat that stays finite, is the pre-registered")
    print("  FIRST ORDER signature. Which of L or N it grows with is not part of the verdict but is")
    print("  physics worth recording: L means an interface, N means none (knots cost nothing to separate).")


if __name__ == "__main__":
    main()

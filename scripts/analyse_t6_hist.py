"""The four pre-registered observables, from tempered energy histograms. Usage:

    python scripts/analyse_t6_hist.py t6_lam0_control

Prints to the screen and writes nothing. Implements PREREGISTRATION.md section T6 and makes no
choices of its own.

HOW THE TRANSITION COUPLING IS FOUND. A histogram measured at coupling g gives the histogram at
a nearby g' by multiplying each energy's count by exp(-H(1/g' - 1/g)); this is standard
single-histogram reweighting. Scanning g' and asking where the two humps carry equal weight
locates the transition. Reweighting is only trustworthy while the two distributions overlap, so
the shift is reported and one that is too large is refused rather than quietly used.

DISCRETENESS. [Kelly22] warns that a discrete action spectrum can make one hump look like
several. Our energies are discrete too, so a candidate pair of humps must be separated by more
than a few energy levels before it is counted; the separation used is reported.
"""
import csv
import sys
from collections import defaultdict
from pathlib import Path

import numpy as np

MAX_SHIFT = 0.25          # refuse a reweight of more than this fraction in 1/g
MIN_LEVELS_APART = 4      # humps closer than this many energy levels are one hump (discreteness)


def reweight(levels, counts, g_from, g_to):
    w = np.log(np.maximum(counts, 1e-300)) - levels * (1.0 / g_to - 1.0 / g_from)
    w -= w.max()
    p = np.exp(w)
    return p / p.sum()


def two_humps(levels, p):
    """Deepest genuine pair of humps, or None. Returns (low, high, valley) as indices."""
    interior = np.arange(1, len(p) - 1)
    maxima = [i for i in interior if p[i] >= p[i - 1] and p[i] >= p[i + 1]]
    best, best_depth = None, -np.inf
    for ai, a in enumerate(maxima):
        for b in maxima[ai + 1:]:
            if b - a < MIN_LEVELS_APART:
                continue
            v = a + int(np.argmin(p[a:b + 1]))
            if v in (a, b):
                continue
            depth = np.log(min(p[a], p[b])) - np.log(max(p[v], 1e-300))
            if depth > best_depth:
                best, best_depth = (a, b, v), depth
    return best


def observables(levels, counts, g0, n):
    """Scan for the coupling where the humps balance; return the pre-registered four."""
    best = None
    for g in np.linspace(g0 * (1 - MAX_SHIFT), g0 * (1 + MAX_SHIFT), 241):
        p = reweight(levels, counts, g0, g)
        hh = two_humps(levels, p)
        if hh is None:
            continue
        a, b, v = hh
        below = p[:v + 1].sum()
        imbalance = abs(np.log(max(below, 1e-300) / max(1 - below, 1e-300)))
        if best is None or imbalance < best[0]:
            best = (imbalance, g, a, b, v, p)
    if best is None:
        return None
    imbalance, g, a, b, v, p = best
    return dict(g_c=g, shift=abs(g - g0) / g0, imbalance=imbalance,
                latent=float(levels[b] - levels[a]) / n,
                barrier=float(np.log(min(p[a], p[b])) - np.log(p[v])),
                levels_apart=int(b - a))


def main(name, out_dir="results"):
    rows = list(csv.DictReader(open(Path(out_dir) / (name + ".csv"), newline="")))
    store = Path(out_dir) / (name + "_hist")
    per_size = defaultdict(list)

    for r in rows:
        n, rep, k, g0 = int(r["N"]), int(r["replica"]), int(r["k"]), float(r["g"])
        f = store / ("N%d_rep%d_k%d.npz" % (n, rep, k))
        if not f.exists():
            continue
        d = np.load(f)
        got = observables(d["levels"].astype(float), d["counts"].astype(float), g0, n)
        if got:
            got.update(N=n, rep=rep, g0=g0, trips=int(r["round_trips"]),
                       binder=float(r["binder"]), c=float(r["c_per_point"]),
                       largest=float(r["largest_frac"]))
            per_size[n].append(got)

    print("T6 by tempering, %s. Criteria from PREREGISTRATION.md section T6.\n" % name)
    print("%-6s %-5s %-9s %-9s %-8s %-9s %-9s %-8s %-7s"
          % ("N", "reps", "g_c", "shift", "levels", "latent", "barrier", "Binder", "trips"))
    summary = []
    for n in sorted(per_size):
        got = per_size[n]
        # for each replica keep its best-balanced coupling, then average over replicas
        by_rep = defaultdict(list)
        for d in got:
            by_rep[d["rep"]].append(d)
        picks = [min(v, key=lambda d: d["imbalance"]) for v in by_rep.values()]
        lat = np.array([d["latent"] for d in picks])
        bar = np.array([d["barrier"] for d in picks])
        print("%-6d %-5d %-9.3f %-9.3f %-8d %-9.4f %-9.3f %-8.5f %-7d"
              % (n, len(picks), np.mean([d["g_c"] for d in picks]),
                 np.mean([d["shift"] for d in picks]),
                 int(np.mean([d["levels_apart"] for d in picks])),
                 lat.mean(), bar.mean(), np.mean([d["binder"] for d in picks]),
                 min(d["trips"] for d in picks)))
        summary.append(dict(N=n, L=np.sqrt(n), latent=lat.mean(), barrier=bar.mean(),
                            latent_err=lat.std(ddof=1) / np.sqrt(len(lat)) if len(lat) > 1 else np.nan,
                            barrier_err=bar.std(ddof=1) / np.sqrt(len(bar)) if len(bar) > 1 else np.nan,
                            binder=np.mean([d["binder"] for d in picks]),
                            trips=min(d["trips"] for d in picks)))

    if len(summary) >= 2:
        L = np.array([s["L"] for s in summary])
        bar = np.array([s["barrier"] for s in summary])
        lat = np.array([s["latent"] for s in summary])
        A = np.vstack([L, np.ones_like(L)]).T
        slope = np.linalg.lstsq(A, bar, rcond=None)[0][0]
        A2 = np.vstack([1.0 / L, np.ones_like(L)]).T
        lat0 = np.linalg.lstsq(A2, lat, rcond=None)[0][1]
        print("\n  barrier against L: slope %+.4f" % slope)
        print("  latent heat extrapolated to infinite size: %+.5f" % lat0)
        print("\n  (Fits shown for orientation only. The pre-registered verdict needs at least three"
              "\n   sizes passing the gates, and the gate on round trips is the one to watch here.)")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "t6_lam0_control")

"""Sandbox look, 22 October 2026 (rule 16: a look, not a result; it can kill, not crown).

The owner's hypothesis (VISION Update 89): perhaps the network's negative curvature at finite coupling is the reason
lambda is above 1. The question put to this script: keeping the published energy unchanged (lambda = 1), does a
background of missing squares (his finite-coupling, negatively curved network) give a curled region an extra cost
that behaves like the curling cost 4 (lambda - 1) per surplus square of our lambda > 1 family?

Written link by link (Q1; VISION Update 5): H = 4 D + 4 (lambda - 1) X, with D the missing squares (sum over links of
max(0, 2 - S_e)) and X the surplus squares (sum of max(0, S_e - 2)). At lambda = 1, H = 4 D exactly, so the surplus
never enters the energy, in any background. Whatever price a curl has at lambda = 1 is either (a) the missing squares
it makes or heals while forming, or (b) entropy: the number of arrangements lost or gained. Only (b) can give a price
per surplus square that the energy does not already charge, and (b) scales with the coupling g.

Four exact looks, each cheap:

  A. The exhaustive census at 16 and 18 points (results/ergodicity_small.csv): the labelled count of every class
     against its surplus X at fixed deficit D. The slope of -g ln(count) in X is the exact entropic price per surplus
     square in that tiny ensemble. Also the same under interchangeable points (one weight per class).
  B. Single switches from two fixed backgrounds: the flat 14 x 14 torus (every link two squares) and the finite Fig. 7
     tiling of the model's author (240 points, every point three squares and one hexagon: his negatively curved
     background; scripts/build_planted_allotrope.py). Every valid switch near one point (both are vertex-transitive),
     priced at lambda = 1 and sorted by whether it adds surplus squares.
  C. Warm networks at lambda = 1 (his model), N = 196 = 4 x 7^2: the saved equilibrium graphs of T36 at g = 3.433 and
     3.697 (results/t36_allotropes_n196_adj/), and fresh short chains from the lattice at colder g (nearly flat).
     For each graph: the defect density D/N, the link census P(S_e = k), the potential of mean force per link
     -(g/4) ln[P(S_e = 3) / P(S_e = 2)] (an effective lambda_eff - 1 for one link, with correlations folded in), and
     the energy price at lambda = 1 of every valid switch, split by the sign of its change in X.
  D. The arithmetic that follows: lambda_eff - 1 from each measure, and how it depends on g.

Usage: python sandbox/background_curl_price.py [--quick] > sandbox/out/background_curl_price_2026-10-22.txt
"""
import argparse
import csv
import glob
import math
import os
import sys
import time
from collections import Counter

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, "src"))
sys.path.insert(0, os.path.join(ROOT, "scripts"))
from graphity.cqg import NO_CAP, run_chain, torus  # noqa: E402
from graphity.cqg_d import _switch, is_valid, surplus, total_squares  # noqa: E402
from graphity.squares import squares_on_edge  # noqa: E402
import build_planted_allotrope as bpa  # noqa: E402


# ----------------------------------------------------------------------------------------------------------------
# helpers
# ----------------------------------------------------------------------------------------------------------------
def link_census(adj):
    """Counts of links by squares carried, S_e = 0..3; plus D and X."""
    c = Counter()
    for u in range(adj.shape[0]):
        for v in adj[u]:
            v = int(v)
            if v > u:
                c[int(squares_on_edge(adj, u, v))] += 1
    d = sum(max(0, 2 - k) * n for k, n in c.items())
    x = sum(max(0, k - 2) * n for k, n in c.items())
    return c, d, x


def all_switches(adj, part, near=4):
    """Every valid switch with u1 on side 0 and u2 within `near` steps, as (dD, dX) at lambda = 1 price 4 dD."""
    side0 = np.flatnonzero(part == 0)
    rows = bpa.switches(adj, part, side0, near=near, lam=1.0)
    out = []
    for dh, ds, dx, *_ in rows:
        dd = -4 * ds + dx                      # D = 4 (N - S) + X, so dD = -4 dS + dX
        out.append((dd, dx))
    return out


def switch_summary(sw):
    """Split switches by the sign of dX; price at lambda = 1 is 4 dD."""
    by = {"dX>0": [], "dX=0": [], "dX<0": []}
    for dd, dx in sw:
        by["dX>0" if dx > 0 else ("dX<0" if dx < 0 else "dX=0")].append(4 * dd)
    lines = []
    for k in ("dX>0", "dX=0", "dX<0"):
        v = by[k]
        if v:
            lines.append("    %-5s n=%6d  share=%5.1f%%  price at lambda=1: min %+5.0f mean %+6.1f  (downhill %5.1f%%, zero %5.1f%%)"
                         % (k, len(v), 100 * len(v) / len(sw), min(v), sum(v) / len(v),
                            100 * sum(1 for p in v if p < 0) / len(v), 100 * sum(1 for p in v if p == 0) / len(v)))
        else:
            lines.append("    %-5s n=     0" % k)
    return "\n".join(lines), by


def surplus_objects(adj):
    """Connected groups of links carrying three squares (links joined through shared points), by size; and how many
    groups are closed rings of four such links on one square (the curled column of paper 2, in kind)."""
    n = adj.shape[0]
    links = []
    for u in range(n):
        for v in adj[u]:
            v = int(v)
            if v > u and squares_on_edge(adj, u, v) > 2:
                links.append((u, v))
    parent = list(range(len(links)))

    def find(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i

    by_point = {}
    for i, (u, v) in enumerate(links):
        for p in (u, v):
            if p in by_point:
                parent[find(i)] = find(by_point[p])
            by_point[p] = i
    groups = {}
    for i in range(len(links)):
        groups.setdefault(find(i), []).append(links[i])
    sizes = Counter(len(g) for g in groups.values())
    rings4 = 0
    for g in groups.values():
        if len(g) == 4:
            pts = Counter(p for e in g for p in e)
            if len(pts) == 4 and all(c == 2 for c in pts.values()):
                rings4 += 1
    return len(links), dict(sorted(sizes.items())), rings4


def pmf(census, g):
    """Potential of mean force per link, in units of 4(lambda - 1): -(g/4) ln[P(3)/P(2)]; and the deficit side."""
    p2, p3, p1 = census.get(2, 0), census.get(3, 0), census.get(1, 0)
    up = -(g / 4) * math.log(p3 / p2) if p3 and p2 else float("nan")
    down = -(g / 4) * math.log(p1 / p2) if p1 and p2 else float("nan")
    return up, down


# ----------------------------------------------------------------------------------------------------------------
# A. the exhaustive census at 16 and 18 points
# ----------------------------------------------------------------------------------------------------------------
def part_a():
    print("A. Exact census at N = 16 and 18 (results/ergodicity_small.csv): entropy against surplus at lambda = 1")
    print("   H(lambda = 1) = 4 D with D = 4 (N - S) + X. Weight of a class with named points = labelled states x exp(-4D/g).")
    with open(os.path.join(ROOT, "results", "ergodicity_small.csv"), newline="") as fh:
        rows = [r for r in csv.DictReader(fh) if r["cap"] == "none" and r["class_id"] != "-1"]
    for n in (16, 18):
        cl = [r for r in rows if int(r["N"]) == n]
        print("\n   N = %d: %d classes" % (n, len(cl)))
        print("   %6s %4s %4s %4s %12s %10s" % ("class", "S", "X", "D", "labelled", "ln(count)"))
        data = []
        for r in cl:
            s, x = int(r["squares"]), int(r["surplus"])
            d = 4 * (n - s) + x
            cnt = int(r["labelled_states"])
            data.append((d, x, math.log(cnt), cnt, s))
            print("   %6s %4d %4d %4d %12d %10.3f" % (r["class_id"], s, x, d, cnt, math.log(cnt)))
        # slope of ln(count) in X at fixed D, where D has more than one X (the entropic price per surplus square)
        byd = {}
        for d, x, lc, cnt, s in data:
            byd.setdefault(d, []).append((x, lc))
        for d in sorted(byd):
            pts = sorted(byd[d])
            if len(pts) >= 2 and pts[0][0] != pts[-1][0]:
                xs = np.array([p[0] for p in pts], float)
                ys = np.array([p[1] for p in pts], float)
                slope = np.polyfit(xs, ys, 1)[0]
                print("   at D = %d: ln(count) changes by %+.3f per surplus square over X = %d..%d; entropic price per"
                      " surplus square = %+.4f g, i.e. lambda_eff - 1 = %+.4f g (named points)"
                      % (d, slope, int(xs.min()), int(xs.max()), -slope, -slope / 4))
        # the ensemble average of X at a few g, named against interchangeable points
        for g in (1.5, 3.0):
            wl = [cnt * math.exp(-4 * d / g) for d, x, lc, cnt, s in data]
            wu = [math.exp(-4 * d / g) for d, x, lc, cnt, s in data]
            xl = sum(w * x for w, (d, x, *_) in zip(wl, data)) / sum(wl)
            xu = sum(w * x for w, (d, x, *_) in zip(wu, data)) / sum(wu)
            print("   g = %.1f: <X>/N = %.3f with named points, %.3f with interchangeable points" % (g, xl / n, xu / n))
    print("\n   Reading: at N = 16 every class has D = 0, so the energy is the same for all of them at lambda = 1 and the"
          "\n   whole ensemble is the counting. The labelled count is (8!)^2 / symmetries, so the price of surplus there is"
          "\n   the symmetry of the curled states, not any surroundings: with interchangeable points it runs the other way.")


# ----------------------------------------------------------------------------------------------------------------
# B. single switches from the flat torus and from the Fig. 7 background
# ----------------------------------------------------------------------------------------------------------------
def part_b():
    print("\nB. Every valid single switch near one point, priced at lambda = 1 (4 dD), by the sign of its change in X")
    adj, part = torus(14, 14, NO_CAP)
    c, d, x = link_census(adj)
    print("   flat 14 x 14 torus, N = 196: links by squares %s, D = %d, X = %d" % (dict(sorted(c.items())), d, x))
    rows = bpa.switches(adj, part, [int(np.flatnonzero(part == 0)[0])], near=4, lam=1.0)
    sw = [(-4 * ds + dx, dx) for dh, ds, dx, *_ in rows]
    txt, by = switch_summary(sw)
    print(txt)
    print("    classes (dD, dX) -> count:", dict(sorted(Counter(sw).items())))
    bg, bpart = bpa.background(240)
    c, d, x = link_census(bg)
    print("   Fig. 7 background, N = 240 (three squares and one hexagon at every point; his negatively curved space):"
          " links by squares %s, D = %d (%.2f per point), X = %d" % (dict(sorted(c.items())), d, d / 240, x))
    rows = bpa.switches(bg, bpart, [int(np.flatnonzero(bpart == 0)[0])], near=4, lam=1.0)
    sw = [(-4 * ds + dx, dx) for dh, ds, dx, *_ in rows]
    txt, by = switch_summary(sw)
    print(txt)
    print("    classes (dD, dX) -> count:", dict(sorted(Counter(sw).items())))
    print("   Reading: a switch that creates a surplus square must first create a square; on a link already carrying two"
          "\n   that square is free at lambda = 1, and on a link carrying one it is paid for (-4). So the energy never"
          "\n   charges for the surplus, and in the deficit background it pays for the square that becomes surplus.")


# ----------------------------------------------------------------------------------------------------------------
# C. warm networks at lambda = 1
# ----------------------------------------------------------------------------------------------------------------
def graph_report(label, adj, part, g, near, do_switches=True):
    c, d, x = link_census(adj)
    n = adj.shape[0]
    up, down = pmf(c, g)
    tot = sum(c.values())
    line = ("   %-34s D/N=%.3f X/N=%.3f  P(S_e=0..3)=%s  PMF per link: surplus %+.3f  deficit %+.3f  [x 4(lambda-1)]"
            % (label, d / n, x / n, "/".join("%.3f" % (c.get(k, 0) / tot) for k in range(4)), up, down))
    print(line)
    out = dict(label=label, g=g, d=d / n, x=x / n, p=[c.get(k, 0) / tot for k in range(4)], up=up, down=down)
    nl, sizes, rings = surplus_objects(adj)
    if nl:
        print("    surplus links: %d, in groups of size -> count %s; closed rings of four on one square: %d" % (nl, sizes, rings))
    out["rings"] = rings
    out["surplus_links"] = nl
    if do_switches:
        t0 = time.time()
        sw = all_switches(adj, part, near=near)
        txt, by = switch_summary(sw)
        print(txt + "    (%d switches, %.0f s)" % (len(sw), time.time() - t0))
        out["sw"] = {k: (len(v), (sum(v) / len(v) if v else float("nan")), (min(v) if v else float("nan")),
                         (sum(1 for p in v if p <= 0) / len(v) if v else float("nan"))) for k, v in by.items()}
    return out


def part_c(quick):
    print("\nC. Warm networks at lambda = 1 (the published model), N = 196")
    results = []
    # C1. fresh short chains from the lattice at colder couplings: nearly flat backgrounds
    print("   C1. fresh chains from the 14 x 14 lattice, 2,000 sweeps then one snapshot (EXPLORATORY; sandbox)")
    reps = 1 if quick else 3
    for g in (1.5, 2.5, 3.0, 3.2):
        for rep in range(reps):
            adj, part = torus(14, 14, NO_CAP)
            side_u = np.flatnonzero(part == 0).astype(np.int64)
            run_chain(adj, side_u, 1.0 / g, 2000, 1, 20261022 + 100 * rep + int(g * 10), lam=1.0, cap=NO_CAP)
            results.append(graph_report("g=%.2f fresh rep%d" % (g, rep), adj, part, g, near=4, do_switches=(rep == 0)))
    # C1b. the same couplings as T36, fresh from the lattice, at lambda = 1 and at lambda = 1.25 (EXPLORATORY): the
    # explicit price 4 (lambda - 1) = 1 should move the per-link ratio P(3)/P(2) by about exp(-1/g) if a link saw
    # only its own price; the comparison says how much a per-link reading responds to a known price.
    print("   C1b. fresh chains at T36's couplings, 5,000 sweeps, lambda = 1 against lambda = 1.25 (EXPLORATORY; sandbox)")
    for g in (3.433, 3.697):
        for lam in (1.0, 1.25):
            for rep in range(reps):
                adj, part = torus(14, 14, NO_CAP)
                side_u = np.flatnonzero(part == 0).astype(np.int64)
                run_chain(adj, side_u, 1.0 / g, 5000, 1, 20261023 + 100 * rep + int(g * 10) + int(lam * 7),
                          lam=lam, cap=NO_CAP)
                r = graph_report("g=%.3f lam=%.2f fresh rep%d" % (g, lam, rep), adj, part, g, near=4,
                                 do_switches=(rep == 0 and lam == 1.0))
                r["lam"] = lam
                results.append(r)
    # C2. the saved T36 equilibrium graphs (20,000 sweeps of equilibration; his model; named points)
    print("   C2. saved T36 graphs at g = 3.433 and 3.697, melt and lattice starts (results/t36_allotropes_n196_adj/)")
    files = sorted(glob.glob(os.path.join(ROOT, "results", "t36_allotropes_n196_adj", "*.npz")))
    want_snaps = ("snap400",) if quick else ("snap200", "snap400")
    want_reps = ("rep0",) if quick else ("rep0", "rep1", "rep2", "rep3")
    picked = [f for f in files if any(s in f for s in want_snaps) and any(("_%s_" % r) in f for r in want_reps)]
    for i, f in enumerate(picked):
        z = np.load(f)
        adj, part = z["adj"].astype(np.int64), z["part"].astype(np.int64)
        name = os.path.basename(f)[:-4]
        g = int(name.split("_")[0][1:]) / 1000.0
        results.append(graph_report("T36 " + name, adj, part, g, near=4, do_switches=(i % 2 == 0)))
    return results


# ----------------------------------------------------------------------------------------------------------------
# D. the arithmetic
# ----------------------------------------------------------------------------------------------------------------
def part_d(results):
    print("\nD. What the numbers say about an effective curling cost at lambda = 1")
    print("   per graph: g, defect density D/N, surplus density X/N, PMF per surplus link (= lambda_eff - 1 for one link),"
          " and the energy price of surplus-adding switches")
    print("   %-34s %5s %7s %7s %9s %9s %9s %9s %6s" % ("graph", "g", "D/N", "X/N", "PMF_up", "PMF_down", "mean dH", "min dH", "rings"))
    for r in results:
        sw = r.get("sw", {}).get("dX>0")
        print("   %-34s %5.3f %7.3f %7.3f %+9.3f %+9.3f %9s %9s %6d"
              % (r["label"], r["g"], r["d"], r["x"], r["up"], r["down"],
                 ("%+.1f" % sw[1]) if sw else "-", ("%+.0f" % sw[2]) if sw else "-", r.get("rings", 0)))
    # the lambda = 1 against 1.25 comparison at the same g: the per-link ratio's response to a known price of 1
    pairs = {}
    for r in results:
        if "lam" in r:
            pairs.setdefault(r["g"], {}).setdefault(r["lam"], []).append(r)
    for g in sorted(pairs):
        if 1.0 in pairs[g] and 1.25 in pairs[g]:
            def ratio(rs):
                p3 = sum(x["p"][3] for x in rs) / len(rs)
                p2 = sum(x["p"][2] for x in rs) / len(rs)
                return p3 / p2 if p2 else float("nan")
            r1, r125 = ratio(pairs[g][1.0]), ratio(pairs[g][1.25])
            if r1 and r125:
                print("   g = %.3f: P(3)/P(2) is %.4f at lambda = 1 and %.4f at lambda = 1.25; their ratio %.3f against"
                      " exp(-1/g) = %.3f for a link that saw only its own price (implied price %.2f in units of"
                      " 4(lambda-1), true 1.00)" % (g, r1, r125, r125 / r1, math.exp(-1 / g), -g * math.log(r125 / r1) / 4))
    print("\n   How to read PMF_up: if the surplus links in a background at coupling g were held only by a per-link price c"
          "\n   in the energy, their share against two-square links would be P(3)/P(2) = exp(-c/g) and c = PMF_up x 4."
          "\n   In our family that price is 4 (lambda - 1), so PMF_up is the lambda_eff - 1 one link sees, correlations"
          "\n   included. PMF_down does the same for a missing square, whose true energy price is 4 (PMF_down = 1 if entropy"
          "\n   played no part); its distance from 1 shows how much the surroundings move these per-link numbers.")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--quick", action="store_true")
    args = ap.parse_args()
    t0 = time.time()
    part_a()
    part_b()
    res = part_c(args.quick)
    part_d(res)
    print("\n(%.0f s)" % (time.time() - t0))


if __name__ == "__main__":
    main()

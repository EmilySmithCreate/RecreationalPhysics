"""Sandbox look, 23 October 2026 (rule 16: a look; it can kill, not crown). Two questions of the owner's, both on
saved three-direction graphs (six links per point), her predictions recorded in sandbox/NOTEBOOK.md first.

A. The slab's edge: does the opening put curl (surplus squares, links at five) in the opened region and uncurl
   (missing squares, links below four) in the curled region? Her rule needs "curl to the daughter, uncurl to the
   mother". Read on the T71 control end states (the fed slab cycling under the layer form, three curling costs,
   64 graphs each) and on the T53 end states (the rod opening one direction in a bath). Every link is classed by
   its squares (flat = 4; surplus = 5; deficit < 4) and placed by the local dimension d of its two endpoints:
   both at the open rung, both at the curled rung, mixed (the seam), or touching a damaged point (d outside the
   ladder's rungs). Reported: surplus and deficit links per region, per thousand links of that region.

B. Flaws per seed in three directions: from T53's per-reading logs, the number of open regions at the first tenth
   (the seeds) and the damaged points (d above the ladder) at the final reading, per replica; and from the end
   states, the damaged points grouped into connected pieces, by size. Compared with two directions' one knot per
   three seeds (O107). Her prediction: fewer per seed in three directions.

Usage: python3 sandbox/slab_edge_and_flaws_3d.py > sandbox/out/slab_edge_and_flaws_3d_2026-10-23.txt
"""
import csv
import glob
import os
import sys
from collections import Counter, defaultdict

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, "src"))
from graphity.cqg_d import squares_on_edge  # noqa: E402
from graphity.dimension import local_dimension_d, pieces_of  # noqa: E402

FLAT = 4            # squares per link on the flat six-link lattice


def link_census_by_region(adj, open_rung, curled_rung):
    d = local_dimension_d(adj)
    n = adj.shape[0]
    reg = {}
    for v in range(n):
        reg[v] = "open" if d[v] == open_rung else ("curled" if d[v] == curled_rung else "damaged")
    counts = defaultdict(lambda: Counter())
    for u in range(n):
        for v in adj[u]:
            v = int(v)
            if v <= u:
                continue
            s = int(squares_on_edge(adj, u, v))
            a, b = reg[u], reg[v]
            where = "damaged" if "damaged" in (a, b) else ("seam" if a != b else a)
            counts[where]["links"] += 1
            if s > FLAT:
                counts[where]["surplus"] += 1
            elif s < FLAT:
                counts[where]["deficit"] += 1
    pts = Counter(reg.values())
    return counts, pts, d


def report_region_counts(label, acc):
    print("  %-44s %8s %8s %8s | %10s %10s" % (label, "links", "surplus", "deficit", "surplus/k", "deficit/k"))
    for where in ("open", "curled", "seam", "damaged"):
        c = acc[where]
        if c["links"]:
            print("  %-44s %8d %8d %8d | %10.1f %10.1f" % (where, c["links"], c["surplus"], c["deficit"],
                                                            1000 * c["surplus"] / c["links"], 1000 * c["deficit"] / c["links"]))


def part_a():
    print("A. Where the curl and the uncurl sit, by region (open rung / curled rung / seam / touching damage)")
    # T71 controls: the slab 4 x L x L fed under the layer form; open rung d = 3, curled rung d = 2
    for lam in ("110", "125", "140"):
        files = sorted(glob.glob(os.path.join(ROOT, "results", "t71_control_lam%s_adj" % lam, "*.npz")))
        acc = defaultdict(Counter)
        pts = Counter()
        for f in files:
            with np.load(f) as z:
                adj = z["adj"].astype(np.int64)
            c, p, _ = link_census_by_region(adj, 3, 2)
            for k, v in c.items():
                acc[k].update(v)
            pts.update(p)
        print("\n T71 controls, lambda = %s, %d end states; points by region: %s" % (lam[0] + "." + lam[1:], len(files), dict(pts)))
        report_region_counts("T71 lam %s" % lam, acc)
    # T53: the rod 4 x 4 x L opening one direction in a bath; open rung d = 2, curled rung d = 1
    for lam in ("125", "140"):
        for g in ("15", "25", "35"):
            files = sorted(glob.glob(os.path.join(ROOT, "results", "t53_l*_lam%s_g%s_adj" % (lam, g), "*.npz")))
            acc = defaultdict(Counter)
            pts = Counter()
            for f in files:
                with np.load(f) as z:
                    adj = z["adj"].astype(np.int64)
                c, p, _ = link_census_by_region(adj, 2, 1)
                for k, v in c.items():
                    acc[k].update(v)
                pts.update(p)
            print("\n T53, lambda = %s, g = %s, %d end states (three lengths); points by region: %s" % (lam[0] + "." + lam[1:], g[0] + "." + g[1:], len(files), dict(pts)))
            report_region_counts("T53 lam %s g %s" % (lam, g), acc)


def part_b():
    print("\n\nB. Flaws per seed in three directions (T53: the rod opening one direction in a bath)")
    print("  seeds = open regions at the first reading with a tenth of the points at d >= 2; damaged = points with d above the ladder at the last reading")
    print("  %-6s %-5s %-5s | %6s %8s %8s %10s | %s" % ("lam", "g", "L", "reps", "seeds", "damaged", "dmg/seed", "damaged pieces by size (end states, pooled)"))
    for lam in ("125", "140"):
        for g in ("15", "20", "25", "30", "35"):
            for L in ("18", "36", "72"):
                path = os.path.join(ROOT, "results", "t53_l%s_lam%s_g%s.csv" % (L, lam, g))
                if not os.path.exists(path):
                    continue
                by = defaultdict(list)
                for r in csv.DictReader(open(path, newline="")):
                    by[int(r["replica"])].append(r)
                seeds, dmg = [], []
                for rep, rows in by.items():
                    n = int(rows[0]["N"])
                    first = next((r for r in rows if int(r["n_open2"]) >= n / 10), None)
                    if first is None:
                        continue
                    seeds.append(int(first["open_regions"]))
                    dmg.append(int(rows[-1]["damaged_d"]))
                sizes = Counter()
                for f in sorted(glob.glob(os.path.join(ROOT, "results", "t53_l%s_lam%s_g%s_adj" % (L, lam, g), "*.npz"))):
                    with np.load(f) as z:
                        adj = z["adj"].astype(np.int64)
                    d = local_dimension_d(adj)
                    damaged = d > 3
                    if damaged.any():
                        for size in pieces_of(adj, damaged):
                            sizes[size] += 1
                if seeds:
                    print("  %-6s %-5s %-5s | %6d %8.1f %8.1f %10.2f | %s" % (lam, g, L, len(seeds), np.mean(seeds), np.mean(dmg),
                                                                           (sum(dmg) / sum(seeds)) if sum(seeds) else float("nan"), dict(sorted(sizes.items()))))


if __name__ == "__main__":
    if "--b" not in sys.argv:
        part_a()
    part_b()

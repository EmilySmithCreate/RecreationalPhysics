"""Sandbox look, 23 October 2026 (rule 16: a look; it can kill, not crown). The owner's prediction, recorded in
sandbox/NOTEBOOK.md before this ran: after a slab opens, the curl ends up inside the open space as closed curled
rings, and the uncurl sits at the lip, on a tiny fraction of flaws.

On T56's saved end states (the slab 4 x L x L under "all at the last" in a bath, 8 replicas per cell, and the untied
controls), with the slab's rungs: open = d = 3 (all three directions open), curled = d = 2 (the slab's own rung),
damaged = anything else. Counted per end state:
  * surplus rings inside the open space: squares whose four links each carry five squares and whose four points all
    sit at d = 3 (the three-direction cousin of paper 2's column);
  * surplus links inside the open space (both ends at d = 3, five squares);
  * deficit links (below four squares) inside the open space, inside the curled region, at the seam (ends at
    different rungs) and touching damaged points;
  * seeds: open_regions3 at the first reading with a tenth of the points at d = 3 (T56's own rule for the slab).
Per cell: replicas that opened, mean seeds, and each count per seed. Rods (4 x 4 x L) are reported with the same
census but their "open" rung is d = 2 (one direction still curled), so their surplus is not read as curl.

Usage: python3 sandbox/curl_in_open_space.py > sandbox/out/curl_in_open_space_2026-10-23.txt
"""
import csv
import glob
import os
import re
import sys
from collections import Counter, defaultdict

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, "src"))
from graphity.cqg_d import squares_on_edge  # noqa: E402
from graphity.dimension import local_dimension_d  # noqa: E402

FLAT = 4


def census(adj, open_rung, curled_rung):
    n = adj.shape[0]
    d = local_dimension_d(adj)
    nb = [set(int(x) for x in row) for row in adj]
    reg = ["open" if d[v] == open_rung else ("curled" if d[v] == curled_rung else "damaged") for v in range(n)]
    sq = {}
    for u in range(n):
        for v in nb[u]:
            if v > u:
                sq[(u, v)] = int(squares_on_edge(adj, u, v))
    c = Counter()
    for (u, v), s in sq.items():
        a, b = reg[u], reg[v]
        where = "damaged" if "damaged" in (a, b) else ("seam" if a != b else a)
        c["links_" + where] += 1
        if s > FLAT:
            c["surplus_" + where] += 1
        elif s < FLAT:
            c["deficit_" + where] += 1
    # surplus rings inside the open space: squares with all four links at five and all four points open
    rings = set()
    for a in range(n):
        if reg[a] != "open":
            continue
        for b in nb[a]:
            if reg[b] != "open" or sq[(min(a, b), max(a, b))] != 5:
                continue
            for dd in nb[a]:
                if dd <= b or reg[dd] != "open" or sq[(min(a, dd), max(a, dd))] != 5:
                    continue
                for cc in nb[b] & nb[dd]:
                    if cc == a or reg[cc] != "open":
                        continue
                    if sq[(min(b, cc), max(b, cc))] == 5 and sq[(min(cc, dd), max(cc, dd))] == 5:
                        rings.add(frozenset((a, b, cc, dd)))
    c["rings_open"] = len(rings)
    c["points_open"], c["points_curled"], c["points_damaged"] = reg.count("open"), reg.count("curled"), reg.count("damaged")
    return c


def seeds_of(csv_path, geometry):
    col_n, col_r = ("n_open3", "open_regions3") if geometry == "slab" else ("n_open2", "open_regions")
    by = defaultdict(list)
    for r in csv.DictReader(open(csv_path, newline="")):
        by[int(r["replica"])].append(r)
    out = {}
    for rep, rows in by.items():
        n = int(rows[0]["N"])
        first = next((r for r in rows if int(r[col_n]) >= n / 10), None)
        out[rep] = int(first[col_r]) if first else None
    return out


def main():
    dirs = sorted(glob.glob(os.path.join(ROOT, "results", "t56_*_adj")))
    print("%-34s %4s %5s | %7s %7s | %9s %9s %10s | %10s %10s %10s %10s" % (
        "cell", "reps", "opened", "seeds", "open%", "rings/sd", "surpl/sd", "deficit/sd", "def_open", "def_curl", "def_seam", "def_dmg"))
    for dpath in dirs:
        name = os.path.basename(dpath)[:-4]
        geometry = "slab" if "slab" in name else "rod"
        open_rung, curled_rung = (3, 2) if geometry == "slab" else (2, 1)
        seeds = seeds_of(os.path.join(ROOT, "results", name + ".csv"), geometry)
        tot = Counter()
        n_opened = 0
        seed_sum = 0
        n_rep = 0
        for f in sorted(glob.glob(os.path.join(dpath, "*.npz"))):
            rep = int(re.search(r"rep(\d+)", os.path.basename(f)).group(1))
            n_rep += 1
            if seeds.get(rep) is None:
                continue
            with np.load(f) as z:
                adj = z["adj"].astype(np.int64)
            c = census(adj, open_rung, curled_rung)
            n_opened += 1
            seed_sum += seeds[rep]
            tot.update(c)
        if n_opened == 0:
            print("%-34s %4d %5d | %7s" % (name, n_rep, 0, "none opened"))
            continue
        npts = tot["points_open"] + tot["points_curled"] + tot["points_damaged"]
        per = lambda k: (tot[k] / seed_sum) if seed_sum else float("nan")
        print("%-34s %4d %5d | %7.2f %7.1f | %9.2f %9.1f %10.1f | %10d %10d %10d %10d" % (
            name, n_rep, n_opened, seed_sum / n_opened, 100 * tot["points_open"] / npts,
            per("rings_open"), per("surplus_open"), per("deficit_seam") + per("deficit_damaged"),
            tot["deficit_open"], tot["deficit_curled"], tot["deficit_seam"], tot["deficit_damaged"]))


if __name__ == "__main__":
    main()

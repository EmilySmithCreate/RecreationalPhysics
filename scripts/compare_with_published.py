"""Compare a sweep result with digitised published points. Usage:

    python scripts/compare_with_published.py results/<name>.csv docs/published/T25_fig3_digitised.csv

For every published point it prints our phi on the matching leg at the nearest
simulated coupling: the mean over replicas, the standard error between replicas,
and the difference. Published series names start with "cool" or "heat".
Prints only; writes nothing.
"""
import csv
import math
import statistics
import sys
from collections import defaultdict


def main(result_path, published_path):
    ours = defaultdict(list)                                   # (leg, g) -> phi of each replica
    with open(result_path, newline="") as fh:
        for r in csv.DictReader(fh):
            ours[(r["leg"], float(r["g"]))].append(float(r["phi"]))
    with open(published_path, newline="") as fh:
        published = list(csv.DictReader(fh))

    print(f"{'leg':4s} {'g publ.':>8s} {'g ours':>8s} {'publ.':>6s} {'ours':>6s} {'+/-':>6s} {'diff':>7s}")
    worst = 0.0
    for p in sorted(published, key=lambda p: (p["series"][:4], -float(p["g"]))):
        leg, g_pub, phi_pub = p["series"][:4], float(p["g"]), float(p["S_over_N"])
        g = min((g for (l, g) in ours if l == leg), key=lambda g: abs(math.log(g / g_pub)))
        phis = ours[(leg, g)]
        err = statistics.stdev(phis) / math.sqrt(len(phis)) if len(phis) > 1 else float("nan")
        diff = statistics.mean(phis) - phi_pub
        worst = max(worst, abs(diff))
        flag = "" if abs(math.log10(g / g_pub)) < 0.01 else "   (nearest coupling is not close)"
        print(f"{leg:4s} {g_pub:8.3f} {g:8.3f} {phi_pub:6.3f} {statistics.mean(phis):6.3f} {err:6.3f} {diff:+7.3f}{flag}")
    print(f"largest |difference| = {worst:.3f}")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])

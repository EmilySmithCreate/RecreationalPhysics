"""Sandbox look (exploratory; rule 16), 25 October 2026: the rod under the owner's pair tie in a warm bath. Usage:

    python sandbox/pair_tie_bath_look.py <lambda>          # runs one curling cost: g = 1.5, 2.0, 2.5, 4 replicas each
    python sandbox/pair_tie_bath_look.py --read            # summarises what has run

The rod 4 x 4 x 18 (two directions curled, one open), six links, the pair tie f = (0, 0, a, 0) (VISION Update 124),
followed by T56's tied bath chain (`scripts/run_curled_bath_tie_d.py`, unchanged) for 20,000 sweeps, read every 1,000.
Output under sandbox/out/pair_tie_bath/ (not results/). The question: once a bath opens the first curled direction, does
the second follow (points reaching d = 3, the flat state), or does the space break (points with d > 3) first?
Declared before the first run: BOTH OPEN (most points at d = 3, few broken), FIRST ONLY (most at d = 2), STAYS (most at
d = 1), BREAKS (a tenth or more of points broken), read per replica at the last reading.
"""
import csv
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "sandbox" / "out" / "pair_tie_bath"
PY = sys.executable


def run(lam):
    OUT.mkdir(parents=True, exist_ok=True)
    a = 4.0 * (lam - 1.0)
    for i, g in enumerate((1.5, 2.0, 2.5)):
        name = f"pairtie_rod_lam{int(round(lam * 100))}_g{int(round(g * 10))}"
        cfg = dict(_purpose="sandbox look, not a result (VISION Update 124)", name=name, section="sandbox",
                   dims=[4, 4, 18], **{"lambda": lam}, g=g, tie=[0.0, 0.0, a, 0.0], replicas=4, n_sweeps=20000,
                   record_every=1000, seed=20261025 + 10 * i + int(round(lam * 100)), save_adjacency=False)
        path = OUT / f"{name}.json"
        path.write_text(json.dumps(cfg, indent=2))
        if (OUT / f"{name}.csv").exists():
            continue
        subprocess.run([PY, str(ROOT / "scripts" / "run_curled_bath_tie_d.py"), str(path), str(OUT)], check=True,
                       stdout=subprocess.DEVNULL)


def word(r):
    n = int(r["N"])
    broken = sum(int(r[f"d{k}"]) for k in (4, 5, 6, 7))
    counts = {k: int(r[f"d{k}"]) for k in (1, 2, 3)}
    if broken >= n / 10:
        return "BREAKS"
    top = max(counts, key=counts.get)
    return {1: "STAYS", 2: "FIRST ONLY", 3: "BOTH OPEN"}[top]


def read():
    for path in sorted(OUT.glob("pairtie_rod_*.csv")):
        rows = list(csv.DictReader(open(path, newline="")))
        last = {}
        for r in rows:
            last[r["replica"]] = r
        words = [word(r) for _, r in sorted(last.items())]
        r0 = next(iter(last.values()))
        print(f"lam {r0['lam']} g {r0['g']}: {words}; at the end d1/d2/d3/broken = "
              + "; ".join(f"{r['d1']}/{r['d2']}/{r['d3']}/{sum(int(r[f'd{k}']) for k in (4, 5, 6, 7))}"
                          for _, r in sorted(last.items())))


if __name__ == "__main__":
    if sys.argv[1] == "--read":
        read()
    else:
        run(float(sys.argv[1]))

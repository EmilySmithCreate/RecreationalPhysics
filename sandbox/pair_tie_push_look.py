"""Sandbox look (exploratory; rule 16), 26 October 2026: one concentrated push into the rod under the owner's pair tie.
Usage:

    python sandbox/pair_tie_push_look.py          # writes the configs and runs them, 12 at a time
    python sandbox/pair_tie_push_look.py --read   # summarises what has run

The owner's decision of 26 October ("We need to do 1"): after the bath look (STAYS in 35 of 36 replicas), give the rod
one push, the role her picture gives the black hole, and see whether the second direction follows the first. The rod
4 x 4 x 18 (two directions curled, one open), six links, sealed, the push E packed into one point's store under the
per-vertex bath (`local_heat`: only moves made from a point spend its store; released energy stays where it is
released), everything else empty; `scripts/run_sealed_curled_d.py`, unchanged. The pair tie f = (0, 0, a, 0)
(VISION Update 124) at lambda = 1.20, 1.25, 1.40, and untied controls at 1.25 and 1.40 (T30's question again, under
local heat). E = 32, 64, 128, 256, 512: the single-move wall is about 26 to 29 under the tie, the first opening's seam
about 180 (out/pair_tie_patch_look.txt). Four replicas, 10,000 sweeps, read every 250. Output under
sandbox/out/pair_tie_push/ (not results/).
Declared before the first run, read per replica at the last reading: BOTH OPEN (most points at d = 3, under a tenth
broken), FIRST ONLY (most at d = 2), STAYS (most at d = 1), BREAKS (a tenth or more of points broken, d > 3); and
whether the rod ever left its start.
"""
import csv
import json
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "sandbox" / "out" / "pair_tie_push"
PY = sys.executable
CELLS = [("pair", 1.20), ("pair", 1.25), ("pair", 1.40), ("none", 1.25), ("none", 1.40)]
SPARKS = (32.0, 64.0, 128.0, 256.0, 512.0)


def configs():
    OUT.mkdir(parents=True, exist_ok=True)
    paths = []
    for tie, lam in CELLS:
        for spark in SPARKS:
            name = f"push_rod_{tie}_lam{int(round(lam * 100))}_E{int(spark)}"
            cfg = dict(_purpose="sandbox look, not a result (VISION Update 124)", name=name, section="sandbox",
                       dims=[4, 4, 18], **{"lambda": lam}, local_heat=True, capacities=["N"],
                       ftable_per_a=[0, 0, 1.0 if tie == "pair" else 0.0, 0], tie_label=f"{tie} tie",
                       sparks=[spark], replicas=4, n_sweeps=10000, record_every=250,
                       seed=20261026 + int(round(lam * 100)) + (0 if tie == "pair" else 1000), save_adjacency=True)
            path = OUT / f"{name}.json"
            path.write_text(json.dumps(cfg, indent=2))
            if not (OUT / f"{name}.csv").exists():
                paths.append(path)
    return paths


def run_one(path):
    subprocess.run([PY, str(ROOT / "scripts" / "run_sealed_curled_d.py"), str(path), str(OUT)], check=True,
                   stdout=subprocess.DEVNULL)


def word(r):
    n = int(r["N"])
    broken = int(r["melted"])
    counts = {k: int(r[f"d{k}"]) for k in (1, 2, 3)}
    if broken >= n / 10:
        return "BREAKS"
    top = max(counts, key=counts.get)
    return {1: "STAYS", 2: "FIRST ONLY", 3: "BOTH OPEN"}[top]


def read():
    for tie, lam in CELLS:
        for spark in SPARKS:
            path = OUT / f"push_rod_{tie}_lam{int(round(lam * 100))}_E{int(spark)}.csv"
            if not path.exists():
                continue
            last = {r["replica"]: r for r in csv.DictReader(open(path, newline="")) if r["final"] == "True"}
            parts = [f"{word(r)}{'' if r['left'] == 'True' else ' (never left)'} "
                     f"{r['d1']}/{r['d2']}/{r['d3']}/{r['melted']}" for _, r in sorted(last.items())]
            print(f"{tie:4s} lam {lam:.2f} E {int(spark):3d}: " + "; ".join(parts))


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--read":
        read()
    else:
        with ThreadPoolExecutor(12) as pool:
            list(pool.map(run_one, configs()))

"""Scratch (2026-10-23): what T71's held-out stage (L = 16) would cost, from the committed stage-1 configs and files.
Reads configs/t71_*.json and results/t71_* (row counts and file sizes only). Writes nothing.

    python3 sandbox/heldout_2026-10-23/t71_heldout_size.py
"""
import csv
import glob
import json
import os
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def n_sweeps(expr, lam, r):
    a = 4.0 * (lam - 1.0)
    return int(round(eval(str(expr), {"__builtins__": {}}, dict(a=a, r=r, max=max, min=min))))


tot_rs = tot_ps16 = tot_ps_stage1 = 0
print("job | sweeps per rate | replica-sweeps at L = 16 | point-sweeps at width 4: L = 16 against stage 1 (L = 8 + 12)")
for p in sorted(glob.glob(str(ROOT / "configs" / "t71_*.json"))):
    cfg = json.load(open(p))
    if "lambdas" in cfg:
        lam = float(cfg["lambdas"][0])
        sw = [n_sweeps(cfg["n_sweeps"], lam, r) for r in cfg["rates"]]
    else:
        lam = float(cfg["lambda"])
        sw = [(int(cfg["n_sweeps"]) // int(cfg["record_every"])) * int(cfg["record_every"])] * len(cfg["rates"])
    rs = int(cfg["replicas"]) * sum(sw)
    ps16 = rs * 4 * 16 * 16
    ps1 = rs * (4 * 8 * 8 + 4 * 12 * 12)
    tot_rs += rs; tot_ps16 += ps16; tot_ps_stage1 += ps1
    print("%s | %s | %d | %.3g against %.3g (ratio %.2f) | seed %d -> %d"
          % (cfg["name"], sw, rs, ps16, ps1, ps16 / ps1, cfg["seed"], cfg["seed"] + 12))
print("all 12 jobs: %d replica-sweeps; point-sweeps at width 4 %.3g at L = 16 against %.3g at stage 1 (ratio %.2f)"
      % (tot_rs, tot_ps16, tot_ps_stage1, tot_ps16 / tot_ps_stage1))

rows12 = rows_all = bytes_all = 0
for p in sorted(glob.glob(str(ROOT / "results" / "t71_*.csv"))):
    if "control" in p:
        continue
    c = Counter(r["L"] for r in csv.DictReader(open(p, newline="")))
    rows12 += c["12"]; rows_all += sum(c.values()); bytes_all += os.path.getsize(p)
print("layer-feed files, stage 1: %d rows (%d at L = 12), %.1f MB; %.0f bytes a row; at L = 16, if the rows a replica logs do not depend on L, about %d rows and %.0f MB"
      % (rows_all, rows12, bytes_all / 1e6, bytes_all / rows_all, rows12, rows12 * bytes_all / rows_all / 1e6))
adj = [os.path.getsize(f) for f in glob.glob(str(ROOT / "results" / "t71_control_*_adj" / "*N576*.npz"))]
print("control saved graphs: %d at N = 576 average %.0f bytes; scaled to N = 1,024: about %.1f MB per job (32 graphs)"
      % (len(adj), sum(adj) / len(adj), 32 * (sum(adj) / len(adj)) * 1024 / 576 / 1e6))
used = set()
for p in glob.glob(str(ROOT / "configs" / "*.json")):
    try:
        s = json.load(open(p)).get("seed")
    except Exception:
        continue
    if isinstance(s, int):
        used.add(s)
print("seeds 20267113 to 20267124 already in a config: %s" % sorted(s for s in used if 20267113 <= s <= 20267124))

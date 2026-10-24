"""Scratch (2026-10-23): which config seeds lie near T74's, so that a seed rule for T74's held-out L = 16 can avoid them.
Reads configs/*.json only. Usage: python sandbox/heldout_2026-10-23/t74_seed_map_2026-10-23.py"""
import collections
import json
from pathlib import Path

seeds = collections.defaultdict(list)
for p in sorted(Path("configs").glob("*.json")):
    try:
        c = json.loads(p.read_text())
    except Exception:
        continue
    if not isinstance(c, dict):
        continue
    s = c.get("seed")
    if isinstance(s, int) and 20267000 <= s <= 20268999:
        seeds[s].append(p.stem)

by_prefix = collections.defaultdict(list)
for s, names in seeds.items():
    for n in names:
        by_prefix[n.split("_")[0]].append(s)
for pre, v in sorted(by_prefix.items(), key=lambda kv: min(kv[1])):
    print("%-6s seeds %d to %d (%d configs)" % (pre, min(v), max(v), len(v)))
dups = {s: n for s, n in seeds.items() if len(n) > 1}
print("seeds used by more than one config: %d" % len(dups))
for s in sorted(dups):
    print("  %d: %s" % (s, ", ".join(dups[s])))
free = [s for s in range(20267509, 20267509 + 54) if s in seeds]
print("of 20267509 to 20267562 (54 seeds), already used: %d" % len(free))
for base in (20267701, 20267801, 20267901, 20268001):
    used = [s for s in range(base, base + 54) if s in seeds]
    print("of %d to %d, already used: %d" % (base, base + 53, len(used)))

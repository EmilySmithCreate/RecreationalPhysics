"""Scratch (2026-10-23, sandbox): what T74's held-out L = 16 configs would contain, built in memory from
`scripts/make_t74_configs.py`'s own cell generator with L = 16 and evaluated by `scripts/run_layer_outside.py`'s
`cell_numbers`. Writes nothing; launches nothing. Usage:

    python sandbox/heldout_2026-10-23/t74_l16_cells_2026-10-23.py
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))
sys.path.insert(0, str(ROOT / "src"))
import make_t74_configs as M  # noqa: E402
import run_layer_outside as R  # noqa: E402

stage1 = list(M.cells())
print("stage 1 cells: %d, seeds %d to %d" % (len(stage1), stage1[0]["seed"], stage1[-1]["seed"]))
keys = sorted(stage1[0].keys())
M.SIZES = (16,)
held = list(M.cells())
print("L = 16 cells from the same generator: %d; keys identical to stage 1: %s" % (
    len(held), sorted(held[0].keys()) == keys))
print("the generator's own seeds for them would be %d to %d (it restarts at SEED0; NOT to be used)" % (
    held[0]["seed"], held[-1]["seed"]))
seen = set()
for cfg in held:
    n = R.cell_numbers(cfg)
    sig = (cfg["lam"], cfg["cap_label"], cfg["feed_label"])
    if sig in seen:
        continue
    seen.add(sig)
    print("%s | a %.2f N_slab %d R %.1f c %.1f gate %.1f n_out %.0f meal %.1f every %d g_bg_warm %.2f n_fed %d "
          "n_digest_max %d n_unfed %d" % (
              cfg["name"], n["a"], n["N_slab"], n["R"], n["c"], n["gate"], n["n_out"], n["R"] * cfg["every"],
              cfg["every"], 4 * n["a"], n["n_fed"], n["n_digest_max"], n["n_unfed"]))

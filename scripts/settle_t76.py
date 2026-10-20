"""T76's settling runs alone, for the bisection that fixes its couplings. Usage:

    python scripts/settle_t76.py configs/t76_settle_<name>.json [out_dir]

PREREGISTRATION T76 fixes its four couplings by a rule: those at which the settled flat 16 x 16 sheet has
rho_eq = 0.003, 0.01, 0.03 and 0.1, found by bisection on settling runs alone (growth off) and written into an
amendment before any growth runs. This script measures rho_eq at the couplings a config lists; the bisection itself
(which couplings to try next, and when to stop) is the amendment's, and each round is its own config, so every
coupling tried is kept (rule 5; S1).

Each replica is exactly the settling stage of scripts/run_t76.py: the flat L x L torus, lambda, no cap,
graphity.row_growth.run_growth with growth off for `n_settle` (200) fair sweeps. rho_eq is the mean of rho = D / N
over the readings of the last `window` (100) fair sweeps (analyse_t76.rho_eq). Streams from
SeedSequence([seed, k, replica]) for the k-th coupling of the list.

Rows: one per (coupling, replica): g, replica, rho_eq, rho_sd (spread of rho over the window), D_mean, curled_share
(mean over the window) and the window's mean acceptance. Prints, per coupling, the mean rho_eq over replicas with
its standard error.

Config keys: name, section ("T76-settle"), L, lambda, couplings (a list), replicas, n_settle, window, n_ref, seed.
At lambda != 1 this is our family around the published model, not combinatorial quantum gravity.
"""
import json
import platform
import sys
from pathlib import Path

import numba
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
sys.path.insert(0, str(Path(__file__).resolve().parent))
from graphity import __version__                                                  # noqa: E402
from graphity.results import ResultWriter, provenance                             # noqa: E402
from graphity.row_growth import GrowthState, run_growth                           # noqa: E402
from analyse_t76 import rho_eq                                                    # noqa: E402

KEYS = ("name", "section", "L", "lambda", "couplings", "replicas", "n_settle", "window", "n_ref", "seed")


def settle(size, g, lam, n_settle, window, n_ref, seed):
    """One replica's settling run: a dict of the window's readings."""
    recs = run_growth(GrowthState.from_torus(int(size)), float(g), float(lam), int(n_settle), 0, 8, seed=seed,
                      n_ref=int(n_ref))
    win = [r for r in recs if r["phase"] == "settle" and r["fair_sweep"] > n_settle - window]
    return dict(rho_eq=rho_eq(recs, n_settle, window), rho_sd=float(np.std([r["rho"] for r in win])),
                D_mean=float(np.mean([r["D"] for r in win])),
                curled_share=float(np.mean([r["curled_share"] for r in win])),
                acceptance=float(np.mean([r["acceptance"] for r in win])))


def main(path, out_dir="results"):
    cfg = json.loads(Path(path).read_text(encoding="utf-8"))
    if cfg.get("section") != "T76-settle":
        raise ValueError("not a T76 settling config")
    missing = [k for k in KEYS if k not in cfg]
    if missing:
        raise ValueError("config lacks %s" % ", ".join(missing))
    if not 0 < int(cfg["window"]) <= int(cfg["n_settle"]):
        raise ValueError("the window must lie inside the settling")
    meta = dict(config=cfg, config_path=str(path), package=__version__, python=platform.python_version(),
                numpy=np.__version__, numba=numba.__version__, **provenance(),
                preregistration="PREREGISTRATION.md section T76 (the couplings' bisection)")
    summary = []
    with ResultWriter(cfg["name"], meta, out_dir) as out:
        for k, g in enumerate(cfg["couplings"]):
            vals = []
            for rep in range(int(cfg["replicas"])):
                row = settle(cfg["L"], g, cfg["lambda"], int(cfg["n_settle"]), int(cfg["window"]), cfg["n_ref"],
                             [int(cfg["seed"]), k, rep])
                out.write(dict(g=float(g), L=int(cfg["L"]), lam=float(cfg["lambda"]), replica=rep, **row))
                vals.append(row["rho_eq"])
            m = float(np.mean(vals))
            se = float(np.std(vals, ddof=1) / np.sqrt(len(vals))) if len(vals) > 1 else float("nan")
            summary.append(dict(g=float(g), rho_eq=m, se=se))
            print("g = %g: rho_eq = %.5f +- %.5f (%d replicas)" % (g, m, se, len(vals)), flush=True)
        meta["summary"] = summary


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else "results")

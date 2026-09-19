"""Cooling-then-heating sweep for the 2D CQG model. Usage:

    python scripts/run_cqg_sweep.py configs/cqg_first_look.json

Writes results/<name>.csv and .meta.json, and refuses to overwrite either (see
graphity/results.py). phi = S/N is the order parameter (1 on the flat torus, ~0
on a large random graph) [KTB19 Eq. (32), D = 2].

Optional config key "heat_start":
    "continue" (default)  the heating leg carries on from the cold end of the
                          cooling leg, whatever state that froze into.
    "torus"               the heating leg starts from a fresh flat torus, as in
                          the published protocol [T25 Fig. 3].

Columns phi_err and chi_err are block-bootstrap error bars and tau_int is the
autocorrelation time in sweeps (ASSUMPTION Q6). Do not trust the error bars of a
row whose tau_int is not far below n_meas / 20, or is NaN (frozen chain).
"""
import json
import platform
import sys
from pathlib import Path

import numba
import numpy as np

from graphity import __version__
from graphity.analysis import autocorr_time, block_bootstrap_mean_var
from graphity.cqg import is_valid, run_chain, torus
from graphity.results import ResultWriter


def main(path, out_dir="results"):
    cfg = json.loads(Path(path).read_text())
    heat_start = cfg.get("heat_start", "continue")
    if heat_start not in ("continue", "torus"):
        raise ValueError(f"heat_start must be 'continue' or 'torus', not {heat_start!r}")
    meta = dict(config=cfg, package=__version__, python=platform.python_version(),
                numpy=np.__version__, numba=numba.__version__)
    with ResultWriter(cfg["name"], meta, out_dir) as out:
        for side in cfg["sides"]:
            n = side * side
            for rep in range(cfg["replicas"]):
                seed = cfg["seed"] + 100000 * rep + side
                adj, part = torus(side)
                side_u = np.flatnonzero(part == 0)
                run_chain(adj, side_u, 0.0, cfg["n_melt"], 1, seed)          # hot start (Q5)
                gs = cfg["couplings"]
                if heat_start == "torus":
                    legs = [("cool", gs), ("heat", gs[::-1])]
                else:
                    legs = [("cool", gs), ("heat", gs[::-1][1:])]
                k = 0
                for leg, values in legs:
                    if leg == "heat" and heat_start == "torus":
                        assert is_valid(adj)                                 # check the cooled state before dropping it
                        adj, _ = torus(side)
                    for g in values:
                        k += 1
                        s, acc = run_chain(adj, side_u, 1.0 / g, cfg["n_equil"], cfg["n_meas"], seed + k)
                        phi = s / n
                        _, phi_err, _, var_err = block_bootstrap_mean_var(phi, seed=seed + k)
                        row = dict(N=n, replica=rep, leg=leg, g=g, phi=float(phi.mean()),
                                   phi_sd=float(phi.std()), chi=float(n * phi.var()),
                                   acceptance=float(acc), phi_err=phi_err,
                                   chi_err=n * var_err, tau_int=autocorr_time(phi))
                        out.write(row)
                        print(row, flush=True)
                assert is_valid(adj)


if __name__ == "__main__":
    main(sys.argv[1])

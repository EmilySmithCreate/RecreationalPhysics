"""Cooling-then-heating sweep for the 2D CQG model. Usage:

    python scripts/run_cqg_sweep.py configs/cqg_first_look.json

Writes results/<name>.csv and .meta.json. phi = S/N is the order parameter
(1 on the flat torus, ~0 on a large random graph) [KTB19 Eq. (32), D = 2].
"""
import csv
import json
import platform
import sys
from pathlib import Path

import numba
import numpy as np

from graphity import __version__
from graphity.cqg import is_valid, run_chain, torus


def main(path):
    cfg = json.loads(Path(path).read_text())
    rows = []
    for side in cfg["sides"]:
        n = side * side
        for rep in range(cfg["replicas"]):
            seed = cfg["seed"] + 100000 * rep + side
            adj, part = torus(side)
            side_u = np.flatnonzero(part == 0)
            run_chain(adj, side_u, 0.0, cfg["n_melt"], 1, seed)          # hot start (Q5)
            gs = cfg["couplings"]
            legs = [("cool", gs), ("heat", gs[::-1][1:])]
            k = 0
            for leg, values in legs:
                for g in values:
                    k += 1
                    s, acc = run_chain(adj, side_u, 1.0 / g, cfg["n_equil"], cfg["n_meas"], seed + k)
                    phi = s / n
                    rows.append(dict(N=n, replica=rep, leg=leg, g=g, phi=float(phi.mean()),
                                     phi_sd=float(phi.std()), chi=float(n * phi.var()),
                                     acceptance=float(acc)))
                    print(rows[-1], flush=True)
            assert is_valid(adj)
    out = Path("results") / f"{cfg['name']}.csv"
    out.parent.mkdir(exist_ok=True)
    with out.open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=rows[0].keys())
        w.writeheader()
        w.writerows(rows)
    meta = dict(config=cfg, package=__version__, python=platform.python_version(),
                numpy=np.__version__, numba=numba.__version__)
    out.with_suffix(".meta.json").write_text(json.dumps(meta, indent=2))


if __name__ == "__main__":
    main(sys.argv[1])

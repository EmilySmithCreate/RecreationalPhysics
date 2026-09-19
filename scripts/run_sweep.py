"""Temperature sweep driven by a JSON config. Usage:

    python scripts/run_sweep.py configs/konopka_r-2.5.json

Writes results/<name>.csv and results/<name>.meta.json (config, package
versions, seeds) so that every number can be regenerated.
"""
import csv
import json
import platform
import sys
from pathlib import Path

import networkx
import numba
import numpy as np

from graphity import __version__
from graphity.analysis import block_bootstrap
from graphity.energy import cycle_weights
from graphity.graphs import (menu_to_array, random_menu_with_planted_cubic,
                             random_regular_connected, to_adj,
                             torus_menu_with_cubic_start)
from graphity.mc import dummy_menu, run_chain


def build(cfg, n, seed):
    kind = cfg["menu"]["kind"]
    if kind == "complete":
        return to_adj(random_regular_connected(n, 3, seed), 3), dummy_menu(), False
    if kind == "random":
        menu, start = random_menu_with_planted_cubic(n, cfg["menu"]["k"], seed)
    elif kind == "torus":
        menu, start = torus_menu_with_cubic_start(cfg["menu"]["sides"])
    else:
        raise ValueError(kind)
    return to_adj(start, 3), menu_to_array(menu), True


def main(path):
    cfg = json.loads(Path(path).read_text())
    weights = cycle_weights(cfg["r"], cfg["l_max"], cfg.get("g_b", 1.0))
    out = Path("results") / f"{cfg['name']}.csv"
    out.parent.mkdir(exist_ok=True)
    rows = []
    for n in cfg["sizes"]:
        for rep in range(cfg["replicas"]):
            seed = cfg["seed"] + 1000 * rep + n
            adj, menu, use_menu = build(cfg, n, seed)
            if use_menu:   # scramble the constructed start state at infinite temperature
                run_chain(adj, menu, True, weights, 0.0, cfg["n_equil"], 1, seed)
            for i, beta in enumerate(cfg["betas"]):   # anneal: reuse state, hot -> cold
                energies, acc = run_chain(adj, menu, use_menu, weights, beta,
                                          cfg["n_equil"], cfg["n_meas"], seed + i + 1)
                e, de, c, dc = block_bootstrap(energies, beta, seed=seed)
                n_nodes = adj.shape[0]
                rows.append(dict(N=n_nodes, replica=rep, beta=beta,
                                 E_per_node=float(e / n_nodes), E_err=float(de / n_nodes),
                                 C_over_N2=float(c / n_nodes**2),
                                 C_err=float(dc / n_nodes**2), acceptance=float(acc)))
                print(rows[-1], flush=True)
    with out.open("w", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)
    meta = dict(config=cfg, package=__version__, python=platform.python_version(),
                numpy=np.__version__, numba=numba.__version__, networkx=networkx.__version__)
    out.with_suffix(".meta.json").write_text(json.dumps(meta, indent=2))


if __name__ == "__main__":
    main(sys.argv[1])

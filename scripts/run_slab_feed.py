"""T67: does the owner's untied slab open from a feed, energy arriving at a fixed rate? Usage:

    python scripts/run_slab_feed.py configs/t67_shared_cn_l8.json

Implements PREREGISTRATION.md section T67 (written 2026-10-16, after one sandbox look and before any registered run;
rule 11's fifth use on piece 5; VISION Updates 58 and 59; the owner's words "the rates may not be fixed but it's good
to run that way for starting"). The slab 4 x L x L with one direction curled, untied, lambda fixed, sealed with empty
stores; every `record_every` sweeps r * record_every units are added to the stores: mode "shared" into store 0 of a
shared bath of C stores (any move may draw it); mode "spot" into one point's own store with per-vertex stores (only
moves from that point spend it; the owner's "one spot per seed"). Each record writes the census (open = points at
local dimension 3, curled = at most 2, damaged = above 3), the number of separate open regions and the largest one,
the stores' mean, the energy fed so far and the drift. A replica stops at the first record with open >= 0.9 N (OPEN),
with damaged > 0.1 N (DAMAGED), or at `n_sweeps` (TIME). The final graph is saved when `save_adjacency` is set.

The chain is `graphity.sealed_tie_d.run_sealed_bath_table_d` with a table of zeros (untied), as T65 and T66. Energy
is conserved to the last bit and the drift, |H + stores - H0 - fed|, is written in every row. Seeds:
SeedSequence([seed, N, mode index, round(1000 r), replica]).
"""
import json
import platform
import sys
from pathlib import Path

import numba
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from graphity import __version__                                          # noqa: E402
from graphity.cqg_d import torus                                           # noqa: E402
from graphity.dimension import local_dimension_d, pieces_of                # noqa: E402
from graphity.results import ResultWriter, provenance                      # noqa: E402
from graphity.sealed_tie_d import energy_table_d, run_sealed_bath_table_d  # noqa: E402

OPEN_FRAC, DAMAGE_FRAC = 0.9, 0.1
MODES = ("shared", "spot")


def census(adj):
    d = local_dimension_d(adj)
    op = d == 3
    sizes = pieces_of(adj, op) if op.any() else []
    return dict(open=int(op.sum()), curled=int((d <= 2).sum()), damaged=int((d > 3).sum()),
                regions=len(sizes), largest=int(max(sizes)) if len(sizes) else 0)


def run_cell(dims, lam, rate, mode, c_bath, n_sweeps, every, seed):
    """One replica. Yields (sweep, census, store_mean, fed, drift, stop) with stop in {None, OPEN, DAMAGED, TIME};
    the last record carries the stop word. The feed for a block is added after the block has run."""
    adj, part = torus(dims)
    n = adj.shape[0]
    side_u = np.flatnonzero(part == 0)
    by_vertex = mode == "spot"
    ftab = np.zeros(len(dims) + 1)
    stores = np.zeros(n if by_vertex else c_bath)
    feed_idx = int(side_u[0]) if by_vertex else 0
    e0 = energy_table_d(adj, lam, ftab)
    fed = 0.0
    yield 0, census(adj), 0.0, 0.0, 0.0, None
    blocks = n_sweeps // every
    for b in range(blocks):
        run_sealed_bath_table_d(adj, side_u, stores, every, seed if b == 0 else -1, lam, ftab, by_vertex=by_vertex)
        stores[feed_idx] += rate * every
        fed += rate * every
        c = census(adj)
        drift = abs(energy_table_d(adj, lam, ftab) + stores.sum() - e0 - fed)
        stop = None
        if c["open"] >= OPEN_FRAC * n:
            stop = "OPEN"
        elif c["damaged"] > DAMAGE_FRAC * n:
            stop = "DAMAGED"
        elif b == blocks - 1:
            stop = "TIME"
        yield (b + 1) * every, c, float(stores.mean()), float(fed), float(drift), stop
        if stop:
            break
    run_cell.final = (adj, part)


def main(path, out_dir="results"):
    cfg = json.loads(Path(path).read_text())
    dims = [int(x) for x in cfg["dims"]]
    n = int(np.prod(dims))
    lam = float(cfg["lambda"])
    mode = cfg["mode"]
    assert mode in MODES
    c_bath = n if mode == "spot" else int(round(eval(str(cfg["capacity"]), {"N": n})))
    every, n_sweeps = int(cfg["record_every"]), int(cfg["n_sweeps"])
    label = "x".join(str(x) for x in dims)
    meta = dict(config=cfg, config_path=str(path), package=__version__, python=platform.python_version(),
                numpy=np.__version__, numba=numba.__version__, **provenance(),
                preregistration="PREREGISTRATION.md section %s, written 2026-10-16" % cfg.get("section", "T67"))
    adj_dir = Path(out_dir) / (cfg["name"] + "_adj")
    with ResultWriter(cfg["name"], meta, out_dir) as out:
        for rate in cfg["rates"]:
            for rep in range(int(cfg["replicas"])):
                seed = int(np.random.SeedSequence([int(cfg["seed"]), n, MODES.index(mode), int(round(1000 * float(rate))), rep]).generate_state(1)[0])
                for sweep, c, mean, fed, drift, stop in run_cell(dims, lam, float(rate), mode, c_bath, n_sweeps, every, seed):
                    out.write(dict(N=n, dims=label, lam=lam, mode=mode, C=c_bath, rate=float(rate), replica=rep, sweep=sweep,
                                   **c, store_mean=mean, fed=fed, drift=drift, stop=stop or ""))
                if cfg.get("save_adjacency"):
                    adj, part = run_cell.final
                    adj_dir.mkdir(parents=True, exist_ok=True)
                    np.savez(adj_dir / ("%s_C%d_r%g_rep%d.npz" % (mode, c_bath, float(rate), rep)), adj=adj, part=part, lam=lam)
                print("dims=%s mode=%s C=%d r=%g rep=%-2d stop=%s at %d | open %d curled %d damaged %d | regions %d largest %d | fed %.0f"
                      % (label, mode, c_bath, rate, rep, stop, sweep, c["open"], c["curled"], c["damaged"], c["regions"], c["largest"], fed), flush=True)
    print("wrote", Path(out_dir) / (cfg["name"] + ".csv"))


if __name__ == "__main__":
    main(sys.argv[1], *(sys.argv[2:3]))

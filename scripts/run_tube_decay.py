"""T7: watch a tube uncurl into a sheet, and look at it while it happens. Usage:

    python scripts/run_tube_decay.py configs/t7_lam125.json

Implements PREREGISTRATION.md section T7. Each replica starts from the exact tube (a torus with
one side of length 4), runs at fixed coupling, and is followed in short blocks. When the
conversion fraction first crosses 25 %, 50 % and 75 % the adjacency is read -- not copied, the
chain is simply paused -- and three things are recorded: the histogram of the local dimension
d(v) over vertices, the connected pieces of the vertices that already read as sheet (d = 2),
and the sweep. The waiting time is the pre-registered one: the first sweep at which phi has
left the tube's value by more than three times its own resting fluctuation. The energy
released is checked against the exact 4(lambda - 1).

Conversion fraction: f = (phi_tube - phi) / (phi_tube - phi_sheet), with phi_tube = 1.25 (one
curled side adds a quarter of a square per vertex) and phi_sheet = 1.

The chain is advanced with seed < 0 after the first block, which carries the random stream on
rather than re-seeding (ASSUMPTIONS Q14). Looking at the graph between blocks uses no random
numbers, so the chain is the same as if it had run uninterrupted.
"""
import json
import platform
import sys
from pathlib import Path

import numba
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from graphity import __version__                                           # noqa: E402
from graphity.cqg import (ENERGY_PER_SQUARE, ENERGY_PER_SURPLUS, NO_CAP,     # noqa: E402
                          run_chain, surplus, torus, total_squares)
from graphity.dimension import local_dimension, pieces_of                  # noqa: E402
from graphity.results import ResultWriter                                  # noqa: E402

PHI_TUBE, PHI_SHEET = 1.25, 1.0
MARKS = (0.25, 0.50, 0.75)
D_BINS = 7                     # d(v) runs 0..6


def snapshot(adj):
    d = local_dimension(adj)
    hist = np.bincount(d, minlength=D_BINS)[:D_BINS]
    pieces = pieces_of(adj, d == 2)
    converted = int((d == 2).sum())
    return hist, len(pieces), (pieces[0] / converted if converted else 0.0), converted


def main(path, out_dir="results"):
    cfg = json.loads(Path(path).read_text())
    lam = float(cfg["lambda"])
    g = float(cfg["g"])
    block = int(cfg.get("block", 5))
    n_sweeps = int(cfg["n_sweeps"])
    stop_at = float(cfg.get("stop_at", 0.98))
    settle = int(cfg.get("settle", 300))     # sweeps to average the final energy over
    meta = dict(config=cfg, config_path=str(path), package=__version__,
                python=platform.python_version(), numpy=np.__version__, numba=numba.__version__,
                preregistration="PREREGISTRATION.md section T7, written 2026-09-22")
    with ResultWriter(cfg["name"], meta, out_dir) as out:
        for lx, ly in cfg["sides"]:
            n = lx * ly
            for rep in range(int(cfg["replicas"])):
                adj, part = torus(lx, ly, NO_CAP)
                side_u = np.flatnonzero(part == 0)
                seed = int(np.random.SeedSequence([int(cfg["seed"]), lx, ly, rep]).generate_state(1)[0])
                h0 = (ENERGY_PER_SQUARE * (n - total_squares(adj))
                      + ENERGY_PER_SURPLUS * lam * surplus(adj)) / n
                phis, sweeps_done, first = [], 0, True
                hit = {}
                waited = None
                thresh = None
                while sweeps_done < n_sweeps:
                    s, x, _ = run_chain(adj, side_u, 1.0 / g, 0, block, seed if first else -1,
                                        lam, NO_CAP, False)
                    first = False
                    sweeps_done += block
                    phi = float(s[-1]) / n
                    phis.append(phi)
                    if sweeps_done <= 200:
                        continue
                    if thresh is None:
                        rest = np.array(phis[: max(1, 200 // block)])
                        thresh = PHI_TUBE - 3.0 * max(rest.std(), 1e-6) - 1e-9
                    if waited is None and phi < thresh:
                        waited = sweeps_done
                    f = (PHI_TUBE - phi) / (PHI_TUBE - PHI_SHEET)
                    for m in MARKS:
                        if m not in hit and f >= m:
                            hit[m] = (sweeps_done,) + snapshot(adj)
                    if f >= stop_at:
                        break
                # T7 amendment 1: settle until the released energy has stopped changing. The
                # first runs settled for a fixed 300 sweeps and caught half the decays on a ledge
                # -- a defected sheet holding 0.22 per point -- which then released the rest in
                # one step hundreds to thousands of sweeps later. So the energy is read in windows
                # of `settle` sweeps and accepted when two consecutive windows agree to 0.5 % of
                # 4(lambda - 1), up to `settle_max` sweeps. The ledge is recorded: the released
                # energy after the first window, and how long the plateau lasted.
                settle_max = int(cfg.get("settle_max", 20000))
                windows, spent = [], 0
                while spent < settle_max:
                    hs = []
                    for _ in range(max(1, settle // block)):
                        s, x, _ = run_chain(adj, side_u, 1.0 / g, 0, block, -1, lam, NO_CAP, False)
                        hs.append((ENERGY_PER_SQUARE * (n - s[-1]) + ENERGY_PER_SURPLUS * lam * x[-1]) / n)
                    spent += max(1, settle // block) * block
                    windows.append(h0 - float(np.mean(hs)))
                    if len(windows) >= 2 and abs(windows[-1] - windows[-2]) <= 0.005 * 4.0 * (lam - 1.0)                             and abs(windows[-1] - 4.0 * (lam - 1.0)) <= 0.01 * 4.0 * (lam - 1.0):
                        break
                sweeps_done += spent
                h1 = h0 - windows[-1]
                first_window = windows[0]
                ledge = sum(1 for w in windows[:-1] if abs(w - windows[-1]) > 0.05 * 4.0 * (lam - 1.0)) * settle
                row = dict(N=n, lx=lx, ly=ly, replica=rep, lam=lam, g=g, seed=seed,
                           sweeps=sweeps_done, waiting=(waited if waited is not None else ""),
                           phi_final=phis[-1], released=(h0 - h1), expected=4.0 * (lam - 1.0),
                           released_first_window=first_window, ledge_sweeps=ledge, settle_sweeps=spent,
                           reached=max([0.0] + [m for m in hit]))
                for m in MARKS:
                    tag = "%d" % int(100 * m)
                    if m in hit:
                        sw, hist, npieces, largest, conv = hit[m]
                        row["sweep_" + tag] = sw
                        row["pieces_" + tag] = npieces
                        row["largest_" + tag] = largest
                        row["converted_" + tag] = conv
                        for k in range(D_BINS):
                            row["d%d_%s" % (k, tag)] = int(hist[k])
                    else:
                        row["sweep_" + tag] = ""
                        row["pieces_" + tag] = ""
                        row["largest_" + tag] = ""
                        row["converted_" + tag] = ""
                        for k in range(D_BINS):
                            row["d%d_%s" % (k, tag)] = ""
                out.write(row)
                print("N=%-4d rep=%-3d waited=%-6s reached=%.2f  released=%.4f (expect %.4f)%s"
                      % (n, rep, waited, row["reached"], h0 - h1, 4 * (lam - 1),
                         ("  at 50%%: d-hist %s, %d pieces, largest %.2f"
                          % ([int(v) for v in hit[0.5][1]], hit[0.5][2], hit[0.5][3])) if 0.5 in hit else ""),
                      flush=True)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else "results")

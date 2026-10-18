"""Second pass of which_side_curls.py: colder, and stopped at the first block in which the sheet has become a tube
(at least 90 % of points at d = 1 and at most 2 at d = 0), so that the readout sees one curl and not the knots."""
import sys
import numpy as np
sys.path.insert(0, "src"); sys.path.insert(0, "sandbox")
from graphity.cqg import torus, run_chain, NO_CAP  # noqa: E402
from graphity.dimension import local_dimension    # noqa: E402
from which_side_curls import axis_links, survival  # noqa: E402  (importing runs nothing: the module's loop is guarded below)
lam, sweeps, every = 0.5, 40000, 100
print("g | lx x ly | rep | stopped at sweep | d-census | surviving links along x (len lx) , y (len ly) | re-threaded axis")
for g in (2.0, 2.5):
    for lx, ly in ((6, 16), (16, 6), (8, 12), (12, 8)):
        links = axis_links(lx, ly)
        for rep in range(6):
            adj, part = torus(lx, ly, cap=NO_CAP)
            side_u = np.flatnonzero(part == 0)
            seed = int(np.random.SeedSequence([20261016, 2, lx, ly, rep, int(g * 10)]).generate_state(1)[0])
            stopped = None
            for b in range(sweeps // every):
                run_chain(adj, side_u, 1.0 / g, 0, every, seed if b == 0 else seed + b + 1, lam=lam, cap=NO_CAP)
                d = local_dimension(adj)
                if (d == 1).sum() >= 0.9 * adj.shape[0] and (d == 0).sum() <= 2:
                    stopped = (b + 1) * every; break
            d = local_dimension(adj)
            sx, sy = survival(adj, links)
            which = "x (len %d)" % lx if sx < sy - 0.05 else "y (len %d)" % ly if sy < sx - 0.05 else "neither clearly"
            print(f"{g} | {lx:2d} x {ly:2d} | {rep} | {stopped if stopped else 'never a tube'} | {[int((d == k).sum()) for k in range(3)]} | {sx:.2f} , {sy:.2f} | {which}", flush=True)

"""Sandbox look, 16 October 2026 (rule 16). The owner: with unequal sides the directions are not interchangeable at
large scale; "first curl will be the 6 dropping to 4", the shortest side. In the toy the energy and the moves are local
and cannot see a side's length, so nothing in the energy picks the 6; whether the dynamics does is the question.
Two-direction rehearsal (configs/cqg_sheet_decay_lam050: at lambda = 0.5 the flat sheet gives way to a tube, which
lies 2 per point lower): flat 6 x 16 and 8 x 12 tori (96 points), lambda 0.5, g = 3.0, 20,000 sweeps, 8 replicas.
Readout at the end: the share of each axis's original links that survive (the axis that curled was re-threaded, so
its links are the ones replaced), the d census (2 flat, 1 tube, 0 cube), and H per point. Axes swapped as a control.
"""
import sys
import numpy as np
sys.path.insert(0, "src")
from graphity.cqg import torus, run_chain, NO_CAP  # noqa: E402
from graphity.dimension import local_dimension                    # noqa: E402

def axis_links(lx, ly):
    """{(u,v): axis} for the original torus, axis 0 along x (length lx), 1 along y (length ly)."""
    out = {}
    for x in range(lx):
        for y in range(ly):
            i = x * ly + y
            out[frozenset((i, ((x + 1) % lx) * ly + y))] = 0
            out[frozenset((i, x * ly + (y + 1) % ly))] = 1
    return out

def survival(adj, links):
    have = {frozenset((u, int(v))) for u in range(adj.shape[0]) for v in adj[u]}
    keep = [0, 0]; tot = [0, 0]
    for e, a in links.items():
        tot[a] += 1; keep[a] += e in have
    return keep[0] / tot[0], keep[1] / tot[1]

if __name__ == "__main__":
  lam, g, sweeps = 0.5, 3.0, 20000
  print("lx x ly | rep | end d-census (d0,d1,d2) | surviving links along x (len lx) , along y (len ly) | which axis re-threaded")
  for lx, ly in ((6, 16), (16, 6), (8, 12), (12, 8)):
      links = axis_links(lx, ly)
      for rep in range(8):
          adj, part = torus(lx, ly, cap=NO_CAP)
          side_u = np.flatnonzero(part == 0)
          seed = int(np.random.SeedSequence([20261016, lx, ly, rep]).generate_state(1)[0])
          run_chain(adj, side_u, 1.0 / g, 0, sweeps, seed, lam=lam, cap=NO_CAP)
          d = local_dimension(adj)
          sx, sy = survival(adj, links)
          which = "x (len %d)" % lx if sx < sy - 0.05 else "y (len %d)" % ly if sy < sx - 0.05 else "neither clearly"
          print(f"{lx:2d} x {ly:2d} | {rep} | {[int((d == k).sum()) for k in range(3)]} | {sx:.2f} , {sy:.2f} | {which}", flush=True)

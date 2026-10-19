"""Sandbox look, 18 October 2026: the owner's spiral. A layer contraction of flat 6 x L x L with the splice SHIFTED
along a transverse direction (x = -1 at (y, z) linked to x = 2 at (y + s, z)), so the curled direction's seam runs as a
spiral: s/L turns per circuit. Reports N, S, X, H, the d census and validity for each even shift s. Exact; a look."""
import sys
import numpy as np
sys.path.insert(0, "src"); sys.path.insert(0, "sandbox")
from graphity.cqg_d import torus                                                   # noqa: E402
from pair_moves import from_sets, to_sets                                        # noqa: E402
from partial_contraction import census                                           # noqa: E402

def shifted_layer_contraction(dims, s, lam):
    Lx, Ly, Lz = dims
    adj, part = torus(dims)
    idx = lambda x, y, z: int(np.ravel_multi_index((x % Lx, y % Ly, z % Lz), dims))  # noqa: E731
    nb = to_sets(adj); removed = set()
    for y in range(Ly):
        for z in range(Lz):
            u, v = idx(0, y, z), idx(1, y, z); removed.update((u, v))
            a, b = idx(Lx - 1, y, z), idx(2, (y + s) % Ly, z)
            nb[a].discard(u); nb[b].discard(v)
            if b in nb[a]:
                return None
            nb[a].add(b); nb[b].add(a)
    for i in removed:
        nb[i] = None
    for i, sset in enumerate(nb):
        if sset is not None:
            sset.difference_update(removed)
            if len(sset) != 6:
                return None
    new, keep = from_sets(nb)
    return census(new, lam)

if __name__ == "__main__":
    lam = 1.25
    for L in (6, 8):
        for s in range(0, L, 2):
            c = shifted_layer_contraction((6, L, L), s, lam)
            print("6x%dx%d -> 4x%dx%d with shift %d (%.2f turns per circuit): %s" % (L, L, L, L, s, s / L, c))

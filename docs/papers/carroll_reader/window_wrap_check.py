"""Check for the draft in this folder, made after T91's held-out reading and not registered. Exact.

Run from the repository root:
    PYTHONPATH="src;scripts" python docs/papers/carroll_reader/window_wrap_check.py      (Windows; ":" elsewhere)

A ball of graph radius 10 on the 32 x 32 torus holds vertex pairs up to 20 apart along one axis, more than half of 32,
so some full-graph shortest paths between its vertices wrap round the torus. The same window is read on a 64 x 64
torus, where no path inside it wraps, with T91's own functions (scripts/carroll_reader.py). The curled torus is read
at 4 x 64 (T91's size) and 4 x 128 as a control. Not part of the record; to be entered in it before the draft is shared.
"""
import numpy as np

from carroll_reader import d_mds, graph_of, mds_spectrum, window
from graphity.cqg import NO_CAP, torus


def main():
    for lx, ly, radii in ((32, 32, (6, 10)), (64, 64, (6, 10)), (4, 64, (10,)), (4, 128, (10,))):
        g = graph_of(torus(lx, ly, NO_CAP)[0])
        for r in radii:
            pts, dist = window(g, 0, r)
            w = mds_spectrum(dist)
            print(f"{lx} x {ly}, R = {r}: {len(pts)} points, eigenvalues / largest {np.round(w[:5] / w[0], 3)}, "
                  f"D_MDS = {d_mds(w)}")


if __name__ == "__main__":
    main()

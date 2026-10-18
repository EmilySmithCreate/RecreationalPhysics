"""Sandbox look, 18 October 2026: which two-switch moves leave no point broken, from flat space and from the slab?

The owner asked whether the reshaping of a flat torus toward the slab can proceed through states with no broken point.
First question on the way: does flat six-link space have ANY clean compound move (two switches, no point left at d > 3)?
Exhaustive over all pairs (first switch with both side-0 ends within `near` of one point; second switch with both
side-0 ends within `near` of the first's endpoints). Reports the clean moves by (dS, dX, dH, census of d). A look.
"""
import sys
from collections import Counter

import numpy as np

sys.path.insert(0, "src")
sys.path.insert(0, "scripts")
from graphity.cqg_d import _switch, is_valid, surplus, torus, total_squares   # noqa: E402
from graphity.dimension import local_dimension_d                              # noqa: E402
from exact_lowest_path import expand, ball                                    # noqa: E402


def census(spec, lam, near=2):
    adj, part = torus(spec)
    n = adj.shape[0]
    s0, x0 = total_squares(adj), surplus(adj)
    side0 = np.flatnonzero(part == 0)
    u1 = int(side0[0])
    w1 = np.array(sorted(v for v in ball(adj, [u1], near) if part[v] == 0), dtype=np.int64)
    a1, b1, c1, d1, _ = expand(adj.copy(), w1, lam)
    # keep only switches that involve u1 (every switch class is seen from u1 by translation symmetry)
    keep = (a1 == u1) | (c1 == u1)
    firsts = list(zip(a1[keep], b1[keep], c1[keep], d1[keep]))
    kinds = Counter(); tried = 0; valid_pairs = 0
    for (u, v, uu, vv) in firsts:
        t = adj.copy(); _switch(t, u, v, uu, vv)
        if not is_valid(t):
            continue
        w2 = np.array(sorted(p for p in ball(t, [u, v, uu, vv], near) if part[p] == 0), dtype=np.int64)
        a2, b2, c2, d2, _ = expand(t.copy(), w2, lam)
        for (p, q, pp, qq) in zip(a2, b2, c2, d2):
            tried += 1
            t2 = t.copy(); _switch(t2, p, q, pp, qq)
            if not is_valid(t2):
                continue
            valid_pairs += 1
            d = local_dimension_d(t2)
            if d.max() > 3:
                continue
            ds, dx = total_squares(t2) - s0, surplus(t2) - x0
            cen = tuple(sorted(Counter(d.tolist()).items()))
            kinds[(ds, dx, round(-16.0 * ds + 4 * lam * dx, 2), cen)] += 1
    print("%s N=%d lambda=%.2f: first switches through u1 %d, pairs tried %d, valid %d, CLEAN pairs %d"
          % ("x".join(map(str, spec)), n, lam, len(firsts), tried, valid_pairs, sum(kinds.values())))
    for (ds, dx, dh, cen), k in sorted(kinds.items(), key=lambda kv: kv[0][2]):
        print("   dS %3d dX %3d dH %7.1f  d-census %s  ways %d" % (ds, dx, dh, dict(cen), k))


if __name__ == "__main__":
    census((6, 6, 6), 1.25)
    census((6, 6, 8), 1.25)
    census((4, 6, 6), 1.25)

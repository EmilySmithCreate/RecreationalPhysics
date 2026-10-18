"""Sandbox look, 18 October 2026: a PART of a layer contracted (the owner's compaction move done patch by patch).

`sandbox/pair_moves.py` showed that contracting a whole layer pair of flat 6 x L x L (every (x = 0, x = 1) pair at
once, x = -1 spliced to x = 2) is exactly the slab 4 x L x L with no point broken, while contracting ONE pair leaves
about 24 points broken whichever of the 120 splicings is used. This script asks what lies between: a patch P of
transverse positions is contracted (the pairs (0, p), (1, p) for p in P removed, (-1, p) spliced to (2, p)), and the
points on the patch's rim in layers 0 and 1, which each lose a link into the patch, are re-linked across the rim.
Every re-linking that keeps the graph simple and bipartite is tried for small patches (brute force over the matchings
of rim stubs that respect the two sides), and the one leaving the fewest broken points (d > 3) is reported, with its
energy. Read backwards, the same states are the slab PARTLY SPLIT back toward flat space, so this is the barrier shape
of the contraction model's opening, the counterpart of T54 for switches. Exact within what it tries; a look (rule 16).
"""
import itertools
import sys
import time
from collections import Counter

import numpy as np

sys.path.insert(0, "src")
from graphity.cqg_d import hamiltonian, is_valid, surplus, torus, total_squares   # noqa: E402
from graphity.dimension import local_dimension_d                                # noqa: E402

sys.path.insert(0, "sandbox")
from pair_moves import from_sets, to_sets                                       # noqa: E402


def census(adj, lam):
    d = local_dimension_d(adj)
    return dict(N=adj.shape[0], S=int(total_squares(adj)), X=int(surplus(adj)), H=hamiltonian(adj, lam),
                d=dict(sorted(Counter(d.tolist()).items())), valid=bool(is_valid(adj)))


def contract_patch(adj, part, dims, patch, matching):
    """Contract the pairs at transverse positions `patch` (set of (y, z)); re-link rim stubs by `matching`, a list of
    ((0, q), (1, q')) position pairs. Returns (adj, part) or None if a duplicate link would arise."""
    Lx, Ly, Lz = dims
    idx = lambda x, y, z: int(np.ravel_multi_index((x % Lx, y % Ly, z % Lz), dims))   # noqa: E731
    nb = to_sets(adj)
    removed = set()
    for (y, z) in patch:
        u, v = idx(0, y, z), idx(1, y, z)
        removed.update((u, v))
        a, b = idx(Lx - 1, y, z), idx(2, y, z)
        nb[a].discard(u); nb[b].discard(v)
        if b in nb[a]:
            return None
        nb[a].add(b); nb[b].add(a)
    for (q0, q1) in matching:
        a = idx(0, *q0); b = idx(1, *q1)
        if a in removed or b in removed or b in nb[a]:
            return None
        nb[a].add(b); nb[b].add(a)
    for i in removed:
        nb[i] = None
    # every survivor must end with exactly deg links
    deg = adj.shape[1]
    for i, s in enumerate(nb):
        if s is not None:
            s.difference_update(removed)
            if len(s) != deg:
                return None
    new, keep = from_sets(nb)
    return new, np.array([part[k] for k in keep], dtype=np.int64)


def rim_stubs(dims, patch):
    """Multiset of rim positions q (not in patch) by the number of patch neighbours they have, transverse only."""
    _, Ly, Lz = dims
    stubs = Counter()
    for (y, z) in patch:
        for dy, dz in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            q = ((y + dy) % Ly, (z + dz) % Lz)
            if q not in patch:
                stubs[q] += 1
    return stubs


def parity(q):
    return (q[0] + q[1]) % 2


def best_contraction(dims, patch, lam, limit=None):
    """Try every side-respecting matching of rim stubs (layer 0 stubs at q to layer 1 stubs at q' with the same
    transverse parity, q != q'); keep the valid state with the fewest broken points, then the lowest energy."""
    adj, part = torus(dims)
    base = census(adj, lam)
    stubs = rim_stubs(dims, patch)
    stubs0 = sorted(stubs.elements())                       # layer-0 stubs, one entry per lost link
    classes = {}
    for q in stubs0:
        classes.setdefault(parity(q), []).append(q)
    # layer-1 stubs are the same multiset; a link (0,q)-(1,q') needs parity(q) == parity(q')
    perms_by_class = [itertools.permutations(cls) for cls in classes.values()]
    tried = valid = 0
    best = None
    t0 = time.time()
    for combo in itertools.product(*perms_by_class):
        tried += 1
        matching = []
        ok = True
        for cls, perm in zip(classes.values(), combo):
            for q0, q1 in zip(cls, perm):
                if q0 == q1:
                    ok = False
                    break
                matching.append((q0, q1))
            if not ok:
                break
        if not ok:
            continue
        res = contract_patch(adj, part, dims, patch, matching)
        if res is None:
            continue
        new, _ = res
        if not is_valid(new):
            continue
        valid += 1
        c = census(new, lam)
        broken = sum(n for d, n in c["d"].items() if d > 3)
        key = (broken, c["H"])
        if best is None or key < best[0]:
            best = (key, c, matching)
        if limit and tried >= limit:
            break
    dt = time.time() - t0
    return base, best, tried, valid, dt


def canonical_strip(dims, y0, width, lam):
    """A strip of `width` rows spanning every z, rim rows y0-1 and y0+width re-linked within the row by z -> z + 2."""
    _, Ly, Lz = dims
    patch = {(y, z) for y in range(y0, y0 + width) for z in range(Lz)}
    adj, part = torus(dims)
    base = census(adj, lam)
    best = None
    for shift in range(2, Lz, 2):
        for cross in (False, True):
            matching = []
            rows = ((y0 - 1) % Ly, (y0 + width) % Ly)
            for r_i, r in enumerate(rows):
                r_other = rows[1 - r_i] if cross else r
                for z in range(Lz):
                    matching.append(((r, z), (r_other, (z + shift) % Lz)))
            res = contract_patch(adj, part, dims, patch, matching)
            if res is None:
                continue
            new, _ = res
            if not is_valid(new):
                continue
            c = census(new, lam)
            broken = sum(n for d, n in c["d"].items() if d > 3)
            key = (broken, c["H"])
            if best is None or key < best[0]:
                best = (key, c, ("shift", shift, "cross", cross))
    return base, best, len(patch)


def report(label, k, base, best, tried, valid, dt):
    if best is None:
        print("%-12s k=%2d  tried %7d  valid %5d  (%.0fs)  NO VALID RE-LINKING" % (label, k, tried, valid, dt))
        return
    (broken, H), c, _ = best
    print("%-12s k=%2d  tried %7d  valid %5d  (%.0fs)  best: broken %3d  dH %7.1f  dS %4d  dX %3d  d %s"
          % (label, k, tried, valid, dt, broken, c["H"] - base["H"], c["S"] - base["S"], c["X"] - base["X"], c["d"]))


if __name__ == "__main__":
    lam = float(sys.argv[1]) if len(sys.argv) > 1 else 1.25
    L = int(sys.argv[2]) if len(sys.argv) > 2 else 6
    dims = (6, L, L)
    print("flat %s contracted patch by patch along x; lambda = %.2f; slab 4x%dx%d sits at dH = %.1f with no point broken"
          % ("x".join(map(str, dims)), lam, L, L, 4 * (lam - 1) * 4 * L * L))
    blocks = {"1x1": {(0, 0)}, "1x2": {(0, 0), (0, 1)}, "2x2": {(0, 0), (0, 1), (1, 0), (1, 1)},
              "2x3": {(y, z) for y in range(2) for z in range(3)}}
    if "--big" in sys.argv:
        blocks["3x3"] = {(y, z) for y in range(3) for z in range(3)}
    for label, patch in blocks.items():
        base, best, tried, valid, dt = best_contraction(dims, patch, lam)
        report("block " + label, len(patch), base, best, tried, valid, dt)
    for width in (1, 2, 3, 4):
        base, best, k = canonical_strip(dims, 0, width, lam)
        report("strip w=%d" % width, k, base, best, 0, 0 if best is None else 1, 0.0)
    # the whole layer, as a check against pair_moves.py
    patch = {(y, z) for y in range(L) for z in range(L)}
    base, best, tried, valid, dt = best_contraction(dims, patch, lam)
    report("whole layer", len(patch), base, best, tried, valid, dt)

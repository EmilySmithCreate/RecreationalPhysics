"""Sandbox look, 18 October 2026: the owner's compaction move, made exact.

Her words: two points whose link shrinks to nothing collapse into themselves, and the points that were linked to them
now link to each other. In the six-link toy that is a PAIR REMOVAL: a linked pair u (side 0), v (side 1) vanishes, and
u's five other neighbours (all side 1) are spliced to v's five other neighbours (all side 0) one to one. Every surviving
point keeps six links, both sides stay separate, and the count falls by two. Its inverse is a PAIR INSERTION: five links
a_i-b_i are cut, a new u is linked to the five b_i and a new v to the five a_i, and u to v; the count rises by two.
The whole-layer version removes every pair (x = 0, x = 1) at once, which takes a direction from six around to four.

This script (a) builds the layer contraction and checks it is the slab; (b) for one local pair removal lists every one
of the 120 splicings and keeps the valid ones (simple graph, hard-core rule), reporting the energy change and how many
points are left broken (d > 3), from flat 6 x 6 x 6 and from the slab 4 x 6 x 6. Exact; a look (rule 16).
"""
import itertools
import sys
from collections import Counter

import numpy as np

sys.path.insert(0, "src")
from graphity.cqg_d import codegree, hamiltonian, is_valid, surplus, torus, total_squares   # noqa: E402
from graphity.dimension import local_dimension_d                                        # noqa: E402


def to_sets(adj):
    return [set(int(x) for x in row) for row in adj]


def from_sets(nb):
    keep = [i for i, s in enumerate(nb) if s is not None]
    idx = {old: new for new, old in enumerate(keep)}
    deg = len(nb[keep[0]])
    out = np.empty((len(keep), deg), dtype=np.int64)
    for new, old in enumerate(keep):
        s = sorted(idx[w] for w in nb[old])
        assert len(s) == deg, (old, len(s))
        out[new] = s
    return out, keep


def pair_removal(adj, part, u, v, pairing):
    """Remove linked u (side 0) and v (side 1); splice u's other neighbours to v's by `pairing` (list of (a, b))."""
    nb = to_sets(adj)
    assert v in nb[u] and part[u] == 0 and part[v] == 1
    for a, b in pairing:
        if b in nb[a]:
            return None            # duplicate link
        nb[a].discard(u); nb[b].discard(v); nb[a].add(b); nb[b].add(a)
    nb[u] = None; nb[v] = None
    new, keep = from_sets(nb)
    newpart = np.array([part[k] for k in keep], dtype=np.int64)
    return new, newpart


def layer_contraction(adj, part, dims, axis=0):
    """Remove the layers x = 0 and x = 1 along `axis`; splice x = -1 to x = 2 at every transverse position."""
    coords = np.array(np.unravel_index(np.arange(adj.shape[0]), dims)).T
    nb = to_sets(adj)
    L = dims[axis]
    removed = []
    for i, c in enumerate(coords):
        if c[axis] in (0, 1):
            removed.append(i)
    for i in removed:
        c = coords[i]
        if c[axis] != 0:
            continue
        j = i + int(np.prod(dims[axis + 1:]))          # the point at x = 1 with the same transverse position
        cm = c.copy(); cm[axis] = (L - 1) % L
        cp = c.copy(); cp[axis] = 2 % L
        a = int(np.ravel_multi_index(cm, dims)); b = int(np.ravel_multi_index(cp, dims))
        nb[a].discard(i); nb[b].discard(j); nb[a].add(b); nb[b].add(a)
    for i in removed:
        nb[i] = None
    new, keep = from_sets(nb)
    return new, np.array([part[k] for k in keep], dtype=np.int64)


def census(adj, lam):
    d = local_dimension_d(adj)
    return dict(N=adj.shape[0], S=int(total_squares(adj)), X=int(surplus(adj)), H=hamiltonian(adj, lam),
                d=dict(sorted(Counter(d.tolist()).items())), valid=bool(is_valid(adj)))


def local_removal_census(spec, lam):
    adj, part = torus(spec)
    base = census(adj, lam)
    u = int(np.flatnonzero(part == 0)[0]); v = int(adj[u, 0])
    A = [int(x) for x in adj[u] if x != v]; B = [int(x) for x in adj[v] if x != u]
    kinds = Counter(); n_valid = 0
    for perm in itertools.permutations(B):
        res = pair_removal(adj, part, u, v, list(zip(A, perm)))
        if res is None:
            continue
        new, newpart = res
        if not is_valid(new):
            continue
        n_valid += 1
        c = census(new, lam)
        kinds[(round(c["H"] - base["H"], 2), c["S"] - base["S"], c["X"] - base["X"], tuple(sorted(c["d"].items())))] += 1
    print("%s: one pair removed (N %d -> %d); %d of 120 splicings valid" % ("x".join(map(str, spec)), base["N"], base["N"] - 2, n_valid))
    for (dh, ds, dx, dcen), k in sorted(kinds.items()):
        print("   dH %7.1f  dS %3d  dX %3d  d-census %s  ways %d" % (dh, ds, dx, dict(dcen), k))


if __name__ == "__main__":
    lam = 1.25
    for spec in ((6, 6, 6), (6, 6, 8)):
        adj, part = torus(spec)
        new, newpart = layer_contraction(adj, part, spec, axis=0)
        target, _ = torus((spec[0] - 2,) + spec[1:])
        print("layer contraction %s -> %s: %s ; built slab: %s" % ("x".join(map(str, spec)), "x".join(map(str, (spec[0] - 2,) + spec[1:])), census(new, lam), census(target, lam)))
    for spec in ((6, 6, 6), (4, 6, 6)):
        local_removal_census(spec, lam)

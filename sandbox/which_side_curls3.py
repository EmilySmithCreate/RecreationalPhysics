"""Third pass: in the tube the sheet curls into, which original axis do the tube's ring links come from? In a 4 x L
tube every ring link lies on three squares and every along-tube link on two (O16's reading), so the ring links of
the product are the links on three squares at the stop. Each is an original x link, an original y link, or new.
If the short side (6) became the rings, the ring links are mostly original x links of the 6 x 16 torus."""
import sys
import numpy as np
sys.path.insert(0, "src"); sys.path.insert(0, "sandbox")
from graphity.cqg import torus, run_chain, NO_CAP, squares_on_edge  # noqa: E402
from graphity.dimension import local_dimension                     # noqa: E402
from which_side_curls import axis_links                            # noqa: E402

def ring_links_by_origin(adj, links):
    counts = {"x": 0, "y": 0, "new": 0}
    for u in range(adj.shape[0]):
        for v in adj[u]:
            v = int(v)
            if v > u and squares_on_edge(adj, u, v) == 3:
                a = links.get(frozenset((u, v)))
                counts["x" if a == 0 else "y" if a == 1 else "new"] += 1
    return counts

lam, g, sweeps, every = 0.5, 2.5, 20000, 100
print("lx x ly | rep | tube at sweep | ring links from: original x (len lx), original y (len ly), new")
for lx, ly in ((6, 16), (16, 6), (6, 24), (24, 6)):
    links = axis_links(lx, ly)
    for rep in range(8):
        adj, part = torus(lx, ly, cap=NO_CAP)
        side_u = np.flatnonzero(part == 0)
        seed = int(np.random.SeedSequence([20261016, 3, lx, ly, rep]).generate_state(1)[0])
        stopped = None
        for b in range(sweeps // every):
            run_chain(adj, side_u, 1.0 / g, 0, every, seed + b, lam=lam, cap=NO_CAP)
            d = local_dimension(adj)
            if (d == 1).sum() >= 0.9 * adj.shape[0] and (d == 0).sum() <= 2:
                stopped = (b + 1) * every; break
        c = ring_links_by_origin(adj, links)
        print(f"{lx:2d} x {ly:2d} | {rep} | {stopped if stopped else 'no tube by %d' % sweeps} | x {c['x']:3d}, y {c['y']:3d}, new {c['new']:3d}", flush=True)

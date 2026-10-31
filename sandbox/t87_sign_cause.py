"""A look (sandbox lane; T87 stage 1 came out SIGNED at r = 2 where we predicted MIRROR). Two checks of the test's own
logic, expectations first: (1) on a perfect 4 x 12 tube, hand-built, a ring of four must be MIRROR at every radius under
the registered test (the reflection of the ring direction fixes two opposite points and preserves sides); if it is not,
the test is wrong. (2) For the SIGNED columns of the N = 144 and N = 512 states, is there a reversal that SWAPS sides
((a, b, c, d) -> (b, a, d, c) or (d, c, b, a)), which the registered test does not count? If most SIGNED columns have a
side-swapping mirror, the sign the test found is the bipartition's (the two sides are distinguishable in the toy, Q15),
not the loop's; if not, the column's surroundings are chiral under every reflection.
Expectation (ours): (1) MIRROR; (2) most SIGNED columns have a side-swapping mirror. Crowns nothing.
"""
import sys
from glob import glob
from pathlib import Path

import networkx as nx
import numpy as np
from networkx.algorithms import isomorphism

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
sys.path.insert(0, str(ROOT / "src"))
from t87_curl_sign import columns_of, cycle_order, graph_of, has_mirror  # noqa: E402


def has_reversal(g, side, loop, radius, side_preserving):
    dist = nx.multi_source_dijkstra_path_length(g, set(loop), cutoff=radius)
    ball = g.subgraph(dist.keys()).copy()
    a, b, c, d = loop
    targets = ([a, d, c, b], [c, b, a, d]) if side_preserving else ([b, a, d, c], [d, c, b, a])
    anchors = {a: 0, b: 1, c: 2, d: 3}
    for target in targets:
        g1, g2 = ball.copy(), ball.copy()
        for v in ball.nodes:
            g1.nodes[v]["lab"] = (dist[v], anchors.get(v, -1))
            g2.nodes[v]["lab"] = (dist[v], -1)
        for i, v in enumerate(target):
            g2.nodes[v]["lab"] = (dist[v], i)
        if isomorphism.GraphMatcher(g1, g2, node_match=isomorphism.categorical_node_match("lab", None)).is_isomorphic():
            return True
    return False


if __name__ == "__main__":
    # (1) a perfect tube: 4 x 12 torus
    g = nx.grid_2d_graph(12, 4, periodic=True)
    g = nx.convert_node_labels_to_integers(g, label_attribute="xy")
    side = {v: (g.nodes[v]["xy"][0] + g.nodes[v]["xy"][1]) % 2 for v in g.nodes}
    ring = [v for v in g.nodes if g.nodes[v]["xy"][0] == 5]
    loop = cycle_order(g, ring)
    print("(1) perfect 4 x 12 tube, ring at x = 5:", ["MIRROR" if has_mirror(g, side, loop, r) else "SIGNED" for r in (2, 3, 4, 6)])
    # (2) the SIGNED columns of the saved states
    files = sorted(glob(str(ROOT / "results/t7d_lam125_n144_adj/*.npz"))) + sorted(glob(str(ROOT / "results/t51_l128_10k_00_adj/*.npz")))
    tot = signed = swap = 0
    for f in files:
        d = np.load(f)
        adj, part = d["adj"], d["part"]
        g = graph_of(adj)
        for pts in columns_of(adj):
            loop = cycle_order(g, pts)
            if loop is None:
                continue
            tot += 1
            if not has_mirror(g, part, loop, 3):
                signed += 1
                if has_reversal(g, part, loop, 3, side_preserving=False):
                    swap += 1
    print("(2) columns %d; SIGNED at r = 3 (side-preserving test) %d; of those, a side-SWAPPING reversal exists for %d" % (tot, signed, swap))

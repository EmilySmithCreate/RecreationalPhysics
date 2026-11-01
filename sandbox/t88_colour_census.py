"""Sandbox look, 1 November 2026 (a look: it can kill, not crown). A colour census of T88's saved rods, fed end against far end.

Question (the owner's, 1 November): in T88 (the pole test; scripts/run_rod_pole.py) a six-link rod 4 x 4 x L, two
directions curled and one open, was fed its whole energy at one end (per-vertex stores on the side-0 points of layer
z = 0) and the opening started there. Her picture (VISION Update 149) has the matter handedness breach first at the
pole. The toy's "colour" is the bipartition: every curled loop's two ways round differ only by which kind of point sits
where (ASSUMPTIONS O170; T87 SIGNED, scripts/t87_curl_sign.py). Prediction inferred from Update 149, marked INFERRED:
a colour skew at the fed end. Ours: none beyond the side-0 feed itself (the stores sat on side-0 points, so a side-0
skew in layer z = 0 is the protocol, not physics; the far end, z = L / 2, is the clean comparison).

Read per saved wiring (results/t88_rod_l{8,12,16}_lam{120,125}_e{120,240,480}_adj/rep*.npz; adj (N, 6), part (N,))
and pooled per cell (L, lambda, E), in three layer bands: FED (z = 0 and its two periodic neighbours), FAR (z = L / 2
and its two neighbours), REST:
  (1) points off the rod's rung (local_dimension_d != 1): count on side 0 and side 1; the fed layer z = 0 alone beside;
  (2) endpoints of links carrying five or more squares and of links carrying fewer than four (cqg_d.squares_on_edge):
      count on each side. Every link joins the two sides, so pooled over the whole rod this is 50 : 50 by construction;
      only the split across band boundaries can move it, and it is reported for completeness;
  (3) every closed loop of four points, all at local dimension 2 (one direction still curled), whose four links each
      carry five squares (the surviving curled loop inside the opened region): T87's sign test at six links, radius 2:
      MIRROR if a side-preserving reversal of the loop extends to an isomorphism of the ball of radius 2 round it that
      keeps every point's distance from the loop and its side (networkx VF2 with node attributes), else SIGNED. Counts
      per band. The sign test is run on every cell (it is fast enough).
Skew statistic: side-0 share of the d != 1 points in a band, with the binomial standard error sqrt(0.25 / n); a band
is SKEWED if |share - 0.5| exceeds three standard errors with n >= 30. Verdict words for the look: SKEW AT THE FED END
(fed band skewed beyond z = 0 while the far band is not), NO SKEW, UNREADABLE (too few objects). Protocol caveat: the
feed itself was one-sided. Output: sandbox/out/t88_colour_census_2026-11-01.txt. Nothing is registered.
"""
import glob
import os
import re
import sys

import networkx as nx
import numpy as np
from networkx.algorithms import isomorphism

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, "src"))
from graphity.cqg_d import squares_on_edge      # noqa: E402
from graphity.dimension import local_dimension_d  # noqa: E402

RUNG_D, OPENED_D = 1, 2
CURLED_SQ, FLAT_SQ = 5, 4
RADIUS = 2
MIN_N, SIGMAS = 30, 3.0


def layers_of(dims):
    return np.array(np.unravel_index(np.arange(int(np.prod(dims))), dims))[2]


def bands_of(dims):
    """0 = FED (z in {0, 1, L-1}), 1 = FAR (z in {L/2 - 1, L/2, L/2 + 1}), 2 = REST."""
    L = dims[2]
    z = layers_of(dims)
    band = np.full(len(z), 2)
    band[np.isin(z, [0, 1, L - 1])] = 0
    band[np.isin(z, [L // 2 - 1, L // 2, L // 2 + 1])] = 1
    return z, band


def graph_of(adj):
    g = nx.Graph()
    g.add_nodes_from(range(adj.shape[0]))
    for v in range(adj.shape[0]):
        for w in adj[v]:
            if w >= 0 and v < w:
                g.add_edge(int(v), int(w))
    return g


def curled_loops(adj, g, d, sq):
    """4-cycles with all four points at d = 2 and all four links at five squares, in cyclic order."""
    loops, seen = [], set()
    for a in range(adj.shape[0]):
        if d[a] != OPENED_D:
            continue
        nb = [int(x) for x in adj[a] if x >= 0 and d[x] == OPENED_D and sq[frozenset((a, int(x)))] == CURLED_SQ]
        for i, b in enumerate(nb):
            for dd in nb[i + 1:]:
                for c in set(g.neighbors(b)) & set(g.neighbors(dd)):
                    if c == a or d[c] != OPENED_D:
                        continue
                    if sq[frozenset((b, c))] == CURLED_SQ and sq[frozenset((c, dd))] == CURLED_SQ:
                        key = frozenset((a, b, c, dd))
                        if key not in seen:
                            seen.add(key)
                            loops.append([a, b, c, dd])
    return loops


def has_mirror(g, side, loop, radius=RADIUS):
    """T87's test: does a side-preserving reversal of the loop extend to an isomorphism of its ball?"""
    dist = nx.multi_source_dijkstra_path_length(g, set(loop), cutoff=radius)
    ball = g.subgraph(dist.keys()).copy()
    anchors = {loop[i]: i for i in range(4)}
    for target in ([loop[0], loop[3], loop[2], loop[1]], [loop[2], loop[1], loop[0], loop[3]]):
        g1, g2 = ball.copy(), ball.copy()
        for v in ball.nodes:
            g1.nodes[v]["lab"] = (dist[v], int(side[v]), anchors.get(v, -1))
            g2.nodes[v]["lab"] = (dist[v], int(side[v]), -1)
        for i, v in enumerate(target):
            g2.nodes[v]["lab"] = (dist[v], int(side[v]), i)
        gm = isomorphism.GraphMatcher(g1, g2, node_match=isomorphism.categorical_node_match("lab", None))
        if gm.is_isomorphic():
            return True
    return False


def census(path, dims):
    f = np.load(path)
    adj, side = f["adj"], f["part"]
    z, band = bands_of(dims)
    d = local_dimension_d(adj)
    g = graph_of(adj)
    sq = {frozenset(e): int(squares_on_edge(adj, e[0], e[1])) for e in g.edges}
    c = np.zeros((3, 2), int)         # (1) d != 1 points: band x side
    c0 = np.zeros(2, int)             # the fed layer z = 0 alone
    hi = np.zeros((3, 2), int)        # (2) endpoints of links at >= 5 squares
    lo = np.zeros((3, 2), int)        # endpoints of links at < 4 squares
    for v in np.flatnonzero(d != RUNG_D):
        c[band[v], side[v]] += 1
        if z[v] == 0:
            c0[side[v]] += 1
    for e, s in sq.items():
        for v in e:
            if s >= CURLED_SQ:
                hi[band[v], side[v]] += 1
            elif s < FLAT_SQ:
                lo[band[v], side[v]] += 1
    sg = np.zeros((3, 2), int)        # (3) loops: band x (SIGNED, MIRROR)
    for loop in curled_loops(adj, g, d, sq):
        sg[band[loop[0]], 1 if has_mirror(g, side, loop) else 0] += 1
    hist = np.bincount(np.minimum(d, 5), minlength=6)   # d = 0..4, 5+ pooled
    return dict(c=c, c0=c0, hi=hi, lo=lo, sg=sg, hist=hist, n_open=int((d != RUNG_D).sum()), damaged=int((d > 3).sum()))


def skew(n0, n1):
    n = n0 + n1
    if n < MIN_N:
        return "n<%d" % MIN_N, 0.0
    share = n0 / n
    se = (0.25 / n) ** 0.5
    return ("SKEWED" if abs(share - 0.5) > SIGMAS * se else "even"), (share - 0.5) / se


def main():
    out = open(os.path.join(HERE, "out", "t88_colour_census_2026-11-01.txt"), "w", encoding="utf-8", newline="\n")

    def say(s=""):
        print(s); out.write(s + "\n")

    say("T88 colour census, 1 November 2026 (sandbox look). Bands: FED = z in {0, 1, L-1}; FAR = z in {L/2-1, L/2, L/2+1}.")
    say("Columns: points off the rung (d != 1) side0:side1 per band, then the fed layer z = 0 alone; endpoints of links at")
    say(">= 5 squares and < 4 squares side0:side1 per band; curled loops in the opened region SIGNED:MIRROR per band.")
    say("z = (share0 - 0.5) / binomial standard error for the d != 1 points. 'n<30' = too few to read.")
    say()
    pooled = {}
    cells = sorted(glob.glob(os.path.join(ROOT, "results", "t88_rod_l*_adj")))
    for cell in cells:
        m = re.search(r"t88_rod_l(\d+)_lam(\d+)_e(\d+)_adj", cell)
        L, lam, E = int(m.group(1)), int(m.group(2)) / 100, int(m.group(3))
        dims = (4, 4, L)
        tot = None
        reps = sorted(glob.glob(os.path.join(cell, "rep*.npz")))
        say("cell L = %d  lambda = %.2f  E = %d  (%d wirings)" % (L, lam, E, len(reps)))
        for p in reps:
            r = census(p, dims)
            say("  %s: off-rung %3d (damaged %2d) | d!=1 FED %3d:%-3d FAR %3d:%-3d REST %3d:%-3d | z=0 %2d:%-2d | "
                ">=5 FED %3d:%-3d FAR %3d:%-3d | <4 FED %3d:%-3d FAR %3d:%-3d | loops S:M FED %d:%d FAR %d:%d REST %d:%d"
                % (os.path.basename(p), r["n_open"], r["damaged"], *r["c"][0], *r["c"][1], *r["c"][2], *r["c0"],
                   *r["hi"][0], *r["hi"][1], *r["lo"][0], *r["lo"][1], *r["sg"][0], *r["sg"][1], *r["sg"][2]))
            if tot is None:
                tot = {k: np.array(r[k]) for k in ("c", "c0", "hi", "lo", "sg", "hist")}
            else:
                for k in tot:
                    tot[k] = tot[k] + r[k]
        pooled[(L, lam, E)] = tot
        fed_w, fed_z = skew(*tot["c"][0]); far_w, far_z = skew(*tot["c"][1])
        z0_w, z0_z = skew(*tot["c0"])
        nb_w, nb_z = skew(tot["c"][0][0] - tot["c0"][0], tot["c"][0][1] - tot["c0"][1])   # fed band minus z = 0
        say("  pooled local-dimension histogram d = 0,1,2,3,4,5+: %s  (d = 2 points are plentiful, but almost none sit on an "
            "intact curled loop: four links at five squares with all four points at d = 2)" % " ".join(map(str, tot["hist"])))
        say("  pooled: d!=1 FED %d:%d (%s, z=%+.1f) | z=0 alone %d:%d (%s, z=%+.1f) | z=1,L-1 %d:%d (%s, z=%+.1f) | "
            "FAR %d:%d (%s, z=%+.1f) | REST %d:%d | loops S:M FED %d:%d FAR %d:%d REST %d:%d"
            % (*tot["c"][0], fed_w, fed_z, *tot["c0"], z0_w, z0_z, tot["c"][0][0] - tot["c0"][0],
               tot["c"][0][1] - tot["c0"][1], nb_w, nb_z, *tot["c"][1], far_w, far_z, *tot["c"][2],
               *tot["sg"][0], *tot["sg"][1], *tot["sg"][2]))
        say()
    say("Summary, one line per cell: band / side0:side1 of d != 1 points / word / loops SIGNED:MIRROR")
    all_c = np.zeros((3, 2), int); all_c0 = np.zeros(2, int); all_sg = np.zeros((3, 2), int)
    for (L, lam, E), tot in sorted(pooled.items()):
        all_c += tot["c"]; all_c0 += tot["c0"]; all_sg += tot["sg"]
        say("  L=%2d lam=%.2f E=%3d | FED %3d:%-3d %-6s | z=0 %3d:%-3d %-6s | z=1,L-1 %3d:%-3d %-6s | FAR %3d:%-3d %-6s | "
            "loops FED %d:%d FAR %d:%d"
            % (L, lam, E, *tot["c"][0], skew(*tot["c"][0])[0], *tot["c0"], skew(*tot["c0"])[0],
               tot["c"][0][0] - tot["c0"][0], tot["c"][0][1] - tot["c0"][1],
               skew(tot["c"][0][0] - tot["c0"][0], tot["c"][0][1] - tot["c0"][1])[0],
               *tot["c"][1], skew(*tot["c"][1])[0], *tot["sg"][0], *tot["sg"][1]))
    say()
    nb0, nb1 = all_c[0][0] - all_c0[0], all_c[0][1] - all_c0[1]
    fed_w, fed_z = skew(*all_c[0]); z0_w, z0_z = skew(*all_c0); nb_w, nb_z = skew(nb0, nb1); far_w, far_z = skew(*all_c[1])
    say("Pooled over all 72 wirings, d != 1 points: FED %d:%d (%s, z=%+.1f); z=0 alone %d:%d (%s, z=%+.1f); "
        "z=1,L-1 %d:%d (%s, z=%+.1f); FAR %d:%d (%s, z=%+.1f); REST %d:%d."
        % (*all_c[0], fed_w, fed_z, *all_c0, z0_w, z0_z, nb0, nb1, nb_w, nb_z, *all_c[1], far_w, far_z, *all_c[2]))
    say("Curled loops in the opened region, SIGNED:MIRROR at r = 2: FED %d:%d, FAR %d:%d, REST %d:%d."
        % (*all_sg[0], *all_sg[1], *all_sg[2]))
    n_fed, n_far = all_c[0].sum(), all_c[1].sum()
    if n_fed < MIN_N and n_far < MIN_N:
        word = "UNREADABLE"
    elif nb_w == "SKEWED" and far_w != "SKEWED":
        word = "SKEW AT THE FED END"
    elif z0_w == "SKEWED" and nb_w != "SKEWED" and far_w != "SKEWED":
        word = "NO SKEW (beyond the fed layer z = 0 itself, which is the protocol: the stores sat on side-0 points)"
    elif far_w == "SKEWED":
        word = "SKEW AT BOTH ENDS" if fed_w == "SKEWED" else "SKEW AT THE FAR END"
    else:
        word = "NO SKEW"
    say("Verdict word for the look: %s" % word)
    say("Caveat: the feed was one-sided by protocol (side-0 stores at z = 0), so only a skew outside z = 0 could be physics.")
    out.close()


if __name__ == "__main__":
    main()

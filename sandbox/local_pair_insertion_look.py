"""Sandbox look (exploratory; rule 16), 25 October 2026: can a flat sheet gain one pair of points locally and stay flat?

The owner's answer (VISION Update 118): "I don't think it can. looking for whole rows." Exact on what it covers: every
degree-preserving insertion of one pair (one point of each kind) into a 10 x 10 flat torus that rewires only links near one
point, checked for flatness (every link on exactly two squares) and for the hard-core rule.

Two forms cover every way to add one pair while keeping four links a point:
  (A) the new points are not joined: cut four links (b_i, w_i), join the new white point to b_1..b_4 and the new black
      point to w_1..w_4;
  (B) the new points are joined: cut three links, join the new white to b_1..b_3 and the new black, the new black to
      w_1..w_3 and the new white.
Links considered: both ends within graph distance R of point 0.
"""
from itertools import combinations
from collections import deque

import numpy as np

from graphity.cqg import torus, is_valid, NO_CAP
from graphity.squares import squares_on_edge

L, R = 10, 4


def near(adj, src, r):
    dist = {src: 0}
    q = deque([src])
    while q:
        a = q.popleft()
        if dist[a] == r:
            continue
        for b in adj[a]:
            b = int(b)
            if b not in dist:
                dist[b] = dist[a] + 1
                q.append(b)
    return set(dist)


def flat(adj):
    n = adj.shape[0]
    for u in range(n):
        for v in adj[u]:
            if u < v and squares_on_edge(adj, u, int(v)) != 2:
                return False
    return True


def build(adj, cut, joined):
    n = adj.shape[0]
    new = np.vstack([adj, -np.ones((2, 4), dtype=np.int64)])
    w_new, b_new = n, n + 1
    bs, ws = [b for b, _ in cut], [w for _, w in cut]
    for b, w in cut:
        new[b, np.where(new[b] == w)[0][0]] = w_new
        new[w, np.where(new[w] == b)[0][0]] = b_new
    new[w_new, :len(bs)] = bs
    new[b_new, :len(ws)] = ws
    if joined:
        new[w_new, 3] = b_new
        new[b_new, 3] = w_new
    return new


def main():
    adj, part = torus(L, L, cap=NO_CAP)
    pts = near(adj, 0, R)
    edges = sorted({(u, int(v)) if part[u] == 0 else (int(v), u)
                    for u in pts for v in adj[u] if int(v) in pts})
    tried = flat_valid = 0
    for k, joined in ((4, False), (3, True)):
        for cut in combinations(edges, k):
            if len({b for b, _ in cut}) < k or len({w for _, w in cut}) < k:
                continue
            g = build(adj, cut, joined)
            tried += 1
            if flat(g) and is_valid(g, cap=NO_CAP):
                flat_valid += 1
                print("flat insertion found:", cut, "joined" if joined else "apart")
    print(f"L = {L}, links within distance {R} of a point: {len(edges)}; insertions tried {tried}; flat and valid {flat_valid}")


if __name__ == "__main__":
    main()

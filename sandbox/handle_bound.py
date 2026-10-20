"""Sandbox look: does the toy's curvature force handles?

Claim (ours, exact by Euler's formula): for a simple bipartite 4-regular graph embedded in a closed orientable surface
of genus g, with D = sum over edges of max(0, 2 - S_e) (S_e = squares through edge e; D = H/4 at lambda = 1),
    g >= 1 + D / 24.
Checked here on the natural embedding of a flat torus (equality: g = 1, D = 0) and on random embeddings of graphs
made by random degree- and side-preserving switches from a torus (the bound must never fail).
"""
import itertools, random, sys

def torus(L):
    idx = lambda x, y: (x % L) * L + (y % L)
    rot = {}
    for x in range(L):
        for y in range(L):
            rot[idx(x, y)] = [idx(x + 1, y), idx(x, y + 1), idx(x - 1, y), idx(x, y - 1)]  # E, N, W, S: natural
    return rot

def edges(rot):
    return {tuple(sorted((u, v))) for u in rot for v in rot[u]}

def squares_per_edge(rot):
    adj = {u: set(vs) for u, vs in rot.items()}
    S = {e: 0 for e in edges(rot)}
    for (u, v) in S:
        for a in adj[u] - {v}:
            for b in adj[v] - {u}:
                if a != b and b in adj[a]:
                    S[(u, v)] += 1
    return S

def genus(rot):
    """Face tracing: the face after dart (u -> v) is (v -> w) with w the successor of u in v's rotation."""
    pos = {v: {w: i for i, w in enumerate(ws)} for v, ws in rot.items()}
    seen, F = set(), 0
    for u in rot:
        for v in rot[u]:
            if (u, v) in seen:
                continue
            F += 1
            a, b = u, v
            while (a, b) not in seen:
                seen.add((a, b))
                ws = rot[b]
                a, b = b, ws[(pos[b][a] + 1) % len(ws)]
    V, E = len(rot), len(edges(rot))
    chi = V - E + F
    return (2 - chi) // 2

def random_switch(rot, rng, n):
    adj = {u: set(vs) for u, vs in rot.items()}
    E = list(edges(rot))
    side = {}
    # two-colour
    start = next(iter(adj)); side[start] = 0; stack = [start]
    while stack:
        u = stack.pop()
        for w in adj[u]:
            if w not in side:
                side[w] = 1 - side[u]; stack.append(w)
    done = 0
    while done < n:
        (a, b), (c, d) = rng.sample(E, 2)
        if side[a] != side[c]:
            c, d = d, c
        # replace a-b, c-d by a-d, c-b (a, c on one side; b, d on the other)
        if len({a, b, c, d}) < 4 or d in adj[a] or b in adj[c]:
            continue
        adj[a].remove(b); adj[b].remove(a); adj[c].remove(d); adj[d].remove(c)
        adj[a].add(d); adj[d].add(a); adj[c].add(b); adj[b].add(c)
        E = list({tuple(sorted((u, v))) for u in adj for v in adj[u]})
        done += 1
    return {u: list(vs) for u, vs in adj.items()}

def deficit(rot):
    return sum(max(0, 2 - s) for s in squares_per_edge(rot).values())

rng = random.Random(1)
t = torus(8)
print("flat 8x8 torus, natural embedding: genus", genus(t), "deficit", deficit(t), "bound", 1 + deficit(t) / 24)
worst = None
for k in (1, 2, 4, 8, 32, 128):
    for rep in range(5):
        g0 = random_switch(t, rng, k)
        D = deficit(g0)
        bound = 1 + D / 24
        for trial in range(200):
            r = {u: rng.sample(vs, len(vs)) for u, vs in g0.items()}
            g = genus(r)
            slack = g - bound
            assert slack >= -1e-9, (k, D, g)
            worst = slack if worst is None else min(worst, slack)
    print(f"{k:4d} switches: deficit {D:4d}, bound {bound:6.2f}, bound never failed in 1000 random embeddings")
print("smallest slack seen:", round(worst, 3))

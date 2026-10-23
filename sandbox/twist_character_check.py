"""Sandbox look, 23 October 2026, revised the same day after an adversarial check (rule 16: a look, not a result; it
can kill, not crown). BUILT GRAPHS ONLY. Nothing is read from results/.

What does the stiff toy carry, by its wiring alone, of a twist? This script computes two twist-like quantities on
built graphs, for the definition the "Current definitions" box of docs/design/regge_stage_b_brief.md is to receive
(handoff of 23 October, item 2.2; the draft entry is sandbox/out/twist_definition_draft_2026-10-23.md):

  1. the MOD-2 ORIENTATION CHARACTER of a closed cycle on the surface the squares make, under a named face rule
     (0: a band carried round the cycle comes back as it left, an annulus; 1: flipped, a Mobius band);
  2. the SEAM SHIFT of a lattice torus (the torsion r of the twisted grids T(n, m, r) of the 20 October note, sec. 7;
     O116's "tube with its seam shifted by two"): a whole number read off the wiring, blind to mirror images.

The face rule is the eq45 brief's (docs/design/eq45_ratio_brief.md, box item 1; the angle sum alpha and the vertex
type are [T25] Sec. IV.2's, the point-by-point choice is ours): at each point, a corner is a pair of its links; the
corner's cycle length is 2 + the shortest path between the two neighbours avoiding the point; a rotation pairs the
four links into two opposite pairs and keeps the other four corners as faces; the point's rotation is the one with
the smallest alpha = sum (k - 2) / k. The default implementation is imported from sandbox/eq45_geometrize_check.py so
that it is the same rule to the letter, INCLUDING its tie-break (the first rotation in slot order among equal alphas).
What the revision adds: the rule as written says nothing about ties between rotations of the SAME vertex type, nor
about which shortest cycle is the face when a corner has several; the eq45 "ties" counter counts only ties between
DIFFERENT types. This script counts both kinds of tie and, where the rule ties, enumerates every completion (every
tie broken every way, every ambiguous corner given each of its shortest cycles) and reports how many close into a
surface and what each closing surface is.

Under a completed rule the chosen corners' cycles are the faces. They form a closed surface when every chosen face
is chosen at every one of its points and every link lies in exactly two chosen faces. On such a surface:
orientability (propagating face orientations across shared links, as scripts/exact_torus_counting.surface);
V - E + F; the mod-2 character of a closed walk of links; the mod-2 character of a ring of diagonals (a cyclic
sequence of faces, consecutive faces sharing a point, each face's entry and exit points being opposite corners).

Second revision, the same day, after a second adversarial check: closure is global, so "no completion closes" said
nothing about WHERE a surface fails, and "the point with no fitting option" was the deepest point of a breadth-first
backtrack, which depends on the search order. Both are replaced by a LOCAL criterion that uses nothing outside the
region it is asked about. A graph's points are sorted by their links' square counts into the CURLED part (a link
carrying three squares), the OPENED part (every link in exactly two) and FLAWED points (a link in fewer than two);
the LIP is the set of links joining a curled point to a point that is not curled. A completion CLOSES ON a region
when every face with all its points in the region, chosen at one of them, is chosen at all of them; nothing outside
the region is decided, and a face with a point outside it is unconstrained. Its BAND there is its faces with all
points in the region: a surface with boundary unless at some point its corners are two opposite ones (a PINCH); its
BOUNDARY is the links lying in exactly one of its faces. The band is read for the curled part alone, the opened part
alone and all points together, over every completion that closes on each, and reported as one-sided or two-sided.
A point is a LOCAL FAILURE if no completion closes on the 3-step ball round it (which holds every square and hexagon
through it): that locates where a surface fails from the graph and the rule alone, whatever order anything was
searched in. The character of a closed walk needs only the band round it (two faces on each of its links, chosen at
both ends), so a defect elsewhere never undefines it. The same pass adds the zigzag of diagonals along the strip
x -> 1 - x maps to itself on the odd-row Klein grids (between columns a/2 and a/2 + 1), which the first version did
not print.

Graphs (all built; validity by cqg.is_valid without the cap; S and X from cqg): the 4 x L tube; its zero-cost family,
the reflected closure (one switch: ring L - 1 joined to ring 0 through x -> 2 - x) and the half-turn closure (two
switches; through x -> x + 2); flat tori; flat Klein grids of two families (a x b, last row to first through x -> -x
with b even, and through x -> 1 - x with b odd); the 4-cube; the eq45 brief's spliced "handle" (spliced the same way
at both ends, which the adversarial check of 23 October found makes it one-sided, a cross-handle) and the same handle
with one splice mirrored (control), with the character of a cycle along each handle in its one closing completion; a
hand-built lip (a stretch of tube four around joined to a stretch of sheet six around through a ring with a chord);
and the helical tori of O116 (the tube with its ring seam shifted by r), against the half-turn closure.

Usage: python3 sandbox/twist_character_check.py > sandbox/out/twist_character_check_2026-10-23.txt
"""
import itertools
import os
import sys
from collections import Counter, defaultdict, deque

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, "src"))
sys.path.insert(0, os.path.join(ROOT, "scripts"))
sys.path.insert(0, HERE)

from graphity.cqg import NO_CAP, is_valid, torus, total_squares, surplus          # noqa: E402
from graphity.squares import squares_on_edge                                       # noqa: E402
from eq45_geometrize_check import (INF, PAIRS, ROTATIONS, angle_term, geometrize, handle_graph,  # noqa: E402
                                   shortest_cycle_points, two_colour)
from read_endpoint_width import twisted_tube, width as shell_width                 # noqa: E402  (O116's builder and reader)
from exact_flat_torus_widths import graph as flat_graph                            # noqa: E402  (O119's wrappings)

try:
    import igraph as ig
except ImportError:                                                                # pragma: no cover
    ig = None
import networkx as nx


# ---------------------------------------------------------------- the built graphs

def index(x, y, a, b):
    return (x % a) * b + (y % b)


def xy(i, b):
    return int(i) // b, int(i) % b


def ring_bundle(length, sigma):
    """The 4 x L tube with ring L - 1 joined to ring 0 through sigma: (x, L - 1) - (sigma[x], 0). The same hand-built
    wiring as tests/test_exact_torus_counting.py::ring_bundle. Adjacency order: ring +, ring -, up, down."""
    adj = np.empty((4 * length, 4), dtype=np.int64)
    inv = [sigma.index(x) for x in range(4)]
    for x in range(4):
        for y in range(length):
            up = index(sigma[x], 0, 4, length) if y == length - 1 else index(x, y + 1, 4, length)
            down = index(inv[x], length - 1, 4, length) if y == 0 else index(x, y - 1, 4, length)
            adj[index(x, y, 4, length)] = (index(x + 1, y, 4, length), index(x - 1, y, 4, length), up, down)
    part = np.array([(x + y) % 2 for x in range(4) for y in range(length)], dtype=np.int64)
    return adj, part


def klein_grid(a, b, c=0):
    """An a x b grid (a even) whose rows wrap round (x mod a) and whose last row is joined to the first through the
    reflection x -> c - x: (x, b - 1) - (c - x mod a, 0). With c = 0 the two kinds of point need b even; with c = 1
    they need b odd (the reflection then fixes no column). Adjacency order: ring +, ring -, up, down. With every
    square as a face it is a closed surface (every link in two squares) closed through a reflection: a Klein bottle
    if it is valid and flat."""
    adj = np.empty((a * b, 4), dtype=np.int64)
    for x in range(a):
        for y in range(b):
            up = index(c - x, 0, a, b) if y == b - 1 else index(x, y + 1, a, b)
            down = index(c - x, b - 1, a, b) if y == 0 else index(x, y - 1, a, b)
            adj[index(x, y, a, b)] = (index(x + 1, y, a, b), index(x - 1, y, a, b), up, down)
    return adj


def handle_mirror(lx, ly, h, mirror_b):
    """The eq45 brief's handle_graph, with the splice at end b optionally mirrored (u1 and u2 swapped). With
    mirror_b = False it is handle_graph(lx, ly, h) link for link; with True the control for correction (4).
    (Ported from the adversarial check's lip4.py.)"""
    adj0, part0 = torus(lx, ly, NO_CAP)
    n0 = lx * ly
    n = n0 + 4 * h
    nb = [list(map(int, adj0[v])) for v in range(n0)] + [[] for _ in range(4 * h)]
    seg = lambda t, j: n0 + 4 * t + (j % 4)                               # noqa: E731
    side = list(map(int, part0)) + [(t + j) % 2 for t in range(h) for j in range(4)]
    for t in range(h):
        for j in range(4):
            nb[seg(t, j)].extend([seg(t, j + 1), seg(t, j - 1)])
            if t + 1 < h:
                nb[seg(t, j)].append(seg(t + 1, j))
                nb[seg(t + 1, j)].append(seg(t, j))

    def splice(x0, y0, layer, mirror):
        lab = lambda x, y: (x % lx) * ly + (y % ly)                          # noqa: E731
        u1, v1, u2, v2 = lab(x0, y0), lab(x0, y0 + 1), lab(x0 + 1, y0 + 1), lab(x0 + 1, y0)
        for p, q in ((u1, v1), (u2, v2)):
            nb[p].remove(q)
            nb[q].remove(p)
        s = side[u1]
        ends_s = [seg(layer, j) for j in range(4) if side[seg(layer, j)] != s]
        ends_o = [seg(layer, j) for j in range(4) if side[seg(layer, j)] == s]
        us = (u2, u1) if mirror else (u1, u2)
        for p, q in zip(ends_s, us):
            nb[p].append(q)
            nb[q].append(p)
        for p, q in zip(ends_o, (v1, v2)):
            nb[p].append(q)
            nb[q].append(p)

    splice(0, 0, 0, False)
    splice(lx // 2, ly // 2, h - 1, mirror_b)
    adj = np.array(nb, dtype=np.int64)
    return adj, np.array(side, dtype=np.int64), [seg(t, j) for t in range(h) for j in range(4)]


def lip_tube_to_sheet(l4, l6):
    """A hand-built lip: l4 rings of a tube four around joined to l6 rings of a sheet six around, closed into a
    torus. At each joint the four tube points T0..T3 link to sheet points S1, S2, S5, S4 (the pairing the two kinds
    of point allow) and the two sheet points left over, S0 and S3, are joined by a chord. Point labels: tube ring t,
    position i -> 4 t + i; sheet ring s, position j -> 4 l4 + 6 s + j. Returns (adj, tube points, sheet points,
    joint tube rings, joint sheet rings)."""
    n = 4 * l4 + 6 * l6
    nb = [[] for _ in range(n)]
    T = lambda t, i: 4 * (t % l4) + (i % 4)                                # noqa: E731
    S = lambda s, j: 4 * l4 + 6 * (s % l6) + (j % 6)                       # noqa: E731

    def add(u, v):
        nb[u].append(v)
        nb[v].append(u)

    for t in range(l4):
        for i in range(4):
            add(T(t, i), T(t, i + 1))
            if t + 1 < l4:
                add(T(t, i), T(t + 1, i))
    for s in range(l6):
        for j in range(6):
            add(S(s, j), S(s, j + 1))
            if s + 1 < l6:
                add(S(s, j), S(s + 1, j))
    pairing = {0: 1, 1: 2, 2: 5, 3: 4}
    for t, s in ((l4 - 1, 0), (0, l6 - 1)):                                # the two joints
        for i, j in pairing.items():
            add(T(t, i), S(s, j))
        add(S(s, 0), S(s, 3))
    adj = np.array(nb, dtype=np.int64)
    assert adj.shape == (n, 4), adj.shape
    return (adj, [T(t, i) for t in range(l4) for i in range(4)], [S(s, j) for s in range(l6) for j in range(6)],
            [[T(l4 - 1, i) for i in range(4)], [T(0, i) for i in range(4)]],
            [[S(0, j) for j in range(6)], [S(l6 - 1, j) for j in range(6)]])


# ---------------------------------------------------------------- the face rule, with its ties made visible

def shortest_paths_avoiding(adj, v, a, b):
    """(length of the shortest a-b path avoiding v, how many such paths); (INF, 0) if none."""
    if a == b:
        return INF, 0
    dist, cnt = {a: 0}, {a: 1}
    q = deque([a])
    while q:
        x = q.popleft()
        if x == b:
            break
        for y in adj[x]:
            y = int(y)
            if y == v:
                continue
            if y not in dist:
                dist[y] = dist[x] + 1
                cnt[y] = cnt[x]
                q.append(y)
            elif dist[y] == dist[x] + 1:
                cnt[y] += cnt[x]
    if b not in dist:
        return INF, 0
    return dist[b], cnt[b]


def all_shortest_cycles(adj, v, a, b, length):
    """Every shortest cycle through the corner a - v - b, as point tuples (v, a, ..., b); `length` is the path length."""
    out = []

    def dfs(path):
        x = path[-1]
        if len(path) - 1 == length:
            if x == b:
                out.append((v,) + tuple(path))
            return
        for y in adj[x]:
            y = int(y)
            if y == v or y in path:
                continue
            dfs(path + [y])

    dfs([a])
    return out


def face_key(cyc):
    m = len(cyc)
    return frozenset(frozenset((int(cyc[t]), int(cyc[(t + 1) % m]))) for t in range(m))


def rule_options(adj):
    """Per point: every rotation of least alpha (more than one = a tie), each as (ktype, corner pair indices);
    plus the corner lengths and shortest-path counts. The eq45 code keeps options[v][0] in slot order."""
    n = adj.shape[0]
    lengths = np.zeros((n, 6), dtype=np.int64)
    counts = np.zeros((n, 6), dtype=np.int64)
    options = []
    for v in range(n):
        for p, (i, j) in enumerate(PAIRS):
            d, c = shortest_paths_avoiding(adj, v, int(adj[v, i]), int(adj[v, j]))
            lengths[v, p] = INF if d >= INF else d + 2
            counts[v, p] = c
        opts = []
        for opp in ROTATIONS:
            corners = [p for p, pr in enumerate(PAIRS) if pr not in opp]
            ktype = tuple(sorted(int(lengths[v, p]) for p in corners))
            opts.append((round(sum(angle_term(k) for k in ktype), 12), ktype, corners))
        opts.sort()
        best = [o for o in opts if o[0] == opts[0][0]]
        options.append([(o[1], o[2]) for o in best])
    return options, lengths, counts


def tie_census(adj, options=None):
    """(points tied between rotations of the same type, points tied between different types)."""
    if options is None:
        options = rule_options(adj)[0]
    same = sum(1 for o in options if len(o) > 1 and len({k for k, _ in o}) == 1)
    diff = sum(1 for o in options if len(o) > 1 and len({k for k, _ in o}) > 1)
    return same, diff


def rotation_order(adj, chosen, v):
    """The point's four neighbours in the cyclic order its chosen corners define (a 4-cycle on its links)."""
    nb = {i: [] for i in range(4)}
    for p in chosen:
        i, j = PAIRS[p]
        nb[i].append(j)
        nb[j].append(i)
    order = [0, nb[0][0]]
    while len(order) < 4:
        order.append([k for k in nb[order[-1]] if k != order[-2]][0])
    return [int(adj[v, k]) for k in order]


def complex_from(adj, faces, chosen_at, chosen_pairs):
    """Assemble the surface data from faces (key -> cycle), the faces chosen at each point and each point's chosen
    corner pairs."""
    n = adj.shape[0]
    rot = [rotation_order(adj, chosen_pairs[v], v) for v in range(n)]
    consistent = {k for k, cyc in faces.items() if all(k in chosen_at[w] for w in cyc)}
    by_edge = defaultdict(list)
    for k in faces:
        for e in k:
            by_edge[e].append(k)
    edges = {frozenset((u, int(w))) for u in range(n) for w in adj[u]}
    on_two = sum(1 for e in edges if len(by_edge.get(e, [])) == 2)
    surface = len(consistent) == len(faces) and on_two == len(edges)
    return dict(rot=rot, faces=faces, chosen_at=chosen_at, consistent=consistent, by_edge=by_edge, edges=edges,
                on_two=on_two, surface=surface, chi=n - len(edges) + len(faces),
                face_lengths=Counter(len(c) for c in faces.values()))


def face_complex(adj):
    """The eq45 rule applied with ITS tie-break (slot order), then the chosen corners' cycles collected as faces
    (one shortest cycle per corner, the BFS's). This is the default path, unchanged from the first version."""
    n = adj.shape[0]
    geo = geometrize(adj)
    faces, chosen_at, infinite = {}, [set() for _ in range(n)], 0
    for v in range(n):
        for p in geo["chosen"][v]:
            if geo["corner_len"][v, p] >= INF:
                infinite += 1
                continue
            i, j = PAIRS[p]
            cyc = tuple(int(t) for t in shortest_cycle_points(adj, v, int(adj[v, i]), int(adj[v, j])))
            key = face_key(cyc)
            faces.setdefault(key, cyc)
            chosen_at[v].add(key)
    cx = complex_from(adj, faces, chosen_at, geo["chosen"])
    cx.update(geo=geo, infinite=infinite)
    cx["surface"] = cx["surface"] and infinite == 0
    return cx


def bad_points(cx):
    """Points at which some face passing through them is not among their chosen faces."""
    return sorted({w for k, cyc in cx["faces"].items() if k not in cx["consistent"] for w in cyc
                   if k not in cx["chosen_at"][w]})


def enumerate_completions(adj, cap=300000):
    """Every way of completing the rule where it is silent: each tied point given each of its least-alpha rotations,
    each chosen corner with several shortest cycles given each of them. Returns a summary and the first closing
    completion as a complex (or None)."""
    n = adj.shape[0]
    options, lengths, counts = rule_options(adj)
    cands = {}                                                     # (v, option index, corner) -> candidate faces

    def candidates(v, oi, p):
        key = (v, oi, p)
        if key not in cands:
            i, j = PAIRS[p]
            if lengths[v, p] >= INF:
                cands[key] = []
            else:
                cycs = all_shortest_cycles(adj, v, int(adj[v, i]), int(adj[v, j]), int(lengths[v, p]) - 2)
                seen = {}
                for cyc in cycs:
                    seen.setdefault(face_key(cyc), cyc)
                cands[key] = list(seen.items())
        return cands[key]

    tied = [v for v in range(n) if len(options[v]) > 1]
    total = closing = 0
    kinds = Counter()
    first = None
    rot_space = itertools.product(*[range(len(options[v])) for v in tied])
    for combo in rot_space:
        pick = [0] * n
        for v, k in zip(tied, combo):
            pick[v] = k
        fixed_faces, fixed_at = {}, [set() for _ in range(n)]
        variables = []                                             # (v, p, [(key, cyc), ...])
        infinite = False
        for v in range(n):
            for p in options[v][pick[v]][1]:
                cs = candidates(v, pick[v], p)
                if not cs:
                    infinite = True
                elif len(cs) == 1:
                    k, cyc = cs[0]
                    fixed_faces.setdefault(k, cyc)
                    fixed_at[v].add(k)
                else:
                    variables.append((v, p, cs))
        if infinite:
            total += int(np.prod([len(c) for _v, _p, c in variables])) if variables else 1
            continue
        size = int(np.prod([len(c) for _v, _p, c in variables])) if variables else 1
        if total + size > cap:
            return dict(total=total, closing=closing, kinds=kinds, tied=len(tied), capped=True), first
        for choice in itertools.product(*[range(len(c)) for _v, _p, c in variables]):
            total += 1
            faces = dict(fixed_faces)
            chosen_at = [set(s) for s in fixed_at]
            for (v, p, cs), k in zip(variables, choice):
                key, cyc = cs[k]
                faces.setdefault(key, cyc)
                chosen_at[v].add(key)
            cnt = Counter()
            for k in faces:
                for e in k:
                    cnt[e] += 1
            if len(cnt) != 2 * n or any(c != 2 for c in cnt.values()):
                continue
            if not all(all(k in chosen_at[w] for w in cyc) for k, cyc in faces.items()):
                continue
            closing += 1
            cx = complex_from(adj, faces, chosen_at, [options[v][pick[v]][1] for v in range(n)])
            ok, pieces = orientable(cx)
            kinds[(cx["chi"], ok)] += 1
            if first is None:
                first = cx
    return dict(total=total, closing=closing, kinds=kinds, tied=len(tied), capped=False), first


def point_options_all(adj):
    """Per point, every option the completed rule allows: (corner slots, {face key: cycle}), one for each
    least-alpha rotation and each choice among a corner's several shortest cycles; a rotation with a corner of
    length inf gives no option. The list search_completions decides over (moved out of it in the second revision;
    nothing it enumerates changed)."""
    n = adj.shape[0]
    options, lengths, counts = rule_options(adj)
    point_options = []
    for v in range(n):
        opts = []
        for ktype, corners in options[v]:
            per_corner, ok = [], True
            for p in corners:
                i, j = PAIRS[p]
                if lengths[v, p] >= INF:
                    ok = False
                    break
                cycs = all_shortest_cycles(adj, v, int(adj[v, i]), int(adj[v, j]), int(lengths[v, p]) - 2)
                seen = {}
                for cyc in cycs:
                    seen.setdefault(face_key(cyc), cyc)
                per_corner.append(list(seen.items()))
            if not ok:
                continue
            for combo in itertools.product(*per_corner):
                faces = dict(combo)
                if len(faces) == 4:
                    opts.append((corners, faces))
        point_options.append(opts)
    return point_options


def search_completions(adj, max_keep=3, node_cap=20_000_000):
    """The same question as enumerate_completions, answered by backtracking point by point with pruning: a face
    chosen at a decided point must be chosen at every decided point it passes through, and no link may lie in more
    than two chosen faces. Every closing completion is counted; the first `max_keep` are kept as complexes. Returns
    (number closing, nodes visited, capped?, kept complexes, depth). The depth (how many points were decided before
    every option failed, and the last point tried) depends on the breadth-first order and is NOT a location of the
    failure; the location is read from the bands (regions, band_of, report_bands)."""
    n = adj.shape[0]
    point_options = point_options_all(adj)
    # decide points in breadth-first order from point 0, so that each new point touches decided ones
    order, seen = [], {0}
    q = deque([0])
    while q:
        v = q.popleft()
        order.append(v)
        for w in adj[v]:
            w = int(w)
            if w not in seen:
                seen.add(w)
                q.append(w)
    chosen = [None] * n
    through = defaultdict(set)                                   # point -> chosen faces passing through it
    link_count = Counter()
    global_faces = {}
    found, kept, nodes, capped, deepest = 0, [], [0], [False], [0, None]

    def place(v, corners, faces):
        added = []
        for k, cyc in faces.items():
            if k not in global_faces:
                global_faces[k] = cyc
                added.append(k)
                for w in cyc:
                    through[w].add(k)
                for e in k:
                    link_count[e] += 1
        chosen[v] = (corners, faces)
        return added

    def unplace(v, added):
        chosen[v] = None
        for k in added:
            cyc = global_faces.pop(k)
            for w in cyc:
                through[w].discard(k)
            for e in k:
                link_count[e] -= 1

    def fits(v, faces):
        for k in through[v]:                                      # faces decided elsewhere that pass through v
            if k not in faces:
                return False
        for k, cyc in faces.items():
            if k in global_faces:
                continue
            for w in cyc:
                if chosen[w] is not None and k not in chosen[w][1]:
                    return False
            for e in k:
                if link_count[e] >= 2:
                    return False
        return True

    def rec(t):
        nonlocal found
        nodes[0] += 1
        if nodes[0] > node_cap:
            capped[0] = True
            return
        if t == n:
            if len(link_count) == 2 * n and all(c == 2 for c in link_count.values()):
                found += 1
                if len(kept) < max_keep:
                    kept.append(complex_from(adj, dict(global_faces), [set(c[1]) for c in chosen],
                                             [c[0] for c in chosen]))
            return
        v = order[t]
        if t >= deepest[0]:
            deepest[0], deepest[1] = t, v
        for corners, faces in point_options[v]:
            if not fits(v, faces):
                continue
            added = place(v, corners, faces)
            rec(t + 1)
            unplace(v, added)
            if capped[0]:
                return

    rec(0)
    return found, nodes[0], capped[0], kept, (deepest[0] + 1, n, deepest[1])


def report_search(adj, label, max_keep=3):
    found, nodes, capped, kept, deep = search_completions(adj, max_keep=max_keep)
    kinds = Counter()
    for cx in kept:
        ok, _p = orientable(cx)
        kinds[(cx["chi"], ok)] += 1
    print("  completions by backtracking search (every tie, every ambiguous corner; pruned on face agreement and "
          "link counts): %d close into a surface%s (%d nodes searched); kinds among the first %d kept: %s"
          % (found, " (CAPPED)" if capped else "", nodes, len(kept),
             ", ".join("V - E + F = %d, orientable %s: %d" % (chi, ok, c) for (chi, ok), c in sorted(kinds.items()))
             or "none"))
    if found == 0:
        print("  (no completion closes the whole graph; where the surface fails is read from the bands below, not "
              "from the search, whose stopping point depends on its order)")
    return kept


# ---------------------------------------------------------------- the local criterion: regions and their bands

def regions(adj):
    """The parts of a graph by its links' square counts (the draft entry's terms): CURLED, a point with a link
    carrying three squares; FLAWED, not curled but with a link carrying fewer than two; OPENED, every link in exactly
    two squares. A point with a link at three and another at one counts as curled. The LIP is the set of links
    joining a curled point to a point that is not curled."""
    n = adj.shape[0]
    curled, opened, flawed = set(), set(), set()
    for v in range(n):
        c = [int(squares_on_edge(adj, v, int(w))) for w in adj[v]]
        if max(c) >= 3:
            curled.add(v)
        elif min(c) < 2:
            flawed.add(v)
        else:
            opened.add(v)
    lip = {frozenset((v, int(w))) for v in curled for w in adj[v] if int(w) not in curled}
    return curled, opened, flawed, lip


def holdable_faces(point_options):
    """The faces some band can hold: a face is holdable only if every one of its points has an option containing it.
    A face that fails this at a point is never chosen at all its points, so it closes nowhere and is in no band. (On
    the hand-built lip every shortest hexagon at a joint passes a chord end, whose only option is four squares; on the
    4-cube and the lattice tori every square is holdable.)"""
    at, cyc_of = defaultdict(set), {}
    for v, opts in enumerate(point_options):
        for _corners, faces in opts:
            for k, cyc in faces.items():
                at[k].add(v)
                cyc_of[k] = cyc
    return {k for k, cyc in cyc_of.items() if all(w in at[k] for w in cyc)}


def ball(adj, v, radius):
    """The points within `radius` steps of v."""
    seen, frontier = {int(v)}, {int(v)}
    for _ in range(radius):
        frontier = {int(w) for u in frontier for w in adj[u]} - seen
        seen |= frontier
    return seen


def closing_completions(adj, region, point_options, holdable, max_keep=4, node_cap=5_000_000):
    """Every completion that CLOSES ON the region: each point of the region given one of its options so that every
    face with all its points in the region, chosen at one of them, is chosen at all of them. Nothing outside the
    region is decided, and a face with a point outside the region is unconstrained. Backtracking over the region's
    points in breadth-first order with two exact prunings: a face inside the region that is not holdable can never
    agree, and a face chosen at a decided point must be chosen at every decided point it passes through. The order
    changes the work, not the set found. Returns (count, number of distinct bands, the first `max_keep` bands as
    complex-like dicts, capped?). The band of a completion is its faces with all points in the region; its `pinch` is
    the points of the region at which the band's corners are two opposite ones, its `boundary` the links in exactly
    one of its faces."""
    region = set(int(v) for v in region)
    order, seen = [], set()
    for s in sorted(region):
        if s in seen:
            continue
        q = deque([s])
        seen.add(s)
        while q:
            v = q.popleft()
            order.append(v)
            for w in adj[v]:
                w = int(w)
                if w in region and w not in seen:
                    seen.add(w)
                    q.append(w)
    inside = {}                                                   # face key -> True if all its points lie in region

    def is_inside(k, cyc):
        if k not in inside:
            inside[k] = all(w in region for w in cyc)
        return inside[k]

    # options that differ only in faces with a point outside the region are one option here (those faces are
    # unconstrained and are in no band of the region); their number is kept as a multiplicity for the count
    opts = {}
    for v in order:
        merged = {}
        for corners, faces in point_options[v]:
            inner = {k: cyc for k, cyc in faces.items() if is_inside(k, cyc)}
            if any(k not in holdable for k in inner):
                continue
            sig = (tuple(corners), frozenset(inner))
            if sig in merged:
                merged[sig][2] += 1
            else:
                merged[sig] = [corners, inner, 1]
        opts[v] = [tuple(m) for m in merged.values()]
    chosen = {}
    through = defaultdict(set)                                    # point -> inside faces chosen at a decided point
    found, bands, kept, nodes, capped = 0, set(), [], [0], [False]

    def fits(v, faces):
        for k in through[v]:
            if k not in faces:
                return False
        for k, cyc in faces.items():
            if is_inside(k, cyc):
                for w in cyc:
                    if w in chosen and k not in chosen[w][1]:
                        return False
        return True

    def band(pick):
        faces = {}
        for v in region:
            for k, cyc in pick[v][1].items():
                if is_inside(k, cyc):
                    faces[k] = cyc
        by_edge = defaultdict(list)
        for k in faces:
            for e in k:
                by_edge[e].append(k)
        rot = {v: rotation_order(adj, pick[v][0], v) for v in region}
        pinch = set()
        for v in region:
            marked = set()
            for k in pick[v][1]:
                if k not in faces:
                    continue
                cyc = faces[k]
                j = cyc.index(v)
                a, b = cyc[(j - 1) % len(cyc)], cyc[(j + 1) % len(cyc)]
                i = rot[v].index(a)
                marked.add(i if rot[v][(i + 1) % 4] == b else (i - 1) % 4)
            if len(marked) == 2 and max(marked) - min(marked) == 2:
                pinch.add(v)
        return dict(faces=faces, by_edge=by_edge, rot=rot, chosen_at={v: set(pick[v][1]) for v in region},
                    pinch=pinch, boundary={e for e, fs in by_edge.items() if len(fs) == 1}, region=region)

    def rec(t):
        nonlocal found
        nodes[0] += 1
        if nodes[0] > node_cap:
            capped[0] = True
            return
        if t == len(order):
            mult = 1
            for u in region:
                mult *= chosen[u][2]
            found += mult
            b = band(chosen)
            sig = (frozenset(b["faces"]), tuple(sorted((v, tuple(b["rot"][v])) for v in region)))
            if sig not in bands:
                bands.add(sig)
                if len(kept) < max_keep:
                    kept.append(b)
            return
        v = order[t]
        for corners, faces, mult_v in opts[v]:
            if not fits(v, faces):
                continue
            chosen[v] = (corners, faces, mult_v)
            added = []
            for k, cyc in faces.items():
                if is_inside(k, cyc):
                    for w in cyc:
                        if k not in through[w]:
                            through[w].add(k)
                            added.append((w, k))
            rec(t + 1)
            for w, k in added:
                through[w].discard(k)
            del chosen[v]
            if capped[0]:
                return

    rec(0)
    return found, len(bands), kept, capped[0]


def band_character(band, walk):
    """The character of a closed walk of links read in a band alone: every point of the walk in the band's region,
    two band faces on each link, chosen at both ends. (None, why) otherwise."""
    if any(p not in band["rot"] for p in walk):
        return None, "a point of the walk is outside the region"
    return character_of_links(band, walk)


def local_failures(adj, point_options, holdable, radius=3):
    """The points round which no completion closes: v is a LOCAL FAILURE if no completion closes on the ball of
    `radius` steps round v (radius 3 holds every square and every hexagon through v). This depends on the graph and
    the rule alone, not on any search order."""
    return sorted(v for v in range(adj.shape[0])
                  if closing_completions(adj, ball(adj, v, radius), point_options, holdable, max_keep=0)[0] == 0)


def report_bands(adj, label, walks=(), point_options=None, labels=None):
    """The outcome words of the draft entry's item 6, read through bands. A region CARRIES A TWIST if every
    completion that closes on it gives a one-sided band there (its distinct bands all one-sided); where some are
    one-sided and some two-sided the counts are printed and no word is given. ALL TWO-SIDED: all points close and
    every band is two-sided. TWIST IN THE CURL: the curled part carries a twist. TWIST IN THE OPEN: the opened part
    does. TWIST ACROSS THE LIP: neither part carries a twist, and all points together close into a one-sided
    surface. NO SURFACE AT THE LIP: no completion closes on all points, and every local failure lies on a lip link
    or one step from one. NO SURFACE AT A FLAW: no completion closes on all points and some local failure lies
    elsewhere. `labels`, if given, names each point's part for the failure list."""
    if point_options is None:
        point_options = point_options_all(adj)
    holdable = holdable_faces(point_options)
    curled, opened, flawed, lip = regions(adj)
    n = adj.shape[0]
    print("  bands (the local criterion): curled points %d, opened %d, flawed %d; lip links %d; options per point "
          "%s; faces no band can hold %d of %d"
          % (len(curled), len(opened), len(flawed), len(lip), dict(sorted(Counter(len(o) for o in point_options).items())),
             sum(1 for k in {k for o in point_options for _c, f in o for k in f} if k not in holdable),
             len({k for o in point_options for _c, f in o for k in f})))
    verdict = {}
    for name, region in (("curled part", curled), ("opened part", opened), ("all points", set(range(n)))):
        if not region:
            print("    %s: no points" % name)
            verdict[name] = None
            continue
        count, distinct, kept, capped = closing_completions(adj, region, point_options, holdable, max_keep=512)
        if capped:
            print("    %s (%d points): the search passed its cap; not decided" % (name, len(region)))
            verdict[name] = None
            continue
        if count == 0:
            print("    %s (%d points): no completion closes on it" % (name, len(region)))
            verdict[name] = "none"
            continue
        kinds, chars = Counter(), {wname: Counter() for wname, _w in walks}
        for b in kept:
            if b["pinch"]:
                kinds[("pinched at %d point%s" % (len(b["pinch"]), "" if len(b["pinch"]) == 1 else "s"), 0, 0)] += 1
                continue
            ok, pieces = orientable(b)
            kinds[("two-sided" if ok else "one-sided", pieces, len(b["boundary"]))] += 1
            if name == "all points":
                for wname, walk in walks:
                    chars[wname][band_character(b, walk)[0]] += 1
        shown = sum(kinds.values())
        print("    %s (%d points): %d completion%s close on it, %d distinct band%s%s; bands: %s"
              % (name, len(region), count, "" if count == 1 else "s", distinct, "" if distinct == 1 else "s",
                 "" if shown == distinct else " (first %d read)" % shown,
                 ", ".join("%s%s: %d" % (side, "" if pieces == 0 else ", %d piece%s, boundary links %d"
                                         % (pieces, "" if pieces == 1 else "s", bd), c)
                           for (side, pieces, bd), c in sorted(kinds.items()))))
        if name == "all points":
            for wname, counts in chars.items():
                print("    character of %s, over the distinct closed surfaces: %s"
                      % (wname, dict(sorted(counts.items(), key=lambda kv: str(kv[0])))))
        sides = {side for (side, _p, _b) in kinds if side in ("one-sided", "two-sided")}
        verdict[name] = ("one-sided" if sides == {"one-sided"} else "two-sided" if sides == {"two-sided"}
                         else "pinched" if not sides else "disagree")
    fails = local_failures(adj, point_options, holdable)
    near_lip = {p for e in lip for p in e} | {int(w) for e in lip for p in e for w in adj[p]}
    if fails:
        where = Counter((labels[v] if labels else ("curled" if v in curled else "opened" if v in opened else "flawed"))
                        + (", on or beside the lip" if v in near_lip else ", away from the lip") for v in fails)
        print("    local failures (no completion closes on the 3-step ball round the point): %d points, %s"
              % (len(fails), dict(sorted(where.items()))))
    else:
        print("    local failures (no completion closes on the 3-step ball round the point): none")
    words = []
    if verdict.get("curled part") == "one-sided":
        words.append("TWIST IN THE CURL")
    if verdict.get("opened part") == "one-sided":
        words.append("TWIST IN THE OPEN")
    if verdict.get("all points") == "one-sided" and not words:
        words.append("TWIST ACROSS THE LIP")
    if verdict.get("all points") == "none":
        words.append("NO SURFACE AT THE LIP" if fails and all(v in near_lip for v in fails) else "NO SURFACE AT A FLAW")
    if verdict.get("all points") == "two-sided" and not words:
        words.append("ALL TWO-SIDED")
    if any(v == "disagree" for v in verdict.values()):
        words.append("(the closed surfaces disagree on %s)" % ", ".join(k for k, v in verdict.items() if v == "disagree"))
    print("  -> outcome words for %s: %s" % (label, "; ".join(words) or "none given"))


def uniform_choice_complex(adj, opp):
    """The same rotation (the opposite pairs `opp`, as slot pairs) at every point, each corner's unique square as
    face: for the 4-cube, where the rule ties three ways at every point."""
    n = adj.shape[0]
    corners = [p for p, pr in enumerate(PAIRS) if pr not in opp]
    faces, chosen_at = {}, [set() for _ in range(n)]
    for v in range(n):
        for p in corners:
            i, j = PAIRS[p]
            cyc = tuple(int(t) for t in shortest_cycle_points(adj, v, int(adj[v, i]), int(adj[v, j])))
            key = face_key(cyc)
            faces.setdefault(key, cyc)
            chosen_at[v].add(key)
    return complex_from(adj, faces, chosen_at, [corners] * n)


def orientable(cx):
    """Propagate face orientations across shared links: (orientable, number of connected pieces of faces)."""
    faces, by_edge = cx["faces"], cx["by_edge"]
    sign, ok, pieces = {}, True, 0

    def runs(f, p, q):                                            # +1 if face f, as oriented, runs p -> q
        cyc = faces[f]
        k = cyc.index(p)
        return sign[f] if cyc[(k + 1) % len(cyc)] == q else -sign[f]

    for start in faces:
        if start in sign:
            continue
        pieces += 1
        sign[start] = 1
        stack = [start]
        while stack:
            f = stack.pop()
            cyc = faces[f]
            for t in range(len(cyc)):
                p, q = cyc[t], cyc[(t + 1) % len(cyc)]
                for h in by_edge[frozenset((p, q))]:
                    if h == f:
                        continue
                    ch = faces[h]
                    kh = ch.index(p)
                    natural = 1 if ch[(kh + 1) % len(ch)] == q else -1
                    want = -runs(f, p, q) * natural             # h must run q -> p
                    if h not in sign:
                        sign[h] = want
                        stack.append(h)
                    elif sign[h] != want:
                        ok = False
    return ok, pieces


def ccw(cyc, sgn, v, rot_v):
    """+1 if the face `cyc`, oriented by sgn, passes v from rot_v[i] to rot_v[i + 1] (with the rotation's listed
    direction), -1 if against it, None if the face's corner at v is not a corner of v's rotation."""
    m = len(cyc)
    k = cyc.index(v)
    a, b = cyc[(k - 1) % m], cyc[(k + 1) % m]
    if sgn < 0:
        a, b = b, a
    if a not in rot_v or b not in rot_v:
        return None
    i = rot_v.index(a)
    if rot_v[(i + 1) % 4] == b:
        return 1
    if rot_v[(i - 1) % 4] == b:
        return -1
    return None


def character_of_links(cx, walk):
    """The mod-2 orientation character of a closed walk of points joined by links, or (None, why)."""
    o = 1
    for t in range(len(walk)):
        u, v = walk[t], walk[(t + 1) % len(walk)]
        fs = cx["by_edge"].get(frozenset((u, v)), [])
        if len(fs) != 2:
            return None, "link %d-%d lies in %d chosen faces" % (u, v, len(fs))
        arrived = []
        for f in fs:
            cu = ccw(cx["faces"][f], 1, u, cx["rot"][u])
            if cu is None:
                return None, "a face on link %d-%d is not a corner of the rotation at %d" % (u, v, u)
            cv = ccw(cx["faces"][f], o * cu, v, cx["rot"][v])    # oriented so that its ccw at u equals o
            if cv is None:
                return None, "a face on link %d-%d is not a corner of the rotation at %d" % (u, v, v)
            arrived.append(cv)
        if arrived[0] != arrived[1]:
            return None, "the two faces on link %d-%d disagree at %d: not a surface there" % (u, v, v)
        o = arrived[0]
    return (0 if o == 1 else 1), "ok"


def character_of_diagonals(cx, ring):
    """ring: cyclic list of (face key, exit point); face i exits at s_i, face i + 1 enters at s_i. Returns the mod-2
    character carried from face to face through each shared point's rotation, or (None, why)."""
    sgn = 1
    for t in range(len(ring)):
        f, s = ring[t]
        g = ring[(t + 1) % len(ring)][0]
        c = ccw(cx["faces"][f], sgn, s, cx["rot"][s])
        cg = ccw(cx["faces"][g], 1, s, cx["rot"][s])
        if c is None or cg is None:
            return None, "a face of the ring is not a corner of the rotation at %d" % s
        sgn = c * cg
    return (0 if sgn == 1 else 1), "ok"


# ---------------------------------------------------------------- the cycles

def follow(adj, start, k):
    """The closed walk from `start` following adjacency slot k (2 = up) until it returns."""
    walk, p = [start], int(adj[start, k])
    while p != start:
        walk.append(p)
        p = int(adj[p, k])
    return walk


def path_within(adj, src, dst, allowed):
    """A shortest walk of links from src to dst through points of `allowed` only (breadth first), or None."""
    prev = {src: None}
    q = deque([src])
    while q:
        x = q.popleft()
        if x == dst:
            break
        for y in adj[x]:
            y = int(y)
            if y in allowed and y not in prev:
                prev[y] = x
                q.append(y)
    if dst not in prev:
        return None
    path, x = [], dst
    while x is not None:
        path.append(x)
        x = prev[x]
    return path[::-1]


def square_through(adj, p, r, u):
    """The square with corner r - p - u and its far corner w (unique by the hard-core rule), as (cycle, w)."""
    w = [int(t) for t in adj[r] if t != p and any(int(s) == int(t) for s in adj[u])]
    if len(w) != 1:
        return None, None
    return (int(p), int(r), w[0], int(u)), w[0]


def opposite(cyc, s):
    return cyc[(cyc.index(s) + 2) % 4]


def zigzag(cx, adj, b, start, first_corner, cross):
    """A ring of diagonals grown face by face. `first_corner` = (slot_r, slot_u) names the first face's corner at
    `start`; at each exit point the next face is chosen by `cross`: 'junction' crosses the link whose two ends have
    different y, 'ring' the link whose ends share y, 'opposite' takes the face opposite in the rotation at the exit
    point (no coordinates used). Stops when the first (face, entry) recurs; cap 8 N faces. Returns (ring, closed)."""
    cyc, w = square_through(adj, start, int(adj[start, first_corner[0]]), int(adj[start, first_corner[1]]))
    if cyc is None:
        return [], False
    f = face_key(cyc)
    if f not in cx["faces"]:
        return [], False
    ring, state0, entry = [], (f, int(start)), int(start)
    for _ in range(8 * adj.shape[0]):
        cyc = cx["faces"][f]
        if len(cyc) != 4:
            return ring, False
        s = opposite(cyc, entry)
        ring.append((f, s))
        if cross == "opposite":
            rot = cx["rot"][s]
            k = cyc.index(s)
            corner = {cyc[(k - 1) % 4], cyc[(k + 1) % 4]}       # f's two neighbours of s
            if not corner <= set(rot):
                return ring, False
            pair = set(rot) - corner                             # the opposite corner's two neighbours
            g = [h for h in cx["chosen_at"][s] if h != f and set(cx["faces"][h]) >= pair | {s}]
        else:
            links = [e for e in f if s in e]
            want = [e for e in links if (xy(min(e), b)[1] != xy(max(e), b)[1]) == (cross == "junction")]
            if len(want) != 1:
                return ring, False
            g = [h for h in cx["by_edge"][want[0]] if h != f]
        if len(g) != 1:
            return ring, False
        f, entry = g[0], s
        if (f, entry) == state0:
            return ring, True
    return ring, False


def ring_from_points(cx, adj, pts):
    """A ring of diagonals given by its points (all of one kind): consecutive points must be the opposite corners of
    one square (exactly two common neighbours), and that square must be a face under the rule. Returns (ring, why)."""
    ring = []
    for t in range(len(pts)):
        p, q = int(pts[t]), int(pts[(t + 1) % len(pts)])
        common = [int(c) for c in adj[p] if any(int(d) == int(c) for d in adj[q])]
        if len(common) != 2:
            return None, "points %d and %d are not opposite corners of a square" % (p, q)
        key = face_key((p, common[0], q, common[1]))
        if key not in cx["faces"]:
            return None, "the square through points %d and %d is not a face under the rule" % (p, q)
        ring.append((key, q))
    return ring, "ok"


def inner_square(cx, adj, c):
    """The four faces at c in rotation order, each exited at the next neighbour: the 45-degree square round c."""
    rot, ring = cx["rot"][c], []
    for i in range(4):
        a, b_ = rot[i], rot[(i + 1) % 4]
        cyc, _w = square_through(adj, c, a, b_)
        if cyc is None or face_key(cyc) not in cx["faces"]:
            return []
        ring.append((face_key(cyc), b_))
    return ring


# ---------------------------------------------------------------- isomorphism and widths

def iso(adj1, adj2):
    """Graph isomorphism of two neighbour arrays (igraph, or networkx VF2 if igraph is missing)."""
    if adj1.shape != adj2.shape:
        return False
    if ig is not None:
        def toig(adj):
            es = {(min(u, int(v)), max(u, int(v))) for u in range(adj.shape[0]) for v in adj[u]}
            return ig.Graph(n=adj.shape[0], edges=sorted(es))
        return bool(toig(adj1).isomorphic(toig(adj2)))
    def tonx(adj):
        g = nx.Graph()
        for u in range(adj.shape[0]):
            for v in adj[u]:
                g.add_edge(u, int(v))
        return g
    return nx.is_isomorphic(tonx(adj1), tonx(adj2))


def lattice_width(w1, w2, reach=6):
    """The shortest closed loop of a lattice torus Z^2 / <w1, w2> that cannot be shrunk: the least |a| + |b| over the
    non-zero lattice vectors (exact for the wraps given, searched over small multiples)."""
    best = None
    for s in range(-reach, reach + 1):
        for t in range(-reach, reach + 1):
            if s == 0 and t == 0:
                continue
            a, b = s * w1[0] + t * w2[0], s * w1[1] + t * w2[1]
            d = abs(a) + abs(b)
            best = d if best is None else min(best, d)
    return best


def links_changed(adj1, adj2):
    e1 = {frozenset((u, int(v))) for u in range(adj1.shape[0]) for v in adj1[u]}
    e2 = {frozenset((u, int(v))) for u in range(adj2.shape[0]) for v in adj2[u]}
    return len(e1 - e2), len(e2 - e1)


# ---------------------------------------------------------------- reporting

def header(name, adj):
    n = adj.shape[0]
    print("=" * 110)
    col = two_colour(adj)
    print("%s: N = %d; valid (4-regular, simple, hard-core, no cap) = %s; bipartite = %s; S = %d (%.3f N); X = %d"
          % (name, n, bool(is_valid(adj, NO_CAP)), col is not None, int(total_squares(adj)),
             total_squares(adj) / n, int(surplus(adj))))
    links = Counter(int(squares_on_edge(adj, u, int(v))) for u in range(n) for v in adj[u] if int(v) > u)
    per_point = Counter(sum(int(squares_on_edge(adj, u, int(v))) for v in adj[u]) // 2 for u in range(n))
    print("  all squares: links by squares carried %s; squares per point %s; a surface by itself: %s"
          % (dict(sorted(links.items())), dict(sorted(per_point.items())),
             "yes (every link in two squares)" if set(links) == {2} else "no (a link carries three squares, or one)"))
    return col is not None


def surface_line(cx):
    if not cx["surface"]:
        bad = bad_points(cx)
        return ("the chosen faces do NOT close into a surface; points where a face is not chosen: %d" % len(bad), bad)
    ok, pieces = orientable(cx)
    kind = ("torus" if ok and cx["chi"] == 0 else "Klein bottle" if cx["chi"] == 0 else
            "sphere" if cx["chi"] == 2 else "chi = %d, %s" % (cx["chi"], "orientable" if ok else "one-sided"))
    return ("a closed surface: connected pieces %d, V - E + F = %d, orientable %s (%s)" % (pieces, cx["chi"], ok, kind),
            [])


def describe(name, adj, b, a=None, rings=True, lines=((0, 0),), extra_points=()):
    header(name, adj)
    options = rule_options(adj)[0]
    same, diff = tie_census(adj, options)
    cx = face_complex(adj)
    geo = cx["geo"]
    types = Counter(tuple("inf" if k >= INF else k for k in t) for t in geo["types"])
    print("  under the face rule: vertex types %s; ties between rotations of the SAME type %d, of different types %d "
          "(the eq45 counter: %d); corners of length inf %d"
          % (dict(types), same, diff, int(geo["ties"].sum()), cx["infinite"]))
    print("  chosen faces %d, by length %s; chosen at every point of theirs %d; links in exactly two chosen faces "
          "%d of %d; squares of the graph not faces %d"
          % (len(cx["faces"]), dict(cx["face_lengths"]), len(cx["consistent"]), cx["on_two"], len(cx["edges"]),
             int(total_squares(adj)) - sum(1 for c in cx["faces"].values() if len(c) == 4)))
    line, bad = surface_line(cx)
    print("  -> " + line + ((" (e.g. %s)" % [xy(p, b) for p in bad[:8]]) if bad else ""))
    if not rings or not cx["surface"]:
        return cx
    # cycles of links
    for (x0, y0) in lines:
        s = index(x0, y0, a, b)
        walk = follow(adj, s, 2)
        ch, why = character_of_links(cx, walk)
        print("  links, line along (up) from %s: length %d, character %s%s"
              % ((x0, y0), len(walk), ch, "" if why == "ok" else " [" + why + "]"))
    for y0 in (0, b - 1):
        walk = follow(adj, index(0, y0, a, b), 0)
        ch, why = character_of_links(cx, walk)
        print("  links, ring round (ring +) at y = %d: length %d, character %s%s"
              % (y0, len(walk), ch, "" if why == "ok" else " [" + why + "]"))
    # rings of diagonals
    for c in [index(1, 1, a, b)] + list(extra_points):
        ring = inner_square(cx, adj, c)
        ch, why = character_of_diagonals(cx, ring) if ring else (None, "a face at the point is not chosen")
        print("  diagonals, inner square round %s: %d faces, character %s%s"
              % (xy(c, b), len(ring), ch, "" if why == "ok" else " [" + why + "]"))
    for y0 in (0, b - 1):
        ring, closed = zigzag(cx, adj, b, index(0, y0, a, b), (0, 2 if y0 == 0 else 3), "junction")
        ch, why = character_of_diagonals(cx, ring) if closed else (None, "did not close")
        pts = [xy(s, b) for _f, s in ring]
        print("  diagonals, zigzag round the curl between rings %d and %d: %d faces, exits %s, character %s%s"
              % (y0, (y0 + 1) % b if y0 == 0 else (y0 + 1) % b, len(ring), pts[:4], ch,
                 "" if why == "ok" else " [" + why + "]"))
    for x0 in sorted(set(range(min(a, 4))) | {a // 2}):              # a // 2: the strip x -> 1 - x maps to itself
        ring, closed = zigzag(cx, adj, b, index(x0, 0, a, b), (0, 2), "ring")
        ch, why = character_of_diagonals(cx, ring) if closed else (None, "did not close")
        print("  diagonals, zigzag along from %s (between columns %d and %d): %d faces, character %s%s"
              % ((x0, 0), x0, (x0 + 1) % a, len(ring), ch, "" if why == "ok" else " [" + why + "]"))
    for x0 in range(min(a, 4)):
        ring, closed = zigzag(cx, adj, b, index(x0, 0, a, b), (0, 2), "opposite")
        ch, why = character_of_diagonals(cx, ring) if closed else (None, "did not close")
        print("  diagonals, straight 45-degree line from %s (opposite face at each exit): %d faces, character %s%s"
              % ((x0, 0), len(ring), ch, "" if why == "ok" else " [" + why + "]"))
    # rings of diagonals given by their points: closing after ONE pass along, which on a surface closed through a
    # reflection means a kink at a point the reflection fixes (the regular zigzag and the straight line above close
    # smoothly only after two passes)
    for x0 in sorted({0, 1, a // 2}):
        pts = [index(x0 + (t % 2), t, a, b) for t in range(b)]
        ring, why = ring_from_points(cx, adj, pts)
        ch, why = character_of_diagonals(cx, ring) if ring else (None, why)
        print("  diagonals, one-pass zigzag through column %d, points %s ... (%d faces): character %s%s"
              % (x0, [xy(p, b) for p in pts[:3]], b, ch, "" if why == "ok" else " [" + why + "]"))
    for dx in (2, a):                                             # crooked rings: more steps one way than the other
        if (b + dx) % 2 or b < dx:
            continue
        plus, minus = (b + dx) // 2, (b - dx) // 2
        steps = [1] * plus + [-1] * minus
        x, pts = 0, []
        for t in range(b):
            pts.append(index(x, t, a, b))
            x += steps[t]
        ring, why = ring_from_points(cx, adj, pts)
        ch, why = character_of_diagonals(cx, ring) if ring else (None, why)
        print("  diagonals, crooked ring from (0, 0), steps %s then the closing diagonal through the last junction "
              "(%d faces): character %s%s"
              % ("+" * plus + "-" * minus, b, ch, "" if why == "ok" else " [" + why + "]"))
    return cx


def report_completions(adj, label, cap=300000):
    summary, first = enumerate_completions(adj, cap)
    print("  completions of the rule (%d tied points, every tie broken every way, every ambiguous corner given each "
          "shortest cycle): %d tried%s; %d close into a surface"
          % (summary["tied"], summary["total"], " (CAPPED at %d)" % cap if summary["capped"] else "",
             summary["closing"]))
    for (chi, ok), c in sorted(summary["kinds"].items()):
        print("    closing surfaces with V - E + F = %d, orientable %s: %d" % (chi, ok, c))
    return first


def flat_klein_bottles(n):
    """Every a x b Klein grid with a b = n (a even, both families) that is valid, bipartite and flat, with its kind."""
    found = []
    for a in range(4, n // 3 + 1, 2):
        if n % a:
            continue
        b = n // a
        if b < 3:
            continue
        c = 0 if b % 2 == 0 else 1
        adj = klein_grid(a, b, c)
        if not is_valid(adj, NO_CAP) or two_colour(adj) is None:
            continue
        if int(total_squares(adj)) != n or int(surplus(adj)) != 0:
            continue
        cx = face_complex(adj)
        ok, pieces = orientable(cx)
        found.append((a, b, c, cx["surface"], cx["chi"], ok))
    return found


def main():
    print("twist_character_check, 23 October 2026 (revised the same day): the mod-2 orientation character under the "
          "eq45 face rule, and the seam shift of lattice tori, on BUILT graphs only (nothing from results/).")
    print("Character 0: a band carried round the cycle comes back as it left (annulus). 1: it comes back flipped "
          "(Mobius). None: undefined there, with the reason.")

    # ---- A. the tube and its zero-cost family; flat tori; flat Klein grids of both families
    for length in (8, 12, 16):
        tube, _ = torus(4, length, NO_CAP)
        describe("tube 4 x %d" % length, tube, length, a=4, lines=((0, 0), (1, 0)))
        refl, _ = ring_bundle(length, [2, 1, 0, 3])
        describe("reflected closure of the 4 x %d tube (ring L - 1 to ring 0 through x -> 2 - x)" % length,
                 refl, length, a=4, lines=((0, 0), (1, 0), (2, 0), (3, 0)))
        half, _ = ring_bundle(length, [2, 3, 0, 1])
        describe("half-turn closure of the 4 x %d tube (through x -> x + 2)" % length, half, length, a=4,
                 lines=((0, 0), (1, 0)))
        print("  moves from the tube: tube -> reflected closure removes %d links and adds %d (one switch); "
              "tube -> half-turn closure removes %d and adds %d (two switches); reflected -> half-turn removes %d "
              "and adds %d (one switch: the zero-cost family is the chain tube - reflected - half-turn, O150)"
              % (links_changed(tube, refl) + links_changed(tube, half) + links_changed(refl, half)))
        print("  pairwise isomorphic? tube~reflected %s, tube~half-turn %s, reflected~half-turn %s"
              % (iso(tube, refl), iso(tube, half), iso(refl, half)))
        for name, g in (("tube", tube), ("reflected closure", refl), ("half-turn closure", half)):
            report_bands(g, "the %s, L = %d" % (name, length),
                         walks=[("the line along from (1, 0)", follow(g, index(1, 0, 4, length), 2)),
                                ("the ring round at y = 0", follow(g, index(0, 0, 4, length), 0))])
    for a, b in ((6, 8), (8, 8)):
        adj, _ = torus(a, b, NO_CAP)
        describe("flat torus %d x %d" % (a, b), adj, b, a=a, lines=((0, 0), (1, 0)))
    for a, b in ((6, 6), (6, 8), (8, 8), (6, 10), (8, 12)):
        describe("flat Klein grid %d x %d (last row to first through x -> -x; b even)" % (a, b), klein_grid(a, b, 0),
                 b, a=a, lines=((0, 0), (1, 0), (2, 0), (a // 2, 0)))
    for a, b in ((8, 5), (8, 7), (8, 11), (8, 13), (12, 5), (16, 5), (6, 5), (6, 7), (10, 5), (10, 7)):
        describe("flat Klein grid %d x %d (last row to first through x -> 1 - x; b odd)" % (a, b),
                 klein_grid(a, b, 1), b, a=a, lines=((0, 0), (1, 0), (2, 0), (a // 2, 0)))
    for a, b, c in ((6, 6, 0), (8, 5, 1)):
        g = klein_grid(a, b, c)
        print("=" * 110)
        print("flat Klein grid %d x %d (x -> %d - x), read through bands:" % (a, b, c))
        report_bands(g, "the flat Klein grid %d x %d" % (a, b),
                     walks=[("the line along from (0, 0)", follow(g, index(0, 0, a, b), 2)),
                            ("the line along from (1, 0)", follow(g, index(1, 0, a, b), 2))])

    # ---- B. the 4-cube: the rule ties three ways at every point
    adj, _ = torus(4, 4, NO_CAP)
    cx = describe("4-cube (4 x 4 torus; six squares at every point)", adj, 4, a=4, rings=False)
    options = rule_options(adj)[0]
    print("  least-alpha rotations per point: %s (all of type %s): the rule leaves the faces undetermined; the eq45 "
          "slot tie-break above gives %d links in two faces of %d"
          % (Counter(len(o) for o in options), options[0][0][0], cx["on_two"], len(cx["edges"])))
    for opp in ROTATIONS:
        ucx = uniform_choice_complex(adj, opp)
        line, _bad = surface_line(ucx)
        print("  the same rotation at every point (opposite slot pairs %s): %s" % (opp, line))
    report_search(adj, "4-cube", max_keep=400)
    report_bands(adj, "the 4-cube", walks=[("the line along from (1, 0)", follow(adj, index(1, 0, 4, 4), 2))])

    # ---- C. the eq45 handle as built, and the control with one splice mirrored
    for mirror in (False, True):
        adj, side, seg = handle_mirror(14, 14, 3, mirror)
        if not mirror:
            adj0, _s0, _g0 = handle_graph(14, 14, 3)
            assert links_changed(adj0, adj) == (0, 0), "handle_mirror(False) must be handle_graph link for link"
        cx = describe("flat 14 x 14 torus with a 3-layer circumference-4 handle spliced in%s (eq45 brief Sec. 2)"
                      % (", the splice at end b MIRRORED (control)" if mirror else ", as built"),
                      adj, 14, a=14, rings=False)
        layer = {p: i // 4 for i, p in enumerate(seg)}
        bad = bad_points(cx)
        print("  under the slot tie-break, points at which some face is not chosen: %d; in the handle by layer %s "
              "(layer 1 is the middle ring); in the lattice %d"
              % (len(bad), dict(sorted(Counter(layer[p] for p in bad if p in layer).items())),
                 sum(1 for p in bad if p not in layer)))
        mid = seg[4:8]
        ch, why = character_of_links(cx, mid)
        print("  links, the handle's middle ring under the slot tie-break: character %s%s"
              % (ch, "" if why == "ok" else " [" + why + "]"))
        options, lengths, counts = rule_options(adj)
        tied = [v for v in range(adj.shape[0]) if len(options[v]) > 1]
        print("  tied points: %d, in the handle by layer %s, in the lattice %d; chosen corners with more than one "
              "shortest cycle (under the first option): %d"
              % (len(tied), dict(sorted(Counter(layer[p] for p in tied if p in layer).items())),
                 sum(1 for p in tied if p not in layer),
                 sum(1 for v in range(adj.shape[0]) for p in options[v][0][1] if counts[v, p] > 1)))
        first = report_completions(adj, "handle")
        report_search(adj, "handle")
        lattice0 = set(range(adj.shape[0])) - set(seg)
        col0 = [seg[4 * t] for t in range(len(seg) // 4)]
        ends = ([int(w) for w in adj[col0[0]] if int(w) in lattice0], [int(w) for w in adj[col0[-1]] if int(w) in lattice0])
        walk0 = col0 + path_within(adj, ends[1][0], ends[0][0], lattice0)
        report_bands(adj, "the handle%s" % (" with one splice mirrored" if mirror else " as built"),
                     walks=[("along the handle's column 0 and back through the lattice", walk0),
                            ("the handle's middle ring", mid)])
        if first is not None:
            ok, pieces = orientable(first)
            ch, why = character_of_links(first, mid)
            print("  the closing completion: V - E + F = %d, orientable %s; the middle ring's character %s%s"
                  % (first["chi"], ok, ch, "" if why == "ok" else " [" + why + "]"))
            # a cycle ALONG the handle: up one column of the handle from the splice at end a to the splice at end b,
            # then back through the lattice by a shortest walk that avoids the handle (where does a one-sided
            # handle carry its twist: round its ring, or along it?)
            lattice = set(range(adj.shape[0])) - set(seg)
            h = len(seg) // 4
            for j in range(4):
                col = [seg[4 * t + j] for t in range(h)]
                pa = [int(w) for w in adj[col[0]] if int(w) in lattice]
                pb = [int(w) for w in adj[col[-1]] if int(w) in lattice]
                if len(pa) != 1 or len(pb) != 1:
                    print("  column %d of the handle has no single lattice neighbour at an end (%s, %s)" % (j, pa, pb))
                    continue
                back = path_within(adj, pb[0], pa[0], lattice)
                walk = col + back
                ch, why = character_of_links(first, walk)
                print("  links, along the handle's column %d and back through the lattice (length %d): character %s%s"
                      % (j, len(walk), ch, "" if why == "ok" else " [" + why + "]"))

    # ---- D. a hand-built lip: a stretch of tube four around joined to a stretch of sheet six around
    for l4, l6 in ((8, 6), (12, 8)):
        adj, tubes, sheet, tjoints, sjoints = lip_tube_to_sheet(l4, l6)
        cx = describe("hand-built lip: %d rings of tube (4 around) joined to %d rings of sheet (6 around) through a "
                      "chorded ring at each joint, closed into a torus" % (l4, l6), adj, 1, rings=False)
        n = adj.shape[0]
        sq = {v: sum(int(squares_on_edge(adj, v, int(w))) for w in adj[v]) // 2 for v in range(n)}
        interior = [v for v in tubes if v not in tjoints[0] + tjoints[1]]
        print("  squares per point: tube interior %s; the two joint tube rings %s; sheet %s"
              % (dict(Counter(sq[v] for v in interior)), dict(Counter(sq[v] for v in tjoints[0] + tjoints[1])),
                 dict(Counter(sq[v] for v in sheet))))
        options, lengths, counts = rule_options(adj)
        tied = [v for v in range(n) if len(options[v]) > 1]
        where = Counter("joint tube ring" if v in tjoints[0] + tjoints[1] else "joint sheet ring"
                        if v in sjoints[0] + sjoints[1] else "tube interior" if v in tubes else "sheet" for v in tied)
        print("  tied points: %d, at %s; their least-alpha types: %s"
              % (len(tied), dict(where), Counter(tuple(k for k, _ in options[v]) for v in tied)))
        bad = bad_points(cx)
        print("  under the slot tie-break, points at which some face is not chosen: %d" % len(bad))
        kept = report_search(adj, "lip", max_keep=2)
        first = kept[0] if kept else None
        chord_ends = [S for S in sjoints[0] if sum(1 for w in adj[S] if int(w) in sjoints[0]) == 3]
        print("  the chord's end points on joint sheet ring 0: %s; squares %s; least-alpha options %s"
              % (chord_ends, [sq[v] for v in chord_ends], [[k for k, _c in options[v]] for v in chord_ends]))
        lip_walks = [("the line along tube column 0 and sheet column 1",
                      [4 * t + 0 for t in range(l4)] + [4 * l4 + 6 * s + 1 for s in range(l6)]),
                     ("the ring round the tube interior (ring 1)", [4 * 1 + i for i in range(4)]),
                     ("the ring round the sheet interior (ring 2)", [4 * l4 + 6 * 2 + j for j in range(6)])]
        part = {v: ("joint tube ring" if v in tjoints[0] + tjoints[1] else "joint sheet ring, chord end"
                    if v in sjoints[0] + sjoints[1] and sum(1 for w in adj[v] if int(w) in sjoints[0] + sjoints[1]) == 3
                    else "joint sheet ring, paired" if v in sjoints[0] + sjoints[1] else "tube interior"
                    if v in tubes else "sheet interior") for v in range(n)}
        print("  parts by label: %s" % dict(sorted(Counter(part.values()).items())))
        report_bands(adj, "the hand-built lip (N = %d)" % n, walks=lip_walks, labels=part)
        if first is not None:
            ok, pieces = orientable(first)
            print("  the first closing completion: V - E + F = %d, orientable %s, faces by length %s"
                  % (first["chi"], ok, dict(first["face_lengths"])))
            walks = [("ring round the tube, interior ring 1", [4 * 1 + i for i in range(4)]),
                     ("ring round the tube, joint ring", tjoints[0]),
                     ("ring round the sheet, interior ring 2", [4 * l4 + 6 * 2 + j for j in range(6)]),
                     ("ring round the sheet, joint ring (the chorded one)", sjoints[0]),
                     ("line along, tube column 0 through sheet column 1",
                      [4 * t + 0 for t in range(l4)] + [4 * l4 + 6 * s + 1 for s in range(l6)]),
                     ("line along, tube column 2 through sheet column 5",
                      [4 * t + 2 for t in range(l4)] + [4 * l4 + 6 * s + 5 for s in range(l6)]),
                     ("line along the sheet's columns 0 and 3, closed through the two chords",
                      [4 * l4 + 6 * s + 0 for s in range(l6)] + [4 * l4 + 6 * s + 3 for s in reversed(range(l6))])]
            for name, walk in walks:
                ch, why = character_of_links(first, walk)
                print("  links, %s: length %d, character %s%s" % (name, len(walk), ch, "" if why == "ok" else " [" + why + "]"))

    # ---- E. the seam shift: O116's helical tori, the half-turn closure, and which "shift by two" is which
    print("=" * 110)
    print("Seam shift (the torsion r of the twisted grids): the 4 x 16 tube with its RING seam shifted by r (O116's "
          "twisted_tube: a walk round the ring arrives r steps along; wraps (4, r) and (0, L)), against the half-turn "
          "closure (the JUNCTION seam shifted by 2; wraps (4, 0) and (2, L); flat.graph(4, 2, L) of O119).")
    L = 16
    hel = {r: twisted_tube(L, r) for r in (0, 2, -2, 4, 6, 8)}
    for r, adj in hel.items():
        cx = face_complex(adj)
        ok, pieces = orientable(cx)
        print("  ring seam shift %+d: valid %s, bipartite %s, S = %d, X = %d (flat: %s); width by shells %s, by the "
              "lattice %d; surface %s, V - E + F = %d, orientable %s"
              % (r, bool(is_valid(adj, NO_CAP)), two_colour(adj) is not None, int(total_squares(adj)),
                 int(surplus(adj)), int(total_squares(adj)) == adj.shape[0] and int(surplus(adj)) == 0,
                 shell_width(adj), lattice_width((4, r), (0, L)), cx["surface"], cx["chi"], ok))
    shifts = (0, 2, 4, 6, 8)
    print("  pairwise isomorphic among ring seam shifts %s:" % (shifts,))
    for r1, r2 in itertools.combinations(shifts, 2):
        print("    shift %d ~ shift %d: %s" % (r1, r2, iso(hel[r1], hel[r2])))
    print("  shift +2 ~ shift -2 (mirror images): %s" % iso(hel[2], hel[-2]))
    half, _ = ring_bundle(L, [2, 3, 0, 1])
    print("  half-turn closure of the 4 x %d tube: width by shells %s, by the lattice %d; ~ flat.graph(4, 2, %d) "
          "(wraps (4, 0), (2, L)): %s; ~ ring seam shift 2 (O116's tube twisted by two): %s; ~ ring seam shift 0 "
          "(the tube): %s"
          % (L, shell_width(half), lattice_width((4, 0), (2, L)), L, iso(half, flat_graph(4, 2, L)),
             iso(half, hel[2]), iso(half, hel[0])))
    tube, _ = torus(4, L, NO_CAP)
    print("  links changed from the tube: to ring seam shift 2, %d removed and %d added (every seam link); to the "
          "half-turn closure, %d and %d" % (links_changed(tube, hel[2]) + links_changed(tube, half)))
    cx2 = face_complex(hel[2])
    chs = []
    for start in (0, 1, 2, 3):
        walk = follow(hel[2], index(start, 0, 4, L), 2)             # slot 2 is 'up' in twisted_tube too
        chs.append(character_of_links(cx2, walk)[0])
    ring6 = [index(0, 0, 4, L), index(1, 0, 4, L), index(2, 0, 4, L), index(3, 0, 4, L),
             index(0, L - 2, 4, L)]                                  # (3,0) -> (0, -2): the six-step way round
    ring6 = ring6 + [index(0, L - 1, 4, L)]
    print("  ring seam shift 2: characters of the four lines along %s; of the six-step loop round %s "
          "(a torus: every cycle 0, though it is a different graph from the tube and from the half-turn closure)"
          % (chs, character_of_links(cx2, ring6)))

    # ---- F. counting only: flat Klein bottles at N = 4L, both families
    print("=" * 110)
    print("Counting only (no run): a reflected closure of the 4 x L tube has N = 4L, S = 1.25 N, X = N, "
          "H = 4 (lambda - 1) N; a flat Klein grid a x b has S = N, X = 0, H = 0 at every lambda. Flat Klein grids of "
          "the two families built here that are valid at N = 4L (a x b, closed through x -> -x for b even, "
          "x -> 1 - x for b odd); 'at least': the classification (Thomassen 1991) is not read, so other flat Klein "
          "bottles may exist at sizes listed as none.")
    for length in range(8, 50, 2):
        n = 4 * length
        found = flat_klein_bottles(n)
        print("  L = %2d, N = %3d: %s" % (length, n, ", ".join("%d x %d (x -> %d - x; %s, chi %d, orientable %s)"
                                                            % (a, b, c, "closed" if s else "NOT closed", chi, ok)
                                                            for a, b, c, s, chi, ok in found) or "none built"))
    print("done")


if __name__ == "__main__":
    main()

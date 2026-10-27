"""Sandbox look (exploratory; rule 16), 26 October 2026: are the toy's 4-cycles faces of cubes, and is its curl local?
Usage:

    python sandbox/cube_face_look.py [n_states]

Task B of `docs/HANDOFF_2026-10-26.md`, from `docs/reading/notes/2026-10-26_paired_defects_gauss_bonnet.md` section 5,
checks 1 to 4. With six links a flat link carries four squares (4-cycles); curl on a link is a square above four
(S_e > 4), anticurl a square below (S_e < 4) (VISION Update 105). A look can kill a claim but never crown one.

Does the starting state obey every rule the owner has adopted (TASKS, O159 section, item 1)? The flat 6 x 6 x 8 torus
does: S = 3N exactly, every link at four squares. The rod 4 x 4 x 18 does NOT: its wrap-around 4-cycles put a fifth
square on every link along the two curled directions, S = 3.5N, which her hard rule (squares held at exactly 3N for six
links) forbids. The saved end states of the push look all started from that rod and so do not obey it either. This look
reads them anyway, to find what a rule-obeying X would have to differ in, and says so.

What is computed, all exact (enumeration):
1. Every 4-cycle of the graph, and every 3-cube subgraph (eight points, twelve links, wired as Q3). A 4-cycle is a
   "cube face" if it is one of the six faces of at least one 3-cube subgraph, otherwise "no cube". On the built tori a
   second, embedding-based reading is added: a 4-cycle "wraps" if its coordinate displacements round the cycle do not
   sum to zero (it goes round a short direction). On the saved end states the labels keep the rod's coordinates, so the
   wrap reading there is nominal only and is marked so.
2. Curl and anticurl per link, and the squares on each link split by class: how many of a link's squares are cube faces,
   how many are not, how many wrap.
3. C, the number of 3-cube subgraphs, against N; and per link, S_e against the number of cubes round it (the note's
   manifold test, first half; whether the cells round a link form one cycle is not checked here).
4. Local neutrality: for each point and radius r = 1, 2, 3, Q(r) = sum of (S_e - 4) over links with both ends within
   graph distance r of the point. Baseline: the same statistic with the per-link values (S_e - 4) shuffled over the
   links (positions shuffled), 100 shuffles. "Small" is declared before running: Q(r) is small (neutral beyond r) if
   the spread of Q(r) over points (its standard deviation) is no larger than the shuffled spread at that r, and its
   largest |Q(r)| is no larger than the shuffled largest. A total of zero with lobes wider than chance is not small.

Words declared before running (for the saved states; the tori are the controls whose answer is known by arithmetic):
  ALL FACES      every 4-cycle, curl included, is a cube face;
  WRAP ONLY      curl sits only on 4-cycles that are not cube faces (the note's "all wrap-around");
  MIXED          curl on both classes.
  NEUTRAL / LOBED for check 4 by the definition of "small" above.
"""
import sys
from collections import Counter, defaultdict
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from graphity.cqg_d import torus  # noqa: E402

OUT = ROOT / "sandbox" / "out" / "pair_tie_push"
N_SHUFFLE = 100
RADII = (1, 2, 3)


def links_of(adj):
    n = adj.shape[0]
    return [(u, int(v)) for u in range(n) for v in adj[u] if 0 <= v and u < v]


def nbrs(adj):
    return [set(int(v) for v in adj[u] if v >= 0) for u in range(adj.shape[0])]


def four_cycles(nb):
    """Each 4-cycle once, as (u, v, x, w) with u its smallest point, v < w its neighbors in the cycle, x opposite.
    (A first version required only u < x and found every cycle twice, once from each diagonal.)"""
    cycles = []
    n = len(nb)
    for u in range(n):
        ns = sorted(nb[u])
        for i in range(len(ns)):
            v = ns[i]
            if v < u:
                continue
            for j in range(i + 1, len(ns)):
                w = ns[j]
                for x in nb[v] & nb[w]:
                    if x > u:
                        cycles.append((u, v, x, w))
    return cycles


def edge(a, b):
    return (a, b) if a < b else (b, a)


def cycle_edges(c):
    u, v, x, w = c
    return frozenset([edge(u, v), edge(v, x), edge(x, w), edge(w, u)])


def cubes(nb):
    """Every 3-cube subgraph, once, as a frozenset of its twelve links; with its six faces (link sets)."""
    found = {}
    n = len(nb)
    for u in range(n):
        ns = sorted(nb[u])
        for i in range(len(ns)):
            a = ns[i]
            for j in range(i + 1, len(ns)):
                b = ns[j]
                for k in range(j + 1, len(ns)):
                    c = ns[k]
                    for xab in (nb[a] & nb[b]) - {u}:
                        for xac in (nb[a] & nb[c]) - {u, xab}:
                            for xbc in (nb[b] & nb[c]) - {u, xab, xac}:
                                for y in (nb[xab] & nb[xac] & nb[xbc]) - {a, b, c, u}:
                                    pts = {u, a, b, c, xab, xac, xbc, y}
                                    if len(pts) != 8:
                                        continue
                                    faces = [frozenset([edge(u, a), edge(a, xab), edge(xab, b), edge(b, u)]),
                                             frozenset([edge(u, a), edge(a, xac), edge(xac, c), edge(c, u)]),
                                             frozenset([edge(u, b), edge(b, xbc), edge(xbc, c), edge(c, u)]),
                                             frozenset([edge(a, xab), edge(xab, y), edge(y, xac), edge(xac, a)]),
                                             frozenset([edge(b, xab), edge(xab, y), edge(y, xbc), edge(xbc, b)]),
                                             frozenset([edge(c, xac), edge(xac, y), edge(y, xbc), edge(xbc, c)])]
                                    key = frozenset().union(*faces)
                                    if len(key) == 12 and key not in found:
                                        found[key] = faces
    return found


def coords_of(dims):
    """Coordinates of torus(dims)'s numbering, checked against the wiring (every link a unit step in one axis)."""
    adj, _ = torus(dims)
    n = adj.shape[0]
    xyz = np.array(np.unravel_index(np.arange(n), dims)).T
    for u in range(n):
        for v in adj[u]:
            d = (xyz[int(v)] - xyz[u]) % np.array(dims)
            steps = [(d[i] in (1, dims[i] - 1)) for i in range(len(dims))]
            if sum(steps) != 1 or sum(d != 0) != 1:
                raise RuntimeError("torus numbering is not C-order; wrap reading unavailable")
    return xyz


def wraps(c, xyz, dims):
    """Does the cycle's displacement round it fail to sum to zero? Minimal image per step; a step of L/2 is read as +L/2
    (ambiguous at side 4: on the undamaged lattice every step is one unit, so it does not arise there)."""
    pts = [c[0], c[1], c[2], c[3], c[0]]
    total = np.zeros(len(dims), dtype=int)
    for a, b in zip(pts[:-1], pts[1:]):
        d = (xyz[b] - xyz[a]) % np.array(dims)
        d = np.where(d > np.array(dims) // 2, d - np.array(dims), d)
        total += d
    return bool(np.any(total != 0))


def q_local(adj, links, charge, radii, rng, n_shuffle):
    """Q(r) per point and the shuffled baseline. Returns {r: (actual array, shuffled std mean, shuffled max mean)}."""
    n = adj.shape[0]
    nb = nbrs(adj)
    balls = {r: [] for r in radii}
    for s in range(n):
        seen = {s}
        frontier = [s]
        for r in range(1, max(radii) + 1):
            nxt = []
            for v in frontier:
                for w in nb[v]:
                    if w not in seen:
                        seen.add(w)
                        nxt.append(w)
            frontier = nxt
            if r in balls:
                balls[r].append(frozenset(seen))
    link_idx = {e: i for i, e in enumerate(links)}
    masks = {}
    for r in radii:
        m = np.zeros((n, len(links)), dtype=bool)
        for s, ball in enumerate(balls[r]):
            for e, i in link_idx.items():
                if e[0] in ball and e[1] in ball:
                    m[s, i] = True
        masks[r] = m
    out = {}
    for r in radii:
        actual = masks[r] @ charge
        stds, maxs = [], []
        for _ in range(n_shuffle):
            sh = masks[r] @ rng.permutation(charge)
            stds.append(sh.std())
            maxs.append(np.abs(sh).max())
        out[r] = (actual, float(np.mean(stds)), float(np.mean(maxs)))
    return out


def survey(name, adj, xyz=None, dims=None, nominal=False, rng=None):
    n = adj.shape[0]
    nb = nbrs(adj)
    links = links_of(adj)
    cyc = four_cycles(nb)
    cb = cubes(nb)
    face_sets = set()
    for faces in cb.values():
        face_sets.update(faces)
    cube_links = Counter()
    for key in cb:
        for e in key:
            cube_links[e] += 1
    s_e = Counter()
    s_face = Counter()
    s_nocube = Counter()
    s_wrap = Counter()
    n_face = n_wrap = n_face_wrap = 0
    for c in cyc:
        es = cycle_edges(c)
        is_face = es in face_sets
        is_wrap = wraps(c, xyz, dims) if xyz is not None else False
        n_face += is_face
        n_wrap += is_wrap
        n_face_wrap += is_face and is_wrap
        for e in es:
            s_e[e] += 1
            if is_face:
                s_face[e] += 1
            else:
                s_nocube[e] += 1
            if is_wrap:
                s_wrap[e] += 1
    S = len(cyc)
    curl = {e: max(s_e[e] - 4, 0) for e in links}
    anti = {e: max(4 - s_e[e], 0) for e in links}
    tot_curl, tot_anti = sum(curl.values()), sum(anti.values())
    # a curl link's squares, by class: how many of its squares are not cube faces, how many wrap
    curl_links = [e for e in links if curl[e] > 0]
    anti_links = [e for e in links if anti[e] > 0]
    nocube_on_curl = sum(s_nocube[e] for e in curl_links)
    face_on_curl = sum(s_face[e] for e in curl_links)
    wrap_on_curl = sum(s_wrap[e] for e in curl_links)
    curl_all_faces = all(s_nocube[e] == 0 for e in curl_links)
    curl_only_nocube = all(s_face[e] <= 4 for e in curl_links) and nocube_on_curl > 0
    manifold_ok = sum(1 for e in links if s_e[e] == cube_links[e])
    word = "ALL FACES" if (curl_links and curl_all_faces) else ("WRAP ONLY" if curl_only_nocube else
                                                               ("MIXED" if curl_links else "NO CURL"))
    wrap_note = " (nominal: rod labels)" if nominal else ""
    print(f"\n== {name}: N {n}, links {len(links)}, squares S {S} (3N = {3 * n}), curl {tot_curl}, anticurl {tot_anti}")
    print(f"   4-cycles: {S}; cube faces {n_face}; not a face of any cube {S - n_face}; "
          + (f"wrap{wrap_note} {n_wrap}, of which cube faces {n_face_wrap}" if xyz is not None else "wrap: n/a"))
    print(f"   3-cube subgraphs C = {len(cb)} against N = {n}  ->  C {'=' if len(cb) == n else '!='} N; "
          f"S {'=' if S == 3 * n else '!='} 3N")
    print(f"   links with S_e equal to the cubes round them: {manifold_ok} of {len(links)}")
    print(f"   curl links {len(curl_links)}: their squares that are cube faces {face_on_curl}, not faces "
          f"{nocube_on_curl}, wrapping{wrap_note} {wrap_on_curl}; anticurl links {len(anti_links)}")
    by_class = Counter((s_face[e], s_nocube[e]) for e in curl_links)
    print(f"   curl links by (faces, non-faces) on the link: {dict(sorted(by_class.items()))}")
    by_class_a = Counter((s_face[e], s_nocube[e]) for e in anti_links)
    print(f"   anticurl links by (faces, non-faces): {dict(sorted(by_class_a.items()))}")
    print(f"   check 1 word: {word}")
    charge = np.array([s_e[e] - 4 for e in links], dtype=float)
    if rng is None:
        rng = np.random.default_rng(20261026)
    q = q_local(adj, links, charge, RADII, rng, N_SHUFFLE)
    words = []
    for r in RADII:
        a, sh_std, sh_max = q[r]
        small = a.std() <= sh_std + 1e-9 and np.abs(a).max() <= sh_max + 1e-9
        words.append("NEUTRAL" if small else "LOBED")
        print(f"   Q(r={r}): mean {a.mean():7.2f} std {a.std():6.2f} max|Q| {np.abs(a).max():5.0f} | shuffled std "
              f"{sh_std:6.2f} max|Q| {sh_max:5.1f} -> {words[-1]}")
    print(f"   check 4 words: r=1 {words[0]}, r=2 {words[1]}, r=3 {words[2]}")
    return dict(S=S, N=n, C=len(cb), curl=tot_curl, anti=tot_anti, word=word, q=words,
                nocube_on_curl=nocube_on_curl, face_on_curl=face_on_curl)


def main():
    n_states = int(sys.argv[1]) if len(sys.argv) > 1 else 6
    rng = np.random.default_rng(20261026)
    for dims in ([6, 6, 8], [4, 4, 18]):
        adj, _ = torus(dims)
        survey(f"torus {dims}", adj, coords_of(dims), tuple(dims), rng=rng)
    rod_xyz = coords_of([4, 4, 18])
    paths = sorted(OUT.glob("push_rod_*_adj/*.npz")) if OUT.exists() else []
    if not paths:
        print("\nno saved end states in sandbox/out/pair_tie_push/: tori only")
        return
    # a few: the first replica of each cell, up to n_states, spanning tie/untied, lambda and push
    picks = [p for p in paths if p.name.endswith("rep0.npz")]
    picks = picks[:: max(1, len(picks) // n_states)][:n_states]
    rows = []
    for p in picks:
        z = np.load(p)
        adj = np.asarray(z["adj"], dtype=np.int64)
        r = survey(f"{p.parent.name[9:-4]} {p.name}", adj, rod_xyz, (4, 4, 18), nominal=True, rng=rng)
        rows.append((p.parent.name[9:-4], r))
    print("\nsummary of saved end states (started from the rod, which her hard rule forbids):")
    for name, r in rows:
        print(f"  {name:18s} S {r['S']:5d} (3N {3 * r['N']}) C {r['C']:5d} curl {r['curl']:4d} anticurl {r['anti']:4d} "
              f"curl squares faces/non-faces {r['face_on_curl']}/{r['nocube_on_curl']} {r['word']:10s} "
              f"Q: {' '.join(r['q'])}")


if __name__ == "__main__":
    main()

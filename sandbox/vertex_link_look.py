"""Sandbox look (exploratory; rule 16), 26 October 2026: is every point's vertex link the octahedron?
Usage:

    python sandbox/vertex_link_look.py [all | n_states]

Item 3 (b) of `docs/design/next_experiments_2026-10-26.md`, the part still owed after `sandbox/cube_face_look.py`: the
vertex-link Euler count per point. A look can kill a claim but never crown one.

The question. For each point p of a six-link graph, take its LINK GRAPH: the vertices are the six neighbors of p; two
neighbors a and b are joined if there is a point q != p adjacent to both (then p-a-q-b is a 4-cycle, a square, through
p); the MULTIPLICITY of the link edge (a, b) is the number of such q. So the link edges counted with multiplicity are
exactly the squares through p, and (exact, by that definition) the link-degree of neighbor a counted with multiplicity
is S_{pa}, the number of squares on the link p-a. Under the hard-core rule (no two points with more than two common
neighbors) a and b share at most p and one other point, so every multiplicity is 0 or 1 and the two counts agree; the
look checks that on every state rather than assuming it.

Reported per point: link edges with and without multiplicity; whether the link is the OCTAHEDRON (K_{2,2,2}: 6
vertices, 12 edges, every vertex of degree 4; the triangulated 2-sphere a point of a closed cubical 3-manifold has);
and otherwise what it is: edges, triangles (3-cliques of the link; not checked to be cube corners), connected
components, planarity (networkx), degree sequence. Named kinds, declared before running:
  OCTAHEDRON          12 edges, degrees (4,4,4,4,4,4).
  STACKED SPHERE      the only other triangulation of the 2-sphere on 6 vertices (12 edges, 8 triangular faces but
                      10 triangles as 3-cliques, two of them separating; planar; degrees (5,5,4,4,3,3): a triangular
                      bipyramid with one face subdivided). Identified by isomorphism to a built reference (networkx),
                      as is the octahedron; a first version of this script asked for 8 triangles and mislabelled it
                      OTHER, caught on the first run and corrected before anything was reported. This is item 3 (b)'s
                      "5-square link beside 3-square links at one point": two links of p with 5 squares, two with 4,
                      two with 3, curl and anticurl paired at p.
  OCTAHEDRON+k DIAG   the octahedron plus k of its 3 antipodal pairs (12 + k edges). A rod point should be k = 2: its
                      neighbors x+1 and x-1 along a curled direction of length 4 share the second point x+2 besides p.
  OTHER               anything else, described by its numbers.

Item 3 (b)'s claim (ours, unverified; arithmetic): S = 3N for a closed cubical 3-manifold with six links per point
follows because each vertex link is a triangulated 2-sphere on 6 vertices, hence 12 edges (Euler: E = 3V - 6), hence
12 squares through every point and S = 12N/4 = 3N, whatever the squares per link. The Euler-like number reported per
point is V - E + T with T the triangle count (2 for a triangulated sphere whose triangles are all faces).

Words, declared before running:
  ALL OCTAHEDRA       every point's link is the octahedron;
  NOT ALL             with the count of points that are not and the kinds found.
Also checked on every state: sum over points of link edges with multiplicity = 4 S (each square is counted once at
each of its four points), S from an independent enumeration of 4-cycles (`cube_face_look.four_cycles`).

Expected (ours, before running): the flat 6 x 6 x 8 torus ALL OCTAHEDRA (S = 3N = 864, 12 edges a point, sum 3,456 =
4 S); the rod 4 x 4 x 18 NOT ALL at all 288 points, each OCTAHEDRON+2 DIAG with exactly 14 link edges (with and
without multiplicity: (4 links x 5 squares + 2 links x 4 squares) / 2 = 14; sum 14 N = 4,032 = 4 x 3.5 N); saved
end states NOT ALL at the broken points, and no STACKED SPHERE anywhere (nothing in the push dynamics aims at one).

Rule-obedience: the flat torus obeys the owner's hard rule (S = 3N, every link at four squares); the rod (S = 3.5N)
and every saved end state (all started from the rod) do not, and are read anyway, marked.

Saved end states: `sandbox/out/pair_tie_push/push_rod_*_adj/*.npz` if present (all of them by default; `n` reads the
first replica of the first n cells); else the look says so and reads the tori only.
"""
import sys
from collections import Counter, defaultdict
from itertools import combinations
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "sandbox"))
from graphity.cqg_d import torus  # noqa: E402
from cube_face_look import four_cycles, nbrs, OUT  # noqa: E402

try:
    import networkx as nx
except ImportError:  # planarity then reads "n/a" and the named kinds fall back to degree sequences
    nx = None


def references():
    """The two triangulations of the 2-sphere on 6 vertices, as networkx graphs."""
    if nx is None:
        return None, None
    octa = nx.complete_multipartite_graph(2, 2, 2)
    # triangular bipyramid: apexes 0, 1; equator 2, 3, 4; then stack vertex 5 on the face (0, 2, 3)
    stacked = nx.Graph()
    stacked.add_edges_from([(2, 3), (3, 4), (4, 2)] + [(a, e) for a in (0, 1) for e in (2, 3, 4)]
                           + [(5, 0), (5, 2), (5, 3)])
    assert octa.number_of_edges() == 12 and stacked.number_of_edges() == 12
    assert sorted(d for _, d in stacked.degree()) == [3, 3, 4, 4, 5, 5]
    return octa, stacked


OCTA_REF, STACKED_REF = references()


def link_graph(nb, p):
    """The link of p: {(a, b): multiplicity} over unordered pairs of neighbors a < b of p."""
    ns = sorted(nb[p])
    mult = {}
    for a, b in combinations(ns, 2):
        q = (nb[a] & nb[b]) - {p}
        if q:
            mult[(a, b)] = len(q)
    return ns, mult


def classify(ns, mult):
    """Kind, edges with multiplicity, simple edges, triangles, components, planar, degree sequences (mult, simple)."""
    e_mult = sum(mult.values())
    e_simple = len(mult)
    deg_m = Counter()
    deg_s = Counter()
    for (a, b), m in mult.items():
        deg_m[a] += m
        deg_m[b] += m
        deg_s[a] += 1
        deg_s[b] += 1
    dm = tuple(sorted((deg_m[v] for v in ns), reverse=True))
    ds = tuple(sorted((deg_s[v] for v in ns), reverse=True))
    adjs = {v: set() for v in ns}
    for a, b in mult:
        adjs[a].add(b)
        adjs[b].add(a)
    tri = sum(1 for a, b, c in combinations(ns, 3) if b in adjs[a] and c in adjs[a] and c in adjs[b])
    # components
    seen = set()
    comps = 0
    for v in ns:
        if v in seen:
            continue
        comps += 1
        stack = [v]
        seen.add(v)
        while stack:
            u = stack.pop()
            for w in adjs[u]:
                if w not in seen:
                    seen.add(w)
                    stack.append(w)
    if nx is not None:
        g = nx.Graph()
        g.add_nodes_from(ns)
        g.add_edges_from(mult.keys())
        planar = bool(nx.check_planarity(g)[0])
        is_octa = e_simple == 12 and nx.is_isomorphic(g, OCTA_REF)
        is_stacked = e_simple == 12 and nx.is_isomorphic(g, STACKED_REF)
    else:
        planar = None
        is_octa = e_simple == 12 and ds == (4,) * 6
        is_stacked = e_simple == 12 and ds == (5, 5, 4, 4, 3, 3)
    if is_octa:
        kind = "OCTAHEDRON"
    elif is_stacked:
        kind = "STACKED SPHERE"
    elif e_simple in (13, 14, 15) and is_octahedron_plus_diagonals(ns, adjs):
        kind = f"OCTAHEDRON+{e_simple - 12} DIAG"
    else:
        kind = "OTHER"
    return dict(kind=kind, e_mult=e_mult, e_simple=e_simple, tri=tri, comps=comps, planar=planar, dm=dm, ds=ds,
                euler=6 - e_simple + tri)


def is_octahedron_plus_diagonals(ns, adjs):
    """Is the simple link graph K_{2,2,2} plus some of the 3 antipodal pairs? Then its complement is a matching of
    3 - k disjoint edges and the graph on the 6 vertices contains the octahedron."""
    non = [(a, b) for a, b in combinations(ns, 2) if b not in adjs[a]]
    if len(non) + len({frozenset(e) for e in non}) == 0:
        return True  # K6 = octahedron + 3 diagonals
    touched = Counter()
    for a, b in non:
        touched[a] += 1
        touched[b] += 1
    return all(c == 1 for c in touched.values())


def survey(name, adj, obeys):
    n = adj.shape[0]
    if (adj < 0).any():
        raise RuntimeError(f"{name}: an empty neighbor slot")
    nb = nbrs(adj)
    S = len(four_cycles(nb))
    kinds = Counter()
    e_mult_tot = 0
    max_mult = 0
    mult_vs_simple_differ = 0
    non_oct = []
    per_point = []
    for p in range(n):
        ns, mult = link_graph(nb, p)
        if len(ns) != 6:
            raise RuntimeError(f"{name}: point {p} has {len(ns)} neighbors")
        c = classify(ns, mult)
        per_point.append(c)
        kinds[(c["kind"], c["e_mult"], c["e_simple"], c["tri"], c["comps"], c["planar"], c["ds"])] += 1
        e_mult_tot += c["e_mult"]
        max_mult = max(max_mult, max(mult.values(), default=0))
        mult_vs_simple_differ += c["e_mult"] != c["e_simple"]
        if c["kind"] != "OCTAHEDRON":
            non_oct.append(p)
    word = "ALL OCTAHEDRA" if not non_oct else f"NOT ALL ({len(non_oct)} of {n} points)"
    stacked = sum(1 for c in per_point if c["kind"] == "STACKED SPHERE")
    twelve_not_oct = sum(1 for c in per_point if c["e_simple"] == 12 and c["kind"] != "OCTAHEDRON")
    sphere12 = sum(1 for c in per_point if c["e_simple"] == 12 and c["planar"] and c["kind"] != "OCTAHEDRON")
    print(f"\n== {name}: N {n}, S {S} (3N = {3 * n}; S/N = {S / n:.4f}); "
          f"{'OBEYS' if obeys else 'DOES NOT OBEY'} the hard rule (S = 3N, every link at four squares)")
    print(f"   sum over points of link edges with multiplicity {e_mult_tot} against 4 S = {4 * S}: "
          f"{'EQUAL' if e_mult_tot == 4 * S else 'DIFFER'}; largest multiplicity {max_mult}; "
          f"points where the two edge counts differ {mult_vs_simple_differ}")
    print(f"   word: {word}; STACKED SPHERE points {stacked}; 12-edge links that are not the octahedron "
          f"{twelve_not_oct} (of which planar, hence a triangulated sphere, {sphere12})")
    if stacked:
        pts = [p for p, c in enumerate(per_point) if c["kind"] == "STACKED SPHERE"]
        # exact identity: link-degree of neighbor a (multiplicity 1) is S_{pa}; read the squares per link directly
        sq = []
        for p in pts[:3]:
            ns, mult = link_graph(nb, p)
            dm = Counter()
            for (a, b), m in mult.items():
                dm[a] += m
                dm[b] += m
            sq.append(tuple(sorted(dm[v] for v in ns)))
        print(f"   stacked points: {pts[:12]}{' ...' if len(pts) > 12 else ''}; squares on their six links "
              f"(first three) {sq}")
    print("   kinds (kind, edges w/ mult, simple edges, triangles, components, planar, simple degrees): count")
    for key, cnt in sorted(kinds.items(), key=lambda kv: (-kv[1], kv[0][1])):
        kind, em, es, tri, comps, planar, ds = key
        print(f"     {kind:20s} E_mult {em:2d} E {es:2d} T {tri:2d} comps {comps} planar {planar!s:5s} "
              f"V-E+T {6 - es + tri:3d} deg {ds}: {cnt}")
    return dict(N=n, S=S, word=word, non_oct=len(non_oct), stacked=stacked, twelve_not_oct=twelve_not_oct,
                sum_ok=(e_mult_tot == 4 * S), max_mult=max_mult, kinds=kinds)


def main():
    arg = sys.argv[1] if len(sys.argv) > 1 else "all"
    rows = []
    for dims, obeys in (([6, 6, 8], True), ([4, 4, 18], False)):
        adj, _ = torus(dims)
        rows.append((f"torus {dims}", survey(f"torus {dims}", adj, obeys)))
    paths = sorted(OUT.glob("push_rod_*_adj/*.npz")) if OUT.exists() else []
    if not paths:
        print("\nno saved end states in sandbox/out/pair_tie_push/: tori only")
    else:
        if arg != "all":
            n_states = int(arg)
            paths = [p for p in paths if p.name.endswith("rep0.npz")][:n_states]
        print(f"\nsaved end states read: {len(paths)} (all started from the rod, which her hard rule forbids)")
        for p in paths:
            z = np.load(p)
            adj = np.asarray(z["adj"], dtype=np.int64)
            label = f"{p.parent.name[9:-4]} {p.name}"
            rows.append((label, survey(label, adj, False)))
    print("\nsummary:")
    all_kinds = Counter()
    for name, r in rows:
        print(f"  {name:45s} N {r['N']:4d} S {r['S']:5d} {r['word']:28s} stacked {r['stacked']:2d} "
              f"12-edge-non-oct {r['twelve_not_oct']:3d} sum=4S {r['sum_ok']} max mult {r['max_mult']}")
        if not name.startswith("torus"):
            for key, cnt in r["kinds"].items():
                all_kinds[key] += cnt
    if all_kinds:
        tot = sum(all_kinds.values())
        print(f"\nkinds over all saved end states ({tot} points):")
        for key, cnt in sorted(all_kinds.items(), key=lambda kv: (-kv[1], kv[0][1])):
            kind, em, es, tri, comps, planar, ds = key
            print(f"     {kind:20s} E_mult {em:2d} E {es:2d} T {tri:2d} comps {comps} planar {planar!s:5s} "
                  f"V-E+T {6 - es + tri:3d} deg {ds}: {cnt}")
        stacked_total = sum(c for k, c in all_kinds.items() if k[0] == "STACKED SPHERE")
        print(f"\nSTACKED SPHERE (the non-octahedral 6-vertex triangulated sphere) over all saved states: "
              f"{stacked_total} points")


if __name__ == "__main__":
    main()

"""Read-only checks accompanying the author's feedback; no simulations or data writes.

Run from the repository root with the project's Python dependencies installed.
These are reviewer calculations (Ours, unverified), not new registered results.
"""
import csv
import math
import sys
from collections import Counter, defaultdict
from itertools import combinations
from pathlib import Path

import networkx as nx
import numpy as np

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "scripts"))

from graphity.cqg import NO_CAP, torus
from exact_torus_level import A, B, NEUTRAL, census, cost, rate_per_sweep


def independent_geometry(adj):
    """Count squares and test orientability of the complex with every square filled."""
    neighbours = [set(map(int, row)) for row in adj]
    faces = {}
    for v, nb in enumerate(neighbours):
        for a, b in combinations(sorted(nb), 2):
            for c in (neighbours[a] & neighbours[b]) - {v}:
                faces.setdefault(tuple(sorted((v, a, c, b))), (v, a, c, b))
    edge_faces = defaultdict(list)
    for i, face in enumerate(faces.values()):
        for a, b in zip(face, face[1:] + face[:1]):
            edge_faces[tuple(sorted((a, b)))].append((i, 1 if a < b else -1))
    counts = Counter(len(x) for x in edge_faces.values())
    graph = nx.Graph([(v, w) for v, nb in enumerate(neighbours) for w in nb])
    out = dict(N=len(adj), S=len(faces), X=sum(max(len(x)-2, 0) for x in edge_faces.values()),
               edge_square_counts=dict(counts), components=nx.number_connected_components(graph))
    # A closed surface also requires a cyclic link at every vertex.
    cyclic_links = True
    for v in range(len(adj)):
        link = nx.Graph()
        link.add_nodes_from(neighbours[v])
        for face in faces.values():
            if v in face:
                k = face.index(v)
                link.add_edge(face[k-1], face[(k+1) % 4])
        cyclic_links &= nx.is_connected(link) and all(d == 2 for _, d in link.degree())
    out["closed_surface"] = counts == Counter({2: graph.number_of_edges()}) and cyclic_links
    if out["closed_surface"]:
        dual = defaultdict(list)
        for pair in edge_faces.values():
            (i, si), (j, sj) = pair
            dual[i].append((j, -si*sj))
            dual[j].append((i, -si*sj))
        signs = {}
        orientable = True
        for start in range(len(faces)):
            if start in signs:
                continue
            signs[start] = 1
            stack = [start]
            while stack:
                i = stack.pop()
                for j, ratio in dual[i]:
                    expected = signs[i] * ratio
                    if j in signs:
                        orientable &= signs[j] == expected
                    else:
                        signs[j] = expected
                        stack.append(j)
        out.update(orientable=bool(orientable), chi=len(adj)-graph.number_of_edges()+len(faces))
    return out


def main():
    # Enumerate the known N=18 class space, then solve the affine inequalities
    # for a strict above-ground minimum on lambda >= 1; no lambda scan.
    from graphity.small_graphs import explore, circulant, one_switch_away
    from graphity.cqg import total_squares, surplus
    classes, _ = explore(circulant(9), NO_CAP)
    intervals = []
    for adj, _ in classes.reps:
        s, x = int(total_squares(adj)), int(surplus(adj))
        inequalities = [(16*(18-s), 4*x)]
        inequalities += [(16*(s-int(total_squares(trial))), 4*(int(surplus(trial))-x))
                         for trial in one_switch_away(adj, NO_CAP)]
        lo, hi = 1.0, math.inf
        possible = True
        for a, b in inequalities:
            if b > 0:
                lo = max(lo, -a/b)
            elif b < 0:
                hi = min(hi, -a/b)
            elif a <= 0:
                possible = False
        if possible and hi > lo:
            intervals.append((s, x, lo, hi))
    print("N18 STRICT MINIMUM INTERVALS", "classes", len(classes.reps), intervals, flush=True)
    for n in (64, 96, 192):
        adj, part = torus(4, n//4, NO_CAP)
        counts, _ = census(adj, np.flatnonzero(part == 0))
        print("EXIT CENSUS", n, dict(sorted(counts.items())), flush=True)
        for lam, g in ((1.25, 1.5), (1.25, 2.5)):
            ab = {k: counts[k] for k in (A, B)}
            extra = rate_per_sweep(counts, n, lam, g)/rate_per_sweep(ab, n, lam, g)-1
            print("RATE CORRECTION", n, lam, g, extra, flush=True)
        # A local d=2 value alone need not imply the flat lattice vertex link.
        from graphity.dimension import local_dimension
        from graphity.cqg import squares_on_edge
        if n == 64:
            from graphity.small_graphs import one_switch_away, sides_first
            for trial in one_switch_away(sides_first(adj, part), NO_CAP):
                d = local_dimension(trial)
                bad = [(v, sorted(int(squares_on_edge(trial, v, int(w))) for w in trial[v]))
                       for v in np.flatnonzero(d == 2)
                       if any(squares_on_edge(trial, v, int(w)) != 2 for w in trial[v])]
                if bad:
                    print("D2 NONFLAT WITNESS", bad[:4], "d histogram", Counter(map(int, d)), flush=True)
                    break
    for lam in (1.30, 1.35):
        tau = 1/(3*math.exp(-(32-16*lam)/1.5)+2*math.exp(-(64-40*lam)/1.5))
        print("WATCH", lam, "tau", tau, "max(T,205) mean", 205+tau*math.exp(-205/tau),
              "survivor-only mean", 205+tau, flush=True)
    print("DISCRETE DEMON", [(delta, delta/math.expm1(delta/3.5)) for delta in (1, 2, 4)], flush=True)
    for n in (64, 96, 144, 192):
        rows = list(csv.DictReader(open(ROOT / "results" / "t8_lam105.csv", newline="")))
        tally = Counter()
        witnesses = []
        for row in rows:
            if int(row["N"]) != n:
                continue
            path = ROOT / "results" / "t8_lam105_adj" / f"N{n}_rep{row['replica']}.npz"
            geo = independent_geometry(np.load(path)["adj"])
            key = (geo["components"], geo["closed_surface"], geo.get("orientable"), geo.get("chi"))
            tally[key] += 1
            if geo.get("orientable") is False:
                witnesses.append(path.name)
        print("FINAL GEOMETRY T8 LAM105", n, dict(tally), "nonorientable examples", witnesses[:3], flush=True)
    for filename in sorted((ROOT / "results").glob("t24_lam*_n64.csv")):
        rows = list(csv.DictReader(open(filename, newline="")))
        tau = 1/(3*math.exp(-(32-16*float(rows[0]['lam']))/1.5)+2*math.exp(-(64-40*float(rows[0]['lam']))/1.5))
        largest = max(float(r["waiting"]) for r in rows if r["waiting"])
        if largest/tau > 10:
            print("LONG WAIT", filename.name, largest, "ratio to tau", largest/tau,
                  "nominal union bound", len(rows)*math.exp(-largest/tau), flush=True)
    tex = (Path(__file__).parent / "paper.tex").read_text(encoding="utf-8")
    import re
    citations = {key for group in re.findall(r"\\cite\{([^}]+)\}", tex) for key in group.split(",")}
    bib = set(re.findall(r"\\bibitem\{([^}]+)\}", tex))
    print("UNDEFINED CITATIONS", sorted(citations-bib), flush=True)


if __name__ == "__main__":
    main()

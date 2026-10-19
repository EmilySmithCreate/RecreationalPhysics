"""Read-only programme impact checks; Ours, unverified. Run from the repo root.

Reads existing data and constructs small exact graph examples. No production runs
or modifications to result files.
"""
import csv
import math
import sys
from collections import Counter, defaultdict
from itertools import combinations
from pathlib import Path

import networkx as nx
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'src'))
sys.path.insert(0, str(ROOT / 'scripts'))

from graphity import cqg_d
from graphity.dimension import local_dimension_d
from graphity.interchangeable_d import try_switch
from analyse_t38 import waits_by_cell, tail_count, fit_mixture, cell_reading, verdict


def folded_cube(degree=6):
    """Q_degree modulo antipodal identification; even degree preserves parity."""
    mask = (1 << degree) - 1
    representatives = sorted({min(v, v ^ mask) for v in range(1 << degree)})
    index = {v: i for i, v in enumerate(representatives)}
    adj = np.array([[index[min(v ^ (1 << k), (v ^ (1 << k)) ^ mask)]
                     for k in range(degree)] for v in representatives], dtype=np.int64)
    part = np.array([v.bit_count() % 2 for v in representatives], dtype=np.int64)
    return adj, part


def summary(adj):
    graph = nx.Graph([(v, int(w)) for v, row in enumerate(adj) for w in row])
    return dict(N=len(adj), degree=adj.shape[1], valid=bool(cqg_d.is_valid(adj)),
                bipartite=nx.is_bipartite(graph), components=nx.number_connected_components(graph),
                S=int(cqg_d.total_squares(adj)), X=int(cqg_d.surplus(adj)),
                d_hist=dict(Counter(map(int, local_dimension_d(adj)))),
                H125=float(cqg_d.hamiltonian(adj, 1.25)))


def main():
    print('T38 DETECTED-WAIT CHECK', flush=True)
    all_rows = defaultdict(list)
    import re
    for path in (ROOT / 'results').glob('t38_*.csv'):
        match = re.match(r't38_lam(\d+)_n(\d+)_\d+\.csv$', path.name)
        if match:
            key = (int(match.group(1))/100, int(match.group(2)))
            all_rows[key].extend(csv.DictReader(open(path, newline='', encoding='utf-8')))
    readings = []
    for cell, w in sorted(waits_by_cell(ROOT / 'results').items()):
        scale, k = tail_count(w)
        p, t1, t2, lr = fit_mixture(w)
        readings.append(cell_reading(k))
        print(cell, 'n', len(w), 'scale', scale, 'tail_count', k,
              'short_share', p, 'short_tau', t1, 'long_tau', t2, '2logLR', lr,
              'reading', readings[-1], flush=True)
        rows = all_rows[cell]
        print('observation audit', cell, 'total rows', len(rows),
              'blank waits', sum(not r['waiting'] for r in rows),
              'recorded at 205', sum(bool(r['waiting']) and float(r['waiting']) == 205 for r in rows),
              'residual at most 25', sum(x <= 25 for x in w), flush=True)
    print('T38 registered verdict', verdict(readings), flush=True)
    print('T10 NOMINAL THERMOMETER RECALIBRATION (delta=1; equilibrium assumption)', flush=True)
    for path in sorted((ROOT / 'results').glob('t10_n*.csv')):
        final = [r for r in csv.DictReader(open(path, newline='')) if r['final'] == '1']
        e = np.array([float(r['bath_T']) for r in final])
        temp = np.array([1/math.log1p(1/x) if x > 0 else 0.0 for x in e])
        print(path.name, 'replicas', len(e), 'mean_energy', float(e.mean()),
              'nominal_mean_g', float(temp.mean()), 'energy_range', (float(e.min()), float(e.max())),
              'recorded_below_1', int((e < 1).sum()), 'nominal_g_below_1', int((temp < 1).sum()), flush=True)
    print('EXACT FULLY SATURATED COUNTEREXAMPLE', flush=True)
    folded, part = folded_cube()
    s = summary(folded)
    assert s['valid'] and s['bipartite'] and s['d_hist'] == {0: 32}
    nb = [set(map(int, row)) for row in folded]
    common = Counter(len(nb[a] & nb[b]) for a, b in combinations(range(len(folded)), 2))
    assert set(common) <= {0, 2}
    print('folded Q6', s, 'independent_common_neighbour_counts', dict(common), flush=True)
    # More than one Q6's worth of vertices, saturated everywhere, no Q6 component.
    several = np.concatenate([folded + k*len(folded) for k in range(4)])
    print('four folded Q6 components', summary(several), flush=True)
    cube, cube_part = cqg_d.torus([4, 4, 4])
    two = np.concatenate((cube, cube + len(cube)))
    u1, u2 = int(np.flatnonzero(cube_part == 0)[0]), len(cube) + int(np.flatnonzero(cube_part == 0)[0])
    v1, v2 = int(two[u1, 0]), int(two[u2, 0])
    joined = two.copy()
    cqg_d._switch(joined, u1, v1, u2, v2)
    assert cqg_d.is_valid(joined)
    print('valid switch joining two Q6 components', summary(joined),
          'delta_H110', float(cqg_d.hamiltonian(joined, 1.1)-cqg_d.hamiltonian(two, 1.1)),
          'delta_H125', float(cqg_d.hamiltonian(joined, 1.25)-cqg_d.hamiltonian(two, 1.25)), flush=True)
    print('SIX-LINK FLAT-SIGNATURE COUNTEREXAMPLE', flush=True)
    adj, part = cqg_d.torus([4, 6, 6])
    edges = np.empty((4*(1+3*(adj.shape[1]-1))+8, 2), dtype=np.int64)
    found = False
    for u1, u2 in combinations(np.flatnonzero(part == 0), 2):
        for v1 in adj[u1]:
            for v2 in adj[u2]:
                trial = adj.copy()
                ok, ds, dx, dh = try_switch(trial, int(u1), int(v1), int(u2), int(v2), 1.25, edges)
                if not ok:
                    continue
                d = local_dimension_d(trial)
                bad = []
                for v in np.flatnonzero(d == 3):
                    incident = sorted(int(cqg_d.squares_on_edge(trial, int(v), int(w))) for w in trial[v])
                    if incident != [4]*6:
                        bad.append((int(v), incident))
                if bad:
                    print('move', (int(u1), int(v1), int(u2), int(v2)),
                          'deltaS', ds, 'deltaX', dx, 'deltaH', dh, 'bad_d3_vertices', bad[:4], flush=True)
                    found = True
                    break
            if found:
                break
        if found:
            break
    assert found
    print('ENERGY ON POINTS LABELLED FLAT IN A SAVED RELIC GRAPH', flush=True)
    from graphity.cqg import total_squares, surplus, squares_on_edge
    for folder in sorted((ROOT / 'results').glob('t37_lam125_g125_L1024_*_adj')):
        found_relic = False
        for path in sorted(folder.glob('*.npz')):
            saved = np.load(path)
            adj = saved['adj']
            lam = 1.25
            d = local_dimension_d(adj)
            h = 16*(len(adj)-int(total_squares(adj))) + 4*lam*int(surplus(adj))
            per_point = []
            for v in range(len(adj)):
                sq = [int(squares_on_edge(adj, v, int(w))) for w in adj[v]]
                per_point.append(16-2*sum(sq)+2*lam*sum(max(x-2, 0) for x in sq))
            per_point = np.array(per_point)
            assert abs(per_point.sum()-h) < 1e-9
            print(path.relative_to(ROOT), 'lambda', lam, 'H', h, 'energy_on_d1', float(per_point[d == 1].sum()),
                  'energy_on_d2', float(per_point[d == 2].sum()),
                  'energy_on_other_d', float(per_point[~np.isin(d, (1, 2))].sum()),
                  'positive_energy_d2_vertices', int(((d == 2) & (per_point > 0)).sum()), flush=True)
            found_relic = True
            break
        if found_relic:
            break
    # Static evidence on whether implemented symmetry acceptance contains the
    # clipping error discussed in the earlier manuscript review.
    for name in ('interchangeable.py', 'interchangeable_d.py'):
        print('CORRECT SYMMETRY RULE', name, flush=True)
        for i, line in enumerate((ROOT / 'src' / 'graphity' / name).read_text().splitlines(), 1):
            if ('np.exp(-d_h / g)' in line or 'min(1.0, p)' in line):
                print(i, line.strip(), flush=True)


if __name__ == '__main__':
    main()

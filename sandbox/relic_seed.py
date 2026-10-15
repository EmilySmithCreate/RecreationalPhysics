"""Sandbox: does a relic seed a fold? Usage:

    python sandbox/relic_seed.py [LENGTH] [REPLICAS] [LAMBDA] [PUSH_SWEEPS] [ENERGIES]

The owner's idea of 14 October: random energy does not curl space, but energy delivered at a relic might, the curl
growing out of the relic (the black hole joining open space to a relic). Here: a sealed 4 x LENGTH tube burps (the
wall's spark, a shared bath of one store per point), is cooled by draining the stores, and is kept only if it ends
with exactly one curled column (one piece of four points at d = 1) and no point at d > 2. Then the stores are
emptied and E units are packed into one store, at a side-0 point next to the column ("near") or as far from it as
the graph allows ("far", the control), with one store per point that only moves made from that point can use
(by_vertex, T26's local spark). The chain runs PUSH_SWEEPS sweeps; every 200 the curled points (d <= 1), the largest
curled piece and whether it holds the relic, and the damaged points (d > 2) are read.
"""
import sys
from collections import deque
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from graphity import sealed                                     # noqa: E402
from graphity.cqg import NO_CAP, hamiltonian, torus             # noqa: E402
from graphity.dimension import local_dimension                 # noqa: E402


def pieces(adj, members):
    """Connected pieces of the set `members`, as lists, largest first."""
    inside = set(int(v) for v in members)
    seen, out = set(), []
    for v in inside:
        if v in seen:
            continue
        seen.add(v)
        q, comp = deque([v]), []
        while q:
            a = q.popleft()
            comp.append(a)
            for b in adj[a]:
                b = int(b)
                if b in inside and b not in seen:
                    seen.add(b)
                    q.append(b)
        out.append(comp)
    return sorted(out, key=len, reverse=True)


def distances(adj, start):
    dist = np.full(adj.shape[0], -1)
    dist[start] = 0
    q = deque([start])
    while q:
        a = q.popleft()
        for b in adj[a]:
            if dist[b] < 0:
                dist[b] = dist[a] + 1
                q.append(b)
    return dist


def burp(length, lam, seed):
    """A burped, cooled tube with exactly one column, or None."""
    adj, part = torus(length, 4, NO_CAP)
    side = np.flatnonzero(part == 0).astype(np.int64)
    n = adj.shape[0]
    demons = np.zeros(n)
    demons[0] = min(32.0 - 16.0 * lam, 64.0 - 40.0 * lam)
    sealed.run_sealed_bath(adj, side, demons, 20000, seed, lam, NO_CAP, None, False)
    for _ in range(100):
        demons *= 0.95
        sealed.run_sealed_bath(adj, side, demons, 100, -1, lam, NO_CAP, None, False)
    demons[:] = 0.0
    sealed.run_sealed_bath(adj, side, demons, 500, -1, lam, NO_CAP, None, False)
    d = local_dimension(adj)
    curled = pieces(adj, np.flatnonzero(d <= 1))
    if len(curled) != 1 or len(curled[0]) != 4 or (d > 2).any():
        return None
    return adj, side, curled[0]


def state(adj, relic):
    d = local_dimension(adj)
    curled = pieces(adj, np.flatnonzero(d <= 1))
    big = curled[0] if curled else []
    return dict(curled=int((d <= 1).sum()), largest=len(big), holds_relic=bool(set(relic) & set(big)),
                relic_left=int(sum(d[v] <= 1 for v in relic)), damaged=int((d > 2).sum()))


def push(adj, side, relic, energy, where, lam, seed, sweeps):
    adj = adj.copy()
    n = adj.shape[0]
    side_set = set(int(v) for v in side)
    near = [int(b) for v in relic for b in adj[v] if int(b) not in relic and int(b) in side_set]
    if where == "near":
        at = near[0]
    else:
        dist = np.min([distances(adj, v) for v in relic], axis=0)
        cand = [v for v in side_set]
        at = max(cand, key=lambda v: dist[v])
    demons = np.zeros(n)
    demons[at] = energy
    e0 = hamiltonian(adj, lam) + demons.sum()
    peak = dict(curled=0, largest=0, damaged=0)
    first = True
    for _ in range(sweeps // 200):
        sealed.run_sealed_bath(adj, side, demons, 200, seed if first else -1, lam, NO_CAP, None, True)
        first = False
        s = state(adj, relic)
        for k in peak:
            peak[k] = max(peak[k], s[k])
    end = state(adj, relic)
    assert abs(hamiltonian(adj, lam) + demons.sum() - e0) < 1e-6
    return end, peak, float(demons.max())


def main():
    length = int(sys.argv[1]) if len(sys.argv) > 1 else 48
    reps = int(sys.argv[2]) if len(sys.argv) > 2 else 6
    lam = float(sys.argv[3]) if len(sys.argv) > 3 else 1.25
    sweeps = int(sys.argv[4]) if len(sys.argv) > 4 else 20000
    energies = [float(x) for x in sys.argv[5].split(",")] if len(sys.argv) > 5 else [16, 32, 64, 128, 256]
    starts, seed = [], 1000
    while len(starts) < reps and seed < 1000 + 40 * reps:
        got = burp(length, lam, seed)
        if got is not None:
            starts.append(got)
        seed += 1
    print("N = %d, lambda = %.2f: %d starts with one column from %d burps" % (4 * length, lam, len(starts), seed - 1000))
    for energy in energies:
        for where in ("near", "far"):
            rows = [push(a, s, r, energy, where, lam, 7000 + i, sweeps) for i, (a, s, r) in enumerate(starts)]
            print("E = %5.0f %-4s | end: curled %s, largest %s, relic kept %s, damaged %s | peak curled %s, largest %s,"
                  " damaged %s" % (
                      energy, where,
                      [e["curled"] for e, _, _ in rows], [e["largest"] for e, _, _ in rows],
                      [e["relic_left"] for e, _, _ in rows], [e["damaged"] for e, _, _ in rows],
                      [p["curled"] for _, p, _ in rows], [p["largest"] for _, p, _ in rows],
                      [p["damaged"] for _, p, _ in rows]), flush=True)


if __name__ == "__main__":
    main()

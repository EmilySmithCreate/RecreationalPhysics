"""Sandbox: does a relic seed a fold when the energy beside it may only curl? Usage:

    python sandbox/relic_curl_seed.py [LENGTH] [REPLICAS] [LAMBDA] [PUSH_SWEEPS] [ENERGIES] [MODES]

The owner's readings (a) and (b) of 14 and 15 October together: the relic is the seed and the energy is curling
energy, a kind that can pay only for curling. Same protocol as `relic_seed.py` (a burped, cooled 4 x LENGTH tube with
exactly one curled column; E units packed into one store next to the column, or as far from it as possible, one store
per point, sealed), with the chain's acceptance changed as `feed_energy.py` does:

MODE "curl": a store may not pay for a move that only breaks squares (lowers the square count without lowering the
surplus); it may pay for any move that changes the curl, even one that breaks squares too (the rule of 11 October).
MODE "strict": a store may pay only for a move that adds surplus squares and breaks none (d_x > 0 and d_s >= 0).
Moves that cost nothing are accepted as always; the rule bites only where energy has to be paid.
"""
import inspect
import sys
from pathlib import Path

import numpy as np
from numba import njit

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "sandbox"))
from graphity import sealed                                     # noqa: E402
from graphity.cqg import NO_CAP, hamiltonian                    # noqa: E402
import relic_seed                                               # noqa: E402

_src = inspect.getsource(sealed.run_sealed_bath.py_func).replace("@njit(cache=True)\n", "")
_old = "if d_h > demons[k]:"
assert _src.count(_old) == 1


def _variant(name, cond):
    src = _src.replace(_old, "if d_h > demons[k] or (d_h > 0 and (%s)):" % cond).replace(
        "def run_sealed_bath(", "def %s(" % name)
    ns = dict(vars(sealed))
    exec(src, ns)
    return njit(ns[name])


CHAINS = {
    "curl": _variant("run_curl_only", "d_s < 0 and d_x >= 0"),
    "strict": _variant("run_curl_strict", "not (d_x > 0 and d_s >= 0)"),
}


def push(chain, adj, side, relic, energy, where, lam, seed, sweeps):
    adj = adj.copy()
    n = adj.shape[0]
    side_set = set(int(v) for v in side)
    near = [int(b) for v in relic for b in adj[v] if int(b) not in relic and int(b) in side_set]
    if where == "near":
        at = near[0]
    else:
        dist = np.min([relic_seed.distances(adj, v) for v in relic], axis=0)
        at = max(side_set, key=lambda v: dist[v])
    demons = np.zeros(n)
    demons[at] = energy
    e0 = hamiltonian(adj, lam) + demons.sum()
    peak = dict(curled=0, largest=0, damaged=0)
    first = True
    for _ in range(sweeps // 200):
        chain(adj, side, demons, 200, seed if first else -1, lam, NO_CAP, None, True)
        first = False
        s = relic_seed.state(adj, relic)
        for k in peak:
            peak[k] = max(peak[k], s[k])
    end = relic_seed.state(adj, relic)
    assert abs(hamiltonian(adj, lam) + demons.sum() - e0) < 1e-6
    return end, peak, float(demons.sum())


def main():
    length = int(sys.argv[1]) if len(sys.argv) > 1 else 48
    reps = int(sys.argv[2]) if len(sys.argv) > 2 else 6
    lam = float(sys.argv[3]) if len(sys.argv) > 3 else 1.25
    sweeps = int(sys.argv[4]) if len(sys.argv) > 4 else 20000
    energies = [float(x) for x in sys.argv[5].split(",")] if len(sys.argv) > 5 else [16, 64, 256]
    modes = sys.argv[6].split(",") if len(sys.argv) > 6 else ["curl", "strict"]
    starts, seed = [], 1000
    while len(starts) < reps and seed < 1000 + 40 * reps:
        got = relic_seed.burp(length, lam, seed)
        if got is not None:
            starts.append(got)
        seed += 1
    print("N = %d, lambda = %.2f: %d starts with one column from %d burps" % (4 * length, lam, len(starts), seed - 1000),
          flush=True)
    for mode in modes:
        chain = CHAINS[mode]
        for energy in energies:
            for where in ("near", "far"):
                rows = [push(chain, a, s, r, energy, where, lam, 7000 + i, sweeps) for i, (a, s, r) in enumerate(starts)]
                print("%-6s E = %5.0f %-4s | end: curled %s, largest %s, relic kept %s, damaged %s | peak curled %s,"
                      " largest %s, damaged %s | energy still in stores %s" % (
                          mode, energy, where,
                          [e["curled"] for e, _, _ in rows], [e["largest"] for e, _, _ in rows],
                          [e["relic_left"] for e, _, _ in rows], [e["damaged"] for e, _, _ in rows],
                          [p["curled"] for _, p, _ in rows], [p["largest"] for _, p, _ in rows],
                          [p["damaged"] for _, p, _ in rows], [round(x) for _, _, x in rows]), flush=True)


if __name__ == "__main__":
    main()

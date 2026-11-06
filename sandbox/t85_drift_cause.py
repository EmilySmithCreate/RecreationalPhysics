"""A look (sandbox lane; rule 11's cheapest discriminating calculation for T85's drift). T85 found alpha* drifting with the
impact parameter b. Written before the run of T85's held-out size as the suspected cause: D is the delay of the fastest
path (free to zigzag round the lumpy halo) while P is taken along the straight line. This recomputes D along a FIXED
zigzag path (the straight-line analogue on body diagonals: alternating (1,1,1) and (1,-1,-1)) for the same knot and halo,
and reports alpha*_straight(b) = alpha_used * D_straight / (2 P) beside T85's alpha*(b).

WRITTEN BEFORE COMPUTING (ours): with both quantities on one path, alpha*_straight is flat in b to within +-10 % up to
the torus's reach; if it still drifts the cause is in the halo's shape and not in the paths.
"""
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from graphity import diagonals, lengths  # noqa: E402
from graphity.cqg_d import _switch, hamiltonian, is_valid, torus  # noqa: E402
from t85_gamma import LAM, make_knot  # noqa: E402

L = int(sys.argv[1]) if len(sys.argv) > 1 else 24
seed = int(sys.argv[2]) if len(sys.argv) > 2 else 20268501
alpha = -0.5
dims = (L, L, L)
adj0, part = torus(dims)
n = adj0.shape[0]
coords = np.array(np.unravel_index(np.arange(n), dims)).T
idx = {tuple(c): i for i, c in enumerate(coords)}
rng = np.random.default_rng(seed)
adjA = adj0.copy()
quad = make_knot(adjA, coords, idx, L, rng)
e_knot = float(hamiltonian(adjA, LAM) - hamiltonian(adj0, LAM))
fA = lengths.curl_fields(adjA, dims)
deltaA, EA = lengths.relax(fA, alpha)
diag = diagonals.diagonal_lengths(deltaA)
R = L // 4


def straight_ticks(start):
    p = np.array(start); total = 0.0
    for k in range(2 * R):
        s = np.array([1, 1, 1]) if k % 2 == 0 else np.array([1, -1, -1])
        cube = tuple(np.mod(p + np.minimum(s, 0), L))
        total += diag[cube]; p = p + s
    return total


def pair_energy_at(x):
    adjB = adjA.copy()
    _switch(adjB, *[idx[tuple((coords[p] + np.array(x)) % L)] for p in quad])
    assert is_valid(adjB)
    return lengths.relax(lengths.curl_fields(adjB, dims), alpha)[1] - 2 * EA


print("L = %d, knot charges %s, E_knot %.0f" % (L, fA.sum(axis=(1, 2, 3)), e_knot))
print("   b   D_fastest  D_straight   P       alpha*_fastest  alpha*_straight")
for b in range(2, L // 2 - 1, 2):
    near_f = diagonals.light_ticks(diag, (-R, b, 0), (R, b, 0))
    far_f = diagonals.light_ticks(diag, (-R, b + L // 2, L // 2), (R, b + L // 2, L // 2))
    D_f = near_f - far_f
    D_s = straight_ticks((-R, b, 0)) - straight_ticks((-R, b + L // 2, L // 2))
    P = 0.0
    for x in range(-R, R + 1):
        P += abs(pair_energy_at((x, b, 0))) / e_knot * np.sqrt(3)
    print("  %2d   %.5f    %.5f    %.5f   %+.4f         %+.4f" % (b, D_f, D_s, P, alpha * D_f / (2 * P), alpha * D_s / (2 * P)), flush=True)

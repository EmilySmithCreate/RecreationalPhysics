"""Exact look before registering the owner's prediction for light in curled space (24 October 2026):
"Light moves same speed through curved space but bounces or slows through matter ie curled space with charge or spin".

On a torus with one side of 4 (a curled direction), the ring round the curl is a 4-cycle, so graphity.u1 counts it as
a square and the field pays for its holonomy. Compare the linear waves (eigenvalues of B^T B, kappa = 1, unit inertia)
on a curled torus 4 x L x L with a flat torus 6 x L x L and 8 x L x L. Plane waves along the open direction y with
momentum k (x and z momentum zero): project the eigenvectors onto the translation eigenspaces by building the Bloch
problem numerically with a translation operator, and report omega(k) for each branch.
"""
import os
import sys

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from graphity.cqg_d import torus  # noqa: E402
from graphity.u1 import Field  # noqa: E402

OUT = os.path.join(os.path.dirname(__file__), "out")
os.makedirs(OUT, exist_ok=True)
lines = []


def say(s=""):
    print(s, flush=True)
    lines.append(s)


def translation(dims, axis):
    """link permutation for a shift by 2 along `axis` (2 keeps the kinds, so link orientation is kept)"""
    adj, part = torus(dims)
    f = Field(adj, part)
    coords = np.array(np.unravel_index(np.arange(len(adj)), dims)).T
    strides = np.array([int(np.prod(dims[a + 1:])) for a in range(len(dims))])

    def shift(i):
        c = coords[i].copy()
        c[axis] = (c[axis] + 2) % dims[axis]
        return int(c @ strides)

    perm = np.empty(f.n_links, dtype=int)
    for l in range(f.n_links):
        perm[l] = f.index[(shift(f.tail[l]), shift(f.head[l]))]
    return f, perm


def dispersion(dims, label):
    f, Ty = translation(dims, 1)
    _, Tx = translation(dims, 0)
    _, Tz = translation(dims, 2)
    M = f.mode_matrix()
    n = f.n_links

    def Pmat(perm):
        P = np.zeros((n, n))
        P[perm, np.arange(n)] = 1.0
        return P

    Py, Px, Pz = Pmat(Ty), Pmat(Tx), Pmat(Tz)
    L = dims[1]
    say(f"\n{label} {dims[0]} x {dims[1]} x {dims[2]}: {f.n_squares} squares; zero modes "
        f"{int(np.sum(np.linalg.eigvalsh(M) < 1e-9))} (gauge {f.n - 1})")
    # restrict to x- and z-translation invariant subspace (sum over the orbit), then Bloch in y
    for m in range(0, L // 2 + 1):
        k = 2 * np.pi * m / (L / 2)            # momentum per shift of 2 sites -> per-site k = pi m / (L/2)/... see below
        phase = np.exp(1j * 2 * np.pi * m / (L // 2))
        # projector onto Ty eigenvalue `phase`, Tx = 1, Tz = 1
        def proj(P, ph, order):
            Q = np.zeros((n, n), complex)
            Pk = np.eye(n)
            for j in range(order):
                Q += (np.conj(ph) ** j) * Pk
                Pk = P @ Pk
            return Q / order
        Q = proj(Py, phase, L // 2) @ proj(Px, 1.0, dims[0] // 2) @ proj(Pz, 1.0, dims[2] // 2)
        # orthonormal basis of the projected space
        u, s, _ = np.linalg.svd(Q)
        B = u[:, s > 1e-8]
        ev = np.sort(np.linalg.eigvalsh(B.conj().T @ M @ B).real)
        kk = np.pi * m / (L // 2) * 1.0        # momentum per site along y (shift of 2 sites has phase 2 kk)
        nz = ev[ev > 1e-9]
        say(f"   k = {kk:5.3f}: omega = " + ", ".join(f"{np.sqrt(x):.4f}" for x in nz[:6])
            + f"   (flat-lattice photon 2 sin(k/2) = {2 * np.sin(kk / 2):.4f}; zero modes here {int(np.sum(ev < 1e-9))})")


for dims, label in (((8, 8, 8), "flat"), ((6, 8, 8), "flat, narrow"), ((4, 8, 8), "curled (side 4)")):
    dispersion(dims, label)

path = os.path.join(OUT, "light_in_curled_space_2026-10-24.txt")
open(path, "w", encoding="utf-8").write("\n".join(lines) + "\n")
print("written", path)

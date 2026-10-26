"""Sandbox look (CLAUDE.md rule 16: not cited, not scored): O151 generalised to every arrangement of side-4 curls.

Question. O151 found that on a 4 x 8 x 8 torus the light polarised along the side-4 curl has
omega^2 = 4 + 4 sin^2(k/2). Which polarisations are massive in D = 2, 3, 4 with one, two or all directions of side 4,
and is the whole spectrum of B^T B what one closed formula says?

Method (exact, linear waves, kappa = 1, unit inertia per link, as in `graphity.u1.Field.mode_matrix`):
  1. the full spectrum of B^T B by dense diagonalisation;
  2. the Bloch prediction: with the link phases converted to the lattice orientation (a +-1 change of sign per link,
     which is orthogonal and keeps the spectrum), the field is a lattice vector potential A_mu(x), every plaquette
     is a square, and on a side-4 direction a the ring round it is a square too. In Fourier space, with
     K_mu = 2 sin(k_mu / 2),
         M(k) = |K|^2 I - K K^T + 4 sum_{a of side 4} delta(k_a, 0) e_a e_a^T,
     a D x D matrix for each of the prod(dims) momenta; the union of their eigenvalues must equal step 1's spectrum;
  3. explicit plane waves along an open direction, each polarisation, checked as eigenvectors of B^T B;
  4. zero modes counted against gauge (N - 1) plus surviving holonomies (D minus the number of side-4 directions).

Run: python sandbox/u1_curl_mass_general.py   (about a minute)
"""
from __future__ import annotations

import itertools
import os
import sys
import time

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "src"))
from graphity import cqg_d, u1  # noqa: E402


def bloch_spectrum(dims):
    curled = [a for a, s in enumerate(dims) if s == 4]
    D = len(dims)
    out = []
    for m in itertools.product(*[range(s) for s in dims]):
        k = np.array([2 * np.pi * mi / s for mi, s in zip(m, dims)])
        K = 2 * np.sin(k / 2)
        M = np.dot(K, K) * np.eye(D) - np.outer(K, K)
        for a in curled:
            if m[a] == 0:
                M[a, a] += 4.0
        out.extend(np.linalg.eigvalsh(M))
    return np.sort(np.array(out))


def lattice_signs_and_axes(f, dims):
    """For each link: its axis, its lower end along that axis, and the sign turning theta into A along +axis."""
    dims = np.array(dims)
    coords = np.array(np.unravel_index(np.arange(f.n), tuple(dims))).T
    axis = np.empty(f.n_links, dtype=int)
    sign = np.empty(f.n_links)
    lo = np.empty((f.n_links, len(dims)))
    for l in range(f.n_links):
        a, b = coords[f.tail[l]], coords[f.head[l]]
        step = (b - a + dims // 2) % dims - dims // 2
        ax = int(np.flatnonzero(step)[0])
        axis[l] = ax
        sign[l] = np.sign(step[ax])
        lo[l] = a if step[ax] > 0 else b
    return axis, sign, lo


def plane_wave(f, dims, geo, pol, kvec, phase):
    """theta for A = e_pol cos(k . x_mid + phase), x_mid the link's midpoint."""
    axis, sign, lo = geo
    th = np.zeros(f.n_links)
    for l in range(f.n_links):
        if axis[l] != pol:
            continue
        mid = lo[l].copy()
        mid[pol] += 0.5
        th[l] = sign[l] * np.cos(np.dot(kvec, mid) + phase)
    return th


def look(dims):
    t0 = time.time()
    f = u1.Field(*cqg_d.torus(dims))
    M = f.mode_matrix()
    ev = np.linalg.eigvalsh(M)
    pred = bloch_spectrum(dims)
    D = len(dims)
    curled = [a for a, s in enumerate(dims) if s == 4]
    open_ = [a for a in range(D) if dims[a] != 4]
    n_zero = int(np.sum(np.abs(ev) < 1e-9))
    want_zero = (f.n - 1) + (D - len(curled))
    print(f"\n=== torus {' x '.join(map(str, dims))}: N = {f.n}, links = {f.n_links}, squares = {f.n_squares}"
          f" (plaquettes {f.n * D * (D - 1) // 2}, rings {sum(f.n // 4 for _ in curled)})")
    print(f"  full spectrum vs Bloch formula: {len(ev)} vs {len(pred)} eigenvalues, max |diff| = "
          f"{np.max(np.abs(ev - pred)):.2e}")
    print(f"  zero modes {n_zero}; gauge N-1 = {f.n - 1} + holonomies D - #curled = {D - len(curled)}"
          f" -> {want_zero}  {'OK' if n_zero == want_zero else 'MISMATCH'}")
    geo = lattice_signs_and_axes(f, dims)
    if open_:
        prop = open_[-1]
        L = dims[prop]
        for m in range(0, L // 2 + 1):
            k = 2 * np.pi * m / L
            kvec = np.zeros(D)
            kvec[prop] = k
            row = []
            for pol in range(D):
                if pol == prop and m != 0:
                    continue  # longitudinal: pure gauge, eigenvalue 0
                want = 4 * np.sin(k / 2) ** 2 + (4.0 if pol in curled else 0.0)
                ok = True
                for phase in (0.0, np.pi / 2):
                    v = plane_wave(f, dims, geo, pol, kvec, phase)
                    if np.linalg.norm(v) < 1e-12:
                        continue
                    ok &= np.allclose(M @ v, want * v, atol=1e-9)
                tag = "curl" if pol in curled else "open"
                row.append(f"pol {pol} ({tag}): w^2 = {want:.4f} {'ok' if ok else 'FAIL'}")
            print(f"  k = 2pi*{m}/{L} along axis {prop}: " + "; ".join(row))
    else:
        # fully curled: the lowest non-zero modes
        nz = ev[np.abs(ev) > 1e-9]
        vals, counts = np.unique(np.round(nz, 9), return_counts=True)
        print("  no open direction; non-zero eigenvalues (value: multiplicity): "
              + ", ".join(f"{v:g}: {c}" for v, c in zip(vals, counts)))
        k0 = [np.linalg.eigvalsh(4.0 * np.eye(D))]
        print(f"  uniform field (k = 0) along each axis: w^2 = {k0[0]}")
    print(f"  ({time.time() - t0:.1f} s)")
    return np.max(np.abs(ev - pred)), n_zero == want_zero


def main():
    cases = [
        (4, 8),            # D = 2, one curled
        (4, 4),            # D = 2, both curled (the 4-cube)
        (8, 8),            # control
        (6, 8, 8),         # control: side 6 gives nothing
        (4, 8, 8),         # D = 3, one curled (O151)
        (4, 4, 8),         # D = 3, two curled
        (4, 4, 4),         # D = 3, all curled (the 6-cube)
        (4, 6, 6, 6),      # D = 4, one curled
        (4, 4, 6, 6),      # D = 4, two curled
        (4, 4, 4, 6),      # D = 4, three curled
    ]
    worst, allok = 0.0, True
    for dims in cases:
        d, ok = look(dims)
        worst = max(worst, d)
        allok &= ok
    print(f"\nworst spectrum difference over all cases {worst:.2e}; zero-mode counts all match: {allok}")


if __name__ == "__main__":
    main()

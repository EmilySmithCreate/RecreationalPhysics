"""Sandbox look (exploratory; rule 16), 25 October 2026: can soft space's number change sharply, making a front?

The owner (VISION Update 120): "In the toy, a sharp change in soft space's number would make a front. - let's keep
investigating this then."

Part 1, exact for the field as built (graphity.soft_field, term 7). Its resting profile at fixed wiring solves
kappa L phi = -q (e - mean e), so phi = -(q/kappa) L^+ (e - mean e): kappa and q scale the depth only, and the shape is
fixed by where the sources sit. On a flat L x L torus with a band of sources (e = 1 on w columns), we read the width over
which phi goes from 10 % to 90 % of its range, for several w and L.

Part 2, a field with two preferred values (an added double well, a (phi^2 - 1)^2 per point, NOT in the toy): the resting
profile between a region at -1 and one at +1, found by relaxing from a sharp step on a chain; read its width and its
energy per unit length of wall (the tension) against kappa / a and against the chain length.
"""
import numpy as np

from graphity.cqg import torus, NO_CAP


def width_10_90(profile):
    lo, hi = profile.min(), profile.max()
    x = (profile - lo) / (hi - lo)
    i_min = int(np.argmin(profile))
    i_max = int(np.argmax(profile))
    a, b = sorted((i_min, i_max))
    seg = x[a:b + 1] if i_min < i_max else x[a:b + 1][::-1]
    return int(np.sum((seg > 0.1) & (seg < 0.9)))


def part1():
    print("Part 1: the field as built (term 7), resting profile across a band of sources")
    for L in (24, 48):
        adj, _ = torus(L, L, cap=NO_CAP)
        n = L * L
        lap = np.zeros((n, n))
        for p in range(n):
            lap[p, p] = 4.0
            for q in adj[p]:
                lap[p, int(q)] -= 1.0
        lp = np.linalg.pinv(lap)
        for w in (2, 6, L // 4):
            e = np.array([1.0 if (p % L) < w else 0.0 for p in range(n)])
            phi = -lp @ (e - e.mean())          # kappa = q = 1; other values only rescale
            row = phi[:L]                        # phi along x (it does not depend on y)
            print(f"  L = {L:2d}, band {w:2d} columns: phi rises from its lowest to its highest over the whole gap; "
                  f"10-90 % width = {width_10_90(row)} links (gap between bands {L - w})")


def part2():
    print("Part 2: an added double well, a (phi^2 - 1)^2 per point (not in the toy)")
    for n in (200, 400):
        for ratio in (1.0, 4.0, 16.0):           # kappa / a
            kappa, a = ratio, 1.0
            phi = np.where(np.arange(n) < n // 2, -1.0, 1.0)
            dt = 0.2 / (kappa + a)
            for _ in range(40000):
                lap = np.zeros(n)
                lap[1:-1] = 2 * phi[1:-1] - phi[:-2] - phi[2:]
                force = -kappa * lap - 4 * a * phi * (phi ** 2 - 1)
                force[0] = force[-1] = 0.0           # ends pinned at -1 and +1
                phi += dt * force
            tension = 0.5 * kappa * np.sum(np.diff(phi) ** 2) + a * np.sum((phi ** 2 - 1) ** 2)
            print(f"  chain {n}, kappa/a = {ratio:4.0f}: wall width (10-90 %) = {width_10_90(phi):2d} links, "
                  f"tension = {tension:.3f} (continuum (4/3) sqrt(2 kappa a) = {4 / 3 * np.sqrt(2 * kappa * a):.3f})")


if __name__ == "__main__":
    part1()
    part2()

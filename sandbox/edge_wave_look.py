"""A look (sandbox lane; the owner's question of 31 October: do gravity waves work like the photon ladder, keeping her
decision that gravity moves on the cube edges and light on the body diagonals?). Exact arithmetic on what is already
built: the edges' stiffness K = 4(6I - A) per axis family (gravity_link_brief, step 1, held out and confirmed at L = 10).
The toy has no time, so a WAVE needs an inertia the toy does not have; this look gives each edge length a unit inertia
(ours, an assumption for the look only) and reads the normal modes of K, which is what the wave spectrum would be.

Predictions (ours, written before running):
  1. The modes are plane waves on the cubic lattice with omega^2 = 4 * sum_i 2 (1 - cos k_i) over the three directions,
     k_i = 2 pi j_i / L. At long wavelength omega = sqrt(4) |k| = 2 |k|: ONE speed for every long wave (as light has in
     the world; gravitational waves and light share c to 1e-15, published, general knowledge). Near the shortest
     wavelengths the speed falls (lattice dispersion), as every lattice does.
  2. The shortest standing wave on the edges is 2 links (k = pi, lengthen-shorten-lengthen), not 4: the photon's 4 comes
     from its quarter turn per link, which the edge lengths do not have. The top of the band is omega^2 = 48.
  3. The three families do not talk (exact, step 1), so a wave running along z can lengthen the x-links where it shortens
     the y-links: that is the "+" polarization of a gravitational wave (squeeze one way, stretch the other; her note of
     20 October), carried by the axis edges alone. The "x" polarization (stretch along (1, 1, 0), squeeze along (1, -1, 0))
     changes the cubes' angles, which the axis-edge lengths cannot express; it would live on the face diagonals. Ours,
     a geometric argument, not computed here.
  4. Spin: a gravitational wave's pattern repeats after a half turn (spin 2), light's after a full turn (spin 1); the
     toy's edge lengths carry no turning angle at all, so "spin 2" is not in the toy; only the squeeze-stretch pattern is.
Crowns nothing.
"""
import numpy as np

L = 8
# K = 4 (6 I - A) on one axis family: the cubic lattice Laplacian times 4
idx = {(x, y, z): i for i, (x, y, z) in enumerate((x, y, z) for x in range(L) for y in range(L) for z in range(L))}
n = L ** 3
A = np.zeros((n, n))
for (x, y, z), i in idx.items():
    for d in ((1, 0, 0), (0, 1, 0), (0, 0, 1)):
        j = idx[((x + d[0]) % L, (y + d[1]) % L, (z + d[2]) % L)]
        A[i, j] = A[j, i] = 1
K = 4 * (6 * np.eye(n) - A)
w2 = np.sort(np.linalg.eigvalsh(K))
print("L = %d: lowest omega^2 (the uniform scaling, free) = %.2e; next = %.6f (predicted 8(1 - cos 2pi/L) = %.6f); top = %.3f (predicted 48)"
      % (L, w2[0], w2[1], 8 * (1 - np.cos(2 * np.pi / L)), w2[-1]))
print("long-wave speed omega/|k| for the longest wave: %.4f (predicted 2 as k -> 0; at k = 2pi/%d: %.4f)"
      % (np.sqrt(w2[1]) / (2 * np.pi / L), L, np.sqrt(8 * (1 - np.cos(2 * np.pi / L))) / (2 * np.pi / L)))
print("wavelength (links) : omega : speed omega/k, for waves along one axis")
for lam in (L, L // 2, 4, 2):
    k = 2 * np.pi / lam
    om = np.sqrt(8 * (1 - np.cos(k)))
    print("  %2d : %.4f : %.4f" % (lam, om, om / k))
# the "+" pattern: a wave along z lengthening x-links, shortening y-links, is two independent family modes with opposite sign
print("'+' polarization: x-family mode phi(z) and y-family mode -phi(z) are both eigenvectors of their own K with the same omega; "
      "the families never couple (K is block diagonal by family), so the pattern propagates as one wave: exact.")

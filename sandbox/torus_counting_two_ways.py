"""Sandbox look, 23 October 2026 (rule 16: a look; it can kill, not crown). At one N every lattice torus ties in
energy at lambda = 1 (the published model), so which torus the network sits in is decided by counting alone. The
owner's picture of the same day: the strange loop is "his many-handled torus with probabilistic version counts".
Two countings, exact on each built torus:

  * named points (his ensemble, as far as we know; every published run): a shape is weighted by its number of
    labelled copies, (n!)^2 / A, with n = N/2 points per side and A the number of side-preserving renamings (Q9);
  * interchangeable points (her knob, Update 12): each shape counts once (Q15).

For each N the rectangular lattice tori a x b with a, b even, a, b >= 4 and a b = N are built (a side of 4 wraps its
links into three squares: the 4 x L torus is the tube, the 4 x 4 torus the 4-cube). Reported per torus: H at
lambda = 1, squares per point, A, log10 of the labelled copies, and the weight of each torus relative to the square
(or squarest) torus under each counting. Twisted tori (a lattice closed with a shift) are valid tori too and are not
built here. Sizes: 144 and 192 (several tori), 160 (the published size), 196 (his N = 4p^2, p = 7).

Usage: python3 sandbox/torus_counting_two_ways.py > sandbox/out/torus_counting_two_ways_2026-10-23.txt
"""
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(HERE), "src"))
from graphity import cqg, symmetry  # noqa: E402

SIZES = (144, 160, 192, 196)
LAM = 1.0


def tori_of(n):
    out = []
    for a in range(4, int(math.isqrt(n)) + 1, 2):
        if n % a == 0 and (n // a) % 2 == 0 and n // a >= 4:
            out.append((a, n // a))
    return out


def main():
    print("Two countings of the lattice tori at one N, lambda = %.1f (exact; sandbox)" % LAM)
    for n in SIZES:
        shapes = tori_of(n)
        half = n // 2
        log_fact2 = 2 * math.lgamma(half + 1) / math.log(10)      # log10 (n!)^2
        rows = []
        for a, b in shapes:
            adj, part = cqg.torus(a, b, cap=cqg.NO_CAP)
            h = cqg.hamiltonian(adj, LAM)
            s_per_point = cqg.total_squares(adj) / n
            aut = symmetry.count(adj, part)
            rows.append((a, b, h, s_per_point, aut, log_fact2 - math.log10(aut)))
        ref = max(rows, key=lambda r: r[4])                        # the most symmetric torus
        print("\nN = %d: %d lattice tori; n = %d per side; log10 (n!)^2 = %.1f" % (n, len(rows), half, log_fact2))
        print("  %-9s %6s %7s %10s %12s | %-22s %-22s" % ("torus", "H", "S/N", "A", "log10 copies",
                                                          "named: weight vs ref", "interchangeable: weight"))
        for a, b, h, sp, aut, lc in rows:
            named = ref[4] / aut                                   # (n!)^2/A over (n!)^2/A_ref
            print("  %-9s %6.0f %7.3f %10d %12.1f | %-22s %-22s" % (
                "%d x %d" % (a, b), h, sp, aut, lc, "%.3g" % named, "1 (all tie)"))
        print("  ref = %d x %d (largest A). Under named points the weight of the loosest torus over the squarest is %.3g;"
              " under interchangeable points every torus has the same weight." % (ref[0], ref[1], max(ref[4] / r[4] for r in rows)))


if __name__ == "__main__":
    main()

"""A look (sandbox lane; the owner's question of 30 October: "a twist term goes into the energy, I am not sure the form. what
are a few reasonable options?"). Four candidate forms for the energy of twist on a loop of n box diagonals with twists
tau_i in thirds, each with one constant set to 1 (the constant's size changes nothing in the rankings below, only the
competition with the curl's cost, which is not in this look):

  E1 periodic:   sum_i (1 - cos 2 pi tau_i)            twist as an angle; a whole turn is free (the XY / Wilson shape; the
                                                       kappa form of 27 October that was ours and not adopted)
  E2 elastic:    sum_i tau_i^2                          torsion of a rod; cost grows with the square of the twist held
                                                       (Kirchhoff rod, DNA twist; general knowledge, to verify)
  E3 mismatch:   sum_i (tau_{i+1} - tau_i)^2            cost only where the twist CHANGES along the loop (her "fights
                                                       itself": opposed twists side by side cost; a gluon fold between
                                                       them would relieve it); uniform twist is free
  E4 elastic + mismatch: E2 + E3

The stability problem the term must solve (the sheet, open item 1): the world has one charged object below the muon,
the electron (n = 3, charge 1 in units of e), and no neutral twisted objects at a few MeV. For each form and each loop
length n = 3 to 9 and charge Q = 0, 1, 2 the look finds the lowest-energy assignment of twists in {-1, -2/3, ..., 1}
with net twist Q, and reports it. What a good form would show (ours, written first): E(n, 1) lowest at n = 3 and rising
with n (so the electron is the cheapest way to hold one charge), E(n, 2) well above 2 E(3, 1) (so charge 2 splits),
and E(n, 0) with twist present (the neutrino's shape) above E(n, 0) with none unless something else pays.

WRITTEN BEFORE COMPUTING (ours): E1 makes a whole twist on one diagonal free, so E(n, 1) = 0 for every n, and it ranks
nothing; E2 favours spreading thirds, E(n, 1) = 1/3 for every n >= 3 (three thirds), flat in n, so it does not pick
n = 3; E3 makes uniform twist free, so E(3, 1) = 0 (three thirds) and E(n, 1) > 0 for n not a multiple of 3, but
E(6, 2) = 0 too (six thirds), so it allows charge 2 at n = 6; E4 gives E(3, 1) = 1/3 and E(6, 2) = 2/3, E(6, 1) > 1/3,
so it is the only one of the four under which the electron is the cheapest charged loop at every n and charge 2 costs
double, but it does not forbid charge 2. None of the four forbids a twisted neutral loop by itself. Crowns nothing.
"""
from fractions import Fraction
from itertools import product
import math

VALUES = [Fraction(k, 3) for k in range(-3, 4)]


def e1(taus):
    return sum(1 - math.cos(2 * math.pi * float(t)) for t in taus)


def e2(taus):
    return float(sum(t * t for t in taus))


def e3(taus):
    n = len(taus)
    return float(sum((taus[(i + 1) % n] - taus[i]) ** 2 for i in range(n)))


def e4(taus):
    return e2(taus) + e3(taus)


FORMS = [("E1 periodic", e1), ("E2 elastic", e2), ("E3 mismatch", e3), ("E4 elastic+mismatch", e4)]


def best(form, n, q, present=None):
    out = None
    for taus in product(VALUES, repeat=n):
        if sum(taus) != q:
            continue
        if present is True and all(t == 0 for t in taus):
            continue
        if present is False and any(t != 0 for t in taus):
            continue
        e = form(taus)
        if out is None or e < out[0] - 1e-12:
            out = (e, taus)
    return out


if __name__ == "__main__":
    for name, form in FORMS:
        print(name)
        print("   n   E(n,Q=1)  twists                   E(n,Q=2)   E(n,Q=0, twist present)")
        for n in range(3, 8):
            b1 = best(form, n, 1)
            b2 = best(form, n, 2)
            b0 = best(form, n, 0, present=True)
            print("   %d   %6.3f    %-24s %6.3f     %6.3f" % (
                n, b1[0], " ".join(str(t) for t in b1[1]), b2[0], b0[0]))
    print("The electron's triangle (-1/3, -1/3, -1/3) under each form: " + ", ".join(
        "%s %.3f" % (name, form([Fraction(-1, 3)] * 3)) for name, form in FORMS))
    print("The pion's loop (2/3, 1/3, 0): " + ", ".join("%s %.3f" % (name, form([Fraction(2, 3), Fraction(1, 3), Fraction(0)])) for name, form in FORMS))
    print("Crowns nothing; the form is a decision under S1 and is hers.")

"""A look (sandbox lane; the owner's instruction of 30 October, "Verify." on the sentence "the form holds only roughly for
some quark triplets"). Koide's relation in ratio form, K = (m1 + m2 + m3) / ((2/3)(sqrt m1 + sqrt m2 + sqrt m3)^2), is 1 for
the charged leptons to five figures. This script asks what K is for quark triplets, with the uncertainty propagated, so that
"roughly" becomes a number.

Masses: PDG 2024 central values from memory, TO VERIFY against the reading agent's PDG table before anything is cited.
Quark masses are not pole masses: u, d, s are MS-bar at 2 GeV, c and b MS-bar at their own scale, t a direct (pole-like)
measurement. Mixing definitions is a choice and the published tests (Rodejohann and Zhang 2011; Kartavtsev 2011;
Zenczykowski 2012; all to be read) make different ones; this look uses the PDG numbers as they come, which is the crudest
choice, and says so.

WRITTEN BEFORE COMPUTING (ours): the leptons give K = 1.000 within 1e-4; (u, c, t) and (d, s, b) give K off 1 by a few
per cent, outside their errors for (u, c, t) and inside for (d, s, b) because the light-quark errors are large; (s, c, b) is
the triplet the literature reports as closest (K within about 1 % of 1); (c, b, t) and (u, d, s) are off by more than 5 %.
Also reported: the Brannen phase delta for each triplet (from the two heaviest, as the lepton fit did), to see whether the
quark phases sit at simple fractions of 2/9 as Zenczykowski is said to report (to verify). Kills nothing by itself; it puts
numbers on "roughly". A triplet with K = 1 inside its errors would be a candidate for G6 and rule 13 would apply.
"""
import math
from itertools import product

# (central MeV, error MeV, definition)
Q = {
    "u": (2.16, 0.07, "MSbar 2 GeV"), "d": (4.70, 0.07, "MSbar 2 GeV"), "s": (93.5, 0.8, "MSbar 2 GeV"),
    "c": (1273.0, 4.6, "MSbar m_c"), "b": (4183.0, 7.0, "MSbar m_b"), "t": (172570.0, 290.0, "direct"),
    "e": (0.51099895, 1.5e-10, "pole"), "mu": (105.6583755, 2.3e-6, "pole"), "tau": (1776.86, 0.12, "pole"),
}
TRIPLETS = [("e", "mu", "tau"), ("u", "c", "t"), ("d", "s", "b"), ("s", "c", "b"), ("c", "b", "t"), ("u", "d", "s"), ("d", "s", "c"), ("u", "s", "b")]


def koide(ms):
    return sum(ms) / ((2.0 / 3.0) * sum(math.sqrt(m) for m in ms) ** 2)


def k_with_error(names, samples=20000, seed=1):
    import random
    rng = random.Random(seed)
    c = koide([Q[n][0] for n in names])
    vals = []
    for _ in range(samples):
        ms = [max(1e-9, rng.gauss(Q[n][0], Q[n][1])) for n in names]
        vals.append(koide(ms))
    vals.sort()
    return c, vals[int(0.16 * samples)], vals[int(0.84 * samples)]


def brannen_phase(names):
    """delta from the two heaviest of the triplet, as the lepton fit did (heaviest at angle delta, the lightest at delta + 1/3 turn,
    the middle at delta + 2/3 turn), solved by bisection on the ratio of root masses; None if the ratio is out of the form's range."""
    ms = sorted(Q[n][0] for n in names)
    r = math.sqrt(2)
    target = math.sqrt(ms[2]) / math.sqrt(ms[1])  # heaviest over middle

    def ratio(d):
        return (1 + r * math.cos(d)) / (1 + r * math.cos(d + 4 * math.pi / 3))

    lo, hi = 0.0, 2 * math.pi / 3
    # ratio is monotone on (0, 2pi/3)? it rises from 1 toward the pole where the middle vanishes; bracket by scanning
    grid = [lo + (hi - lo) * i / 2000 for i in range(2001)]
    vals = [ratio(g) for g in grid]
    for i in range(2000):
        if (vals[i] - target) * (vals[i + 1] - target) < 0:
            a, b = grid[i], grid[i + 1]
            for _ in range(100):
                m = 0.5 * (a + b)
                if (ratio(a) - target) * (ratio(m) - target) <= 0:
                    b = m
                else:
                    a = m
            d = 0.5 * (a + b)
            A = math.sqrt(ms[2]) / (1 + r * math.cos(d))
            pred_light = (A * (1 + r * math.cos(d + 2 * math.pi / 3))) ** 2
            return d, A, pred_light
    return None


if __name__ == "__main__":
    print("Koide ratio K (1 = exact) with 68 % range from the quoted errors; masses as PDG quotes them (mixed definitions):")
    for t in TRIPLETS:
        c, lo, hi = k_with_error(t)
        inside = lo <= 1.0 <= hi
        print("  %-14s K = %.4f  [%.4f, %.4f]  %s  (%s)" % (
            ",".join(t), c, lo, hi, "K=1 inside" if inside else "K=1 OUTSIDE", "; ".join(Q[n][2] for n in t)))
    print()
    print("Brannen phase from the two heaviest, and the lightest mass it then predicts:")
    for t in TRIPLETS:
        out = brannen_phase(t)
        light = min(Q[n][0] for n in t)
        if out is None:
            print("  %-14s no phase in range" % ",".join(t))
            continue
        d, A, pl = out
        print("  %-14s delta = %.4f rad = %.4f turn (delta/(2/9) = %.3f); A = %.3f sqrt(MeV); lightest predicted %.4g MeV vs %.4g (%+.0f %%)" % (
            ",".join(t), d, d / (2 * math.pi), d / (2 / 9), A, pl, light, 100 * (pl / light - 1)))
    print()
    print("Masses from memory; VERIFY against the PDG table before citing. Crowns nothing.")

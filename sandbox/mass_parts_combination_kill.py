"""A look (sandbox lane; the owner's instruction of 30 October: separate the twist, spin, charge and loop parts of mass and
stop treating MeV as one unit that adds and subtracts cleanly). If the parts combine other than by addition, a whole count
would show up not in m but in some power of m. Published hints (general knowledge, to verify): energies add but masses do
not (a proton's quarks weigh a few MeV each and the proton 938); Koide's relation is exact in square roots of mass; the
rest energy and momentum combine as squares (E^2 = m^2 + p^2).

Test: for p in (1/2, 1, 2), is there an n_e up to 5,000 at which n_e * (m/m_e)^p is whole for muon, proton, neutron and
tau together, beyond chance? p = 1 is the test already run; p = 1/2 is the Koide hint; p = 2 is parts in quadrature.

WRITTEN BEFORE COMPUTING (ours): passes at chance level for all three powers. A count that is whole in sqrt(m) or m^2
beyond chance would be a candidate for how the parts combine and would then meet rule 13 (count the other combinations
that match). Kills: 'the parts combine as plain squares or plain square roots with one unit' if chance. Crowns nothing.
"""
M_E = 0.51099895000
MASSES = {"muon": (105.6583755, 2.3e-6), "proton": (938.27208816, 2.9e-7), "neutron": (939.56542052, 5.4e-7), "tau": (1776.86, 0.12)}


def run(power, n_max=5000, sigma=3.0):
    ratios = {}
    for k, (m, e) in MASSES.items():
        r = (m / M_E) ** power
        ratios[k] = (r, abs(power) * r * e / m)
    passes, expect = [], 0.0
    for n in range(1, n_max + 1):
        good, p = True, 1.0
        for r, dr in ratios.values():
            x = n * r
            if abs(x - round(x)) > sigma * n * dr + 1e-12:
                good = False
            p *= min(1.0, 2 * sigma * n * dr)
        expect += p
        if good:
            passes.append(n)
    print("power %.1f: all four whole at %d values of n_e to %d (chance %.2f): %s" % (power, len(passes), n_max, expect, passes[:8]))
    mu = ratios["muon"]
    mu_pass = [n for n in range(1, n_max + 1) if abs(n * mu[0] - round(n * mu[0])) <= sigma * n * mu[1]]
    mu_exp = sum(min(1.0, 2 * sigma * n * mu[1]) for n in range(1, n_max + 1))
    print("   muon alone: %d (chance %.1f); (m_mu/m_e)^p = %.6f" % (len(mu_pass), mu_exp, mu[0]))


if __name__ == "__main__":
    for p in (0.5, 1.0, 2.0):
        run(p)

"""A look (sandbox lane; the owner's request of 29/30 October: "build out the table"): the observed particles written in
her counts. Step 1 of the five-step path of VISION Update 148.

Her rules used (hers; docs/design/twist_curl_rules_current.md): mass counts looped diagonals, a long diagonal counting
one; the electron is the unit, n_e diagonals (n_e = 3 as it stands, open whether larger); charge is net twist in thirds;
spin 1/2 on a full curl, 1 on a half curl.

Inputs: PDG masses, from memory (general knowledge; every value is to be verified against the PDG 2024 listings before
any number here is quoted outside the sandbox). Uncertainties are given where they matter for the integer test.

What the table reports, per particle: mass in units of the electron (m/m_e, measured); charge in thirds; spin; the
diagonal count n = n_e * m/m_e for n_e = 3; n mod 3; for charged leptons the gluons per run k = (n - 3)/3 under equal
spacing.

The integer test (exact arithmetic on her rule, ours): if mass is a count, then for every particle n = n_e * (m/m_e)
must be a whole number within the measurement error. The muon-to-electron ratio is known to about 2e-8 (relative), so
for n_e up to a few thousand the product's error is far below 1 and the test is sharp. The script lists every n_e from
1 to N_MAX for which the muon, the proton (ratio known to 6e-11 relative) and the tau (ratio known to about 7e-5
relative) all give whole numbers within their errors, and the nearest misses.

WRITTEN BEFORE COMPUTING (ours): for n_e = 3 the muon gives 620.30, not an integer, so n_e = 3 fails the integer test
outright; the record's "621 = 3 + 3 x 206" rounded 206.77 to 206. We expect no n_e below 100 to pass all three, and
expect a scatter of near-passes at larger n_e of the kind any three irrational-looking ratios produce by chance (about
N_MAX * (2 tol)^3 by counting). Kills, if the enumeration says so: "n_e = 3 is consistent with mass as a count" (ours,
declared). If some n_e passes with the tau too, it is a candidate and no more: rule 13 (count how many arbitrary
combinations would also match) applies before it is called anything. Crowns nothing.
"""
import math

M_E = 0.51099895000  # MeV, PDG (from memory; to verify)
U_E = M_E / 3.0

# name, mass MeV, +- MeV, charge in thirds, spin (units of hbar), content (general knowledge)
PARTICLES = [
    ("electron", 0.51099895, 3e-10, -3, 0.5, "lepton"),
    ("muon", 105.6583755, 2.3e-6, -3, 0.5, "lepton"),
    ("tau", 1776.86, 0.12, -3, 0.5, "lepton"),
    ("neutrino (any)", 8e-7, 8e-7, 0, 0.5, "lepton; mass < 0.8 eV (bound)"),
    ("photon", 0.0, 0.0, 0, 1.0, "boson"),
    ("pi+", 139.57039, 0.00018, 3, 0.0, "u anti-d"),
    ("pi0", 134.9768, 0.0005, 0, 0.0, "u anti-u / d anti-d"),
    ("K+", 493.677, 0.016, 3, 0.0, "u anti-s"),
    ("K0", 497.611, 0.013, 0, 0.0, "d anti-s"),
    ("eta", 547.862, 0.017, 0, 0.0, "uu dd ss"),
    ("rho(770)", 775.26, 0.25, 3, 1.0, "u anti-d, spins parallel"),
    ("omega(782)", 782.66, 0.13, 0, 1.0, "uu dd"),
    ("eta'(958)", 957.78, 0.06, 0, 0.0, "uu dd ss"),
    ("phi(1020)", 1019.461, 0.016, 0, 1.0, "s anti-s"),
    ("proton", 938.27208816, 2.9e-7, 3, 0.5, "uud"),
    ("neutron", 939.56542052, 5.4e-7, 0, 0.5, "udd"),
    ("Lambda", 1115.683, 0.006, 0, 0.5, "uds"),
    ("Sigma+", 1189.37, 0.07, 3, 0.5, "uus"),
    ("Sigma0", 1192.642, 0.024, 0, 0.5, "uds"),
    ("Sigma-", 1197.449, 0.030, -3, 0.5, "dds"),
    ("Xi0", 1314.86, 0.20, 0, 0.5, "uss"),
    ("Xi-", 1321.71, 0.07, -3, 0.5, "dss"),
    ("Delta(1232)", 1232.0, 2.0, 6, 1.5, "uuu (Delta++)"),
    ("Omega-", 1672.45, 0.29, -3, 1.5, "sss"),
    ("D+", 1869.66, 0.05, 3, 0.0, "c anti-d"),
    ("J/psi", 3096.900, 0.006, 0, 1.0, "c anti-c"),
    ("B+", 5279.34, 0.12, 3, 0.0, "u anti-b"),
    ("Upsilon(1S)", 9460.30, 0.26, 0, 1.0, "b anti-b"),
    ("W", 80369.2, 13.3, 3, 1.0, "boson"),
    ("Z", 91187.6, 2.1, 0, 1.0, "boson"),
    ("Higgs", 125200.0, 110.0, 0, 0.0, "boson"),
    ("up (MS-bar 2 GeV)", 2.16, 0.07, 2, 0.5, "quark; scheme-dependent"),
    ("down (MS-bar 2 GeV)", 4.70, 0.07, -1, 0.5, "quark; scheme-dependent"),
    ("strange (MS-bar 2 GeV)", 93.5, 0.8, -1, 0.5, "quark; scheme-dependent"),
    ("charm (MS-bar m_c)", 1273.0, 5.0, 2, 0.5, "quark; scheme-dependent"),
    ("bottom (MS-bar m_b)", 4183.0, 7.0, -1, 0.5, "quark; scheme-dependent"),
    ("top (direct)", 172570.0, 290.0, 2, 0.5, "quark"),
]


def table(n_e=3):
    print("electron unit: n_e = %d diagonals, %.6f MeV per diagonal" % (n_e, M_E / n_e))
    print("%-24s %14s %8s %5s %12s %6s %8s  %s" % ("particle", "mass MeV", "Q/3", "spin", "n (count)", "n mod3", "k=(n-3)/3", "content"))
    for name, m, dm, q, s, content in PARTICLES:
        n = n_e * m / M_E
        k = (n - 3) / 3
        print("%-24s %14.6g %8d %5.1f %12.2f %6d %8.1f  %s" % (name, m, q, s, n, round(n) % 3, k, content))
    print()


def integer_test(n_max=5000, tol_sigma=3.0):
    # ratios to the electron mass, with absolute errors (from the mass errors above; m_e's error is negligible)
    ratios = {
        "muon": (105.6583755 / M_E, 2.3e-6 / M_E),
        "proton": (938.27208816 / M_E, 2.9e-7 / M_E),
        "tau": (1776.86 / M_E, 0.12 / M_E),
    }
    print("integer test: n_e such that n_e * (m/m_e) is whole within %.0f sigma for muon, proton and tau" % tol_sigma)
    for k, (r, dr) in ratios.items():
        print("   %-7s m/m_e = %.9f +- %.1e" % (k, r, dr))
    passes = []
    for n_e in range(1, n_max + 1):
        ok = True
        dists = []
        for k, (r, dr) in ratios.items():
            x = n_e * r
            d = abs(x - round(x))
            dists.append(d)
            if d > tol_sigma * n_e * dr + 1e-12:
                ok = False
        if ok:
            passes.append((n_e, dists))
    # chance expectation: product of the windows
    expect = 0.0
    for n_e in range(1, n_max + 1):
        p = 1.0
        for k, (r, dr) in ratios.items():
            p *= min(1.0, 2 * tol_sigma * n_e * dr)
        expect += p
    print("   n_e from 1 to %d: %d pass all three; chance expectation %.2f" % (n_max, len(passes), expect))
    for n_e, d in passes[:40]:
        print("      n_e = %5d  muon n = %.4f  proton n = %.4f  tau n = %.3f" % (
            n_e, n_e * ratios["muon"][0], n_e * ratios["proton"][0], n_e * ratios["tau"][0]))
    # muon alone, the sharp one
    mu, dmu = ratios["muon"]
    mu_pass = [n_e for n_e in range(1, n_max + 1) if abs(n_e * mu - round(n_e * mu)) <= tol_sigma * n_e * dmu]
    print("   muon alone: %d of %d pass; first ten: %s" % (len(mu_pass), n_max, mu_pass[:10]))
    print("   n_e = 3: muon n = %.4f, proton n = %.4f, tau n = %.3f" % (3 * mu, 3 * ratios["proton"][0], 3 * ratios["tau"][0]))
    print()


def koide():
    me, mm, mt = 0.51099895, 105.6583755, 1776.86
    q = (me + mm + mt) / (math.sqrt(me) + math.sqrt(mm) + math.sqrt(mt)) ** 2
    print("Koide: (m_e + m_mu + m_tau) / (sqrt m_e + sqrt m_mu + sqrt m_tau)^2 = %.6f  (2/3 = %.6f)" % (q, 2 / 3))
    print("in counts the same ratio is unit-free: it holds for n as for m, whatever n_e.")
    print()


if __name__ == "__main__":
    table(3)
    integer_test()
    koide()

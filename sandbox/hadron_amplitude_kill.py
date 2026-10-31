"""A look (sandbox lane; gap G4 of docs/design/koide_gaps_2026-10-30.md, "several loops"; the owner's "proceed where you can").
The Koide form says a lepton's root-mass is an amplitude, constant part plus signed part. The simplest rule for several
loops is that amplitudes ADD: sqrt(m_hadron) = sum over its quark loops of a_q, each flavour one amplitude. The proton
(uud), neutron (udd) and charged pion (u, anti-d) then fix two constants a_u, a_d from three masses, so the pion is a
prediction, and the Delta++ (uuu, spin 3/2, 1232 MeV) and rho+ (u anti-d, spin 1, 775 MeV) are held out.

Masses (PDG 2025, MeV): p 938.27208816, n 939.5654205, pi+ 139.57039, Delta(1232) 1232 +- 2, rho(770) 775.26 +- 0.23.

Three rules, each with its expectation WRITTEN BEFORE COMPUTING (ours):
  R-add:  sqrt m = sum a_q (antiquark same as quark). Two constants, fitted on p and n; pion predicted.
          Expectation: fails badly; the nucleon difference is 0.02 sqrt(MeV) while the pion needs a_u + a_d = 11.8 and the
          nucleons need it near 20.4 (= 61.3/3). Kill.
  R-anti: as R-add but an antiquark's amplitude is NEGATIVE (the sign Brannen's neutrino uses). Pion = a_u - a_d = 0.02.
          Expectation: fails worse (pion predicted below 1 MeV). Kill.
  R-spin: sqrt m = sum a_q - u_s * s (her E-C: spin takes mass away; u_s a third constant). Three constants fitted on p, n,
          pion; Delta++ and rho+ held out. Expectation: the fit exists (three equations, three unknowns) but u_s comes out
          with the WRONG SIGN (spin adds root-mass, since the spin-1/2 nucleons need a bigger sum than the spin-0 pion), and
          the held-out Delta++ and rho+ both miss by a factor of about two in mass. Kill of the additive-amplitude family
          with a linear spin term.
Also printed, rule 13: for each rule, constants, masses used, predictions, and the miss on each held-out mass.
Crowns nothing. If a rule's held-out masses land within 1 %, it is a candidate, not a result (count the alternatives first).
"""
import math

M = {"p": 938.27208816, "n": 939.5654205, "pi": 139.57039, "Delta": 1232.0, "rho": 775.26}
S = {k: math.sqrt(v) for k, v in M.items()}


def report(name, consts, preds):
    print(name)
    for k, v in consts.items():
        print("   constant %-4s = %+.4f sqrt(MeV)" % (k, v))
    for k, root in preds.items():
        m = math.copysign(root * root, 1.0)
        print("   %-6s predicted sqrt = %+.3f -> %.1f MeV; measured %.1f; miss %+.0f %%" % (k, root, m, M[k], 100 * (m / M[k] - 1)))


# R-add: 2a_u + a_d = sqrt m_p, a_u + 2a_d = sqrt m_n
au = (2 * S["p"] - S["n"]) / 3
ad = (2 * S["n"] - S["p"]) / 3
report("R-add (2 constants from p, n; pion, Delta++, rho+ predicted):", {"a_u": au, "a_d": ad},
       {"pi": au + ad, "Delta": 3 * au, "rho": au + ad})
# R-anti: same constants; pion = a_u - a_d (anti-d negative); rho likewise
report("R-anti (antiquark negative; same constants):", {"a_u": au, "a_d": ad}, {"pi": au - ad, "rho": au - ad, "Delta": 3 * au})
# R-spin: 2a_u + a_d - u/2 = Sp ; a_u + 2a_d - u/2 = Sn ; a_u + a_d - 0 = Spi
ad_minus_au = S["n"] - S["p"]
sum_ud = S["pi"]
# add the nucleon equations: 3(a_u + a_d) - u = Sp + Sn
u = 3 * sum_ud - (S["p"] + S["n"])
au2 = (sum_ud - ad_minus_au) / 2
ad2 = (sum_ud + ad_minus_au) / 2
report("R-spin (3 constants from p, n, pion; Delta++ at s = 3/2 and rho+ at s = 1 held out):",
       {"a_u": au2, "a_d": ad2, "u_s": u},
       {"Delta": 3 * au2 - u * 1.5, "rho": au2 + ad2 - u * 1.0})
print("   sign check: u_s %s, so in this rule spin %s root-mass" % ("> 0" if u > 0 else "< 0", "takes away" if u > 0 else "ADDS"))
print()
print("rule 13: R-add 2 constants, 2 masses fitted, 3 predicted; R-anti the same; R-spin 3 constants, 3 fitted, 2 predicted.")
print("Masses PDG 2025 (Delta and rho from memory, to verify). Crowns nothing.")

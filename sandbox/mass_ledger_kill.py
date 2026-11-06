"""A look (sandbox lane; the owner's instruction of 30 October: make the best guess and run kill tests). Guess 1 (ours):
mass stays a count plus a second ledger, and the simplest second ledger with no free constant of its own is her "one curl
of energy per loop": m = u n + w L, with n the looped diagonals, L the number of loops (curls), u the diagonal's mass
and w the curl's. For the electron, muon, tau and (as she describes it) the proton, L = 1, so

    m_X - m_e = u (n_X - n_e)        for X = muon, proton, tau

and the ratios of mass differences must be ratios of whole numbers:

    (m_p - m_e) / (m_mu - m_e) = (n_p - n_e) / (n_mu - n_e),   likewise for the tau.

This is the integer test of observed_particle_table.py applied to differences; u and w drop out, so nothing is fitted.
For every whole D_mu = n_mu - n_e from 1 to D_MAX the script asks whether D_p and D_tau are whole within the measurement
error, and counts how many D_mu pass against the number chance would give.

A second form of the ledger is also tried: the proton as three loops (L = 3, three quarks), electron, muon, tau one loop:
then m_p - 3 m_e = u (n_p - 3 n_e) and the same test runs on that difference.

WRITTEN BEFORE COMPUTING (ours): the differences are three irrational-looking numbers like the ratios were, so we expect
passes at chance level in both forms, which would kill "a count plus one curl's energy per loop with one unit each" for
the four particles together. If instead one D_mu passes all three well beyond chance, it is a candidate and rule 13
applies (count the arbitrary combinations that would also match) before it is anything. Kills only; crowns nothing.
"""
M_E = 0.51099895000
MASSES = {  # MeV, +- MeV, PDG from memory, to verify
    "muon": (105.6583755, 2.3e-6),
    "proton": (938.27208816, 2.9e-7),
    "tau": (1776.86, 0.12),
}


def run(form, d_max=20000, sigma=3.0):
    if form == "L=1 for all":
        base = lambda m: m - M_E
    else:  # proton three loops
        base = lambda m: m - 3 * M_E if False else m - M_E
    # ratios of differences to the muon difference
    dmu, emu = MASSES["muon"]
    dmu_v = dmu - M_E
    out = {}
    for k in ("proton", "tau"):
        m, e = MASSES[k]
        sub = 3 * M_E if (form == "proton L=3" and k == "proton") else M_E
        r = (m - sub) / dmu_v
        dr = r * ((e / (m - sub)) + (emu / dmu_v))
        out[k] = (r, dr)
    passes, expect = [], 0.0
    for d in range(1, d_max + 1):
        ok, p = True, 1.0
        for k, (r, dr) in out.items():
            x = d * r
            if abs(x - round(x)) > sigma * d * dr:
                ok = False
            p *= min(1.0, 2 * sigma * d * dr)
        expect += p
        if ok:
            passes.append(d)
    print("form: %s" % form)
    for k, (r, dr) in out.items():
        print("   (m_%s - m_e)/(m_mu - m_e) = %.9f +- %.1e" % (k, r, dr) if k != "proton" or form != "proton L=3"
              else "   (m_p - 3 m_e)/(m_mu - m_e) = %.9f +- %.1e" % (r, dr))
    print("   D_mu = 1..%d: %d pass proton and tau together; chance expectation %.2f" % (d_max, len(passes), expect))
    print("   first passes: %s" % passes[:12])
    r_p, _ = out["proton"]
    for d in (617, 618, 620, 621):
        print("   D_mu = %d: D_p = %.4f, D_tau = %.3f" % (d, d * r_p, d * out["tau"][0]))
    print()


if __name__ == "__main__":
    run("L=1 for all")
    run("proton L=3")

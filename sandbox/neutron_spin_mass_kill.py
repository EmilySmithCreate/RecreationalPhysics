"""A look (sandbox lane; the owner's idea of 30 October: "Maybe a 1/2 spin cancels mass when there is no twist", and her
request to add the neutron to the table). Two readings of her sentence, and the neutron is the object that tells them apart:

  Reading A (object level): an object with spin 1/2 and no NET twist has its mass cancelled. The neutrino (net 0, spin
      1/2, mass below 8e-7 MeV) fits. The neutron (net 0, spin 1/2, 939.57 MeV) does not. Kind: measurement.
  Reading B (loop level): a LOOP whose own twists cancel to zero weighs nothing; a loop with net twist weighs its count.
      The neutrino is one such loop. The neutron's three loops each carry net twist (-1/3, -1/3, +2/3), so none cancels
      and the neutron weighs as the proton does. Reading B survives the neutron.

Under reading B two things are then exact arithmetic on measured masses (PDG from memory, to verify):

  (1) The neutron and proton have the same three loops up to sign, so under "mass counts looped diagonals with one unit"
      m_n - m_p must be a whole number of units: (m_n - m_p)/m_e = 2.531 and n_e * 2.531 must be whole.
  (2) The integer test of observed_particle_table.py with the neutron added: n_e at which e, mu, p, n, tau are all whole.

WRITTEN BEFORE COMPUTING (ours): reading A is killed by the neutron with no computation. For (1), at n_e = 3 the
difference is 7.59 units, not whole; over n_e to 5,000 we expect passes at chance level, since 2.531 is as irrational-
looking as the other ratios. For (2) we expect the four-ratio test to pass at about chance (fewer than the 3 of the
three-ratio test). Kills only; crowns nothing.
"""
M_E = 0.51099895000
MASSES = {  # MeV, +- MeV
    "muon": (105.6583755, 2.3e-6),
    "proton": (938.27208816, 2.9e-7),
    "neutron": (939.56542052, 5.4e-7),
    "tau": (1776.86, 0.12),
}


def run(n_max=5000, sigma=3.0):
    mn, en = MASSES["neutron"]
    mp, ep = MASSES["proton"]
    d = (mn - mp) / M_E
    dd = (en + ep) / M_E
    print("reading A: neutron has net twist 0, spin 1/2 and mass %.3f MeV; the neutrino below 8e-7 MeV. KILLED (measurement)." % mn)
    print("reading B, (1): (m_n - m_p)/m_e = %.7f +- %.1e; at n_e = 3 that is %.3f units (allowed error %.1e)" % (d, dd, 3 * d, 3 * sigma * dd))
    passes = [n for n in range(1, n_max + 1) if abs(n * d - round(n * d)) <= sigma * n * dd]
    expect = sum(min(1.0, 2 * sigma * n * dd) for n in range(1, n_max + 1))
    print("   n_e = 1..%d: %d values make the difference whole; chance %.2f; first: %s" % (n_max, len(passes), expect, passes[:8]))
    ratios = {k: (m / M_E, e / M_E) for k, (m, e) in MASSES.items()}
    ok, expect4 = [], 0.0
    for n in range(1, n_max + 1):
        good, p = True, 1.0
        for k, (r, dr) in ratios.items():
            x = n * r
            if abs(x - round(x)) > sigma * n * dr + 1e-12:
                good = False
            p *= min(1.0, 2 * sigma * n * dr)
        expect4 += p
        if good:
            ok.append(n)
    print("reading B, (2): n_e at which muon, proton, neutron and tau are all whole: %d (%s); chance %.2f" % (len(ok), ok[:10], expect4))
    print("   at n_e = 3: neutron n = %.3f, proton n = %.3f" % (3 * ratios["neutron"][0], 3 * ratios["proton"][0]))


if __name__ == "__main__":
    run()

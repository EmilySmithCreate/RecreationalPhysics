"""A look (sandbox lane; the owner's instruction of 30 October: mass as an equation with positive and negative twist parts,
spin, loops with and without twist, and ratios of emergent values, not one additive number). The first published equation
of that shape is Koide's relation in Brannen's form (Koide 1983/1990 abstracts read; Brannen 2006 not read, from general
knowledge, to verify):

    sqrt(m_g) = A * (1 + sqrt(2) * cos(delta + 2*pi*g/3)),   g = 0, 1, 2 for tau, electron, muon (Brannen's ordering as it comes out of the fit).

Two constants (A, delta) for three masses, so it makes exactly one prediction, which is Koide's relation
(sum sqrt m)^2 = (3/2) sum m. In her terms each lepton's root-mass is a constant part plus a signed part at an angle a
third of a turn apart from the others, and the electron is the one where the two parts nearly cancel.

What this script does, with its expectations written first:
  (1) Fit A and delta from the electron and muon only; predict the tau (held out) and compare with the measured value.
      Expectation (published): the prediction lands within about 0.2 MeV of 1776.86, i.e. Koide holds.
  (2) Report delta in turns, the three cos values, and the angle at which the signed part cancels the constant part
      exactly (cos phi = -1/sqrt(2), phi = 3/8 turn): a loop at that angle is massless. Expectation: the electron sits
      within a few hundredths of a turn of it.
  (3) Count constants against data points: 2 constants, 3 masses, 1 prediction. Rule 13 applies before anything more.
  (4) Her nucleons with NO new constant: if the proton and neutron are three loops whose root-mass amplitudes add, each
      loop taking one of the three lepton amplitudes with either sign, is 938.27 or 939.57 MeV reached? Expectation
      (ours): no; the nearest combination is reported with its miss. A hit within the measured errors would be a
      candidate and rule 13 would apply.
Kills (4) if no combination lands; records what the published form gives and where her 'near cancellation' sits in it.
"""
from itertools import combinations_with_replacement, product
import math

M = {"electron": 0.51099895, "muon": 105.6583755, "tau": (1776.86, 0.12)}


def fit_from_e_mu():
    # sqrt(m_mu) = A(1 + r cos(d + 2pi/3)), sqrt(m_e) = A(1 + r cos(d + 4pi/3)), r = sqrt 2. Solve for d by bisection on the ratio.
    r = math.sqrt(2)
    se, smu = math.sqrt(M["electron"]), math.sqrt(M["muon"])
    target = smu / se

    def ratio(d):
        return (1 + r * math.cos(d + 4 * math.pi / 3)) / (1 + r * math.cos(d + 2 * math.pi / 3))

    # ratio(d) rises from 1 at d = 0 to infinity at d = pi/12 (where the electron is massless); bracket (0, pi/12)
    lo, hi = 0.0, math.pi / 12 - 1e-12
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if ratio(mid) > target:
            hi = mid
        else:
            lo = mid
    d = 0.5 * (lo + hi)
    A = se / (1 + r * math.cos(d + 2 * math.pi / 3))
    return A, d


if __name__ == "__main__":
    A, d = fit_from_e_mu()
    r = math.sqrt(2)
    tau_pred = (A * (1 + r * math.cos(d))) ** 2
    print("fit from electron and muon: A = %.6f sqrt(MeV), delta = %.6f rad = %.5f turn (2/9 rad = %.6f)" % (A, d, d / (2 * math.pi), 2 / 9))
    print("held-out tau: predicted %.3f MeV, measured %.2f +- %.2f MeV, difference %.2f MeV (%.1f sigma)" % (
        tau_pred, M["tau"][0], M["tau"][1], tau_pred - M["tau"][0], (tau_pred - M["tau"][0]) / M["tau"][1]))
    for name, g in (("tau", 0), ("electron", 1), ("muon", 2)):
        phi = d + 2 * math.pi * g / 3
        c = r * math.cos(phi)
        print("   %-8s angle %.4f turn: sqrt m = A (1 %+.4f) = %.4f; constant part A = %.4f, signed part %+.4f" % (
            name, (phi / (2 * math.pi)) % 1, c, A * (1 + c), A, A * c))
    zero = math.acos(-1 / r)
    phi_e = (d + 2 * math.pi / 3) % (2 * math.pi)
    print("exact cancellation at %.4f turn (cos = -1/sqrt 2); the electron sits at %.4f turn, %.4f turn away" % (
        zero / (2 * math.pi), phi_e / (2 * math.pi), abs(phi_e - zero) / (2 * math.pi)))
    s = sum(math.sqrt(m if not isinstance(m, tuple) else m[0]) for m in M.values())
    q = s * s / sum(m if not isinstance(m, tuple) else m[0] for m in M.values())
    print("Koide ratio from measured masses: %.6f (form says 1.5 exactly)" % q)
    print("constants 2, masses 3, predictions 1 (rule 13).")
    amps = {g: A * (1 + r * math.cos(d + 2 * math.pi * g / 3)) for g in (0, 1, 2)}
    best = []
    for combo in combinations_with_replacement((0, 1, 2), 3):
        for signs in product((1, -1), repeat=3):
            s = sum(sg * amps[g] for sg, g in zip(signs, combo))
            best.append((s * s, combo, signs))
    for name, m in (("proton", 938.27208816), ("neutron", 939.56542052)):
        near = min(best, key=lambda b: abs(b[0] - m))
        print("(4) %s as three signed lepton amplitudes: nearest %.2f MeV (loops %s, signs %s), miss %.1f%%" % (
            name, near[0], near[1], near[2], 100 * (near[0] - m) / m))
    s3 = (3 * amps[2]) ** 2
    print("    three loops at the muon's angle: %.1f MeV (proton +%.1f%%); the nucleons' root masses are %.3f and %.3f sqrt(MeV)" % (
        s3, 100 * (s3 / 938.27208816 - 1), math.sqrt(938.27208816), math.sqrt(939.56542052)))

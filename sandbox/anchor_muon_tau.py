"""A look (sandbox lane; the owner's "proceed" of 30 October on: use the muon or the pion as the second anchor for the two
constants of the twist term, and predict the third). Exact arithmetic under the state as built; predictions written
before the numbers were computed. Published inputs (general knowledge, to verify at the source: PDG): m_mu/m_e = 206.768,
m_tau/m_e = 3477.23, m_pi+-/m_e = 273.13.

The term: E = eps [sum tau^2 + sum (tau_next - tau)^2] + eps_w Wr^2 per loop; the loop's "mass" here is its energy under
the term (a reading, ours: the sheet's mass is a count of diagonals, and this look asks only whether the term's energies
can stand in the measured ratios). Two constants, so two anchors pin them and the third particle is the prediction.

Exact, no computing needed:
  electron: the triangle of thirds, Wr = 0: E_e = eps / 3.
  pion (flat, as built: loops of net 2/3 and 1/3): 4/9 + 1/3 = 7/9, Wr = 0: E_pi / E_e = 7/3 = 2.33 against 273.13
      measured. So the flat pion CANNOT be the second anchor: its ratio is fixed with no constant free, and it is wrong
      by a factor of about 117. (Kills: "the pion anchors the term as built".) A coiled pion could; not built.
  muon: her hypothesis of 29 October, the next stable object after the electron is a coil of some minimum size. A coil of
      n >= 4 box diagonals holding charge 1 in thirds costs 5/9 eps at best (three thirds side by side), plus eps_w Wr^2.
      The anchor pins r = eps_w / eps = (206.768/3 - 5/9) / Wr_mu^2.
  tau: predicted as the next coil of the same family: E_tau / E_e = 3 (5/9 + r Wr^2).

Predictions (ours, written before running): the coil families of sandbox/coil_writhe.py have writhe growing by a fixed
step per turn (tight 0.760 + 1.013 (m - 1); wide 0.925 + 1.143 (m - 1)), so the ladder of ratios goes roughly as m^2 and
is coarse: steps of 25 to 100 per cent. The tau needs Wr_tau / Wr_mu = sqrt((3477.23/3 - 5/9) / (206.768/3 - 5/9)) = 4.11
on the muon's own family, which falls between turns, so on ONE family (muon and tau both tight, or both wide) no coil
lands within 1 per cent of the tau. Across the four family pairings and m up to 6 there are about 20 candidate
combinations at that spacing, so we expect at least one to land within a few per cent BY CHANCE; a match there counts
for nothing (rule 13) until a rule says which coil is the muon and which the tau. Crowns nothing.
"""
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from coil_writhe import TURN, WIDE, coil, writhe  # noqa: E402

MU, TAU, PI = 206.768, 3477.23, 273.13
FAMILIES = {"tight": (TURN, [(2, 1, 1), (2, 1, -1)], [(-2, -1, -1), (-2, -1, 1)]),
            "wide": (WIDE, [(2, 1, 1), (2, 1, -1), (2, 1, 1), (2, 1, -1)], [(-2, -1, -1), (-2, -1, 1), (-2, -1, -1), (-2, -1, 1)])}

if __name__ == "__main__":
    print("electron E/eps = 1/3; flat pion E/eps = 7/9, ratio 7/3 = %.2f against %.2f measured: the flat pion cannot anchor" % (7 / 3, PI))
    wr = {name: {m: writhe(coil(m, *fam)) for m in range(1, 7)} for name, fam in FAMILIES.items()}
    need = np.sqrt((TAU / 3 - 5 / 9) / (MU / 3 - 5 / 9))
    print("the tau needs Wr_tau / Wr_mu = %.3f on the muon's family" % need)
    hits = []
    for mf, mm in ((f, m) for f in FAMILIES for m in (1, 2)):
        r = (MU / 3 - 5 / 9) / wr[mf][mm] ** 2
        print("muon = %s coil, m = %d turns, Wr = %.3f: pins eps_w/eps = %.1f" % (mf, mm, wr[mf][mm], r))
        for tf in FAMILIES:
            for mt in range(1, 7):
                ratio = 3 * (5 / 9 + r * wr[tf][mt] ** 2)
                off = 100 * (ratio / TAU - 1)
                flag = "  <-- within 1%" if abs(off) < 1 else ""
                print("    tau = %s m = %d (Wr %.3f): predicted m_tau/m_e = %7.1f, off by %+6.1f%%%s" % (tf, mt, wr[tf][mt], ratio, off, flag))
                hits.append((abs(off), mf, mm, tf, mt, ratio))
    hits.sort()
    print("combinations tried: %d; nearest: muon %s m=%d, tau %s m=%d, %.1f (%.2f%% off)" % (len(hits), *hits[0][1:5], hits[0][5], hits[0][0]))

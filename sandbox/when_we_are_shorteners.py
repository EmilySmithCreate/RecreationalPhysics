"""Sandbox look (rule 16): under the per-universe reading of piece 12's rule (ii) (VISION Update 68), what does each
proposed shortener of the observer era do to "when we are"?

    python sandbox/when_we_are_shorteners.py        # writes sandbox/out/when_we_are_shorteners_2026-10-18.txt

The owner's question of 18 October (`sandbox/NOTEBOOK.md`): the only issue left is that we are at 1.4e10 years where the
published count ([LBS16]) puts the most likely observer near 1e13; does what we know about ourselves (no interaction
between planets, no space wars, a rip or dark energy pulling galaxies apart) bring the prediction forward?

Uses the Stage E population model (`src/orh/cosmic.py`, Loeb et al.'s equations with declared knobs, O125). Reads off
F_today (the share of the observer count before our age) and the peak of dP/dln t under: (a) all stars, no window;
(b) red dwarfs excluded (m >= 0.5); (c) her observation window as a hard cut at 1e11 yr; (d) a rip at 30, 50, 100 Gyr;
(e) an interaction factor gamma (company helps or hurts). A look; it supports nothing (rule 16).
"""
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from orh.cosmic import PLANCK18, PopulationModel   # noqa: E402

TODAY = PLANCK18["age_Gyr"]


def read(model, w, cut_gyr=None):
    t = model.t
    w = w.copy()
    if cut_gyr is not None:
        w[t > cut_gyr] = 0.0
    s = model.summarize(w)
    return s["F_today"], s["t_peak_gyr"], s["t50_gyr"]


def main():
    model = PopulationModel()
    lines = []
    P = lines.append
    P("When we are, under the per-universe reading (Update 68), on the Stage E population model (ref class 'moments', tau_evo 0)")
    P("columns: share of the observer count before today (F_today); peak of dP/dln t (Gyr); median (Gyr)")
    P("")
    rows = [
        ("(a) all stars m >= 0.08, no window, star formation cutoff 50 Gyr (Loeb et al.'s setting)", dict(m_min=0.08), None),
        ("(b) red dwarfs excluded, m >= 0.5", dict(m_min=0.5), None),
        ("(b') Sun-like only, m >= 0.9", dict(m_min=0.9), None),
        ("(c) all stars, her observation window as a hard cut at 100 Gyr", dict(m_min=0.08), 100.0),
        ("(c') all stars, window at 1000 Gyr", dict(m_min=0.08), 1000.0),
        ("(d) all stars, a rip at 30 Gyr", dict(m_min=0.08), 30.0),
        ("(d') all stars, a rip at 50 Gyr", dict(m_min=0.08), 50.0),
        ("(d'') all stars, a rip at 100 Gyr (same arithmetic as c)", dict(m_min=0.08), 100.0),
        ("(e) all stars, company helps, gamma = +1 (weight x density of inhabited planets)", dict(m_min=0.08, gamma=1.0), None),
        ("(e') all stars, company hurts, gamma = -1", dict(m_min=0.08, gamma=-1.0), None),
        ("(f) all stars, observers last 1 Gyr per planet (L_obs)", dict(m_min=0.08, L_obs=1.0), None),
        ("(g) all stars, each inhabited planet counted once at its origin (ref class 'origins')", dict(m_min=0.08, ref_class="origins"), None),
    ]
    for label, kw, cut in rows:
        w = model.weight(**kw)
        F, peak, med = read(model, w, cut)
        P("%-90s F_today %.3f  peak %8.1f  median %8.1f" % (label, F, peak, med))
    P("")
    P("Reading. Two kinds of change move the peak: a cut in time (a window or a rip; the same arithmetic at the same")
    P("time) and WHO COUNTS. Weighting every inhabited planet by how long its observers last (rows a, c) accumulates")
    P("the long-lived red-dwarf planets and puts the peak at trillions of years; counting each inhabited planet once at")
    P("its origin, or giving observers a short life per planet (rows f, g), follows the planet-formation rate and puts")
    P("the peak near 5 Gyr, with over nine tenths of the count before today. Our age is a surprise only in row (a).")
    P("So 'no interaction between planets' brings the prediction forward only if it is read as a rule for who counts")
    P("(each civilization once), which is the known lever of piece 14, not a shortening of the habitable era; a factor")
    P("that multiplies every time alike (row e) moves nothing. A rip brings it forward too, but the data (DESI DR2,")
    P("weak, w0 > -1, wa < 0) lean away from one, and under a constant dark energy galaxies and the Local Group stay")
    P("bound, so what dark energy shortens is the window, which she already has, not the habitable era.")
    out = Path("sandbox/out/when_we_are_shorteners_2026-10-18.txt")
    out.write_text("\n".join(lines) + "\n")
    print("\n".join(lines)); print("wrote", out)


if __name__ == "__main__":
    main()

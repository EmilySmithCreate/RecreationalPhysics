# The Koide form as the first member of the mass system, and the gaps it leaves

*Written 2026-10-30 on the owner's decision of that morning ("let's move forward with koide form and identify what gaps it
leaves"). The form and its arithmetic: `docs/design/twist_curl_relations_2026-10-30.md` §5, `sandbox/koide_brannen_look.py`.
Every line says whose it is. Masses are PDG values from memory, to verify. Koide's papers are read in abstract only; Brannen's
is not read (general knowledge, to verify); both are owed before any of this is cited.*

## The member adopted

*Status line, 2026-10-30:* G1 adopted by the owner the same day; the readings for G2, G5 and G6 ordered by her ("Read.", "Verify.", "complete the listed readings") and recorded below under "Readings done".

For the three charged leptons (hers, adopted; the form is published):

    √m_g = A (1 + √2 cos φ_g),   φ_g = δ + g/3 turn,   g = 0 (tau), 1 (electron), 2 (muon)

with A = 17.716 √MeV and δ = 0.222222 rad fitted on the electron and muon, the tau then predicted at 1776.97 MeV
(measured 1776.93 ± 0.09, PDG 2025; the 1776.86 ± 0.12 first written here was the older value, corrected 2026-10-30). Equivalent as a constraint, which is how the system holds it: (Σ√m)² = (3/2) Σm, plus the three
angles a third of a turn apart. In her parts: a constant part and a signed part per loop, the electron the near-cancellation
(17.72 − 17.00), a loop at 3/8 turn massless.

## The gaps, each with its test

| # | gap | what the form gives | what the system still lacks | test or kill | kind |
|---|---|---|---|---|---|
| G1 | the angle from the loop | three angles a third of a turn apart | a rule reading φ from the loop's parts; the leptons share one twist content (−⅓, −⅓, −⅓), so φ cannot come from the twists; it has to come from what differs, the runs k of R8 | *exact, no constant (ours):* φ = δ + (k + 1)/3 turn mod 1 with k = 0, 1, 2 for electron, muon, tau reproduces the ordering the fit gives (tau, electron, muon round the circle). **ADOPTED by the owner, 2026-10-30 ("Adopt.")**; what it predicts beyond the three leptons is nothing yet, since k is read from the lepton's name and not from a wiring (G9) | theory structure |
| G2 | the phase δ | 0.222222 rad = 2/9 to six digits (Brannen's observation, to verify) | why 2/9 rad; in turns it is 1/(9π), not a fraction of a turn, so it is not "thirds of thirds" of a turn | reading owed: published attempts to derive δ; then whether any count in her parts gives 2/9 rad | theory structure |
| G3 | the scale A | A² = 313.86 MeV | which part sets A; *noted, rule 13 applied, not a result:* 3A² = 941.6 MeV is 0.35 % above the proton and 0.21 % above the neutron, with measured errors a million times smaller, so it is a near miss and a known one (the "constituent quark mass" of about m_p/3; general knowledge, to verify) | a derivation of A from the nucleon that lands inside the errors, or none; count the other combinations that come as close (rule 13) | measurement |
| G4 | several loops | one loop at a time | how amplitudes combine for the nucleons and mesons; three signed lepton amplitudes added never give the nucleons (nearest 950.9 MeV, 1.3 % high) | E-B with one constant, or each quark loop with its own δ; test on proton, neutron, pion together (three masses, so at most two constants) | theory structure |
| G5 | the neutrinos | a loop at 3/8 turn is massless | three neutrinos with tiny, unequal masses (differences of order 10⁻⁸ MeV, measurement); whether they obey the same form with their own δ, and whether that δ is 3/8 turn minus a small amount | reading owed (Brannen 2006 is said to predict the three neutrino masses from this form; to verify); then the oscillation differences against the form | measurement |
| G6 | the quarks | nothing: the form is for leptons | whether quark loops obey it; published: it holds only approximately for some quark triplets (to verify) | reading owed; then the integer-style test with quark masses and their scheme errors | measurement |
| G7 | spin | absent; all three leptons spin ½ | her "spin must cancel mass somehow" is replaced, for the leptons, by the angle; whether spin enters at all is invisible until a spin-0 object (the pion) is in the system | G4's pion test | theory structure |
| G8 | what √m is | the amplitude that adds | which emergent quantity the root of mass is in her parts (the thing with a positive and a negative part); energies combine as squares in standard physics (to verify), which is the same shape | hers to name; no test until named | theory structure |
| G9 | reading from a wiring | nothing | the parts (loops, runs k, twists) read from a saved toy wiring; curl and counts read today, twist has no reading rule | the diagonals build (relations document §6, item 3) | theory structure |

## What the form does for the record

- The integer tests stand as kills of the additive one-unit form only (§3 of the relations document).
- Rule 13 count for the member adopted: 2 constants, 3 masses, 1 prediction (held). Each gap closed with a new constant
  must bring at least one new held-out mass with it, or it is a fit.
- Koide's own 1983 paper derived the relation inside a composite model of quarks and leptons (abstract only), which is the
  same family as her loops; reading it in full is the first reading owed.

## Readings done (2026-10-30; three fresh agents, from the sources; notes in `docs/reading/notes/`)

| gap | reading | verdict |
|---|---|---|
| G2, the phase | `2026-10-30_koide_originals.md`; `2026-10-30_koide_quarks_phase.md` | **NOT DERIVED.** 2/9 is within 1σ with PDG 2025 masses (δ_L = 0.2222248 ± 0.000006); Brannen found it in 2005 and calls it a coincidence; Koide calls it "an amazing coincidence ... there is no reason for the relation" and advises against taking it seriously; Żenczykowski assumes it; the one 2026 model reaching it sets a free coefficient to 1. Also: Koide exact and δ = 2/9 exact are incompatible at the 10⁻⁶ level (two tau predictions, 1776.9689 and 1776.9664, both inside the error) |
| G3, the scale | same | the pole-against-running fact: K and δ hold for pole masses (10⁻⁵) and drift by 0.2 and 0.5 % at m_Z; Koide: "a serious theoretical problem"; Sumino's family gauge symmetry is the one published repair. A rule at the deepest level has to survive down to the measured masses, not up |
| G5, the neutrinos | `2026-10-30_brannen_neutrinos.md` | **READ.** Not a massless loop at 3/8 turn: the same form with one root negative, the scale 3¹¹ smaller and the phase 1/24 turn further (δ_ν = 2/9 + π/12). Stage 1 is a two-constant fit to two splittings; stage 2 reads two integers off that fit. Against today's data the splittings sit 2 to 3σ high (inside 3σ), the sum 0.060 eV is allowed (DESI's bound 0.072 is near), and Brannen moved his own scale in 2010. Not refuted, not "dead center" |
| G6, the quarks | `2026-10-30_koide_quarks_phase.md`; `sandbox/quark_koide_look.py` | **VERIFIED as "roughly", with the number.** No quark triplet is at K = 1 within its errors; (c, b, t) is half a per cent off and whether it passes depends on which of the top mass's three definitions (10 GeV apart) is used; (s, c, b) is the farthest; the six-quark ratio crosses Koide at some scale between 2 GeV and m_Z (Kartavtsev). Phases: up near 2/27, down near 1/9 at 2 GeV (Żenczykowski's 4/27 needs m_s ≈ 160 MeV). Koide's own reason: "the gluon cloud" |
| G8, what √m is | `2026-10-30_koide_originals.md` | the published ancestor: √m is a VEV (1990) or a coupling to a heavier partner (1982), and the mass is its square; a signed quantity, which Brannen's negative neutrino root uses |

Still owed: the 1982 Lett. Nuovo Cim. text itself (paywalled; its two constraints read only through Koide's restatements);
Rosen 2007 in full; a common-scale running of the six quark masses with current inputs.

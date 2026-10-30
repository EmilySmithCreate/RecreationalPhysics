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
| G4 | several loops | one loop at a time | how amplitudes combine for the nucleons and mesons; three signed lepton amplitudes added never give the nucleons (nearest 950.9 MeV, 1.3 % high) | E-B with one constant, or each quark loop with its own δ; test on proton, neutron, pion together (three masses, so at most two constants). **Done 2026-10-30 (`sandbox/hadron_amplitude_kill.py`): amplitudes that add, one per flavour, are KILLED three ways** (pion predicted 417 MeV; antiquark negative gives 0; a linear spin term fits p, n, π with spin *adding* root-mass and then misses the Δ by 159 % and the ρ by 83 %). Open: hadrons as their own triplets (Brannen's hadron paper, unread) or a non-linear rule | theory structure |
| G5 | the neutrinos | a loop at 3/8 turn is massless | three neutrinos with tiny, unequal masses (differences of order 10⁻⁸ MeV, measurement); whether they obey the same form with their own δ, and whether that δ is 3/8 turn minus a small amount | reading owed (Brannen 2006 is said to predict the three neutrino masses from this form; to verify); then the oscillation differences against the form | measurement |
| G6 | the quarks | nothing: the form is for leptons | whether quark loops obey it; published: it holds only approximately for some quark triplets (to verify) | reading owed; then the integer-style test with quark masses and their scheme errors | measurement |
| G7 | spin | absent; all three leptons spin ½ | her "spin must cancel mass somehow" is replaced, for the leptons, by the angle; whether spin enters at all is invisible until a spin-0 object (the pion) is in the system | G4's pion test | theory structure |
| G8 | what √m is | the amplitude that adds (and, since 2026-10-30, does not add across loops) | which emergent quantity the root of mass is in her parts (the thing with a positive and a negative part); energies combine as squares in standard physics (to verify), which is the same shape | hers to name from the options below; no test until named | theory structure |
| G9 | reading from a wiring | nothing | the parts (loops, runs k, twists) read from a saved toy wiring; curl and counts read today, twist has no reading rule | the diagonals build (relations document §6, item 3) | theory structure |

## G8, the options for what root-mass is (written 2026-10-30 for the owner's decision)

What is fixed by the arithmetic before any choice: for each lepton √m = A(1 + √2 cos φ), a constant part A shared by the
three and a signed part A√2 cos φ (tau +24.44, muon −7.44, electron −17.00 √MeV) whose three values sum to zero exactly;
the leptons share one twist content, so the signed part is a function of the runs k (G1, adopted), not of the twists; and
the signed part cannot be made to add loop by loop for the hadrons (G4). The published ancestors are Koide's own: a
coupling to a heavier partner (1982), a field setting whose square is the mass (1990), and Brannen's negative root for the
lightest neutrino. The options, each with what it allows and what would test it:

| | √m is ... | sign allowed? | adds across loops? | in the toy today | what decides between it and the others |
|---|---|---|---|---|---|
| O1 | **a coupling**: how strongly the loop is tied to something heavier (Koide 1982: a coupling G to a heavy partner; the mass is G² times that partner's scale) | yes | no (a product, not a sum) | the partner is not identified; candidates: the curled column the loop sits on, a seam | needs the partner named; then A is the partner's scale and G3 closes |
| O2 | **a setting of the background**: the size of a field the loop sits in; mass its square (Koide 1990) | yes | no | the toy has no fields; its nearest is the tie strength or the curling cost per point | if the three settings must sum so that trace = traceless (the 1990 minimum), the 2/3 comes free; the 2/9 does not |
| O3 | **a signed count**: √m = u_L × (a positive count: loops, diagonals) + u_k × (a signed function of the runs k, summing to zero over a generation) | yes, when the signed part exceeds the constant | not linearly (G4) | L and n are read today; k and its sign are not | the signed function of k must be cos(δ + (k+1)/3 turn) to match; why a count of runs gives a cosine is then the question |
| O4 | **a quantum amplitude**: mass = \|amplitude\|², the amplitude carrying a phase, as in the parked wave rule (T15 rung 4) | yes, and a phase | by superposition, not by addition of squares | nothing in the toy evolves amplitudes; adopting it is the wave-rule decision held since 23 September | ties G8 to the quantum leg; Brannen's circulant matrix is literally an operator with eigenvalues √m, which fits here best |
| O5 | **a length or size**: mass grows as the square of a size (a radius, a count of links round the loop), so √m is the size | ~~no~~ **yes, by orientation** (her correction, 2026-10-30: "Why can't a size be negative? This is the 2d equation set not a plane"; an oriented loop has a signed area, and the toy's loops are oriented by their curl) | yes, if sizes add (killed for flavour amplitudes, G4) | the most toy-like: a loop's size is read from its wiring; its sign would be the curl's orientation, the open question of 29 October | ~~excludes Brannen's neutrinos~~ *withdrawn:* a negative root is a loop curled the other way, which is the neutrino's one-handedness in her terms (ours, unverified) |

~~The one fork a decision changes today: whether a root-mass can be negative.~~ *Withdrawn 2026-10-30 after her correction: every option now allows a sign.* **Her position (2026-10-30): O1, O2 and O3 all make sense, held together; O4 is adopted ("We definitely need waves in the toy", the wave-rule decision; `amplitude_rule_brief.md`, section 3, VISION addendum of this date); O5 stands with its sign from orientation.** What separates the options now is what the constant part A is: a partner's scale (O1), a background (O2), a count (O3), an operator's eigenvalue scale (O4), a size (O5); the first test that could tell them apart is reading A from a wiring (G9).

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

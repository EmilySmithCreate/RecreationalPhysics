# Brief for a fresh reader: the record of 28 October 2026, evening (the unit, the spectrum, T84, T85, the coil, the master equation)

*Written 29 October 2026 for a reviewer who starts with no history of this work (CLAUDE.md rules 12 and 22). The owner,
Emily Smith, will start the session and pass this page to you. You are meant to be a different model from the one that
wrote the record (Claude); Codex is the intended reader. Six earlier briefs covered the record to the afternoon of
28 October; the sixth's report is `docs/reviews/2026-10-28_codex_report.md`, recorded as ASSUMPTIONS O166, and the record
from that point on has had no audit. Read the earlier reports if you like, but write your own findings first. Part A is
to be done blind: it names what not to read until it is finished.*

## Who you are and what you may do

A fresh, skeptical reader of a hobbyist physics research programme. **Work read-only:** edit, commit and push nothing.
You may run scripts and tests; sandbox scripts print to the terminal; run nothing that writes to `results/`. Return your
report as your final message in Markdown; the owner saves it as `docs/reviews/2026-10-29_codex_report.md` and the next
working session records it as an ASSUMPTIONS O entry with what you found and what you got wrong.

**Repository:** `https://github.com/EmilySmithCreate/RecreationalPhysics`, branch `claude/particle-sector-2026-10-24`, at
the commit this brief is committed in (`git log -1 -- docs/reviews/2026-10-29_codex_audit_brief.md`); read nothing later.

**Setup:** Python 3.10+, `pip install -e ".[dev]"`, `PYTHONPATH=src:scripts` (Windows `"src;scripts"`).
`tests/test_lengths.py` and `tests/test_diagonals.py` take under a minute. Costs: `scripts/t84_landscape.py 16 -0.5 20268401`
about a minute (do not write to `results/`: pass a fourth argument, an output directory of your own, or read the committed
files); `scripts/t85_gamma.py 16 20268501` a few minutes (same caution); `sandbox/t85_drift_cause.py 24` a few minutes;
`sandbox/coil_writhe.py 1 2 3 4` seconds; `sandbox/proton_loop_fold.py 3 4 5` five minutes; `sandbox/warm_space_window_d.py 8`
five minutes.

**Read first:** `CLAUDE.md` (rules 1, 4 to 7, 10 to 15) and the top of `VISION.md` (the hypothesis, claims 1 to 6, the bar).

## The master equation, as the record now states it (for your checking, not your belief)

Every run uses one energy, terms switched on as needed; what follows is the record's own summary, and your first job is
to say whether it is one consistent model or several (`docs/design/diagonals_brief_2026-10-28.md`,
`docs/design/gravity_link_brief.md`, `docs/design/twist_curl_rules_2026-10-27.md`, VISION Updates 135 to 143):

    E = 16(3N − S) + 4X                       the published curvature (six links); terms 1, 2
      + 4(λ − 1) X                            the curling cost, ours; term 3
      + ½ δᵀ K δ + α Σ_e |c_e| δ_e            lengths on the cube edges: K = 4(6I − A) per axis family (exact), c_e = S_e − 4,
                                              Σ_e δ_e = 0 on each family (her scale rule: the total length fixed near matter)
      body diagonals: ℓ = √(ℓx² + ℓy² + ℓz²)  derived from each cube's edges, no constant (her decision; light moves on them,
                                              one tick per unit of length)
      twist on a diagonal only where there is curl ("no curl, no twist, nothing"), in thirds on box diagonals and halves on
      face diagonals, signed by the diagonal's colour; a loop's total whole; charge = twist + photons held; spin from the
      twist alone; mass = 0.170 MeV per looped diagonal (the electron, three white thirds, is the unit, 0.511 MeV)
      + ε Σ_d |h_d|                           photons held
      growth: a double row added to every empty ring at a fixed chance per sweep, never removed (the clock; not built)

## Part A, blind: six questions

Do this part **before** reading ASSUMPTIONS O167 and O168, VISION Updates 139 to 143 and their addenda, PREREGISTRATION T84's
"Reading" and Amendment 2, T85's Amendment 1 and "Reading", `sandbox/LOG.md` entries dated 28 October after 15:00 UTC, and
`sandbox/NOTEBOOK.md` after 19:00 UTC. Say in your report whether you kept to it.

1. **The spectrum.** From the rules in the master equation and one exact fact you can verify in a minute (every step
   (±1, ±1, ±2) changes x + y + z by an even number, so a closed loop of box diagonals is one colour), derive what charged
   particles the rules allow and at what masses, before reading the record's statement of it. Then say which single rule
   would be needed to leave a gap between the electron and the muon (105.7 MeV = 621 looped diagonals), and whether the
   three candidates the record names (a minimum coil size; fold must be whole; only the pyramid is stable small) survive:
   `sandbox/coil_writhe.py` gives the smallest closed coils' fold; `sandbox/proton_loop_fold.py 5` gives the five-diagonal
   loops, 48 of which have |writhe| = 1.000 to three decimals (verify this; is it exact, and why?).
2. **T85's definition.** Read PREREGISTRATION T85 as registered. The quantity α* = α·D/(2P) compares a light delay D on the
   *fastest* path with a potential integral P on the *straight* line. Before reading the record's reading: is that a
   consistent test of Einstein's γ, what should it do as the impact parameter grows, and what is the right form? Then run
   `sandbox/t85_drift_cause.py 24` and say whether its "straight" path is a fair straight line on this lattice.
3. **Is γ even the right target?** The toy has no clocks. In Einstein's weak field the Shapiro delay is (1 + γ)·(a path
   integral of the potential) and the Newtonian pull is a *time* effect. Say what, if anything, in this family plays the
   role of the time part of the metric, and whether a length-only model can have a γ at all, or only a light-bending
   analogue. Cite the weak-field formulas you use.
4. **The unit and the ring.** The electron is three looped diagonals at 0.511 MeV, so the proton is 5,508 and, the record
   argues, must be an open ring 2,800 to 4,300 links across to be 0.84 fm if the electron sits under 10⁻¹⁸ m. Check the
   arithmetic, then say which bound on the electron's size applies to a loop of twist (scattering limits against the
   moment-based figure), with sources, and what the proton's measured form factor says about a ring.
5. **Mass as a count.** "Mass counts looped diagonals, 0.170 MeV each" makes a particle's mass proportional to its length.
   Name the cheapest measured fact that this contradicts or supports (the lepton masses; the proton's size against its
   mass; the pion's), and say whether binding energy has any place in the rules.
6. **Twist only with curl.** The owner's statement of 29 October: a diagonal has twist only where it has curl, "no curl, no
   twist, nothing, 0 degrees of freedom". On the flat six-link torus every square's curl is zero, so twist can live only at
   defects of the wiring. Say what that implies for the electron (three looped diagonals) as an object of the toy: what
   wiring defect would carry exactly three box diagonals with curl, and does one exist among the one- and two-switch
   objects of `scripts/exact_relic_search_d.py` (O58)?

## Part B: the record's answers, and the rules

Now read everything. For each Part A answer say whether the record agrees and, where not, which is right. Then:

7. **Rule 10.** List every physical conclusion stated on 28 October after 15:00 UTC and check its kind (exact, measured,
   interpretation, the author's) and that none moved kinds without a dated line; in particular the sentences around
   "reach emerges", the γ "prediction with no free constant", and the ring.
8. **Rule 14.** T84 and T85 each name a held-out size whose numbers were written from the smaller sizes and held. Could
   either prediction have failed, given what was already known from the smaller sizes? Which held-out claim was a size
   claim and which an arithmetic identity?
9. **Rule 11.** T85 failed the owner's prediction; the record's cheapest discriminating calculation was the straight-path
   recomputation. Was it the cheapest, was it done before or after the held-out run, and does its conclusion ("the drift
   across b was the test's definition") follow for the lopsided knot too?
10. **The owner's words.** Three attributions to check against `sandbox/NOTEBOOK.md`: "mass counts looped diagonals",
    "gravity travels through the cube edges and light through the body diagonal links", and "no curl, no twist". For each,
    is the record's rule what she wrote, or the assistant's reading of it?
11. **What is missing.** The cheapest calculation or known result most likely to show that the master equation above
    cannot describe our universe. Name it and, if it takes under an hour, do it.

## Report

Findings first, ranked by how much they would change the record if right, each with file and line, what the record says,
what you find, how you checked. Then what you could not check. Then a one-paragraph verdict. Do not summarise the record.

# Brief for a fresh reader: the record of 28 October 2026 (the loop rules for particles, gravity carried on the links, T83, and the exact claims behind them)

*Written 28 October 2026 for a reviewer who starts with no history of this work (CLAUDE.md rules 12 and 22). The owner,
Emily Smith, will start the session and pass this page to you. You are meant to be a different model from the one that
wrote the record (Claude); Codex is the intended reader. Five earlier briefs covered the record up to 27 October; their
reports are in `docs/reviews/`, the latest recorded as ASSUMPTIONS O163. You may read them, but write your own findings
first. This brief has two parts, and the first is to be done blind: it names what not to read until it is finished.*

## Who you are and what you may do

You are a fresh, skeptical reader of a hobbyist physics research programme. You have not seen the conversations that
produced its record. **Work read-only:** do not edit, commit or push anything in the repository. You may run the
repository's scripts and tests. Sandbox scripts print to the terminal or write under `sandbox/out/` (untracked); do not
run anything that writes to `results/`. Return your report as your final message, in Markdown; the owner will save it as
`docs/reviews/2026-10-28_codex_report.md`, and the next working session will record it as an ASSUMPTIONS O entry
(rule 12), with what you found and what you got wrong.

**Repository:** `https://github.com/EmilySmithCreate/RecreationalPhysics`, branch `claude/particle-sector-2026-10-24`,
at the commit this brief is committed in (the commit's own hash is in `git log -1 -- docs/reviews/2026-10-28_codex_audit_brief.md`);
read nothing from later commits. Everything dated 28 October has had no audit.

**Setup:** Python 3.10+, `pip install -e ".[dev]"`, then run with `PYTHONPATH=src:scripts` (on Windows `"src;scripts"`).
`tests/test_lengths.py` takes about ten seconds; the full suite about fifteen minutes and you do not need it. Running
costs: `sandbox/regge_step1_stiffness.py 6` about two minutes, `_b.py 6` about ten, `8` and `10` longer;
`sandbox/relaxed_lengths_pull.py` under a minute; `sandbox/gravity_carrier_isotropy.py` under a minute;
`sandbox/pyramid_check.py` and `sandbox/t83_defect_footprint.py` seconds; `sandbox/proton_loop_fold.py 3 4 5` about
five minutes, length 6 about an hour. T83's stage-1 run took about ten minutes on a laptop and its result is in
`results/t83_curl_corr_stage1.csv`; do not rerun it into `results/`.

**Read first:** `CLAUDE.md` (the rules; especially 1, 4 to 7, 10 to 15) and the top of `VISION.md` (the hypothesis,
claims 1 to 6, and the bar).

## Part A, blind: five questions, each to be answered from the sources before reading the record's own answer

Do this part **before** reading VISION Update 136 and its addenda, ASSUMPTIONS O165, PREREGISTRATION T83's "Read"
paragraph and T84, `docs/design/gravity_link_brief.md` from its section 4 result onward, and the LOG lines of 28 October
in `sandbox/LOG.md`. Write your answers down, then go on to Part B. The blindness is by instruction, not by a pin; say in
your report whether you kept to it.

What you may read for Part A: `VISION.md` up to and including Update 135; `docs/design/twist_curl_rules_2026-10-27.md`;
`docs/design/gravity_link_brief.md` sections 1 to 3 and 5 to 7; PREREGISTRATION T83 up to its "Disclosure" paragraph;
the scripts named below (their headers state predictions written before they ran; that is allowed); `src/graphity/lengths.py`
and `tests/test_lengths.py`; `src/graphity/correlation.py`; `results/t83_curl_corr_stage1.csv` and `_curves/`; the git
history of all of these.

1. **Is the stiffness claim right, and is it the published curvature?** `sandbox/regge_step1_stiffness.py` takes the
   curvature of [T25] Sec. II.2 (uniform measure on the sphere of neighbours, transport cost by shortest paths,
   κ = 1 − W/d) over link lengths on the flat six-link torus and perturbs lengths. Before running it, derive by hand
   what the first- and second-order change in H = −4D Σ κ should be for one lengthened link and for two parallel links
   one step apart, under that definition. Then run it at L = 6 and compare. Say whether the definition in the script is
   the paper's (check Sec. II.2 and Eq. (8) of arXiv:2512.17676 yourself; the hand check at S = 0, 1, 2 in two
   dimensions is in the script's header), whether H should carry a factor of the edge length (as Regge's action does)
   and what that would change, and whether a quadratic form found by finite differences at δ = ±0.01 to ±0.2 can be
   trusted when the transport cost is a linear programme (piecewise linear in the lengths).
2. **Does a gapless stiffness give a pull?** `src/graphity/lengths.py` claims E_relax = −(α²/2)|c|ᵀK⁺|c| and so an
   attraction between any two relics for either sign of α. Check the algebra, the handling of the zero mode on a torus
   (what the mean-removal does to a pair's energy at separation L/2), and whether `sandbox/relaxed_lengths_pull.py`'s
   "ratio to two point sources" is a fair test of Newton's shape on a 16³ torus. Then say what, physically, a length
   that relaxes instantly to its minimum means for the chain (is the pull a force, or a change of the energy landscape
   the walls may still forbid?).
3. **T83's scoring.** Read PREREGISTRATION T83 as registered and `results/t83_curl_corr_stage1.csv`. Score it by its
   own words. Then ask what the quantity C(r) of `graphity.correlation` measures on a sheet that is 99 % flat with a
   handful of defects, and compute, your own way, what one isolated defect contributes to C(3). Say whether the
   registered words could ever have returned SHORT on a surviving sheet at these sizes.
4. **The loop rules for particles** (`docs/design/twist_curl_rules_2026-10-27.md`; the sheet
   `https://claude.ai/artifact/T2318KjX32xDrHep2fRowD`, which the owner will share if you ask). Take the rules as
   written (loop total = twist + fold is whole; spin angle = ½ × net twist angle; mass = |twist| + |fold|; sign by
   colour; the pyramid) and look for an internal contradiction or a conflict with a published fact, the cheapest first.
   Three places to start: whether "spin = ½ × net twist" survives for the neutron, the pion and the photon; whether
   the Möbius form (linking = twist + 2·fold, odd) is Denne and Larsen's statement or a reading of it; and whether
   `sandbox/proton_loop_fold.py`'s writhe is the right quantity for a lattice polygon (it uses the Gauss integral on
   straight segments; check one loop by hand or by another method).
5. **The isotropy argument.** `sandbox/gravity_carrier_isotropy.py` compares three carriers by the potential of one
   source along the axis and the diagonals. Say whether its three definitions are the only reasonable ones, whether
   the point-scalar rows at r = 16 and 24 are box effects as claimed, and what measured bound on the direction
   dependence of gravity (or of the speed of light) the record should cite instead of "far better than 8 %".

## Part B: the record's own answers, and what they got wrong

Now read VISION Update 136 and its addenda, ASSUMPTIONS O165, PREREGISTRATION T83's "Read" and T84, the rest of the
gravity link brief, and the 28 October LOG lines. For each of your Part A answers, say whether the record agrees, and
where it does not, which is right. Then:

6. **Rule 10.** List every sentence written on 28 October that states a physical conclusion ("reach emerges", "a pull of
   Newton's shape", "flat space is a minimum in the lengths") and check that each is labelled exact, measured,
   interpretation or the author's, and that nothing moved between kinds without a dated line.
7. **Rule 11.** T83's reading gives four answers for the owner's failed prediction. Are they the four the rule asks,
   and is "the scoring gate was the assistant's error" a complete account, or does it hide that the question itself
   (curl felt through flat sheet) may have no equilibrium state to be asked in?
8. **Rule 14.** Step 1's held-out size (L = 10) was predicted to repeat L = 6 and 8 to every digit, and did. Was that a
   size claim that could have failed, given that the coupling was already seen to have range one at L = 6?
9. **The owner's words.** `sandbox/NOTEBOOK.md` records her messages verbatim with a Fable line after each. Pick three
   decisions attributed to her on 28 October (the tie's sign, "step 2 runs uncoupled", "adjust my prediction") and
   check that the record's statement of each is what she wrote, not a reading of it; where the assistant adjusted her
   prediction at her instruction, say whether the adjustment went beyond what she asked.
10. **What is missing.** The cheapest calculation, known result, limit or symmetry argument most likely to show that the
    link-length gravity of Update 136 cannot be the gravity we measure. Name it and, if it takes under an hour, do it.

## Report

Findings first, ranked by how much they would change the record if right; for each, the file and line, what the record
says, what you find, and how you checked. Then what you could not check. Then a one-paragraph verdict on the day. Do
not summarise the record back; the owner has it.

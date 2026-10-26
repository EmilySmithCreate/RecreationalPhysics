# Brief for a fresh reader: the record of 25 to 26 October 2026 (the twin X, the pair tie, the push, anticurl, the hard rule)

*Written 26 October 2026 for a reviewer who starts with no history of this work (CLAUDE.md rules 12 and 22). The owner,
Emily Smith, will start the session and pass this page to you. You are meant to be a different model from the one that
wrote the record (Claude); Codex is the intended reader. Two earlier briefs covered the record up to VISION Update 120;
their reports are in `docs/reviews/`, and the second is recorded as ASSUMPTIONS O158. You may read them, but write your
own findings first.*

## Who you are and what you may do

You are a fresh, skeptical reader of a hobbyist physics research programme. You have not seen the conversations that
produced its record. **Work read-only:** do not edit, commit or push anything in the repository. You may run the
repository's scripts and tests. The sandbox scripts write only to `sandbox/out/`, which is not tracked, so you will have
to regenerate any output you want to check. Do not run anything that writes to `results/`. Return your report as your
final message, in Markdown; the owner will save it as `docs/reviews/2026-10-26_codex_report.md`, and the next working
session will record it as an ASSUMPTIONS entry (rule 12).

**Repository:** `https://github.com/EmilySmithCreate/RecreationalPhysics`, branch `claude/particle-sector-2026-10-24`,
**at commit `29afa5c9`** (full `29afa5c9d53dab428a9e20fcfcaa8fa4c7932eca`). This brief is committed just after it; read
nothing else from later commits. No in-session audit of this material exists yet, so nothing in the commit is already
corrected for you.

**Setup:** Python 3.10+, `pip install -e ".[dev]"`, then run scripts with `PYTHONPATH=src`. The tests that cover the code
used here (`tests/test_cqg_d.py`, `test_dimension.py`, `test_sealed_d.py`, `test_sealed_local.py`, `test_sealed_tie_d.py`,
`test_exact_walls_tie_d.py`) take a few minutes; the full suite takes about half an hour and you do not need it.
Running costs: the exact looks (`pair_tie_patch_look.py`, `hard_rule_moves_look.py`, `hard_rule_pairs_look.py 1`) take
seconds to a minute each. The bath look takes hours, so inspect it and run a shortened copy if you want a check. The
push look (`sandbox/pair_tie_push_look.py`) is 25 cells of about 10 minutes each, run 12 at a time.
`sandbox/breakage_anticurl_look.py` reads the push look's saved end states, so it needs the push look (or some cells
of it) first.

**Read first:** `CLAUDE.md` (the rules; especially 1, 4 to 7, 10 to 16 and 19 to 22) and the top of `VISION.md` (the
hypothesis, claims 1 to 6, and the bar).

## The question

From 25 to 26 October the owner changed what X, the curled state that opens into space, is meant to be in the toy:
two curled directions that open together as twins, opposite in handedness. She asked for a "tie" in the energy so that
curling two directions costs the same as curling one. The assistant then:

- recorded her decisions (VISION Updates 122 to 125, 127 and 128);
- withdrew a registered test at her word (T82);
- computed exact single-move walls and opened-patch energies under the tie;
- ran three sandbox looks on a six-link rod (a warm bath, a concentrated push, a reading of where the anticurl sits);
- looked exactly at what her "hard rule" (curl minus anticurl held at zero) allows with the toy's move;
- recorded the second Codex audit (O158, Update 126), with corrections in place and a check of T71's results files.

The headline readings: no push opened both directions cleanly; where opening happened, a fifth to a third of points
broke; broken points carry the anticurl; and under the hard rule clean space cannot move at all.

**Your job: find what is wrong.** Assume there are errors in the code, the physics, the arithmetic, the attribution of
ideas, the labelling of statements (rule 10: exact, measured, interpretation, hers), the sandbox discipline (rule 16:
a look can kill a claim but never crown it; its words are declared before it runs) and the process, and look for them.
A clean bill is a possible answer, but it should be earned.

## What to read

1. `VISION.md`, **Updates 122 to 128**; Update 126 is the record of the last audit (check it against
   `docs/reviews/2026-10-25b_codex_report.md` and ASSUMPTIONS **O158**). Also the in-place corrections marked "O158" in
   Updates 113, 118 and 120.
2. `sandbox/NOTEBOOK.md`, entries dated 2026-10-25 from "A rod between 2 curled slabs" on, and 2026-10-26: her words,
   verbatim.
3. `docs/design/owner_questions_2026-10-24.md`, the read-backs T1a to T1e and their answers.
4. `sandbox/LOG.md`, the lines dated 2026-10-25 from "pair tie walls" on, and 2026-10-26.
5. The sandbox looks: `sandbox/pair_tie_patch_look.py`, `pair_tie_bath_look.py`, `pair_tie_push_look.py`,
   `breakage_anticurl_look.py`, `hard_rule_moves_look.py`, `hard_rule_pairs_look.py`; and the walls script they build on,
   `scripts/exact_walls_tie_shape_d.py` (run with `--f=0,0,a,0`), with T54's `scripts/exact_t54_patch.py`.
6. The code the looks run on:
   - `src/graphity/cqg_d.py` (the six-link model, its energy H = 16(3N − S) + 4λX and its switch move);
   - `src/graphity/dimension.py` (`local_dimension_d`: the number of open directions d at a point; a point with
     d > 3 is called "broken");
   - `src/graphity/sealed_d.py` and `src/graphity/sealed_tie_d.py` (sealed runs with energy stores, and the tie table
     ftab[d]; note `table_total`, where a d beyond the table costs 0);
   - `scripts/run_sealed_curled_d.py` (the push look's runner: `local_heat`, `ftable_per_a`) and
     `scripts/run_curled_bath_tie_d.py` (the bath look's runner).
7. The assumptions behind them: ASSUMPTIONS **Q21** (the six-link energy), **Q22** (the local spark), **O41**, **O106**
   (the tie's walls), **O115** (a tied slab breaking in a bath, and the broken point's zero cost), **O158**; VISION
   **Update 105** (the hard rule, its two forms, the definitions of curl and anticurl).
8. For the T71 check in O158: `PREREGISTRATION.md` section T71, `scripts/analyse_t71.py`, `results/t71_*.csv`. The
   per-birth numbers in O158 came from a scratch script that is not in the repository; recompute them from the CSVs
   (the rise in `daughter_energy` at each logged birth, against a N_slab = 4(λ − 1) N_slab).

## What to check

Write each finding with where it is, what is wrong, what is right, how you know (a computation you ran, a source, an
argument), and how sure you are. Cover at least:

1. **The pair tie and its walls.** Is f = (0, 0, a, 0) per point what Update 124 says she asked for ("curling two costs
   the same as curling one", "each direction carries its own cost", "half the curl energy each")? Are the rod and slab
   both 2a per point above flat under it, and is the release at each opening as stated (nothing at the first, 2a per
   point at the second)? Are the single-move walls and the patch energies right, and does the reading "the second barrier
   is below the first" follow from two different patch shapes, neither shown to be the cheapest path? What does it mean
   that a broken point (d > 3) costs 0 in the table?
2. **The sandbox looks as looks.** For the bath and push looks: were the words (BOTH OPEN, FIRST ONLY, STAYS, BREAKS)
   declared before the runs, are they applied as written by the `--read` functions, and are the readings in the LOG
   and in Updates 124 and 125 faithful to the outputs? The push look ran a short smoke test before the full run; does
   that affect anything? Are the tied and untied cells comparable (their seeds differ)? Does "where the tied rod
   opened, 41 to 71 % of opened points reached d = 3, against about a third untied" compare like with like? Is energy
   conserved in the runs (the `drift` column)?
3. **Anticurl and breakage (Update 127).**
   - Check the identity H = 4 × anticurl + 4(λ − 1) × curl, with curl = Σ_e (S_e − 4)₊ and
     anticurl = Σ_e (4 − S_e)₊ over links.
   - Check that the anticurl sits on links touching broken points, and the comparison of curl near broken points
     against the share of links there (is that baseline the right one?).
   - Check the reading that the most broken runs end near curl minus anticurl = 0, and whether "breakage is opening
     past flat" is a fair reading of d > 3.
   - Check the claim that every rod look so far ran an X that her own hard rule forbids.
4. **The hard rule looks (Update 128).**
   - Is the single-switch enumeration complete? It fixes u1 at point 0 and relies on the tori being vertex-transitive;
     check that the rod 4 × 4 × 18 and the flat 6 × 6 × 8 are, for both sides of the bipartition, under this move.
   - Is the pair search correct and complete for what it claims (second switch within 1 or 2 links, both graphs on the
     way obeying the hard-core rule, the undo excluded)?
   - Note that every restoring pair found was the space put back; is the undo exclusion in `second_moves` wrong, and
     does it matter for the conclusion?
   - Does "clean space is frozen under the hard rule with the published move" follow, and is "not shown beyond two
     switches" stated clearly enough?
   - Is the soft form μ(S − 3N)² fairly described as "like the hard rule with excursions of any length"?
5. **Her words against our readings.** Any reading of the assistant's presented as her decision; any decision
   recorded that she did not make; any of her words misquoted or dropped; any assistant conclusion listed among her
   answers. In particular:
   - the pair tie's form, marked "to confirm" in Update 124;
   - the inferred BOTH OPEN for the push look;
   - her "proceed" of 26 October, read as taking up the assistant's suggestion;
   - her two questions in Update 127, from a message cut off by an interrupt.
6. **The O158 record.**
   - Does ASSUMPTIONS O158 report the second Codex audit fairly, including what it got wrong?
   - Are the in-place corrections right? Three to check: (a) an antimatter-rich twin obeys the same laws; (b) CP
     violation only makes the histories not exact mirrors; (c) Boyle, Finn and Turok's branches lie before and after
     one Big Bang.
   - Was leaving the layer code's affordability guard unfixed until T71's and T74's held-out stages are read the right
     call?
   - Are the nine new `REFERENCES.bib` entries correct?
7. **Physics from memory.** Each was stated in Updates 122 to 128. Check each is stated correctly and marked "general
   knowledge, to verify" where it was not read:
   - Hawking radiation and a black hole's ringdown;
   - virtual pairs (the Lamb shift, the Casimir force) and Tryon's 1973 universe from a vacuum fluctuation;
   - magnetic dipoles and monopoles (Dirac 1931; 't Hooft and Polyakov 1974; DeGrand and Toussaint 1980 on monopoles
     in compact lattice electromagnetism);
   - the neutron as a neutral particle with a magnetic moment.
8. **Internal consistency.**
   - Contradictions between Updates 122 to 128, the questions file, the notebook and earlier decisions still standing.
     For example: the tie was withdrawn on 16 October and returns here; the hard rule was decided on 25 October but no
     rod look obeys it; Update 122's "half the curl energy each" against Update 120's "each twin carries the full
     curling cost".
   - Whether the push look's protocol (sealed, energy released where it is released) fits claim 6 as written.

## What to return

A single Markdown report, in plain American English (the owner is a software engineer, not a physicist; define terms):

1. **Summary** (ten lines at most): the most important things to fix, in order.
2. **Findings**, numbered, under the eight headings above, each with where, what, what is right, how you know, and how
   sure you are.
3. **What you ran:** each script or test, with its output where it disagrees with the record.
4. **Missing published work:** the published models, theorems or measurements most relevant here, with authors and
   years, "to verify" where unsure. Topics: constrained Monte Carlo moves that preserve a global count (and what is
   known about their ergodicity); paired curvature defects (disclinations and dislocations) on lattices; universes in
   pairs or from black holes; monopoles on lattices. Her stated aim is to apply existing mathematics to her ideas, so a
   good match is welcome news.

Do not write "nobody has done X"; write "I did not find X" and say where you looked. Mark anything you did not check at
its source as such.

## What not to do

Do not propose new mechanisms for her hypothesis and do not rewrite her ideas; judge what was recorded, computed,
coded, run and answered. Do not read commits after the one named above (this brief excepted). Do not change any file.

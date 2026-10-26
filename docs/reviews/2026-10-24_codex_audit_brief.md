# Brief for a fresh reader: the record of 24 October 2026 (the particle handoff and the photon field)

*Written 24 October 2026 for a reviewer who starts with no history of this work (CLAUDE.md rules 12 and 22). The owner,
Emily Smith, will start the session and pass this page to you. You are meant to be a different model from the one that
wrote the record (Claude); Codex is the intended reader.*

## Who you are and what you may do

You are a fresh, skeptical reader of a hobbyist physics research programme. You have not seen the conversations that
produced its record. **Work read-only:** do not edit, commit or push anything in the repository. You may run the
repository's scripts and tests (they write only to `sandbox/out/`, which is not tracked, or to your own scratch folder);
do not run anything that writes to `results/`. Return your report as your final message, in Markdown; the owner will
save it as `docs/reviews/2026-10-24_codex_report.md`, and the next working session will record it as an ASSUMPTIONS
entry (rule 12).

**Repository:** `https://github.com/EmilySmithCreate/RecreationalPhysics`, branch `claude/particle-sector-2026-10-24`,
**at commit `39466620`**. Check out that commit and read nothing from later commits: a separate in-session audit of the
same day may land after it, and you are meant to be blind to it.

**Setup:** Python 3.10+, `pip install -e ".[dev]"`, then `pytest tests/test_u1.py` (about ten seconds) to check the new
module runs. The full suite takes about half an hour; you do not need it.

**Read first:** `CLAUDE.md` (the rules; especially 1, 2, 5, 7, 10, 12 to 16 and 19 to 22) and the top of `VISION.md`
(the hypothesis, claims 1 to 6, and the bar). You do not need the rest of the history.

## The question

On 24 October 2026 the owner brought a handoff for a particle sector of her hypothesis (kept as received at
`docs/geometric_particle_model_handoff_2026-10-24.md`; her own ideas are its section 1). Over the day she answered
several rounds of questions; the assistant ran a series of exact "looks", built a compact U(1) lattice gauge field on
the toy's graphs with tests and a reproduction gate (run three times), recorded six VISION updates (96 to 101), and ran
two automated multi-agent passes of its own (a slot-by-slot check of a worksheet, and a publishability red team).

**Your job: find what is wrong.** Assume there are errors in the physics, the code, the statistics, the attribution of
ideas, and the process, and look for them. A clean bill is a possible answer, but it should be earned.

## What to read

In this order:

1. `docs/geometric_particle_model_handoff_2026-10-24.md` (what she brought).
2. `VISION.md`, **Updates 96 to 101** (at the end of the file). These record her decisions, in her words, and the
   assistant's checks.
3. `docs/design/particle_handoff_brief_2026-10-24.md` (her comments are kept in it between `#` marks, as she wrote
   them), `docs/design/u1_rewiring_graph_brief_2026-10-24.md`, `docs/design/owner_questions_2026-10-24.md`, and the two
   addenda at the end of `docs/design/loop_rule_worksheet_2026-10-23.md`.
4. `ASSUMPTIONS.md`: **Q29** (the field), **O151** (light in a curled direction, with its same-night correction) and
   **O152** (the red-team pass).
5. `TASKS.md`, the section "24 October: the owner's particle handoff" (Gates U1, U1′ and U1″, each with its acceptance
   and its reading).
6. `src/graphity/u1.py`, `tests/test_u1.py`, `scripts/run_u1_gate.py`, the three gate configs
   `configs/gate_u1_2d.json`, `configs/gate_u1b_2d_winding.json`, `configs/gate_u1c_2d_winding_long.json`, and their
   results in `results/gate_u1*`.
7. `sandbox/NOTEBOOK.md` and `sandbox/LOG.md`, the entries dated 2026-10-24, and the sandbox scripts they cite
   (`sandbox/particle_handoff_looks.py`, `u1_gate_topology.py`, `u1_gate_autocorr.py`, `strand_answers_look.py`,
   `diagonal_112_look.py`, `strip_corner_and_ring_energy.py`, `light_in_curled_space.py`, `u1_curl_mass_general.py`,
   `u1_graph_free_energy.py`). Each runs in seconds to minutes; run any you doubt.
8. `docs/reading/notes/2026-10-24_prior_work_u1_curl_mass.md` (a rule-15 note).

## What to check

Write each finding with where it is, what is wrong, what is right, how you know (a computation you ran, a source, an
argument), and how sure you are. Cover at least:

1. **The field's code.** Does `graphity.u1` implement compact U(1) correctly on these graphs (link orientation by kind,
   the sign of each link in a square's holonomy, Gauss's law, the force used in the evolution)? Is the Metropolis
   update detailed-balanced as its docstring argues? Is the winding move (`Field.instanton` with
   `metropolis(..., instanton=...)`) a valid move: symmetric, detailed-balanced, and does it change the winding by one?
   Can any test in `tests/test_u1.py` fail only in ways that do not matter, or not fail at all?
2. **The exact answer used as the gate.** Is `exact_mean_cos_2d` (the character expansion on a closed two-direction
   torus) correct, including the role of the alternating square signs?
3. **The gate sequence.** U1 failed; a diagnosis and a fix followed; U1′ failed by one point; a diagnostic followed;
   U1″ (four times the sweeps, same acceptance) passed. Was each acceptance written before its run (check the commit
   order)? Is passing on the third run, after two failures, sound by rule 2, or is it a gate tried until it passed? Is
   the "eight of ten points read high" remark in U1″'s reading a warning sign the reading underplays?
4. **O151 and its correction.** Is the corrected statement right: that on a side-4 curled direction the field component
   along the curl is a massive Wilson-line scalar with ω² = 4 + K², while light in the open directions keeps the flat
   speed, and that the mass exists only because every 4-cycle is counted as a square? Is the general formula pinned by
   `test_bloch_formula_with_side_four_rings_gives_the_whole_spectrum` correct?
5. **The exact looks.** Re-run them. Do the printed numbers hold (ring counts, angles, rotation orders, the 3Q + t table,
   the 1 × 1 × 2 counts, ring bending energies, the leading-order field reward)? Is anything printed as a conclusion that
   the code does not compute?
6. **The light-lowers-the-curling-cost claim.** Is the leading-order reward ln I₀(β) per square right, and is the
   effective-curling-cost formula λ_eff − 1 = (λ − 1) − (g/16) ln I₀(β) correctly derived (units, the 1/16, the tube's
   extra quarter square per point)? Is the statement that every correction term is positive (so the leading order
   underestimates the effect) right?
7. **Her words against our readings.** Using her comments in the particle brief, the notebook entries and the VISION
   updates, find any place where a reading of the assistant's is presented as her decision, a decision is recorded that
   she did not make, or her words are misquoted (rules 10, 20). Find any idea or question of hers from the day that
   reached neither VISION nor the notebook (rule 21).
8. **Kinds of statement.** Any physics written from memory and not marked "general knowledge, to verify" (rule 19); any
   sandbox look used to support a claim (rule 16); any "we have not found" without a note (rule 15); any first look
   described as a finding (rule 7).
9. **The prior-work note.** Is its verdict (PARTLY FOUND) fair? Did it miss the closest published work on a gauge field
   whose action includes the loop round a short compact direction, or on gauge fields on emergent or random graphs?
   Check that each cited arXiv number exists and says what is claimed.
10. **The particle definitions as they now stand** (Updates 97 to 101: thirds on body diagonals, halves on face
    diagonals, charge as net signed thirds, antiparticle as the mirror image). Without proposing a model of your own:
    are they consistent with each other and with the exact facts in the record? Which observed facts do they already
    contradict?

## What to return

A single Markdown report, in plain American English (the owner is a software engineer, not a physicist; define terms),
with these sections:

1. **Summary** (ten lines at most): the most important things to fix, in order.
2. **Findings**, numbered, under the ten headings above, each with where, what, what is right, how you know, and how
   sure you are.
3. **What you ran:** each script or test, with its output where it disagrees with the record.
4. **Missing published work:** the published models, theorems or measurements most relevant to the day's work that the
   record does not cite, with authors and years, "to verify" where unsure. Her stated aim is to apply existing
   mathematics to her ideas, so a good match is welcome news.

Do not write "nobody has done X"; write "I did not find X" and say where you looked. Mark anything you did not check at
its source as such.

## What not to do

Do not propose new mechanisms for her hypothesis and do not rewrite her ideas; judge what was recorded, computed and
answered. Do not read commits after `39466620`. Do not change any file.

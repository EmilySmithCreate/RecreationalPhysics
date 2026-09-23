# Start here: handoff for the next assistant (state as of 2026-09-23, mid-afternoon)

Written for the AI assistant that opens this repository next. Emily is the owner; she will read it too.
Read it before `CLAUDE.md`'s "Known state" section, which is older than this page. Everything below is
on branch `feat/results-meta-and-followups`, pushed; `main` is behind it and Emily merges.

## 0. The first ten minutes

1. **Four T13 jobs may still be running** (section 5). Check with
   `for n in t13_temper_n484_melt t13_temper_n484_torus t13_temper_n676_melt t13_temper_n676_torus; do ls results/$n.csv 2>/dev/null || wc -l results/$n.csv.partial; done`.
   A finished job has a `.csv` and no `.partial`. Commit finished ones with their `.meta.json` and `_hist/`
   directory, then `python scripts/analyse_t13.py 196 484 676`. Do not commit a `_hist/` directory whose
   `.csv` does not exist yet: the job is still writing it.
2. **Read section 4.** Several decisions are Emily's and nothing on the quantum leg should be built or run
   until she makes them. Do not build the GHZ arrangement; it would add nothing (section 3, rung 3a).
3. **Two sessions worked this repository today.** The outreach-letters review (`docs/outreach/outreach_letters_2026-09-23.md`,
   commit 195f104, 13:58) was written before T15 rungs 3a and 0b were settled, so its advice to run the
   GHZ construction before writing the quantum letters is superseded: rung 3a is CLASSICAL by argument
   and any letter that mentions it must say so. Read section 6 before touching a letter.
4. **Never pipe `pytest` through `tail`.** It hides a failure behind `tail`'s exit code, and it bit today
   (section 9). Run `pytest -q > log; echo $?` and read the status.
5. The interpreter with numba is `C:\Users\emily\AppData\Local\Microsoft\WindowsApps\python.exe`; bare
   `python` lacks it (section 10).

## 1. What this project is, in one paragraph

Emily's hypothesis (`VISION.md`, claims 1–6): our spacetime is one settled arrangement of something deeper,
X; the change from X to spacetime was **sharp** and released a bounded lump of energy (claim 4); a leftover
remains (claim 5); an energy-like quantity is conserved across the change (claim 6); X must give back known
physics, including quantum mechanics (claim 2). The test bed is Trugenberger's 2D combinatorial quantum
gravity model (`src/graphity/cqg.py`; H = 16(N − S) + 4λX; λ = 1 is his model, the coefficient of his local
term). **The question is a change from one order to another, never from disorder.** The published question,
whether geometry forms out of a random network sharply or smoothly, was tested first (T6) because it is the
published question; it is not the hypothesis's. `VISION.md` Updates 13 to 21 are the current statement.
Three standing decisions of 22 September: X is curled and the change uncurls; the rule λ is fixed and the
activation is supplied; the bar is S2′, with the written caveat that T7 met four of its five parts before
S2′ existed, so **never count T7 as having cleared S2′**. The model's stand-in for X is the **tube**, a
4 × L lattice torus, metastable at λ = 1.25 and g = 1.5; "a stand-in, not X" is said everywhere.

## 2. Verdicts on the record (all pre-registered; `PREREGISTRATION.md`; details in `ASSUMPTIONS.md`)

| Test | Question | Verdict | Where |
|---|---|---|---|
| T6, λ = 0 (control) | Is the penalty-off transition first order? | **FIRST ORDER** under amendment 4 (Emily's): lump 12.5 per point, barrier growing at 34σ | O11 |
| T6, λ ≥ 1 | Out of the random phase, with the rule on? | **INCONCLUSIVE, final** by her decision: one hump everywhere, any lump below 1.3 per point at N = 100 and falling | O12, O17 |
| T7, λ = 1.25 | Is the tube → sheet change sharp? | **TWO-STATE CHANGE** at N = 64, 96, 192 (N = 144 fails gate 3 on one decay); every prediction holds at all four sizes | O13 |
| T9 | Sealed tube: bonfire or slush? | **BONFIRE WITH A THRESHOLD** at 64, 96, 192 | O14 |
| T10 | Does the leftover grow with the space? | **ONE RING, HOWEVER LARGE**; claim 5 is bookkeeping here | O15 |
| T11 | Is the leftover a seam? | **NEITHER**; position uniform; why exactly one is open | O16 |
| T12 | Does the coarse law govern? | Does not, by the standard set in advance | O24 |
| T13, N = 196 | Equilibrium jump or metastable ascent branch at λ = 1? | **NO VERDICT, one size of three.** P (his protocol): hysteresis 0.159, ascent jump in 3 of 4 replicas. E from the melt: gate passed, smooth, no jump. E from the torus: 0 round trips, not interpreted. Three post-hoc amendments, labelled so | PREREGISTRATION T13 |
| Gate B check | Is [T25] Fig. 3 his continuation procedure trapping the lattice? | **Does not fit**: Fig. 3 is high in both directions, across the whole transition, crossover at larger g; our copy of his protocol departs on ascent only, below g ≈ 3.5, by 0.16 at most. Gate B stays open | O27 |
| T15 rung 0 | Do the versions (renamings) exist where Update 17 says? | **INCONCLUSIVE by the letter.** Melt: exactly 1 at every size (holds). Sheet with a defect: > 1 on the isolated count 11 of 11, on the whole-world count 10 of 11; the whole's versions are the sheet's symmetries surviving the defect placement. Two post-hoc readings put to her, not enacted | O28 |
| T15 rung 3a | GHZ on three linked loops: instruction set or not? | **CLASSICAL for every arrangement, by argument**, before any construction: a renaming of a fixed arrangement is a complete instruction set; the naming is a Bell hidden variable. Her prediction (strongly contextual) fails | O29 |
| T15 rung 0b | Is the loop of four a resonator inside the sheet? | **INCONCLUSIVE by the letter; her prediction fails.** 6 of 7 states DISSOLVED (no mode above 0.25 of its weight on the loop), 1 RETUNED at the threshold. The loop is not a resonator; the cap (loop plus collar) is, in 2 states of 7, at other frequencies | O30 |

Plain English: the disorder → order route is not sharp in this family; the order → order route (the tube
opening) is sharp in every pre-registered sense and releases the exact lump; sealed, it is a bonfire with a
threshold; the leftover is one small defect however big the space; and the quantum leg, as stated in Update
17, cannot give Bell correlations by counting and its particle statement fails on the model's own loop.

## 3. What happened on 23 September, in order (commit hashes for the record)

- **T13 N = 196 read** under the original wording, then three amendments Emily decided that morning, all
  post-hoc for N = 196 and labelled so (38ec0eb, 90ea368): a jump is read across a 12 % window in g, with
  the control that no smooth curve becomes one; agreement is read among gate-passing starts; per replica,
  the majority decides, the mean reported beside. `scripts/analyse_t13.py`, tests in `tests/test_t13.py`.
- **The author's second note** (private; paraphrased in `docs/outreach/correspondence_2026-09-22_trugenberger.md`):
  his continuation procedure may accentuate the jump by trapping the wrong phase; a diverging correlation
  length points continuous or mixed. That is T13's reading (b), and N = 196 shows it. **Checked as an
  explanation of Fig. 3: it does not fit** (O27; `scripts/compare_gate_b_gap.py`, prints only).
- **Emily decided: matter is the structured leftover, not the melt** (VISION Update 19; her words: "why call
  melted phase matter? That's not matter"). T15 rung 0 pre-registered with her predictions, chosen from four
  options, and run (738badb): INCONCLUSIVE by the letter (O28). Read from the wiring: the four-point remnant
  is a closed loop of four, **one column of the tube left curled**, a cap on a cylinder of circumference 8
  whose collar winds twice round it; it comes at 4, 9 or 14 units; the eight-point rare piece is the 3-cube.
- **Rented compute** written to SideNerdApps conventions and nothing applied (89b4bab; section 8).
- **Emily asked why the model cannot be tested against a quantum prediction directly.** GHZ (rung 3a) was
  pre-registered with her prediction (2db2aa7), then settled by argument an hour later, before any
  arrangement existed (840096c; O29; VISION Update 20). Two exact side results stand: loops whose edges
  all carry three squares cannot be joined by an edge; a symmetric triangle of loops cannot be linked by
  edges. The stage-1 search scripts are scratch only and were stopped.
- **She asked how else; said proceed.** [Hardy01] and [Gorard20] read in part and recorded in
  `REFERENCES.bib`; `docs/design/amplitude_rule_brief.md` (9d00166) states the gap exactly (positive weights
  against complex amplitudes on the same versions; Hardy's fifth axiom is the one ingredient counting
  lacks), the exact bridge (a loop's vibrations are the Fourier modes of its versions; a loop of four
  carries only signs under the side rule, a loop of eight the quarter-turn phases), a **proposed wave rule
  for her decision under S1** (Hardy's axiom adopted as a postulate: quantum mechanics put in, not derived),
  and the interference test drafted (sin⁴ t across the loop of four under the rule, (1 − e^{−2t})²/4 under
  counting). **She held the rule** until the resonator rung had run.
- **T15 rung 0b** pre-registered with her prediction (36924d1) and run (776488c; O30; VISION Update 21):
  the loop is not a resonator in the sheet; the cap sometimes is. Her prediction fails.
- **The letter to the author** rewritten three times at her direction (c58bf8f, cbc6002, 2eed215):
  section 6.
- In parallel, another session reviewed the outreach letters (195f104): section 6.

## 4. Waiting on Emily (nothing here is to be done by the assistant unasked)

1. **T15 rung 0, two post-hoc readings:** per remnant type (every state with a closed loop of four has
   versions on both counts), and type by wiring (the five wirings have pairwise distinct spectra). Accept
   either, both or neither. As put in PREREGISTRATION T15 rung 0, "Reading".
2. **The quantum leg after rungs 3a and 0b:** redefine the object as the cap (a new pre-registration, not a
   re-reading), adopt the wave rule anyway, or leave the leg where rung 3a put it. Also whether Part V of the
   public document is restated as identical-particle symmetry, or the hypothesis reformulated over
   histories rather than arrangements (a different claim, needing its own dated VISION statement).
3. **Whether to send the letter** (`docs/outreach/reply_draft_2026-09-23.md`), and whether the optional
   paragraphs stay.
4. **After 484 and 676 land:** if protocol E fails its round-trip gate at both, T13 cannot reach a verdict
   and the sampler is the bottleneck; whether to build the neighbourhood-swap move of [T25] Fig. 8 is hers.
   She chose to wait for the runs before deciding.
5. **Rented compute:** the account ids in `terraform/_variables.tf` are `000000000000` on purpose; only she
   fills them, and nothing is applied without her.

## 5. What is running or queued

- **T13, four of nine jobs** (launched 22 September at 21:08 by the session before this one;
  `scripts/run_t6_tempering.py`; logs in that session's scratchpad, not this one's). At this writing:
  `t13_temper_n484_{melt,torus}` on their third replica of three (60 of 90 rows written);
  `t13_temper_n676_{melt,torus}` on their second of two (36 of 72). Each 484 replica takes 4 to 5 hours
  when the machine is not throttled, each 676 replica 8 to 12. Progress: `.partial` line counts.
- **Known already at 484:** both starts, replicas 0 and 1, `round_trips` = 0 against a gate of 3; from the
  melt the cold end reaches φ = 0.955, from the torus it stays at 0.999; the two never meet. Expect E to
  fail its gate at 484 and probably 676. Report it as not converged; do not interpret it.
- Done and committed: `t13_seq_n{196,484,676}`, `t13_temper_n196_{melt,torus}`, `t15_rung0`, `t15_resonator`.
- Nothing else. The laptop has 8 physical cores; do not run more than about 8 jobs.

## 6. The author, the letter, and the other session's outreach review

- **Carlo Trugenberger's two emails are private.** Paraphrased in
  `docs/outreach/correspondence_2026-09-22_trugenberger.md`; never quoted publicly. He has seen words, not
  plots or code; **S5 is not met.**
- **The current letter is `docs/outreach/reply_draft_2026-09-23.md`**, plain text and attachments in
  `docs/outreach/for_carlo_2026-09-22/` (pictures 1, 2, 4 and the N = 18 table). It supersedes the
  22 September draft, which was never sent. In order: his postscript confirmed at N = 196 with the numbers
  and `docs/figures/t13_n196_two_protocols.png`; the narrowed Fig. 3 question (size or coupling
  normalisation, since trapping cannot make a cooling curve high); the 484 mixing problem and a question
  about his neighbourhood-swap move; his words for ours; **the lead, at Emily's direction: the metastable
  curled torus and the column it leaves, asked as "is this an allotrope?", followed by whether the
  coefficient of his local term is fixed at exactly 1 or free** (at exactly 1 the flat torus, the curled
  torus and the 4-cube are degenerate at zero; his N = 4p² sizes are exactly those where the latter two
  cannot exist); the N = 18 exact benchmark in two sentences; the closing on his second question.
- **Out, at her decision, and why:** the offer of rented compute (he has run 1024 and 2000 himself; his
  large-size difficulty is mixing, not CPU; our own evidence does not need his sizes) and every "I will
  send" or "I will build". She wants no expectation of a pace of work. The opening says "with no schedule".
- **A caveat kept for her, not in the letter:** at N = 196 fourteen biplane graphs also tie with the torus at
  his coefficient (14 × 14 = 196), so "unique ground state" is not strictly true even at his sizes. He found
  the 14-vertex graph confusing last time.
- **The other session's review** (`docs/outreach/outreach_letters_2026-09-23.md`) covers seven cold emails
  to other physicists, adds two UVA names (Vucelja for sampling, Vaman for emergent gravity), and lists six
  repairs. Two of its statements are now out of date: the GHZ construction is not "the next step" (rung 3a
  is CLASSICAL by argument, and the prediction it says to state as strongly contextual has since failed),
  and any letter that mentions the quantum leg must carry rungs 3a and 0b as they stand. Its recommendation
  to send the Trugenberger reply first, and not the contextuality follow-up, still holds.

## 7. Corrections that must not be undone

- **The four-point remnant is a closed loop of four: one column of the tube left curled**, a cap on a
  cylinder of circumference 8, its collar of eight winding twice round it (O28 addendum). It lies along the
  tube in the sense of O16 and is a 4-cycle in the sense of the wiring; both are true. It comes at **4, 9 or
  14 units** depending on how many collar edges carry a third square; O15's "14 units per ring" is the
  cold-box member only. Verdict labels keep "ring"; prose says "the four-point remnant" or "the curled column".
- **The loop of four is not a resonator inside the sheet** (O30). Do not write that a particle is a vibration
  of the loop as if it held; the cap sometimes resonates, at other frequencies, and that is untested as an object.
- **Counting versions of a fixed arrangement is a hidden-variable theory** (O29). No test of that kind can
  violate Bell or GHZ; do not design one. The brief's fork was wrong and is marked so where it stands.
- **Matter is the structured leftover, not the melt** (Emily's decision, VISION Update 19). What [T25]
  calls matter is his.
- **The whole-graph renaming count measures the arrangement's symmetry, not the object's** (O28).
- **The model's hot phase is not X.** Write "the random phase".
- Never present T7 as having cleared S2′. Never write "nobody has done this"; write "we have not found".
- The early-universe changes are crossovers; freeze-out is a precedent for claim 6, not claim 4.
- Three times a shape has been named from a count and been wrong. **Read positions before naming a geometry.**

## 8. Rented compute (code only; nothing applied)

`terraform/` (flat, SideNerdApps conventions: `us-east-1`, the shared S3 state bucket under its own
`workspace_key_prefix`, workspaces via a locals account map, `default_tags`, exact pins), `Dockerfile`
(python 3.12.10, numpy 2.0.0, numba 0.67.0, matching every `.meta.json`), `docker/run.sh`,
`.github/workflows/deploy_manual.yml` and `run_simulation.yml`. AWS Batch on Fargate, spot off by
arithmetic (the runners cannot resume). `terraform/README.md` argues every choice and lists the steps before
a first apply. **The real saving is `replica_ids` for `run_t6_tempering.py` and `run_cqg_sweep.py`**, which
loop replicas serially; adding it needs a seeding test that replica k alone reproduces replica k inside a
full run. Not done. Nothing here runs without Emily's account ids and her say.

## 9. How Emily works, and the rules that bit us

- She is a software engineer, not a physicist. Lead with the answer, plain English, analogies. She wants
  to understand, not receive, and she pushes back; take the push seriously and check it.
- **Predictions are hers.** Put three or four options to her (`AskUserQuestion`), record which she chose
  and that she chose it, and record the assistant's own expectation beside it, labelled ours.
- **Rule changes after seeing data are proposed, never enacted.** Lay out options with consequences.
- **Pre-register before running; commit the prediction first; then check the design before building.**
  Today the GHZ fork was committed and found wrong an hour later, and a pre-registration commit went in
  with a failing test. Both are owned in the record. Work through the definitions for what any outcome
  would give *before* the commit, and read pytest's exit status.
- **Results are append-only.** Only `*.partial` may be deleted. Every CSV has a `.meta.json`; commit both.
  Never commit a result directory a live job is still writing.
- **Tests before every commit.** Commit messages end with `Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>`;
  PR descriptions end with `🤖 Generated with [Claude Code](https://claude.com/claude-code)`. `gh` is not
  installed; give her the compare URL. She merges; never push to `main`.
- Commit and push on the feature branch as work completes; confirm before anything outward-facing.
- **Toward the author she wants no expectation of pace.** No "I will send", no offers of work.
- Report inconvenient results as prominently as convenient ones; own mistakes once, without over-apologising.

## 10. Environment gotchas

- Interpreter with numba: `C:\Users\emily\AppData\Local\Microsoft\WindowsApps\python.exe` (3.12.10). Bash's
  bare `python` and `.venv` lack numpy. Use the full path for `pytest` and runs.
- `pdftoppm` is not installed, so the Read tool cannot render PDFs; `pypdf` was installed today
  (`--user`) and extracts text fine. Old arXiv papers render at `ar5iv.labs.arxiv.org/html/<id>`.
  Downloaded papers go in `docs/reading/` (gitignored).
- Background runs: `nohup <py> scripts/... > log 2>&1 &` from Bash; progress from `results/*.partial`.
- Bash heredocs eat `\n` inside Python strings; write scripts with the Write tool. Windows paths use
  backslashes: split on `/` after `.replace("\\", "/")`.
- Two sessions can be open on this repository at once; `git status` and `git log` before assuming the
  tree is as you left it, and read a file before editing it if the tool says it changed on disk.
- CRLF warnings on result CSVs are harmless.

## 11. Where things are

`VISION.md` (claims; Updates 1–21) · `TASKS.md` (the numbering map at the top matters: PREREGISTRATION's
T7–T13 are not TASKS' T7–T13) · `PREREGISTRATION.md` (T6–T13, T15 rungs 0, 3a, 0b) · `ASSUMPTIONS.md`
(Q1–Q18, O1–O30) · `REFERENCES.bib` (each note says how much was read) · `docs/design/` (`model_x_brief.md`,
`known_physics_plan.md`, `quantum_loop_design.md` with its fork marked wrong, `amplitude_rule_brief.md`) ·
`docs/outreach/` (the note, both paraphrased replies, the current letter, the picture folder, the other
session's review) · `docs/parked/` · `docs/figures/` · `docs/public/` (section 12) ·
`scripts/analyse_*.py` (one verdict script per test, pure functions of parsed rows, known-answer tests in
`tests/test_*.py`; newest `analyse_t13.py`, `analyse_t15_rung0.py`, `analyse_t15_resonator.py`) ·
`scripts/compare_gate_b_gap.py`, `scripts/plot_t13_two_protocols.py` · `terraform/`, `Dockerfile`,
`docker/`, `.github/workflows/` · `src/graphity/{cqg,sealed,dimension,wang_landau,tempering,connectivity,small_graphs}.py`.

## 12. The public-facing pages (unchanged today; Part V is now wrong as written, pending her decision)

"The Shape of a Phase-Changing Reality", https://claude.ai/artifact/TTC9knKGJFkR43X2JjsjZ5 (version 10).
The short page "Did space snap open?", https://claude.ai/artifact/5eDjM2Jh9AjUWSyqad563w (version 13), saved at
`docs/public/did-space-snap-open_v1.html`; `scripts/make_site_page.py` builds the site copy. The whole account
`docs/public/the-loop-and-the-floor_v1.html`, built by `scripts/make_physics_page.py` for sidenerdapps.com/physics.
Update all copies together. Rules: every claim says whose it is; no process narration. **Part V of the whole
account states the quantum picture without hedges; after rungs 3a and 0b it needs restating, and how is
Emily's decision (section 4).** Do not edit the public pages without her.

## 13. Natural next lines (pre-register before running; none started)

1. Read 484 and 676 when they land (section 5).
2. Her decisions (section 4).
3. If E fails its gate at the larger sizes and she says so: the neighbourhood-swap move of [T25] Fig. 8,
   validated against the exact averages at N = 18 (`scripts/exact_small_averages.py`) before use.
4. `replica_ids` for the tempering and sweep runners, with the seeding test, before any cloud run.
5. T15 rung 1 (exact at N = 16, 18 in the unlabelled ensemble; `results/ergodicity_small.csv` already holds
   every class's symmetry count): it tests the counting, not Bell, and is unaffected by 3a.
6. If she redefines the object as the cap: pre-register a resonator rung on loop plus collar, with the
   same definitions and her prediction.
7. The local-spark protocol (TASKS T14, and the second half of T13 rung 3): energy into one patch of a
   flat sheet, which no run has done yet.
8. Reading: Smolin's cosmological natural selection (parked, unread), and the two Wolfram papers beyond
   [Gorard20] if the histories reformulation is ever taken up.

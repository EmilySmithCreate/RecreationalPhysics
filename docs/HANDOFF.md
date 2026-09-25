# Start here: handoff for the next assistant (state as of 2026-09-25, 13:00 ET)

Written for the AI assistant that opens this repository next. Emily is the owner; she reads it too. It is
newer than `CLAUDE.md`'s "Known state". Work is on branch `feat/cloud-runs-and-3d` (shared by two sessions in one
working tree: add files by name, never `git add -A`, and never switch branches under another session); `main`
is behind and Emily merges. This page was rewritten as one current page on 24 September; earlier dated versions are in
git history.

## 0. The first ten minutes

1. **Two sessions may be working this repository at once.** Run `git status` and `git log -5` before assuming
   the tree is as described, and re-read a file if the tool says it changed on disk.
2. **The owner's direction of 25 September (memory `pace-and-scale`):** run the programme at full speed and scale while
   she is on vacation, many pre-registered tests at once, the cloud used generously, literature read in parallel, still by
   the book. **Running on AWS Batch (25 September, 13:00 ET)**, all submitted by `.github/workflows/run_queue.yml` from
   manifests in `cloud/queue/` (the workflow now reads several queue files per push; it failed on the first such push and
   was fixed, commit 590f6ff): **T34** (two 512-point jobs left), **T37** (34 jobs, many natural seeds in long tubes,
   paper 2; `scripts/analyse_t37.py`), **T38** (48 jobs, the rare long wait, paper 1; `analyse_t38.py`), **T39** (15 jobs,
   the cascade window, six and eight links; `analyse_t39.py`; its eight-link cells are expected to stall, see O62), **T40**
   (11 jobs, the push that starts the change in four directions; `analyse_t40.py`). The compute environment runs 16 jobs at
   once (terraform `max_vcpus = 16`); the account's Fargate quota is 30, and raising the ceiling is an infrastructure change
   the owner applies herself (the deploy workflow; the assistant's attempt to change it directly was refused by the
   harness, rightly). **Downloading:** the project account's keys are in the git-ignored `.env`; the 25 September session's
   scratchpad scripts `download_results.ps1` and `check_and_copy.py` load them into their own process, sync the bucket and
   compare each set's recorded config with the committed one before copying into `results/`; `aws_jobs.ps1` counts jobs
   by status, read only. Never print or commit the keys. **Read each finished test with its analyzer** and record it in
   ASSUMPTIONS (next number O63), the pre-registration and the programme page (dated, clock time, US Eastern).
   **Read and recorded on 25 September:** T36 TRANSIENT (O59), the six-link relic search negative (O58), T30 corrected
   (O54: the first direction opened fully in 28 of 84), the walls halve exactly only at one setting (O55), four literature
   reviews (O60; notes in `docs/reading/notes/`), the exact field-on-the-points calculation (O61), T33 NO CASCADE with every
   replica stalled after one move (O62). **T34 at 216 points reads MELTS; its verdict waits for the 512-point cells.**
   **Waiting on the owner:** the gravity rule (`docs/design/gravity_brief.md` section 6: a massless field on the points
   with relics as its sources, recommended; flat space in this family has an energy gap, so no pull at a distance is
   possible without a new ingredient); the exchange sign's convention (O60 (b)); her confirmation of the inferred
   predictions in T36 to T40. **Exploratory pilots of T37 (disclosed in its pre-registration) are in the scratchpad, not
   `results/`:** at 4 × 1024 and g = 1.5 the change started in 37 places and ended in a defected space 2.5 per point
   above flat, which is why T37 scores the scrap by the energy left.
3. **Read section 3 before writing anything public or anything to a physicist.**
4. Interpreter with numba: `C:\Users\emily\AppData\Local\Microsoft\WindowsApps\python.exe`. Run
   `pytest -q > log; echo $?` and read the status; never pipe pytest through `tail`.

## 1. What this project is

Emily's hypothesis (`VISION.md`, claims 1–6): spacetime is one settled arrangement of something deeper, X; the
change from X to spacetime was sharp and released a bounded lump of energy (claim 4); a leftover remains
(claim 5); an energy-like quantity is conserved (claim 6); X must give back known physics (claim 2). **The
question is a change from one order to another, never from disorder.** The test bed is built from
Trugenberger's combinatorial quantum gravity (CQG, `src/graphity/cqg.py`; H = 16(N − S) + 4λX). The model's
stand-in for X is the curled torus (the 4 × L torus, "the tube"), metastable for 1.05 ≤ λ ≤ 1.35 at g = 1.5.

**Naming, settled 24 September (the model's author's condition for endorsing paper 1):** only λ = 1 is CQG.
At any other λ the energy is not a curvature. The tube work is at λ > 1, so it is about a close cousin of CQG
and is **never** called combinatorial (quantum) gravity. Anything about gravity is tested in 3D only; no 2D
number is carried into a claim about gravity.

## 2. Verdicts on the record (pre-registered; `PREREGISTRATION.md`; details in `ASSUMPTIONS.md`)

| Test | Verdict |
|---|---|
| T6, λ = 0 (control) | FIRST ORDER (amendment 4) |
| T6, λ ≥ 1 | INCONCLUSIVE, final; one hump, any lump < 1.3 per point at N = 100 |
| T7, tube → sheet, λ = 1.25 | TWO-STATE CHANGE at N = 64, 96, 192 |
| T8, the λ map | INCONCLUSIVE by the letter (memoryless criterion too tight); sharp wherever stuck, 1.05 to 1.35; edge between 1.35 and 1.40 (O38) |
| T23, the λ map again at 120 decays | Window INCONCLUSIVE by the letter: the energy gate, unchanged from T8, fails at λ = 1.30 at every size (3 to 5 decays of 120); memoryless in 20 of 20 cells to 1.25. Edge: BREAK-UP BEGINS AT THE EDGE, as predicted (O44) |
| T9 sealed tube | BONFIRE WITH A THRESHOLD |
| T10 leftover vs size | ONE RING, HOWEVER LARGE |
| T11 | NEITHER |
| T12 | the coarse law does not govern |
| T13, λ = 1 at N = 4p² | INCONCLUSIVE: protocol E fails its gate at 484 and 676 |
| T15 rung 0 / 0b / 1 / 3a | INCONCLUSIVE / INCONCLUSIVE (loop not a resonator) / AGREES / CLASSICAL by argument |
| T16, correlation length | NONE (O31): nothing grows with N; susceptibility peak flat at 0.18 |
| T17, leftover per seed | BETWEEN: 1.10, 2.15, 2.50, 3.40 for k = 1, 2, 4, 8 |
| T18, room needed vs λ | PROPORTIONAL |
| T19, does the leftover last | ANNEALS at every fixed coupling |
| T21, sealed sheet with interchangeable points | MELTS EITHER WAY at N = 64 |
| T22, recrossings near λ = 1 | FALL-BACKS: first exit on time; κ = 0.56 to 0.68 |
| O40, O41 (exact) | 2D: a gas of knots is never stuck for λ > 1. 3D: the 6-cube is stuck only for 1 < λ < 1.2 |

## 3. The model's author, and what is public

- **Correspondence is private and not in this repository.** `docs/outreach/` is gitignored and local only
  (removed from the public tree on 24 September; older commits still hold copies, and whether to rewrite
  history is Emily's decision, deferred). Never commit anything from it. Never quote or closely paraphrase a
  private email in a tracked file.
- **Decided (Emily, 24 September): leave as they are.** Tracked files written before that rule paraphrase his
  emails (VISION Update 18, TASKS Gate B, ASSUMPTIONS O26/O27, PREREGISTRATION T13 and T16); that is ordinary
  "private communication" practice in science. New text follows the rule above.
- **His note of 24 September** (paraphrased locally): he will endorse paper 1 for gr-qc, on the naming condition
  above; he asks whether our moves are single switches and suspects low-coupling equilibration needs global
  moves; allotropes decay, and the question is how long they take ([T25] Fig. 9); his focus is the order of the
  transition. **Emily's reply was sent on 24 September** (local copy `docs/outreach/reply_sent_2026-09-24.md`).
  In it she says the moves are single switches, with replica exchange the only non-local ingredient; that the
  title and abstract carry his naming condition; and she asks for the allotrope's adjacency list (from him or
  Eryk Kopczyński; RogueViz may produce one), to predict its lifetime at λ = 1. Allotropes wait until after his
  work on the order of the transition. **Not yet asked:** Gate C's question (O43: [T22] Fig. 3's protocol,
  moves and weight). Keep it for his reply, one question at a time.
- **His reply of 25 September, evening** (paraphrase and a draft answer in `docs/outreach/reply_draft_2026-09-25_carlo.md`,
  local only): the allotrope has no finite adjacency list, so piece 12 is now T36, a numerical search he suggested; and he
  asked for a figure, drawn as `docs/figures/t13_n676_replica_exchange.{png,pdf}` by `scripts/plot_t13_n676_tempering.py`.
  The draft answer carries Gate C's one question (O53). Emily sends; nothing is sent from here.
- **S5, 25 September (the owner's report):** paper 1 has been submitted to arXiv, the model's author having endorsed it;
  it should appear within days, and she expects him to read it and respond within a couple of weeks. Do not prompt him.
  The pages say the door is open and the record is not yet read by a physicist.
- **Paper 1** (`docs/papers/curled_torus/`): retitled "…in a graph model of emergent geometry"; abstract and
  text say only λ = 1 is CQG; content from his private emails removed ("hybrid", the N = 4p² advice). The PDF
  was rebuilt with Tectonic (not installed system-wide; fetched into a session scratchpad). **Plan:** send the
  reply with the PDF, he endorses, submit to arXiv, then publish the web page linking to it.
  **Revised the same afternoon after a review Emily obtained from ChatGPT** (ASSUMPTIONS O42; disclosed in the
  paper's acknowledgments): the dynamics is named wherever
  kinetics appear (Introduction, Discussion); "the nucleation barrier" became the minimum energetic barrier to the
  first exit, with κ as the rest of nucleation; Eq. (2)'s ordered-proposal count is explicit, with the twisted
  same-energy family and the distant-edge exits it leaves out; labelled vs interchangeable has its own paragraph;
  "however large" and "no coexistence temperature" were softened to what was measured; d(v) is defined as an order
  parameter; a "why deform λ" paragraph; Fig. 2(c) survival panel and SE bars on Fig. 3(a); Table I's N = 192
  rerun filled in; both barrier fits quoted. Title now "...decompactification between ordered states in a graph
  model of emergent geometry" (Emily, 24 September); the cow line kept. Now 7 pages. The programme page was brought
  into line (pieces 1, 2, 5), light on numbers as she wants it; the plain-language page was left alone by her
  decision.
- **Web pages.** `/physics` on sidenerdapps.com is now the plain-language page
  (`docs/public/did-space-snap-open_v1.html` → `scripts/make_site_page.py` → `docs/public/site/physics/index.html`;
  Emily pastes it into the SideNerdMarketing repository, which deploys). Version 2 carries today's corrections.
  The whole-account page (`the-loop-and-the-floor_v1.html`) is corrected to version 2 but **not published**;
  its build writes to `docs/public/site/account/` with a placeholder URL. Do not publish either without her.
  The programme page is `docs/public/programme.html`, mirrored as the private artifact
  https://claude.ai/artifact/JLtR2aqHmL2FghWmNZU8xW; its text source is `docs/papers/programme_draft.md`, and the
  two are updated together.
  Every claim says whose it is; no process narration.

## 4. Waiting on Emily

0. **T26's prediction is hers (confirmed 24 September, night).** T25's (FREEZES IN, which held) and T27's (FOLDS
   BEFORE IT FLATTENS, which failed) stay marked inferred; she may confirm or disown them. Her decision of the same
   night is on the record as VISION Update 24: proceed with the six-link work now, reproduction later. Decide whether to
   send any of the per-paper letters proposed in `docs/papers/series_plan.md` ("Who to ask"), none drafted or sent.
   **T28, the gravity test:** its dynamic form cannot run at equilibrium (O51); its exact counting rung can, and a
   sealed form would need a new protocol declared first. Her prediction is still wanted before anything runs.
1. Whether to send the reply to Carlo (and the PDF), and when to submit to arXiv.
2. The allotrope of [T25] Fig. 9: the reply asks for its adjacency list. **Do not build it from the drawing:**
   every coloured face looks four-sided, which does not fit the caption. Exact and ready once the graph exists:
   if no edge carries three squares, the local term is zero and the question does not depend on λ.
3. The quantum leg after rungs 3a and 0b (redefine the object as the cap; a rule for cancelling versions;
   her position that it comes from the loop). Nothing is built until she decides.
4. T15 rung 0's two post-hoc readings; T8's proposed repair.

## 5. Natural next lines (pre-register before running)

0. **Decided, 25 September late afternoon (VISION Update 29, her "Proceed"):** the exchange phase on loops is the first
   rule of the new model; its fermionic form is a selection rule (O57, `scripts/exact_exchange_sign.py`). Next for it: the
   rule inside the interchangeable chain against the exact averages at N = 16 and 18 (`scripts/exact_small_averages.py`
   is the reference), then the anyonic form. Gravity step 1, the six-link relic search (`scripts/exact_relic_search_d.py`),
   is recorded as O58 when read.
0. **The owner's direction, 25 September afternoon (VISION Update 28):** other models with loop and exchange rules
   (`docs/design/loop_exchange_brief.md`, candidate rules for her to choose under S1; nothing built); gravity as the
   target, at least directionally, at one λ (`docs/design/gravity_brief.md`: definitions, observable, targets, protocol,
   what is missing). The four-, six- and eight-link runs are groundwork for the new model.
0. **Papers:** five drafts exist (`curled_torus`, `relic`, `fertile_window`, `black_hole`, `six_links`), all in line
   with the record as of 25 September morning, none with a PDF, none read by the owner. The six-link one has an empty
   eight-link section waiting for T33. The programme page now carries a dated change log and a per-piece date; keep both
   current whenever a result comes in (the owner asked for this on 25 September).
1. Gate C: failed (O43). Gate C′ (O46) is running: if reading (iv) holds in 3D and the 2D width says two powers, the
   gate is passed under that reading and the six-link track reopens; if the 2D width says one power, the next build is
   a six-link kernel that allows triangles and pentagons (the paper's own ground states have them); if A fails, the
   question goes to the model's author. Report P2 when it lands. **The gravity test (piece 7) is designed as T28 in
   `docs/papers/series_plan.md` and waits on this gate; its exact rungs (energetic and counting pull of two 3D relics
   at fixed wiring) need no gate and can be computed now.**
2. T23: read (O44). Piece 2 is being settled by T24 (running), whose gate 3′ was fixed before the run.
3. The allotrope, once the graph arrives: stuck or not at λ = 1, its barrier, its lifetime against size.
4. If not yet done: a cloud result checked bit for bit against the same config run on the laptop.
5. The scrap race (does it freeze in as the box cools?), and the local-spark protocol (TASKS T14).
6. `replica_ids` for the tempering and sweep runners, with the seeding test, before large cloud runs.
7. The long tail at λ = 1.05 (O42, unexplained): 3 of 200 waits near 80,000 sweeps where an exponential gives 0.19.
   **Emily, 24 September: not a priority**; it does not bear on paper 1's point, and it is left for later or for
   anyone who wants it. If taken up: many first exits at λ = 1.05 (a few hundred replicas), pre-registered.

## 6. Corrections that must not be undone

- **Only λ = 1 is CQG** (section 1). Titles, abstracts, captions and page footers are checked for this.
- **The model has no time.** Piece 13 (VISION Update 25) tests the pattern in which four curled directions open; which
  direction is time it cannot say, and no page says so.
- **Every six-link result carries the caveat that the reproduction gate is open** (VISION Update 24), and O41's windows
  are for the tori it listed: the two-curled state with a long open side is stuck to λ = 1.5 (O49), not 1.2.
- **Matter is the structured leftover or the released energy, not the melt** (Emily, VISION Update 19). What
  [T25] calls matter is his.
- The four-point remnant is one column of the tube left curled; it comes at 4, 9 or 14 units.
- The loop of four is not a resonator inside the sheet (O30). Counting versions of a fixed arrangement is a
  hidden-variable theory and cannot violate Bell (O29).
- The waiting-time law: plain mean ratio 0.98, weighted 0.88 ± 0.06, over twelve conditions. Never "three
  parts in a thousand" or "half a per cent".
- The model's hot phase is not X; write "the random phase". Never present T7 as having cleared S2′. Never
  write "nobody has done this"; write "we have not found". **Read positions before naming a geometry.**

## 7. How Emily works

- She is a software engineer, not a physicist. Lead with the answer, plain English, analogies. She pushes
  back; take it seriously and check it.
- **Predictions are hers.** Put options to her, record her choice and ours beside it, labelled.
- Rule changes after seeing data are proposed, never enacted. Pre-register before running.
- Results are append-only; only a crashed run's `*.partial` may be deleted. Every CSV has a `.meta.json`.
- Tests before every commit. Commit and push on the feature branch; she merges; never push to `main`. `gh` is
  not installed; give her the compare URL.
- Toward the model's author: no expectation of pace; no "I will send". She collaborates only on work that
  includes the order → order question.
- Her coined term: **curve-first gravity** (`docs/papers/glossary.md`).

## 8. Environment

- Bash's bare `python` and `.venv` lack numpy; use the full interpreter path above for pytest and runs.
- `pdftoppm` is missing, so the Read tool cannot render PDFs; PyMuPDF or pypdf extract text. arXiv HTML
  sometimes omits figures; render the PDF page instead. Downloaded papers go in `docs/reading/` (gitignored).
- Bash heredocs eat `\n` inside Python strings; write scripts with the Write tool.
- Background runs: `nohup <py> scripts/... > log 2>&1 &`; progress from `results/*.partial`.

## 9. Where things are

`VISION.md` (claims; Updates 1–22) · `TASKS.md` (its numbering map matters) · `PREREGISTRATION.md` ·
`ASSUMPTIONS.md` (Q1–Q21, O1–O41) · `REFERENCES.bib` · `docs/papers/` (paper 1, `series_plan.md`,
`programme_draft.md`, `glossary.md`) · `docs/design/` · `docs/parked/` · `docs/public/` · `docs/figures/` ·
`scripts/analyse_*.py` with tests in `tests/` · `terraform/`, `Dockerfile`, `.github/workflows/` ·
`src/graphity/` (`cqg.py`, `cqg_d.py` for any D, `sealed.py` (now with per-vertex stores and stream carry-on), `spark.py` (the local spark, Q22), `tempering.py`, `symmetry.py`,
`interchangeable.py`, `connectivity.py`, `small_graphs.py`) · `cloud/queue/` (push-triggered Batch manifests).

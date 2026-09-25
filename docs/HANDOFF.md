# Start here: handoff for the next assistant (state as of 2026-09-25, early morning)

Written for the AI assistant that opens this repository next. Emily is the owner; she reads it too. It is
newer than `CLAUDE.md`'s "Known state". Work is on branch `feat/cloud-runs-and-3d` (shared by two sessions in one
working tree: add files by name, never `git add -A`, and never switch branches under another session); `main`
is behind and Emily merges. This page was rewritten as one current page on 24 September; earlier dated versions are in
git history.

## 0. The first ten minutes

1. **Two sessions may be working this repository at once.** Run `git status` and `git log -5` before assuming
   the tree is as described, and re-read a file if the tool says it changed on disk.
2. **Running (25 September, early morning).** Nothing on the laptop: Gate C's P2 finished and is read (O46 addendum: fully ordered to g = 4 with
   long equilibration, which undercuts the 1/g² reading), and the exploratory 3D window scans are read (O51: no coupling
   at which a flat 3D sheet rearranges without melting). On AWS Batch,
   each set submitted by the push-triggered workflow `.github/workflows/run_queue.yml` from a manifest under
   `cloud/queue/`: **T24** (28 jobs, `2026-09-24_t24.txt`), **Gate C′** (4 jobs, `2026-09-24_gatec2.txt`; O46;
   `scripts/analyse_gatec2.py`), and **T30 and T32** (14 jobs, `2026-09-25_t30_t32.txt`; the six-link tests of piece 11,
   read with `scripts/analyse_t30.py`), and **T33** (6 jobs, `2026-09-25_t33.txt`; the eight-link pattern test of piece 13,
   read with `scripts/analyse_t33.py`; about eight hours a job). Results land in the bucket; download, check and commit
   them as T23's were. **To see the Batch jobs' state from a laptop without the project account's credentials:** push a
   change to `cloud/status/request.txt` (any text); the `queue_status` workflow then writes `cloud/status/latest.md`
   (job states and the bucket's finished results) and commits it, readable from the repository.
   **Read and recorded tonight:** T25 FREEZES IN (O47), T27 STAYS MELTED and T26 MELTS (O48). A finished local job has a `.csv` and
   no `.partial`. Never commit a result a live job is still writing. **Read each finished test with its analyzer** (`scripts/analyse_t24.py`,
   `analyse_t25.py`, `analyse_t26.py`) and record the verdict in ASSUMPTIONS (next numbers O46 onward; O45 is the other session's exploratory Gate C reading), the
   pre-registration section, and the programme page. **The owner's predictions in T25 to T27 are inferred from
   her stated positions** (PREREGISTRATION says so in each); ask her to confirm or replace them before any
   verdict is quoted as hers. `results/explore_c_fastboth.csv` is the other session's untracked result: not ours
   to commit. T23 is done and read (O44). American spelling in everything written from tonight on (her request).
   **Gate C has FAILED (ASSUMPTIONS O43):** the six-link code does not reproduce [T22] Fig. 3 at the unscaled
   couplings or at couplings × N^(1/3), and the shapes differ. By rule 2 the six-link (D = 3) track is stopped:
   no D = 3 result, including O41's window, is quoted or interpreted until it is resolved. **Exploratory (O45):** a
   fast heating leg (20 sweeps per coupling) from a slowly cooled state reproduces Fig. 3's steepness and plateau,
   with its axis about our g / 5 to 6, which suggests the figure is a heating curve that lags equilibrium. The
   question for the model's author: was Fig. 3 a heating run from an ordered start, how many sweeps per coupling,
   and how is ħg defined in its weight. Hold it for his next reply.
   Note: commit `0746203` (labelled as the Gate C criterion) also carries the removal of `docs/outreach/` and
   the old `docs/public/site/index.html` from the tracked tree, swept in from the shared index.
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

0. **Read tonight's four tests** when they land (section 0, item 2), then bring the programme page (both files and
   the artifact), `series_plan.md`, and the paper drafts `docs/papers/relic/` and `docs/papers/fertile_window/`
   into line with the verdicts. Paper 4 (the black-hole piece) is not drafted; T26 and T27 are its first results.
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

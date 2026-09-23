# Start here: handoff for the next assistant (state as of 2026-09-23, morning)

Written for the AI assistant that opens this repository next. Emily is the owner; she will read it too.
Read it before `CLAUDE.md`'s "Known state" section, which is older than this page.

## 0. Newest first: 23 September, morning

- **Outreach letters reviewed (23 September, afternoon):** `docs/outreach/outreach_letters_2026-09-23.md` reviews Emily's seven draft cold emails against each recipient's 2024 to 2026 work and the repo's record, adds two UVA people the list was missing (Vucelja for sampling, Vaman for emergent gravity), and holds the refined letters. It recommends sending the existing Trugenberger reply first and not the contextuality follow-up.
- **T13 at N = 196 is read (PREREGISTRATION T13, "Reading at N = 196"): NO VERDICT, one size of three.**
  Protocol P (his protocol copied): hysteresis 0.159, ascent jump in 3 of 4 replicas. Protocol E from the melt:
  gate passed, smooth, no jump. E from the torus: 0 round trips, not interpreted. Three amendments to T13 were
  decided by Emily that morning, **all post-hoc for N = 196 and labelled so**: (1) a jump is read across a
  window of 12 % in g, not only between neighbours — the control being that no smooth curve becomes a jump;
  (2) equilibrium agreement is read among gate-passing starts; (3) per replica, the majority decides, the mean
  reported beside. `python scripts/analyse_t13.py 196 484 676`; known-answer tests in `tests/test_t13.py`.
- **The author wrote again** (second note; paraphrased in the correspondence file, private): his procedure of
  starting each coupling from the previous coupling's graph may accentuate the jump by trapping the wrong
  phase — T13's reading (b), which the N = 196 data already shows. **Checked as an explanation of Gate B's
  Fig. 3 and it does not fit** (ASSUMPTIONS O27; `scripts/compare_gate_b_gap.py`): Fig. 3 is high in both
  directions and its crossover is at a larger g. The reply draft carries the N = 196 result and the narrowed
  question, with a figure for him (`docs/figures/t13_n196_two_protocols.png`). Not sent.
- **Emily decided: matter is the structured leftover, not the melt** (VISION Update 19). T15 rung 0 was
  pre-registered with her predictions and run the same morning: **INCONCLUSIVE by the letter** (ASSUMPTIONS
  O28; PREREGISTRATION T15 rung 0). Melt: one version at every size. Sheet with a defect: versions on the
  isolated count always, on the whole-world count in 10 of 11 — the whole's versions are the sheet's
  symmetries surviving the defect placement. The four-point remnant is, by wiring, a closed loop of four; the
  eight-point piece is the 3-cube. Two post-hoc readings under which every prediction holds are **put to her,
  not enacted**.
- **T15 rung 3a (GHZ) was pre-registered with Emily's prediction (strongly contextual) and then settled by
  argument before any arrangement was built: CLASSICAL for every arrangement** (PREREGISTRATION T15 rung 3a;
  ASSUMPTIONS O29; VISION Update 20). A renaming of a fixed arrangement is a complete instruction set, so the
  naming is a Bell hidden variable and no counting test of this kind can violate Bell or GHZ. Her prediction
  fails. What survives: rungs 0 to 2 and interference (rung 4, needs a dynamical rule). **Waiting on her:**
  whether Part V of the public document is restated as identical-particle symmetry, or the hypothesis is
  reformulated over histories (a different claim). Do not build the GHZ arrangement; it would add nothing.
- **She then asked how else the quantum predictions could be tested, and said proceed.** [Hardy01] and
  [Gorard20] were read in part and recorded; `docs/design/amplitude_rule_brief.md` states the gap exactly
  (positive weights against complex amplitudes on the same versions), the exact bridge (a loop's vibrations
  are the Fourier modes of its versions; a loop of four carries only signs under the side rule, a loop of
  eight the quarter-turn phases), and **a proposed rule for her decision under S1**: amplitudes on a loop's
  points evolving by its Laplacian, which is Hardy's fifth axiom adopted as a postulate and puts quantum
  mechanics in rather than deriving it. The interference test is drafted there. **Ready without any
  decision:** whether a loop's vibration survives as a localised mode when the loop sits in a sheet (the
  brief's section 5, on the saved two-loop states); pre-register with her prediction, then run.
- **Rented compute** exists as code and nothing else: `terraform/`, `Dockerfile`, `docker/run.sh`,
  `.github/workflows/{deploy_manual,run_simulation}.yml`, following SideNerdApps conventions (AWS Batch on
  Fargate, spot off by arithmetic). **Nothing applied; account ids are `000000000000` on purpose.** The real
  saving is `replica_ids` for the tempering and sweep runners, which needs seeding tests first
  (`terraform/README.md`).
- Four T13 jobs are still running (section 5).

## 0b. The author replied (2026-09-22, night)

Carlo Trugenberger answered Emily's note the same day. **Private email; paraphrased in
`docs/outreach/correspondence_2026-09-22_trugenberger.md`; never quote it publicly.** What it moves:
the "cap" (Q3) is disputed by him and is no longer a published case; his own current view of the λ = 1
transition is a **hybrid** one, two continuous branches with a jump, at N = 1024 on cold ascent; and
he advises N = 4p² with p prime for a unique ground state. A reply is drafted in
`docs/outreach/reply_draft_2026-09-22.md` with a picture made for him
(`docs/figures/for_authors_torus_vs_tube.png`). The next run on the disorder → order track is T6 at
N = 196, 484, 676 in both directions with tempering, pre-registered first, to tell an equilibrium jump
from a metastable ascent branch. S5 is not met; he has seen words, not plots or code. Also new on
22 September, night: the public document `docs/public/the-loop-and-the-floor_v1.html` (five parts, the
loop withheld until Part III), VISION Update 17 (the author's quantum hypothesis) and the design brief
`docs/design/quantum_loop_design.md` (T15).

## 1. What this project is, in one paragraph — and what changed on 22 September

Emily's hypothesis (`VISION.md`, claims 1–6): our spacetime is one settled arrangement of something
deeper, X; the change from X to spacetime was **sharp** and released a bounded lump of energy (claim 4);
a leftover remains (claim 5); an energy-like quantity is conserved across the change (claim 6). The test bed
is Trugenberger's 2D combinatorial quantum gravity model (`src/graphity/cqg.py`; H = 16(N − S) + 4λX).

**The question is a change from one order to another, never from disorder.** X is a specific, stable-for-now
arrangement. The published question — does geometry form *out of a random network* sharply or smoothly — was
tested first (T6) because it is the published question; that is *not* the hypothesis's question, and the
previous assistant re-scoped late. Do not repeat that. `CLAUDE.md`'s opening "one question" predates this
re-scoping; `VISION.md` Updates 13 and 14 are the current statement. Three decisions Emily made on 22 September:

- **Direction:** X is curled and the change uncurls. X has *fewer* large dimensions than spacetime.
- **Trigger:** the rule (λ) is fixed; the activation is supplied — by a thermal fluctuation or a delivered push.
- **The bar:** S2′ (VISION, "What success means") for a change between two orders, with the written caveat that
  T7 met four of its five parts before S2′ existed. Never count T7 as having cleared S2′.

The model's stand-in for X is a **tube**: a 2D sheet with one direction curled to length 4, sitting 4(λ − 1)
per point above the flat sheet at λ > 1, metastable at λ = 1.25 and g = 1.5, unstable at λ = 1.5.
"The tube is a stand-in, not X" is stated everywhere; keep it so.

## 2. Verdicts on the record (all pre-registered in `PREREGISTRATION.md`; details in `ASSUMPTIONS.md` O11–O16)

| Test | Question | Verdict | Where |
|---|---|---|---|
| T6, λ = 0 (control) | Is the penalty-off transition first order? | **FIRST ORDER** under amendment 4 (Emily's) — lump 12.5/pt, barrier +34σ with size | O11 + addendum |
| T6, λ ≥ 1 | Out of the random phase, with the rule on? | One hump at every λ/size/replica; any lump < 1.3/pt at N = 100 and shrinking. **INCONCLUSIVE, final** — criterion 3 unreadable as an energy cumulant, and the φ-cumulant version (amendment 5 (a)) reads the hot edge; Emily decided to leave it there (not the hypothesis's route) | O12, O17 + addendum |
| T7, λ = 1.25 | Is the tube → sheet change sharp? | Amendment 4 (a) enacted by Emily: the twelve read from their wiring (`t7d_*`, `scripts/analyse_t7_states.py`). **TWO-STATE CHANGE at N = 64, 96, 192**; N = 144 fails gate 3 on one decay (changed state inside its last measuring window). Predictions hold at all four sizes. `python scripts/analyse_t7.py lam125 t7b t7c t7d` | O13 + three addenda |
| T9 | Sealed tube: bonfire or slush? | **BONFIRE WITH A THRESHOLD** at 64/96/192; no stall in 420 runs; crossover ∈ (N/4, N/2], predicted N/3.5 inside | O14 |
| T10 | Does the leftover grow with the space? | **ONE RING, HOWEVER LARGE** (0.9–1.05 per box at 64–288). Claim 5 is bookkeeping in this model | O15 |
| T11 | Is the one leftover a seam where the front's ends meet? | **NEITHER** — position uniform. Why exactly one: **open** | O16 |

Plain-English summary: the disorder → order route is not sharp in this family; the order → order route (tube
opening) is sharp in every pre-registered sense and releases the exact lump; sealed, it is a bonfire with a
threshold; the leftover is one small defect however big the space.

## 3. Corrections that must not be undone

- **The leftover is a four-point remnant lying *along* the tube, not a ring around it** (O16). Four vertices at
  local dimension 1, one extra square, six surplus edges, 14 units at λ = 1.25, one cluster. "Ring" was a guess
  from the count alone. Pre-registered verdict labels ("ONE RING, HOWEVER LARGE") keep their names; prose says
  "four-point remnant". The first non-tube vertices at departure are 4–6 in 4–5 adjacent columns (a line), not
  "two rings".
- **A second, rarer leftover exists:** a 20-unit twist (S = N, X = 4; two vertices at d = 1, two at d = 3), in
  9 of 80 cold boxes (O15).
- Three times this project has labelled a shape from a count and been wrong. **Read positions before naming a
  geometry.**
- Never write "nobody has done this". Say "we have not found".
- The early-universe changes (electroweak, QCD) are **crossovers**; freeze-out is **not** a phase transition — it
  is a precedent for claim 6 (accounting), not claim 4 (sharpness). A reader corrected this on the page.

## 4. Decisions (updated 2026-09-22, evening)

Both decisions below were made by Emily (option (a) each) and enacted; results in section 2. The one that
reopened (T6 criterion 3 at λ ≥ 1) was settled the same evening: left INCONCLUSIVE, no further rule change.
Nothing is waiting on her. The text below is kept as the record of what was put to her.

### As put to her

- **T7 amendment 4.** The replays (amendment 3, done: `results/t7c_lam125_n*.csv`, `python scripts/analyse_t7.py lam125 t7b t7c`)
  showed 12 of 240 decays resting on states that are neither the sheet nor the four-point remnant, energies 8–45
  units. Gate 3's list of allowed final states was an assumption. Options: **(a)** replay the twelve once more with
  the final adjacency saved, read each state from the graph, and pass gate 3 when the released energy equals the
  exact energy of the structure read (recommended); **(b)** gate only decays that reached the full release and
  report the rest. Note: a decay with `settle_sweeps` = cap did *not* "keep moving" — amendment 1's settle loop
  terminates only at the full release, so any ledge runs to the cap. Do not repeat that misreading (O13, second addendum).
- **T6 amendment 5.** At λ ≥ 1 the cold phase is the sheet at H = 0, and the Binder *energy* cumulant collapses
  there (it is not shift-invariant), so criterion 3 cannot be read and the verdict is INCONCLUSIVE by the letter.
  Options: **(a)** use the fourth-order cumulant of φ instead, computed from the `t6c` files as they stand
  (recommended); **(b)** declare criterion 3 uninformative at λ ≥ 1 and issue the verdict on criteria 1–2 with the
  bound. Expected outcome under either: NO EVIDENCE OF FIRST ORDER AT THESE SIZES.

## 5. What is running or queued

- **T13: four of nine jobs still running** (launched 2026-09-22 at 21:08 by the previous session;
  `t13_temper_n484_{melt,torus}` and `t13_temper_n676_{melt,torus}`, `scripts/run_t6_tempering.py`). The machine
  throttled overnight (one N = 196 replica took 6 h instead of 50 min); Emily has turned her sleep timer off.
  Progress: `results/t13_*.partial` line counts and the `_hist/` dirs, which stay untracked until the run finishes.
  Done and committed: `t13_seq_n{196,484,676}`, `t13_temper_n196_{melt,torus}`. When a CSV lands, commit it with
  its meta and `_hist/`, then `python scripts/analyse_t13.py 196 484 676`. **Known already:** replica 0 of both
  N = 484 runs returned `round_trips` = 0 against a gate of 3. If E fails its gate at both larger sizes, T13 cannot
  reach a verdict and the sampler is the bottleneck — the neighbourhood move of [T25] Fig. 8 is the candidate,
  and Emily chose to wait for the runs before deciding that.
- Nothing else. The laptop has 8 physical cores; do not run more than ~8 jobs.

*22 September, evening:* the `t7d_*` replays and the `t6c_*` reruns finished and are read (O13, O17).

*Update, late evening (22 Sept), after a run of questions from Emily about gravity, dark energy and black
holes.* Five new pieces of work, all committed, all EXPLORATORY except the two that are exact:

- **Q18 (exact): zero is the floor.** A chain on graphs that allow triangles and pentagons
  (`general_chain.py`, built for this) plus a short argument: the hard-core rule forbids a triangle beside a
  square and two triangles on an edge, so every valid edge has curvature at most zero and **nothing sits
  below flat space**. Space is stable; the cuboctahedron, the obvious lower candidate, is illegal.
- **O20: a sealed sheet given energy melts rather than folds**, at four λ and budgets 0.5 to 16 a point.
  Folding is four times cheaper per square and still loses. **Read the correction under O20 before quoting
  it:** melted is the random phase, which [T25] calls matter, and equilibrium heating randomises by
  construction, so this is weaker than it first sounds.
- **O21: three braces runs.** A cold sheet accepts no move at all; two closed pieces survive exactly where
  the sheet does; a cooled melt jams at about +2 a point. **The jam was not real and is withdrawn.** Emily challenged it —
  she said she did not believe such a state exists and that there should be two phases with nothing between
  — and the check agrees: downhill moves exist from both end states (2 of 4264, and 1 of 4646), so the chain
  had stopped rather than settled. O21 now records that, with the lesson: a stopped chain and a resting
  state look identical in an energy trace, so ask for the moves out.
- **O22 (exact): no long-range force between leftovers, and it is a theorem.** Two defects cost exactly
  twice one at every separation, and 16 less only where they touch. H is a sum of per-edge terms, so any
  defects sharing no square are additive. Gravity here, if it exists, must be entropic.
- **Emily's positions changed twice and both are recorded** (`docs/parked/extension_2026-09-22.md`):
  refolding is *expensive* and paid for by concentrated energy, so space never needs to be metastable (the
  dark-energy-as-excess leg is dropped, and the page says so); and gravity may be a pull back towards
  symmetry, which in standard language is symmetry restoration at high density. Smolin's cosmological
  natural selection is the closest published relative of her loop and **neither of us has read it**.

## 6. Natural next lines (pre-register before running)

**Waiting on Emily (23 September):** (a) the two post-hoc readings of T15 rung 0 — per remnant type, and type by
wiring — accept either, both or neither; (b) whether to send the reply to the author (`docs/outreach/reply_draft_2026-09-22.md`)
with the new N = 196 paragraph and picture; (c) after 484 and 676 land, whether to build the neighbourhood move if
protocol E fails its gate there. **Ready with nothing new needed:** T15 rung 1 (exact at N = 16, 18 in the unlabelled
ensemble; `results/ergodicity_small.csv` already holds every class's symmetry count); `replica_ids` for the tempering
and sweep runners, with a seeding test that replica k alone reproduces replica k inside a full run, before any cloud run.

0. **At Emily's request:** the known-physics ladder (`docs/design/known_physics_plan.md`, TASKS T13) and
   the leftover-per-seed test (TASKS T14). Start with the reading and rung 1's reproduction gate.

1. ~~T7 replays~~ done (amendments 3 and 4).
2. Why one remnant per cold box — no hypothesis in hand after the seam refutation. A read of *what* the remnant is
   (its edges, its exact shape) would come before any new mechanism guess.
3. ~~Do remnants attract one another~~ **answered exactly, O22: only by touching, and no long-range force is
   possible.** What remains of that item is the other half: does a *local* spark on a flat sheet re-curl it or melt
   it (discriminates Emily's black-hole picture from [T25]'s). It needs a local-spark protocol — energy delivered
   to one patch rather than to a shared demon — which does not exist yet and is the single most useful thing to
   build next. Everything measured so far heats the whole sheet, and equilibrium heating always randomises.
4. Where the metastable window closes between λ = 1.25 and 1.5 (PREREGISTRATION T8, the λ map).
5. Writing to the authors (both groups) — draft was given in chat only, never in the repo; VISION "Before anything
   is shown to anyone" lists the items. Then a physicist reader (S5).

## 7. The public-facing pages

"The Shape of a Phase-Changing Reality", a claude.ai artifact owned by Emily:
https://claude.ai/artifact/TTC9knKGJFkR43X2JjsjZ5 — version 10, 31 sections, updated through T11. Written for a
non-scientist and a physicist reader. To update: `Artifact read` the URL (it saves the full HTML locally), edit,
republish with `url`. Its figures are published files alongside (kept on republish). Rules for it: every claim
says whose it is (the coloured boxes); no process narration (who reminded whom, when) — that goes in commits and
`ASSUMPTIONS.md`; lattice citations in section 1 are marked "to verify" and are not in `REFERENCES.bib`.

**The short page, which is the one being published:** "Did space snap open?",
https://claude.ai/artifact/5eDjM2Jh9AjUWSyqad563w — Version 13 at this writing. Saved verbatim at
`docs/public/did-space-snap-open_v1.html`; `scripts/make_site_page.py` builds `docs/public/site/index.html`
from that copy for sidenerdapps.com (own head, sharing tags, public links, no-JavaScript notes, every picture
inline SVG). **Update all three together**: edit the scratchpad copy, republish the artifact, copy to
`docs/public/`, rerun the build. It now carries the loop section, the gravity rung and the dropped
dark-energy leg.

**The whole account, for sidenerdapps.com/physics** (added 2026-09-22, night): `docs/public/the-loop-and-the-floor_v1.html`
is the artifact source (title "Did Space Snap Open?", the short page's design, five parts, the author's own coda);
`scripts/make_physics_page.py` builds `docs/public/site/physics/index.html` from it, a complete document with no
JavaScript and every picture inline, to be copied into the SideNerdMarketing repository at the path that serves
`/physics/`. Update the source, republish the artifact, rerun the build, and copy the output across.

## 8. How Emily works, and the rules that bit us

- She is a software engineer, not a physicist. Lead with the answer, plain English, analogies (chemical reaction,
  supercooled water, bonfire vs slush, stuck door). She wants to understand, not receive.
- **Rule changes after seeing data are proposed, never enacted by the assistant.** Lay out the options with
  consequences; she decides (`AskUserQuestion` works well). Then enact exactly what she chose and re-run.
- **Pre-register before running; commit the prediction first.** Disclose anything already seen at writing time.
- **Results are append-only.** Only `*.partial` may be deleted. Every CSV has a `.meta.json` — commit both.
- **Tests before every commit** (`pytest`, ~2–4 min). Commit messages end with
  `Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>`; PR descriptions end with
  `🤖 Generated with [Claude Code](https://claude.com/claude-code)`. Give her the compare URL
  (`https://github.com/EmilySmithCreate/RecreationalPhysics/compare/main...<branch>`); `gh` is not installed.
- **Branch from fresh `main` every time.** Stacked branches fall behind; after a PR merges, pushes to that branch
  go nowhere. She merges; the assistant never pushes to `main`.
- Commit and push on feature branches as work completes (she said "proceed"); confirm before anything
  hard to reverse or outward-facing.
- Report inconvenient results as prominently as convenient ones; own mistakes once, without over-apologising.

## 9. Environment gotchas

- Interpreter with numba: `C:\Users\emily\AppData\Local\Microsoft\WindowsApps\python.exe`. Bash's bare `python`
  lacks numba. Use the full path for `pytest` and runs.
- Background runs: `nohup <py> scripts/... > log 2>&1 &` from Bash; stdout is block-buffered — the runners print
  with `flush=True`, but progress is best read from `results/*.partial` line counts.
- Bash heredocs eat `\n` inside Python strings — write Python with the Write tool, not a heredoc.
- Windows `git status` was slow because of 1,665 loose objects and ~800 untracked npz files: `git gc` done,
  `core.untrackedCache` and `core.fscache` on. Result files are 17 MB tracked; no storage move needed.
- CRLF warnings on result CSVs are harmless.
- The previous assistant's auto-memory lived under a *different* working directory (`SideNerdDocs`); if this chat
  opened in `RecreationalPhysics`, that memory is not loaded. This document is the substitute.

## 10. Where things are

`VISION.md` (claims, Updates 1–19) · `TASKS.md` (task list; note the numbering map at the top: PREREGISTRATION's
T7/T8/T9/T10/T11 ≠ TASKS' T7/T8/T9) · `PREREGISTRATION.md` (T6–T13 with amendments, and T15 rung 0) · `ASSUMPTIONS.md`
(O1–O28 and Q-items) · `docs/parked/` (the menu study; the 2026-09-22 extension) · `docs/design/model_x_brief.md`,
`known_physics_plan.md`, `quantum_loop_design.md` · `docs/outreach/` (the note, the author's replies paraphrased, the
reply draft and its picture folder) · `scripts/analyse_*.py` (one verdict script per test, each a pure function of
parsed rows with known-answer tests in `tests/test_*.py`; `analyse_t13.py`, `analyse_t15_rung0.py` newest) ·
`scripts/compare_gate_b_gap.py` (prints only) · `terraform/`, `Dockerfile`, `docker/`, `.github/workflows/` (rented
compute, not applied) · `src/graphity/{cqg,sealed,dimension,wang_landau,tempering,connectivity,small_graphs}.py`.

# Start here: handoff for the next assistant (state as of 2026-09-22, evening)

Written for the AI assistant that opens this repository next. Emily is the owner; she will read it too.
Read it before `CLAUDE.md`'s "Known state" section, which is older than this page.

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

- Nothing. All runs of 22 September are complete and committed.

- `t6c_lam{1,125,15}_n{64,100}` (six jobs, slow): T6 λ ≥ 1 reruns with a trimmed 14-rung ladder. When
  `results/t6c_*.csv` exist (no `.partial`), run `python scripts/analyse_t6_phi.py t6c_lam1_n64` etc. If gate 4
  (round trips) is met, issue the λ ≥ 1 verdicts under criterion 3 *as enacted* (amendment 4). Expected: not first
  order (one hump); say so plainly and record it as O17.
- Nothing else. The laptop has 8 physical cores; do not run more than ~8 jobs.

*Update, evening:* nothing running. The `t7d_*` replays finished and are read.

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

## 6. Natural next lines (none started; pre-register before running)

0. **New, at Emily's request:** the known-physics ladder (`docs/design/known_physics_plan.md`, TASKS T13) and
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

`VISION.md` (claims, Updates 1–14) · `TASKS.md` (task list; note the numbering map at the top: PREREGISTRATION's
T7/T8/T9/T10/T11 ≠ TASKS' T7/T8/T9) · `PREREGISTRATION.md` (T6–T11 with amendments) · `ASSUMPTIONS.md` (O1–O16 and
Q-items) · `docs/parked/` (the menu study; the 2026-09-22 extension) · `docs/design/model_x_brief.md` ·
`scripts/analyse_*.py` (one verdict script per test, each a pure function of parsed rows with known-answer tests in
`tests/test_*_analysis.py`) · `src/graphity/{cqg,sealed,dimension,wang_landau,tempering,connectivity}.py`.

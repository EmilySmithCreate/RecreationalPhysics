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
| T6, λ ≥ 1 | Out of the random phase, with the rule on? | One hump at 36/64/100; any lump < 1.3/pt and shrinking; **no verdict yet** (gate 4 failed by diffusion; `t6c_*` reruns going) | O12 |
| T7, λ = 1.25 | Is the tube → sheet change sharp? | All three predictions hold at 4 sizes × 2 seed sets. **Verdict withheld**: gate 3 fails on 14 of 240 decays that had not settled at the 30,000-sweep cap. **Amendment 3 proposed, Emily deciding** | O13 + addendum |
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

## 4. Open decision for Emily (explain it to her if she has not answered)

**T7 amendment 3.** Under amendment 2 (enacted), every decay that *settled* passes gate 3; 14 of 240 were
cut off by the 30,000-sweep settle cap while still moving (`settle_sweeps = 30000` in `results/t7b_lam125_n*.csv`;
their seeds are in the `seed` column). Options: **(i)** replay those 14 seeds with the cap at 100,000 and apply
the gate as it stands — a run-length change, cannot manufacture a pass, recommended; **(ii)** gate only settled
decays and report the unsettled count, which must be a minority; **(iii)** leave the verdict withheld.
If (i): `scripts/run_tube_decay.py` needs a way to run a chosen replica list with a larger `settle_max`
(check its config keys first); write a config `t7c_*` naming the seeds; results under a new name.

## 5. What is running or queued

- `t6c_lam{1,125,15}_n{64,100}` (six jobs, slow): T6 λ ≥ 1 reruns with a trimmed 14-rung ladder. When
  `results/t6c_*.csv` exist (no `.partial`), run `python scripts/analyse_t6_phi.py t6c_lam1_n64` etc. If gate 4
  (round trips) is met, issue the λ ≥ 1 verdicts under criterion 3 *as enacted* (amendment 4). Expected: not first
  order (one hump); say so plainly and record it as O17.
- Nothing else. The laptop has 8 physical cores; do not run more than ~8 jobs.

## 6. Natural next lines (none started; pre-register before running)

1. T7 replays (if Emily chooses (i)).
2. Why one remnant per cold box — no hypothesis in hand after the seam refutation. A read of *what* the remnant is
   (its edges, its exact shape) would come before any new mechanism guess.
3. Step-4 items from Emily's parked extension (`docs/parked/extension_2026-09-22.md`): do remnants attract one
   another (readable from T9/T10 files: excess energy vs. separation); does a *local* spark on a flat sheet re-curl
   it or melt it (discriminates her black-hole picture from [T25]'s).
4. Where the metastable window closes between λ = 1.25 and 1.5 (PREREGISTRATION T8, the λ map).
5. Writing to the authors (both groups) — draft was given in chat only, never in the repo; VISION "Before anything
   is shown to anyone" lists the items. Then a physicist reader (S5).

## 7. The public-facing page

"The Shape of a Phase-Changing Reality", a claude.ai artifact owned by Emily:
https://claude.ai/artifact/TTC9knKGJFkR43X2JjsjZ5 — version 10, 31 sections, updated through T11. Written for a
non-scientist and a physicist reader. To update: `Artifact read` the URL (it saves the full HTML locally), edit,
republish with `url`. Its figures are published files alongside (kept on republish). Rules for it: every claim
says whose it is (the coloured boxes); no process narration (who reminded whom, when) — that goes in commits and
`ASSUMPTIONS.md`; lattice citations in section 1 are marked "to verify" and are not in `REFERENCES.bib`.

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

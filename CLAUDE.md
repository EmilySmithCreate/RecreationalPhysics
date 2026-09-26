# Project memory for Claude Code

Read this first, then **`docs/HANDOFF.md`** (the state as of 2026-09-22, the open decision, what is running, and the corrections that must not be undone — it is newer than the "Known state" section below). Then read @VISION.md (the fixed reference for what we are testing and why; Updates 13 and 14 are the current statement) and @TASKS.md (what to do next, in order). Read `ASSUMPTIONS.md` before touching any model code.

## What this project is

A hobbyist's hypothesis about emergent spacetime, tested honestly on toy models. The owner, Emily, is a software engineer, not a physicist. The work asks one question:

> When one specific, stable-for-now arrangement changes into another that looks like space, is the change sharp — a seed, a front, a definite lump of energy released — and what does the lump do when it has nowhere to go?

*(Re-scoped 2026-09-22, VISION Update 13. The earlier form of the question — whether geometry forms first order **out of a random network** — is the published question, was tested first (T6), and is not the hypothesis's: X is a specific arrangement, never a random tangle. The model's stand-in for X is the tube of VISION Update 8.)*

Current test bed: Trugenberger's 2D combinatorial quantum gravity model (`src/graphity/cqg.py`). Earlier work on Konopka's graphity model and a "restricted menu" idea is parked but kept (`energy.py`, `mc.py`, `graphs.py`, `docs/parked/`).

## Non-negotiable rules

1. **Every assumption has a source or is marked "Ours".** Add it to `ASSUMPTIONS.md` with a status (Sourced / Calibrated / Ours / Unverified) in the same commit as the code that relies on it. Cite section or equation numbers. Never invent a citation; if unsure of a detail, write "to verify".
2. **Reproduce before extending.** A published number or curve must be matched before any new result built on that code is interpreted. The gates are in `TASKS.md`. Do not skip or weaken a gate; if one fails, stop and report.
3. **No cherry-picking (VISION S1).** Parameter families are explored only along knobs fixed in advance, and every setting that was run is kept and reported.
4. **Pre-register.** Predictions and analysis choices are committed to `PREREGISTRATION.md` before the runs that test them. Exploratory runs are labelled exploratory in their config `_purpose` field and in any write-up.
5. **Results are append-only.** Never overwrite or delete files in `results/`. Every result comes from a config in `configs/` via a script in `scripts/`, with seeds in the config and a `.meta.json` beside the CSV. No hand-edited data. The runners refuse to overwrite; a `*.partial` file is scratch left by a crashed run and is the only thing in `results/` that may be deleted.
6. **Tests must pass** (`pytest`) before every commit. New kernels need: an independent brute-force check (networkx), an exactness check of incremental updates against full recomputation, constraint-preservation checks, and a same-seed reproducibility check.
7. **Say what is not known.** Distinguish measured, published, and guessed. Physics reasoning produced by an AI (including you) is unreviewed: label it "Ours, unverified". Do not describe a first look as a finding. Report inconvenient results as prominently as convenient ones.
8. **Plain language for the owner.** Explain results without jargon, define terms, lead with the answer, and push back when something does not hold up. She wants to understand the work, not just receive it.
9. **Do not drift.** A new idea goes to the parked list in `VISION.md` unless it bears on the working question. Changes to `VISION.md` are deliberate commits that say why.

## Commands

```bash
pip install -e ".[dev]"
pytest                                                        # all tests
python scripts/run_cqg_sweep.py configs/cqg_first_look.json   # ~3 min
python scripts/run_sweep.py configs/smoke_test.json           # parked Konopka model
```

## Code conventions

- Python 3.10+, NumPy, Numba for inner loops (`@njit(cache=True)`), networkx only for setup and tests.
- Graph state: `(N, degree)` int64 neighbour array; `-1` marks a temporarily empty slot during a move.
- `cqg.run_chain` returns `(S, X, acceptance)`: squares and surplus squares after each measurement sweep. H = 16(N − S) + 4λX. Its optional last argument `conn`, an `(n_meas, 4)` integer array, receives the connectivity numbers of `connectivity.py` (pieces, largest, vertices in baby universes, 4-cubes) without changing the chain.
- Monte Carlo moves must have a written detailed-balance argument in the module docstring.
- Source keys in comments (`[T25]`, `[KTB19]`, ...) match `REFERENCES.bib`, whose `note` fields record whether each paper was read in full, abstract only, or not at all.
- Keep modules small and readable; the owner must be able to follow every line.

## Known state (2026-09-22)

`docs/HANDOFF.md` is the one-page current state and is newer than this section; `ASSUMPTIONS.md` O1–O18 holds the numbers. What follows is what stays true.

**The kernel and the model.** `cqg.py` covers the whole λ line: `run_chain(..., lam, cap, glauber)` with `cap=CAP` (2) or `NO_CAP`; in a config, `"cap": null`, `"lambda"`, `"acceptance"`. The capped model is a published case ([KTB19] Sec. 4, Figs. 8 and 9; ASSUMPTIONS Q3) and is the λ → ∞ end of the knob; [T25] Eq. 22 is the soft penalty. A unit test pins the capped path bit for bit to its pre-T2 output. The energy (Q1), the hard-core rule (Q2) and the published hot-phase floor (O5: 0.126 is a formula, so our 0.120 at N = 160 is not a discrepancy) were checked against the sources directly.

**Gates.** Gate A passed (2026-09-20, owner's decision): at λ = 0 the jump, the hysteresis of about 2 in g and the shattering into baby universes appear at N = 64, 96, 160, with her wording "baby universes, reporting how many are 4-cubes". Gate B **cannot pass** against [T25] Fig. 3: we match it at both ends and differ by up to 0.41 between g = 2 and 6.3, while the same runs match [KTB19] Fig. 8a to rms 0.005, and the two published figures disagree with each other (0.62 against 0.99 at g = 5). The axis is log base 10, confirmed three ways; the owner's triangles-and-pentagons explanation was tested and ruled out. It is a question for the authors, not a bug hunt. Whether Fig. 8a should become the gate instead is her open decision.

**Pre-registered verdicts on the record** (`PREREGISTRATION.md`; details in O11–O17). T6 at λ = 0, the control: **FIRST ORDER**. T6 at λ = 1, 1.25, 1.5: **INCONCLUSIVE, final** by her decision, with one hump everywhere and any lump below 1.30 per point at N = 100 and falling. T7 (tube → sheet, λ = 1.25): **TWO-STATE CHANGE** at N = 64, 96, 192; N = 144 fails the energy gate on one decay. T9: **BONFIRE WITH A THRESHOLD**. T10: **ONE RING, HOWEVER LARGE**. T11: **NEITHER**. **Never present T7 as having cleared S2′**: that bar was written after four of its five parts were met (VISION, "What success means").

**Corrections that must not be undone.** The leftover is a **four-point remnant lying along the tube**, not a ring around it (O16); pre-registered verdict labels keep the word "ring", prose does not. Rarer resting states exist, 8 to 45 units, read from their wiring (O13, third addendum). Three times a shape has been named from a count and been wrong: **read positions before naming a geometry.** Never write "nobody has done this"; write "we have not found". The early-universe electroweak and QCD changes are **crossovers**, and freeze-out is not a phase transition: it is a precedent for claim 6, not claim 4.

**Never call the model's hot phase "X"** (owner's correction, 2026-09-20; VISION Update 5). X is a specific, relatively stable arrangement; the model's hot side is a random graph, a stand-in at best. Write "the random phase". The hypothesis's own route is order → order (the tube), and the disorder → order route is the published question (VISION Update 13).

**When reading papers, search the text; do not rely on a summary.** arXiv HTML converts to searchable text with formulas intact. Two published figures here use different log bases (natural in [KTB19] Fig. 8, base 10 in [T25] Fig. 3).

**Samplers.** Single chains freeze at low coupling (acceptance < 1 %): use `scripts/run_cqg_tempering.py`, trustworthy at N = 160 down to g of about 3, and always report `round_trips` and the spread between replicas. Flat-histogram sampling needs its frozen-weight second stage and must not be re-seeded in short blocks (Q14). Ergodicity is proved by exhaustive listing for N ≤ 18, with and without the cap, up to renaming within a side (Q9); the chain reproduces the exact averages at N = 16 and 18, and `scripts/exact_small_averages.py` is what any new sampler is validated against. `small_graphs.py` expects side 0 to be vertices 0..n−1 (`sides_first` converts a torus).

**Sealed machinery** (`src/graphity/sealed.py`, Q12). Energy is conserved to the last bit and the temperature is read off the bath rather than imposed. One spare-energy store cannot hold a lump, so the bath is C stores and C is a declared knob, scanned and not tuned. A tube with nothing to spare never converts; the spark that starts one is sharply 12 units at every size from N = 48 to 192.

**The dimension ladder and the design track** (VISION step 5, `docs/design/model_x_brief.md`). Dimension = the number of edge pairs at a vertex closing no square: sheet 2, tube 1, 4-cube 0. At λ > 1 the tube sits 4(λ − 1) per vertex above the sheet; below λ = 1 the ladder inverts and the mechanism runs the wrong way (space → knots). Exhaustive search at N = 18 finds dips above the flat ground state for 1 < λ < 1.6 and none above. A new knob needs a dated VISION decision before any run (S1). Rewarding any small loop more curls the network into closed pieces (Q10).

**A lesson worth keeping.** A threshold in energy *per vertex* is an absolute threshold proportional to N: that alone produced most of an apparent size effect (5.0σ before the correction, 2.9σ after). When comparing sizes, check whether the criterion itself scales.

**What the model says about gravity, dark energy and black holes** (added 2026-09-22; ASSUMPTIONS Q18, O20-O22). Two of these are exact and hold whatever the sampling: **zero is the floor** -- the hard-core rule forbids a triangle beside a square, so no valid arrangement sits below flat space and space is stable, not metastable; and **there is no long-range force between leftovers** -- H is a sum of per-edge terms, so defects sharing no square are exactly additive, with an attraction of 16 only where they touch. Anything like gravity here would have to be entropic. Two are exploratory: a sealed sheet given a budget of energy **melts rather than folds** at every budget and every lambda tried, though folding is four times cheaper per square; and a cold sheet, left alone, accepts no move at all. **Read O20's correction before quoting it:** melted is the random phase, which [T25] calls matter, and heating at equilibrium randomises by construction, so it is weaker evidence than it looks. The one route not yet tested is a **local** spark -- energy into one patch with cold space around it -- which needs a protocol that does not exist yet (T14) and is the next thing to build.

**Public-facing work.** The plain-language page and a draft post are in `docs/public/`; correspondence with physicists lives in `docs/outreach/`, which is **gitignored and local only** (this repository is public; never commit anything from it, and never quote or closely paraphrase a private email in a tracked file). Rules for the pages: every claim says whose it is, and no process narration.

## Disclosure

All code and documents so far were drafted with Claude (Anthropic) in conversation with the owner. Keep the disclosure section of the README accurate.

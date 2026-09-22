# Does space form in a sharp change?

Monte Carlo experiments on a published model of emergent geometry, testing one link in a personal
hypothesis: that our spacetime is a settled arrangement of something else, and that the change which
produced it was **first order** — sharp, with a bounded lump of energy released.

This is a hobby project by a software engineer, not a physicist. Every run is pre-registered or
labelled exploratory; every setting that was run is reported; no physicist has reviewed any of it.
Nothing here is a claim about the real universe. The plain-language version of this page is
[`docs/public/did-space-snap-open_v1.html`](docs/public/did-space-snap-open_v1.html).

| Read this | For |
|---|---|
| [`docs/HANDOFF.md`](docs/HANDOFF.md) | the current state in one page: verdicts, corrections that must not be undone, what is running |
| [`VISION.md`](VISION.md) | the six claims, the success conditions (S1–S5, S2′), how this differs from the published programme, and every decision with its date |
| [`PREREGISTRATION.md`](PREREGISTRATION.md) | what each test would measure and what each outcome would mean, committed before its runs, with dated amendments |
| [`ASSUMPTIONS.md`](ASSUMPTIONS.md) | every assumption with a source or marked "Ours"; the observation log O1–O18 with the numbers |
| [`TASKS.md`](TASKS.md) | what is next, with acceptance tests and the two reproduction gates |
| [`docs/design/known_physics_plan.md`](docs/design/known_physics_plan.md) | the ladder towards claim 2: dimension, a speed limit, defect interaction |
| [`REFERENCES.bib`](REFERENCES.bib) | sources, each marked read-in-full / abstract-only / unread |
| [`CLAUDE.md`](CLAUDE.md) | working rules for AI-assisted sessions |

## The model

2D combinatorial quantum gravity (Kelly, Trugenberger and Biancalana 2019; Trugenberger 2025).
States are 4-regular bipartite graphs on N vertices in which no two vertices share more than two
neighbours (the hard-core rule); moves are edge switches; the energy is

    H = 16 (N − S) + 4 λ X,     S = squares,  X = Σ_e (S_e − 2)₊

with λ the knob between the two published settings: λ = 0 is the global term alone (cold phase:
isolated 4-cubes and other "baby universes"), λ = 1 is the full Ollivier curvature (cold phase: a
flat sheet), and the hard cap of two squares per edge is the λ → ∞ end. Observables: φ = S/N, the
surplus X, the local dimension d(v) (2 = sheet, 1 = tube, 0 = knot), and connectivity.

The hypothesis's own change is **order → order**: a *tube* (a torus with one side curled to length
4, sitting 4(λ − 1) per vertex above the flat sheet at λ > 1) opening into the sheet. The published
question is **disorder → order**: geometry forming out of a random graph. Both are measured here;
they are not the same question (VISION Updates 5 and 13).

## What has been done and tested

Pre-registered verdicts are in `PREREGISTRATION.md`; the numbers behind each are in `ASSUMPTIONS.md`.

| Test | Question | What was run | Verdict |
|---|---|---|---|
| **Gate A** | Does our kernel reproduce the published λ = 0 behaviour? | cooling/heating at N = 64, 96, 160 | **Passed**: jump 0.65 → 1.46, hysteresis ≈ 2 in g, cold phase ≈ N/16 baby universes (84–95 % of vertices) |
| **Gate B** | Does it reproduce Trugenberger (2025) Fig. 3 at N = 160? | both published variants, tempered | **Not reproduced**: agreement at both ends, up to 0.41 apart between g ≈ 2 and 6.3. The same runs match Kelly et al. (2019) Fig. 8a to rms 0.005, and the two published figures disagree with each other (0.62 vs 0.99 at g = 5). An open question for the authors, not a bug |
| **T4** ergodicity | Do the moves reach every state? | exhaustive enumeration, N ≤ 18 (1,785,021,235,200 labelled states at N = 18) | Switch moves connect every class, with and without the cap; exact averages reproduced. Unproven above N = 18 |
| **T5** tempering | Can the cold side be sampled? | N = 18 (vs exact), then N = 160 | Trustworthy down to g ≈ 3, where a single chain stopped at g ≈ 5 |
| **T6 control** (λ = 0) | Is the disorder → order change first order where it is known to be? | flat-histogram walks along φ, N = 48, 64, 96 | **FIRST ORDER**: latent heat 10.32 / 11.27 / 12.50 per point, barrier growing at 34 σ. Criterion 3 had to be repaired (it could never have returned "first order" here); the repair is recorded beside the verdict |
| **T6** (λ = 1, 1.25, 1.5) | Same question where the cold phase is a sheet | tempering along φ, N = 36, 64, 100, 4 replicas | **INCONCLUSIVE, final** (the author's decision): one hump at every λ, size and replica; any latent heat below 1.30 / 1.28 / 1.26 per point at N = 100 and falling. Criterion 3 cannot be read where the cold phase sits at H = 0, and the φ-cumulant replacement reads the hot edge instead of the transition |
| **T7** (λ = 1.25) | Is the tube → sheet change sharp? | 4 sizes × 2 seed sets × 30 decays, N = 64–192 | **TWO-STATE CHANGE** at N = 64, 96, 192: memoryless waits (CV 0.76–1.19), ≥ 98.8 % of vertices at d ∈ {1,2} at half conversion, converted region 85–99 % in one front, exactly 4(λ − 1) released, in two sharp steps via a 14-unit four-point remnant. N = 144 fails the energy gate on one decay |
| **T9** sealed | Bonfire, boil-off or slush? | 3 sizes × 7 bath sizes × 20 runs = 420 | **BONFIRE WITH A THRESHOLD**: 179 clean sheets, 154 melted, 87 in between, **0 slush**; crossover C* ∈ (N/4, N/2] at every size against a predicted N/3.5; energy conserved to the last unit in all 420 |
| **T10** leftover | Does the leftover grow with the space? | N = 64–288, fresh seeds, 80 runs | **ONE RING, HOWEVER LARGE**: 0.85–1.05 per box, slope indistinguishable from zero. The committed prediction failed |
| **T11** seam | Is the leftover where the front's two ends meet? | N = 64, 96, 70 boxes | **NEITHER**: its position is indistinguishable from uniform. Why exactly one is open |

Exploratory, and labelled so (`ASSUMPTIONS.md` section D and O1–O18): the Arrhenius waiting time
(measured/predicted 0.98 over a ninetyfold range, nothing fitted); the 12-unit spark threshold, the
same at N = 48–192; the leftover fixed by the energy released (predicted from a separate equilibrium
curve, matched to 0.003); labelled-vs-unlabelled counting (exact at N = 16, 18); and where the
released energy sits in the sealed end states (O18).

Two findings of our own, checked by computer and unreviewed: a **14-vertex baby universe** (the
incidence graph of the 7-point biplane) that ties with the 4-cube in energy at every λ, and a
**30-vertex closed piece** with H = 0 under the published prices for triangles and pentagons.

## What it adds up to

| Claim (VISION) | Status in the model |
|---|---|
| 1 — space is a settled arrangement of something deeper | Holds: geometry appears with nothing put in by hand; published work agrees |
| 2 — known physics comes back out | Untested: no time, no quantum behaviour. The ladder is planned in `docs/design/known_physics_plan.md` |
| 3 — X and space are two arrangements of one thing | Holds: sheet, tube and knot are the same edges rewired |
| 4 — the change was sharp, releasing a lump | Split by route: **not sharp** out of disorder at N ≤ 100 (bound < 1.3/point, falling); **sharp** from one order to another (T7). S2′ was written after four of its five parts were met, so T7 does not count as clearing it |
| 5 — a leftover remains | Holds, but small: one four-point remnant per box however large. The author's hypothesis that it is dark matter is recorded in VISION Update 16 and tested by TASKS T14 |
| 6 — the books balance | Holds by construction, and the construction survived 420 sealed conversions |

**Open decisions and gaps:** whether Kelly et al. (2019) Fig. 8a should replace Trugenberger (2025)
Fig. 3 as Gate B; where the metastable window closes between λ = 1.25 and 1.5; why a cold box ends
with exactly one remnant; and S5 — no physicist has read any of this. A draft note to the model's
authors is in [`docs/outreach/`](docs/outreach/note_to_model_authors.md).

## Run it

```bash
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
pytest                                                          # 156 tests, about 90 s
python scripts/run_cqg_sweep.py configs/cqg_first_look.json     # about 3 minutes
```

Then the pre-registered measurements, each `run` followed by its `analyse`:

```bash
python scripts/run_tube_decay.py   configs/t7b_lam125_n64.json  # T7: does the tube open sharply?
python scripts/analyse_t7.py       lam125 t7b t7c t7d
python scripts/run_sealed_tube.py  configs/t9_n64_CN.json       # T9: bonfire or slush?
python scripts/analyse_t9.py
python scripts/run_t6_tempering.py configs/t6c_lam125_n64.json  # T6: one hump or two?
python scripts/analyse_t6_phi.py   t6c_lam125_n64
```

Outputs: `results/<name>.csv` and `results/<name>.meta.json` (config, seeds, package versions). A
runner refuses to start if its output exists; while a run is in progress its rows go to
`<name>.csv.partial`. Re-running `configs/cqg_first_look.json` on a second machine (Windows against
Linux) reproduced its CSV byte for byte.

## Reproducibility rules

1. Every number comes from a config in `configs/` and a script in `scripts/`. No hand-edited data.
2. Seeds live in the config. Results are append-only, and the runners enforce it (`results.py`).
3. Predictions are committed to `PREREGISTRATION.md` before the runs that test them; amendments are
   dated, the original is left standing, and any rule changed after seeing data says so beside its
   verdict.
4. Whole parameter maps are published, not selected members.
5. Every analysis script that issues a verdict has known-answer tests (`tests/test_*_analysis.py`,
   `tests/test_t6_phi_binder.py`, `tests/test_t7_states.py`).

## Layout

```
src/graphity/cqg.py            the kernel: switch moves, energy, torus and melt starts
src/graphity/dimension.py      local dimension d(v) and the pieces of a chosen set of vertices
src/graphity/connectivity.py   connected pieces, baby universes, 4-cubes
src/graphity/squares.py        the two smallest graph readers, shared by the modules above
src/graphity/small_graphs.py   every state at N ≤ 18: ergodicity and exact averages
src/graphity/tempering.py      parallel tempering across the coupling ladder
src/graphity/wang_landau.py    flat-histogram sampling, with the frozen-weight second stage
src/graphity/wl_ising.py       the 4×4 Ising check with an exactly known answer
src/graphity/sealed.py         sealed and leaky runs: a demon, or a bath of C stores
src/graphity/full_curvature.py slow exact reference with triangles and pentagons allowed
src/graphity/analysis.py       fluctuations, block bootstrap, autocorrelation time
src/graphity/results.py        result writer that never overwrites
src/graphity/{energy,mc,graphs}.py   parked: the Konopka graphity study
scripts/                       44 runners, analysers and plotters; one analyse_* per pre-registered test
configs/                       92 experiment definitions, each with its seeds and a _purpose
results/                       outputs, append-only
tests/                         156 tests
docs/HANDOFF.md                start here for the current state
docs/design/                   the model-X brief and the known-physics plan
docs/public/                   the plain-language write-up and a draft post
docs/outreach/                 draft note to the model's authors
docs/parked/                   the menu study and the cosmological extension
docs/reading/                  walkthroughs of the sources (PDFs are local, not committed)
docs/figures/                  figures, each made by a scripts/plot_*.py
docs/published/                points digitised from published figures
```

## Limits

Toy sizes: at most 288 points, and the size comparisons reach 96 (disorder → order) and 192 (the
tube). The stand-in for X is a curled sheet, chosen by us; nothing here says X is a tube. Matter,
time and quantum behaviour are out of reach. One success condition (S2′) was written after the runs
that met most of it. Two pre-written rules had to be corrected after seeing the data they judged.
No physicist has reviewed any of it.

## Licence

MIT (see [`LICENSE`](LICENSE)). Anyone may use, copy, change and share the code and the documents,
for any purpose, provided the copyright notice stays with them. There is no warranty.

## Contributing

Pull requests are welcome from anyone. Only the owner merges into `main`. A pull request needs to
pass the tests (they run on every pull request) and follow [`CLAUDE.md`](CLAUDE.md): every
assumption sourced or marked "Ours", nothing in `results/` overwritten, and nothing described as a
finding before its gate has passed.

## Disclosure

Code and documents were drafted with Claude (Anthropic) in conversation with the author. Physics
arguments marked "Ours" in `ASSUMPTIONS.md` have not been reviewed by a physicist.

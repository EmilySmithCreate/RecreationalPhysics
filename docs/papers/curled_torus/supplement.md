# Supplemental methods and reproducibility

**The curled torus burps: activated escape and conversion in a graph model of emergent geometry**

Emily Smith · 9 October 2026

This supplement gives computational certificates, sampling details, uncertainty estimates and a map from claims to code and data. Calculations beyond the cited literature are the author's, computer-checked and not independently reviewed by a physicist. The analyses below use existing trajectories; none changes the recorded data or the prespecified tests.

The source-data snapshot is [RecreationalPhysics commit 40b1ae68844a72bd73ffdc74d5c385844ab16f17](https://github.com/EmilySmithCreate/RecreationalPhysics/tree/40b1ae68844a72bd73ffdc74d5c385844ab16f17). The accompanying `release_manifest.json` gives SHA-256 hashes of the manuscript, figures, PDF, abstract, analysis code and check outputs. Text files use UTF-8/LF. Configuration metadata contain seeds and software versions but do not consistently identify the original execution commit.

## Neutral-basin certificate

`scripts/analyse_curled_revision.py --neutral` starts from a perfect 4×(N/4) torus. It enumerates every valid switch from each representative and groups neutral targets by side-preserving graph isomorphism, using igraph's canonical labelling. Newly discovered classes enter a breadth-first queue. The queue empties only after every neutral target maps to an enumerated class. Relabelling maps switches bijectively, so a complete census per class certifies closure of the reachable quotient.

At lambda=1.25, every energy-neutral switch is checked to have (Delta S, Delta X)=(0,0); no additional zero-energy channel is omitted. All nonneutral costs are positive, with minimum 12. Nonnegative stores holding a total budget below 12 can therefore support neutral moves but cannot leave this basin. The certificate depends on the enumerator and isomorphism implementation; it is not a general theorem for arbitrary N.

| N | Reachable classes | Side-preserving symmetry orders | Minimum exit cost | Distinct full censuses |
|---|---:|---|---:|---:|
| 48 | 3 | 48, 96, 96 | 12 | 1 |
| 64 | 3 | 64, 128, 128 | 12 | 1 |
| 96 | 3 | 96, 192, 192 | 12 | 1 |
| 144 | 3 | 144, 288, 288 | 12 | 1 |
| 192 | 3 | 192, 384, 384 | 12 | 1 |
| 288 | 3 | 288, 576, 576 | 12 | 1 |

The smaller N=32 control has three neutral classes but more than one full census. This explicitly limits extrapolation of full-hazard invariance. The test suite includes this boundary case.

The A+B expression approximates the total hazard. At N=192, lambda=1.25, g=1.5, other moves add 0.8846% to the A+B rate. `neutral_closure_2026-10-09.log` records full-hazard checks; the supplied independent census output is in `reviewer_checks_2026-10-09.log`. With constant hazard p per attempt, the exact waiting law is geometric and its mean is 1/(2Np) sweeps.

## Small-system minima and endpoint geometry

The independent check script exhausts the 26 N=18 classes and solves affine single-move inequalities on lambda≥1. The strict above-ground minima are (S,X)=(21,12) on 1<lambda<8/5 and (22,16) on 1<lambda<4/3. These are open intervals; a zero-cost switch violates strictness.

The square-complex reader fills every four-cycle, checks that each edge has two incident faces and every vertex link is cyclic, and then checks connectedness, orientability and Euler characteristic. All 120 T8 lambda=1.05 endpoints are connected closed orientable surfaces with Euler characteristic zero, hence tori. Tests use a known 6×6 flat torus, a curled 4×16 graph and a disconnected union of two flat tori. The disconnected control is locally a surface but is not one torus.

These checks do not measure noncontractible cycle lengths, aspect ratios or the scaling of both periods with N. They do not certify the topology of every other dataset. The same reader reproduces a valid d=2 witness with incident edge square counts [1,2,2,3], demonstrating why a local count alone is insufficient.

## Detector behavior and event counts

T38 uses w′=W−200, scale tau_hat=median(w′)/ln 2, and the count k10 above 10 tau_hat. Its prespecified rule is TAIL for k10≥3, NO TAIL for k10≤1, UNCLEAR otherwise; two TAIL cells yield the classification TWO POPULATIONS.

| lambda | N | Total rows | Detector crossings | Missing crossings | k10 | Cell result |
|---|---:|---:|---:|---:|---:|---|
| 1.25 | 64 | 4000 | 3942 | 58 | 2 | UNCLEAR |
| 1.25 | 192 | 1000 | 1000 | 0 | 1 | NO TAIL |
| 1.30 | 64 | 4000 | 3868 | 132 | 14 | TAIL |
| 1.30 | 192 | 1000 | 1000 | 0 | 5 | TAIL |

All 190 missing detector crossings reach f≥0.75. They are therefore not ordinary censored long survivors. The reported tail statistic excludes these rows. At T8 lambda=1.30 and 1.35, respectively 118 and 117 of 120 runs have detector crossings, while all reach half and three-quarter conversion.

No `results/t38_*_waiting/*.npz` files exist in the frozen snapshot. Final states cannot reconstruct those waiting histories. Detector effects, repeated failed growth and additional traps cannot be distinguished decisively from these files. A future attempt-resolved experiment should record the first exit, every return, commitment, threshold history and missing events jointly, under prespecified tail tests.

T22 observes all 240 first exits, but only 239 runs reach f≥0.25 before the cap. First-exit means and intervals include all observed exits; the reciprocal-exit statistic uses completed runs. For example, the N=96, lambda=1.05 first-exit mean is about 9302; restricting it to committed runs would instead give about 7485. These samples answer different questions.

## Replica uncertainty and random streams

Replicas are the independent units within a setting. The analysis uses exact 95% Clopper–Pearson intervals for binomial outcomes, 10,000 whole-replica bootstrap resamples with seed 20261009 for means, and chi-square intervals for complete first-exit means conditional on a continuous exponential model. These interval calculations are exploratory. Per-size release intervals are given; pooled binomial intervals are nominal reference intervals assuming a common success probability across the pooled sizes.

The exploratory Arrhenius scan reuses each replica's random seed across couplings. Its pooled bootstrap simulates cells independently and does not reproduce that cross-cell dependence; the 432-wait p=0.53 is nominal. The T22 runner includes lambda in its seed derivation. Its 240 attempt-counted exits provide the direct comparison with the first-exit model. The exploratory budget scan also reuses streams across budgets, so its binomial intervals apply to each individual setting, not a pooled set of independent budget experiments.

| N | T7b largest-component mean | 95% replica-bootstrap interval | Individual replicas below 0.7 / 30 |
|---|---:|---|---:|
| 64 | 0.9944 | [0.9833, 1.0000] | 0 |
| 96 | 0.9606 | [0.9283, 0.9863] | 1 |
| 144 | 0.9551 | [0.9064, 0.9948] | 3 |
| 192 | 0.9219 | [0.8635, 0.9713] | 5 |

The median is one in each cell. A passing cell mean therefore does not establish a single dominant region in every replica, nor does it establish a unique seed or interface. Signature intervals, component extrema, observed-event denominators, release counts and bath proxies are in `revision_analysis_2026-10-09.log`.

## Reservoir model

At lambda=1.25, Delta H=−16 Delta S+5 Delta X is integral. The initial T9 stores contain 0 or 12. Valid move costs 12 and 25 have gcd 1, ruling out a coarser common energy increment but not proving accessibility or mixing over all allocations.

Conditional on a canonical distribution over levels 0,delta,2delta,..., the mean is u_D(g)=delta/expm1(delta/g). With delta=1, u_D(3.5)=3.023777. Energy balance gives C*≈[epsilon N+s−U_graph(g_m)]/u_D(g_m). Neglecting the seed and residual graph energy gives N/3.024, an approximate scale rather than a calibrated crossover.

On the T9 grid, the majority-sheet criterion changes between C=N/4 and N/2 at all tested sizes. Recorded conservation drift is zero. The CSV column `bath_T` is raw mean store energy. Conditional discrete-coupling proxies in T10 span 0.8406–1.0128. Individual store histograms were not saved, so a canonical thermometer calibration cannot be established from these data.

## Analysis design

Waiting and morphology component tests and the dedicated tail-count rule were specified before the corresponding runs. Endpoint-energy criteria were partly developed after inspection, so endpoint energy classification is exploratory. The three map protocols have distinct combined acceptance criteria and all return INCONCLUSIVE. Their complete definitions, amendments and cell outcomes are preserved in `PREREGISTRATION.md` and the experiment analyzers. The paper does not promote a component success, graph-validity check or retrospective diagnostic to a successful combined confirmation.

The topology and neutral-closure certificates are finite computational statements; they do not acquire stronger scope from being computed after data. The stated size limits, independent controls and complete censuses determine their scope.

## Claim-to-evidence map

Paths are relative to the repository root. Experiment identifiers provide stable links to configurations; the reader need not reconstruct the sequence of drafts.

| Result | Code | Configuration / data |
|---|---|---|
| Energy and N=18 inequalities | `src/graphity/cqg.py`, `src/graphity/small_graphs.py`, independent check script in this directory | Exact enumeration; `reviewer_checks_2026-10-09.log` |
| Exit channels and corrections | `scripts/exact_torus_level.py` | Conditions in script; independent census log |
| Neutral closure | `scripts/analyse_curled_revision.py --neutral` | Fixed sizes in script; `neutral_closure_2026-10-09.log` |
| Arrhenius scan / Fig. 2a | `scripts/run_waiting_time.py`, `scripts/plot_paper_fig1.py` | `configs/cqg_tube_arrhenius_lam125.json`; matching result CSV |
| T7 morphology | `scripts/run_tube_decay.py`, `scripts/plot_paper_fig1.py` | `configs/t7*_lam125_n*.json`; matching CSVs |
| T8 map / Fig. 3 | `scripts/analyse_t8.py`, `scripts/plot_paper_fig_lambda.py` | `configs/t8_lam*.json`; matching CSVs; T7b at lambda=1.25 |
| Torus endpoints | Independent check script in this directory | `results/t8_lam105_adj/*.npz`, 120 graphs |
| Seed budget | `scripts/run_spark_threshold.py` | `configs/cqg_spark_threshold_lam125.json`; matching CSV |
| Reservoir products | `scripts/run_sealed_tube.py`, `scripts/analyse_t9.py`, supplementary analysis | `configs/t9_n*_C*.json`; matching CSVs |
| Cold relics | `scripts/analyse_t10.py`, supplementary analysis | `configs/t10_n*.json`; matching CSVs |
| First exits / returns | `scripts/run_exits.py`, `scripts/analyse_t22.py`, supplementary analysis | `configs/t22_exits_*.json`; matching CSVs |
| 120-run maps | `scripts/analyse_t23.py`, `scripts/analyse_t24.py` | `configs/t23_*.json`, `configs/t24_*.json`; CSVs and T24 endpoint graphs |
| Dedicated tail test | `scripts/analyse_t38.py` | `configs/t38_*.json`; matching CSVs; `t38_audit_2026-10-09.log` |
| Pooled distributions / positions | `scripts/analyse_paper_stats.py` | T7, T8, T11, T22; `paper_stats_2026-10-09.log` |
| Intervals / event counts / bath proxies | `scripts/analyse_curled_revision.py` | `revision_analysis_2026-10-09.log` |
| Schematic / Fig. 1 | `scripts/plot_paper_fig_tori.py` | Drawing only, not a measured interface |

## Reproduction

Install the project's `dev` and `plots` dependencies and Tectonic. From the repository root:

```text
python docs/papers/curled_torus/reviewer_checks_2026-10-09.py
python scripts/analyse_curled_revision.py --neutral
python scripts/analyse_curled_revision.py
python scripts/analyse_paper_stats.py
python scripts/analyse_t38.py
python -m pytest -q
python scripts/build_curled_paper.py --tectonic /path/to/tectonic
```

The build regenerates the three figures, synchronizes the abstract directly from TeX, checks references and layout, compiles the PDF and writes the release manifest. Validation outputs accompany the package. The simulations remain reproducible through the frozen configurations and their recorded seeds, subject to the stated execution-provenance limitation.

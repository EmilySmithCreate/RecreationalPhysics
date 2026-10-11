# Curled-torus revision supplement — 9 October 2026

This is the audit trail accompanying the revised paper. New reasoning and retrospective analyses are **Ours, unverified by an independent physicist**. Computational agreement is not peer review. No production simulations were rerun, no files in `results/` were changed, and no historical verdict was rescored.

The starting source and data snapshot is **40b1ae68844a72bd73ffdc74d5c385844ab16f17**, fetched from `origin/main`. Work is on `review/curled-torus-feedback-2026-10-09`. The original feedback and reviewer script are retained unchanged. The release manifest identifies revised source, scripts, figures, PDF, abstract and check outputs by SHA-256; it deliberately does not claim that the historical metadata identify every original execution commit.

## Response to the review

| Review point | Assessment and incorporated change |
|---|---|
| 1. Demon thermometer | Agree. The raw `bath_T` is mean store energy. Derived the geometric-level inversion, reported it only conditionally, corrected the helper's quarter-integer comment, and replaced N/3.5 by the energy-balance formula. No evidence of equilibration or a full accessible spectrum is invented. |
| 2. Counting versus geometry | Agree; the supplied counterexample reproduces. Added d=6−q and f=mean(d)−1. Replaced claims of certified order by counting signatures and corrected figure labels. |
| 3. Decompactification and topology | Agree. All 120 T8 lambda=1.05 endpoints pass the independent surface certificate. Limited topology statements to those endpoints; withdrew claims of macroscopic opening of both periods. |
| 4. Single front | Agree. Retained the original component statistic, added replica distributions and uncertainty, and explicitly reported multiple early patches and the failed T12 test. |
| 5. Stopping times | Agree. Added a clock/observable table. First exits, commitment, detector crossings and conversion snapshots have separate definitions. The reciprocal exit count is not claimed as a derived transmission coefficient. |
| 6. Long tails | Agree with the criticism, but the review missed the completed **T38 TWO POPULATIONS** result recorded in O84. Added it and its denominators. The physical mechanism remains unresolved. |
| 7. Recording floor | Agree. The dashed curve is an idealized floor, not the full detector. Distinguished E[max(T,a)] from E[T given T>a], selection and threshold contamination. |
| 8. Persistence boundary | Agree. The 200-sweep boundary is operational, not an energetic spinodal. Reproduced the exact N=18 inequality intervals. |
| 9. Symmetry weighting | Agree. Put the symmetry ratio inside the Metropolis–Hastings minimum; corrected the free-energy increment to g log(cN). Removed the quantum-multigraph citation as justification for a classical weighting choice. No alternative-ensemble lifetime is inferred. |
| 10. Energy release | Agree. Q=epsilon N−H_f, and window averages differ from final graph energies. Corrected the broader lambda=1 claim and the plotting label “flat”, which was actually an energy-window criterion. |
| 11. Neutral closure | Agree that the sampled walk was insufficient. A new exhaustive quotient enumeration closes this gap at each listed size; it does not prove an arbitrary-size theorem. |
| 12. Seed localization | Agree. The seed is globally available energy. **Additional correction:** the scan's `left` flag records departure from initial (S,X), not completed conversion. Reported 8/8 as escape, with duration, grid and binomial interval. |
| 13. Ensemble and coexistence | Agree. Conservation is for graph plus stores. Added bath multiplicity and accessibility caveats; removed an equilibrium coexistence inference. |
| 14. Registration and uncertainty | Agree. Added the chronology, preserved failures, distinguished retrospective energy amendments and fresh repeats, and calculated replica-level intervals. |
| Smaller corrections | Defined ensemble, coupling, normalization, domain and protocols; added the dedicated dated prior-work note and frozen evidence map; synchronized the abstract and regenerated figures/PDF. |

## Stronger exact finite-size evidence

`python scripts/analyse_curled_revision.py --neutral` starts from a perfect 4×(N/4) torus. For each representative it enumerates **every** valid switch and groups neutral targets by side-preserving graph isomorphism using igraph's canonical labelling. New classes enter a breadth-first queue; completion means every neutral target maps to an already enumerated class. Relabelling maps switches bijectively, so one full census per class suffices for closure of this reachable quotient.

At lambda=1.25, it also checks that every zero-energy move has (Delta S, Delta X)=(0,0); no other zero-energy channel is omitted. All nonneutral costs are positive with minimum 12. Consequently, a nonnegative bath of total energy below 12 can execute neutral moves but cannot leave this basin. This is a computational certificate conditional on the enumerator and isomorphism implementation, with independent existing kernel/isomorphism tests; it is not a hand proof for arbitrary N.

| N | Classes | Side-preserving symmetry orders | Minimum exit cost | Distinct full censuses |
|---|---:|---|---:|---:|
| 48 | 3 | 48, 96, 96 | 12 | 1 |
| 64 | 3 | 64, 128, 128 | 12 | 1 |
| 96 | 3 | 96, 192, 192 | 12 | 1 |
| 144 | 3 | 144, 288, 288 | 12 | 1 |
| 192 | 3 | 192, 384, 384 | 12 | 1 |
| 288 | 3 | 288, 576, 576 | 12 | 1 |

The A+B prediction remains an approximation to the **total** hazard. For example, at N=192, lambda=1.25, g=1.5, other moves add 0.8846% to the A+B rate. The new certificate preserves the full census rather than only A and B. For a constant hazard p per attempt, the exact law is geometric and the mean is 1/(2Np) sweeps.

The reviewer script independently reproduces the N=18 strict-minimum intervals: (S,X)=(21,12) on (1,8/5), and (22,16) on (1,4/3). Its topology reader fills every square and checks links, edge incidences, orientability, connectedness and Euler characteristic; all 120 lambda=1.05 endpoints certify tori. Tests use a known 6×6 torus, a curled 4×16 graph and a disconnected union of two flat tori as controls. Periods and aspect ratios remain unmeasured.

## Detector audit and selection

The completed T38 analysis reproduces O84's **TWO POPULATIONS** label. Its rule, based on a median-derived scale and tail counts, is not an independently calibrated test identifying two physical states.

| lambda | N | Total rows | Detector crossings | Missing crossings | Tail count | Registered cell result |
|---|---:|---:|---:|---:|---:|---|
| 1.25 | 64 | 4000 | 3942 | 58 | 2 | UNCLEAR |
| 1.25 | 192 | 1000 | 1000 | 0 | 1 | NO TAIL |
| 1.30 | 64 | 4000 | 3868 | 132 | 14 | TAIL |
| 1.30 | 192 | 1000 | 1000 | 0 | 5 | TAIL |

All 190 missing crossings reach at least f=0.75. Thus missing W is not equivalent to a right-censored long wait; conversion can complete without this detector firing. The historical analyzer drops these rows. Saved time histories are needed to distinguish threshold contamination from the physical route. No `results/t38_*_waiting/*.npz` files exist in the frozen snapshot, despite the configured snapshot protocol. The paper reports that absence rather than implying that waiting graphs have been audited.

At T8 lambda=1.30 and 1.35 there are likewise only 118 and 117 detected waits among 120 runs, although all reach half and three-quarter conversion. T22 has all 240 first exits but only 239 commitment events; the first-exit intervals include **every** observed first exit, while the reciprocal-exit statistic retains the historical completed-run selection. The lambda=1.05, N=96 first-exit mean is therefore about 9302, not the approximately 7485 obtained by restricting it to completed runs.

**Previous claim → failure → replacement → falsification test:** a common exponential clock for all waits → detector omissions and T24/T38 tail failures → the first-exit calculation is supported while detected conversion has unresolved tails → a fresh prespecified attempt-resolved study must jointly record first exit, returns, commitment, the threshold history and missing events. No new mechanism or adjustable kinetic parameter is proposed in this revision.

## Reservoir correction

At lambda=1.25, Delta H=−16 Delta S+5 Delta X and initially integer stores stay integral. Valid costs 12 and 25 establish gcd 1 for the observed allowed increments, but do not prove mixing over every bath allocation. The geometric-level model with delta=1 gives mean energy 3.023777 at g=3.5. Conservation gives the conditional estimate C*≈[epsilon N+s−U_graph(g_m)]/u_D(g_m). The simpler N/3.024 neglects seed and residual graph energy and is explicitly approximate.

The T9 original grid shows the majority-sheet crossover between C=N/4 and N/2 at the tested sizes, unchanged by relabelling the thermometer. Drift is recorded as zero in all T9 runs. The discrete coupling proxies in T10 span 0.8406–1.0128, so the old “below g=1” reading is not universally true even if canonical equilibration were assumed. Historical tests remain available and their labels unchanged; the paper withdraws their uncalibrated thermodynamic interpretation. No individual demon energy distributions were stored, so those data cannot establish a canonical thermometer calibration.

## Uncertainty

`revision_analysis_2026-10-09.log` contains counts, exclusions, replica-bootstrap intervals for signature/component means, component min/median/max and individual failures, exact binomial intervals for release and reservoir criteria, and continuous-exponential-model intervals for first-exit means. These are retrospective, not replacements for registered tests. Binomial intervals describe repeated runs at the stated settings; pooled release fractions average the stated sizes and are not an asymptotic population claim. The script keeps first-exit samples separate from commitment-selected samples.

At half conversion in T7b, 0, 1, 3 and 5 of 30 replicas at N=64,96,144,192 individually have largest-component fraction below 0.7, despite all four cell means passing. This directly illustrates why the original average does not establish one front in every run.

## Claim-to-evidence map

Paths are relative to the repository root. Configurations and raw data are in the frozen base snapshot; the new analysis and revised figure scripts are identified in the release manifest.

| Claim or figure | Script / code | Configurations | Data / output |
|---|---|---|---|
| Energy and ideal counts | `src/graphity/cqg.py`; reviewer checks | Exact calculation, no simulation config | `reviewer_checks_2026-10-09.log` |
| N=18 strict minima | reviewer checks; `src/graphity/small_graphs.py` | Exhaustive inequalities lambda≥1 | Same log |
| A/B and omitted moves | `scripts/exact_torus_level.py` | Conditions listed in that script | Reviewer log; `neutral_closure_2026-10-09.log` |
| Neutral-basin certificate | `scripts/analyse_curled_revision.py --neutral` | Fixed sizes in script | `neutral_closure_2026-10-09.log` |
| T7 morphology / Fig. 2 | `scripts/run_tube_decay.py`, `scripts/plot_paper_fig1.py` | `configs/t7*_lam125_n*.json` | `results/t7*_lam125_n*.csv` |
| Arrhenius panel | `scripts/plot_paper_fig1.py` | `configs/cqg_tube_arrhenius_lam125.json` | `results/cqg_tube_arrhenius_lam125.csv` |
| T8 map / Fig. 3 | `scripts/plot_paper_fig_lambda.py`, `scripts/analyse_t8.py` | `configs/t8_lam*.json` | `results/t8_lam*.csv`, plus T7b at 1.25 |
| Endpoint torus certificate | `reviewer_checks_2026-10-09.py` | T8 lambda=1.05 | `results/t8_lam105_adj/*.npz` (120 graphs) |
| Seed threshold | `scripts/run_spark_threshold.py` | `configs/cqg_spark_threshold_lam125.json` | `results/cqg_spark_threshold_lam125.csv` |
| Reservoir product | `scripts/run_sealed_tube.py`, `scripts/analyse_t9.py` (historical), new revision analysis | `configs/t9_n*_C*.json` | `results/t9_n*_C*.csv` |
| Cold relics | `scripts/analyse_t10.py` (historical), new revision analysis | `configs/t10_n*.json` | `results/t10_n*.csv` |
| First exits / fallbacks | `scripts/analyse_t22.py`, new revision analysis | `configs/t22_exits_*.json` | `results/t22_exits_*.csv` |
| Repeated maps | `scripts/analyse_t23.py`, `scripts/analyse_t24.py` | `configs/t23_*.json`, `configs/t24_*.json` | Matching CSVs and T24 `_adj` directories |
| T38 tail test | `scripts/analyse_t38.py`, new revision analysis | `configs/t38_*.json` | `results/t38_*.csv`; `t38_audit_2026-10-09.log` |
| Pooled distribution / positions | `scripts/analyse_paper_stats.py` | Bootstrap and permutation choices in script | T7, T8, T11, T22; `paper_stats_2026-10-09.log` |
| Uncertainty / denominators / bath proxies | `scripts/analyse_curled_revision.py` | Retrospective fixed bootstrap seed in script | `revision_analysis_2026-10-09.log` |
| Schematic / Fig. 1 | `scripts/plot_paper_fig_tori.py` | Drawing only | `fig_tori.pdf`; explicitly not a measured interface |

## Reproduce and build

Use Python with the project's `dev` and `plots` dependencies installed. Run from the repository root:

```text
python docs/papers/curled_torus/reviewer_checks_2026-10-09.py
python scripts/analyse_curled_revision.py --neutral
python scripts/analyse_curled_revision.py
python scripts/analyse_paper_stats.py
python scripts/analyse_t38.py
python -m pytest -q
python scripts/build_curled_paper.py --tectonic /path/to/tectonic
```

The build command regenerates the three figures, extracts the abstract from the TeX source, compiles the PDF and writes the content-hash manifest. Compilation and full-suite results are recorded with this revision. Generated TeX auxiliary files are not release artifacts. This package is suitable for a critical reader; it does not certify a question-free paper or independent physics review.

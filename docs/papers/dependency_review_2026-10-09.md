# Dependent-document and analysis review — 9 October 2026

Scope: trace the curled-torus corrections into other repository documents and reporting code.
This is an internal audit, not part of the reader manuscript. Scientific interpretations
remain **Ours, unverified by an independent physicist**. The common reference is
[measurement_scope.md](measurement_scope.md).

| Affected material | Correction |
|---|---|
| README, glossary, series plan and programme source | Counting observables, connectivity, energy release and finite-time persistence replace stronger geometric or equilibrium claims. The paper is an unpublished manuscript. |
| Relic, fertile-window, six-link and black-hole drafts | Correct inherited geometry/front/temperature premises; distinguish initial gap from actual release. Fertile-window now includes T38, the all-observed T22 mean and the correct two-channel positive-barrier endpoint 1.6. |
| Public HTML and post | Correct count-based interpretations, remove the uncalibrated N/3.5 chart prediction, regenerate the site copy and ladder page. The archived programme fragment points to current source. No website deployment performed. |
| Historical registers and design/reading notes | Add dated correction pointers without rewriting original predictions or rescoring failures. Correct Q12's level-spacing assertion and Q15's classical weighting justification directly. |
| Dimension and sealed-bath docstrings | Define what the stored statistics measure and the assumptions needed for thermometry. No simulation kernel changed. |
| T9/T10 reporting | Identify count-based outcome labels and mean store energy; preserve historical scoring, including T10's uncalibrated threshold. |
| T22 reporting | Retain the conditional historical score; separately report every observed first exit, including the unconverted replica. Its inclusion changes the N=96, λ=1.05 mean from 7485 to 9302 sweeps. Reciprocal exit count is not a transmission probability. |
| Statistical and T38 reporting | State the pooled-bootstrap dependence limitation, detector-clock approximation and exclusion of missing detector crossings from the historical tail score. |
| Sealed-sheet budget runner | Remove unjustified use of 4λ as a demon level spacing. Always report measured mean energy; calculate the temperature proxy only for an explicit positive level spacing. Old result temperature columns remain unvalidated. |
| Exploratory sealed-run plot | Show escape counts over the stated duration, allow neutral moves, and avoid inferring a unique endpoint or equilibrium from final graph energy. |

Validation: the full suite passed **831 tests**. After adding the runner regression cases,
the focused suite passed **6 tests** (the four T22 tests plus two new thermometer cases), for
**833 distinct passing tests** across the two runs. T9, T10, T22 and T38 reproduce their
historical verdicts. All four edited companion manuscripts compile without overfull boxes or
undefined references; the relic draft's malformed table rows were repaired. Generated HTML
JavaScript passes syntax checks. The regenerated figure and companion table pages were
visually inspected. The paper release manifest now covers 38 files, including the affected
analysis sources and validation log. Raw results and configs are unchanged.

Evidence: [validation log](curled_torus/followthrough_validation_2026-10-09.log).
This pass checks propagation of the identified errors; it is not independent physics review
or a new validation of every later research claim in the repository.

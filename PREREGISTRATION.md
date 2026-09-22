# Pre-registration

Rule 4 of `CLAUDE.md`: predictions and analysis choices are committed here **before** the runs that test them. The git commit containing a section is its timestamp. Nothing below may be edited after its runs have started; corrections are added as dated amendments underneath, with the original left standing.

---

## T6. The order of the geometry-forming transition

**Written 2026-09-21; revised the same day, before any production run, after reading the methodology literature and three papers the project had not seen.** What follows fixes what will be measured and what each outcome will be taken to mean.

### Why this measurement and not another

VISION success condition S2 asks whether the transition is first order. Every measurement in this repository so far is an average taken at one coupling, which cannot answer it: a barrier is exactly the place a thermal chain refuses to go. The density of states does answer it, because from it the whole energy distribution follows at every coupling, including the part no chain visits.

### The four observables, and why four rather than one

All four come free from the same density of states, and the field's own literature treats them as the standard set for exactly this question. Measuring one and not the others is how a weak first-order transition gets missed.

| Observable | What it is | First order | Continuous |
|---|---|---|---|
| **Latent heat** `Δe` | the gap between the two humps of P(H), per point | stays finite as N grows | shrinks to zero |
| **Barrier** `ΔF` | depth of the valley between the humps, in ln P | grows like the interface, so like √N | bounded, or zero |
| **Binder energy cumulant** `B_min` | the minimum of 1 − ⟨H⁴⟩/3⟨H²⟩² | tends to a value **below 2/3** | tends to **2/3** |
| **Specific heat peak** `C_max` | the height of the heat-capacity peak | grows in proportion to N | grows like a smaller power |

**The latent heat is the one that matters most for claim 4**, and the earlier draft of this section did not include it. Claim 4 is not a claim that a barrier exists; it is a claim that a *lump of energy comes out*, and the lump **is** the latent heat. A barrier with no latent heat would satisfy S2's letter and do nothing claim 4 needs.

Reported alongside at every point, because the thesis found in the reading calls the higher-degree configurations "nearly geometric" and S4 needs to know: the connectivity observables of T3 (`pieces`, `largest_frac`, `baby_frac`, `cube_frac`) **on both sides of the transition and in the valley between**.

### What will be run

| Choice | Value | Why this and not something else |
|---|---|---|
| Sizes | N = 36, 64, 100, 144, and **256 if the smaller four converge** | Square tori (L = 6, 8, 10, 12, 16) so the interface length is unambiguous; a rectangle has two cross-sections and the cheapest interface takes the short one. 256 is added because it matches a published size of the second group, allowing direct comparison at λ = 0. |
| Knob λ | 0, 1, 1.25, 1.5 | 0 and 1 are the two published settings. 1.25 and 1.5 are where the flat sheet is provably the lowest-energy arrangement, which is where S2 and S4 could both hold. The whole map is published whichever way it comes out (S1). |
| Method | Wang–Landau over (S, X), then the frozen-weight refinement | Bins are (S, X) rather than the energy, so one run covers every λ. Stage one is never reported alone (Q14). |
| Independent runs | 4 seeds per (N, λ) | The spread between them is the error bar. Block-based error bars underestimate and will not be quoted. |
| Window | A band in (S, X) around the transition, edges fixed from the tempering equilibrium curve before the run starts and recorded in the config | The full range is too many bins to flatten at the larger sizes. Restricting is legitimate; ln g is correct inside the window. |

**The transition coupling is located separately at each size**, as the coupling where the two humps carry equal weight. This is deliberate: the thesis reports that the critical temperature "appears to be asymptotically nonfinite", and our own T9 measures it drifting with ln N. A criterion that assumed one fixed transition coupling across sizes would be wrong if either is right.

### Validation gates, all of which must pass before any number is interpreted

1. **Ising**: the 4×4 density of states reproduced to better than 0.05 in ln g. *(Passed: 0.006–0.013.)*
2. **Exact enumeration**: N = 16 and 18 reproduced to better than 0.05 in ln g, every bin found and none invented. *(Passed: 0.016 and 0.014.)*
3. **At each production size**: the four seeds must agree on `ΔF` to better than 20 % of the value being claimed, and on `Δe` to better than 10 %. A size failing either is reported as not converged and excluded from the fits, and the exclusion is reported.
4. **Round trips**: each run must cross its window end to end at least 20 times. Reported with every run.

### What each outcome will be taken to mean

Fits are over at least three sizes that passed gate 3.

- **FIRST ORDER** — `Δe` extrapolates to a non-zero value at 3 standard errors, **and** `ΔF` grows with a slope positive at 3 standard errors, **and** `B_min` sits below 2/3 and is not rising towards it. All three.
- **NO EVIDENCE OF FIRST ORDER AT THESE SIZES** — `Δe` extrapolates to zero within 2 standard errors, and `ΔF` shows no growth, and `B_min` approaches 2/3. **Deliberately not called "continuous".** The literature is explicit that at a weak first-order transition the usual analyses can work deceptively well and return continuous-looking answers, so this wording is what the evidence supports.
- **INCONCLUSIVE** — anything else, including the three criteria disagreeing with each other. A real outcome; it will not be resolved afterwards by adding sizes, changing the fit, or dropping a size that misses the line. Any such change is a new pre-registration.

### What would count against the hypothesis

**Written before the answer is known.**

- If the result is **no evidence of first order** at every λ where the settled state is a sheet, **VISION claim 4 does not live in this model family**, and the write-up will say so in those words. That is the primary way this can fail, and it is the expected outcome on the published evidence.

- **And the obvious escape is closed in advance.** It will be tempting to answer that the transition is first order but too weak to see at these sizes. That answer does not help, and here is why: **a transition too weak to detect is also too weak to do claim 4's job.** The claim needs a lump large enough to become the matter and light of a universe. If `Δe` at the largest size is consistent with zero, then whatever latent heat exists is below our resolution — and the write-up will state the measured upper bound on it and say plainly that a lump that small cannot carry the claim. The bound, not the absence, is the result.

- Finding first order only at λ < 1 rescues nothing. That is already known, and there the cold state is knots rather than a space, so S2 is satisfied while S4 is not.

- If the barrier grows but the ordered side is not connected through the transition (`largest_frac` well below 1), S2 is met and S4 is not, and the write-up will say the two still have not been met together.

### What this measurement cannot show

Anything about the real universe; anything about X, which is not what this model contains; and anything about claims 2 or 6. A result here bears on claim 4 in the narrow sense of *whether geometry forms out of a random phase sharply or gradually*, which is narrower than claim 4 as VISION states it.

### Amendments

*(Add below with a date, leaving the original standing.)*

#### Amendment 1, 21 September 2026 — the reaction coordinate changes from H to φ

**Status: written after the λ = 0 control ran at N = 36 and N = 64, and before any run under the new coordinate.** That ordering is the whole point of writing it down, and the original text above stands unaltered.

**What is wrong with the original.** The four observables were to be read off the histogram of the energy H = 16(N − S) + 4λX. H is a sum of two integers with two different quanta, so which energies are reachable — and how many ways each is reached — is arithmetic between 16 and 4λ. Where 4λ divides 16 the reachable energies form a uniform lattice; where it does not, the histogram grows teeth at the period of that arithmetic. Two of the four pre-registered λ values are of the second kind: λ = 1.25 (quanta 16 and 5) and λ = 1.5 (quanta 16 and 6). Measured at λ = 1.25, N = 36, the counts on consecutive levels ran 2899, 30, 181, 1024, 2046, 1964, 34, and the analysis read two teeth as humps 19 levels apart with a barrier of 1.7. **This is a defect of the coordinate, provable from the arithmetic of 16 and 4λ without reference to any result.** It is not a judgement about which answer is wanted.

**What changes.** The reaction coordinate becomes S, equivalently φ = S/N — the order parameter by which the transition is defined in the first place. S is an integer with unit spacing at every λ, so there is no comb by construction. Runs will store the joint (S, X) histogram, from which H follows exactly for any λ; the per-sweep values already exist in the run and were simply not saved.

**What does not change, and is restated here so that it cannot be quietly adjusted later:**

- **The four observables keep their meanings.** In particular the latent heat stays an *energy* difference between the two phases — that is what a latent heat is. What changes is only that the two phases are identified in φ before their energies are compared.
- **The free-energy barrier is measured along φ.** This is the one observable whose definition genuinely moves, from a valley in the energy histogram to a valley in the φ histogram. Both are standard; the second is the one that is well defined at every λ.
- **The gates, the fit, the three verdicts and the falsification clause are untouched**, including the clause that a transition too weak to detect is too weak to do claim 4's job, and that the write-up will then state the measured upper bound.
- **The λ values stay {0, 1, 1.25, 1.5}.** They are not being trimmed to the ones with convenient arithmetic.

**What is discarded and why.** No barrier measured under the old coordinate will be quoted, including at λ = 0 and λ = 1, where the lattice is uniform and the comb does not arise. The reason is separate and is recorded as O8 in `ASSUMPTIONS.md`: at λ = 0, N = 36 the three ladder rungs that can see the transition disagree about the barrier by 54.9 %, against 0.9 % for the transition coupling. A number that depends that strongly on which rung it is approached from is not a measurement, whatever the coordinate. The transition coupling g_c, which is stable, is not affected by this and stands.

**A guard added under the old coordinate is withdrawn.** `analyse_t6_hist.py` gained a coarse-graining veto that was written after seeing the λ = 1.25 data it rejects, and it moved the λ = 0, N = 36 barrier from 0.969 to 0.436. Tuning a threshold against the data it judges is the thing this document exists to prevent. The veto's idea — that a real barrier survives coarse-graining and a lattice artefact does not — is sound, and under φ it is not needed, because there is no comb to veto.

#### Amendment 2, 21 September 2026 — the λ = 0 size sequence is multiples of 16

**Status: written after λ = 0 ran at N = 36 and N = 64 under amendment 1, and before any run at the sizes it adds.**

**What is wrong with the original.** The pre-registered sizes are square tori, N = 36, 64, 100. At λ = 0 the cold phase shatters into 16-point knots, and the smallest valid piece has 14 points. So N = 64 = 4 × 16 shatters into four whole knots (measured φ = 1.422), while N = 36 = 2 × 16 + 4 cannot — its cold phase is one knot plus a 20-point ribbon (measured φ = 1.278) — and N = 100 = 6 × 16 + 4 is knots-plus-ribbon again. **These are two different cold phases with different energies**, which is why the latent heat measured 5.8 per point at N = 36 and 9.5 at N = 64: not statistics, structure. A finite-size fit across 36 / 64 / 100 would be fitting a line through a structural step. This is arithmetic (section 19 of the write-up, the ribbon, applied to the size list) and does not depend on any result.

**What changes.** For λ = 0 the sizes entering the fit are multiples of 16: **64, 96 (16 × 6), 128 (16 × 8)**, with 144 (12 × 12) and 160 (16 × 10) if affordable. These are the Gate A sizes. The already-run 36 and the pre-registered 100 are reported but do not enter the λ = 0 fit.

**What does not change.** For λ ≥ 1 the cold phase is the flat sheet, which exists at every size, so the square tori stand there. The observables, gates, verdicts and falsification clause are untouched.

#### Amendment 3, 21 September 2026 — the λ = 0 barrier is measured by a one-dimensional flat-histogram walk

**Status: written after the walk was validated against exact counts at N = 16 and against tempering at N = 36, and before its result at any larger size was seen.**

**What is wrong with the method as run.** Tempering across the λ = 0 transition collapses at the transition rung — swap acceptance 0.26 at g ≈ 6.75 at N = 64 on both a shared ladder and a per-size one — because across a first-order transition adjacent rungs stop sharing energies, and the gap grows with N. Densifying the ladder does not remove this; it is the textbook case for a flat-histogram method, which walks through the valley rather than trying to hop it. The original pre-registration named Wang-Landau as the instrument and moved to tempering when the two-dimensional walk over (S, X) failed at N = 36 (Q17). But at λ = 0 the energy is 16(N − S) alone: X never enters, the density of states is one-dimensional in S, and the walk is over tens of bins rather than hundreds.

**What changes.** At λ = 0 the four observables are read from the one-dimensional density of states in S (`scripts/run_wl_lam0.py`), which gives the full P(φ) at every coupling. The walk must reproduce the exact N = 16 counts (it does: `test_one_dimensional_walk_in_s_matches_the_exhaustive_count_summed_over_x`) and must agree with tempering where tempering works (at N = 36: phases at φ = 0.917 | 1.278 by both; g_c 7.34 against 7.51). Round trips across the reachable range of S are reported with every row, and gate 4 applies to them.

**What does not change.** Tempering remains the instrument at λ ≥ 1, where there is no wall, and remains a cross-check at λ = 0 where it can reach. Observables, gates, verdicts, falsification clause untouched.

#### Verdict at λ = 0 under the rules above, 22 September 2026: INCONCLUSIVE

Three sizes (48, 64, 96) pass gates 3 and 4. Criterion 1 met (latent heat 12.5 ± 0.02 per point at N = 96). Criterion 2 met (barrier slope +1.59 ± 0.05 against L, 34 standard errors). Criterion 3 not met as written: the Binder minima 0.381, 0.480, 0.575 are below 2/3 but rising. The rules say the criteria disagreeing is INCONCLUSIVE and is not to be resolved afterwards by changing the rule. It is not. Full table in `ASSUMPTIONS.md` O11.

#### PROPOSED amendment 4 — not enacted; Emily's decision — criterion 3 is mis-specified

**Written after the λ = 0 verdict above, and it would change that verdict. That is stated first so it cannot be missed.**

The value a first-order transition predicts for the Binder minimum is not 2/3. For two phases at energies e₊ and e₋ per point it is 1 − 2(e₊⁴ + e₋⁴)/(3(e₊² + e₋²)²), which is 2/3 only when |e₊| = |e₋| (Challa, Landau and Binder 1986). In this model the cold phase sits at φ = 1.5 (e₋ = −8) and the hot one near 0.7 (e₊ ≈ 4.8), so the first-order limit is about 0.59, and the finite-size approach to it is from below. The measured minima are rising towards 0.59, not towards 2/3; at N = 96 the measured value is 0.575 against a predicted 0.594. As written, criterion 3 can never return FIRST ORDER in this model, whatever the physics — and it is the positive control, where the transition is known to be first order, that exposed this.

**Proposed wording.** Criterion 3: the Binder minimum lies below 2/3 at every size, and at the largest size lies within 0.03 of the two-spike prediction computed from that size's measured phase energies. The prediction has no free parameter.

**Why this is proposed rather than made.** It is a rule change after seeing data, which this document forbids me to make. What makes it defensible for Emily to make is (a) the formula is textbook, (b) the defect was found on the control and not on the cases under test, and (c) the alternative — issuing λ ≥ 1 verdicts under a criterion that fails the positive case — is worse. **If adopted:** λ = 0 becomes FIRST ORDER, and the same criterion applies unchanged at λ ≥ 1. **If not adopted:** λ = 0 stays INCONCLUSIVE, and criterion 3 must be declared uninformative and dropped from the λ ≥ 1 verdicts *before* they are read, for the same reason. Either way is honest; leaving it as it stands is not.

---

## T7. The λ map

To be written before T8 runs. It may reuse the criteria above, and if it does it will say so explicitly rather than restating them.

The draft for the parked menu study is in `docs/parked/PREREGISTRATION_menu_study.md`.

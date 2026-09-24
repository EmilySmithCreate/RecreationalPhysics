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

#### Amendment 4, 22 September 2026 — ENACTED at the author's decision — criterion 3 is compared to the two-spike prediction

**Status: proposed after the λ = 0 control had run (text below, as proposed); adopted by the author on 22 September 2026 with the wording in "Enacted wording" at the end of this amendment. The λ = 0 verdict is re-issued under it in `ASSUMPTIONS.md` O11; the same rule applies unchanged to λ ≥ 1.**

**Written after the λ = 0 verdict above, and it would change that verdict. That is stated first so it cannot be missed.**

The value a first-order transition predicts for the Binder minimum is not 2/3. For two phases at energies e₊ and e₋ per point it is 1 − 2(e₊⁴ + e₋⁴)/(3(e₊² + e₋²)²), which is 2/3 only when |e₊| = |e₋| (Challa, Landau and Binder 1986). In this model the cold phase sits at φ = 1.5 (e₋ = −8) and the hot one near 0.7 (e₊ ≈ 4.8), so the first-order limit is about 0.59, and the finite-size approach to it is from below. The measured minima are rising towards 0.59, not towards 2/3; at N = 96 the measured value is 0.575 against a predicted 0.594. As written, criterion 3 can never return FIRST ORDER in this model, whatever the physics — and it is the positive control, where the transition is known to be first order, that exposed this.

**Proposed wording.** Criterion 3: the Binder minimum lies below 2/3 at every size, and at the largest size lies within 0.03 of the two-spike prediction computed from that size's measured phase energies. The prediction has no free parameter.

**Why this is proposed rather than made.** It is a rule change after seeing data, which this document forbids me to make. What makes it defensible for Emily to make is (a) the formula is textbook, (b) the defect was found on the control and not on the cases under test, and (c) the alternative — issuing λ ≥ 1 verdicts under a criterion that fails the positive case — is worse. **If adopted:** λ = 0 becomes FIRST ORDER, and the same criterion applies unchanged at λ ≥ 1. **If not adopted:** λ = 0 stays INCONCLUSIVE, and criterion 3 must be declared uninformative and dropped from the λ ≥ 1 verdicts *before* they are read, for the same reason. Either way is honest; leaving it as it stands is not.

**Enacted wording (the author's choice among the options put to her, 22 September 2026).** Criterion 3: the Binder minimum lies below 2/3 at every size; at the largest size it lies within 0.05 of the two-spike prediction computed from that size's measured phase energies; and the gap between prediction and measurement shrinks with N. The prediction has no free parameter. The tolerance in the proposed wording above was 0.03; the measured gap at N = 96 is 0.019, so the case is decided the same way under either, and the choice of tolerance is not what decides it. `scripts/analyse_wl_lam0.py` implements this wording.

#### Verdict at λ = 1, 1.25 and 1.5 under the rules above, 22 September 2026: INCONCLUSIVE

Reruns with a trimmed ladder meet gate 4 everywhere (46 to 400 round trips per replica). In the region where φ changes there is one hump at every λ, size and replica; the largest latent heat that could hide in it is below 1.30, 1.28 and 1.26 per point at N = 100 and falling with size, against 12.5 measured at λ = 0 (the falsification clause's required output). Criteria 1 and 2 therefore come out in the direction of "no evidence". **Criterion 3 cannot be evaluated:** the Binder energy cumulant depends on where the energy zero sits, and at λ ≥ 1 the cold phase is the flat sheet at exactly zero energy, where the cumulant collapses whatever the shape of the distribution (`ASSUMPTIONS.md` O17). The rules make a criterion that cannot be read INCONCLUSIVE, and say it is not to be resolved afterwards by changing the rule. It is not.

#### Amendment 5, 22 September 2026 — ENACTED at the author's decision, option (a) — criterion 3 at λ ≥ 1 uses the cumulant of φ, which does not depend on the energy zero

**Status: proposed after the λ ≥ 1 verdict above (text below, as proposed); adopted by the author on 22 September 2026, option (a), with the wording in "Enacted wording" at the end of this amendment. The enacted wording was written into this file before any value of the φ cumulant was computed.**

**Written after the λ ≥ 1 verdict above, and it would change how that verdict is read. Stated first so it cannot be missed.**

At λ = 0 both phases sit far from zero energy and the Binder energy cumulant behaves; at λ ≥ 1 the cold phase *is* the zero, and the cumulant is undefined in effect. Two options: **(a)** criterion 3 at λ ≥ 1 uses the fourth-order cumulant of φ, the order parameter, which does not move when the energy zero does — computed from the `t6c` files as they are, and the verdict re-read (expected: NO EVIDENCE OF FIRST ORDER AT THESE SIZES, if the φ-cumulant minimum approaches 2/3 with size, as its energy cousin appears to in the transition window); **(b)** criterion 3 is declared uninformative at λ ≥ 1, and the verdict rests on criteria 1 and 2 with the bound. Either is honest. What is not honest is issuing a verdict at λ ≥ 1 under a criterion that cannot be read, in either direction.

**Enacted wording (the author's choice, option (a), 22 September 2026).** At λ ≥ 1, criterion 3 uses U_φ = 1 − ⟨φ⁴⟩ / 3⟨φ²⟩², computed from the joint (S, X) histograms of the `t6c` runs (N = 64, 100) and the `t6b` runs (N = 36, which already met gate 4), reweighted across each rung's coupling range under the same guards as the rest of the φ analysis (at most 25 % in 1/g; an effective sample of at least max(500, 2 % of the rung)). Per replica, U_min is the minimum over every rung and every admissible coupling; per size, the mean over replicas, with their spread reported beside it. **Criterion 3 reads as approaching 2/3 exactly when the gap 2/3 − U_min shrinks at each step from the smallest size to the largest (36 → 64 → 100).** If it does, the verdict at that λ is NO EVIDENCE OF FIRST ORDER AT THESE SIZES, criteria 1 and 2 having come out as stated above; if it does not, the verdict stays INCONCLUSIVE. Nothing is re-run. `scripts/analyse_t6_phi_binder.py` implements this wording.

#### Verdict at λ = 1, 1.25 and 1.5 under amendment 5 (a), 22 September 2026: INCONCLUSIVE — and the wording, not the physics, is why

The gap 2/3 − U_min is 0.0101, 0.0116, 0.0114 at λ = 1; 0.0099, 0.0113, 0.0117 at λ = 1.25; 0.0098, 0.0113, 0.0114 at λ = 1.5 (N = 36, 64, 100; replica spreads below 0.0007). It does not shrink at each step, so criterion 3 is not met as enacted and the verdict is INCONCLUSIVE. **The reason is a defect in the enacted wording, which the assistant drafted:** U_φ has no minimum at the transition. It falls steadily from 2/3 on the cold side towards the hot side, because its distance from 2/3 is set by the relative width of P(φ), which grows as the mean of φ falls. So "the minimum over every rung and coupling" always lands at the hot edge of the scan (g = 10.0, the 25 % reweight above the top rung at g = 8, in every replica at every size), in the random phase, where it tracks how the random phase's φ falls with N at fixed g, not the change. The wording was fixed before any value was computed, as the rules require, but the shape of U_φ was not checked first. Per-rung values are in `ASSUMPTIONS.md` O17, addendum. **Decided by Emily, 2026-09-22, evening: option (i).** INCONCLUSIVE stands as the final verdict of these runs, and no further change is made to criterion 3. Her reason: the random-phase route is the published question, not the hypothesis's, and the measurements — one hump everywhere, any lump below 1.30, 1.28, 1.26 per point at N = 100 and falling — are the result whatever the label. Criteria 1 and 2 and the bound are unaffected: one hump at every λ, size and replica, any lump below 1.30, 1.28, 1.26 per point at N = 100 and falling.

---

## T7. Is the change from one order to another sharp? The tube → sheet decay

**Written 2026-09-22, before any run under it.** The existing traces in `results/cqg_tube_waiting_lam125.csv` were recorded for a different question (how long the wait is) and have been looked at only as means; their *shape* has not been examined and the predictions below are made before it is.

### Why this and not T6

T6 asked whether the change from the model's disordered phase to a geometry is sharp. It is not, at any setting where the cold state is a sheet, and the published work agrees. But the hypothesis under test was never about the disordered phase. Claim 3 says X is an *arrangement* — with its own degrees of freedom and its own order — and claim 4 says the change from that arrangement to space was sharp and released a lump. That is a change from one order to another, and T6 did not test it. This does.

The published family contains such a change with no new ingredient. For λ > 1 a torus with one side curled to length 4 — the tube, one large dimension and one curled — sits above the flat sheet by exactly 4(λ − 1) per point and is long-lived (thousands of sweeps at g = 1.5), and then uncurls into the sheet, releasing exactly that energy (VISION Update 9; the design brief). The tube is a stand-in for X: an arrangement, more symmetric than the sheet in the sense that one direction has been identified with itself, higher in energy, metastable. The sheet is space. **The question is whether the change between them is sharp in the sense claim 4 needs.**

### What "sharp" means when there is no temperature to sweep

A metastable state decays at fixed temperature, so the T6 machinery (two humps in a histogram over a coupling scan) does not apply. For an order → order change, "first order" means: the two arrangements are distinct states; the change begins at a place and spreads, with old and new order coexisting across an interface while it happens; and the energy comes out as the interface moves. "Continuous" means the whole system deforms smoothly through intermediate arrangements, everywhere at once, with no coexistence. These are distinguishable by looking at the system *while it changes*, which the existing runs never did — they recorded only φ.

### The observables

A vertex has four edges and six pairs of edges. Each pair that closes no square is a direction that stays large; the count is the vertex's **local dimension** d(v): 2 on the sheet, 1 on the tube, 0 in a cube (`test_sheet_tube_cube_ladder`; to be extended to a per-vertex function and validated on those three exact states before use).

1. **Waiting-time distribution.** The time from the start until the decay begins, over many independent replicas. A change that starts by a rare local event is memoryless: the waiting times are exponentially distributed, with standard deviation equal to the mean (coefficient of variation ≈ 1). A smooth deformation has a characteristic time and a narrow distribution (CV ≪ 1).
2. **Coexistence.** At the moment the system is half converted (φ halfway between the tube's and the sheet's), the histogram of d(v) over vertices. Two-state: most vertices at d = 1 or d = 2 and few in between. Continuous: mass in the intermediate values, or a single hump that has moved.
3. **Where the new order is.** At quarter, half and three-quarter conversion, the vertices with d(v) = 2 as a set: how many connected pieces, and the largest piece's share. A front: one piece holding most of it. Everywhere at once: many pieces, none dominant.
4. **The lump.** Energy released per point, against the exact 4(λ − 1). A check, not a question.

### What will be run

Tubes 16×4, 24×4, 36×4, 48×4 (N = 64, 96, 144, 192), λ = 1.25 and 1.5, g = 1.5, starting from the exact tube, Metropolis, independent seeds; at least 30 decays per (size, λ). During each run, when φ first crosses 25 %, 50 % and 75 % of the way from the tube's value to the sheet's, the adjacency is snapshotted and d(v) computed for every vertex. The waiting time is the sweep at which φ first leaves the tube's value by more than the run's own resting fluctuation (defined as three times the standard deviation of φ over the first 200 sweeps, before any decay).

### Predictions, written before looking

*Ours, unverified.* If claim 4's mechanism is what the tube shows: (a) CV of the waiting time between 0.7 and 1.3 at every size; (b) at half conversion, at least 80 % of vertices at d ∈ {1, 2}; (c) at half conversion, the largest connected d = 2 piece holds at least 70 % of the converted vertices. Recorded and not predicted: how the mean waiting time scales with N (the earlier 1/N prediction was refuted at 2.9σ, Update 9).

### Gates

1. d(v) reproduces 2 / 1 / 0 on the exact sheet, tube and 4-cube, every vertex.
2. At least 30 decays per (size, λ) that reached 75 % conversion within the run.
3. The released energy per point within 1 % of 4(λ − 1) in every decay counted.

### Verdicts

- **TWO-STATE CHANGE** — (a), (b) and (c) all hold at every size run. This is what a first-order order → order change looks like, and it is the shape claim 4 needs.
- **CONTINUOUS DEFORMATION** — CV < 0.4 at every size, and fewer than 50 % of vertices at d ∈ {1, 2} at half conversion. The tube does not *switch* to the sheet; it slides. Claim 4's "sharp" fails in this family at the one order → order change it contains.
- **INCONCLUSIVE** — anything else. As in T6, not to be resolved by adjusting thresholds afterwards.

### What this cannot show

That X *is* a tube, or that the universe did this. That a lump large enough for claim 4 exists — 4(λ − 1) is a model constant. Anything about a sealed system: that is T8, the bonfire-or-slush question, which needs its own pre-registration and this result first.

### Amendments

#### Amendment 1, 22 September 2026 — how long to wait before reading the released energy

**Status: written after the first runs (`t7_lam125_n*`, `t7_lam15_n*`) and before the rerun (`t7b_lam125_n*`). The first runs stand and are reported.**

**What went wrong.** The section above did not say how long to wait after conversion before reading the final energy; the runner waited a fixed 300 sweeps. Gate 3 then failed on every decay at both λ. Eight decays followed for 6,000 sweeps show why: about half release the full 4(λ − 1) at once, and the other half release **0.78 of it, sit on that value for hundreds to thousands of sweeps, and then release the rest in one step**. The same 0.78 every time — a specific defected sheet, a second metastable state on the way down, which then also switches sharply. A 300-sweep read catches the system on that ledge. Read after 6,000 sweeps, all eight give 1.00.

**What changes.** The final energy is read in windows of 600 sweeps and accepted when two consecutive windows agree to 0.5 % of 4(λ − 1) and the value is within gate 3's 1 % of it, up to a cap of 30,000 sweeps. The release after the first window and the length of any ledge are recorded with every decay, since the ledge is itself the kind of sharp step claim 4 describes and should not be thrown away by the protocol that was blind to it. Gate 3 is unchanged; only the point at which it is applied is fixed.

**What is not changed.** The three observables, the three predictions and the verdicts. Gate 3 as a criterion.

#### Amendment 2, 22 September 2026 — ENACTED at the author's decision — gate 3 checks the energy at whichever state the decay reached

**Status: proposed after the ledge was seen (text below, as proposed); adopted by the author on 22 September 2026 with the wording in "Enacted wording" at the end of this amendment. The verdicts are re-issued under it in `ASSUMPTIONS.md` O13.**

**Written after the rerun `t7b_lam125_n*`, which it would change the verdict of. Stated first.**

Under amendment 1 the settle runs until the released energy has stopped changing, up to 30,000 sweeps. Gate 3 still fails at every size: 16 to 21 of 30 decays pause on the ledge at 0.76 to 0.87 of the full release, and a few are still there at the cap, having sat on it for 21,000 to 27,000 sweeps. **The ledge is longer-lived than the tube** (which waits 700 to 900 sweeps). No finite settle can make every decay finish, because the second step has its own long, apparently memoryless wait.

Gate 3 was written as an energy-conservation check: is the lump the known 4(λ − 1)? The answer is yes — every decay that completes its second step releases 1.00 to within 1 %, and every decay on the ledge releases the ledge's own value, the same 0.78 each time. What gate 3 actually tests, as written, is whether every decay completes *both* steps inside the run, which is a question about the ledge's lifetime and not about the lump.

**Proposed wording.** Gate 3: every counted decay's released energy, at the end of the settle, is within 1 % of *either* 4(λ − 1) *or* the ledge value (the modal first-window release across decays at that size). Energy is thereby checked exactly at whichever state the decay has reached. Decays on the ledge are counted for predictions (a), (b) and (c), which concern the first switch and are measured at half conversion, before the ledge is reached.

**Enacted wording (the author's choice among the options put to her, 22 September 2026).** Gate 3: every counted decay's released energy per point, at the end of the settle, is within 1 % of 4(λ − 1) *either* for the full sheet *or* less one ring's energy, (24λ − 16)/N — 14/N at λ = 1.25 — for the ledge, the ledge having been identified as one ring of the tube (O13; `scripts/diagnose_ledge_and_start.py`). Both values are exact arithmetic; nothing is read off the data. This is stricter than the proposed wording, which would have taken the modal ledge value from the data: a decay resting on anything other than the full sheet or a single ring fails the gate, and is reported as such rather than accommodated. Decays on the ledge are counted for predictions (a), (b) and (c) as in the proposed wording. `scripts/analyse_t7.py` implements this.

**Outcome under it (same day):** gate 3 still fails at every size, because 2 to 6 decays per size were still moving when amendment 1's 30,000-sweep cap ended them; every decay that settled is at the sheet or the one-ring ledge. Details in `ASSUMPTIONS.md` O13. The verdict stays withheld.

#### Amendment 3, 22 September 2026 — ENACTED at the author's decision, option (i): the unsettled decays are replayed with a longer cap

**Status: proposed after the outcome of amendment 2 (text below, as proposed); the author chose option (i) on 22 September 2026, with the wording in "Enacted wording" at the end of this amendment, before any replay was run.**

**Status: written after the outcome above, before any further run.**

Amendment 1 set a settle cap of 30,000 sweeps and did not say what gate 3 makes of a decay that reaches the cap without two consecutive windows agreeing. As enacted, such a decay fails the gate, although it is not in any state to be checked. Two options, in the order recommended:

- **(i) Finish the measurement, no rule change.** The affected decays are reproducible from the seeds recorded with them. Replay those seeds with the cap raised to 100,000 sweeps and read where they settle; then apply gate 3 exactly as enacted. A longer settle cannot manufacture a pass — it can only reveal the resting state — and a decay that settles on anything other than the sheet or one ring fails as written.
- **(ii) Amend gate 3:** it applies to settled decays only (two consecutive windows agreeing, as amendment 1 defines); the number of unsettled decays is reported for each size and must be fewer than half. This is the weaker option, because it lets a minority of decays go unexamined.

Either is honest; leaving the gate to fail on decays that never settled is a statement about the cap, not about the change.

**Enacted wording (option (i), the author's choice, 22 September 2026).** The fourteen decays of `t7b_lam125_n*` that reached the 30,000-sweep settle cap — N = 64: replicas 1, 25; N = 96: 3, 10, 20, 23; N = 144: 3, 5; N = 192: 3, 5, 8, 10, 20, 22 — are replayed from the same configuration seeds (20261057, 20261065, 20261077, 20261089), the same replica indices and the same code path, with `settle_max` raised from 30,000 to 100,000 sweeps and nothing else changed; results under `t7c_lam125_n*` (`replica_ids` in the config names the replicas). **Reproducibility gate:** a replay must reproduce its original decay up to the old cap — identical `waiting` and identical `released_first_window` — or it is not the same decay, is left out of the table and is reported. **The verdict** is then gate 3 exactly as enacted in amendment 2, applied to the t7b table with those fourteen rows replaced by their replays (`scripts/analyse_t7.py lam125 t7b t7c`). A replay that has still not settled at 100,000 sweeps fails the gate as written and is reported; option (ii) is not enacted by this amendment.

**Outcome (same day, 10:42).** All fourteen replays reproduced their originals; two finished to the sheet (N = 64 replica 1 at 44,400 sweeps; N = 192 replica 10 at 84,600); twelve reached 100,000, six of them with their released energy unchanged to the last digit since 30,000. Gate 3 fails at every size as written; the verdict stays withheld. Details: `ASSUMPTIONS.md` O13, second addendum, which also corrects an earlier inference — a decay at the cap is one that did not reach the full release, not necessarily one still moving, because amendment 1's settle loop terminates only at the full release.

#### Amendment 4, 22 September 2026 — ENACTED at the author's decision, option (a) — identify the resting states instead of assuming them

**Status: written after the outcome of amendment 3, before any further run (text below, as proposed); adopted by the author on 22 September 2026, option (a), with the wording in "Enacted wording" at the end of this amendment, before any replay under it was run.**

Gate 3's list of final states that count (the sheet; one four-point remnant) was an assumption, and twelve decays rest on states outside it, with retained energies from 8 to 45 units. Two options:

- **(a) Identify, then check.** Replay the twelve from their seeds once more, with the final adjacency saved (`results/t7d_*` plus a small `.npz` per decay); read each resting state — local-dimension histogram, connected pieces at d ≠ 2, extra squares, surplus edges — and pass gate 3 for a decay exactly when its released energy equals the exact energy of the structure read, to within the same 1 %. Nothing is assumed about which structures occur; each is named from the graph and its energy computed from its wiring. A decay whose energy does not match its own read structure fails.
- **(b) Option (ii) of amendment 3:** gate 3 applies only to decays that reached the full release; the number that did not is reported per size and must be fewer than half. Weaker: it leaves the twelve unread.

Recommended: (a). Either way the three predictions, which concern the first switch, are unaffected.

**Why proposed rather than made.** It changes a gate after the data it judges were seen. What makes it defensible: the three predictions are met at every size on both the first run and the rerun with fresh seeds, and the change concerns only which decays are admitted, not what is measured on them; and the thing it admits — a decay resting on a second sharp step — is more of what claim 4 describes, not less. **If adopted:** the λ = 1.25 verdict is TWO-STATE CHANGE. **If not:** the verdict is withheld and the three predictions are reported as met with the gate outstanding.

**Enacted wording (the author's choice, option (a), 22 September 2026).** The twelve decays that reached neither the sheet nor the four-point remnant under amendment 3 are replayed from their recorded seeds with the cap of amendment 3 (100,000 sweeps), saving the final adjacency (`results/t7d_lam125_n*.csv`, and one `.npz` per decay in `results/t7d_lam125_n*_adj/`). A replay whose waiting time or first-window release differs from its original is rejected as not the same decay, as in amendment 3. Each resting state is read from its saved adjacency — the histogram of local dimension, the connected pieces of vertices at d ≠ 2, the extra squares S − N and the surplus edges X — and its exact energy is computed from that wiring, H = 16(N − S) + 4λX. Gate 3 passes for a decay exactly when its recorded released energy equals the release implied by the structure read, to within 1 %; a decay that does not match its own structure fails. Each structure is named from the graph; nothing is assumed about which occur. All other decays are judged as under amendment 2.

#### Verdict under amendment 4 (a), 22 September 2026: TWO-STATE CHANGE at N = 64, 96, 192; N = 144 fails gate 3 on one decay

The twelve replays (`configs/t7d_lam125_n*.json`) reproduced their originals exactly, waiting time and first-window release, and saved their final adjacency. Read from their wiring (`scripts/analyse_t7_states.py`), eleven match their recorded release exactly and pass gate 3; one, N = 144 replica 3, does not: it had held about 23 units since 30,000 sweeps (release 0.842 at both caps), then dropped to a state holding 8 during its last measuring window, so the recorded release (that window's average) does not match its final structure, and it fails as written. With the other decays judged under amendment 2 (`scripts/analyse_t7.py lam125 t7b t7c t7d`): gate 3 passes at N = 64, 96 and 192 and fails at 144, which is reported and not interpreted. **PRE-REGISTERED VERDICT, λ = 1.25, sizes 64, 96, 192: TWO-STATE CHANGE.** Predictions (a), (b) and (c) hold at all four sizes including 144. What the resting states are: `ASSUMPTIONS.md` O13, third addendum.

**Recorded, and not a change to anything:** at λ = 1.5 the tube is not metastable at g = 1.5 — it is at φ = 0.95 by sweep 50 in every replica, as it was in the design-track pilot at g = 1.0. There is no waiting time to measure and no switch to see. The section above listed λ = 1.5 assuming a long-lived tube there, and it is not one. Those runs are reported as what they are: the unstable case, which the verdict language was not written for and to which no verdict is applied.

---

## T8. The λ map (formerly T7)

To be written before it runs. It may reuse the criteria above, and if it does it will say so explicitly rather than restating them.

### Written 23 September 2026, late night, before any run

**The λ map along the tube: does the order → order change stay sharp as the coefficient comes down towards 1?**

#### Why

Every result on the order → order route (T7, T9, T10, T11) is at λ = 1.25, and the only other setting run on the tube, λ = 1.5, has no metastable tube to study. The model's author has said the coefficient must be exactly 1 (third note, 23 September), and at exactly 1 the tube and the sheet have the same energy, so nothing is released. **This map asks what happens between: is 1.25 a lucky point, or the middle of a family in which the change is sharp all the way down, with the release shrinking to zero as λ → 1?** Under S1 the whole map is published, whichever way it comes out. **The owner's framing, the same night:** in her theory λ is above 1, probably about 1.25, because only λ > 1 releases a lump; if there are many loops, a universe drawn at random belongs to the most prolific one, so the scan maps the ingredients of fertility (how long X stays stuck, the push that starts it, the lump, what the new space must absorb, the scrap left behind). She also asked for it because the model's author will need it before he engages with anything above 1 (docs/parked/extension_2026-09-22.md, decisions of 23 September).

#### Exact facts, computed before any run (to be committed as `scripts/tube_exit_moves.py` with its output)

Every switch the chain can propose out of the 16 × 4 and 24 × 4 tubes was listed (corrected the same evening: a first listing also counted switches between opposite sides, which the chain never makes; ASSUMPTIONS O20, correction) and sorted by its change in squares (ΔS) and surplus squares (ΔX); the cost of a move is −16ΔS + 4λΔX. Two families are cheapest:

| Move | (ΔS, ΔX) | Count | Cost | λ where it is the cheapest way out |
|---|---|---|---|---|
| A (the one of Update 9) | (−2, −4) | 3N | 32 − 16λ | below 4/3 |
| B | (−4, −10) | 2N | 64 − 40λ | above 4/3 |

A sweep is 2N attempts out of 4N² equally likely proposals, so 3N moves are offered 3 times a sweep at every size, which is Update 9's count, and 2N moves twice. Hence, at g = 1.5, **the mean waiting time before the first exit** is predicted with nothing fitted as
  τ(λ) = 1 / [ 3 exp(−(32 − 16λ)/g) + 2 exp(−(64 − 40λ)/g) ]:

| λ | 1.05 | 1.10 | 1.15 | 1.20 | 1.25 | 1.30 | 1.35 | 1.40 | 1.45 | 1.50 |
|---|---|---|---|---|---|---|---|---|---|---|
| τ, sweeps | 8,330 | 4,844 | 2,788 | 1,570 | 845 | 419 | 183 | 68 | 22 | 7 |
| release per point, 4(λ − 1) | 0.2 | 0.4 | 0.6 | 0.8 | 1.0 | 1.2 | 1.4 | 1.6 | 1.8 | 2.0 |

**The scrap near λ = 1, exact.** T7's analysis prices the common resting state, one curled column (the four-point remnant), at 24λ − 16 above the sheet (14 at λ = 1.25). It does not vanish as λ → 1, while the lump 4(λ − 1)N does. As a share of the lump: at N = 64, 22 % at λ = 1.25, 41 % at 1.10, 72 % at 1.05; at N = 192, 7 %, 14 % and 24 %. Below λ = 1 + 8/(4N − 24) (1.035 at N = 64, 1.011 at N = 192) a column left behind would cost more than the whole lump, so the tube could not end on it downhill. **So near λ = 1 the scrap keeps a large share of the lump, and the share falls with N.**

*Caveat, ours:* Update 9's check (mean observed over predicted 0.997) used move A alone; at g = 1.5 and λ = 1.25 move B adds about 18 % to the rate, so either B-moves mostly fall back into the tube or the earlier check was at couplings where B was negligible. That is checked first, from the existing T7 waiting times, before any new run is interpreted.

#### Named or interchangeable points: which, why, and the expected effect

**In the owner's theory the points are interchangeable** (VISION Update 12). The runs below use named points, as every run on the tube has, for one reason: the interchangeable version needs a count of each proposed arrangement's symmetries at every move, which is unaffordable at these sizes (ASSUMPTIONS Q15). **What the switch would change is computable exactly, and it is stated here so that the named-points result is not read as the theory's.** Counted before any run: the perfect tube has **2N** symmetries (128 at N = 64, 192 at N = 96), and one move out of it leaves **2** by either of the two cheapest ways out (1 to 4 by the other kinds of move; one arrangement checked per kind); the perfect square sheet has 4N, and one move out of it leaves 1 to 4. With interchangeable points each arrangement is weighted by its symmetry count relative to named points, so:

- **The first step out of the tube is N times rarer.** The effective wall rises by g ln N (6.8 at N = 96, g = 1.5), and **the waiting time is multiplied by N**: 81,000 sweeps instead of 845 at λ = 1.25, N = 96. With named points the wait does not depend on N (Update 9); with interchangeable points it grows in proportion to it. A larger X is more stable for longer.
- **The lump is unchanged**: the tube and the sheet differ in symmetry by a factor of about 2, a free-energy difference of g ln 2 ≈ 1 against a release of 4(λ − 1)N.
- **The front is expected to be unchanged**: while the change runs, the arrangement has 1 to 4 symmetries, so the two weightings differ by at most a factor of 4 on any step. *To verify* on the saved T7 snapshots before this is relied on.
- *Ours, unverified:* this is transition-state reasoning. The equilibrium weights are fixed by the choice of points; the kinetics are not uniquely fixed by them, so "N times rarer" is the change in the effective barrier, not a derived clock.

**Reported with every waiting time:** the named-points value measured, and the interchangeable-points value it implies (× N).

#### What will be run

T7's protocol and its enacted amendments exactly (`scripts/run_tube_decay.py`, observables (a) to (c), gates 2 and 3 as amended, and the resting-state reading of amendment 4 (a)), at λ = 1.05, 1.10, 1.15, 1.20, 1.30, 1.35, 1.40, 1.45; **all four T7 sizes**, N = 64, 96, 144, 192 (tubes 16, 24, 36, 48 × 4); g = 1.5; 30 decays per (size, λ); block 5; stop at 98 % conversion; `n_sweeps` 100,000 (up from T7's 30,000, because the predicted mean wait at λ = 1.05 is 8,330 sweeps); settle windows of 600 sweeps with `settle_max` 100,000 (T7 amendment 3); the final graph saved (`save_adjacency`, as T7 amendment 4 (a)); and one new column, `f_200`, the conversion fraction at sweep 200, recorded by reading the graph only (checked the same night: two committed T7b decays replayed with it are identical in every column). Configs `configs/t8_lam{105,110,115,120,130,135,140,145}.json`, one per λ with the four sizes, seeds inside. λ = 1.25 and 1.5 are already on the record and are not rerun.

#### Definitions, fixed now

- **Metastable at (λ, N)**: in more than half the decays, `f_200` < 0.25: the tube is still a tube when its 200-sweep resting stretch ends. (T7's waiting time needs that stretch to define the tube's own fluctuation; a tube that has already gone has no resting state to leave, and its waiting time is not read.) *Corrected before any run: the draft said "median waiting time at least 200 sweeps", which is undefined for a tube that breaks up inside its resting stretch.*
- **Sharp at (λ, N)**: T7's TWO-STATE CHANGE criteria (a), (b), (c) all hold.
- **Reaches the sheet**: the decay ends at the sheet or at one of the resting states read from the wiring (T7 amendment 4 (a)), with its released energy matching that state exactly.
- **Waiting-time law holds**: the mean waiting time is within 25 % of τ(λ) above.
- **Gates**, as T7: gate 2 (at least 30 decays reaching 75 % conversion) and gate 3 as amended (each decay's release matches the sheet, the four-point ledge at 24λ − 16, or a resting state read from its wiring). A (λ, N) that fails a gate is reported and not read; a (λ, N) that is not metastable has no decay to gate and is reported as such.
- **Scrap**, reported at every (λ, N) and not part of any verdict: the share of decays ending at the sheet, on the four-point ledge, and elsewhere; and the mean release as a share of 4(λ − 1).

#### Predictions

1. **As λ comes down towards 1:** (a) sharp at every metastable λ, the release shrinking as 4(λ − 1); (b) sharp down to some λ, then the change stalls or slides because the release is too small to drive a front; (c) near 1 the opened patch re-curls, and the tube never converts within the cap.
2. **Where metastability ends at g = 1.5:** (a) below 1.3; (b) between 1.3 and 1.4; (c) between 1.4 and 1.5.
3. **The waiting-time law** is the assistant's arithmetic, not the owner's theory, so it is recorded as ours only and is a check, not a prediction: it holds within 25 % at every metastable λ.

**The owner did not choose among these.** Her position, recorded the same night: λ is above 1 in her theory, probably about 1.25, and only λ > 1 gives a lump. That is recorded as her expectation that a window above λ = 1 exists in which X is stuck for now and releases a lump; it is not a pick among 1 (a) to (c) or 2 (a) to (c).

**Ours, unverified:** 1 (a), because the front at 1.25 ran freely with release 1 per point and nothing in the move costs changes character below 4/3; 2 (b), at about 1.33, where move B takes over and the predicted wait falls through 200 sweeps. And on the scrap, not scored: the share of decays resting on the column rises as λ → 1 and falls with N, following the exact shares above.

#### Verdicts

- **SHARP DOWN TO 1** — metastable and sharp at every λ from 1.05 to the metastable edge, at every size that passes its gates, releasing 4(λ − 1). Consequence: the author's model at exactly 1 is the limit of a family in which the order → order change is sharp, with a release that vanishes there.
- **A FLOOR** — sharp from the metastable edge down to some λ*, and not sharp (stalls, slides or re-curls) below it at every size that passes its gates. λ* is reported; 1.25 was not a lucky point, but the mechanism needs the coefficient at least λ* above 1.
- **INCONCLUSIVE** — anything else.

#### What this cannot show

Anything at exactly λ = 1, where there is no release. Anything at other couplings: g is fixed at 1.5 as in T7, and near λ = 1 a colder g would lengthen the waits beyond the cap. That X is a tube.


#### Reading, 24 September 2026: INCONCLUSIVE by the letter; the change is sharp at every λ where the tube is stuck

`python scripts/analyse_t8.py` (tests `tests/test_t8.py`); figure `docs/papers/curled_torus/fig_lambda.pdf`.

**Per λ, by the rules as written.** 1.05, 1.15, 1.20: **sharp** at every size that passes its gates (1.20, N = 96 fails gate 3 on one decay). 1.10: **unread**, criterion (a) fails at N = 64 (CV 0.64) and N = 192 (1.36). 1.30: **unread**, (a) fails at N = 96, 144, 192 (0.65 to 0.67). 1.35: **unread**, gate 3 fails at every size (2 to 5 decays per size end in states whose energy matches none of the allowed ones) and (a) fails (0.37 to 0.62). 1.40, 1.45: **not metastable** (median f_200 0.28 to 1.12). λ = 1.25 is T7's TWO-STATE CHANGE, not rerun. **Verdict: INCONCLUSIVE.**

**What holds everywhere the tube is stuck (1.05 to 1.35, every size):** predictions (b) and (c), the two orders side by side (95 to 100 % of vertices at d ∈ {1, 2} at half conversion) and one front (the largest converted piece 76 to 100 % of the converted vertices); the release exactly 4(λ − 1) wherever the decay reaches the flat torus. **The metastable edge lies between 1.35 and 1.40**; our prediction put it near 1.33 (2 (b), between 1.3 and 1.4: holds). Near λ = 1 every decay ends at the flat torus (100 % at 1.05); the share ending on a defected sheet rises with λ (13 % at 1.25 in T7b, the same protocol; 21 % at 1.30; 54 % at 1.35). The waiting-time law (ours, a check) holds within 25 % at 1.15 to 1.30 at most sizes and fails near λ = 1 (observed 1.15 to 1.43 times Eq. (2)) and at 1.35, where the mean wait is pressed against the 200-sweep floor.

**A design weakness, owned.** Criterion (a) asks the coefficient of variation of thirty waiting times to lie in 0.7 to 1.3. For exponential waits its standard error at thirty decays is about 0.13 to 0.18, so the band is about ±2 standard errors, and across 28 cells several failures are expected by chance alone. It also interacts with the 200-sweep rest: where the mean wait is only a few times 200, the spread is compressed. **A repair was computed before being proposed** (the CV of wait − 200): it fixes λ = 1.30 at three sizes, overcorrects at N = 64 (1.54), still fails two sizes at 1.35, and leaves 1.10 unchanged, so **it changes no verdict and is not proposed.** The honest reading is that criterion (a) was too tight to be decisive at thirty decays per cell; (b), (c) and the release carry the result.

---

## T9. Bonfire or slush: the tube in a sealed box

**Written 2026-09-22, after T7 and before any sealed run of a tube.** The only sealed runs so far (Update 9) established that a tube with an empty demon never converts and that the spark costs exactly 12 units; none followed a conversion.

### The question

Every T7 run was at fixed temperature: an unlimited bath carried the lump away the instant it appeared. Claims 4 and 5 are about what happens when it cannot. The author's three cases (design brief): wide open, semi-permeable, sealed. In a sealed system the energy a converting region releases stays, and either feeds the change onward — a bonfire — or heats the rest until it stops — the slush of supercooled water — or does something else. T7 says the change is a front releasing 4(λ − 1) per point as it goes; this asks what that front does to its own surroundings.

### The knob that has to be declared, and why

The Creutz demon of `sealed.py` is one number. Its temperature is its mean energy, so a tube releasing N × 4(λ − 1) units into one demon reaches g ≈ N × 4(λ − 1) — 64 at N = 64, λ = 1.25 — against a sheet that melts near g ≈ 3 to 4. A one-demon box cannot hold the lump at any size; the outcome would be set by the bookkeeping and not by the physics. **So the bath has a capacity, C: C demons, each move paying or receiving from one chosen at random.** Energy is still conserved exactly and the demons' mean energy still reads the temperature; C sets how much the temperature rises per unit released, 1/C. This is a modelling choice — how many other degrees of freedom the released energy can go into — and it is the knob of this experiment. It is stated here before a run and it will be scanned, not tuned.

### What will be run

Tubes 16×4, 24×4, 48×4 (N = 64, 96, 192), λ = 1.25, sealed (leak = 0). One demon starts with the spark, 12 units; the rest start empty. C ∈ {1, N/16, N/8, N/4, N/2, N, 2N}. Twenty replicas per (N, C), 30,000 sweeps. Recorded every 25 sweeps: φ, X, the mean demon energy (the bath temperature), and at the end the local-dimension histogram and the pieces of the vertices at each d.

### Observables

1. **Conversion fraction at the end**, f = (φ_tube − φ)/(φ_tube − φ_sheet), and its time course.
2. **Bath temperature**, the mean demon energy, against conversion fraction.
3. **What the product is**, from the final local-dimension histogram: sheet (d = 2 nearly everywhere), sheet with leftover rings (a few clusters at d = 1, as in T7's ledge), tube (d = 1), or melted (mass at d ≥ 3 and at 0).
4. **Energy bookkeeping**: H + Σ demons constant to the last unit, every sweep. A gate, not an observable.

### Predictions, written before looking

*Ours, unverified.* Let g_melt be the coupling at which the λ = 1.25 sheet's φ has fallen to 0.9 on the equilibrium curve — about 3.5 at N = 64 (`cqg_n64_lam125_tempering`). The bath reaches temperature (12 + f N · 4(λ − 1)) / C when a fraction f has converted.

- (a) **A crossover in C, at C* ≈ N · 4(λ − 1) / g_melt** (about N/3.5). For C well above C*, the bath never reaches g_melt: conversion completes and the product is a sheet — bonfire. For C well below C*, the bath passes g_melt while conversion is under way: the converted part melts and the product is disordered — boil-off, not slush. The predicted C* grows in proportion to N.
- (b) **No supercooled-water stall.** In water the released heat brings the mixture to the temperature where ice and liquid have equal free energy, and the change stops there with both present. That needs a coexistence temperature. The tube is above the sheet in energy at every g and, being the more symmetric arrangement, has no more configurational entropy, so I predict no coupling at which the two have equal free energy and therefore no run in which conversion halts with tube and sheet both present, the bath warm but below g_melt, and nothing melting. If such runs occur, prediction (b) fails and the tube has a coexistence temperature I have argued it cannot.
- (c) **Leftover rings survive the bonfire.** For C above C*, T7's ledge — one or two rings of the tube left behind — should appear in the sealed product at about the rate it does at fixed temperature, since the front is the same front.

### Gates

1. Energy conservation exact in every run.
2. With C = 1 and the spark, the tube converts at least once (so the spark is still the spark).
3. Twenty replicas per (N, C).

### Verdicts

- **BONFIRE WITH A THRESHOLD** — (a) holds: complete conversion to a sheet above a C* that scales with N, boil-off below it; and (b) holds.
- **SLUSH** — a band of C in which conversion halts partway with tube and sheet both present, the bath below g_melt, stable to the end of the run, at every size. Prediction (b) fails; claim 5's mechanism is thermodynamic, not kinetic.
- **INCONCLUSIVE** — anything else, including a crossover that does not scale with N.

### What this cannot show

Whether the universe had a bath. What C means physically beyond "how many other places the energy can go". Anything at λ ≠ 1.25 or off the tube.

## T10. Does the leftover grow with the space? Leftover rings in a cold sealed box

**Written 2026-09-22, while T9 runs and before any run of this design.** It is the test VISION S2′ names as the unmet, falsifiable part. **Disclosure of what had been seen when it was written:** T9's N = 64 and N = 96 tables (every C) and the verdict they give; in those, the sheets at C ≥ N/2 hold a leftover ring in 83 to 100 % of replicas, and the number of rings per sheet had not been read. T7b's ledges at N = 144 and 192 sit at released fractions consistent with one to three rings (0.77 to 0.90, where one ring is 0.90 to 0.93). No N = 192 sealed end state had been read. This section adds nothing to T9's verdict items.

### The question

Claim 5 says what did not convert accounts for the rest of the books. If the leftover in a cold sealed box is one ring however large the tube, it is a single defect, negligible at scale, and claim 5 is bookkeeping (VISION Update 10's worry, back again). If it grows in proportion to the space — a density — claim 5 is a statement about the universe's contents. At C = 2N the bath ends near g ≈ 0.5, far below the temperature at which a ring can climb out (at g = 1.5 the ledge lasts 600 to 27,000 sweeps; O13), so whatever the front leaves behind is frozen and the count is the front's own doing: a rate per length swept, or a one-off.

### What will be run

Tubes 16×4, 24×4, 48×4, 72×4 (N = 64, 96, 192, 288), λ = 1.25, sealed, spark 12, **C = 2N**, twenty replicas, 30,000 sweeps, a fresh seed (not T9's). `scripts/run_sealed_tube.py`, unchanged; the same observables as T9.

### Observables

1. **Rings**: the number of connected pieces of vertices at d = 1 in the final state, and the size of the largest.
2. **Excess energy** of the final state over the perfect sheet, H − 0, in units.
3. **Conversion fraction** over the last 3,000 sweeps.
4. Energy bookkeeping, exact. A gate.

### Predictions, written before looking

*Ours, unverified.*

- (a) **The leftover grows with the space.** The mean number of rings rises with N: a straight line through the four means has positive slope at more than three standard errors, and the mean at N = 288 exceeds the mean at N = 64 by more than the replica scatter at either size.
- (b) **Rings are additive.** Excess energy = 14 units per ring when the rings are separate pieces of four. For this energy, which is a sum over edges, two rings sharing no edge contribute independently, so this is a check that "ring" is being read correctly, not a physics prediction. Pieces of eight (two rings adjacent) are recorded, not predicted.
- (c) **Nothing leaves.** The conversion fraction changes by less than 14/N (one ring's worth) over the last 3,000 sweeps in every replica, and the bath ends below g = 1 at every N.

### Gates

1. Energy conservation exact in every run.
2. Twenty replicas per N.
3. Every replica converts (f_final ≥ 0.9). Update 9 found the 12-unit spark sufficient at every size to 192; N = 288 is new. A size at which the spark fails is reported and excluded, and the verdict is then over the sizes that converted, with that said.

### Verdicts

- **THE LEFTOVER GROWS WITH THE SPACE** — (a) and (c) hold.
- **ONE RING, HOWEVER LARGE** — the mean count is within the replica scatter of 1 at every size and the slope is not positive at three standard errors; (c) holds.
- **INCONCLUSIVE** — anything else, including (c) failing (rings leaving within the run, so the count is not the front's).

### What this cannot show

Anything at other C, where the bath is warm enough for rings to come and go and the leftover is thermal rather than kinetic; that is a different question with a different prediction and is not run here. What a ring is for the universe. Whether rings attract one another: (b) reads separated rings, and pieces of eight are only counted.

## T11. Is the leftover ring a seam?

**Written 2026-09-22, after T9 (ASSUMPTIONS O14) and while T10 runs, before any run of this design.** What had been seen: T9's ring counts (one ring in 18 or 19 of 20 coldest-box sheets at every size); T7's departure positions (flat along the tube) and nucleus (two adjacent rings). The ring's position relative to where the change started had not been read anywhere.

### The question

One ring however long the tube is what a seam would leave. The tube is a loop; the front spreads both ways from where it starts; its two ends meet once, on the far side. If that is the mechanism, the ring sits at the antipode of the start. The alternative in the same data is that the ring is the seed's partner, left at the start. Or neither: anywhere.

### What will be run

A cold sealed box as T10 (C = 2N, spark 12 in one demon, λ = 1.25): tubes 16×4 (forty replicas) and 24×4 (thirty), fresh seeds, run in blocks of five sweeps so that the first departure from the tube is caught. Recorded per replica: the columns along the tube of the first non-tube vertices; at the end, the columns of the vertices at d = 1 and the number of rings; the circular distance in columns from the start (the circular mean of the first non-tube columns) to the ring. Each replica runs to 90 % conversion plus 2,000 sweeps, cap 30,000. `scripts/run_seam_check.py`; `scripts/analyse_t11.py`.

### Predictions, written before looking

*Ours, unverified.* Only replicas ending with exactly one ring enter.

- (a) **Seam**: at each size, at least 60 % of single-ring replicas have the ring at a distance of at least three quarters of the half-length from the start, and the median distance is at least that. A ring placed at random would give about 25 %.
- (b) **Not at the start**: fewer than 30 % within 1.5 columns of the start (random: about 19 %).

### Gates

1. Energy conservation exact. 2. At least 15 single-ring replicas per size.

### Verdicts

- **SEAM** — (a) and (b) at both sizes.
- **AT THE SEED** — at least 60 % within 1.5 columns of the start, at both sizes.
- **NEITHER** — anything else that passes the gates.
- **INCONCLUSIVE** — a gate fails.

### What this cannot show

Why a meeting of fronts leaves a ring rather than closing cleanly. Anything at warmer baths, where rings are thermal as well. Anything at other λ. Whether the result carries to a sheet with two large directions, where "the far side" is a line and not a point.

## T12. Does the coarse law govern? (written 2026-09-22, before the runs)

**Why this test exists.** The author reads her picture as a strange loop in Hofstadter's sense: a
coarse level (space, dimensions, matter) made of a fine level (the network), which then acts back on
the fine level. That reading is only worth anything if **the coarse level has laws of its own**. In
physics that has a technical meaning and a standard test: a coarse law is real when it predicts what
the microscopic system does *without* using microscopic detail, and when it keeps predicting it as
the microscopic details are changed. If the coarse description predicts nothing, the strange loop is
a way of speaking and adds no physics, and the honest thing is to find that out before building on
it. Nothing here needs a new knob (S1 untouched).

**The coarse model, written down in full before any run.** A tube part-converted into a sheet is
described by two numbers and nothing else: the fraction f of points converted, and the two fronts
between the orders. Then

    H(f) = H(tube) − Δ · f · N + 2σ ,   with Δ = 4(λ − 1) the gap per point and σ the cost of one front.

Δ is known exactly and is not fitted. σ is one number, fitted once, and must then be the same
everywhere.

**Predictions (ours; no free parameters except σ).**

1. **Linearity.** H against the number of converted points is a straight line through the run, with
   slope exactly −4(λ − 1) per point. Pass: the fitted slope is within 2 % of the exact value at
   every size and coupling.
2. **The front cost does not change with size.** σ read off the intercept is the same at N = 64, 96,
   144 and 192 to within its own scatter. Pass: no trend with N at more than two standard errors.
3. **The front advances at a rate set locally.** A tube's front is a ring of fixed size whatever the
   tube's length, so **points converted per sweep is independent of N**, and therefore the converted
   *fraction* per sweep falls as 1/N. Pass: points per sweep flat in N (no trend at more than two
   standard errors) and fraction per sweep consistent with 1/N.
4. **The coarse law survives a change of microscopic rule.** Metropolis and Glauber acceptance are
   different microscopic dynamics with the same equilibrium. Predictions 1 and 2 must hold for both,
   with the same Δ and the same σ. Rates in prediction 3 may differ between the two; the
   N-independence may not.

**What each outcome means.**

- **All four hold:** the coarse level predicts the microscopic runs without microscopic input and
  survives a change of rule. That is what "the upper level is real" means in physics, and the strange
  loop reading has something under it. It is *not* evidence for the cosmology; it is evidence that
  the two-level description is doing work.
- **1 and 2 hold, 3 fails:** the energy bookkeeping is coarse-grainable but the dynamics are not. The
  upper level describes what states cost and not what happens, which is weaker and must be said.
- **1 fails:** there is no two-number description, the front is not a front in the sense assumed, and
  the whole framing goes back in the box.
- **4 fails while 1–3 hold:** the coarse law is an artefact of one acceptance rule, which would be a
  surprise worth its own investigation, and it would mean the coarse level is not autonomous.

**Fixed before running.** λ = 1.25 (the vision's track; the tube is metastable there and not at 1.5).
g = 1.5 and 2.0. N = 64, 96, 144, 192. Four replicas per cell, both acceptance rules, seeds derived
from one recorded seed. Blocks of 25 sweeps; a run stops when the converted fraction passes 0.98 or
at 20 000 sweeps. Only the stretch between 10 % and 90 % converted is fitted, so that nucleation at
one end and the last defects at the other cannot flatter the fit. Runs that never nucleate are
reported and excluded from the fits; runs that nucleate more than once (two fronts starting
separately) are reported separately, since the coarse model assumes one converted region.

**What would make this test worthless:** fitting σ per size, or per coupling, or dropping runs that
do not fit. σ is fitted once over everything, and every run that nucleated is in the fit.

### T12 VERDICT (2026-09-22, same day): NOT ESTABLISHED

64 replicas, 59 nucleated, 5 never did; 21 of the 59 converted in more than one patch, which is
outside the coarse model's own assumption of a single converted region and is reported separately
below as the pre-registration says.

| Criterion | Result | |
|---|---|---|
| 1 linearity | slope −1.51 to −0.76 per run; median exactly −1.000, mean −0.980 | **FAIL** |
| 2 front cost fixed | σ = 11.3 ± 3.7, no trend with N (one-patch runs) | **PASS** |
| 3 front advances locally | 0.236, 0.163, 0.136, 0.113 points a sweep at N = 64, 96, 144, 192 | **FAIL** |
| 4 same under both rules | Glauber −0.980 / σ 11.2; Metropolis −0.980 / σ 11.3 | **FAIL** on the 2 % bound, though the two rules agree to three decimals |

**Criterion 1 fails on both readings of its own wording.** Taken per replica the worst run is 51 %
off; taken per cell of size and coupling, which is what "at every size and coupling" most naturally
means, the worst cell is 15 % off. There is nothing here for the author to adjudicate, and the
looser reading was computed and is reported precisely so that it cannot be said the strict one was
chosen to suit the answer.

**The failure is not spread evenly, and that is the useful part.** The two coldest, largest cells
land at 0.15 % and 1.03 % of the exact gap. Every badly failing cell is at g = 2.0, where the chain
is warm and "converted" is read off a local dimension that thermal noise makes flicker, and where
conversions also start in several places at once (most warm runs are in the multi-patch group, which
is why those cells hold one run each). So the honest statement is that the coarse energy law is
recovered where the measurement is clean and is not recovered where it is noisy, and **this run
cannot separate a failure of the law from a failure of the proxy.** Doing so needs a cleaner measure
of what has converted, which is a new test and not a reinterpretation of this one.

**Criterion 3 was mis-derived by the assistant and would have been wrong even if it had passed.** It
predicted a rate flat in N. By the same counting that Q13 did for nucleation — a sweep is 2N
attempts, proposals go as N², and the moves that advance a *front* are a fixed handful rather than
one per site — a local front should advance as 1/N in sweeps, not flat. The measured rate follows
neither: it falls roughly as N^−0.7, between the two. So the dynamics are not captured by either
version of the coarse picture, and the defect in the prediction is the assistant's.

**What held that was never registered.** Runs whose sheet arrived in more than one patch give
σ = 25.3 ± 24.5, about twice the 11.3 of the single-patch runs — which is what the coarse model
says should happen, because two converted regions have four fronts and the fit divides by two. The
model got a prediction right that nobody asked it for.

**What this means for the strange-loop reading** (`docs/design/strange_loop_note.md`, item 3): the
claim that the coarse level has autonomous laws is **not established**. What is established is
narrower and still worth something: the cost of a front is one number that does not move with size,
and both acceptance rules give the same two numbers to three decimals, so what the coarse
description does capture is not an artefact of one microscopic rule. The dynamics are not captured
at all.

The draft for the parked menu study is in `docs/parked/PREREGISTRATION_menu_study.md`.

---

## T13. The λ = 1 transition at N = 4p²: an equilibrium jump, or a lattice branch surviving on ascent? (written 2026-09-22, night, before the runs)

### Why this test, now

The model's author replied to our note on 2026-09-22 (paraphrased in `docs/outreach/correspondence_2026-09-22_trugenberger.md`; private). His current view of the transition at λ = 1 is a **hybrid** one: two continuous branches with a jump between them, seen in his own runs at N = 1024 under a protocol of cold ascent, each coupling starting from the previous, smaller one's final state, with 240 sweeps of warm-up and 10,000 sweeps per coupling. Our equilibrium runs at N ≤ 160 (ASSUMPTIONS O10, O12, O17) show no jump in either direction. Two readings are open and this test separates them: **(a)** the jump is an equilibrium discontinuity that appears only at sizes above ours; **(b)** the jump is the lattice branch surviving past the transition on ascent and then collapsing, which is metastability of the protocol and not a property of the equilibrium curve. He also advised N = 4p² with p prime, where he states the ground state is unique; those are the sizes used.

### What will be run

| Choice | Value | Why |
|---|---|---|
| Model | λ = 1, no cap, hard-core rule, Metropolis | His model as he describes it: the full Hamiltonian with the hard-core restriction always imposed. The "cap" is not used anywhere in this test. |
| Sizes | N = 196, 484, 676 (14 × 14, 22 × 22, 26 × 26; p = 7, 11, 13) | His form N = 4p². 1024 is not of that form and is beyond one laptop for tempering; 676 is as far as the budget allows. |
| **Protocol P** (copy of his) | one chain per replica; 40 couplings geometric from g = 12.0 to 1.5 (5.3 % apart); cold descent from a melted torus, then cold ascent from a fresh lattice torus (`heat_start: torus`); 240 sweeps warm-up and 10,000 measured sweeps per coupling; 4 replicas | As close to his stated protocol as his description allows. Not known and therefore assumed: his coupling range (ours brackets the crossover generously), his move set, and that his ascent starts from the lattice torus. |
| **Protocol E** (equilibrium) | parallel tempering by T6's runner, `scripts/run_t6_tempering.py`, which writes the (S, X) histograms (its meta file names T6's pre-registration because the runner is T6's, unchanged; the config's `_purpose` names this section); ladders 9.0 → 2.2 in 20 rungs (196), 7.5 → 2.0 in 30 (484), 7.0 → 2.0 in 36 (676), spacings 7.2, 4.5, 3.5 %; 4 sweeps per round; 5,000 + 25,000 rounds (196), 8,000 + 32,000 (484, 676); **two starts**, every copy melted and every copy the lattice torus; 4, 3 and 2 replicas per start | Rung spacing shrinks as 1/√N so that swaps keep being accepted. The two starts are the equilibrium check: a curve that depends on where it started is not an equilibrium curve. |
| Configs | `configs/t13_seq_n{196,484,676}.json`, `configs/t13_temper_n{196,484,676}_{melt,torus}.json` | Seeds inside. |

### Observables

φ(g) per leg (P) and per start (E); for P the ascent-minus-descent difference at each coupling; for E the melt-minus-torus difference and the spread between replicas; the (S, X) histograms per coupling that the tempering runner writes, for T6's two-hump reading; `swap_rate`, `round_trips`, `tau_int`, `acceptance`; the connectivity columns.

### Definitions, fixed now

- **A jump** in a curve: φ changes by more than **0.25** between two neighbouring couplings that are less than 12 % apart in g. (Our smooth N = 160 curve never moves more than about 0.1 between neighbours at that spacing; Fig. 3 of the 2025 review moves about 0.45 within 7 %.)
- **Hysteresis** (P): at some coupling the ascent φ exceeds the descent φ by more than **0.15**.
- **Equilibrium agreement** (E): the two starts agree within **0.03** in φ at every rung, and replicas agree within 0.03 in the crossover region (0.3 < φ < 0.9).
- **An equilibrium jump**: E shows a jump at the same rung (± one rung) from both starts, with equilibrium agreement, **and** the (S, X) histogram at the nearest rung shows two humps by T6's reading (`scripts/analyse_t6_phi.py`).
- **A metastable branch**: P shows hysteresis and a jump on ascent, while E shows equilibrium agreement and no jump.

### Predictions, written before looking (ours, unverified)

1. **E is smooth and start-independent at every size.** Both starts agree within 0.03 at every rung at N = 196, as they did at 160, and we predict the same at 484 and 676. The crossover (φ = 0.5) moves to lower g with size, roughly as ln N: about 5.4, 4.3 and 3.9 ± 0.5 at 196, 484 and 676, from the capped first look's drift line (ASSUMPTIONS section D; a rough guide, the uncapped curve sits slightly higher).
2. **P shows the lattice surviving on ascent.** Heating from the lattice torus with 240 sweeps of warm-up, the chain stays near φ = 1 past the equilibrium crossover and then collapses within a few couplings: a jump on ascent and hysteresis against descent. Descent agrees with E within 0.05 wherever the single chain still moves (g above about 3) and freezes below that, as in O10.
3. **The ascent jump grows and moves with size:** larger at 676 than at 196, and at a higher g, because the lattice branch's metastability grows with the interface it would have to nucleate.

### Gates

- E: swap rates between 0.15 and 0.6 at every link; `round_trips` at least 5 per replica at 196 and at least 3 at 484 and 676 (the budget at these sizes does not reach T6's 20; the number is reported, and a size below its gate is reported as not converged and its E result is not interpreted); replica spread within 0.03 in the crossover region.
- P: no gate; it is a protocol whose non-equilibrium behaviour, if any, is the thing being looked for. `acceptance` and `tau_int` are reported for every row.

### Verdicts

- **EQUILIBRIUM JUMP** — E meets the equilibrium-jump definition at two or more sizes that pass the gates. Consequence: the author's hybrid reading is reproduced at equilibrium; T6's λ ≥ 1 verdict is reopened at these sizes, and the latent-heat bound is re-measured there.
- **METASTABLE BRANCH** — P shows hysteresis and an ascent jump at two or more sizes, and E shows equilibrium agreement and no jump at those sizes. Consequence: the jump in the 2025 figure and in the 1024-node runs is a property of cold ascent with a short warm-up, not of the equilibrium curve; T6's bound on the latent heat is extended to N = 676 and reported.
- **INCONCLUSIVE** — anything else, including E failing its gates at 484 and 676, or P showing no jump anywhere (in which case his protocol as we copied it does not reproduce his figure, and that is a question back to him rather than a result).

### What this cannot show

Anything at N = 1024 or beyond; the critical scaling that would make a jump "hybrid" rather than first order (no exponents are measured); anything about the hypothesis's own route (the tube), which is not touched by this test; and anything about his code, which we have not seen.

#### Reading at N = 196 under the rules above, 23 September 2026: NO VERDICT — one size of three

All three verdicts require two or more sizes. N = 484 and 676 were still running when this was written, so nothing is decided here; what follows is the first size read against the definitions as originally written, recorded before the amendments below so that the amendments cannot be mistaken for the reading that prompted them.

**Protocol P.** Descent and ascent agree to within 0.004 from g = 12 down to 3.7. Below that the ascent, started from the lattice torus, stays near φ = 1.000 while the descent rises smoothly. **Hysteresis is met:** ascent exceeds descent by 0.159 at g = 3.164 (0.158 and 0.154 at the couplings either side), against 0.15. **A jump is not met as written:** no single step exceeds 0.25 on either leg in the replica mean, and per replica only one of four does (rep 1, 0.737 → 0.991). The largest single step on ascent is 0.172, 0.254, 0.133, 0.209 in replicas 0 to 3.

**Protocol E, melt start: passes every gate.** Round trips 5, 15, 8, 12 against a gate of 5; swap rates 0.202 to 0.575 inside 0.15 to 0.6; replica spread below 0.03 across the crossover. No jump anywhere. Crossover φ = 0.5 at g = 5.90, against prediction 1's 5.4 ± 0.5 — inside, at the upper edge.

**Protocol E, lattice start: fails every gate.** Round trips 0 in all four replicas; swap rates 0.046 to 0.997, outside the gate; replica spread 0.173 at g = 3.19. Reported as not converged and not interpreted, as the gate requires.

**Predictions.** Prediction 1 is half met: E from the melt is smooth, and its crossover is inside the predicted band, but start-independence could not be demonstrated because one start did not converge. Prediction 2 is met in substance and fails on its letter: the lattice does survive on ascent and produces hysteresis, but the collapse does not register as a jump under the per-step definition. Prediction 3 needs the larger sizes.

**The bound.** T6's φ reading on the gate-passing melt run (`scripts/analyse_t6_phi.py t13_temper_n196_melt`) puts any latent heat hiding in a single hump below **0.955 per point at N = 196**, against below 1.30 at N = 100 (T6, amendment 5 verdict). The bound tightens with size.

#### Amendment 1, 23 September 2026 — ENACTED at the author's decision — a jump is measured across a window in g, not between neighbours

**Status: proposed after the N = 196 reading above (text below, as proposed); adopted by the author on 23 September 2026 with the wording in "Enacted wording" at the end of this amendment. No run is repeated and no data is re-collected; only the reading changes.**

**Written after the N = 196 reading above, and it would change that reading. Stated first so it cannot be missed.**

The definition asks how far φ moves **between neighbouring couplings**. The spacing of those neighbours is a choice we made, not a property of the model: protocol P uses 40 couplings from g = 12 to 1.5, so neighbours are 5.3 % apart. On ascent at N = 196 the curve moves from φ = 0.74 to 1.00 — a move of 0.26 — but it takes two couplings to do it, so every single step is below 0.25 and the rule returns "no jump". With 20 couplings (11 % apart) the same collapse would be one step and would count; with 80 (2.6 % apart) it would split four ways and read as smooth. The "less than 12 % apart" clause sets a ceiling on the separation and no floor, so a fine grid dilutes a jump without limit. This is the same shape of defect as the one already on the record in `CLAUDE.md`: a criterion that moves with a quantity we chose rather than with the physics.

**Proposed wording.** A jump in a curve: φ changes by more than **0.25** between two couplings on that curve less than **12 %** apart in g, which need not be neighbouring. Threshold, window and curves are unchanged; only "neighbouring" is dropped.

**The control, run before this was proposed.** A repair is honest only if it does not manufacture jumps in curves that are smooth. Applied to the smooth curves in the same data, the windowed rule returns **0.040** in all four replicas of the gate-passing melt run and **0.060 to 0.064** in all four replicas of protocol P's descent leg — four to seven times below the 0.25 threshold. Applied to the ascent it returns 0.266, 0.281, 0.204, 0.257 where the per-step rule returned 0.172, 0.254, 0.133, 0.209. One further property: at protocol E's rung spacing (7.2 % at N = 196, 4.5 % and 3.5 % above) at most one step fits inside a 12 % window at N = 196, so **this amendment does not change any E reading at that size**; it bears on protocol P, whose grid is fine enough to split a collapse.

**Why this is a post-hoc repair, said plainly.** It was proposed after the data it changes, which this document forbids the assistant to enact. What makes it defensible for Emily to enact is (a) the control above, computed before adoption and reported whichever way it came out, (b) it applies identically to every size, both legs and both protocols, and (c) it removes a dependence on a sampling choice rather than adding a free parameter — there is no tolerance in it to tune. What it costs is stated without hedging: three of four ascent replicas at N = 196 change from "no jump" to "jump" under it, and that is a change in the direction we expected, which is exactly why the control matters more than the argument.

**Enacted wording (the author's decision, 23 September 2026).** A jump in a curve: φ changes by more than 0.25 between two couplings on that curve less than 12 % apart in g, not necessarily neighbouring. All other definitions, thresholds, gates, predictions and verdicts stand as written. `scripts/analyse_t13.py` implements this wording, and reports the per-step value beside the windowed one at every size so that both readings stay visible.

#### Amendment 2, 23 September 2026 — ENACTED at the author's decision — equilibrium agreement is read within the starts that pass their gate

**Status: proposed after the N = 196 reading above (text below, as proposed); adopted by the author on 23 September 2026 with the wording in "Enacted wording" at the end of this amendment.**

**Written after the N = 196 reading above, and it changes which verdicts are reachable. Stated first so it cannot be missed.**

Three sentences of this section lock against each other. "Equilibrium agreement" is defined as a comparison **between the two starts**. The gate says a run below its round-trip threshold is **not interpreted**. The METASTABLE BRANCH verdict **requires** "E shows equilibrium agreement". At N = 196 the melt start passes its gate and the lattice start fails it with 0 round trips in all four replicas, so the clause needs a run the gate forbids interpreting, and the verdict needs the clause. As written, **whenever the lattice start does not mix, METASTABLE BRANCH is unreachable** — although a lattice start that will not mix is exactly what a metastable branch would look like. The test cannot return its own most likely answer. That is a defect in the wording and not a result.

The opposite repair — counting a stalled start as evidence *for* metastability — is proposed and **rejected here**, so that it is on the record as considered. Zero round trips is equally consistent with the sampler being too weak at that size, which is the precise confusion the gate exists to prevent. Reading it as physics would be the motivated choice.

**Enacted wording (the author's decision, 23 September 2026).** Equilibrium agreement (E) is read within the starts that pass their gate: the replicas of a gate-passing start agree within 0.03 in φ in the crossover region (0.3 < φ < 0.9), and where two or more starts pass their gates at a size, those starts agree within 0.03 at every rung. A start that fails its gate is reported as not converged and takes no part in the verdict; its difference from a gate-passing start is reported at every rung as a diagnostic, prominently and with its round trips beside it, and is read as neither agreement nor disagreement. A size at which no start passes its gate is reported as not converged and its E result is not interpreted, as before. Nothing else changes, and in particular the verdicts still require two or more sizes.

**What this does not do.** It does not make the lattice start's failure evidence for anything, and it does not lower the round-trip gate. The proper resolution is a sampler able to mix from the lattice — the neighbourhood move of [T25] Fig. 8, noted in `TASKS.md` T4 as not built — which stays the follow-up and needs its own pre-registration. Until then, a size whose lattice start stalls carries E on its melt start alone, and the stall is reported as an open question rather than an answer.

#### Amendment 3, 23 September 2026 — ENACTED at the author's decision — each replica is a curve, and a majority of them decides

**Status: proposed after the N = 196 reading and adopted by the author on 23 September 2026, both before N = 484 and N = 676 were read. Those two sizes were still running when this was written, so for them this amendment is not post-hoc; for N = 196 it is, and that is why it is here rather than in the original text.**

The definitions say "a jump in a curve" and never say, where a protocol has replicas, whether the curve is the replica mean or each replica separately. At N = 196 the two readings disagree: the replica mean moves 0.211 across a 12 % window and does not jump, while three of four replicas individually move 0.266, 0.281 and 0.257 and do. Both numbers are correct; they answer different questions.

The reason they differ is not noise. Replicas collapse at slightly different couplings, and averaging curves whose step is in different places flattens the step — the same reason one does not average hysteresis loops with different coercive fields and then report that the loop has gone. Under the mean, a collapse that every single run shows can read as no collapse at all, and that failure gets worse with more replicas, not better.

Against that: reading per replica is the reading that returns "jump" at N = 196, which is the answer we expected, and the author is adopting it having been told so plainly.

**Enacted wording (the author's decision, 23 September 2026).** Where a protocol has replicas, each replica is a curve, and the protocol shows a jump at a size when **more than half of its replicas do**. The replica-mean reading is computed and reported beside it at every size, and any size where the two disagree is flagged in the output, so that a reader can apply either. Thresholds, window and everything else stand as written. `scripts/analyse_t13.py` implements this wording.

**What it returns at N = 196:** three of four ascent replicas jump, so protocol P shows an ascent jump, and with hysteresis already met (0.159) prediction 2 is met in full at this size rather than in substance only. Nothing follows for the verdict, which still needs two or more sizes.


#### Reading at N = 196, 484 and 676, 23 September 2026, evening: INCONCLUSIVE — protocol E fails its gate at 484 and 676

All nine jobs finished; `python scripts/analyse_t13.py 196 484 676`, under the three enacted amendments. **The verdict is INCONCLUSIVE by the rule written in advance ("including E failing its gates at 484 and 676").** Both verdicts that name a mechanism need E read at two or more sizes, and E can be read at one.

**Protocol P, his procedure: the lattice branch at every size, growing.** Hysteresis 0.159, 0.292, 0.342 at N = 196, 484, 676, each largest at g = 3.164; ascent jump in 3, 4 and 4 of 4 replicas (replica mean 0.211, 0.321, 0.401). The heating leg leaves φ = 1 at g ≈ 3.3 to 3.5 at every size, while the equilibrium crossover moves down (φ = 0.5 at g ≈ 5.9, 4.3, 3.9). **So the lattice breaks at a coupling that does not move with N, and the curve it falls onto is lower at each larger size, which is why the jump grows.** Prediction 3 is met on size and fails on position: the ascent jump is larger at 676 than at 196, but it does not move to higher g. Descent agrees with the melt-start tempering curve to 0.002 or better at every coupling above g ≈ 3.3 (interpolated between rungs).

**Protocol E: fails its gate at 484 and 676, not interpreted.** Round trips 0 in every replica from both starts. Descriptively, and not as a result: the melt start and the torus start agree to 0.001 in φ at every rung above g ≈ 3.2 (484) and 3.1 (676) and never meet below it, the torus start staying at φ ≈ 1 and the melt start rising smoothly to 0.95. At N = 196 the melt start passes (reading above) and the torus start does not.

**Predictions.** 1: the crossovers came out 5.9, 4.3 and 3.9 against the predicted 5.4, 4.3 and 3.9 ± 0.5, all inside the band; start-independence could not be shown at any size below g ≈ 3.2. 2: met at all three sizes. 3: met on size, fails on position.

**What this leaves.** Above g ≈ 3.2, four ways of producing the curve (both legs of P, both starts of E) agree at every size, so there is no hysteresis there. Below it, no sampler used here reaches equilibrium at 484 or 676, and even at 196 the lattice start never unlocked. Whether the lattice or the defected melt branch is the equilibrium state in that window is the open question, and it is his question about hysteresis. The two ways to answer it are a move that mixes (the neighbourhood swap of [T25] Fig. 8) or a direct comparison of the two branches' free energies; which one, if either, is the owner's decision (HANDOFF section 4).

---

## T15 rung 0. Do the versions exist where the hypothesis says? (written 2026-09-23, before the run)

### Why this test, now

VISION Update 17 reads superposition as the set of undetectably different versions of an arrangement: the renamings that leave every relationship intact. It also names a strain against itself. [T25] Sec. VI.1 calls the melted phase matter, and Q15 measured a melted graph at N = 160 to have **exactly one** renaming — so under Update 17 the object [T25] calls matter is the one object in the model with nothing to be in superposition of.

**The author resolved that strain on 23 September 2026: the melt is not what plays the particle; the structured leftover is** (her words: "why call melted phase matter? That's not matter"). Her reasons, put in order: matter has species, conserved quantities and discrete masses, and a maximum-entropy tangle offers none of them; the leftovers this project actually measured are structured defects of fixed size, 8 to 45 units (O13 third addendum, O15, O16), not blobs of melt; and [T24] itself moves the same way, making dark matter *allotropes* — metastable arrangements — rather than melt. Recorded in VISION as a dated decision.

This rung tests the decision rather than assuming it. If the structured leftover is the wavelike object, it must be the thing that carries versions.

### What will be run

No simulation. Every input is already on disk and every number is exact.

| Object | Where from |
|---|---|
| The leftovers | the 12 saved final states of `results/t7d_lam125_n{64,96,144,192a,192b}_adj/*.npz`, each an (N, 4) neighbour array read by T7 amendment 4 |
| A perfect sheet | `torus(lx, ly)` at each matching size |
| A melt | the same kernel run hot, at each matching size, seeds in the config |

### Observables

For every object, both of these, **reported side by side** (the author's choice, 23 September 2026, fixed before the run because it changes the answer):

- **whole graph** — the renamings of the entire arrangement, sheet and defect together. This is Update 17's claim as written: points that can be swapped without changing *any* relationship. A defect pins a location and destroys the sheet's translations, so this number is expected to be small.
- **defect only** — the renamings of the subgraph induced on the vertices whose local dimension is not 2. This isolates the object, but a defect is not a thing on its own, so it measures something slightly weaker than the claim.

And the **Laplacian spectrum** (eigenvalues of D − A) of each defect, to ask whether the distinct leftover types have distinct frequencies. `graphity.small_graphs.log_automorphisms` gives the counts; `graphity.dimension.local_dimension` names the defect vertices.

### Definitions, fixed now

- **A version exists** when the renaming count is greater than 1; the count is reported as an integer wherever it is small enough to be exact, and as its logarithm otherwise.
- **Two spectra differ** when their sorted non-zero eigenvalues differ by more than 1e-9 in any position, or differ in length. Exact arithmetic on integers; the tolerance is for floating point only.
- **A leftover type** is a defect structure as `scripts/analyse_t7_states.py` names it from the wiring, not from a count (CLAUDE.md: read positions before naming a geometry).

### Predictions, written before looking (the author's, 23 September 2026)

**Chosen from four options put to her, of which two would have counted against Update 17.** She chose the strongest.

1. **A remnant in a sheet has more than one renaming**, on both counts.
2. **A melt has exactly one**, at every size (this half is close to settled: Q15 measured it at N = 160).
3. **The distinct leftover types have distinct Laplacian spectra** — the frequency labels the type, which is what "a particle is an allowed vibration of a small closed loop, and the frequency sets its type" requires.

### Gates

None beyond arithmetic. Every count is exact and every input is committed. The one check: `log_automorphisms` must return 0 (ln 1) for a graph known to be rigid and the published 320 for the N = 160 sheet of Q15, or the tool is wrong and nothing else is read.

### Verdicts

- **VERSIONS EXIST AND LABEL TYPE** — all three predictions hold. Update 17's first two steps survive their cheapest test, and rung 3 has a target to be designed against.
- **VERSIONS EXIST** — 1 and 2 hold, 3 fails. The leftover is wavelike but frequency does not label species; the particle-type half of Update 17 is withdrawn or redesigned.
- **NO VERSIONS IN ANYTHING REAL** — 1 fails: remnants have exactly one renaming, as the melt does. Then only idealised perfect arrangements carry versions, and VISION Update 12 already says nothing is ever in those. Update 17 loses its footing in this model and should say so.
- **INCONCLUSIVE** — anything else, including the tool failing its check.

### What this cannot show

Anything about quantum observations: no experimental data enters this test and none is compared to. Whether these versions behave like superposition (rung 1 asks whether the time-fractions match the counts; rung 2 asks about measurement). Anything about Bell correlations, which need a notion of measurement in the model that does not exist. And, as everywhere in this project, anything about the real universe.

### Reading, 2026-09-23, the same morning (`configs/t15_rung0.json`, `scripts/analyse_t15_rung0.py`, `results/t15_rung0.csv`; the analyser's known-answer tests in `tests/test_t15_rung0.py`)

**PRE-REGISTERED VERDICT: INCONCLUSIVE.** Prediction 2 holds. Predictions 1 and 3 fail by the letter, each on a point stated below that is the author's to rule on. Nothing in the definitions was changed after the numbers were seen; the two readings that would change the verdict are proposed here and not enacted.

**Gate.** `log_automorphisms` returned 320 for the 16 × 10 sheet and 1 for Q15's melt (seed 2024); the helper used on defect subgraphs, which the named tool cannot take, returned 320 on the same sheet. Every whole-graph count below was also re-derived with a second isomorphism engine (networkx VF2++, a separate implementation) and agreed exactly.

| object | N | whole graph | defect only | pieces off the sheet, read from the wiring |
|---|---|---|---|---|
| N64 rep 25 | 64 | 2 | 32 | two closed loops of four |
| N96 rep 3 | 96 | 8 | 1152 | two 3-cubes |
| N96 rep 10 | 96 | 2 | 576 | a 3-cube; four single edges (two at d = 1, two at d = 3) |
| N96 rep 20 | 96 | **1** | 48 | four single edges (two at d = 1, two at d = 3); a point at d = 1; a point at d = 3 |
| N96 rep 23 | 96 | 4 | — | none: flat everywhere (S = N, X = 4); takes no part |
| N144 rep 3 | 144 | 16 | 32 | two closed loops of four |
| N144 rep 5 | 144 | 224 | 32 | two closed loops of four |
| N192 rep 3 | 192 | 2 | 96 | a closed loop of four; four single edges |
| N192 rep 5 | 192 | 2 | 576 | a 3-cube; four single edges |
| N192 rep 8 | 192 | 4 | 36864 | two 3-cubes; a closed loop of four; two open lines of three |
| N192 rep 20 | 192 | 16 | 32 | two closed loops of four |
| N192 rep 22 | 192 | 2 | 96 | a closed loop of four; four single edges |
| perfect sheet | 64 / 96 / 144 / 192 | 256 / 192 / 576 / 384 | 1 | none (4N for a square torus, 2N otherwise) |
| tube, the start of every decay | 64 / 96 / 144 / 192 | 128 / 192 / 288 / 384 | same | every point is at d = 1 (2N) |
| melt | 64 / 96 / 144 / 192 | 1 / 1 / 1 / 1 | 1 | |

"Closed loop of four" is the piece `analyse_t7_states.py` names the four-point remnant; "3-cube" is its "8 at d = 1"; each identification was made by direct isomorphism (networkx) against the named graph, not from a count or a spectrum. The twist of O15 (two at d = 1, two at d = 3) never appears as one piece: its two pairs are not adjacent, so the induced subgraph shows it as two single edges.

**Prediction 1 — FAILS by the letter.** Whole graph > 1 in 10 of 11 states with a defect; defect only > 1 in 11 of 11. The exception is N = 96 replica 20: two twists and a separate two-point fragment, three different defects at generic positions, and no renaming of the whole survives. **What the whole-graph renamings are** (read, not assumed): in every state they move the sheet points as well as the defect, and no renaming other than the identity fixes every sheet point. They are the sheet's own symmetries that happen to survive where the defects sit. A single symmetric defect keeps a reflection or two (2, 4); two identical loops at symmetric positions keep more (16; and 224 at N = 144, a group of order 2⁵ · 7 acting on every point, confirmed by both engines and not read further); three different defects keep none. So the whole-graph count measures the symmetry of the arrangement of the world, not anything the object carries. *Post-hoc, the author's call:* read prediction 1 per remnant type rather than per state, under which every state containing a closed loop of four (7 of 7) has more than one renaming on both counts; or leave the letter, which says that a world with three different things in it has exactly one version, as the melt does.

**Prediction 2 — HOLDS.** Exactly one renaming at N = 64, 96, 144 and 192, on both counts.

**Prediction 3 — FAILS by the letter, and each failure is between names, not between spectra.** The three clashes are an edge at d = 1 against an edge at d = 3 (both 0, 2), a point at d = 1 against a point at d = 3 (both 0), and an open line of three at d = 1 against one at d = 3 (both 0, 1, 3): the composition name carries d, and the induced subgraph has no d in it. By wiring the pieces are of five kinds, and their spectra are pairwise distinct: the closed loop of four (0, 2, 2, 4; frequencies √2, √2, 2, exactly as VISION Update 17 computed for such a loop before any leftover was read; 4 renamings within sides, 8 in all), the 3-cube (0, 2, 2, 2, 4, 4, 4, 6; 24 within sides), the open line of three (0, 1, 3), the single edge (0, 2) and the single point (0). *Post-hoc, the author's call:* type by wiring, under which prediction 3 holds; or by the composition name as the definition says, under which it fails.

**Not claimed.** That any of this is superposition; rung 1 asks whether the counts are what the loop's time-fractions equal. What the 224 is. The defect-only count treats isomorphic fragments as interchangeable, so 576 at N = 96 replica 10 includes the 4! orderings of four single edges that the whole graph tells apart by d; it is the pre-registered number, kept with the same-side rule, and the any-side count is beside it in the file.

---

## T15 rung 3a. GHZ on three linked loops of four: is there an instruction set? (written 2026-09-23, before any construction exists)

### Why this rung, and why now

The author asked, after rung 0, why the model cannot be tested against a quantum prediction directly. The answer is that GHZ can be, and that it needs nothing from the other rungs: it is a yes/no question about which outcomes can occur at all, never about a probability, so rung 1's validation of "probability equals count" is not a prerequisite. The design is section 3 of `docs/design/quantum_loop_design.md` (rung 3a), made concrete here with what rung 0 found this morning about the loop.

**The loop, as read (rung 0, and the wiring read the same morning).** The four-point remnant is a closed loop of four points, one column of the tube that stayed curled while the columns round it opened. Each of its four edges carries three squares (the loop itself and one square to either side), each of its points keeps exactly one open pair (d = 1), and eight sheet points (d = 2) form a collar round it. It occurs at three energies, 4, 9 and 14 units at λ = 1.25, according to whether none, two or four collar edges carry a third square (`t7d` N = 144 replica 3; N = 64 replica 25 and N = 144 replica 5; the cold-box remnant of O16). Its renamings within sides, alone, number 4: the identity, the swap of its two side-0 points, the swap of its two side-1 points, and both. That is the object this rung is built from.

**Two obstructions, found while fixing the definitions below, the same morning and before this section was committed.** The first draft defined a loop as a 4-cycle every edge of which lies in three squares, and a link as one edge between two loops. Both are ruled out by hand, so the definitions were changed before anything was built or computed. *(1) Hard-core.* Let loop A carry a link edge a0–b0 to loop B, and let a0's loop edges a0–a1 and a0–a3 each lie in three squares. The two side squares of a0–a1 must use a0's two other neighbours, b0 and a collar point p, one each (two squares through the same pair would give a1 and that neighbour three common neighbours). The square through b0 is (a0, a1, z, b0) with z a common neighbour of a1 and b0; z cannot be a point of B without a second link, so z is b0's fourth neighbour x, and x ~ a1. The same for a0–a3 gives x ~ a3. Then a0 and x have the three common neighbours a1, a3, b0, which the hard-core rule forbids. So **two loops with three-square edges cannot be joined by an edge.** The model's own 9-unit remnant has one loop edge in two squares, so the three-square condition was never the right definition of the object. *(2) Parity.* For a loop's swap of its two side-0 points to survive as a renaming of the arrangement, its links must sit at those two points (a swap must carry a link to a link). A link edge changes side; moving to the swap partner within a loop does not. Round a triangle of link edges A → B → C → A the side therefore changes three times and must come back to itself, which is impossible. So **a symmetric triangle of loops cannot be linked by edges.** A link that is a shared point changes side twice per link and closes.

### Definitions, fixed now

- **A loop** is a closed loop of four points, a 4-cycle, which in this model is one square; its two side-0 points and its two side-1 points. No condition on how many squares its edges carry is imposed (see obstruction 1). What a loop must have is its own four renamings within sides, realised by the arrangement it sits in: acceptance condition (c) below.
- **A link** between two loops is one point adjacent to exactly one point of each: a shared collar point, not an edge (see both obstructions). Three loops A, B, C are **pairwise linked** when each pair shares exactly one link point, the three link points are distinct, and no other point is adjacent to more than one loop.
- **A detector** is a rigid defect, meaning a connected piece off the sheet with exactly one renaming within sides on its own, joined to a loop point by one edge. Attaching it is one switch: the loop point's collar edge that is not a link is replaced by an edge to the detector, and the detector's freed edge goes to the freed collar point, so every degree stays four. The graph after attachment is a different graph, and it is that graph whose renamings are counted. The same detector is used at every loop and in every context; what it is, is stated when built, and its rigidity is checked by counting before it is used.
- **A setting** is which point of the loop the detector is joined to: setting 1, a point on side 0; setting 2, the point on side 1 adjacent to it, a quarter of the way round. The two points of a setting's side are the pair the loop's own renaming swaps.
- **An outcome** is which of that swapped pair the detector's point is, in the naming: red for the point named first when the arrangement is written down, green for its swap partner. Formally, for a context (three settings, one per loop) the renamings of the whole arrangement with all three detectors attached are listed; the **support** of the context is the set of colour triples (one per loop) that some renaming carries the reference triple to. Before any detector attaches, every naming is one class; each detector splits it, and a triple is in the support exactly when some naming realises it.
- **The four contexts** are 111, 122, 212, 221, as in [Mermin90].
- **An instruction set** is an assignment of a colour to each of the six (loop, setting) pairs. It **respects** a context when the triple it gives for that context lies in the context's support. The arrangement is **strongly contextual** when no instruction set respects all four contexts at once ([AB11]'s strong contextuality, checked by trying all 64 assignments).
- **Compatibility**: the set of colours that loop A can show under setting 1 must be the same whichever settings B and C have. If it is not, the construction signals at the level of supports, and no verdict on contextuality is issued.

### What will be run

1. **Construction** (exact search, by hand and by program; `is_valid` with the hard-core rule; no chain). Acceptance, fixed now: **(a)** a valid, connected state of N points, N stated when built; **(b)** three loops pairwise linked as defined; **(c)** with no detector attached, the renamings of the whole arrangement within sides include, for each loop, one that swaps its two side-0 points and one that swaps its two side-1 points, so that every setting has two outcomes; **(d)** reported, not required: N, the energy at λ = 1.25, the histogram of d, and whether every single switch out of it raises the energy. "In a sheet", every point off the loops, links and collars at d = 2, is what the picture wants and is reported; if the smallest arrangement found is not sheet-like, that is said. The full adjacency is committed in `results/` with the config that names it. If no arrangement meeting (a) to (c) is found, the search is stated (what was tried, how far) and the verdict is NO VALID ARRANGEMENT.
2. **The detector**, built and its rigidity counted.
3. **The four contexts**, each a rewiring of the arrangement; for each, `is_valid`, then every renaming within sides of the whole arrangement, then the support.
4. Compatibility, then the instruction-set check over all 64 assignments.

### Prediction (the author's, 2026-09-23, chosen before any construction exists)

**Strongly contextual:** the 111 context's support contains no triple with an odd number of red, while each of 122, 212 and 221 contains only triples with an odd number of red, so that no instruction set respects all four. This is the quantum row of Table 3 in the design brief. *Recorded beside it, ours, from the brief:* our own expectation is the classical row, because the renamings of a fixed arrangement are a hidden variable; the one route to her prediction is that the three attachments, being three rewirings under the hard-core rule, leave a different set of renamings than any single attachment does.

### Verdicts

- **STRONGLY CONTEXTUAL** — compatibility holds and no instruction set respects all four supports. The author's prediction holds; the counting picture reproduces the strongest non-classical fact there is, in a model with no phase in it.
- **CLASSICAL** — compatibility holds and some instruction set respects all four supports. The picture is the symmetry of identical points and no more; Part V of the public document is restated as such.
- **NO VALID ARRANGEMENT** — step 1 finds no valid arrangement, the search having been stated (what was tried, how far). The rung stops as a result.
- **INCONCLUSIVE** — a context cannot be built (a detector attachment invalid under the hard-core rule), compatibility fails, a support is empty, or the detector is not rigid.

### What this cannot show

Any measured number: the test is dimensionless and compares supports, not probabilities or masses. Interference, which needs a phase the model does not have. That the loops were "made in one event": the arrangement is built, not grown, and how three linked loops would come to exist is not modelled. Anything about the real universe. A positive result is a structural match to one quantum fact and would be reported as exactly that.

### Reading, 2026-09-23, about an hour after the section above was committed: settled at the design stage, by argument, before any arrangement was built

**Nothing was built and no context was computed.** Stage 1 was started: an exhaustive completion search at the smallest size the definitions allow, which the hard-core rule puts at 36 points (each loop's two side-1 points need four distinct collar points, since a shared one would give them three common neighbours). It found valid completions and none meeting condition (c) in the time given, and was stopped when the following was seen.

**The argument.** An outcome, as defined above, is read from a renaming σ of the arrangement: red if σ fixes the setting point, green if σ carries it to its swap partner. Renamings that carry a loop onto another loop define no outcome and are set aside; the rest, call them G_loops, act on each loop as one of that loop's four renamings within sides, so each σ fixes or swaps A's side-0 pair, fixes or swaps A's side-1 pair, and likewise for B and C. **Each σ is therefore a complete instruction set: it assigns a colour to all six (loop, setting) pairs at once.** The support of a context is the set of colour triples that the elements of G_loops give when read at that context's three setting points. Attaching the detectors decides which renamings survive into the measured graph, and that is the partition of G_loops into outcome classes; but a class's colour is the colour of any of its members, so survival changes the classes and never the colours. Every σ respects all four supports, an instruction set exists for every arrangement, and compatibility holds by construction. The one thing that can go wrong, a detector that fails to pin its point so that a class carries two colours, leaves the outcome undefined (INCONCLUSIVE); it cannot make the supports contextual. The same argument gives rung 3b's answer without a construction: with equal-weight namings, the probability of a colour triple is the fraction of G_loops carrying it, a probability distribution over instruction sets, which is a local hidden-variable model in Bell's sense, so S ≤ 2 for every arrangement.

**VERDICT: CLASSICAL, for every arrangement in which the outcomes are defined, by argument.** The author's prediction fails. The pre-registered verdict names a computed arrangement; what is established is stronger, and building one would add nothing. The brief said in advance what this means (`docs/design/quantum_loop_design.md`, section 5): "Rung 3a: the 111 context shows an odd number of red, for every construction tried … Any of these ends the quantum leg of the hypothesis as stated, and the public document's Part V would then be a description of identical-particle symmetry and no more."

**What it closes and what it does not.** It closes every test in which the versions are the renamings of one fixed arrangement and a measurement reads them: the naming is a hidden variable, and Bell's theorem applies, exactly as the brief's "honest expectation" said and now for a reason rather than a hunch. It does not touch rungs 0 to 2, which test the counting and not Bell. It does not touch rung 4, interference, which was always going to need a dynamical rule and a VISION decision. And it does not touch a picture in which the versions are versions of *histories* rather than of arrangements ([Gorard20]'s multiway systems, not read), which is a different hypothesis from Update 17's and would need its own statement. *Ours, unverified: a short argument, unreviewed by a physicist.*

**Recorded as a lesson.** The fork in the brief, "if the joint attachments decide which namings survive … the supports can be the quantum ones", was wrong as written: survival changes the classes, not their colours. It should have been checked before the section above was written, and it was checked about an hour after. The two obstructions recorded above stand on their own and are still true.

---

## T15 rung 0b. Is the closed loop of four a resonator inside the sheet? (written 2026-09-23, before the run)

### Why this rung, and why now

Update 17 says a particle is an allowed vibration of a small closed loop. Rung 0 found the loop, a closed loop of four that is one column of the tube left curled, and its vibrations in isolation: Laplacian eigenvalues 0, 2, 2, 4, frequencies √2, √2, 2. Rung 3a showed that counting versions cannot give quantum correlations, and `docs/design/amplitude_rule_brief.md` says the missing ingredient is a rule for combining amplitudes, which the author chose the same day to hold until this rung has run. This rung asks the question any such rule would need answered first: **when the loop sits in a sheet, does it still vibrate as a thing of its own?** A resonator in a sheet is a localised mode of the whole arrangement's Laplacian; a defect that merely scatters the sheet's own modes is not one. Counting and the wave rule share the Laplacian, so this needs no decision.

### What will be run

No simulation. Inputs: every saved resting state of T7 amendment 4 that contains at least one closed loop of four (`results/t7d_lam125_n*_adj/*.npz`; by rung 0's reading, seven of the twelve: N = 64 replica 25; N = 144 replicas 3 and 5; N = 192 replicas 3, 8, 20 and 22). States with a 3-cube are read beside, for the cube, and take no part in the verdict. Controls: the isolated loop of four; a perfect 12 × 12 sheet with an eight-point set made of two disjoint squares; and, in each leftover state, twenty random eight-point sets, seeds in the config.

### Definitions, fixed now

- **The operator** is L = D − A of the whole arrangement. Eigenvalues are grouped within 1e-9 into eigenspaces. The constant mode, λ = 0, is excluded: it belongs to the whole sheet.
- **Localisation** of an eigenspace on a point set S is the largest eigenvalue of that eigenspace's projector restricted to S: the most weight any unit vector in the eigenspace can carry on S. It is 1 exactly when some mode lives on S alone, and a mode spread evenly over N points carries |S|/N. This is basis-independent, which matters because two identical loops in one sheet share their modes in symmetric and antisymmetric pairs.
- **A mode is localised on the loops** when its eigenspace has localisation at least 0.5 on the union of the state's loop-of-four points (8 points of 64 to 192, so 0.04 to 0.125 if spread evenly). The union, not one loop, for the reason just given; the per-loop number, and the number on loops plus their collars, are reported beside.
- **At the isolated frequency** means an eigenvalue within 0.25 of 2 or of 4.
- **Per state:** ISOLATED when localised modes exist within 0.25 of both 2 and 4; RETUNED when localised modes exist but not at both; DISSOLVED when no localised mode exists.

### Prediction (the author's, 2026-09-23, chosen from three options)

**They survive, localised on the loop, at the isolated frequencies:** every loop-of-four state is ISOLATED. *Recorded beside it, ours:* a curled column inside an opened sheet is a piece of tube, and a tube's own modes are a cylinder's, so some retuning by the collar would not surprise us; we make no prediction of our own.

### Gates

The isolated loop must give localisation 1 at eigenvalues 2 and 4. The perfect sheet with the two-square set must give localisation below 0.5 at every eigenvalue. In every leftover state all twenty random eight-point sets must stay below 0.5 at every eigenvalue. If any gate fails the threshold does not discriminate and nothing else is read.

### Verdicts

- **RESONATOR AT THE ISOLATED FREQUENCIES** — every loop-of-four state is ISOLATED. The prediction holds; "a particle is a vibration of a small closed loop" holds structurally in this model.
- **RESONATOR, RETUNED** — every state has a localised mode, and not every state is ISOLATED.
- **NOT A RESONATOR** — every state is DISSOLVED. The loop is a defect, not a resonator, and the particle picture fails here whatever rule combines amplitudes.
- **INCONCLUSIVE** — any other mix of states, or a gate failing.

### What this cannot show

Which rule combines amplitudes: both share the operator. Anything dynamical: an eigenvector is a standing pattern, not a motion. Anything about real particles. The 3-cube's modes are reported and not judged.

### Reading, 2026-09-23, the same afternoon (`configs/t15_resonator.json`, `scripts/analyse_t15_resonator.py`, `results/t15_resonator.csv`)

**PRE-REGISTERED VERDICT: INCONCLUSIVE by the letter, and the prediction fails: no state is ISOLATED.** Six of the seven loop-of-four states are DISSOLVED; the seventh is RETUNED, at the threshold. Gates: the isolated loop gives 1.000 at eigenvalues 2 and 4; the 12 × 12 sheet gives 0.444 at most; every random eight-point set in every state stays below 0.5 (the largest, 0.472, is in the one RETUNED state).

| state | loops | most weight any mode carries on the loops (eigenvalue) | even spread | with the collars | class |
|---|---|---|---|---|---|
| N = 64 rep 25 | 2 | 0.249 (0.16 and 7.84) | 0.125 | 0.670 | DISSOLVED |
| N = 144 rep 3 | 2 | 0.111 | 0.056 | 0.307 | DISSOLVED |
| N = 144 rep 5 | 2 | 0.511 (2.10 and 5.90); 0.501 (2.79 and 5.21) | 0.056 | 0.586; 0.946 | RETUNED |
| N = 192 rep 3 | 1 | 0.057 | 0.021 | 0.169 | DISSOLVED |
| N = 192 rep 8 | 1, and two cubes | 0.154 | 0.021 | 0.444 | DISSOLVED |
| N = 192 rep 20 | 2 | 0.083 | 0.042 | 0.247 | DISSOLVED |
| N = 192 rep 22 | 1 | 0.169 | 0.021 | 0.475 | DISSOLVED |

**What the numbers say, plainly.** In six states of seven no mode of the whole arrangement carries more than a quarter of its weight on the loop, and in four of them no more than about twice what an evenly spread mode would carry. The loop's own vibrations at 2, 2 and 4 do not survive its embedding: they dissolve into the sheet's modes. Eigenvalues near 2 and 4 do occur in the whole spectrum (2.009, 3.94 and 4.06 at N = 192 replica 3), with loop weight 0.05; those are the sheet's modes passing through the loop, not the loop's own. The one RETUNED state crosses the threshold by 0.001 and 0.011, in the same state where random eight-point sets reach 0.472, so its localisation is barely distinguishable from what that state's symmetry (224 renamings, rung 0) hands any eight points. **The closed loop of four is not a resonator in this model.** Its eigenvalue pairs are mirror images about 4, as every bipartite spectrum's are.

**Reported beside, post-hoc, not judged: where anything resonates, it is the cap, not the loop.** With the collars included (twelve points per loop), N = 144 replica 5 has a mode carrying 0.946 of its weight at eigenvalues 2.79 and 5.21, and N = 64 replica 25 one carrying 0.670 at 0.16 and 7.84; the other five reach 0.17 to 0.48. So a resonator exists in two states of seven, and it is the curled column together with its double-wound collar, at frequencies that are not the isolated loop's. Whether the object of Update 17 should be the cap rather than the loop is the author's call and would be a new pre-registration, not a re-reading of this one.

**The 3-cube**, beside: at most 0.36 of any mode's weight on the cube's points, at eigenvalues 3.3 and 4.7, against the isolated cube's 2, 4 and 6. Not a resonator either, by the same measure.

**Not claimed.** Anything dynamical. That no combining rule could rescue the picture: the wave rule was held pending this, and what this says is that the loop alone is not the object such a rule would act on. Anything about real particles. `pr_best` is "inf" in the file where an eigenspace has no weight on the loops at all; it is a faithful output, not an error.

**A process fault, owned.** The commit that timestamped this section (36924d1) was made with one test failing. The test assumed an 8 × 8 sheet keeps every mode below 0.5 on eight points, which is false for so small and so symmetric a sheet (a degenerate eigenspace of dimension d can put d · 8/64 on them), and the tail of the test output hid the failure. The pre-registered gate is at 12 × 12, where the value is 0.444, and it passed. The test was corrected in the commit that carries this reading; nothing in the definitions or the data changed.

## T16. The correlation length of [KTB19] Fig. 9a at N = 4p², with the susceptibility (written 2026-09-23, evening, before the runs)

### Why this measurement, and what it is not

The model's author asked for it in his reply of 23 September (private; paraphrased in `docs/outreach/correspondence_2026-09-22_trugenberger.md`): the correlation-length plot of [KTB19] Fig. 9a, for a talk he gives on 5 October, and whether replica exchange can show that cooling and heating give the same curve. **It is a measurement made at his request on the disorder → order route, the published question, not the hypothesis's (VISION Update 13).** It tests no claim of VISION, and there is no prediction of the owner's to record; she asked for it to be run. It is labelled exploratory in every config.

### What will be run

| Choice | Value | Why |
|---|---|---|
| Model | λ = 1, no cap, hard-core rule, Metropolis | His model, as in T13. |
| **Protocol E** (equilibrium) | parallel tempering from melted tori, T13's N = 196 ladder for every size (20 rungs, g = 9.0 → 2.2), 4 sweeps per round, 5,000 + 25,000 rounds, a snapshot of every coupling every 25 rounds (1,000 per coupling); N = 36, 100, 196 (6 × 6, 10 × 10, 14 × 14; p = 3, 5, 7); 4 replicas | The sizes at which tempering mixes: T13 found 5 to 15 round trips at 196 and none at 484 or 676. |
| **Protocol P** (his procedure) | T13 protocol P exactly (40 couplings g = 12 → 1.5, 240 sweeps warm-up, 10,000 measured, cold descent from a melt then cold ascent from the lattice torus), a snapshot every 100 sweeps (100 per coupling); N = 196, 484, 676; 4 replicas | The sizes he can use for a talk, read only where they are trustworthy (below). |
| Code | `src/graphity/correlation.py` (ASSUMPTIONS Q19), `scripts/run_t16_correlation.py`, configs `configs/t16_{temper,seq}_n*.json`, one process per replica | Seeds inside the configs. |

### Observables

Per row (size, replica, protocol, leg, coupling): φ; the susceptibility χ = N var(φ); ξ / diameter by [KTB19] Eq. (4.15) under Q19's choices, its mean and standard error over snapshots; the same computed once from the snapshot-averaged C(r); the counts of snapshots skipped for no fluctuation or no usable distance; the averaged C(r) itself (stored).

### Rules for reading, fixed now

- **E gate**, as T13: every replica makes at least 5 round trips and every swap rate lies in 0.15 to 0.6. A size that fails is reported and not read.
- **P is read only where it is at equilibrium by its own evidence**: at couplings where the replica-mean φ of the cooling and heating legs differ by less than 0.03. Elsewhere its rows are reported as the protocol's branches, not as equilibrium. (At N = 484 and 676 in T13 this held for g above about 3.3, where both tempering starts agreed as well.)
- **Peaks.** For each size and protocol, the coupling and height of the largest χ and the largest ξ / diameter among the rows that are read. A peak at the first or last read coupling is "at the edge" and not a peak.
- **Divergent tendency** (the words of [KTB19] Fig. 9): the peak height of ξ / diameter rises with N across every read size, by more than two standard errors between the smallest and the largest. **None**: it does not. **Not readable**: a peak at the edge, or more than half the snapshots at the peak coupling skipped.
- **The author's hysteresis question**, answered as far as these runs allow: for P at each size, the largest heat-minus-cool difference in φ and in ξ / diameter; for E, one start only, so this run adds nothing to T13 on hysteresis below g ≈ 3.2, and the write-up says so.

### Our expectation (ours, unverified)

χ peaks near the crossover, at g ≈ 5.9, 4.3 and 3.9 for N = 196, 484, 676 (T13's measured crossovers), with a peak height that grows with N. ξ / diameter under the literal definition will be noisy, because it is read from only 5 to 26 distances, and its peak, if any, will sit near χ's. Whether its height rises with N we do not know; Kelly's thesis warns that correlation lengths may not be well defined in this model.

### What this cannot show

The order of the transition: a correlation length that grows over three sizes is what a continuous transition predicts and does not exclude a weak first-order one, and three sizes fit no exponent. Anything below g ≈ 3.2 at 484 and 676 on the heating side, where T13's samplers do not mix. Anything about the tube.

#### Reading, 23 September 2026, night: replica exchange readable at one size only; his procedure NONE

`python scripts/analyse_t16.py` (rules as pre-registered; tests in `tests/test_t16.py`); figure `docs/figures/t16_correlation.png`.

**Protocol E gate: N = 196 passes; N = 36 and 100 fail, on the swap-rate ceiling only.** Round trips 529 to 626 (N = 36) and 44 to 60 (N = 100), far above the gate of 5, but swap rates reach 0.889 and 0.689 against the ceiling of 0.6. N = 196: 9 to 13 round trips, swap rates 0.195 to 0.577. **The fault is the assistant's drafting:** the ceiling was copied from T13, where each size had its own ladder, and here one ladder serves three sizes, so the smaller ones swap more than they need to. A high swap rate costs efficiency, not correctness. **Proposed amendment, not enacted (the owner's decision): drop the ceiling.** What it would return, computed before any decision: at N = 36 and 100, Eq. (4.15) runs away to 10^10 to 10^12 at several rungs (single snapshots in which C(r) is just below 1 at some distance), so the peak heights would fall with N and the reading would be NONE, as it is for P. **The amendment changes no verdict.** With one readable size, E's tendency is NOT READABLE.

**Protocol P, read where its legs agree (26, 26 and 27 of 40 couplings at N = 196, 484, 676): NONE.** Peaks of ξ / diameter: 0.645 ± 0.174 at g = 8.71, 1.339 ± 0.536 at g = 8.71, 1.170 ± 0.844 at g = 1.58 (half its snapshots skipped, the lattice). Not rising at each step, and the largest minus the smallest is 0.525 against 2σ = 1.724.

**Susceptibility.** Peaks 0.183 (g = 6.33), 0.181 (g = 4.60), 0.180 (g = 4.60) for P at 196, 484, 676; 0.183 (g = 7.21) for E at 196.

**Our expectation, against the result.** χ peaks near the crossover: held (peaks at g ≈ 6.3, 4.6, 4.6 against crossovers 5.9, 4.3, 3.9). χ's peak height grows with N: **failed**, flat at 0.18 across a size range of 3.4. ξ noisy: held.

**Exploratory, and labelled so because it is not among the reading rules.** (1) The averaged C(r) is 0.10 to 0.23 at r = 1, 0.01 to 0.04 at r = 2, and within about ±0.01 of zero beyond, at every coupling from g = 12 to 1.5 and at every size; it does not reach further near the crossover. (2) The largest contributions to Eq. (4.15) come from distances near the diameter, where few pairs exist (e.g. C(8) = 0.22 at N = 196, g = 9), and from snapshots in which C(r) is just below 1; the formula measures those, not the decay of C(r). (3) χ's peak moves to lower g with N, as the crossover does, while its height stays put.

**What this says (ours, unverified).** At these sizes nothing in the fluctuations grows with N at the crossover: correlations stay one to two steps long and the susceptibility peak keeps its height. That is neither the continuous signature (χ and ξ growing) nor the first-order one (χ's peak growing like N). It looks like a smooth crossover at these sizes, and it cannot rule out either kind of transition at larger N. **It does not reproduce the divergent tendency of [KTB19] Fig. 9a**, with that paper's definition as we read it (ASSUMPTIONS Q19); whether that paper computed ξ differently is a question for its authors.

## T17. Does each seed leave its own leftover? (TASKS T14; written 2026-09-23, night, before the runs)

### Why

T10 found one leftover per converted tube, however large the tube, and every one of those tubes opened from a single seed. The owner's hypothesis about dark matter (VISION Update 16; her decisions of 23 September in `docs/parked/extension_2026-09-22.md`) needs the leftover to be made **per seed**: many seeds, each leaving a scrap, so that the amount of leftover tracks how the change started rather than being one defect per space. This test plants k seeds in one tube and counts.

### What will be run

λ = 1.25; one tube 96 × 4 (N = 384, longer than any T10 tube, so eight seeds sit twelve columns apart); a cold sealed box as T10 (C = 2N demons) but **every demon empty**: instead of a 12-unit spark, **k seeds are planted before the run**, each being move A (ΔS = −2, ΔX = −4, cost 12; the step the spark pays for) at columns j · 96/k, chosen deterministically (`scripts/run_seeded_tube.py`, `plant_seeds`, tested in `tests/test_seeded_tube.py`: k seeds cost exactly 12k and touch only their own columns). k ∈ {1, 2, 4, 8}; twenty replicas each; 30,000 sweeps; configs `configs/t17_seeds_k{1,2,4,8}.json`, seeds inside.

**Disclosed:** a smoke run of the protocol at N = 96 (six decays, 6,000 sweeps, scratchpad, not a result) was made to check that a planted seed converts a tube with empty demons. It does; the leftover counts were 1, 1, 1 (k = 1) and 1, 2, 1 (k = 2).

### Observables

At the end of each run, as T10: the local-dimension histogram; the connected pieces of vertices at d = 1 and their sizes (**the leftover count** is the number of pieces, T10's observable); the count of pieces of exactly four (T10's alternative reading, reported beside); the conversion fraction; the energy retained, H at the end; energy drift.

### Gates

1. Energy conserved to the last unit in every run (drift 0).
2. At every k, at least 18 of 20 runs convert (final conversion fraction at least 0.9).

### Definitions, fixed now

The **slope** is the least-squares slope of the leftover count against k over all runs that pass gate 2, with its standard error; the mean count per k is reported.

### Predictions

The owner's stated hypothesis (Update 16) is option (a); **her pick among the options has not been given**, and she asked on 23 September that the night's work design tests and predictions in her absence.

- (a) **ONE PER SEED**: slope between 0.75 and 1.25.
- (b) **ONE PER TUBE**: slope within ±0.25 of zero, mean near 1 at every k.
- (c) **BETWEEN**: slope from 0.25 to 0.75.

**Ours, unverified:** (c) leaning (b). T11 found the single leftover's position uniform, neither at the seed nor where the two fronts meet, which argues against leftovers being made at seams; if the leftover is instead a defect the conversion must leave for a global reason (a 4 × L torus turning into a flat torus of a different shape), the count stays near one, and extra seeds add only leftovers that anneal before the end.

### Verdicts

ONE PER SEED, ONE PER TUBE or BETWEEN as defined above, if both gates pass at every k; otherwise INCONCLUSIVE.

### Named or interchangeable points

Named, for the reason in T8. The expected effect of interchangeable points on the count is small: final states with one, two or more leftovers at generic positions have one to a few symmetries each, so the weights differ by small factors; only leftovers placed symmetrically (evenly spaced, as planted seeds could make them) gain more, and that bias would favour counts equal to k. Recorded so it can be checked on the saved states if the result sits near a boundary.

### What this cannot show

Anything about the amount of dark matter in the universe. How seeds arise without being planted. Anything at another λ or size.

## T18. How much room does the new space need, as λ changes? (written 2026-09-23, night, before the runs)

### Why

T9 found that, sealed, the change completes only if its surroundings can take the lump (BONFIRE WITH A THRESHOLD), and that the room needed scales with N, as a release of 4(λ − 1)N into C stores against a melting coupling predicts. That was at λ = 1.25 only. Paper 3 of the series (`docs/papers/series_plan.md`) needs it across λ: the lump grows with λ − 1, so the room the new space needs to survive its own birth should grow too. This measures it at λ = 1.10, 1.25 and 1.40.

### What will be run

One tube 24 × 4 (N = 96); one seed planted as in T17 (move A at column 0; cost 32 − 16λ), every demon empty; sealed; C ∈ {N/32, N/16, N/8, 3N/16, N/4, 3N/8, N/2, 3N/4, N, 2N} = {3, 6, 12, 18, 24, 36, 48, 72, 96, 192}; twenty replicas per (λ, C); 30,000 sweeps; λ ∈ {1.10, 1.25, 1.40}. `scripts/run_seeded_tube.py` with a list of capacities (its seed derivation then includes C; T17's single-capacity runs are unchanged, checked by rerunning the T17 smoke test bit for bit). Configs `configs/t18_room_lam{110,125,140}.json`.

### Observables and definitions, fixed now

Each run's product is classified by T9's rules exactly (`scripts/analyse_t9.py`, `classify`): sheet, melted, tube, stalled, other. **C\*(λ)** is the smallest C at which a majority of the twenty runs end as a sheet. The ratio **R = C\*(1.40) / C\*(1.10)** is the reading.

### Gates

Energy conserved to the last unit in every run. At each λ, some C has a majority of sheets (otherwise C\* is undefined and that λ is reported as never clean at N = 96).

### Predictions

The owner has not given a pick (she asked for the night's tests to be designed in her absence). **Ours, unverified:** the room needed grows in proportion to the lump, C\* ∝ N · 4(λ − 1) / g_melt, with g_melt the melting coupling of the flat sheet, which should depend weakly on λ because λ acts only on edges with three squares, which a sheet near melting rarely has. Then R ≈ 4(0.40) / 4(0.10) = 4.

- (a) **PROPORTIONAL**: R ≥ 2.5.
- (b) **WEAKER THAN PROPORTIONAL**: 1.5 < R < 2.5.
- (c) **FLAT**: R ≤ 1.5 (the room needed does not depend on the lump).

Ours: (a). The grid steps by factors of 4/3 to 2, so R is read on the grid and reported with the grid's resolution.

### Named or interchangeable points

Named. Interchangeable weighting would favour the flat sheet (4N symmetries against about 1 for a melt), so it would lower C\* at every λ by a similar factor; the ratio R should be affected less than C\* itself. Recorded as expected, not checked.

### What this cannot show

The actual room a new universe has; anything at N other than 96; the melting coupling at λ = 1.10 and 1.40, which is assumed close to 1.25's, not measured.

#### Reading, 24 September 2026: PROPORTIONAL (R = 6.0)

`python scripts/analyse_t18.py` (tests `tests/test_t18.py`). **A correction to the script before the reading, stated plainly:** its energy gate first tested drift == 0 and reported a failure; the drifts are floating-point rounding (largest 1.7e-13 at λ = 1.40; exactly 0 at λ = 1.25, where 4λ is exact in binary) against energy steps of 4.4 and more, so energy is conserved to the last unit as the gate asks; the test now uses 1e-6. C\* = **12, 36, 72** at λ = 1.10, 1.25, 1.40 (C\*/N = 0.125, 0.375, 0.75). **R = 6.0: PROPORTIONAL.** Our prediction held on the rule and undershot the size: we expected R ≈ 4, and the room needed grows faster than the lump (C\* / [4(λ − 1)N] = 0.31, 0.375, 0.47), so the melting coupling of the new sheet probably falls as λ rises, which was assumed away and not measured. At λ = 1.40 even the largest bath (C = 2N) gave a clean sheet in only 16 of 20 runs.

## T21. Does a sealed sheet given energy fold rather than melt when the points are interchangeable? (series paper 4; written 2026-09-24, before the runs)

### Why

The owner's picture of a black hole is a closed region in which concentrated energy re-curls space towards X (her statement of 23 September: in open space energy spreads and space heals; in a closed region it folds). O20 put a budget of energy into a sealed flat sheet and found melting, not folding, at every budget and λ tried, with named points. Her theory has interchangeable points (VISION Update 12), and under that weighting an arrangement gains its symmetry count: a complete fold (a whole 4-cube, 192 symmetries; a whole curled tube, 2N) gains a great deal, a melt gains nothing. That is the one route by which folding could win, and O20 could not see it. The fast count (Q20) now makes the interchangeable version runnable at N = 36 and 64.

### What will be run

λ = 1.25; flat tori 6 × 6 (N = 36) and 8 × 8 (N = 64); named and interchangeable points (`scripts/run_refold.py`; interchangeable runs use `graphity.interchangeable`, validated against exact averages at N = 18); two sealed protocols:
- **single**: O20's own, one demon holding the budget. Budgets 0.5, 1, 2, 4 per point, as O20. *Stated plainly: one demon holding the whole budget samples the graph almost uniformly below the total energy, which favours disorder; it is kept so the comparison with O20 is like for like.*
- **bath**: C = 2N demons, the budget starting in one (T9's bath, a proper temperature near budget/2). Budgets 2, 4, 8, 16 per point.

Six replicas per (size, points, protocol, budget); 4,000 sweeps; configs `configs/t21_refold_n{36,64}_{named,interchangeable}.json`, seeds inside. A four-run smoke test at N = 36 (200 sweeps) checked both code paths and energy conservation and is disclosed: at budget 1 the single demon left 8 melted vertices both ways, the bath left the sheet flat both ways.

**Structural fact, exact, fixed before the runs:** at N = 36 no complete fold exists (36 is not a multiple of 16, and a 4 × 9 torus is not bipartite), so N = 36 tests partial folds only; at N = 64 both complete folds exist (four 4-cubes; the 16 × 4 tube).

### Observables

As O20: at the end, vertices at local dimension below 2 (folded), at 2 (flat), above 2 (melted); **the folded share of the damage**, folded / (folded + melted), where there is damage; the symmetry count of the final graph; energy drift.

### Gates

Energy conserved to the last unit in every run.

### Definitions and verdicts, fixed now

At a (size, protocol, budget) the **folded share** is the mean over replicas with damage. For each size and protocol:
- **FOLDS WITH INTERCHANGEABLE POINTS**: at some budget, the interchangeable folded share is at least 0.5 while the named one is below 0.5.
- **MELTS EITHER WAY**: at every budget with damage, both folded shares are below 0.5.
- **FOLDS EITHER WAY**: at some budget both are at least 0.5 (O20 would then not reproduce at these sizes).
- **INCONCLUSIVE**: anything else.
The overall reading is the verdict at N = 64 under the bath protocol, which is the one with complete folds on offer and a proper temperature; the others are reported beside it.

### Predictions

The owner's statement (a closed region folds) corresponds to FOLDS WITH INTERCHANGEABLE POINTS; her pick is not yet given. **Ours, unverified: MELTS EITHER WAY**, at both sizes. The symmetry gain is large only for complete folds; a partly folded sheet has one to a few symmetries, like a melt; and the number of distinct melted arrangements grows so fast with the energy that a factor of 192⁴ · 4! (four identical 4-cubes) is unlikely to beat it at N = 64 above the melting temperature, while below it nothing breaks at all.

### What this cannot show

Anything about real black holes; anything above N = 64; a local, concentrated spark (the budget is spread through the whole box, as in O20); anything at other λ.

#### Reading, 24 September 2026: MELTS EITHER WAY (the overall reading, N = 64, bath)

`python scripts/analyse_t21.py` (tests `tests/test_t21.py`). Energy exact in every run. **N = 64, bath: MELTS EITHER WAY**; folded share at most 0.27 (interchangeable) against 0.18 (named) at budget 2, falling to 0.02 both ways at 16. N = 64, single: MELTS EITHER WAY. N = 36, single: MELTS EITHER WAY. **N = 36, bath: FOLDS WITH INTERCHANGEABLE POINTS by the letter, and fragile**: at budget 2 the interchangeable share is 0.61 from only three damaged replicas against a named 0.43, and at budget 4 the order reverses (0.25 against 0.40). The owner's prediction (a closed region folds) fails at the size where complete folds exist; ours (MELTS EITHER WAY) holds there and fails at N = 36 under the bath. What this does not test, recorded again: a local push with cold space around it; the budget is spread through the whole box, as in O20.

## T15 rung 1. Does the time spent in each arrangement equal the count's prediction? (written 2026-09-24, before the run)

### Why

`docs/design/quantum_loop_design.md` puts rung 1 first because nothing above it can be trusted without it: in the owner's quantum picture (VISION Update 17) the probability of a version is its share of the count, so a chain with interchangeable points must spend its time in each arrangement in exactly those proportions. It is validation, not physics. The tools it needs were built the same night (ASSUMPTIONS Q20; `graphity.symmetry.canonical_key`, tested to be blind to renaming within sides and to separate distinct arrangements).

### What will be run

N = 16 and 18 (every arrangement listed: 5 and 26 classes, symmetry counts identical to `results/ergodicity_small.csv`, checked before this was written); (λ, g) = (1.0, 10.0) and (0.0, 10.0); six replicas per (N, λ, g); 500 sweeps discarded, 20,000 measured; `scripts/run_t15_rung1.py`, configs `configs/t15_rung1_n16.json` and `configs/t15_rung1_n18.json`. Two routes: **A**, the interchangeable chain's fraction of sweeps in each class; **B**, the named chain's fraction reweighted by each class's symmetry count. **Control**: the named chain's raw fractions against the named probabilities. A 700-sweep smoke run of both routes (two replicas) checked the machinery and is disclosed; it is far too short to read.

### Definitions, fixed now

For each (N, λ, g) and route: the replica-mean fraction per class, its standard error over replicas, and the total-variation distance TV = ½ Σ |mean − p| against the exact interchangeable probabilities.

### Verdicts

- **AGREES**: for both routes at every (N, λ, g), TV < 0.03, and every class with p ≥ 0.02 lies within 4 standard errors + 0.005 of p.
- **DISAGREES**: any route at any setting fails while its control passes.
- **INCONCLUSIVE**: the control fails at some setting (then the machinery, not the physics, is at fault), or anything else.

### Predictions

Validation, so the prediction is agreement (ours, and the design's). The owner's pick has not been given; this rung does not test her picture, only the tool every later rung needs.

### What this cannot show

Anything quantum. It checks that "probability = share of the versions" is what a chain with interchangeable points actually does, at the two sizes where the versions can be listed.

#### Reading, 24 September 2026: BETWEEN

`python scripts/analyse_t17.py` (tests in `tests/test_t17.py`). Gate 1: energy exact in all 80 runs. Gate 2: every run at every k converted. Leftovers per tube (pieces at d = 1), mean over twenty: **1.10, 2.15, 2.50, 3.40** at k = 1, 2, 4, 8 (pieces of exactly four: 1.05, 1.80, 2.25, 2.35). **Slope 0.288 ± 0.039 leftovers per extra seed: BETWEEN.** The owner's option (a), ONE PER SEED, holds at k = 2 and fails beyond it; ours, leaning ONE PER TUBE, also fails: the count grows with the number of seeds. Stated plainly: the slope is about one standard error above the 0.25 boundary with ONE PER TUBE, and a straight line is a poor description of means that rise by 1.05, then 0.35, then 0.90; the growth looks less than proportional, and whether extra leftovers anneal or merge when fronts meet was not measured. "Mean near 1" in ONE PER TUBE's definition had no number; the verdict is read on the slope, as the verdict table states, and the means are given so the other reading can be checked (they are not near 1 beyond k = 1, so it gives the same answer).

#### Reading, 24 September 2026: AGREES

`python scripts/analyse_t15_rung1.py` (tests `tests/test_t19_rung1.py`). At N = 16 and 18, λ = 0 and 1, g = 10, both routes agree with the exact interchangeable probabilities: total-variation distances 0.0040, 0.0052, 0.0067, 0.0097 (route A) and 0.0007, 0.0062, 0.0046, 0.0125 (route B), every class within its bound; the controls agree too (0.0013 to 0.0075). **AGREES.** Validation only: with interchangeable points, the time the chain spends in each arrangement is that arrangement's share of the count. Every later rung can now rely on it.

## T19. Does a leftover move, stay, or anneal away? (series papers 2 and 5; written 2026-09-24, before the runs)

### Why

Paper 5 asks whether leftovers pull on each other. If a leftover never moves, a pull cannot be seen by watching two of them and must be measured by holding them at chosen separations. Paper 2 needs to know whether the scrap lasts: in the owner's picture it is dark matter, which must be long-lived.

### What will be run

`scripts/run_leftover_mobility.py`, config `configs/t19_mobility.json`. Each replica makes a sheet with leftovers exactly as T17 at k = 1 (24 × 4 tube, λ = 1.25, one planted seed, cold sealed box of 2N empty demons, 30,000 sweeps); a replica not ending with exactly one leftover piece is recorded and not followed. The sheet is then run at fixed coupling g ∈ {1.0, 1.25, 1.5} for 100,000 sweeps; every 500 sweeps the vertices at d = 1 are read and the **displacement** recorded: the shortest graph distance, in the current graph, from the leftover's current vertices to those it started on. Ten replicas per g.

**Disclosed:** a smoke run (two replicas, g = 1.5, 2,000 sweeps followed) checked the code: one leftover stayed in place, one annealed away between 1,500 and 2,000 sweeps.

### Definitions, fixed now

Per followed replica: **moved** if its displacement reaches 2 or more at any block while a leftover exists; **annealed** if, never having moved, it has no vertex at d = 1 at the end; **stayed** if, never having moved, it still exists at the end. Per g, the verdict is the outcome of more than half the followed replicas (MOVES, ANNEALS, STAYS), otherwise MIXED. At least six followed replicas per g are required; otherwise NOT READ.

### Predictions

The owner's pick has not been given. Options: (a) MOVES at some g; (b) ANNEALS at the warmer couplings, STAYS at the colder; (c) STAYS at every g. **Ours, unverified:** (b): STAYS at g = 1.0, ANNEALS at 1.5, MIXED at 1.25. At fixed g = 1.5 the decays of T8 mostly end at the flat torus, which says a leftover can anneal there; in T10's cold box (bath near 0.5) it survived 30,000 sweeps.

### Named or interchangeable points

Named. Interchangeable weighting favours the flat sheet (4N symmetries) over a sheet with one leftover (a few), so it should hasten annealing; recorded as expected, not checked.

### What this cannot show

How long a leftover would last at a universe's temperatures; anything about two leftovers.

#### Reading, 24 September 2026: ANNEALS at every coupling

`python scripts/analyse_t19.py` (tests `tests/test_t19_rung1.py`). Followed replicas 9, 10, 10 (one at g = 1.0 did not end with exactly one leftover). **g = 1.0: 9 of 9 annealed**, first sweep without a leftover between 4,000 and 80,500; **g = 1.25: 10 of 10 annealed** within 500 to 13,000; **g = 1.5: 8 annealed, 2 moved** first, all gone within 11,000. Verdict ANNEALS at every g. Our prediction (b) held at the warmer couplings and failed at g = 1.0, where we expected STAYS. **Inconvenient for the owner's picture, and said as plainly:** the leftover is not permanent at fixed temperature in this model; it lasted the full 30,000 sweeps only in T10's cold boxes, whose bath ends near 0.5. Whether it moves before it goes is answered only at g = 1.5, twice.

## T22. Near λ = 1, do exits from the curled torus fall back? (written 2026-09-24, before the runs)

### Why

In T8 the measured waits near λ = 1 run 15 to 43 % longer than Eq. (2) of the curled-torus paper (the owner noticed the pattern in Fig. 3(a) and asked whether the curve should change; it should not, being fitted to nothing). Eq. (2) predicts the time to the **first exit** from the perfect torus. Two readings of the gap, and this test separates them: **(i) fall-backs**: exits happen at Eq. (2)'s rate, but when the release is small some fall back into the torus instead of growing into a front, so the wait counts several exits; **(ii) a late first exit**: the exit rate itself is below Eq. (2) (a move counted as available is refused more often than assumed). At the other end of Fig. 3(a) the gap is the 200-sweep watch (paper, Sec. V); this test has no watch.

### What will be run

`graphity.exits.run_until_through` (tested in `tests/test_exits.py`: one more exit than fall-backs in every decay that goes through; reproducible from its seed; samples the kernel's ensemble at N = 18 against the exact average). It uses the kernel's move and counts **every** accepted move, so an exit that heals within a sweep is seen. The perfect 4 × L torus at g = 1.5; λ = 1.05, 1.10, 1.25; N = 64, 96; **forty decays** per (λ, N); a decay ends when a quarter of the torus has converted (it has gone through), or at 100,000 sweeps. `scripts/run_exits.py`, configs `configs/t22_exits_n{64,96}_lam{105,110,125}.json`. Recorded per decay: exits, fall-backs, sweeps to the first exit, sweeps to going through.

### Definitions, fixed now

At each (λ, N): the mean number of exits per decay, E, with its standard error over decays; the mean time to the first exit, T1, in sweeps (attempts / 2N), with its standard error; τ from Eq. (2). **F** (fall-backs present): E − 1 > 2 standard errors. **L** (first exit late): T1 − τ > 2 standard errors. The share of exits that go through is reported as 1/E.

### Verdicts, read at λ = 1.05 (λ = 1.10 and 1.25 reported beside, 1.25 as the control where T8 found no gap)

- **FALL-BACKS**: F and not L at both sizes.
- **LATE FIRST EXIT**: L and not F at both sizes.
- **BOTH**: F and L at both sizes.
- **NEITHER**: neither at both sizes (the gap is not reproduced by this measurement).
- **MIXED**: the sizes disagree.

### Predictions

The owner's pick has not been given (she asked for the test after seeing the figure). **Ours, unverified: FALL-BACKS**, with about 70 to 87 % of exits going through at λ = 1.05 (E ≈ 1.15 to 1.43), inferred from the size of T8's gap; at λ = 1.25, E close to 1.

### Named or interchangeable points

Named. With interchangeable points the torus carries 2N symmetries and a state one move away about 2, so exits would be about N times rarer and **returns to the torus about N times more favoured**: fall-backs would become more common, not less. Recorded as expected, not checked.

### What this cannot show

Why a fall-back happens (the arrangement at the moment of return is not recorded); anything at other couplings or sizes.

#### Reading, 24 September 2026: FALL-BACKS by the letter, and the explanation it was written to test does not hold

`python3 scripts/analyse_t22.py` (tests `tests/test_exits.py`). Forty decays per cell; all went through except one at
λ = 1.05, N = 96, which was still a torus at 100,000 sweeps.

| λ | N | exits per decay E | share going through 1/E | F | first exit T1 (sweeps) | τ, Eq. (2) | L |
|---|---|---|---|---|---|---|---|
| 1.05 | 64 | 1.50 ± 0.12 | 0.67 | yes | 10174 ± 2466 | 8330 | no |
| 1.05 | 96 | 1.79 ± 0.21 | 0.56 | yes | 7485 ± 1506 | 8330 | no |
| 1.10 | 64 | 1.80 ± 0.15 | 0.56 | yes | 5134 ± 791 | 4844 | no |
| 1.10 | 96 | 1.65 ± 0.14 | 0.61 | yes | 4326 ± 560 | 4844 | no |
| 1.25 | 64 | 1.48 ± 0.11 | 0.68 | yes | 824 ± 110 | 845 | no |
| 1.25 | 96 | 1.52 ± 0.11 | 0.66 | yes | 905 ± 111 | 845 | no |

**Verdict at λ = 1.05: FALL-BACKS** (F and not L at both sizes). Our predicted verdict held; **our numbers did not**.
We predicted that 70 to 87 % of exits would go through at λ = 1.05; the measured share is 56 to 67 %. We also predicted
E close to 1 at the control, λ = 1.25; it is about 1.5 there too.

**What this means, said plainly.**
- **The first exit is on time.** Measured move by move, with no watch, T1 agrees with Eq. (2) in all six cells, each
  within one standard error. This is the most direct check of Eq. (2)'s counted attempt frequencies so far.
- **Recrossings are a general feature, not a near-λ = 1 effect.** About one exit in three returns to the torus at
  every λ tested. So they cannot explain an excess that appears only near λ = 1, which was the point of the test.
- **T8's excess is not reproduced.** T8's waits at the same cells: 9941 ± 1685 and 11915 ± 2767 at λ = 1.05, and
  5767 ± 674 and 6847 ± 1397 at 1.10 (N = 64, 96). These agree with T1 here within 1 standard error at N = 64, and
  are 1.4 and 1.7 standard errors above it at N = 96. The premise of reading (i) was partly mistaken: T8's wait is
  in effect the first exit visible at a check, because at λ ≤ 1.10 the resting fluctuation that sets its threshold
  is almost always zero. It counts several exits only when an exit heals between two checks. **Ours:** the simplest
  reading of T8's excess near λ = 1 is statistical, 1 to 1.4 standard errors per cell. T8's larger sizes, 144 and
  192, were not re-tested here.
- **The time to go through**, to a quarter converted, is 1.5 to 1.7 times the first exit at every λ. It includes
  the recrossings and the early growth. T8's times to the same quarter agree with it within 1.2 standard errors,
  except at λ = 1.10, N = 96 (2.2).

In the paper's terms (glossary), the transmission coefficient is κ = 1/E = 0.56 to 0.68, the same at λ = 1.25 as near 1.

## T23. The λ map again, four times the decays, with the memoryless check sized to the sample (written 2026-09-24, before any run)

### Why

T8 came out INCONCLUSIVE for two stated reasons. **(1) The memoryless check was mis-sized.** It asked that the
coefficient of variation (CV) of the waiting time lie between 0.7 and 1.3. Simulated now: thirty truly memoryless
waits fall outside that band 5.5 % of the time, so a false fail somewhere in 28 cells was likely. It was also
applied to the whole wait, including the 200-sweep resting stretch, which pulls the CV below 1 wherever waits are
short. **(2)** At λ = 1.35 the energy gate failed for two to five decays per size. The owner wants piece 2 of the
programme settled. Re-reading T8's data under repaired rules would be an after-the-fact amendment, so this is a
new run with fresh seeds, and the rules are fixed first.

### What will be run

T8's protocol exactly (`scripts/run_tube_decay.py`: g = 1.5, block 5, stop at 98 %, `n_sweeps` 100,000, settle
600 with `settle_max` 100,000, `save_adjacency`, `record_f_200`) at λ = 1.05, 1.10, 1.15, 1.20, 1.25, 1.30 and
1.35, and N = 64, 96, 144 and 192 (tubes 16, 24, 36 and 48 × 4), with **120 decays per (λ, N)**. Fresh seeds, one
per λ (20262405 to 20262435), each decay's stream drawn from SeedSequence(seed, lx, ly, replica) as before. One
config per (λ, N), 28 in all (`configs/t23_lam<tag>_n<N>.json`, written by `scripts/make_t23_configs.py`).
λ = 1.25 is run this time, where T8 took it from T7. λ = 1.40 and 1.45 are not rerun: T8 found them not stuck,
and nothing here asks about them. The runs go on the rented machines (`terraform/`, one Batch job per config) or
the laptop; the image pins the laptop's versions. `docker/run.sh` now uploads the saved final graphs as well,
because gate 3 reads resting states from them.

### Definitions, fixed now

- Metastable, reached (at least 75 % converted), (b) two orders side by side (at least 80 % of vertices at
  d ∈ {1, 2} at half conversion), (c) one front (the largest converted piece holds at least 70 %), gate 2 (at
  least 30 decays reaching 75 %) and gate 3 (the release matches the sheet, the ledge at 24λ − 16, or a state read
  from its saved wiring): **all exactly as T8**, by calling `analyse_t8.cell`.
- **(a′) Memoryless, replacing (a).** From the decays that reach 75 % in a metastable cell, take r = waiting − 200,
  the time after the resting stretch. If the process is memoryless, r is exponential with the same mean. (a′)
  holds when the sample CV of r (ddof 1) lies inside the central 99.9 % band of the CV of n independent
  exponential draws, where n is the number of decays read. The analysis computes the band from 200,000 simulated
  samples with seed 20262399. For reference: n = 120, 0.756 to 1.379; 90, 0.728 to 1.455; 60, 0.678 to 1.531;
  40, 0.619 to 1.671; 30, 0.568 to 1.774. A memoryless cell fails it one time in a thousand, so a false fail
  somewhere in the 24 window cells has a chance of about 2.4 %.
- **Sharp at (λ, N):** (a′), (b) and (c). **Status per λ:** T8's `lam_status` (sharp, not sharp, unread, not
  metastable).

### The hypothesis has two parts, and each has its own verdict

- **The window, λ = 1.05 to 1.30.** SHARP ACROSS THE WINDOW if every λ has status "sharp"; NOT SHARP AT (the
  list) if every λ is "sharp" or "not sharp" and at least one is "not sharp"; otherwise INCONCLUSIVE, with the
  reason.
- **The edge, λ = 1.35, reported separately and not part of the window verdict.** Pooled over sizes and compared
  with λ = 1.30: **(E1)** the share of decays ending at the flat torus is lower at 1.35, by more than two standard
  errors of the difference; **(E2)** the share of decays whose converted region is in more than one piece at 25 %
  conversion (`pieces_25` > 1, several seeds at once) is higher at 1.35, by more than two standard errors.
  BREAK-UP BEGINS AT THE EDGE if both hold; NO BREAK-UP if neither; PARTIAL if one.

`scripts/analyse_t23.py`, tested in `tests/test_t23.py` before any run.

### Predictions

**The owner's (24 September): SHARP ACROSS THE WINDOW, and BREAK-UP BEGINS AT THE EDGE.** Said plainly: this was
chosen after seeing T8, and that is what a repeat is for. T8's shares ending flat, 79 % at 1.30 and 46 % at 1.35,
informed the edge half. Her reality sits at about λ = 1.25, in the middle of the window.

**Ours: the same.** In the window we expect (a′) to hold everywhere. T22 found the first exit on time from 1.05 to
1.25, and recrossings do not break memorylessness, because a random number of memoryless tries is still
memoryless. The waiting-time law (mean wait within 25 % of τ) is reported as before and not scored.

### Named or interchangeable points

Named, for T8's reason (the per-move symmetry count is unaffordable at these sizes). The expected effect of
interchangeable points is T8's: waits multiplied by about N, and the release and the front unchanged (the front
still to verify).

### What this cannot show

Anything at other couplings, at sizes beyond 192, with interchangeable points, or outside λ = 1.05 to 1.35. It
is still the 2D model: one curled direction and one open, the partial state the owner's rule for three
dimensions forbids (O40, VISION Update 22).

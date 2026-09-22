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

**Why proposed rather than made.** It changes a gate after the data it judges were seen. What makes it defensible: the three predictions are met at every size on both the first run and the rerun with fresh seeds, and the change concerns only which decays are admitted, not what is measured on them; and the thing it admits — a decay resting on a second sharp step — is more of what claim 4 describes, not less. **If adopted:** the λ = 1.25 verdict is TWO-STATE CHANGE. **If not:** the verdict is withheld and the three predictions are reported as met with the gate outstanding.

**Recorded, and not a change to anything:** at λ = 1.5 the tube is not metastable at g = 1.5 — it is at φ = 0.95 by sweep 50 in every replica, as it was in the design-track pilot at g = 1.0. There is no waiting time to measure and no switch to see. The section above listed λ = 1.5 assuming a long-lived tube there, and it is not one. Those runs are reported as what they are: the unstable case, which the verdict language was not written for and to which no verdict is applied.

---

## T8. The λ map (formerly T7)

To be written before it runs. It may reuse the criteria above, and if it does it will say so explicitly rather than restating them.

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

The draft for the parked menu study is in `docs/parked/PREREGISTRATION_menu_study.md`.

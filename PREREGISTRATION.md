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

*(None since the revision above. Add below with a date, leaving the original standing.)*

---

## T7. The λ map

To be written before T8 runs. It may reuse the criteria above, and if it does it will say so explicitly rather than restating them.

The draft for the parked menu study is in `docs/parked/PREREGISTRATION_menu_study.md`.

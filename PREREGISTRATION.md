# Pre-registration

Rule 4 of `CLAUDE.md`: predictions and analysis choices are committed here **before** the runs that test them. The git commit containing a section is its timestamp. Nothing below may be edited after its runs have started; corrections are added as dated amendments underneath, with the original left standing.

---

## T6. The order of the geometry-forming transition

**Written 2026-09-21. No production run has been made.** The sampler is built and validated (`ASSUMPTIONS.md` Q14, Q15 and section D); what follows fixes what will be measured and what each outcome will be taken to mean.

### Why this measurement and not another

VISION success condition S2 asks whether the transition is first order. Every measurement in this repository so far is an average taken at one coupling, which cannot answer it: a barrier is exactly the place a thermal chain refuses to go. The density of states does answer it, because from it the whole energy distribution follows at every coupling, including the part no chain visits.

The signature is a **free-energy barrier**: at the transition, the distribution of energies has two humps with a valley between them. The depth of that valley is

    ΔF = ln P(higher hump) − ln P(valley floor)

measured at the coupling where the two humps have equal height. **The test is not whether ΔF is non-zero at one size — it is how ΔF grows with size.**

### The prediction, stated before the runs

For a first-order transition in two dimensions the barrier is the cost of the interface between the two phases, which is a line, so

    ΔF  ∝  L  ∝  √N        (first order)
    ΔF  →  bounded or zero  (continuous)

**This is the whole of the test.** A barrier that does not grow is not a barrier in the thermodynamic limit, however large it looks at one size.

### What will be run

| Choice | Value | Why this and not something else |
|---|---|---|
| Sizes | N = 36, 64, 100, 144 (square tori, L = 6, 8, 10, 12) | Square so that the interface length is unambiguous. A rectangular torus has two different cross-sections and the cheapest interface takes the short one, which would confound the scaling. |
| Knob λ | 0, 1, 1.25, 1.5 | 0 and 1 are the two published settings. 1.25 and 1.5 are where the flat sheet is provably the lowest-energy arrangement, which is where S2 and S4 could both hold. The whole map is published whichever way it comes out (S1). |
| Method | Wang–Landau over (S, X), then the frozen-weight refinement | Bins are (S, X) rather than the energy, so one run covers every λ. Stage one is never reported alone (Q14). |
| Independent runs | 4 seeds per (N, λ) | The spread between them is the error bar. Block-based error bars underestimate and will not be quoted. |
| Window | A band in (S, X) around the transition, its edges fixed from the tempering equilibrium curve before the Wang–Landau run starts and recorded in the config | The full range is too many bins to flatten at N = 144. Restricting is legitimate; ln g is correct inside the window. |

### Validation gates, all of which must pass before any number above is interpreted

1. **Ising**: the 4×4 density of states reproduced to better than 0.05 in ln g. *(Passed: 0.006–0.013.)*
2. **Exact enumeration**: N = 16 and 18 reproduced to better than 0.05 in ln g, every bin found and none invented. *(Passed: 0.016 and 0.014.)*
3. **At each production size**: the four seeds must agree on ΔF to better than 20 % of the ΔF being claimed. If they do not, that size is reported as not converged and excluded from the fit, and the exclusion is reported.
4. **Round trips**: each run must cross its window end to end at least 20 times. Reported with every run.

### What each outcome will be taken to mean

Let ΔF be fitted against L as ΔF = aL + b, over at least three sizes that passed gate 3.

- **FIRST ORDER** — `a > 0` by at least 3 standard errors, **and** ΔF ≥ 1 at the largest size. Both, not either.
- **CONTINUOUS** — `a` is within 2 standard errors of zero, **or** ΔF < 1 at every size. A barrier below 1 in log-probability is crossed freely and is not a barrier.
- **INCONCLUSIVE** — anything else. Explicitly including: `a > 0` at between 2 and 3 standard errors; fewer than three sizes passing gate 3; or the two criteria for first order splitting (a growing barrier that is still below 1, or a barrier above 1 that is not growing).

**Inconclusive is a real outcome and will be reported as one.** It will not be resolved by adding sizes after the fact, by changing the fit, or by dropping a size that does not fit the line. Any such change is a new pre-registration.

### What would count against the hypothesis

**This is the part that matters, and it is written before the answer is known.**

- If the result is CONTINUOUS at **every** λ where the settled state is a sheet (λ > 1), then **VISION claim 4 does not live in this model family**, and the write-up will say so in those words. That is the primary way this can fail, and it is the expected outcome on the published evidence.
- Finding FIRST ORDER only at λ < 1 rescues nothing. That is already known, and there the cold state is knots rather than a space, so S2 is satisfied while S4 is not. It will be reported and not counted.
- If the barrier grows but the ordered side is not connected (T3's `largest_frac` well below 1 through the transition), S2 is met and S4 is not, and the write-up will say that the two still have not been met together.

### What this measurement cannot show

Anything about the real universe; anything about X, which is not what this model contains; and anything about claims 2 or 6, which this model has no purchase on. A result here bears on claim 4 in the narrow sense of *whether geometry forms out of a random phase sharply or gradually*, which is narrower than claim 4 as VISION states it.

### Amendments

*(None. Add below with a date, leaving the original standing.)*

---

## T7. The λ map

To be written before T8 runs. It may reuse the criteria above, and if it does it will say so explicitly rather than restating them.

The draft for the parked menu study is in `docs/parked/PREREGISTRATION_menu_study.md`.

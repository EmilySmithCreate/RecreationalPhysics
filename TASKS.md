# Tasks, in order

Each task has an acceptance test. Do them in order; do not start a task whose predecessor's gate has not passed. When a task is done, tick it here in the same commit.

Notation: N vertices, S total squares, S_e squares on edge e, φ = S/N, g coupling (acts like temperature), λ strength of the local term. D = 2 throughout (4-regular bipartite graphs).

## T1. Rectangular torus  ☑ (2026-09-19)

`torus(side)` only builds L×L. Add `torus(lx, ly)` (both even). Needed because the published curve is at N = 160 (e.g. 16×10).

Accept: tests for 16×10: 4-regular, bipartite, S = N, every S_e = 2, `is_valid` true.

Done: `test_rectangular_torus`. Both sides must also be ≥ 6 (ASSUMPTIONS Q5). The runner takes `[lx, ly]` entries in `"sides"`, which need `"seed_scheme": "independent"` (Q7). `torus(L)` is unchanged, so `cqg_first_look` still reproduces bit for bit.

## T2. Full Hamiltonian with the λ knob  ☑ (2026-09-19)

Replace the hard cap by the soft local term (ASSUMPTIONS Q1, Q3; [T25] Eq. 22):

    H = 16 (N − S) + 4 λ Σ_e (S_e − 2)₊

- Make the cap optional (`cap=None` means no cap). Keep the hard-core rule (no two vertices with more than two common neighbours). With the cap off, allow small tori again (the 4×4 torus is the 4-cube Q4).
- The move changes S_e on every edge of every lost or gained square. Simplest correct approach: collect the affected edge set (edges of all squares through the two removed edges before the move, and through the two added edges after it), evaluate the local term on that set before and after.
- Offer both acceptance rules: Metropolis, and Glauber p = 1/(1 + exp(ΔH/g)) as in [T25] Eq. 28. Both satisfy detailed balance.

Accept:
- Q4 (4×4 torus, N = 16, S = 24, every S_e = 3): H = 0 at λ = 1 and H = −128 at λ = 0.
- Flat torus: H = 0 for every λ. Melted large graph: H ≈ 16N.
- Incremental ΔH equals full recomputation after 10⁴ random moves at λ ∈ {0, 0.5, 1}.
- λ = 1 with `cap=2` reproduces the existing capped results bit for bit (regression). "Bit for bit" means the eight columns of `results/cqg_first_look.csv`; newer runs carry three extra columns (`phi_err`, `chi_err`, `tau_int`). This holds across machines: checked Linux against Windows on 2026-09-19.

Done. `run_chain(..., lam, cap, glauber)` now returns (S, X, acceptance), where X = Σ_e (S_e − 2)₊ is the number of surplus squares on over-full edges, so H = 16(N − S) + 4λX. Decisions taken, all in the docstring of `cqg.py`:
- The cap was kept as an option, not removed: it is a published model ([KTB19] Sec. 4; ASSUMPTIONS Q3). `cap=2` or `NO_CAP`; in a config, `"cap": null`. "No cap" and "cap = 3" are the same thing, because the hard-core rule alone limits an edge to three squares.
- ΔX is found as the task suggested: list the edges of every lost and gained square, sum X over the list in the new graph, switch the move back, sum over the same list in the old graph, switch forward.
- Acceptance tests: `test_four_cube_energies`, `test_flat_torus_has_zero_energy_for_every_lambda`, `test_melted_graph_has_energy_near_16n`, `test_incremental_energy_is_exact` (λ = 0, 0.5, 1), and the regression as a permanent unit test, `test_capped_kernel_is_bit_for_bit_what_it_was`, pinned to numbers recorded before the change. The full-size regression on `cqg_first_look` was also re-run by hand. Rule 6 checks for a new kernel (networkx brute force, constraint preservation, same-seed) are in `tests/test_cqg.py`; Metropolis and Glauber are tested to agree.

## T3. Connectivity observables  ☑ (2026-09-20)

Number of connected components, size of the largest, and a census of isolated Q4 components. Needed to detect the published "shattering into hypercubes" at λ = 0 and to check success condition S4 (a connected space).

Accept: unit tests on hand-built graphs (one torus; two disjoint tori; a torus plus a Q4).

Done: `src/graphity/connectivity.py`, tests in `tests/test_connectivity.py` (the three hand-built cases, plus a comparison with networkx on graphs the chain shattered by itself). `run_chain` takes an optional `conn` array and the runner writes four new columns: `pieces`, `largest_frac`, `baby_frac`, `cube_frac` (ASSUMPTIONS Q8). Looking does not change the chain; `cqg_first_look` re-run at full size is identical on its original columns.
- The census follows the published definition, not only "Q4": [KTB19] Sec. 3.3.1 defines the λ = 0 ground-state pieces as "baby universes", connected pieces with three squares on every edge, and its Fig. 5 draws them as 4-cubes. 4-cubes are counted separately among them.
- **Finding on the way (ours): the 4-cube is not the only one.** A 14-vertex graph (points and blocks of the 7-point biplane) qualifies too and ties with the 4-cube in energy at every λ. It matters for Gate A's wording below, and for T7.
- To make the two smallest readers (`has_edge`, `squares_on_edge`) usable from both modules they moved, unchanged, to `src/graphity/squares.py`; `cqg.py` still exports them.

## GATE A. Reproduce the published λ = 0 behaviour  ☑ (2026-09-20, owner's decision)

Published: with the global term only, the transition is first order and the graph decomposes into isolated hypercubic complexes ([T25] "Cycle condensation"; [KTB19]; [GV21]).

Accept: at λ = 0, several sizes, cooling and heating: hysteresis around the transition, and a cold phase dominated by baby universes, reporting how many of them are 4-cubes. If this does not appear, stop: either our model reading or our sampling is wrong. *(Reworded by the owner on 2026-09-20 from "dominated by Q4 components": the baby universe is the published definition of these pieces, and the 4-cube is not the only one; ASSUMPTIONS Q8. The run that passed meets the old wording as well.)*

**Passed, 2026-09-20.** The owner decided, on the evidence in the last bullet below, that `cqg_lam0_first_look` together with the two quench runs passes this gate. Her reasons as agreed in conversation: the gate is a reproduction check, not a test of the hypothesis, and both criteria are met at three sizes. What passing means, and what it does not: our reading of the model and our sampler reproduce what is published for the global term alone. It does not mean the transition has been shown to be first order (that is VISION S2, task T6), and the runs stay labelled exploratory in their configs.

Note, 2026-09-20 (the criterion above is unchanged; this records what T3 turned up, for the owner to decide).
- **"Dominated by Q4 components" may be too narrow.** The published definition of the λ = 0 ground-state pieces is the baby universe ([KTB19] Sec. 3.3.1), and the 4-cube is not the only one (ASSUMPTIONS Q8). Proposed reading, NOT adopted: "a cold phase dominated by baby universes (`baby_frac`), reporting how many of them are 4-cubes (`cube_frac`)". If only 4-cubes ever appear the two readings agree.
- **A second published curve exists for this gate:** [KTB19] Fig. 6, a quench at λ = 0 for N = 100 to 200, where φ passes 1 within a few hundred sweeps and reaches 1.2 to 1.35 by sweep 1000. It can be digitised as Fig. 8a was. Its "sweep" is not defined in the paper, so only the shape and the heights are comparable, not the clock.
- Sizes should be chosen knowing that perfect shattering into 4-cubes needs N divisible by 16, and into the 14-vertex piece N = 14a + 16b.
- **Outcome of a first look, same day (exploratory; ASSUMPTIONS section D).** At N = 64, 96 and 160, four replicas: on cooling φ jumps from about 0.65 to about 1.46 between two neighbouring couplings; on heating the shattered state survives to a coupling about 2 higher; inside that loop each replica sits in one of two states about 0.85 apart in φ and nothing sits between; on the hot side of it the two legs agree to 0.005. The cold phase is about N/16 pieces, 84 to 95 % of vertices in baby universes, 75 to 87 % in 4-cubes. The two quench figures of [KTB19] (Fig. 6 at λ = 0, Fig. 7 at λ = 1) are reproduced in kind as well. **Decisions for the owner:** (1) does this pass Gate A, given that the run was exploratory and the gate is a reproduction check, not a test of the hypothesis; (2) adopt the "baby universes" reading above or keep "Q4 components", which this run also meets. Gate B's two open decisions are unchanged. **Both decided by the owner on 2026-09-20: yes, and adopt; see the top of this section.**

## GATE B. Reproduce [T25] Fig. 3 at λ = 1  ☐

Published: N = 160, φ against log g, cooled from random and heated from the torus, no hysteresis, random-phase floor 0.126.

Accept: floor 0.126 ± 0.01; heating and cooling agree within errors through the crossover; cold end above 0.9 when heated from the torus. **Human step for Emily:** open arXiv:2512.17676 Fig. 3 and compare the position of the rise by eye; record the comparison in ASSUMPTIONS section D. If the figure's axis cannot be matched, write to the author rather than guessing.

Note, 2026-09-19 (the criteria above are unchanged; this records what is known about them, for the owner to decide). Both human steps have been done from the sources; details and quotations in ASSUMPTIONS section D and O5.
- **The 0.126 is theory, not data.** [T25] writes it as (3⁴/4)/160. The measured points of Fig. 3 sit at 0.129. Our 0.120 at infinite temperature is the correct finite-size value for the hard-core rule, which [T25] Fig. 1(b) confirms we read correctly.
- **The axis is the plain coupling, log base 10.** The published rescaling is |V|^(1−2/D), which is no rescaling at D = 2. ([KTB19] Fig. 8a uses a *natural* log; do not mix the two.)
- **The figure has been digitised** (`docs/published/T25_fig3_digitised.csv`, 22 points), so "by eye" is no longer needed.
- **Demonstrated: the written criteria do not discriminate.** The capped kernel at N = 160 passes all three (floor 0.128; heating and cooling agree to 0.001 through the crossover; 1.000 at the cold end) and still differs from the published curve by up to 0.44 on the cold side (`results/cqg_n160_capped_vs_t25fig3.csv`). On the hot side it agrees to about 0.01.
- **Proposed replacement, NOT adopted; the owner decides.** Accept when, at λ = 1 without the cap, the largest difference from the 22 digitised points is below 0.05 (the published dots scatter by about 0.02 among themselves), using only couplings where our heating and cooling agree and τ is far below the block length. The capped kernel scores 0.44 on this and fails, as a control should. If λ = 1 fails too, stop and write to the authors: the text of [T25] does not say which model Fig. 3 shows, nor how long its runs were.
- **Outcome, same day (exploratory; ASSUMPTIONS section D): λ = 1 fails too**, 0.41 on this criterion, with the curve smooth and in equilibrium. But the same run reproduces the *other* published N = 160 curve, [KTB19] Fig. 8a, to rms 0.005. So the kernel is not the problem; the two published figures disagree with each other (0.62 against 0.99 at g = 5). **Gate B as a reproduction of [T25] Fig. 3 cannot pass with either published variant, and the reason is not in the papers.** Decisions for the owner: (1) whether [KTB19] Fig. 8a, the gate VISION step 2 originally named, should be the λ = 1 gate instead, in which case the exploratory evidence says it would pass; (2) whether to write to the authors now, with the two digitised curves and our two runs attached, rather than after both gates as planned below. Gate A does not depend on either decision.

## T4. Ergodicity check  ☑ (2026-09-20)

For the smallest sizes that admit valid graphs, enumerate the configuration space exhaustively and confirm the move set connects it (or document which parts it cannot reach). Add the "neighbourhood swap" move of [T25] Fig. 8 if needed.

Done (ASSUMPTIONS Q9; `src/graphity/small_graphs.py`; `scripts/check_ergodicity.py` with `configs/ergodicity_small.json`; `tests/test_small_graphs.py`). Started while Gate B was still open, because it checks the sampler and interprets no new result.
- **Exhaustive result:** no states for N ≤ 12; N = 14 has one class and the chain cannot move in it (harmless); N = 16 has 5 classes and N = 18 has 26, all joined by the switch; under the cap the first states appear at N = 18, 3 classes, all joined. Completeness is proved by counting: the labelled states are counted directly (1 785 021 235 200 at N = 18) and the classes the switch reaches add up to exactly that.
- **What "joined" has to mean** (ours): all classes up to renaming vertices, not all labelled states. That is enough for every observable we use, and the docstring of `small_graphs.py` says why.
- **A bonus the task did not ask for:** with every state known, ⟨S⟩ is exact at N = 16 and 18, and the chain reproduces it for λ = 0, 0.5, 1 under both acceptance rules. This is now the strongest test of the kernel.
- **Not shown:** anything for N ≥ 20 (the count at N = 20 did not finish in about 40 minutes). The neighbourhood swap was not needed at these sizes and has not been added. If a freezing problem at large N turns out to be a connectivity problem, this is where to look again; T5 (parallel tempering) addresses slowness, not reachability.

## T5. Parallel tempering  ☐

Replica exchange across the g grid. Accept: exchange rates 20–40 % between neighbours; cold replicas reach φ > 0.95 from a random start at N = 160; results consistent with plain runs where those equilibrate.

## T6. Entropy curve s(φ) by Wang–Landau  ☐

[WL01]. Flat-histogram sampling over S. Validate first on a system with a known answer (e.g. 2D Ising on a small lattice, exact density of states available), then apply to the graph model.

Accept: Ising check within tolerance; s(φ) curves for N ∈ {36, 64, 100, 160} at λ ∈ {0, 1}; at λ = 0 a convex dent must appear (consistency with Gate A).

## T7. Pre-register the λ map  ☐

Write `PREREGISTRATION.md`: λ ∈ {0, 0.25, 0.5, 0.75, 1}; sizes; observables (dent in s(φ) and its scaling with N; hysteresis width; largest-component fraction; Q4 census); what counts as first order, as continuous, as inconclusive; what would count against the hypothesis. Commit before running.

## T8. Run the λ map, then the sealed runs  ☐

Questions: at which λ does the order change? Is there any λ with a first-order transition **and** a connected space (VISION S2 and S4 together)? Then fixed-total (sealed) runs as in VISION step 3.

## T9. Unexplained drift  ☐

The capped variant showed the half-order coupling moving with ln N (ASSUMPTIONS D). Repeat the measurement at λ = 1 with parallel tempering and several replicas. Either it disappears, or it is characterised properly (fit 1/g against ln N with errors) and compared with the N-independence stated in [T22].

Note, 2026-09-19, from the sources (ASSUMPTIONS, first-look section): the N-independence in [T22] is a consequence of a continuum-limit argument in [KTB19] Sec. 3.1.1, not a measurement, and [KTB19] Fig. 8a itself shows curves for N = 100 to 200 that do not collapse, in the direction of our drift. So the thing to explain is no longer why we see a drift, but whether it is logarithmic. The prediction to test is a slope of 1 for 16/g against ln N; the first look gave 1.12 with one replica and no error bar.

## Design track (VISION plan step 5)

Brief: `docs/design/model_x_brief.md`. Done so far: the dip census at N ≤ 18 (`scripts/dip_census.py`, `configs/dip_census_small.json`), and a finer one at N = 18 (`configs/dip_census_fine.json`): dips above the flat ground state for 1 < λ < 1.6, none above. `scripts/exact_small_averages.py` gives exact averages at N = 16 and 18 for any g and λ; T5 and T6 should be validated against it. Next, cheapest first: (1) rehearse the S3 measurement on the backwards reaction, sheet to cubes at 0 < λ < 1, where the energy released per vertex is known exactly, 8(1 − λ); (2) after T5, look for dips above the flat ground state at N = 64 to 160 for 1 < λ < 2. Exact small-size work may run alongside the tasks above; anything that interprets new physics waits for the gates.

## Later

Scorecard against "the spot" (VISION step 4): spectral dimension, volume-growth dimension, curvature uniformity, shortcut census, stability under perturbation. Allotrope ladder of [T24]: does squares-per-vertex move in jumps with hysteresis?

## Before anything is shown to anyone

VISION S5: a physicist reads it. Draft a short, honest note to C. Kelly, F. Biancalana or C. Trugenberger once Gates A and B have passed: what was reproduced, what was not, the code link, and a request for a sanity check.

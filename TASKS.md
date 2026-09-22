# Tasks, in order

Each task has an acceptance test. Do them in order; do not start a task whose predecessor's gate has not passed. When a task is done, tick it here in the same commit.

Notation: N vertices, S total squares, S_e squares on edge e, φ = S/N, g coupling (acts like temperature), λ strength of the local term. D = 2 throughout (4-regular bipartite graphs).

**Numbering, 2026-09-22.** `PREREGISTRATION.md` numbers its sections by the order they were written and its T7, T8 and T9 are not this page's T7, T8 and T9. The map: PREREGISTRATION **T6** = this page's T6 (order of the disorder-to-order transition, redirected to tempering); PREREGISTRATION **T7** (tube → sheet, the order-to-order change) has no entry here and is the first result on the design track, plan step 5; PREREGISTRATION **T8** (the λ map) = this page's T7 + T8; PREREGISTRATION **T9** (the sealed tube) is the sealed half of this page's T8 and is the order-to-order version of T11. This page's T9 (the drift) is untouched by any of them. PREREGISTRATION **T10** (does the leftover grow with the space) and **T11** (is the leftover ring a seam) have no entries here; both are step-4 items on the design track. Pre-registration numbers are frozen with their results; this page's are not renumbered either, so that the history reads.

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

**Re-opened as a richer target, 2026-09-21** (the gate stays passed; this adds work, it does not withdraw it). [GV21] was read in full by the owner and our record of it was wrong twice over: it is **Monte Carlo on real graphs, not mean field**, and it was filed as abstract-only. It simulates exactly this energy (its Eq. 2.6 has no saturation bracket, so λ = 0) at N = 128 and 256, degrees 3–8, and reports a **first-order transition with clear hysteresis for every degree above 3**. New reproduction targets, all at λ = 0: (1) its Fig. 3A, φ against coupling, cooling against heating, several N at d = 4; (2) the cold-phase census, ≈ N/2^d hypercubes **plus one closed bipartite "ribbon" holding the leftover nodes** — our runs leave 5–16 % of vertices outside baby universes and we have never asked whether that remainder is one connected piece, which `connectivity.py` can answer from data we already have; (3) its Fig. 3B, ribbon fraction against coupling; (4) its Fig. 7, a closed chain of hypercubes under a connectedness constraint at N = 128. **Ribbon: done, 2026-09-21, and it is there** (`configs/cqg_lam0_ribbon.json`; ASSUMPTIONS section D). At sizes deliberately not multiples of 16, the cold phase is k knots plus exactly one other connected piece, and that piece is the largest: at N = 100, `pieces` = 6.00 in every measured sweep with `largest_frac` = 1 - `baby_frac` to four figures; at N = 36, `pieces` = 2.00, one knot of 16 plus one piece of 20. The same equality holds in the partly-converted rows, which is the object T11 is about. Topology (closed, bipartite) not yet confirmed — that needs a snapshot rather than a sweep average. **A modelling difference to handle first:** they do *not* impose bipartiteness — they start from ordinary random regular graphs and bipartiteness *emerges* in the clustered phase (their Sec. 2.3), where our kernel imposes it. A non-bipartite mode would use `full_curvature.py` (Q10), whose ergodicity is unproven. **Before comparing any number**, settle the coupling units (on a d-regular graph Tr A⁴ = 8·squares + const, so μ₄ maps to 8μ₄ per square; ours, unverified) and the sign convention of their Eq. (2.1) against their Fig. 3A.

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

## T5. Parallel tempering  ☑ (2026-09-20)

Replica exchange across the g grid. Accept: exchange rates 20–40 % between neighbours; cold replicas reach φ > 0.95 from a random start at N = 160; results consistent with plain runs where those equilibrate.

Done (`src/graphity/tempering.py`, `scripts/run_cqg_tempering.py`, ASSUMPTIONS Q11 and section D). Validated first against exact averages at N = 18, which is a stronger check than the three criteria. Then the capped model at N = 160 from random starts: swap rates 0.24 to 0.45 on average, cold end φ = 0.958 to 0.974 in all four replicas, and agreement with the plain run to 0.0007 at the three couplings they share.
- **What it bought:** the equilibrium curve can now be trusted down to g of about 3 (four replicas agree to 0.002 to 0.004) where a single chain stopped at 5.
- **What it did not:** below g = 3 graphs made at most one round trip per replica in 18 000 rounds, replicas differ by up to 0.02 and τ is in the thousands. The ordered cold graphs carry frozen-in defects. More rounds, not a finer ladder, is the remedy, or the neighbourhood move of [T25] Fig. 8.
- **Seen on the way:** under the cap at N = 160 the curve is steepest, slowest and most fluctuating at g ≈ 2.85. That is where T6 should look for that model.

## Sequencing note, 2026-09-21 (owner's question: must the connected-sampler papers be read before planning the computation?)

**Yes for some of the work and no for T6, and the split is clean.**

- **T6 does not need a connectivity-preserving move.** It samples the whole state space, disconnected configurations included; that is the point of a flat-histogram walk over the energy. It is pre-registered and can run now.
- **Gate A's re-run and T11 do need one, and we do not have one.** [GV21]'s Fig. 7 (a closed chain of hypercubes under a connectedness constraint) and its Fig. 3B (the ribbon fraction) both come from a connectivity-preserving sampler, and T11 asks whether the half-converted state holds a connected geometric region, which is unanswerable without one.
- **Read before building it, not after:** [VL05], which is the actual algorithm [GV21] cites, and [Lamas25], which describes a connected sampler and a Hamiltonian with a connectivity term. Building our own first and discovering afterwards that two groups already did it better is the expensive order.

## Connected sampling: decided by reading, 2026-09-21

The owner asked that the sources be read before the machinery was designed. They were, and the answer is that **most of the machinery should not be built.**

**What the reading found.**
- **[Lamas25]** (abstract and method section read): its "connected sampler" is the naive one — propose, check, reject if disconnected. It also uses edge *addition and deletion* rather than switches, so it does not preserve degree and its ensemble is not ours; and it runs simulated annealing, which finds low-energy configurations but does not sample an equilibrium distribution, so nothing like a density of states or a free-energy barrier can come out of it. **Not transferable.** Its sizes are N = 128 to 1024 with 16 000 steps and 10 runs, which is a much lighter computation than ours.
- **[VL05]**: solves a different problem (uniform generation from scratch for arbitrary degree sequences); its value is efficiency at large sparse sizes. **Decided: do not implement.**
- **[Taylor81]**: the theorem that settles it. Any connected graph reaches any other of the same degree sequence by switches **with every intermediate graph connected.** So *switch, and reject if the graph would come apart* is irreducible on connected graphs, and detailed balance is automatic because a restricted state space with a symmetric proposal is still detailed-balanced.

**The approach, therefore.** Add a `connected=True` option to the existing kernel that rejects any switch which would disconnect the graph. No new move, no new algorithm. `connectivity.py` already counts pieces and is compiled, and the check need only run on moves that are otherwise accepted, so the cost falls with the acceptance rate.

**Checked 2026-09-21, and the check came out vacuous** (`scripts/check_connected_ergodicity.py`; ASSUMPTIONS Q16). The restricted walk reaches every connected class at N = 16 and 18 with and without the cap — but the restriction refused **zero** moves at both sizes, because every valid state that small is connected anyway (the smallest valid piece is 14 vertices, so two pieces need 28, and enumeration cannot reach 28). So the property is **unproven on our space**, Taylor's guarantee is not inherited through the hard-core constraint, and every connected run must report the share of proposals refused for disconnection so a reader can judge how hard the restriction was working. Original note follows.

**The one thing that must be checked before any of it is interpreted.** Taylor's theorem covers a degree-constrained space. Ours also carries the hard-core constraint, and **[Swap17] states in its title that adding a constraint can destroy exactly this swap-connectivity.** So irreducibility on our space is not inherited and has to be demonstrated: restrict T4's exhaustive enumeration to connected valid states at N = 16 and 18 and check that the switch, refusing disconnecting moves, still joins them all. That machinery exists (`small_graphs.explore`); it needs one filter. **If it fails, the plan changes and we report that it failed.**

## T6. The order of the transition  ☐  — REDIRECTED 2026-09-21, from flat-histogram sampling to parallel tempering

**Why the change.** The flat-histogram instrument was built, validated against two exactly known answers, and then failed on the real problem for a structural reason (ASSUMPTIONS Q17): at N = 36 it made **zero round trips** across its own window, so ln f never fell, the weights ran to a spread of 24 796 against a true spread of order 90, and the second stage froze in a single bin. A restricted window does produce round trips, which locates the fault in the diffusion distance rather than in the kernel — but the measurement needs a window spanning both phases, which is the wide one that cannot be crossed.

**What replaces it, and why that is not a retreat.** [RdF15] asks exactly our question — *is the transition in this model really first order?* — in 4D Euclidean dynamical triangulation, and answers it with **parallel tempering plus energy histograms**. They also state the reason a plain chain cannot do it: at a first-order transition the correlation length stays finite, but the autocorrelation time diverges because moves between the two coexisting phases are exponentially suppressed as the system grows. Tempering is the standard remedy, **this project already has it (T5), and it is already validated against exact averages at N = 18 (Q11).**

**The four pre-registered observables are unchanged and all obtainable this way.** `temper()` already returns the full per-sweep series of S and X at every coupling, and H = 16(N − S) + 4λX, so the energy histogram at each coupling follows directly:
- **latent heat** — separation of the two peaks of that histogram, at the coupling where they carry equal weight;
- **barrier** — ln(peak/valley) of the same histogram;
- **Binder energy cumulant** and **heat capacity** — from the moments of the same series.

Nothing in PREREGISTRATION.md section T6 needs changing except the sentence naming the method; the sizes, knob settings, seeds, gates, criteria and falsification conditions all stand as written. **That is the test of whether a pre-registration was written well: the method changed and the criteria did not have to.**

**What is needed:** a runner that writes the energy histogram per coupling (`temper` returns the series; the current tempering runner writes only summary rows), and a coupling ladder that brackets the transition at each size. Both are small.

**What is kept from the flat-histogram work:** the code, its Ising validation, its exact-enumeration validation at N = 16 and 18, and the two schedule repairs. All correct and all tested; only the claim that it is the right tool for *this* measurement is withdrawn. It remains the right tool for a density of states over a narrow window, which T11 may want.

## T6 (superseded method). Entropy curve s(φ) by Wang–Landau  ☐

[WL01]. Flat-histogram sampling over S. Validate first on a system with a known answer (e.g. 2D Ising on a small lattice, exact density of states available), then apply to the graph model.

Accept: Ising check within tolerance; s(φ) curves for N ∈ {36, 64, 100, 160} at λ ∈ {0, 1}; at λ = 0 a convex dent must appear (consistency with Gate A).

**Sampler built and validated, 2026-09-21; no production run yet** (`src/graphity/wang_landau.py`, `src/graphity/wl_ising.py`, `tests/test_wang_landau.py`; ASSUMPTIONS Q14 and section D).
- **The Ising acceptance criterion is met**: the 4×4 density of states, brute-forced over all 65 536 states, is reproduced to 0.006–0.013 in ln g across 15 bins spanning a factor of 10⁴.
- **A stronger check the task did not ask for**: the graph kernel against our own exhaustive enumeration at N = 16 and 18 (T4). Every bin found, none invented, worst error 0.016 and 0.014 in ln g; canonical ⟨φ⟩ rebuilt from it matches the exact value to 0.0002. This checks the kernel, where the Ising check only checks the schedule, and the two failing separately is how a fault would be located.
- **Bins are (S, X), not the energy**, so one run gives every λ at once — which makes T8's λ map nearly free and is what S1 wants.
- **Two faults found and fixed**, both invisible without a known answer: plain Wang-Landau saturates (ten times the work, same 20–30 % error) and needs the unbiased second stage `refine`; and re-seeding in short blocks damages the walk (Q14), which also reached `tempering.py` and was checked not to have moved any T5 result.
- **Still to do before the acceptance criteria are met**: pre-register (rule 4, and it is the next thing), then the s(φ) curves at the four sizes and both λ, and the dent at λ = 0.

## T7. Pre-register the λ map  ☐

Write `PREREGISTRATION.md`: λ ∈ {0, 0.25, 0.5, 0.75, 1}; sizes; observables (dent in s(φ) and its scaling with N; hysteresis width; largest-component fraction; Q4 census); what counts as first order, as continuous, as inconclusive; what would count against the hypothesis. Commit before running.

## T8. Run the λ map, then the sealed runs  ☐

**Reframed 2026-09-21.** This is not an open question nobody has looked at; it is a **live disagreement between two groups, each of which has only looked at one end of the knob.** [GV21] finds first order with hysteresis at λ = 0, where the cold phase is knots and not a space, and says the Trugenberger group's earlier runs were too small to hold more than one hypercube so the configuration looked homogeneous. [T25] reports a continuous transition at λ = 1, where the cold phase *is* a space. **They are not contradicting each other on the same model.** No published work runs both energies in one code at matched sizes and asks how the barrier scales, which is exactly what T6 plus this task would do. Say so in the write-up and in the letter.

Questions: at which λ does the order change? Is there any λ with a first-order transition **and** a connected space (VISION S2 and S4 together)? Then fixed-total (sealed) runs as in VISION step 3.

## T9. Unexplained drift  ☐

**Correction, 2026-09-21: the supporting citation is withdrawn.** [DQM25] was recorded as reporting the transition moving with ln N; it was read in full by the owner and **it does not say that.** The claim came from a third-party review page, not the paper. The drift is now supported by our own measurement and by the non-collapse visible in [KTB19] Fig. 8a, and by nothing else.


The capped variant showed the half-order coupling moving with ln N (ASSUMPTIONS D). Repeat the measurement at λ = 1 with parallel tempering and several replicas. Either it disappears, or it is characterised properly (fit 1/g against ln N with errors) and compared with the N-independence stated in [T22].

Note, 2026-09-19, from the sources (ASSUMPTIONS, first-look section): the N-independence in [T22] is a consequence of a continuum-limit argument in [KTB19] Sec. 3.1.1, not a measurement, and [KTB19] Fig. 8a itself shows curves for N = 100 to 200 that do not collapse, in the direction of our drift. So the thing to explain is no longer why we see a drift, but whether it is logarithmic. The prediction to test is a slope of 1 for 16/g against ln N; the first look gave 1.12 with one replica and no error bar.

## Design track (VISION plan step 5)

Brief: `docs/design/model_x_brief.md`. Done so far: the dip census at N ≤ 18 (`scripts/dip_census.py`, `configs/dip_census_small.json`), and a finer one at N = 18 (`configs/dip_census_fine.json`): dips above the flat ground state for 1 < λ < 1.6, none above. `scripts/exact_small_averages.py` gives exact averages at N = 16 and 18 for any g and λ; T5 and T6 should be validated against it. Braces (triangles), the owner's idea: `src/graphity/full_curvature.py`, ASSUMPTIONS Q10; at the published prices they favour a closed 30-vertex piece that ties with the flat sheet, not a braced space. The rehearsal on the backwards reaction is done too (`configs/cqg_sheet_decay_lam0*.json`, exploratory): a perfect flat sheet below λ = 1 waits, then drops abruptly in steps that land on the exact levels, the first of them a dimension curling up. **The forward direction has been seen too** (`configs/cqg_tube_uncurls_lam1*.json`, exploratory): at λ = 1.25 a perfect tube lasts thousands of sweeps and then opens out into one connected, perfectly flat sheet, giving off exactly the 1 per vertex known in advance; at λ = 1.5 it does not last. **Both of those next steps were taken the same day** (exploratory; ASSUMPTIONS section D; VISION Update 9). Waiting times at N = 64 to 192: our pre-registered 1/N prediction is **not supported** (2.9 standard errors at the largest size, after correcting a size-dependent criterion that first made it look like 5.0), though the end state and the energy given off per vertex are the same at every size. Sealed runs (`src/graphity/sealed.py`, Q12): energy is conserved exactly, a tube with nothing to spare can never convert, and the spark it needs is sharply 12 units at every size from N = 48 to 192 (320 recorded runs, `configs/cqg_spark_threshold_lam125.json`), which points the opposite way from the waiting times and is unresolved. Figures: `docs/figures/sealed_story.png` and `docs/figures/equilibrium_curves.png`. Next on this track: (0) reconcile those two (waiting time against g, to see whether there is a wall at all, and where the conversion starts in the graph); (1) leaky runs across a range of leak rates, the author's semi-permeable wall; (2) with T5, look for dips above the flat ground state at N = 64 to 160 for 1 < λ < 2. Exact small-size work may run alongside the tasks above; anything that interprets new physics waits for the gates.

## T10. The second knob: named points or interchangeable ones  ☐

Every run in this repository, and as far as we know every published CQG run, treats vertices as **labelled** — vertex 17 is a different thing from vertex 41. [DQM25] (read in full by the owner, 2026-09-21) studies the alternative, where points are interchangeable as identical particles are, so each isomorphism class counts once. In *their* ensemble the choice decides whether there is a transition at all: the labelled free model is Erdős–Rényi with an analytic free energy and no transition, while the unlabelled free and ferromagnetic models both show one. Their sampling rule (Eq. 72) multiplies the Metropolis acceptance by |Aut(G′)|/|Aut(G)|, which needs an automorphism count at every step. They cite [EK25] for a first-order transition in unlabelled networks that is absent when labelled; **read [EK25] before starting this task.**

This is a knob, so under S1 it needs a dated VISION decision before any run, and the whole of it gets published whichever way it comes out. The owner's argument for it (ours, unverified): VISION says the relationships are the real thing and the layout is a convenience, and by the same reasoning the *names* are a convenience too, which makes the unlabelled ensemble the more faithful model of X. The owner's argument against, recorded in the same breath: unlabelled counting favours arrangements with large symmetry groups, and a shattered state of k identical knots is about as symmetric as an arrangement gets, so **this knob most likely favours shattering and works against claim 4.**

**Feasibility measured, 2026-09-21** (`scripts/measure_symmetry_cost.py`; ASSUMPTIONS Q15): the correction needs a renaming count per step, and at N = 160 one count takes 0.11 s for a fully shattered state, 11.7 s for a perfect sheet and 24.3 s for a melted one. The ordering is the opposite of the obvious guess: the shattered state is cheapest because the group factorises over pieces, and the melted one is dearest because the work goes into proving there is no symmetry, for an answer that is always 1. At about 10^8 moves a run, **no per-move correction is affordable**; apply it to measured configurations or per energy level and check that approximation against the exact small-size answer below. Also measured: a shattered state is favoured by 10^29.4, a sheet by 320, a melted graph by exactly 1, so the two treatments agree for the low-symmetry states that a universe with matter in it resembles and differ most for the idealised ones.

**Free head start, done 2026-09-21 (exact, exploratory, no new runs):** `results/ergodicity_small.csv` already records the symmetry count and the labelled-state count of every class at N = 16 and 18, so both ensembles can be evaluated exactly by arithmetic. The labelled ensemble weights a class by (n!)²/A and the unlabelled one weights it by 1, so the unlabelled ensemble favours a class by exactly its symmetry count A. At N = 16 the 4-cube has A = 192 against a typical few, and its share of the ensemble rises **from 1.3 % to 20 %, a factor of 15**, at λ = 1 where every class is degenerate; at λ = 0, g = 20 it rises from 0.13 to 0.73 and φ moves from 1.347 to 1.454, towards the shattered value of 1.5. At N = 18, where no 4-cube fits, the shift in φ is smaller and at λ = 1 runs the other way (−0.02 to −0.07). **So the mechanism is real and exactly quantified, and at the smallest size where a knot exists it points where the owner said it would.** These sizes cannot shatter — one piece only — so this demonstrates the mechanism, not its consequence. *Ours, unverified; a state of k identical 4-cubes would carry symmetry of order 192^k·k!, so the enhancement should grow steeply with size.*

## T12. Read the coarse-grained literature before building anything there  ☐

**Added 2026-09-21** (owner's proposal, and owner's question about whether anyone has worked there).

**The proposal.** A second model whose state is not a network of points but **the dials themselves** — which directions are large, which are small, how many of each, and how they relate — with the energy written over configurations of dials rather than over wirings.

**Why it is worth considering.** It sidesteps the size problem completely: a network standing in for the observable universe would need of order 10^122 points and we run 160. And the argument of ASSUMPTIONS Q15 licenses it — energy, what cannot happen, and the character of a change are the three things that survive a change of level, and those three are claims 4, 5 and 6. A coarse model cannot derive geometry from relationships, but it can ask whether a change between two settings of the dials is sharp and what it releases.

**Why it is not a free lunch.** Putting the dials in by hand is the move VISION's own filter rejects: a model that already contains dimensions cannot answer where dimensions come from. It would be a *second* model answering different claims, not a replacement, and the write-up has to say so.

**The answer to "has anyone done this" is yes, extensively — and this repository already recorded several of them and has read none.** That is the actual state, and it is the reason this task is a reading task.

Read in this order:
1. **[BV89]** — why three directions grow large and the rest stay small, argued at exactly this level. Already in the bibliography, unread.
2. **[W82]** — a spacetime with a curled-up direction shown to be unstable and able to decay: a transition between two dial settings, and the nearest published relative of the illustration in VISION. Already in the bibliography, unread.
3. **[BP00]** — the landscape: vast numbers of stable dial settings with first-order transitions between them. Claim 4's shape, at scale, in print. Added today.
4. **[Carlip17]** — review of the convergence on effective dimension falling to about 2 at short distances. Added today.
5. **[AJL05]** — causal dynamical triangulations, a competitor approach VISION's survey does not mention, whose main observable is one we already plan to measure. Added today.
6. **[C77]**, **[G81]**, **[GW83]**, **[BGG87]** — the false-vacuum and old-inflation group, all already recorded and all unread. They are the same shape of argument one level up.

**A specific thing to look for while reading** (ours, unverified, and the reason this task is worth doing rather than skipping). The network model already contains a dial model: the sheet/tube/knot ladder of T3 is "how many directions are large", except that here the dials are *derived from the wiring* rather than put in by hand, and they change by themselves. So the tube experiment of the design track is not only a waiting-time measurement — it is **a dimension changing from one to two in a model where no dimension was assumed, with the released energy measured**. If [BV89] and its successors ask "why three directions" with the directions assumed, that is the same question asked one level down. **Find out whether anyone has already framed it that way.** If they have, read them; if they have not, that is the one place where this project has something a mature field does not, and it should be the centre of any write-up.

Accept: a written summary of what each says, what is already settled, and what — if anything — a hobby project could add. **If the honest answer is "nothing", that is the result and the task ends there**, which is a perfectly good outcome and cheaper than finding out later. Building a second model needs its own dated VISION decision after this, under S1.

## T11. What does the half-converted state look like?  ☐

**Added 2026-09-21** (owner's question; VISION Update 12). Every statement in this project about the S2-against-S4 tension, first order but no space at lambda = 0 and a space but no latent heat at lambda = 1, is about the **fully settled** state: the ground state, or a run cooled far past the transition. Nothing is ever in that state. A universe with matter in it is partly converted, which is [T25]'s own position, since for him matter *is* the unconverted part.

So the object claims 4, 5 and 6 are about is the coexistence state, and **nobody has looked at whether it contains a connected geometric region.** At fixed temperature it cannot be looked at: no temperature setting gives a flask of thirty per cent ice, and the canonical ensemble jumps the gap. At fixed total energy it is exactly what you get.

Accept: sealed runs (Q12) at a total energy inside the coexistence gap, at lambda = 0 and at settings above 1, reporting the connectivity observables of T3 **on the coexistence state itself** (`pieces`, `largest_frac`, `baby_frac`, `cube_frac`) and what the largest piece is by the dimension ladder: sheet, tube or knot. The question is narrow and answerable. Is there a connected geometric region inside the half-converted state, and does it survive?

Needs no new machinery: `sealed.py` and `connectivity.py` both exist. Pre-register first (rule 4).

## T13. Known physics out of the model (claim 2): the ladder  ☐

**Added 2026-09-22** at the author's request. Plan: `docs/design/known_physics_plan.md`. Rungs, cheapest first: (1) is what the tube opens into really space (volume-growth and spectral dimension, curvature, locality; reproduce [T25]'s dimension numbers first); (2) is there a speed limit (front position against time; spread of a local disturbance); (3) does matter curve space and do defects attract (energy against curvature; defect–defect interaction, already seen to be non-zero in O13's third addendum; what a local spark does to a flat sheet); (4) the 3+1 and quantum claim of [T23–T25], after reading. Each run pre-registered; no new energy knob without a VISION decision.

Accept: rung 1 reproduces [T25]'s published dimensions with our tools before any number of ours is read.

## T14. Leftover per seed: could the leftover be a real share?  ☐

**Added 2026-09-22** (author's question). Every tube so far opened from one seed (every cold T10 box caught mid-conversion, 78 of 80, had one sheet patch), so whether each seed leaves a scrap is untested. Plant k = 1, 2, 4, 8 seeds with a local spark on a long tube in a cold sealed box and count leftovers; or use tubes long enough (N ≳ 400) for seeds to form naturally. Pre-register: leftovers ∝ k against leftovers = 1 whatever k. Shares the local-spark code with T13 rung 3. Details in the plan above.

*Added the same evening:* the author's hypothesis that the leftover is dark matter (VISION Update 16). A first look (ASSUMPTIONS O18) says a sparse sprinkle of scraps could be enough, because matter thins out more slowly than radiation; the needed share at the conversion is about 0.7 eV divided by the starting temperature. So the test should also measure **how the leftover scales with the number of seeds**, which is what would turn a seed density into a dark-matter amount.

## Later

Scorecard against "the spot" (VISION step 4): spectral dimension, volume-growth dimension, curvature uniformity, shortcut census, stability under perturbation. Allotrope ladder of [T24]: does squares-per-vertex move in jumps with hysteresis?

## Before anything is shown to anyone

VISION S5: a physicist reads it. Draft a short, honest note to C. Kelly, F. Biancalana or C. Trugenberger once Gates A and B have passed: what was reproduced, what was not, the code link, and a request for a sanity check. **Ask also where the evidence for "continuous" lives.** [T25] cites [29] for "several other diagnostics ... with positive results", and [29] is [KTB19], which says of itself that a finite-size-scaling analysis is "at present even ... precluded" and that "we are some way off the asymptotic regime". So the decisive test has not been attempted by anyone (ASSUMPTIONS, section D). That is the gap T6 fills, and we are better placed than they were. The sharpest way to put the disagreement (ASSUMPTIONS, axis section): we match Fig. 3 at both ends, to 0.001 to 0.039 over eleven points from g = 6.3 to 178 and to 0.04 at g = 2, and differ only in between, where its points drop almost vertically at one coupling and ours rise smoothly. The author asked whether Fig. 3 might have allowed triangles and pentagons, since [T25]'s Eq. (22) includes them and it says only that one *can* use bipartite graphs. Tested and ruled out: allowing them roughly halves the square count in the hot phase, while Fig. 3's hot dots sit where the bipartite value is (ASSUMPTIONS, axis section). So the question for the authors is the narrow one about the window between g = 2 and g = 6.3. Also worth a line each: the 14-vertex baby universe (Q8) and the 30-vertex triangle-and-pentagon piece with H = 0 (Q10).

# Assumption register

Every assumption in the code and the planned paper, with its source and how far
it has been checked. Keys in square brackets refer to `REFERENCES.bib`.

**Status legend**

- **Sourced** – taken directly from a paper we read in full; location given.
- **Calibrated** – not stated in the source; we chose the option that reproduces a published number.
- **Ours** – our own choice or argument. No external authority. Needs scrutiny.
- **Unverified** – relies on something we have not read or checked.

## A. Reproducing the basic graphity model (Phase A)

| # | Assumption | Source | Status |
|---|---|---|---|
| A1 | States are simple graphs on N labelled vertices. Energy = valence term + cycle term. | [K08] Sec. II A, Eqs. (7)–(12) | Sourced |
| A2 | Simulate exactly 3-regular graphs only, which removes the valence coupling; set g_B = 1; r = −2.5; count cycles up to L_max = 9 ("energy at the percent level"). | [K08] Sec. IV, Eq. (46) and Sec. IV A | Sourced |
| A3 | Cycle counting convention: P(a, L) counts each simple cycle once per vertex **and once per orientation** (factor 2). On 3-regular graphs "closed walk with no repeated edge" is the same as "simple cycle". | Definition of cycle: [K08] Sec. II A. Factor 2: **not stated in [K08]**. | Calibrated: factor 2 gives ε₀ = −12.207, matching the published −12.2 ([K08] Sec. IV A 2); factor 1 gives −6.10. Test: `test_ground_state_energy_matches_konopka`. |
| A4 | The r = −2.5 ground state is a ring of six-vertex units, each K₃,₃ minus one edge. | [K08] Sec. IV A 1 describes "six groups of six vertices connected in a chain" maximising 4-cycles; the wiring is only in Fig. 2(a), which we could not read. | Calibrated (same check as A3). A3 and A4 are calibrated **jointly** against one number, so they are not independent confirmations. Reading the original Java source ([K08] ref. 29, arXiv source package) would settle both. |
| A5 | Monte Carlo move: local edge switch on a path a–b–c–d, (ab, cd) → (ac, bd). Preserves degree and connectedness; symmetric proposal on regular graphs. | [K08] Sec. IV says its moves (Fig. 1a, 1b) preserve degree and connectedness; figure not read. Detailed-balance argument: ours, written out in `mc.py`. Metropolis rule: [NB99]. | Ours. **[K08] uses two move types; we use one.** This may be why our chains get trapped more easily (open issue O1). |
| A6 | One sweep = N·v₀/2 attempted moves. | [CP12] Sec. IV defines a sweep as N_E steps. [K08] gives no unit. | Sourced from a different paper; affects run lengths only, not equilibrium values. |
| A7 | Start from a connected random 3-regular graph (Steger–Wormald algorithm via networkx). Random cubic graphs are connected with probability → 1. | Start state: [K08] Sec. IV A 1, citing [SW99]. Connectivity: [W99]. | Sourced |
| A8 | Specific heat C = β²(⟨E²⟩ − ⟨E⟩²), plotted as C/N², bootstrap errors. | [K08] Eq. (41), Fig. 5; [CP12] Sec. IV C | Sourced. Block (not single-sweep) bootstrap is our choice, following standard practice for correlated samples [NB99]. |
| A9 | Reproduction targets: ε₀ = −12.2; specific-heat maxima near β = 0.13, 0.16, 0.17, 0.18 for N = 60, 120, 180, 240; analytic estimate β_c ≈ (v₀/2 − 1) ln N / \|ε₀\|, which overshoots by ~20 %. | [K08] Sec. IV A 3 and Eq. (43a) | Sourced |

## B. The new ingredient: a restricted menu (Phase B)

| # | Assumption | Source | Status |
|---|---|---|---|
| B1 | Only edges in a fixed "menu" graph M may be switched on. M = complete graph recovers the original model exactly, which is our regression test. | The published models all use the complete graph: [KMS06] Sec. II, [K08] Sec. II, [CP12] Sec. III. The restriction is ours. | Ours. Novelty claim rests on ~7 literature searches, **not exhaustive**. Two relevant papers are still unread: [WG15], [DQM25]. |
| B2 | Random menu = planted random cubic graph + independent random (K−3)-regular graph, made edge-disjoint by edge swaps. | Ours. Sums of independent random regular graphs are known to be contiguous to uniform random regular graphs [W99] – **section not yet checked by us**. The swap repair step is a small extra bias. | Ours / Unverified |
| B3 | Lattice menu = d-dimensional periodic grid (degree 2d); start state = a connected 3-regular spanning subgraph (brick-wall construction generalised to d dimensions). | Ours. Correctness (3-regular, connected, inside menu) is tested in `test_torus_menus` for d = 2, 3, 4. | Ours, tested |
| B4 | The disordered-phase entropy is super-extensive (∝ N ln N) because any vertex can link to any other, and this drives T_c → 0. | [K08] Eqs. (34), (35), (43); [CP12] Sec. IV C and Fig. 10 (ΔS/N_V = γ′ ln N_V + b, γ′ ≈ 0.065) | Sourced |
| B5 | Published remedies are: finite universe, couplings that grow with N, long-range repulsion between defects. | [CP12] Abstract and Sec. V; coupling remark also in [K08] Sec. VI | Sourced |

## C. The argument the paper would make

| # | Claim | Source | Status |
|---|---|---|---|
| C1 | In a uniform random K-regular graph with K fixed, the number of cycles of each fixed length k is asymptotically Poisson with mean (K−1)^k / (2k): a finite number that does **not** grow with N. | Bollobás (1980) and Wormald (1981), as stated in [W99] Thm 2.5; extension to slowly growing K in [MWW04]. We confirmed the statement through secondary sources quoting it; we have **not** read [W99] itself. | Sourced (secondary) |
| C2 | Therefore a subgraph of a random bounded-degree menu can gain at most a fixed total energy, Σ over energy-lowering L of \|w(L)\|·(K−1)^L/(2L), so the cycle energy per node falls like 1/N and there is no ordered phase as N → ∞. | Ours, follows from C1 and A1. Bound implemented in `analysis.random_menu_energy_bound`. | Ours. A referee should check it. **The constant is large**: 627 for K = 4, 21 098 for K = 6, 8.7 million for K = 12 (r = −2.5, L_max = 9), so the argument only bites when N ≫ (K−1)^L_max. It is an expectation bound, and it applies only to Hamiltonians that reward cycles of bounded length. |
| C3 | For the ground state of A4 to fit inside a random menu at all, K must grow roughly like N^(1/3) (first-moment estimate). | Ours, back-of-envelope. | Ours, **unchecked**. Do not quote without a proper derivation. |
| C4 | On a lattice menu the entropy is extensive, so T_c should not depend on N. | Textbook statistical mechanics of short-range lattice models; the general entropy argument is spelled out in [CP12] Sec. IV C. | Expected, not yet simulated. This half is unsurprising on its own. |

## D. The 2D combinatorial quantum gravity model (VISION step 2)

Full statements and derivations are in the docstring of `src/graphity/cqg.py`.

| # | Assumption | Source | Status |
|---|---|---|---|
| Q1 | Energy H = 16(N − S) once no edge carries more than two squares; general form 4·Σ_e(2 − S_e)₊. | Derived by us from the edge-curvature formula [T22] Eq. (2) at D = 2 on bipartite graphs. Matches the global term of [T24] Eq. (4) and the D = 2 mean-field action of [KTB19]. | Ours, cross-checked on two limits (random graph 16N, flat torus 0). **Confirmed against [T25] on 2026-09-19 (text read directly, not summarised):** Eq. (21) defines H = −2D Σ_i Σ_{j∼i} κ(ij), a sum that visits every edge twice, and Eq. (8) gives κ = −(2 − S_e)₊/2 for D = 2 without triangles or pentagons; together, H = 4 Σ_e (2 − S_e)₊ exactly. One wrinkle: read with each edge counted once, the local term as printed in [T25] Eq. (22), and the matching correction term in [KTB19] Sec. 3.3, would carry a coefficient 2, not 4. Only 4 makes the paper's own statement true that the two effects "cancel exactly" (4-cube: −128 + 4·32 = 0), so its edge sums must run over both orientations. |
| Q2 | On bipartite graphs the hard-core rule is equivalent to "no two vertices share more than two neighbours" (no K₂,₃). | Rule: [T22], [T24]. Equivalence: ours. | Ours; consistent with the text definition in [T25] ("any two cycles can share at most one edge", for triangles, squares, pentagons). ~~Figure of excluded subgraphs ([T25] Fig. 1) not inspected.~~ **Inspected 2026-09-19: confirmed.** Of the five excluded subgraphs, (b), labelled (□,□), is the only one made of squares alone: two vertices joined to three common neighbours, which is K₂,₃. The other four each contain a triangle or a pentagon and cannot occur in a bipartite graph. [T25] also says the maximum number of squares on an edge is 2D − 1 = 3, which is what "at most two common neighbours" implies. |
| Q3 | ~~No edge may carry more than 2 squares (hard cap).~~ **Superseded.** [T25] Sec. "Cycle condensation" describes the published model as using the *full* Hamiltonian, Eq. (22): the global term plus a **soft local term that penalises** edges with more than 2D−2 squares, with no hard cap. It states that the two effects "cancel exactly" so that denser configurations are "degenerate" with the torus, which confirms our Q1 coefficient and our 4-cube tie. It also states: global term only → **first-order** transition into isolated hypercubic complexes ([KTB19], [GV21]); full Hamiltonian → **continuous** transition. | [T25]; our first-look code | **Our first look simulated a third variant (global term + hard cap), which is neither of the two published cases.** Its results do not yet test the published claims. To do: implement the local term, remove the cap, rerun. **Corrected 2026-09-19, after reading [KTB19] Sec. 3.3 and Sec. 4 directly: the capped variant IS a published case.** [KTB19] defines P_ω as the set of edges with more than d − 2 squares (plus triangles), i.e. more than 2 for us, and states that its simulations (Figs. 8 and 9, the evidence offered for a continuous transition) ran "the mean field action" on the space with P_ω = ∅, where "both the exact action and the mean field action agree". That is this code: cap of 2, H = 16(N − S). Our first reading of [KTB19] was right; this row's "superseded" went too far. So there are three published cases, not two, and they lie on one line (*Ours*): H = 16(N − S) + 4λ Σ_e (S_e − 2)₊ with λ = 0 (first order, hypercubes), λ = 1 (full Ollivier curvature, [T25]) and λ → ∞ (the cap, [KTB19] Sec. 4). [KTB19] did not simulate the annealed transition at λ = 1; it says only that this "seems likely" to be "in the same universality class". T2 is still needed for λ = 0 and λ = 1. |
| Q4 | Move = bipartite edge switch; symmetric proposal; invalid states rejected. Connectedness not enforced. Acceptance: Metropolis min(1, a), or Glauber 1/(1 + 1/a), with a = exp(−ΔH/g). | "Edge switches": [KTB19] Sec. 4. Details: ours. Metropolis: [NB99]. Glauber: [T25] Eq. (28), read from the source text. | Ours. Both rules satisfy p(ΔH)/p(−ΔH) = a, which with a symmetric proposal is detailed balance; they are tested to give the same average (`test_glauber_and_metropolis_sample_the_same_distribution`). ΔH is exact, tested against full recomputation and against networkx at λ = 0, 0.5, 1 (`test_incremental_energy_is_exact`). Ergodicity: proved by exhaustive listing for N ≤ 18, with and without the cap; unproven beyond (Q9). |
| Q5 | Start from an lx×ly torus, both sides even and ≥ 6, melted at infinite temperature. A side of 4 is refused: it closes a 4-cycle around the torus, so half the edges carry three squares and S = 1.25 N. | Ours. | Ours; melting is tested (`test_melts_at_infinite_temperature`), the 16×10 case in `test_rectangular_torus`. The side-of-4 statement was checked by brute force with networkx on 4×6 and 4×10. |
| Q6 | Error bars on φ and on the fluctuation measure N·var(φ): block bootstrap over 20 blocks of sweeps, 500 resamples (columns `phi_err`, `chi_err`). Beside them, the integrated autocorrelation time τ in sweeps (`tau_int`), summed with an automatic window that stops at the first t ≥ 5τ. | Block bootstrap: same choice as A8, [NB99]. Windowing rule: [S97], **from general knowledge, not read by us**; the factor 5 is a conventional value, to verify. | Ours, tested on series with known answers (`tests/test_analysis.py`). **Limits:** the error bars hold only where a block (n_meas/20 sweeps) is much longer than τ. Where the chain is freezing they are underestimates, which would make heating and cooling look *more* different than they are, i.e. it would fake hysteresis. `tau_int` is a lower bound when the series never decorrelates, and NaN when the chain did not move at all. Twenty blocks and one replica is a first-look choice; the pre-registration (T7) must fix the production choice. |
| Q7 | Random seeds. "legacy": config seed + 100000·replica + L + step, the formula of the first look. "independent": one seed per (config seed, lx, ly, replica, step) drawn through numpy's `SeedSequence`, which is built to turn such a tuple into statistically independent streams. | Ours. `SeedSequence`: numpy documentation, from general knowledge. | Ours, tested (`test_seed_schemes`). **Known flaw of "legacy":** it reuses seeds across sizes (L = 10 at step 5 and L = 14 at step 1 get the same one), so runs at different sizes are not strictly independent. The effect on the first look is expected to be negligible, since the same random numbers drive different systems, but it is not measured. "legacy" stays the default only so that `cqg_first_look` reproduces bit for bit (T2 regression); it refuses rectangles. **Every new config should say `"seed_scheme": "independent"`.** |
| Q8 | Connectivity observables (task T3), each averaged over the measurement sweeps: number of connected pieces (`pieces`), share of vertices in the largest (`largest_frac`), share of vertices in **baby universes** (`baby_frac`), and share of vertices in baby universes that are 4-cubes (`cube_frac`). A baby universe is a connected piece in which every edge carries the largest possible number of squares, 2D − 1 = 3; these are the lowest-energy pieces the global term allows, −8 per vertex. The census is strict: a cube with one defect, or two cubes joined by a few edges, counts as zero. | Definition of a baby universe, and that the λ = 0 ("mean field") vacua are collections of them: [KTB19] Sec. 3.3.1, text read directly. What they look like at D = 2: [KTB19] Fig. 5, inspected 2026-09-20: four separate 16-vertex pieces drawn like 4-cubes, and one larger piece not yet split. "Isolated, weakly interacting hypercubic complexes": [T25] Sec. "Cycle condensation". The strict census, the test for a 4-cube (4-bit addresses, every edge flips one bit) and the four summary numbers: ours. | Ours, tested against networkx, including a true isomorphism test on graphs the chain itself shattered (`tests/test_connectivity.py`). Looking uses no random numbers and is tested to leave the chain unchanged; `cqg_first_look` was re-run at full size and is identical on its eight original columns. **Finding (ours, checked by computer, 2026-09-20): the 4-cube is not the only baby universe.** The graph of the seven points and seven blocks of the biplane (the complement of the Fano plane; 14 vertices, any two points in exactly two blocks) is a valid state with three squares on every edge, so it ties with the 4-cube in energy per vertex at every λ (`test_the_four_cube_is_not_the_only_baby_universe`). Neither [KTB19] nor [T25] mentions it; [KTB19] allows for it in general terms ("situations where more than one baby universe exists"). Whether it appears in simulations is an open question that `baby_frac − cube_frac` answers. We have not shown that these two are the only ones. **Wrinkle:** [KTB19] gives φ = (2D − 1)/(D − 1) for a baby universe, which is 3 at D = 2; with φ = S/N, the normalisation that reproduces its Fig. 8a, the value is 1.5, and its own Fig. 6 (quench at λ = 0) climbs towards 1.5, not 3. We read the printed formula as missing a factor 2. **Limit:** because the census is strict, `baby_frac` is a lower bound on how far a cold state has shattered; read it together with φ (1.5 when perfect) and `surplus` (2 when perfect). |
| Q9 | Ergodicity of the edge switch (task T4). **What has to hold:** the switch must join all *classes* of states, a class being all states that differ only by renaming vertices within a side. That is enough, and joining all labelled states is not needed: every observable we use is unchanged by such renaming, and renaming turns moves into moves, so if all classes are joined, every region the chain can be confined to is a renamed copy of every other and gives the same averages. **How completeness is proved:** by counting. The labelled states are counted directly, without reference to the moves (L = G·C(n,4)·(n−1)!, where G is the number of tables with increasing rows that contain one fixed row). The classes reached by switches from one state are collected, and a class whose graph has A side-preserving symmetries holds (n!)²/A labelled states. If these add up to L, the list is complete and the switch joins all of it. | Ours: the argument, the counting formula and the code (`src/graphity/small_graphs.py`). Isomorphism tests and symmetry counts: networkx (VF2). | Ours, tested (`tests/test_small_graphs.py`; recorded run `results/ergodicity_small.csv`). **Result, exhaustive, no sampling:** no states exist for N ≤ 12. N = 14: 151 200 labelled states, one class (the biplane graph of Q8), and *no* switch from it is valid, so the chain cannot move there at all; harmless, because there is one class. N = 16: 635 040 000 states, 5 classes, all joined. N = 18: 1 785 021 235 200 states, 26 classes, all joined. Under the cap: no states up to N = 16; N = 18: 20 118 067 200 states, 3 classes, all joined. The counting formula is checked against a brute-force count that shares none of its reasoning (N = 14). **The chain is then checked against exact answers:** with every state and its energy known, ⟨S⟩ is a finite sum. At N = 16 and N = 18, for λ = 0, 0.5 and 1, both acceptance rules, the chain agrees with the exact value to within its error of about 0.03 % (section D below). This tests the proposal, both terms of the energy, the acceptance rules and ergodicity together. Also tested: the kernel's quick validity check agrees with the full one on every possible switch from several states (`test_quick_validity_check_agrees_with_the_full_one`). **Limits, stated plainly:** this proves ergodicity only for N ≤ 18. N = 20 was started and its direct count did not finish in about 40 minutes. For the sizes we simulate (64 and up) ergodicity remains unproven, as it is in the published work, which does not discuss it; what these sizes give is the absence of a counterexample where one could be found, and a sampler verified against exact results. The "neighbourhood swap" of [T25] Fig. 8 was not needed at these sizes and has not been added. |
| Q10 | The energy on graphs that need not be two-sided, so that triangles and pentagons can occur (`src/graphity/full_curvature.py`; a slow exact reference for small graphs, not a simulation kernel). Edge curvature κ = T/4 − [1 − (2+T+S)/4]₊ − [1 − (2+T+S+P)/4]₊ with T, S, P the triangles, squares and pentagons through the edge; H = −4 Σ κ over both directions of every edge. Valid graphs: 4-regular, simple, no two cycles of length 3 to 5 sharing more than one edge. Move: the general edge switch, (a,b),(c,d) → (a,c),(b,d) or (a,d),(b,c). | Curvature: [T25] Eq. (8); energy: Eq. (21); prices of the three kinds of loop in the global term, 9/8 : 1 : 5/8, Eq. (22); the rule about shared edges: [T25] Def. 2 and Fig. 1. All read from the text. The published simulations, and our kernel, use two-sided graphs, where T = P = 0 ([T25]; [KTB19] Sec. 4). The general move: ours. | Ours, tested (`tests/test_full_curvature.py`): on two-sided graphs the general energy equals the kernel's H at λ = 1 on every state tried. **Why it was written:** the owner asked whether a "brace", a diagonal support across a block, could stabilise an arrangement. A brace makes triangles, so the published formula already prices it. **Exact results at the published prices:** (1) the flat square sheet stays a dip when braces are allowed (cheapest way out +16). (2) The braced sheet (kagome: every edge in one triangle, no squares) is valid, sits 4 per vertex above the flat sheet, and is *not* a dip: one move that puts a pentagon beside two triangles lowers it by 20, whatever price the triangles are given; followed downhill on a 27-vertex torus it stops in a dip at 1.78 per vertex. (3) **The 30-vertex closed piece with a triangle and a pentagon on every edge (the icosidodecahedron) has κ = 0 on every edge, so H = 0, the same as the flat sheet, and it is a dip (way out +20).** In the global term this is (9/8)(2/3) + (5/8)(2/5) = 1 square's worth per vertex. [T25] argues that triangles and pentagons "are excluded for an homogenous ground state" because a triangle–pentagon couple earns 9/8 + 5/8 < 2; that compares per couple, not per vertex, and this arrangement looks like a counterexample to the conclusion. The rule about shared edges was checked against [T25] Fig. 1 (image inspected 2026-09-20): each of its five excluded subgraphs is a pair of short cycles sharing two or more edges, which is the rule the code applies, and in this piece a triangle and a pentagon share exactly one edge, which the text allows. *Ours, unreviewed;* one for the note to the authors. It is a closed piece, not a space: paying braces any more than the published price would favour such pieces over the flat sheet. |
| Q11 | Parallel tempering (task T5): one copy of the system at each of several couplings, ordinary sweeps, then offers to swap whole graphs between neighbouring couplings, accepted with probability min(1, exp((1/g_i − 1/g_j)(H_i − H_j))). Neighbours only, pairs (1,2),(3,4),… and (2,3),(4,5),… on alternate rounds; every (round, copy) has its own seed and the swap decisions their own stream, all from one numpy `SeedSequence`. | The method: standard (replica exchange), from general knowledge, [NB99] for the Metropolis rule. The detailed-balance argument for the swap is written out in `src/graphity/tempering.py`. The details listed here: ours. | Ours, tested (`tests/test_tempering.py`). **Decisive test:** at N = 18, four couplings at once, each coupling reproduces the exact average for *its own* coupling (λ = 0 and 1, both acceptance rules); a wrong swap rule would pull the four together. **Limit:** tempering makes a frozen chain move, it does not make slow physics fast. Report `round_trips` (graphs that went from the hottest coupling to the coldest and back) with every run; where it is 0 or 1 the cold end has not been refreshed from the hot end and is not in equilibrium. |
| Q12 | Sealed and leaky runs (`src/graphity/sealed.py`). Beside the graph one number, the DEMON, holds energy and is never allowed to go negative; a switch is accepted exactly when the demon can pay for it, ΔH ≤ demon, and then demon −= ΔH. Same moves, same configuration space, same validity rules as `cqg.run_chain`. After each sweep the demon keeps a fraction (1 − leak) of its energy and the rest is counted as gone: leak = 0 is sealed, leak = 1 removes everything given off as fast as it appears, in between is the author's semi-permeable wall. The leak is a choice of protocol, not of model, and is declared before a run like any other knob (S1). | The demon: Creutz 1983, from general knowledge, not read by us; standard. The leak and the rest: ours. | Ours, tested (`tests/test_sealed.py`). **Exact by construction and checked:** H + demon + what has leaked never changes, to the last bit, at λ = 0, 0.5, 1 and 1.25; the demon never goes negative; energy only ever leaves. That is the bookkeeping VISION claim 6 asks for. **The temperature is measured, not set:** the demon settles into P(demon) ∝ exp(−demon/g), so its mean gives g = step/ln(1 + step/mean) where step is the smallest possible change of H (16 at λ = 0, 4 at λ = 1, 5 at λ = 1.25). Prepared at a known coupling and then sealed, the demon reads it back: 5.1 ± 0.1 for g = 5, 7.7 ± 0.2 for 8, 13.5 ± 1.9 for 12, 20.9 ± 1.4 for 20 (N = 144, six runs each; the error grows with g because the demon fluctuates more). **Limit:** the demon is one degree of freedom against N, so it takes almost none of the energy; the temperature reading is meaningful only after the run has settled. |
| Q13 | The wall round an arrangement, and how often the sampler offers a way over it, are both countable exactly rather than fitted. From a perfect tube at λ = 1.25: the cheapest valid switch costs **B = 12** (it loses two squares and four surplus squares, 32 − 20), and the number of proposals that do so is exactly **6N**, out of the 4N² the sampler can make (it picks (u₁, slot) and (u₂, slot) independently from N/2 vertices and 4 slots). A sweep is 2N attempts, so the chances of a way over the wall per sweep are 2N · 6N/4N² = **3, at every size**. Under Metropolis the waiting time should then be 1/(3 exp(−B/g)) sweeps. | Ours; the counting is exact and is checked by `scripts/run_waiting_time.py` against the measured waits. | Ours, tested (section D below). **This settles a contradiction we had written down and resolves it in favour of the local wall.** The earlier claim that the waiting time ought to fall like 1/N was simply a malformed prediction: a sweep is already 2N attempts, and the proposals go as N² while the good ones go as N, so the two factors of N cancel exactly and a flat waiting time in sweeps is what a *local* wall predicts. |
| Q14 | **Re-seeding the random generator in short blocks damages a run, and every driver that calls the kernel repeatedly must carry one stream instead.** `cqg.run_chain`, `wang_landau._wl_sweeps` and `wl_ising._ising_sweeps` now take `seed < 0` to mean "carry on the previous call's stream"; `seed >= 0` seeds as before, so every existing script and the bit-for-bit regression are untouched. `tempering.temper` and the Wang-Landau drivers seed once and then pass −1. | Ours. The effect was found while validating T6 against a known answer and is measured, not assumed. | Ours, measured. **The evidence:** 4×4 Ising, weights held at the exactly correct density of states, total work fixed at 200 000 sweeps, twelve independent runs of each variant. Carried on one stream the visit histogram is flat to **0.023 ± 0.009**; re-seeded every 200 sweeps it is flat only to **0.409 ± 0.280**, and the damage grows with the number of re-seeds (1 block 0.985, 10 blocks 0.971, 100 blocks 0.871, 1000 blocks 0.879 on min/mean). **It is extra noise, not a bias:** the draws themselves are clean (200 000 fresh seeds; the mean, the share of each value and the pairwise correlations of the first six draws are all where they should be), and averaged over runs the histogram is flat to 0.4 %. **Does it change any result already recorded?** Checked, and no. `tempering.temper` used to re-seed at every (round, copy), about 200 000 times per production run, five sweeps apart. Measured against the exactly known ⟨S⟩ at N = 18, λ = 1, four couplings, 24 runs each way: the old seeding lands −0.0, +0.7, −0.5, +0.5 standard errors from exact and the new one −0.3, −0.6, −1.8, −1.5. Both are consistent with exact, so **T5 and everything built on it stand**; the run-to-run spread we already report absorbs the extra noise. For a flat-histogram walk it would not have been absorbed, because the noise goes straight into ln g, which is why it was found there and fixed everywhere. |

### First look (2026-09-19, `configs/cqg_first_look.json`; one replica, short runs, NOT publication quality)

- A crossover from random (φ = S/N near its finite-size floor) to ordered (φ → 0.9+) exists, as published.
- **The crossover moves with system size.** Coupling at which φ = 0.5: g = 7.64, 5.51, 4.34, 3.51 for N = 100, 196, 400, 900. Against ln N, 1/g rises almost linearly with slope ≈ 0.07. The plain energy-versus-entropy count (16 energy units per node against ≈ ln N entropy per node for 4-regular graphs; same argument as [K08] Eq. (43)) predicts 1/16 = 0.0625. [T22] states the D = 2 critical coupling does not depend on N. **Until Q2–Q3 are verified and the published curve is compared directly, this is a discrepancy to investigate, not a finding.** *(Added 2026-09-19 from the sources. The N-independence is a theoretical statement, not a measurement: [KTB19] Sec. 3.1.1 rescales the coupling by |V|^(1−2/D) so that the continuum limit of the action stays finite, the exponent is zero at D = 2, and [T22] repeats it as g_cr(N) = χ_cr N^(1−2/D). [KTB19] says a finite-size-scaling analysis of the N-dependence was "impractical in the present model". Its own Fig. 8a, six sizes from N = 100 to 200, shows the curves NOT collapsing, larger N lying lower at the same coupling, which is the direction of our drift; the text says collapse "is not evident until rather high values" of the inverse coupling and puts it down to finite-size effects. A power law with exponent zero is exactly where a logarithm can hide. Still not a finding: one replica, four sizes.)*
- No hysteresis between cooling and heating in the crossover region. Small differences appear only at g ≤ 3 where acceptance is below 1 %, i.e. the chain is freezing.
- The peak of the fluctuation measure N·var(φ) is ≈ 0.16 at every size. No sharpening with N, so at these sizes there is no sign of a first-order transition, and no sign of a sharpening critical point either.
- **Independent check passed:** the hot-phase floor of φ matches the Poisson prediction (2D−1)⁴/4 = 20.25 squares regardless of N quoted in [T25]: predicted 0.2025, 0.1033, 0.0506, 0.0225; measured 0.198, 0.106, 0.053, 0.024 for N = 100, 196, 400, 900. *(Qualified later on 2026-09-19, see O5: these were measured at g = 200, not at infinite temperature, and the agreement is a few per cent with a trend in N, measured/predicted running from 0.98 to 1.07. "Passed" overstates it.)*
- **The gate is now concrete** ([T25] Fig. 3): S/N against log g at **N = 160**, cooled from random and heated from the torus, no hysteresis, random-phase floor 0.126. Needs a rectangular torus (e.g. 16×10) and the full Hamiltonian (see Q3). **Not yet passed.**
- The published curve is for a single size, so our drift-with-N observation is neither confirmed nor contradicted by it. [T25] does not discuss N-dependence of the 2D critical coupling.

### N = 160 against [T25] Fig. 3 (2026-09-19, `configs/cqg_n160_capped_vs_t25fig3.json`; EXPLORATORY, four replicas, not a gate)

What was compared. The published points were read off the figure by `scripts/digitise_t25_fig3.py` (22 points, `docs/published/T25_fig3_digitised.csv`, good to about ±0.005; the axis is log₁₀ g). The capped kernel was run at the same size and the same 22 couplings, cooled from random and heated from a fresh torus. Parameters were fixed from the published figure before the run; it was run once. Table: `python scripts/compare_with_published.py results/cqg_n160_capped_vs_t25fig3.csv docs/published/T25_fig3_digitised.csv`.

- **Hot side, g ≥ 6.3 (11 published points): agreement.** Differences are mostly below 0.01 and never above 0.024, which is about the scatter of the published dots among themselves. Heating at g = 6.31 gives 0.482 against a published 0.481. The onset of the rise is therefore in the same place.
- **Cold side, g < 6.3: large disagreement, up to 0.44.** Published: 0.73, 0.84, 0.99 on cooling at g = 6.0, 5.7, 5.1, and 0.89, 0.97 on heating at g = 5.9, 5.6, a jump of about 0.45 within 7 % in g. Ours: a smooth rise, 0.50, 0.52, 0.58 at the same couplings.
- **Our side of that disagreement can be trusted for g ≥ 5.** From g = 15.85 down to g = 5.01, cooling from random and heating from a perfect torus, opposite starting points, agree to 0.001 in all four replicas, with τ between 1 and 11 sweeps against blocks of 200. Two opposite starts converging is the practical test of equilibrium. So the capped model at N = 160 has φ = 0.53 at g = 5.6, where the published figure has 0.97. Equilibrium values do not depend on the acceptance rule, so Metropolis against Glauber cannot be the reason.
- **Below g ≈ 4 nothing can be concluded.** At g = 3.98 the heated torus is still melting (0.75, replicas 0.15 apart, τ ≈ 490, longer than a block); at g ≤ 2 the torus stays at exactly 1 and the cooled graph is stuck near 0.95, τ undefined. This is the freezing already noted; it needs parallel tempering (T5).
- **Reading (Ours, unverified). WITHDRAWN the same day: the next section tested it and it failed.** [KTB19] Fig. 8a, which is explicitly the capped model, is also smooth at N = 160: about 0.53, 0.62, 0.73 at G = 6, 5, 4 *read by eye, not digitised*, against our 0.50, 0.58, 0.68. So this code agrees with the published capped model and disagrees with [T25] Fig. 3 exactly where the two published figures disagree with each other. The simplest explanation is that Fig. 3 shows the other model, the full Hamiltonian without the cap, which is what the text of [T25] says it is discussing. If so, the published evidence already contains a contrast that bears on the working question: **a hard cap gives a smooth crossover; the soft penalty gives a sharp jump, with the onset in the same place.** A jump of 0.45 in the order parameter within 7 % in coupling at N = 160, with no hysteresis, is presented in [T25] as continuous; it is at least as much what a weak first-order transition looks like at that size. Only T2 can test this. Until then it is a reading of two published figures and one exploratory run, not a finding.
- **What the run shows about Gate B as written.** This run *passes* all three written criteria (floor 0.128; heating and cooling agree through the crossover; 1.000 at the cold end when heated from the torus) while differing from the published curve by up to 0.44. The written criteria cannot tell a right model from a wrong one. The digitised points can.

### λ = 1 without the cap at N = 160, against both published figures (2026-09-19, `configs/cqg_n160_lam1_nocap_vs_t25fig3.json`; EXPLORATORY, four replicas, not a gate)

The first run of the T2 kernel. Identical to the capped control above in every respect except that the cap is lifted, so the cap is the only difference between the two. The question was fixed before the run: does lifting the cap produce the jump of [T25] Fig. 3? Run once; everything kept.

- **Answer: no.** At λ = 1 without the cap the curve is still smooth: 0.51, 0.54, 0.56, 0.62 at g = 6.3, 5.9, 5.6, 5.0, about 0.04 above the capped model and nowhere near the published 0.48, 0.89, 0.97, 0.99. Largest difference from [T25] Fig. 3: 0.41. **The reading offered in the previous section, that Fig. 3 shows the uncapped model, is not supported and is withdrawn.**
- **It is in equilibrium there.** For every g from 10 down to 5, cooling from random and heating from a perfect torus agree to 0.003 in all four replicas, with τ ≤ 8 sweeps against blocks of 200. The fluctuation measure χ stays flat near 0.17; a jump of 0.45 between two states would push it to order N·(0.45/2)² ≈ 8. Lifting the cap also helps the chain move: at g = 3.98 the two legs now differ by 0.010 where the capped model had 0.075.
- **[KTB19] Fig. 8a is reproduced.** Its N = 160 series was digitised (`scripts/digitise_ktb19_fig8a.py` → `docs/published/KTB19_fig8a_N160_digitised.csv`; the calibration is checked by the recovered couplings coming out as the integers 1, 2, 4, 5 … 19, to 0.2 %). Over the 14 published points with g ≥ 4.9, where our chain is in equilibrium: **rms difference 0.005, largest 0.009** (`python scripts/compare_with_published.py results/cqg_n160_lam1_nocap_vs_t25fig3.csv docs/published/KTB19_fig8a_N160_digitised.csv interpolate 4.9`). This is the curve VISION names as the gate of plan step 2. It is independent evidence, to half a per cent, that the sampler and the T2 energy are right. Whether to call that gate passed is the owner's decision: one size, one exploratory run, and only the range where we equilibrate.
- **A wrinkle, reported as found.** The text of [KTB19] Sec. 4 says Fig. 8 was made on the capped space (Q3). The numbers say otherwise: the capped model fits the same 14 points with rms 0.015 and lies up to 0.040 low, and that gap is eight times the digitising error. The figure matches the *uncapped* full Hamiltonian. We cannot explain the mismatch between that paper's text and its figure. Q3's correction stands as a statement of what the text says.
- **So the conflict is between the two published figures, not between us and the literature** (*Ours*). Same group, same model family, same N = 160: at g = 5, Fig. 8a has 0.615, which we reproduce, and [T25] Fig. 3 has 0.99. They also differ on the hot side, 0.348 against 0.311 at g = 10. That is about the scatter of a single configuration (the spread of φ from sweep to sweep is 0.03 at this size), which suggests the points of Fig. 3 are single configurations, not averages. One more hint that Fig. 3 is not the uncapped model: that model cools to φ ≈ 1.005, packing surplus squares onto edges (0.19 per vertex), while every cold point of Fig. 3 lies below 1.
- **Unexplained, and not resolvable from the papers.** [T25] does not say which variant Fig. 3 shows, how long its runs were, or whether its points are averages. Only the authors can say. This is the case the proposed Gate B text provides for: stop and write to them.
- **What it means for the working question, stated plainly because it is not the answer hoped for.** Neither published variant we can build shows any first-order signal at N = 160: no jump, no hysteresis between opposite starts, no growth of χ. At this size both are smooth crossovers, which is what the published "continuous" claim predicts. The one published figure that looks like a first-order jump is the one we cannot reproduce. λ = 0 (Gate A), where first order is the *published* result, is now the natural next test of the kernel and of the hypothesis.

### Parallel tempering at N = 160 (2026-09-20; task T5; EXPLORATORY, four replicas, every copy started from its own melted torus)

`configs/cqg_n160_capped_tempering.json`: the capped model, 14 couplings from g = 6.31 to 2.0, 6000 rounds thrown away and 12 000 recorded, 5 sweeps a round, so 60 000 recorded sweeps per coupling. The three hottest couplings are couplings of the plain run `cqg_n160_capped_vs_t25fig3`. "Spread" is the standard deviation between the four replicas.

| g | φ, tempering | spread | φ, plain run (both legs) | swap rate to next colder | τ (sweeps) | χ |
|---|---|---|---|---|---|---|
| 6.31 | 0.4820 | 0.0001 | 0.4820 | 0.29 | 3 | 0.149 |
| 5.62 | 0.5272 | 0.0004 | 0.5278 | 0.26 | 4 | 0.140 |
| 5.01 | 0.5744 | 0.0005 | 0.5751 | 0.24 | 7 | 0.132 |
| 4.50 | 0.6211 | 0.0007 | | 0.29 | 12 | 0.124 |
| 4.10 | 0.6628 | 0.0004 | | 0.27 | 18 | 0.118 |
| 3.75 | 0.7047 | 0.0009 | | 0.28 | 34 | 0.115 |
| 3.45 | 0.7460 | 0.0011 | | 0.28 | 70 | 0.114 |
| 3.20 | 0.7879 | 0.0017 | | 0.29 | 163 | 0.118 |
| 3.00 | 0.8287 | 0.0037 | | 0.32 | 421 | 0.143 |
| 2.85 | 0.8769 | 0.0076 | | 0.32 | 2128 | 0.179 |
| 2.70 | 0.9208 | 0.0080 | | 0.45 | 921 | 0.044 |
| 2.50 | 0.9350 | 0.0079 | | 0.40 | 1353 | 0.026 |
| 2.25 | 0.9500 | 0.0056 | | 0.33 | 1226 | 0.008 |
| 2.00 | 0.9645 | 0.0071 | (0.96, frozen) | | 1604 | 0.004 |

- **T5's three criteria.** Swap rates: 0.24 to 0.45 on average (asked: 0.2 to 0.4); single replicas show 0.07 to 0.58 at the two coldest pairs. Cold end from a random start: φ = 0.958 to 0.974 at g = 2 in all four replicas (asked: above 0.95). Agreement with plain runs where those equilibrate: to 0.0007 at all three shared couplings.
- **How far down it can be trusted.** Four independent replicas from random starts agree to 0.002 for g ≥ 3.2 and to 0.004 at g = 3.0, with τ far below the run length. A single chain could be trusted only for g ≥ 5, so the equilibrium curve now reaches from φ = 0.57 to φ = 0.83. Below g = 3 the replicas differ by up to 0.02, τ is one to two thousand sweeps, and graphs made one round trip per replica or none in 18 000 rounds: treat those rows as approximate. The cold graphs are ordered with a few frozen-in defects.
- **What the curve looks like.** Smooth from 0.48 to 0.96, with no jump anywhere. It is steepest near g = 2.85, where τ peaks and the fluctuation measure χ rises to 0.18 and then falls by a factor of four within one step of the ladder. Something orders there at this size. Whether that is a continuous change or a weak abrupt one cannot be told from one size and no histograms; it says where T6 should look under the cap. It is nowhere near g of 5 to 6, where [T25] Fig. 3 has its jump to 0.99: at g = 5 equilibrium is 0.574, now from two independent methods.

### The density of states, and the sampler checked against answers known exactly (2026-09-21; task T6; `src/graphity/wang_landau.py`, `src/graphity/wl_ising.py`; NOT YET A PRODUCTION RUN)

The measurement VISION S2 needs is the entropy curve: for every energy, how many arrangements have it. A thermal chain cannot supply it, because it never visits the energies that matter. Wang-Landau [WL01] does, by raising the weight of wherever it has just been until it walks flat over the energy. The bins here are the pair (S, X) rather than the energy, so **one run covers every λ at once**, which is what S1's "publish the whole map" asks for.

- **Checked against the 4×4 Ising model**, where all 65 536 states are listed one by one and counted (`wl_ising.exact_dos`, no shared code with the sampler). Over 15 bins spanning a factor of 10⁴ in g, the worst error in ln g is **0.006 to 0.013** across three seeds.
- **Checked against our own exhaustive enumeration** at N = 16 and 18 (T4, Q9). Every bin found, none invented: worst error in ln g **0.016 at N = 16 and 0.014 at N = 18**. Canonical averages rebuilt from it agree with the exact ⟨φ⟩ to **0.0002** at g = 3, 6 and 20.
- **Plain Wang-Landau does not converge, and this is why the check mattered.** Ten times the work left the error where it was, at 20 to 30 % in g; the 1/t rule of [BP07] improves it but does not fix it. The cure is a second stage (`refine`): freeze the weights, count visits, add ln(visits). That is ordinary importance sampling with known weights, so it is unbiased by construction and its error falls like one over the square root of the time. It takes the Ising error from 20 % to under 1 %. **Stage one alone is never reported.**
- **The error bar from blocks within one run underestimates**, because the blocks are correlated; the spread between independent runs is the one to quote (`spread`).
- **Found on the way:** the re-seeding fault of Q14, which was invisible until there was a known answer to check against.
- **Not done:** any production run. T6 is pre-registered first, per rule 4. Nothing here interprets new physics; it is sampler validation, which is why it was built while the λ map is still unrun.

### Has anyone already tried to falsify "continuous"? Traced to its source (2026-09-20, at the author's asking)

[T25] supports its claim that the transition is continuous with two things: no hysteresis in its own Fig. 3, and

> "Of course, several other diagnostics for a second order transition have been tested [29], with positive results."

**Reference [29] is [KTB19]**, the 2019 paper we have read in full and whose Fig. 8a we reproduce. So the decisive evidence traces to one paper, and that paper states its own limits plainly:

> "Computational runtimes have prevented us from a more complete characterisation of the classical phase (via, for instance Hausdorff dimension calculations) or of the critical behaviour of the system. A finite size scaling analysis may well help to improve matters in this regard, though **at present even such an analysis is precluded**: an examination of figure 8 at the coupling values around criticality (as obtained from figure 9) indicate that **we are some way off the asymptotic regime**." ([KTB19] Sec. 5)

What [KTB19] does offer is a correlation length that shows a "divergent tendency" (its Fig. 9), which its own Sec. 4–5 calls a "reasonable indication" in D = 2.

- **So the decisive test has not been attempted by anyone, and the published record says so.** Finite-size scaling, which is what distinguishes a weak first-order transition from a continuous one, is named as out of reach in the only paper carrying the evidence, and the 2025 review cites that paper without repeating the caveat.
- **This is not a criticism of the reading, it is a statement of what is open.** Their reading may well be right. But "continuous" is an inference from one correlation-length plot at N ≈ 200, not a measurement that survived an attempt to kill it.
- **It is also exactly the gap task T6 fills**, and we are better placed than they were: parallel tempering reaches the cold couplings a single chain could not (T5), and the exhaustive enumeration at N ≤ 18 gives a density of states a Wang-Landau sampler must reproduce exactly, which is a validation nobody in the published work had. The barrier between two humps, and how it grows with N, is the measurement neither paper made.

### Why is the released energy always assumed to have somewhere to go? (2026-09-20, at the author's asking)

Every calculation in [T25] and [KTB19] weights an arrangement by exp(−H/g) at a fixed g. That is the canonical ensemble, and it carries an assumption that is rarely stated: the system is in contact with an unlimited reservoir at temperature g, which absorbs any energy released and supplies any energy needed. Nobody writes it down because for ordinary physics it is true — a sample in a laboratory really does sit in a room.

Three reasons it is the default, and one reason it matters here (*the first three are standard; the fourth is ours, unverified*):

1. It is far easier. The partition function factorises and free energies can be computed.
2. For most quantities and large systems the canonical and the fixed-total-energy (microcanonical) treatments agree, so the choice usually does not matter.
3. In cosmology the expansion of space supplies the cooling, so a falling temperature is a reasonable stand-in for it. Neither paper models expansion; the coupling is simply turned by hand.
4. **But the agreement in (2) is known to fail at exactly one place: a first-order transition.** At fixed total energy a system can sit in the coexistence region, where the two phases are both present and the released energy is visibly raising the temperature of what is left. The canonical ensemble cannot represent that state at all: it jumps across the coexistence region, and the latent heat appears only as a discontinuity, never as something the system does. So the standard choice of ensemble is blind in precisely the place VISION claims 4, 5 and 6 live.

This is why the sealed machinery of Q12 is not an optional extra. It is the setting in which the question can be asked at all, and it is genuinely absent from the published work in this model family.

### Which log is the axis of [T25] Fig. 3? Re-checked, and what it shows (2026-09-20, at the author's asking)

The whole "not reproduced" conclusion rests on reading the axis, labelled `log[g]`, as base 10, so it was checked again from the numbers rather than from the earlier note. Three independent ways, all agreeing:

1. **The label and the floor.** The axis runs from −1.0 to 2.25. Base 10 puts the hot end at g = 178, where the published S/N is 0.129; the random-phase value is 0.126 by the paper's own formula (O5). A natural log would put that end at g = 9.5, where our equilibrium value is 0.37 and the curve is nowhere near flat.
2. **Our own curve, on the hot side.** Read base 10, eleven consecutive published points from g = 6.3 to 178 sit on our equilibrium curve to between 0.001 and 0.039. Read as a natural log, no point anywhere agrees: the differences run from 0.15 to 0.61.
3. **Overall.** rms difference over the points inside our range: 0.186 base 10 against 0.393 natural. *(The 0.186 is dominated entirely by the window in the next paragraph; outside it the agreement is near-perfect.)*

**So the axis is base 10, and the earlier reading stands. But the disagreement is much narrower than "rms 0.30" suggested, and stating it properly matters.** Taking each published point against our equilibrium curve:

| log[g] | g | Published S/N | Ours | Difference |
|---|---|---|---|---|
| 2.25 down to 0.80 | 178 down to 6.3 | 0.129 rising to 0.481 | | **0.001 to 0.039, eleven points** |
| 0.78 | 6.03 | 0.728 | 0.532 | −0.196 |
| 0.77 | 5.88 | 0.887 | 0.543 | −0.344 |
| 0.76 | 5.73 | 0.844 | 0.555 | −0.289 |
| 0.75 | 5.59 | 0.970 | 0.566 | −0.404 |
| 0.70 | 5.06 | 0.992 | 0.613 | −0.379 |
| 0.60 | 3.95 | 0.997 | 0.736 | −0.261 |
| 0.31 | 2.02 | 0.970 | 1.011 | **+0.041** |
| below 0.31 | below 2 | 0.96 to 1.00 | (outside our range, but our curve has already reached 1.01) | |

- **The two curves agree at both ends and differ only in between.** Both start at the random-phase floor of about 0.13 and both reach about 1 at g ≈ 2. What differs is how they get there: the published points drop almost vertically at one coupling, log[g] between 0.75 and 0.80, while ours rises smoothly across the whole window from g = 6.3 down to 2. This is not a disagreement about which phases exist. It is a disagreement about the shape of the crossing, which is precisely the question this project asks.
- **[T25]'s own reading of its figure is that the transition is continuous**, on the ground that its two legs show no hysteresis (its text under Fig. 3). Ours show no hysteresis either. So the two of us agree on that much and differ on the steepness.
- **A candidate explanation, raised by the author, tested, and ruled out by the figure itself.** [T25]'s energy, Eq. (22), is written with triangles, squares and pentagons. It then argues the first and last away: "triangles and pentagons can survive only as isolated defects but are excluded for an homogenous ground state and we can henceforth neglect them", followed by "to make numerical simulations less computationally intensive one can use bipartite graphs". The author pointed out, rightly, that this is permissive rather than a statement about Fig. 3, and that the argument for dropping them is about the *ground state* while Fig. 3 is about the *transition*, where the paper's own words leave them alive as defects. Since triangles earn 9/8 against a square's 1, allowing them could plausibly have steepened the rise, which would have explained why we reproduce [KTB19] Fig. 8a and not this figure.
  **It does not survive contact with the hot end of the figure.** At infinite temperature, where the arrangement is whatever is most numerous, the number of squares per vertex is (`src/graphity/full_curvature.py`, scratch runs; general graphs melted by valid switches of the general edge switch, Q10):

  | N | (3⁴/4)/N, the value [T25] quotes | Bipartite (no triangles or pentagons) | General (both allowed) |
  |---|---|---|---|
  | 48 | 0.422 | 0.377 ± 0.002 | 0.194 ± 0.014 |
  | 64 | 0.316 | 0.288 ± 0.001 | 0.120 ± 0.023 |
  | 160 | 0.127 | 0.120 (our published-size run) | not measured; the trend above is away from bipartite, not towards it |

  Triangles and pentagons compete for the same edges under the hard-core rule, so allowing them roughly halves the square count, and the gap widens with N (the general value is 46 % of the quoted figure at N = 48 and 38 % at N = 64). **[T25]'s own measured hot dots sit at 0.129 at N = 160, within digitising error of the 0.126 it quotes, and our bipartite runs give 0.120.** A run with triangles and pentagons would sit at roughly half that. So Fig. 3's hot end is bipartite, and the disagreement between it and our curve is *not* explained by triangles. *Caveat: the general-graph melting is a slow scratch random walk whose ergodicity is unproven (Q10); the effect is a factor of two, far larger than any plausible error in it, but it has not been made a recorded run.*
- **So the disagreement remains unexplained**, and the question for the authors is the narrow one: between g = 2 and g = 6.3 their points drop almost vertically where ours rise smoothly, while we agree at both ends. What configuration space, run length and protocol produced that window?

### Parallel tempering at N = 160 with the full Hamiltonian (2026-09-20; `configs/cqg_n160_lam1_nocap_tempering.json`; EXPLORATORY, four replicas)

The same ladder and protocol as the capped run above, at λ = 1 without the cap: the model of [T25], in the range below g = 5 where a single chain freezes and where the two published figures disagree most. Graphs made 2 to 4 round trips per replica, against 0 to 1 under the cap, so this ladder circulates better.

| g | φ | spread between replicas | plain run | swap rate | τ (sweeps) |
|---|---|---|---|---|---|
| 6.31 | 0.5111 | 0.0002 | 0.5107 | 0.26 | 3 |
| 5.62 | 0.5633 | 0.0004 | 0.5629 | 0.23 | 5 |
| 5.01 | 0.6177 | 0.0003 | 0.6172 | 0.24 | 7 |
| 4.50 | 0.6707 | 0.0006 | | 0.28 | 11 |
| 4.10 | 0.7170 | 0.0007 | | 0.28 | 16 |
| 3.75 | 0.7607 | 0.0004 | | 0.31 | 24 |
| 3.45 | 0.8011 | 0.0009 | | 0.34 | 34 |
| 3.20 | 0.8369 | 0.0012 | | 0.40 | 44 |
| 3.00 | 0.8672 | 0.0002 | | 0.50 | 46 |
| 2.85 | 0.8906 | 0.0006 | | 0.45 | 64 |
| 2.70 | 0.9164 | 0.0019 | | 0.28 | 136 |
| 2.50 | 0.9511 | 0.0038 | | 0.16 | 335 |
| 2.25 | 0.9843 | 0.0050 | | 0.26 | 452 |
| 2.00 | 1.0134 | 0.0044 | (0.99, frozen) | | 1817 |

Figure: `docs/figures/equilibrium_curves.png`, which puts both tempering runs, the plain runs and both published figures on one axis.

- **Against the published figures, now in equilibrium.** [KTB19] Fig. 8a: our curve passes through its digitised points to 0.003 to 0.005 at g = 4, 5 and 6; at its coldest point, g = 2, we are 0.106 above it (1.013 against 0.907), which is where that paper's single quenches would be furthest from equilibrium. [T25] Fig. 3: still not reproduced, rms 0.297 over the seven digitised points in this range, worst 0.404. At g = 5 the published figure reads 0.99 and our equilibrium value is 0.618, now from two independent methods (plain chains agreeing between opposite starts, and tempering with round trips). See the axis section above for where exactly the two disagree: only between g = 2 and g = 6.3, and not at either end.
- **No jump anywhere.** The curve is smooth from 0.51 to 1.01 across the whole ladder, and τ rises steadily rather than exploding at one coupling. Unlike the capped model, there is no single place where the fluctuations spike: χ was flat within 15 % down to g = 2.5.
- **Trustworthy range.** Four independent replicas from random starts agree to 0.002 down to g = 2.7 and to 0.005 at g = 2.0, with 2 to 4 round trips each.

### Claim 5 as a prediction, and the prediction tested (2026-09-20; `configs/cqg_n64_lam125_tempering.json` and `configs/cqg_spark_wide_lam125.json`; EXPLORATORY, ten replicas)

Update 11 argued that claim 5 could be narrowed from "there is a leftover" to **the leftover is fixed by the energy released, with no freedom**, because a sealed run conserves its total energy exactly and the state it settles into is then not a free choice. That is testable in two steps, and both were run here.

**Step one, the right-hand side.** The equilibrium curve at λ = 1.25, N = 64, by parallel tempering, because a single chain freezes below g = 3 there. A first attempt with ordinary chains gave energies that jumped about between neighbouring couplings, which was the freezing showing itself in the data; the tempered run makes 6 to 9 round trips per replica and four replicas agree to 0.003 in φ.

**Step two, the prediction.** Sealed runs starting from a perfect tube with a fixed spark, so the total energy per vertex is 1 + spark/N and never changes. The predicted φ was read off the equilibrium curve and written into `configs/cqg_spark_wide_lam125.json` before the run.

| Spark | Total energy per vertex | φ predicted | φ measured | Difference |
|---|---|---|---|---|
| 12 | 1.1875 | 0.952 | 0.966 ± 0.008 | +0.014 |
| 24 | 1.3750 | 0.943 | 0.952 ± 0.003 | +0.008 |
| 48 | 1.7500 | 0.923 | 0.922 ± 0.003 | −0.001 |
| 96 | 2.5000 | 0.880 | 0.878 ± 0.008 | −0.002 |
| 160 | 3.5000 | 0.814 | 0.811 ± 0.006 | −0.003 |

- **The prediction holds across the range it was built to test.** φ falls by 0.14 from the smallest spark to the largest, and the three largest sparks land on the predicted curve to 0.003. Figure: `docs/figures/leftover_determined.png`.
- **This test replaced a weak one, and the weak one is worth recording.** The first comparison used sparks of 12, 13 and 16, whose predicted φ differ by only 0.003; it agreed, but it confirmed the level and could say nothing about the trend. Reporting that as a success would have overstated it.
- **The two smallest sparks sit 0.008 and 0.014 high**, which at spark 24 is three standard errors. The likeliest reason is incomplete settling: with little spare energy a sealed run explores slowly, and 25 000 sweeps may not be enough. That is a check to run, not a conclusion.
- **What it means for the claim.** Claim 5 is no longer only bookkeeping. In this model family, at this λ and size, the amount of leftover disorder is a determined function of the energy released and of nothing else. The step that is not tested is the one that matters for the hypothesis: whether a *real* transition releases a latent heat at all, which is task T6.
- **Limits:** one λ, one size, one starting arrangement, ten runs a point, and the identification of the leftover disorder with matter remains a reading rather than a measurement.

### The wall measured against temperature: a prediction with nothing fitted (2026-09-20; `configs/cqg_tube_arrhenius_lam125.json`; EXPLORATORY, sixteen replicas)

Counting exactly beforehand (Q13): the cheapest way out of a perfect tube costs 12, and the sampler offers exactly 3 such moves a sweep at every size, so the waiting time should be 1/(3 exp(−12/g)) sweeps with nothing fitted at all. Perfect tubes at λ = 1.25, sixteen runs at each of six couplings and two sizes.

| N | g | Mean wait | Predicted | Observed / predicted |
|---|---|---|---|---|
| 64 | 1.40 | 2553 ± 499 | 1760 | 1.45 ± 0.28 |
| 64 | 1.50 | 1611 ± 449 | 994 | 1.62 ± 0.45 |
| 64 | 1.60 | 620 ± 266 | 603 | 1.03 ± 0.44 |
| 64 | 1.75 | 302 ± 53 | 317 | 0.95 ± 0.17 |
| 64 | 2.00 | 125 ± 25 | 134 | 0.93 ± 0.19 |
| 64 | 2.50 | 30 ± 10 | 41 | 0.74 ± 0.25 |
| 144 | 1.40 | 1361 ± 341 | 1760 | 0.77 ± 0.19 |
| 144 | 1.50 | 878 ± 223 | 994 | 0.88 ± 0.22 |
| 144 | 1.60 | 457 ± 120 | 603 | 0.76 ± 0.20 |
| 144 | 1.75 | 266 ± 49 | 317 | 0.84 ± 0.16 |
| 144 | 2.00 | 151 ± 34 | 134 | 1.12 ± 0.25 |
| 144 | 2.50 | 29 ± 6 | 41 | 0.71 ± 0.14 |

- **The prediction holds.** Over twelve conditions, sixteen runs each, spanning waiting times from 29 to 2552 sweeps (a ninety-fold range) and two sizes, the plain mean of the ratios is 0.983 and the weighted mean is 0.884 ± 0.060; every single ratio lies between 0.71 and 1.62. Nothing was fitted: both the barrier and the prefactor were counted from the starting arrangement before the run. The weighted mean sits 1.9 standard errors below 1, which is worth watching rather than explaining away: it would be consistent with the tube occasionally leaving by a route a little cheaper than the one we counted, and a wider range of couplings would settle it.
- **What that settles.** The wall round the tube is the single local move, height 12, and the rate at which the sampler offers a way over it is the counted 3 a sweep. There is no collective barrier hiding behind the measurement.
- **The fitted barrier, for completeness.** A weighted straight-line fit of ln(wait) against 1/g gives 14.4 ± 1.0 at N = 64 and **12.07 ± 0.87 at N = 144**, the latter landing on the counted 12 exactly. The fit is poorly conditioned either way, because 1/g spans only 0.40 to 0.71, so the slope and the intercept trade off and neither is well determined alone; the intercepts come out at 0.09 and 0.27 chances a sweep against the counted 3, which is the trade-off showing itself rather than a real disagreement. The ratio test above uses both counted numbers together and does not have that weakness.
- **Limits:** one λ, one starting arrangement, tubes whose curled side is always 4, sixteen runs a point, and a range of 1/g too narrow to separate the barrier from the prefactor by fitting.

### The waiting time and size: a prediction of ours, twice misread, now resolved (2026-09-20; `configs/cqg_tube_waiting_lam125.json`; EXPLORATORY, twelve replicas)

**Read this section together with the Arrhenius section above, which supersedes its conclusion.** The story went wrong twice and is worth keeping in full as a record of how. First the criterion was size-dependent, which exaggerated the effect (corrected below). Then, with that fixed, the remaining flatness was still called a prediction "not supported" — but the prediction itself was malformed. A sweep is 2N attempts, and the sampler's proposals go as N² while the ways over the wall go as N, so the two cancel exactly: **a flat waiting time in sweeps is precisely what a local wall predicts** (Q13). The measurements were right throughout; the expectation set against them was wrong.

The config records a prediction written **before** the run: if the tube gives way by nucleation, one region going over a wall and the rest following, the typical waiting time should fall roughly like 1/N, because a larger tube offers more places to start. Perfect tubes at λ = 1.25, g = 1.5, four sizes, twelve replicas each, 30 000 sweeps.

**A mistake of ours, found and corrected the same day.** The first reading of these runs asked when the energy per vertex had moved by 0.3, which is an *absolute* energy of 0.3 N: at N = 64 one event of 12 units was nearly enough, at N = 192 five were needed. That biased the waiting time upwards for large systems, in exactly the direction of the conclusion, and it was reported before the flaw was noticed. Both readings are given below; the corrected one is the second.

| N | Mean wait, corrected criterion (the graph leaves the exact tube) | Median | What 1/N predicted | Off by | Mean wait, first (flawed) criterion |
|---|---|---|---|---|---|
| 64 | 835 ± 200 | 762 | (the reference) | | 1119 ± 187 |
| 96 | 1048 ± 340 | 688 | 557 | +1.4 σ | 1533 ± 393 |
| 144 | 752 ± 261 | 425 | 371 | +1.5 σ | 1127 ± 250 |
| 192 | 1165 ± 302 | 762 | 278 | +2.9 σ | 2200 ± 366 |

- **The prediction is still not supported, but much less strongly than first reported.** The corrected waiting times are flat with size where 1/N would have them fall threefold, and the largest size is 2.9 standard errors from the prediction, not 5.0. With twelve runs and waiting times that are spread exponentially, that is suggestive and not conclusive: it needs more replicas before anything is made of it.
- **The other half of the prediction holds.** The end state is the same at every size: 9 to 11 runs in 12 end as a *perfectly* flat sheet (energy exactly 0, φ exactly 1), and the average energy per vertex at the end is 0.01 to 0.12 against the tube's 1.00. So the energy given off per vertex is the exact 4(λ − 1) at every size tried, which is what the rehearsal was built to measure.
- **What it costs the picture.** VISION Update 8 calls this an existence demonstration of the *shape* of claim 4. It still is: something stable for now, a threshold, an abrupt change, a definite energy given off, a flat connected result. But "the tube gives way where a wall is crossed locally" was our guess about the mechanism, and the first test of it does not support it. The sealed measurement below says the wall itself *is* local and sharply 12 units at every size, so if both hold, what varies with size is not the wall but how often the system tries and fails. The two are not yet reconciled, and the honest position is that the mechanism is unknown.
- **Limits:** one coupling, one λ, twelve replicas, tubes whose curled side is always 4. Waiting times of this kind are usually spread exponentially, so twelve runs give about 30 % on each mean.

### Sealed runs: what becomes of the energy given off (2026-09-20; `configs/cqg_spark_threshold_lam125.json`; EXPLORATORY, eight replicas)

Figure: `docs/figures/sealed_story.png`, which puts this beside the waiting-time measurement above.

`src/graphity/sealed.py` (Q12). λ = 1.25, perfect tubes, nothing added and nothing removed (leak = 0), 12 000 to 20 000 sweeps. The demon starts with a fixed lump, the "spark", and there is no other source of energy.

`configs/cqg_spark_threshold_lam125.json` sweeps the spark against the size: eight sparks from 4 to 16, five sizes from N = 48 to 192, eight replicas each, 320 runs. The answer is the same at every size and perfectly sharp.

| Spark given to the whole system | 4 | 8 | 10 | 11 | 11.5 | 12 | 13 | 16 |
|---|---|---|---|---|---|---|---|---|
| Runs of 8 that converted, at **every** size (48, 64, 96, 144, 192) | 0 | 0 | 0 | 0 | 0 | 8 | 8 | 8 |

- **A sealed system with nothing to spare cannot start.** With an empty demon the tube sits for ever, although the state it would convert to is lower: acceptance is 0.4 %, so the graph does move, but only through switches that leave S and X alone, and it can never pay the wall. That is what the author's supercooled water says: the bottle needs the tap. It is now a permanent test (`test_a_sealed_tube_with_nothing_to_spare_cannot_convert`).
- **The wall is exactly 12, and it does not grow with the system.** Nothing below 12 ever started a conversion and nothing at 12 or above ever failed to, at any of the five sizes. Twelve is exactly the cheapest move out of the tube the energy allows: losing two squares and four surplus squares costs 32 − 20 = 12 at λ = 1.25. So the cost of *starting* is local and fixed while the energy given off, 1 per vertex, grows with the system. That is the condition for a runaway. *It points the opposite way from the waiting-time measurement above, and the two are not reconciled.*
- **Sealed, where it ends is fixed by what it was given.** The released energy has nowhere to go but back into the graph, so the end state sits on the line "total energy in", 1 + spark/N per vertex: 1.19 measured against 1.25 expected at N = 64 with a spark of 16, the difference being what the demon still holds. It never reaches the perfect flat sheet that the fixed-temperature runs reach. That is claim 5 measured: what came out of the change is warmer than what went in.
- **Sealed, the released energy manufactures exactly what [T25] Sec. VI.1 calls matter** (*ours, unverified*; recorded 2026-09-20 after the author asked why one would choose between claim 4 and his account). At N = 64 a converted tube ends at φ = 0.971, 0.957 and 0.945 for sparks of 12, 13 and 16, never at the perfect 1.000 that the same conversion reaches at fixed temperature. The shortfall, about two to four squares' worth, is random-phase disorder scattered through a geometric network, which is his definition of a matter particle. So the two accounts of where matter comes from may be one account seen from two ends: the latent heat is what makes the random regions. His is written at fixed coupling, where the energy leaves and only incomplete conversion can leave anything behind; a universe has no bath. What still separates them is what sets the *amount* (his: how fast it cooled; claim 4: the latent heat, fixed by the model) and the fact that leftover bubbles are compatible with either order of transition while a latent heat is not.
- **Not claimed:** none of this is a measurement of a latent heat in the thermodynamic sense, the identification of those defects with matter is a reading and not a measurement, nothing here says whether such a defect is stable, and the reconciliation with the waiting-time result is open.

### A curled-up dimension opening out into the flat sheet (2026-09-20; `configs/cqg_tube_uncurls_lam125.json`, `configs/cqg_tube_uncurls_lam150.json`; EXPLORATORY, four replicas)

Design brief, direction A: the mechanism of VISION claim 4 the right way round, inside the published family, with no new knob. Above λ = 1 the flat sheet is the lowest state and a tube (one side of the torus curled to length 4: one large dimension where the sheet has two) lies exactly 4(λ − 1) per vertex above it (`test_sheet_tube_cube_ladder`). Each run starts as a perfect tube, a 16 × 4 or 24 × 4 torus, at one coupling; no cap, Metropolis, 30 000 sweeps. "Perfectly flat" means energy exactly 0, φ exactly 1 and no surplus, which forces two squares on every edge. Figure: `docs/figures/tube_uncurls.png`.

| λ (tube above sheet) | N | g | Still a tube at the end | Reached the perfectly flat sheet (sweep) | Others, energy per vertex at the end |
|---|---|---|---|---|---|
| 1.25 (+1) | 64 | 1.0 | 2 of 4 | 1 (left the tube at 4100, flat at 23 200) | 1 on its way, +0.22 (left at 24 500) |
| | 64 | 1.5 | 0 | 4 (500 to 7900); one was +0.06 over the last 2000 sweeps | |
| | 64 | 2.0 | 0 | 4 (600 to 4300) | |
| | 96 | 1.0 | 2 of 4 | 1 (7750) | 1 on its way, +0.62 (left at 29 100) |
| | 96 | 1.5 | 0 | 3 (2250 to 5800) | 1 stuck with defects, +0.33 |
| | 96 | 2.0 | 0 | 2 (950; 15 650, as two flat pieces) | 2 stuck with defects, +0.42 and +0.95 |
| 1.5 (+2) | 64 | 1.0, 1.5, 2.0 | 0 of 12 | 1 of 12 | 11 stuck with defects, +0.44 to +0.88; all left the tube within 500 sweeps |
| | 96 | 1.0, 1.5, 2.0 | 0 of 12 | 1 of 12 (two flat pieces) | 11 stuck with defects, +0.31 to +1.06; all left within 500 sweeps |

- **At λ = 1.25 this is the wiring the hypothesis asks for, in miniature.** A specific arrangement with one large dimension, higher in energy than the space-like one, lasts for thousands of sweeps at low coupling (half the runs at g = 1 outlast 30 000), then gives way within a few hundred sweeps and ends as one connected, perfectly flat sheet with two large dimensions, having given off exactly the 1 per vertex known in advance. No new knob was needed: λ = 1.25 is inside the range VISION fixed.
- **At λ = 1.5 it is not.** The tube is gone within 500 sweeps at every coupling tried, so it is not stable for now, and the result is nearly always a sheet with frozen-in defects. That fits the exact census at N = 18, where the window with dips above the flat state closes between 1.55 and 1.6.
- **Caveats, as plainly as the result.** (1) Sixty-four or ninety-six vertices are not a space; "flat sheet" here is a small flat torus-like graph. (2) The tube is long-lived but it is *not* a strict dip: some single moves out of it cost nothing (exact check at N = 32), so requirement R2 of the brief is met in practice, not in the strict sense. (3) Fixed temperature: the energy given off is carried away, so nothing here speaks to claims 5 and 6. (4) Nothing here says how the system would come to be a tube in the first place; below λ = 1 tubes form from sheets (the rehearsal above), so a slow change of λ through 1 is one route, and it is a guess. (5) Four replicas, two sizes, couplings from a one-replica pilot, nothing pre-registered. (6) It is not a phase transition in the thermodynamic sense: nothing has been measured about how the waiting time or the energy per vertex behaves as N grows, and S2 is about exactly that.

### A flat sheet that is stable for now, giving way (2026-09-20; `configs/cqg_sheet_decay_lam050.json`, `configs/cqg_sheet_decay_lam025.json`; EXPLORATORY, four replicas)

Design brief, experiment 2. Below λ = 1 the flat sheet is a dip of the energy but not the lowest state (Q-ladder: tube −4(1 − λ) per vertex, 4-cubes −8(1 − λ); `test_sheet_tube_cube_ladder`, `test_which_arrangements_are_dips`). Each run starts as a perfect flat sheet at one coupling, no cap, Metropolis, 20 000 sweeps, energy per vertex recorded every 50 (`scripts/run_cqg_quench.py` with `"start": "torus"`). Figure: `docs/figures/sheet_decay.png`.

| λ (levels: tube, cubes; way out of the sheet) | N | g | Runs that left the sheet, and when (sweep) | Energy per vertex over the last 2000 sweeps |
|---|---|---|---|---|
| 0.5 (−2, −4; 8) | 64 | 2.5 | none of 4 (one brief excursion and back) | 0 |
| | 64 | 3.0 | 3 of 4: 5400, 11 700, 13 450 | −1.99 (one tube, one piece), −2.95, −3.36; the fourth still 0 |
| | 64 | 3.5 | 4 of 4: 650 to 5650 | −2.94 to −3.83 |
| | 64 | 4.0 | 4 of 4: 50 to 4300 | −2.35 to −3.72 |
| | 144 | 2.5 | none of 4 | 0 |
| | 144 | 3.0 | 1 of 4: 5300 | −3.30; the others 0 |
| | 144 | 3.5 | 4 of 4: 3050 to 6200 | −2.59 to −3.42 |
| | 144 | 4.0 | 4 of 4: 350 to 2200, **into the random phase** | +2.6 to +3.3 (energy taken up, not given off) |
| 0.25 (−3, −6; 4) | 64 | 2.5 | 1 of 4: 3250 | −3.00 exactly (φ = 1.250, X/N = 1.00, one piece: a tube) |
| | 64 | 3.0 | 3 of 4: 1600, 2000, 3500 | −3.75, −4.50, −5.04 |
| | 64 | 4.0 | 4 of 4: 350 to 750 | −3.71 to −5.95 |
| | 64 | 5.0 | 4 of 4: 50 to 150 | −4.78 to −5.83 |
| | 144 | 2.5 | 1 of 4: 6000 | −4.05; the others 0 |
| | 144 | 3.0 | 3 of 4: 1250, 7850, 15 300 | −3.66, −4.00, −4.56 |
| | 144 | 4.0 | 4 of 4: 800 to 1450 | −5.30 to −5.96, in 8 or 9 pieces (N/16 = 9), 76 to 97 % in baby universes |
| | 144 | 5.0 | 4 of 4: 100 to 250, **into the random phase** | +4.8 to +5.1 |

- **Stable for now, then abrupt.** At the colder couplings the sheet survives the whole run; at intermediate ones it sits at exactly zero for hundreds to fifteen thousand sweeps and then drops within a few hundred. Runs at the same coupling leave at very different times, which is what crossing a wall by chance looks like.
- **The first step is a dimension curling up.** Several runs stop at exactly the tube level, in one piece, with φ = 1.25 and one surplus square per vertex: one of the sheet's two large dimensions has looped in.
- **The plateaus are exact mixtures of the rungs.** −3.75 at N = 64, λ = 0.25 is one 4-cube and a 48-vertex tube, (16·(−6) + 48·(−3))/64; −4.50 is two cubes and a 32-vertex tube; −4.00 at N = 144 is 48 vertices in cubes and 96 in tubes. So the energy given off per converted vertex can be read off and checked against a number known in advance, which was the purpose of the rehearsal. The fullest conversion, λ = 0.25, N = 144, g = 4, gives off 5.92 to 5.96 per vertex against the exact 6.
- **What it gives way into depends on the coupling.** Cold enough, the knots; too warm, the random phase, and then energy is taken up.
- **What this is not.** It is the mechanism of VISION claim 4 running the wrong way round: space is the state that gives way, and what it gives way to is not a space. It is at fixed temperature, so the energy given off is carried away and cannot set anything off (the design brief's "what happens to the released energy"). No waiting-time statistics should be read from four runs.

### The chain against exact averages at N = 16 and N = 18 (2026-09-20; task T4; a test of the sampler, not a physics result)

Every state at these sizes is known with its energy (Q9), so ⟨S⟩ at any coupling is a finite sum. Sixteen independent chains of 8000 sweeps each, started from the 4-cube; "diff/err" is the difference from the exact value in units of the chain's own standard error.

| λ | g | Exact ⟨S⟩ | Metropolis | diff/err | Glauber | diff/err |
|---|---|---|---|---|---|---|
| 0 | ∞ | 20.8000 | 20.7983 ± 0.0028 | −0.6 | 20.7986 ± 0.0033 | −0.4 |
| 0 | 20 | 21.5564 | 21.5520 ± 0.0071 | −0.6 | 21.5483 ± 0.0070 | −1.2 |
| 0 | 12.5 | 22.3412 | 22.3348 ± 0.0075 | −0.9 | 22.3291 ± 0.0094 | −1.3 |
| 0 | 8.33 | 23.3634 | 23.3714 ± 0.0100 | +0.8 | 23.3704 ± 0.0070 | +1.0 |
| 0.5 | 16.7 | 21.1819 | 21.1878 ± 0.0043 | +1.4 | 21.1872 ± 0.0056 | +1.0 |
| 0.5 | 6.67 | 22.1968 | 22.1887 ± 0.0084 | −1.0 | 22.2052 ± 0.0099 | +0.8 |
| 1 | any | 20.8000 | 20.7928 ± 0.0031 | −2.3 | 20.7986 ± 0.0033 | −0.4 |

- At N = 16 and λ = 1 every state has H = 0 (every edge carries at least two squares), so the answer is pure counting and does not depend on g. That is why the permanent test goes on to N = 18, where the full energy differs from state to state (`test_chain_matches_the_exact_average_at_eighteen_vertices`).
- The table above was produced by a scratch script and is not reproducible from the repository as it stands; the permanent versions are the tests, which use 12 chains of 4000 sweeps and demand agreement within five standard errors. One entry in fourteen at −2.3 is what chance gives.

### Quenches at λ = 0 and λ = 1 against [KTB19] Figs. 6 and 7 (2026-09-20; EXPLORATORY, four replicas, not a gate)

`configs/cqg_quench_lam0_vs_ktb19fig6.json` and `configs/cqg_quench_lam1_vs_ktb19fig7.json`, run by the new `scripts/run_cqg_quench.py`: melt, then zero temperature (a switch is accepted only if it does not raise H), 1000 sweeps, at the six published sizes N = 100 to 200. [KTB19] shows one run per size and defines neither its sweep nor the temperature of its quench, so shapes and heights can be compared, not the clock. The published values below were read off the figures by eye, not digitised. φ is the mean of our four replicas.

| | Published | Ours |
|---|---|---|
| λ = 0, does φ pass 1? | Yes, within a few hundred sweeps (Fig. 6) | Yes, in all 24 runs, at sweep 80 to 190; later for larger N, as published |
| λ = 0, φ at sweep 1000 | 1.17 to 1.36 | 1.37 to 1.42 (single runs 1.29 to 1.47); at our sweep 500, 1.28 to 1.38 |
| λ = 0, what the graph becomes | Breaks into baby universes (Fig. 5: four 16-vertex pieces and one larger, unfinished) | On average 5.5 to 10 pieces (single runs 4 to 12); 52 to 73 % of vertices in finished baby universes, the rest in one or two larger unfinished pieces |
| λ = 1, is φ held near 1? | Yes: "an (approximate) upper barrier", with "minor breaches" (Fig. 7); about 0.93 to 1.02 at sweep 1000, 0.97 to 1.04 by sweep 10 000 | Yes: 0.95 to 1.02 at sweep 1000 (single runs 0.92 to 1.07); 7 of 24 runs pass 1 at some point, and the highest value recorded in any run is 1.10 |
| λ = 1, connected? | Not stated | One piece in 22 of 24 runs, two in the others; no baby universes |

- **Reading.** Both published behaviours are reproduced in kind: the global term alone drives the graph past the torus value and shatters it, and the local term stops it at the torus value and keeps it connected. Ours runs roughly twice as fast per sweep as the published curves, which would fit a published sweep of N attempted switches against our 2N, but that is a guess.
- **The 14-vertex baby universe appears by itself, often.** At sweep 1000 the 24 quenches at λ = 0 hold 123 finished 4-cubes and 20 other baby universes, and in every run the vertices in baby universes that are not 4-cubes number 0, 14 or 28 (from `baby_frac` and `cube_frac` in the result file). For the eight runs at N = 100 and N = 160 the final graphs were rebuilt from the config's seeds in a scratch script and every piece was put through a networkx isomorphism test: 32 4-cubes, 6 biplane graphs, 9 unfinished pieces, nothing else. That script is not in the repository; the counts from the result file are. So the published description of the λ = 0 cold phase as hypercubic is incomplete, at least for this sampler: about one finished piece in seven is the biplane graph of Q8. *Ours, unverified; exploratory.*
- **What this does not show.** A quench is not equilibrium, and none of this bears on the order of the transition. It checks the model reading and the sampler against two more published figures, at λ = 0 for the first time.

### λ = 0, cooling and heating at N = 64, 96, 160 (2026-09-20, `configs/cqg_lam0_first_look.json`; EXPLORATORY, four replicas, not a gate run)

Global term only, no cap, Metropolis. Each replica is melted, cooled through 18 couplings from g = 100 to g = 3, then heated back from whatever the cold end froze into; 2000 + 4000 sweeps per coupling. Sizes are multiples of 16 so that a perfect tiling by 4-cubes exists. φ = 1.5 on perfect baby universes.

| N | Cooling: φ jumps between | Heating: φ falls back between | Largest heat − cool (replica mean) | Cold end, g = 3: φ; pieces (N/16); `baby_frac`; `cube_frac` |
|---|---|---|---|---|
| 64 | g = 6.5 (0.81) and 6.0 (1.46) | g = 7.5 and 9 | 0.66 at g = 6.5 | 1.48; 4.0 (4); 0.93; 0.87 |
| 96 | g = 6.0 (0.74) and 5.0 (1.48) | g = 7.0 and 8 | 0.82 at g = 7.0 | 1.49; 6.0 (6); 0.95; 0.87 |
| 160 | g = 5.5 (0.64) and 4.5 (1.45) | g = 5.5 and 7.5 | 0.82 at g = 5.5 | 1.46; 9.2 (10); 0.84; 0.75 |

- **Two states, nothing in between.** Inside the loop every replica sits in one of two well-separated states at the same coupling. N = 160, heating, g = 6.0: three replicas at 1.45 to 1.49 and one at 0.62, while all four cooling replicas are at 0.58. N = 96, cooling, g = 5.5: one at 0.80, three at 1.44 to 1.50. The only intermediate averages come from runs that switch during the measurement (`phi_sd` of 0.2 to 0.3 against 0.01 to 0.06 otherwise). The gap is about 0.85 in φ, which is about 13.6 in H per vertex.
- **On the hot side the two legs agree**: for g ≥ 9 the largest difference in any replica is 0.005, with τ of 1 to 3 sweeps. So the disagreement is confined to the loop; it is not a general failure to equilibrate.
- **The cold phase is shattered and made of baby universes**, mostly 4-cubes; at N = 160 about 14 vertices per replica are in baby universes that are not 4-cubes, which is one 14-vertex piece of Q8. It is not a space: VISION S4 fails here, as published.
- **This is what [T25] and [GV21] report for the global term alone** (first order, hysteresis, isolated hypercubic complexes), now seen with our own kernel, and it is the opposite of what the same kernel does at λ = 1 and under the cap, where the two legs agree to 0.003 and the graph stays in one piece.
- **Not claimed.** Hysteresis in a sweep of finite length shows two long-lived states, which is what a first-order transition produces, but it is not by itself proof of one. The loop's position moves to lower g with N (the cooling jump from about 6.2 to about 5.0) while its width stays near 2, and we have not yet asked why. The proof VISION S2 asks for is a two-humped histogram whose valley deepens with N, or a dent in s(φ) (T6). Inside the loop τ reaches 300 sweeps and the error bars there mean nothing (Q6). Four replicas, one run length, couplings chosen by eye.
- **For the owner:** Gate A reads "at λ = 0, several sizes, cooling and heating: hysteresis around the transition, and a cold phase dominated by Q4 components". This run shows both at three sizes. Whether an exploratory run may pass a reproduction gate, and whether "Q4 components" should read "baby universes", are her decisions (see the note under Gate A in `TASKS.md`).

## Open issues

- **O1 Trapping.** At N = 36, β = 0.2, runs from random starts reached −7 to −9 per node; a slow anneal reached −10.1 to −11.2; none found −12.2, and none went below it. [K08] Sec. IV reports the same ruggedness and mentions simulated tempering. Plan: add parallel tempering and the second move type before any production run.
- **O2 Ergodicity inside a menu.** Not established for our single move. Must be tested (e.g. by exhaustive enumeration on tiny menus) before Phase B results mean anything.
- **O3 Small sizes.** ln N changes little between N = 60 and 240; [K08] itself says its range cannot establish logarithmic scaling. Bounded menus make larger N affordable.
- **O4 What none of this touches.** Monte Carlo steps are not physical time and the model is Euclidean ([CP12] Sec. VI). Nothing here tests Lorentz invariance, 3+1 dimensions, inflation or dark matter.
- **O5 The hot floor sits below the published value, and the hard-core rule is why.** (2026-09-19, exploratory.) At truly infinite temperature (1/g = 0) on the 16×10 torus the code gives 19.15 ± 0.03 squares, φ = 0.1197, against the Poisson 20.25 (φ = 0.1266) and the published floor 0.126. That is 5 % low: far outside the statistical error, yet inside Gate B's tolerance of ±0.01. To find the cause the graph was melted under three sets of rules (5 seeds each, 400 + 3000 sweeps):

  | Rules in force | Squares at N = 160 | Squares at N = 900 |
  |---|---|---|
  | cap of 2 squares per edge + hard core (the code as it is) | 19.15 ± 0.03 | 20.10 ± 0.04 |
  | hard core only (the published space, as we read it) | 19.23 ± 0.05 | 20.03 ± 0.04 |
  | neither (plain random 4-regular bipartite graphs) | 20.62 ± 0.02 | 20.29 ± 0.04 |

  So the hard-core rule (Q2) removes the squares; the cap makes no measurable difference; and the deficit is a finite-size effect that fades as N grows. Consequences:
  - The first look's floor comparison was made at g = 200, where the Boltzmann factor e^(16/200) ≈ 1.08 raises the square count while the hard-core rule lowers it. The two partly cancel, by an amount that changes with N. The agreement with 20.25/N was therefore weaker evidence than it looked.
  - The floor **cannot** tell the capped variant from the published model (rows 1 and 2 agree). It **can** test our reading of the hard-core rule, but only if the published 0.126 is a measured value. It may simply be the theory value 20.25/160 = 0.1266, quoted.
  - **Human step for Emily:** find out in [T25] how the 0.126 was obtained. If it was measured, our reading of Q2 gives a floor 5 % too low and has to be re-examined before T2. Either way Gate B's tolerance on the floor could shrink from ±0.01 to about ±0.002; the statistics allow it easily.
  - **Caveat on reproducibility:** rows 2 and 3 were run by editing the constants `CAP` and `MAX_CODEGREE` in a scratch copy of `cqg.py`, so those four numbers cannot yet be regenerated from a config in this repository. Redo them from a config once T2 makes the cap optional. Row 1 at N = 160 is reproduced by `test_chain_runs_on_a_rectangle_and_melts_to_the_published_floor`.
  - All of this is "Ours, unverified".
  - **Resolved 2026-09-19 from the source.** [T25], "Cycle condensation": the density of squares "increases from (3⁴/4)/160 = 0.126 (for N = 160 in the example below) in the random phase". So 0.126 is the theory formula, not a measurement, and there is no conflict with published data. The hard-core reading is confirmed separately (Q2). The measured points of [T25] Fig. 3 sit at 0.129 at both g = 178 and g = 100 (`docs/published/T25_fig3_digitised.csv`). The suggestion to tighten Gate B's floor tolerance is withdrawn: the published number it would be compared with is a large-N formula that a correct finite-N simulation should miss by about 5 %.

## Provenance

Code and documents were drafted with Claude (Anthropic) in conversation with the
author and should be disclosed as such in any submission. Physics estimates marked
"Ours" originated in that conversation and have not been reviewed by a physicist.

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
| Q3 | ~~No edge may carry more than 2 squares (hard cap).~~ **Superseded.** [T25] Sec. "Cycle condensation" describes the published model as using the *full* Hamiltonian, Eq. (22): the global term plus a **soft local term that penalises** edges with more than 2D−2 squares, with no hard cap. It states that the two effects "cancel exactly" so that denser configurations are "degenerate" with the torus, which confirms our Q1 coefficient and our 4-cube tie. It also states: global term only → **first-order** transition into isolated hypercubic complexes ([KTB19], [GV21]); full Hamiltonian → **continuous** transition. | [T25]; our first-look code | **Our first look simulated a third variant (global term + hard cap), which is neither of the two published cases.** Its results do not yet test the published claims. To do: implement the local term, remove the cap, rerun. **Corrected 2026-09-19, after reading [KTB19] Sec. 3.3 and Sec. 4 directly: the capped variant IS a published case.** [KTB19] defines P_ω as the set of edges with more than d − 2 squares (plus triangles), i.e. more than 2 for us, and states that its simulations (Figs. 8 and 9, the evidence offered for a continuous transition) ran "the mean field action" on the space with P_ω = ∅, where "both the exact action and the mean field action agree". That is this code: cap of 2, H = 16(N − S). Our first reading of [KTB19] was right; this row's "superseded" went too far. So there are three published cases, not two, and they lie on one line (*Ours*): H = 16(N − S) + 4λ Σ_e (S_e − 2)₊ with λ = 0 (first order, hypercubes), λ = 1 (full Ollivier curvature, [T25]) and λ → ∞ (the cap, [KTB19] Sec. 4). [KTB19] did not simulate the annealed transition at λ = 1; it says only that this "seems likely" to be "in the same universality class". T2 is still needed for λ = 0 and λ = 1. **Addendum 2026-09-22, from the author's reply (paraphrased in `docs/outreach/correspondence_2026-09-22_trugenberger.md`): he has no such restriction in his code; only the hard-core rule is ever imposed. So the capped kernel is our reading of Sec. 4, disputed by the author, and not a published case. The λ → ∞ end of the knob stays in the code and on the record as ours.** |
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
| Q15 | **CORRECTION, 2026-09-21, by the owner, before any run: quotienting by isomorphism is STANDARD practice in neighbouring approaches and is not a new idea.** Causal dynamical triangulations sums over *inequivalent* triangulations weighted by 1/|Aut(T)|, and states the reason as principled rather than technical: a path integral over geometries should carry no relabelling redundancy, because relabelling is not a physical change. Causal set theory treats labels as surplus structure in the same way. Any claim that this is unexplored is false and is withdrawn. **What may survive is narrower and is the owner's formulation:** those approaches quotient labels out of an ensemble that already assumes a great deal of geometric structure (simplices glued into causal spacetimes; orderings already causal), whereas the proposal here is to use interchangeable-constituent counting as the central thermodynamic quantity in a comparison *between* a pre-geometric relational organisation and a spacetime-like one, with neither side assumed to be a geometry. Those are different operations. **Before any novelty is claimed**, search group field theory, tensor models, causal sets and graphity for isomorphism-class microstate entropy compared across a geometric phase transition (task T12). **A point of precision that sharpens the concern and was worth checking:** the number of named versions of a shape is (n!)^2/A. The (n!)^2 is the same for every shape at a given size, so it cancels from every ratio, average and difference and inflates nothing -- the factorial does *not* swamp the measurement. What does not cancel is the division by A, and A varies by e^62 between a shattered state and a sheet at N = 160 (measured below). So named counting underweights symmetric arrangements by exactly their symmetry, which is a real, finite and computable effect rather than an artefact. | **Named points against interchangeable ones**, and how much of an arrangement is genuinely interchangeable. Named counting (what every run here and, as far as we know, every published CQG run does) weights a shape by its number of distinct named versions, (n!)^2/A; interchangeable counting weights every shape once. So the second favours a shape by **exactly A**, the number of renamings that leave every relationship intact and keep each point on its own side. `small_graphs.log_automorphisms` computes ln A piece by piece, because the group factorises over connected pieces and the arrangements whose groups are too large to list are exactly the ones that come apart. | The two ensembles, and the sampling rule that realises the second (Metropolis ratio x |Aut(G')|/|Aut(G)|): [DQM25] Eq. (72), read in full by the owner. The reading that a point is distinguishable only to the extent that its relationships distinguish it, and therefore that A *derives* rather than assumes which points are interchangeable: ours. | Ours, tested and measured. **Tested:** `log_automorphisms` returns 192 for the 4-cube, which is the side-preserving half of its known group of order 2^4 x 4! = 384 and independently the value `results/ergodicity_small.csv` records for that class; 320 for the 16x10 torus (160 translations x 2 reflections); the exact factorisation A^k k! for k copies of one shape; and 1 for a melted graph. **Measured at N = 160** (`scripts/measure_symmetry_cost.py`): ten separate 4-cubes are favoured by e^67.7 = 10^29.4 and take 0.11 s to count; a perfect sheet by 320, 11.7 s; a melted graph by exactly 1, 24.3 s. The ordering of the costs is the opposite of the obvious guess: the shattered state is cheapest because it factorises, and the melted one is dearest because the work goes into proving there is no symmetry, for an answer that is always 1. **Consequence for the plan:** a correction at every move is unaffordable at any of those speeds (a run makes about 10^8 moves), so it is applied to measured configurations or per energy level, and that approximation is checked against the exact small-size answer. **Exact at small size** (`scripts/labelled_vs_unlabelled.py`, arithmetic on a committed result): at N = 16 the 4-cube's share rises from 1.3 % to 20 % at lambda = 1 where every class is degenerate, and at lambda = 0, g = 20 from 0.13 to 0.73 with phi moving 1.347 to 1.454, towards the shattered 1.5; at N = 18, where no 4-cube fits, the shift is smaller and at lambda = 1 runs the other way. **Limits:** N <= 18 is one piece and cannot shatter, so this is the mechanism and not its consequence; and it is a statement about which arrangements an ensemble favours, not about the order of a transition, which is what T10 is actually for. *Ours, unverified:* at lambda > 1 and cold, the energy gap between a shattered state and a sheet (320 units at N = 160) suppresses the shattered one by about 10^-70 against a symmetry gain of 10^29.4, so this does not overturn which arrangement is lowest; at warmer couplings the two become comparable, which is a calculation rather than a worry. |
| Q16 | **Connected runs use the simplest possible move: the ordinary switch, with any proposal that would break the graph into pieces refused.** No new move, no new algorithm. `one_switch_away(..., connected=True)` and `explore(..., connected=True)` in `small_graphs.py`; the production flag is still to be added to the kernel. | **Detailed balance is automatic** and is not an assumption: restricting a symmetric proposal to a subset of states leaves it symmetric. **Irreducibility is the assumption.** [Taylor81] proves it for a space constrained only by degree -- any connected graph reaches any other by switches with every intermediate graph connected -- and that is quoted from sources citing it rather than from the original. | **Ours, and NOT established on our space. Read this before interpreting any connected run.** [Swap17] reports that adding a constraint can destroy exactly the swap-connectivity Taylor guarantees, and our space adds the hard-core rule on top of degree, so the guarantee is not inherited. **We tried to check it exhaustively and the check is vacuous** (`scripts/check_connected_ergodicity.py`, 2026-09-21). The restricted walk does reach every connected class at N = 16 and 18, with and without the cap -- but the restriction **refused zero moves** at both sizes, so the walk it performed was the unrestricted one and the result says nothing. The reason is arithmetic: the smallest valid piece has 14 vertices (Q8), so two pieces need at least 28, and every valid state at 16 or 18 vertices is connected whether or not you ask. Exhaustive enumeration cannot reach 28 (N = 20 did not finish in about 40 minutes, Q9), so **this property cannot be established exhaustively with the machinery we have.** **What must therefore be reported with every connected run:** the share of proposals refused for disconnection. Where it is small the restriction barely bites and the chain is effectively the unrestricted one, whose ergodicity T4 did establish at small size; where it is large -- the shattered phase at λ = 0 is the case to worry about -- the restriction is doing real work and any result carries this caveat. A cheaper partial check that has not been done: start the restricted chain from two very different connected states at a simulable size and see whether each reaches the other's neighbourhood. That is evidence, not proof. |
| Q17 | **The flat-histogram approach to T6 does not work on this model at production size, and the reason is structural rather than a tuning problem.** Diagnosed 2026-09-21 at N = 36, the smallest pre-registered size, before any result was taken from it. | Ours, measured. | Ours, measured, and the numbers are the point. **What was seen.** Starting from a perfect flat torus with the whole (S, X) range as the window: 4015 cells of which 737 reachable, 2x10^7 moves, and **zero round trips** -- the walk never crossed its own window once. Consequences, in order: (a) the flatness criterion was never met, because new bins were still being discovered at round 358 of 556 and every late bin drags the histogram minimum down; (b) so ln f never left its starting value of 1.0 through the entire run; (c) so the accumulated weights ran to a spread of **24 796** where the true spread of ln g at this size is of order 90; (d) so the frozen-weight second stage could not move at all, visiting **one bin** out of 737. Two repairs were made and are kept because they are right in themselves -- the histogram now restarts whenever a new bin appears, and ln f is halved after a bounded number of rounds whether or not the histogram is flat -- and together they got ln f down to 2x10^-3 and the second stage up from 1 bin to 24. **Still useless, and still zero round trips.** A window restricted to S in 20..40, X in 0..24 did produce 30 round trips, which shows the diffusion distance is the obstacle rather than the kernel; but the transition needs a window spanning the disordered and the ordered side, which is exactly the wide window that cannot be crossed. **The kernel is not at fault** and was checked separately: an ordinary chain on the same graph at infinite temperature accepts 45 % of moves and visits 63 distinct (S, X) in 2000 sweeps. **Conclusion:** flat-histogram sampling over a two-dimensional bin space is the wrong instrument here. Measuring one energy ladder at a time, or splicing overlapping windows, would each address it; but [RdF15], which asks precisely our question in a neighbouring model, answers it with **parallel tempering**, which this project already has and has validated against exact averages (Q11). T6 is redirected accordingly; see TASKS. The Wang-Landau code, its Ising and exact-enumeration validations (Q14, section D) and the two repairs above are kept: they are correct, they are tested, and nothing about them is withdrawn except the claim that this is the right tool for this measurement. |
| Q18 | **Zero is the floor of the published energy, and allowing braces does not change that.** A chain over graphs that need not be two-sided (`src/graphity/general_chain.py`), so that the static reference of Q10 can be asked what a *run* does. Same energy, same validity rule, the general edge switch of Q10, energy recomputed exactly at every attempted move; a sweep is 2N attempts as elsewhere. | The energy and the validity rule: [T25] Eqs. (8), (21), Def. 2, Fig. 1, as Q10 records. The chain, the floor argument and everything below: ours. | **Ours, tested** (`tests/test_general_chain.py`), and it answers the question the author asked on 2026-09-22: if refolding space is free, does space refold? **(1) Two exclusions that come from the hard-core rule and not from the prices.** A triangle and a square sharing an edge leave a pentagon that shares two edges with each, and two triangles on one edge leave a square that does the same; both are refused. The cuboctahedron, the obvious candidate for an arrangement below the sheet, is invalid for exactly this reason. **(2) So a valid edge carries T = 0, or T = 1 with S = 0, and over every such loading the curvature is at most zero. H is therefore never negative: the flat sheet is not metastable, and nothing in this model family sits below space.** Equality needs every edge to carry either two squares (a sheet) or one triangle and a pentagon (a closed braced piece). **(3) The H = 0 family has at least three members**: the flat sheet (a dip, wall 16); the 30-point icosidodecahedron (a dip, wall 20); and the 15-point L(Petersen), ten triangles and twelve pentagons, which is **frozen** -- not one valid switch exists out of it. **(4) Braces without pentagons are expensive**: the line graphs of the girth-6 cubic graphs (Heawood, Moebius-Kantor, Pappus, Desargues) all sit at exactly +4 per vertex and none is a dip, as the kagome sheet does. **(5) A sheet that wraps in an odd number of steps carries free pentagons** -- once an edge has two squares both brackets are saturated, so further loops on it cost nothing -- **and they halve its wall, 8 against 16.** **What this means for the author's picture** (*ours, unverified*): dark energy as space holding a little extra above something lower needs an arrangement below space, and there is none here, with or without braces. Refolding is free but never downhill, so what decides between space and a knot at a given temperature is entropy, not energy. **Limit, stated plainly:** the chain has no exactly known distribution to check against, because the hard-core rule leaves no valid graph below 14 points (Q8) and enumeration cannot reach the sizes that do exist (Q9), so its runs are read qualitatively -- does it refold, does it survive -- and not as equilibrium averages; irreducibility is unproven for this move set (Q10). |
| Q19 | **The correlation length of [KTB19] Fig. 9, read as written, with three choices the paper leaves open.** `src/graphity/correlation.py`. Per edge phi_sq = S_e / (d - 2); per vertex f(u) the average of phi_sq over its d edges; C(r) the average of (f(u) - phi)(f(v) - phi) over pairs at graph distance r, divided by the variance of the *edge* field; xi = -< r / log C(r) >, divided by the diameter. **Choices (ours):** (1) the outer average is over the distances r = 1 .. diameter with 0 < C(r) < 1, each counted once; other distances are skipped and counted; (2) a graph with no edge fluctuation (a perfect lattice) is skipped and counted; (3) pairs in different pieces are ignored. Both averages are over one graph, then over snapshots. | [KTB19] Sec. 4, the two displayed equations after Fig. 8 and the text of Fig. 9 (arXiv HTML searched directly, 2026-09-23). Whether Fig. 9's axis is natural log like Fig. 8a: to verify. | **Calibrated against a brute-force networkx computation** (`tests/test_correlation.py`); the choices are **Ours**. Caution from the group's own first author (Kelly's thesis, REFERENCES [Kelly22] note): interactions here are not short range and random graphs have diameters growing only as log N, so "correlation lengths are not well defined" is a real possibility. At our sizes the diameter runs from about 5 (N = 36, random phase) to 26 (N = 676, lattice), so xi / diameter is read from a handful of distances. |
| Q20 | **The fast symmetry count, and a chain with interchangeable points.** `src/graphity/symmetry.py` counts side-preserving automorphisms with igraph's `count_automorphisms` (bliss; from general knowledge, not read by us) in about a millisecond at N = 64 to 676, against 1 to 45 s for Q15's counter; the two agree exactly on perfect tori (4x4 = 192, 16x4 = 128, 12x12 = 576, 16x10 = 320) and on melted graphs (`tests/test_symmetry.py`). `src/graphity/interchangeable.py` uses it inside a chain: the kernel's own move, accepted with min(1, exp(-dH/g) A(G')/A(G)) as in Betre and Lewis Eq. (72) [DQM25], or, sealed, with the demon paying dH and the factor A(G')/A(G) alone. | The acceptance factor: [DQM25] Eq. (72), read in full by the owner. The rest: ours. | **Calibrated** against the exact interchangeable averages at N = 18 (`tests/test_interchangeable.py`): <S> = 19.59 +- 0.08 against 19.53 exact at lambda = 1, g = 10 (named: 20.01); 21.26 +- 0.05 against 21.29 at lambda = 0, g = 10 (named: 20.96); 18.99 +- 0.31 against 19.53 at the colder g = 4 (slower mixing). Energy conserved exactly in the sealed version. Cost: every valid proposal is counted, so it is meant for N up to about 64. **Consequence:** the per-move correction Q15 called unaffordable is affordable at small N; the sealed-sheet refold test (series paper 4) and quantum rung 1 (T15) can now be run with interchangeable points. |

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

### The ribbon: another group's prediction about our own cold phase, tested (2026-09-21; `configs/cqg_lam0_ribbon.json`; EXPLORATORY, four replicas, three sizes)

[GV21] reports that the cold phase at the penalty-off setting is about N/16 knots **plus one closed bipartite "ribbon"** holding the leftover points. Our earlier λ = 0 runs could not test it: their sizes (64, 96, 160) are all multiples of 16, so the graph shatters into a whole number of 4-cubes with no remainder and `baby_frac` reaches 1.000. The sizes here — N = 36, 100, 120 — are deliberately not multiples of 16. The two pictures are far apart and the existing columns separate them: if the leftover is one piece it IS the largest piece, so `largest_frac` = 1 − `baby_frac` and `pieces` ≈ `baby_frac`·N/16 + 1; if it scatters, `largest_frac` sits near 16/N.

- **It is there.** Of the shattered-phase rows, 11 match the one-ribbon prediction, 2 the scattered one and 4 neither.
- **N = 36:** `pieces` = 2.00 in every measured sweep, `baby_frac` = 0.444 (one 16-point knot) and `largest_frac` = 0.5556, which is 20/36 exactly. One knot plus one 20-point piece.
- **N = 100:** `pieces` = 6.00 in every measured sweep, `baby_frac` = 0.785, `largest_frac` = 0.215 = 1 − 0.785 to four figures. Five knots plus one piece holding the rest.
- **N = 120:** `pieces` ≈ 7.25, and the equality holds to about 0.03 over the middle of the shattered range.
- **The rows where shattering is incomplete behave the same way**, which is the more interesting half: in the partly-converted state at N = 36 and 100 the unconverted remainder is also a single connected piece. That is the object T11 is about, arriving from a different direction.
- **Limits:** the columns are averages over measurement sweeps, so a row is a blur over whatever the run visited; `pieces` = 6.00 exactly means it was 6 in every measured sweep, which is strong, but confirming the ribbon's *topology* (closed, bipartite) needs a snapshot and has not been done. Four replicas, one coupling ladder, not pre-registered.

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

- **O6 The analysis could manufacture a barrier out of nothing, and did.** (2026-09-21.) `scripts/analyse_t6_hist.py` decides where the transition is, how far apart the two humps are and how deep the valley between them is; all three feed the pre-registered verdict, and none had been tested against a case with a known answer. Built such cases (`tests/test_t6_analysis.py`) and found three faults — the first two mine, the third the one that mattered:
  - The `MIN_LEVELS_APART` guard did not do the job its comment claimed. It rejects humps closer than four bins, but a histogram that alternates up-down from one bin to the next has peaks at *every even* spacing, four included, so a 4 % wobble on a single hump was reported as a latent heat of 0.16. Replaced with a binomial [1,2,1]/4 smoothing, which annihilates a one-bin alternation exactly. Peaks, valley and depth are now measured on the smoothed curve, which can shrink a real barrier but cannot invent one.
  - **An empty bin was being read as a deep bin.** `reweight` floors zero counts at 1e-300, so an energy the run never visited became a valley of depth ln(1e300) ≈ 690. On one hump plus counting noise this invented a barrier in **6 of 25** histograms, each reporting a "barrier" of about 690 — not a measurement of anything, only the logarithm of the clamp. The analysis is now restricted to the longest unbroken stretch of energies actually visited. That is also the physically right rule: to measure the cost of crossing a valley the run has to have crossed it, and a valley too deep to cross shows up as no round trips, which is already a gate.
  - Reweighting was allowed to run far enough that a handful of sweeps in the sparse tail could carry the whole answer. Now limited by effective sample size rather than by a fixed shift in g, because whether a given shift is safe depends on how wide the histogram is.

  After the repairs, on 1800 synthetic histograms that were one hump plus counting noise, across three sample sizes and three widths: **0 invented barriers**. On genuinely two-humped histograms it recovers the latent heat to better than 1 % and the barrier to about 1 % (0.32 against 0.33, 2.11 against 2.14, 8.47 against 8.49 in log units). It also correctly *declines* to measure a barrier of 8.5 from 200,000 sweeps, too few to cross it, and measures it from 2,000,000, which are enough — the refusal is the guard working, not a failure.

  **Not claimed.** These are synthetic Gaussian histograms. They test the arithmetic of the analysis, not whether tempering equilibrates, and a real histogram can be wrong in ways a Gaussian cannot.

- **O7 One coupling ladder cannot serve three sizes, and the failure is the physics.** (2026-09-21, exploratory.) The first T6 control used a single 18-rung ladder for N = 36, 64 and 100. At N = 36 it worked: 48 to 58 round trips per replica, four replicas started from different couplings all reweighting onto g_c = 7.39 to 7.55, latent heat about 5.8 per point, barrier about 0.9. At N = 64 it gave **zero round trips in every replica**, and the run says why:

  | k | g | φ | swap acceptance |
  |---|---|---|---|
  | 6 | 7.50 | 0.710 | 0.65 |
  | 7 | 7.00 | 0.756 | **0.27** |
  | 8 | 6.60 | 1.176 | 0.46 |
  | 9 | 6.30 | 1.455 | 0.80 |

  Acceptance is 0.62 to 0.80 along the whole ladder and collapses only where φ jumps. That is not a tuning failure, it is the latent heat: across the transition neighbouring rungs stop sharing any energies in common, so no replica can cross, so the ladder is severed exactly where the measurement has to happen. It gets worse with size because the gap grows with size.

  Consequences, and what was changed:
  - **The ladder spacing must fall like 1/N.** Two rungs exchange when the tilt between them times the energy gap is of order one, and the gap is about 5.8 N. `scripts/make_t6_ladder.py` now places rungs uniformly in 1/g (not in g, which crowds the hot end and starves the cold) at spacing 1.5/(5.8 N), finely through a window around g_c and three times coarser outside. This gives 13 rungs at N = 36, 24 at N = 64, 37 at N = 100.
  - **One config per size**, since a shared `couplings` list cannot express this. Also lets the three sizes run at once.
  - **The cold tail was cut.** The coldest rungs of the first attempt had a move acceptance of 0.0001 — frozen, contributing nothing but extra ladder for a replica to diffuse across.
  - **Zero round trips is a gate failure, not a result.** Gate 4 caught this. The severed run was stopped rather than left to spend hours at N = 100 producing data that could not pass.
  - **Not claimed.** That the repaired ladder restores round trips at N = 64 and 100 is the expectation behind the redesign, not yet an observation. If it does not, tempering is the wrong instrument at these sizes and that is the finding — Wang-Landau already failed here (Q17), and the honest outcome would be an upper bound on the barrier rather than a measurement of it.

- **O8 The transition coupling is measurable; the barrier is not yet, and the energy is the wrong ruler.** (2026-09-21, exploratory.) Two findings, and a disclosure.

  **The barrier does not survive being asked twice.** A barrier is a property of the system, so reweighting to it from one rung of the ladder or from another are two routes to one number. At λ = 0, N = 36, of 13 rungs the three that can see the transition give:

  | rung g | g_c | latent | barrier |
  |---|---|---|---|
  | 8.731 | 8.040 | 5.78 | 0.700 |
  | 8.216 | 7.993 | 6.37 | 0.436 |
  | 7.758 | 7.968 | 5.78 | 0.416 |

  Spread across rungs: **g_c 0.9 %, latent heat 9.9 %, barrier 54.9 %.** So g_c is a measurement, the latent heat is marginal, and the barrier is not a measurement at all — and the barrier is the observable the first-order verdict leans on hardest, since the pre-registered criterion is how it grows with size. A quantity that changes by half its value depending on which rung you approach it from cannot be fitted against √N. **No barrier number should be quoted from this data.**

  **The energy spectrum is a comb at most λ, and H is therefore a poor reaction coordinate.** The energy is 16(N − S) + 4λX, a sum of two integers with two quanta, so which energies are reachable — and how many ways each is reached — is arithmetic between 16 and 4λ. Where 4λ divides 16 the lattice is uniform and there is no comb: λ = 0 (quantum 16) and λ = 1 (quantum 4). Where it does not, the histogram grows teeth. At λ = 1.25 (quanta 16 and 5) the counts at N = 36 ran 2899, 30, 181, 1024, 2046, 1964, 34 on consecutive levels, and the analysis read two teeth as humps 19 levels apart with a barrier of 1.7. That is arithmetic, not physics. Note this hits two of the four pre-registered λ values: 1.25 and 1.5 (quanta 16 and 6) are combed; 0 and 1 are clean.

  **The fix worth considering, which is a change to a pre-registered method and so is Emily's call.** Use S — equivalently φ = S/N, the order parameter the transition is actually defined by — as the reaction coordinate instead of H. S is an integer with uniform spacing at every λ, so there is no comb by construction. The two phases are then identified in φ, the latent heat remains an *energy* difference between them (it must, that is what a latent heat is), and the free-energy barrier is measured along φ, which is standard practice. This needs `run_t6_tempering.py` to store the joint (S, X) histogram rather than the H histogram — the per-sweep S and X already exist in the run and are simply not saved. One side benefit: the stored object is then the same one the Wang-Landau work used. **Correcting something I said too strongly when first proposing this:** storing (S, X) does *not* mean one run serves every λ. It fixes H exactly for any λ, but a tempering run still samples only its own λ's distribution, so moving to another λ is a reweight and is limited by overlap exactly as moving in g is. It is Wang-Landau, which measures the density of states itself, for which one run genuinely serves every λ — and that is the method that failed at size (Q17).

  **Disclosure, because it matters for how the numbers are read.** Three guards in the analysis were repaired today (O6) for reasons independent of any result: each was demonstrably wrong on synthetic histograms whose answer was known by construction. The coarse-graining veto, by contrast, was added *after* seeing the λ = 1.25 data it rejects, and its two constants (`COARSE_BINS`, `COARSE_TOL`) are choices that move the numbers — adding it changed the λ = 0, N = 36 barrier from 0.969 to 0.436. That is tuning an instrument while looking at what it measures, which is the thing the pre-registration exists to prevent. It is recorded here rather than quietly kept. The veto is still the right idea — a real barrier should survive coarse-graining and a comb tooth should not — but it wants fixing at the source, by choosing a coordinate with no comb in it, rather than by a threshold that has seen the answer.

- **O9 First results along φ; the ladder wall at λ = 0; and the pre-registered sizes mix two cold phases.** (2026-09-21, late; exploratory.) Runs `t6b_*` under amendment 1.

  **The coordinate change did what it was for.** λ = 0, N = 36, four replicas, 73 round trips: g_c 7.506, latent 5.82, barrier 0.949. Spread across the six rungs that see the transition: **g_c 1.6 %, latent 4.1 %, barrier 17.0 %** — against 0.9 / 9.9 / 54.9 % along H (O8), and twice as many rungs see it. The g_c of 7.5 has now been measured on three different ladders in two different coordinates. And λ = 1.25 at N = 36, which along H had shown a "barrier of 1.7", shows **no two-hump structure at all** along φ; nor does λ = 1.5. That is the comb gone.

  **λ = 1 at N = 36 and 64: nothing at the transition.** The analysis does find pairs of humps, but at g_c ≈ 1.7 — deep in the cold phase, below the bottom of the transition region — separated by Δφ ≈ 0.08, and with rung spreads of **73 % in g_c, 339 % in latent heat, 57 % in barrier**. Different rungs are finding different small wiggles in the ordered phase, not one property of the system. Round trips are 22 at N = 64, so it is not a sampling failure. Read as: no two-phase structure at the geometry-forming change at these sizes, which is the published picture. Not a verdict — one λ, two sizes, gate 3 not yet applied.

  **λ = 0 at N = 64 hits the ladder wall.** Two replicas: two clear humps, g_c 6.572 (rung spread 1.2 %), latent 9.54, barrier 4.28 — but **1 to 2 round trips**, and swap acceptance collapses to **0.26 at g = 6.75**, the same place and the same value as the severed shared-ladder run (O7). The rule 1.5/(5.8 N) failed because it was sized from the N = 36 latent heat and the gap at N = 64 is 9.5 per point, so the product came out near 2.5. Gate 4 fails; the 4.28 is not quoted, since a valley crossed once or twice reads deeper than it is. `t6b_lam0_n64_dense` (33 rungs, packed three times finer across g = 7.05 to 6.35) is running to find out whether targeted densification restores round trips. If it does not, tempering has reached its known limit at first-order transitions — the gap grows like N, the rungs needed grow with it, and the time to diffuse across them grows with their square — and the honest λ = 0 result at N ≥ 64 is "two phases, transition coupling measured, barrier not measurable by this method".

  **Why the latent heat grew from 5.8 to 9.5, which an intensive quantity should not do.** N = 36 is 2 × 16 + 4 and the smallest valid piece is 14 points, so at λ = 0 its cold phase cannot be whole knots: it is one knot plus a 20-point ribbon, at φ = 1.278. N = 64 is 4 × 16 exactly: four knots, φ = 1.422. **Those are different cold phases with different energies, so their latent heats differ for a structural reason, not a statistical one.** N = 100 is 6 × 16 + 4 and will be knots-plus-ribbon again. The pre-registered square tori 36 / 64 / 100 therefore mix two cold phases at λ = 0, and a √N fit across them would be fitting through a structural step. This is arithmetic — the ribbon result of section 19 applied to the size list — and I did not connect the two when the sizes were chosen. It affects λ = 0 only; at λ ≥ 1 the cold phase is the sheet, which exists at any size. **Proposed as amendment 2 for Emily, not enacted:** for λ = 0 use multiples of 16 — 64, 96, 128, 144, 160 — which are the Gate A sizes, presumably chosen for this reason in the first place. Whether the pre-registered 36 and 100 are then reported alongside or set aside is her call; the runs at 100 continue regardless, and gate 4 will say what it says.

- **O10 The λ = 0 barrier by a one-dimensional walk; two instruments agree bin by bin; and what the λ = 1 "humps" are.** (2026-09-21, late; exploratory, under amendments 2 and 3.)

  **The instrument.** At λ = 0 the energy is 16(N − S) alone, so the density of states is one-dimensional in S and the Wang-Landau walk that failed over (S, X) at N = 36 (Q17: 737 bins, zero round trips) is a different problem over S alone (49 bins at N = 36). `wang_landau.py` gained `track_x=False`; `run_wl_lam0.py` runs a scout pass to find the reachable range of S and then the real walk on exactly that range, so round trips mean what they say. Validated three ways before any number was read at a new size: it reproduces the exact N = 16 counts summed over X (new test); at N = 36 it puts the two phases at φ = 0.917 | 1.278, the same to three figures as tempering, with g_c 7.34 against tempering's 7.51; and at N = 64, overlaid bin by bin against the tempering histogram at the nearest rung, **the two agree to a few per cent across the whole hot phase (S = 37 to 65)** — two unrelated methods giving one P(S). Round trips: 191 at N = 36, 52–55 at N = 64, 16 at N = 96, 3 at N = 128 on a unit-length walk.

  **A bug in my analysis of the walk, found by that overlay.** The walk at N = 64 has a valley of depth about 4.3 between the hot hump and the knots, plain in the overlay; the analysis reported 0.044. `two_humps` accepted only *interior* maxima, and at λ = 0 the ground state is the highest reachable S — the cold hump sits exactly on the edge of the visited range and could not be seen. An end bin higher than its one neighbour is a maximum; the rule was arbitrary and is fixed. This was a defect independent of any result (the exclusion made no sense on its own terms), and the fix raised the N = 64 barrier from 0.04 to 5.10, so it is stated here rather than absorbed.

  **Why tempering's untrusted N = 64 barrier of 4.28 was nevertheless close.** The overlay shows why it was untrusted: the tempering rung nearest the transition had 1, 21, 35 and 169 counts in the cold bins where the walk puts 6 % of the weight — its 1–2 round trips made visible — and reweighting a handful of counts happened to land near the right depth. The guards did not catch it because the tail was sparse, not empty. The walk is the quoted instrument; tempering at λ = 0 is the cross-check, as amendment 3 says.

  **Two seeds at N = 64 agree.** g_c 6.870 / 6.890, latent 11.24 / 11.31, barrier 5.10 / 5.44 — spreads 0.3 %, 0.6 %, 6.4 %, inside gate 3's 10 % and 20 %. Four seeds each at N = 48 (8 × 6, three knots), 64 and 96 are running; `scripts/analyse_wl_lam0.py` applies gates 3 and 4 and fits whatever passes. First look at the growth, one seed each and gate 4 not yet passed at 96: barrier 5.10 (N = 64) → 8.77 (N = 96), a factor 1.72 for a factor 1.22 in L and 1.5 in N. If that holds with four seeds it is faster than an interface (∝ L) and closer to ∝ N, which would fit knots that cost nothing to separate — a shattering rather than a front. **Not claimed until the seeds are in.**

  **An overwrite, disclosed.** The second seed at N = 64 was launched before the runner had a `--tag` argument and wrote `results/wl_lam0_N64.npz` over the first seed's file. Both seeds' numbers survive in `results/wl_lam0.jsonl` (appended, not overwritten) and above; the first seed's ln g(S) itself is lost. Results are append-only by project rule and this broke it. Tags were added before anything else was launched.

  **What the λ = 1 "humps" were.** O9 recorded pairs of humps at λ = 1, N = 36 and 64 at g ≈ 1.7 with rung spreads of 73 %, 339 %, 57 %. At λ = 1 exactly, the flat sheet, the tube and the 4-cubes tie in energy (`test_four_cube_energies`; the design brief), so the cold end is a *degenerate manifold* of states at different φ. Reweighting in g cannot shift the balance between states of equal energy — their relative weight does not depend on g at all — so a "g_c" between them is undefined, which is precisely the wild spread. Those humps are the sheet/tube/cube degeneracy of Q15 showing up in P(φ), not a transition; and they are where the symmetry count of section 9 would decide the balance if it were applied. At the geometry-forming change itself λ = 1 shows nothing two-phased at these sizes. The upper bounds from `analyse_t6_phi.py`: latent heat **< 1.65 (N = 36), < 1.51 (N = 64)** per point at λ = 1, and similarly at 1.25 and 1.5, against 11–12 measured at λ = 0 on the clean sizes — and the bound falls with N, as a continuous transition's would.

- **O11 The λ = 0 control: three sizes pass every gate; two of the three verdict criteria are met overwhelmingly; the third is mis-specified, and the control caught it.** (2026-09-22, early. `scripts/analyse_wl_lam0.py`, one-dimensional walks under amendments 1–3.)

  **The data.** Four seeds at each of N = 48, 64, 96 (three, four and six whole knots), every walk ≥ 20 round trips (gate 4), seeds agreeing to 6 %, 15 % and 7 % on the barrier and to 0.6 %, 2.7 % and 0.5 % on the latent heat (gate 3):

  | N | g_c | φ hot \| cold | latent heat | barrier | Binder min | C_max / N |
  |---|---|---|---|---|---|---|
  | 48 | 7.538 ± 0.017 | 0.792 \| 1.500 | 10.32 ± 0.01 | 3.83 ± 0.05 | 0.381 | 24.1 |
  | 64 | 6.860 ± 0.070 | 0.750 \| 1.500 | 11.27 ± 0.09 | 5.15 ± 0.24 | 0.480 | 45.0 |
  | 96 | 6.202 ± 0.010 | 0.698 \| 1.500 | 12.50 ± 0.02 | 8.43 ± 0.12 | 0.575 | 99.3 |

  **Criterion 1 (latent heat non-zero at 3 s.e.): met.** 12.5 per point at the largest size; the intercept against 1/L is 17.8 ± 0.1. (That intercept assumes a 1/L approach, which is a guess about the form; but nothing about the form could bring 12.5 to zero.)

  **Criterion 2 (barrier grows, slope positive at 3 s.e.): met.** Against L: +1.59 ± 0.05, 34 standard errors. Against N: +0.096 ± 0.003, also 34. Three points cannot tell the two forms apart (rms residual 0.19 against L, 0.10 against N); recorded, not claimed. If it is N, the knots cost nothing to separate and the transition is a shattering rather than a front; that is a question for N = 128 and 160.

  **Criterion 3 (Binder minimum below 2/3 and not rising towards it): not met by the letter, and the letter is wrong.** The minima are 0.381, 0.480, 0.575 — below 2/3, and rising. But the value a first-order transition *predicts* for the Binder minimum is not 2/3. For a distribution that is two spikes at the phase energies e₊ and e₋, B = 1 − 2(e₊⁴ + e₋⁴)/(3(e₊² + e₋²)²), which equals 2/3 only when |e₊| = |e₋| and is otherwise below it by an amount fixed by the two energies (this is the standard result; Challa, Landau and Binder 1986). From the measured phase energies — e₊ = 16(1 − φ_hot), e₋ = 16(1 − 1.5) = −8 — the prediction is 0.501, 0.541, 0.594 at the three sizes, itself rising because the hot phase moves with N. The measured 0.575 at N = 96 sits 0.02 below its own first-order limit of 0.594 and 0.09 below 2/3. **The minima are rising towards 0.59, not towards 2/3**, and the approach from below is the known finite-size behaviour at a first-order transition. The pre-registered wording did not anticipate this, and read literally it can never return FIRST ORDER on a case where the two phase energies differ in magnitude — which is every case in this model, since the cold phase is at φ = 1.5 and the hot one near 0.7. The same two-spike arithmetic also predicts C_max/N = N Δe²/(4 g_c²): 22.5, 41.7, 97.5 against measured 24.1, 45.0, 99.3 — a fourth check, consistent.

  **The pre-registered verdict at λ = 0 is therefore INCONCLUSIVE**, on the stated ground that the criteria disagree, and the pre-registration says that outcome is not to be resolved afterwards by changing the rule. That is correct and it stands.

  **What the positive control was for.** The config for the first λ = 0 run said: if the instrument cannot see a first-order transition here, no null result at λ > 1 means anything. The instrument sees it — a latent heat of 12 and a barrier growing at 34 standard errors are not ambiguous. What cannot see it is criterion 3 as written. That is exactly what a positive control exists to catch, and it has to be fixed *before* the λ ≥ 1 verdicts are issued, not after, or the null results there would be judged by a rule that fails the positive case. **Proposed as amendment 4, for Emily and not enacted:** criterion 3 compares the Binder minimum to the two-spike prediction computed from the measured phase energies, requiring it to lie below 2/3 and within a stated tolerance of that prediction, rather than requiring it not to rise. The honest caveat, stated so it cannot be missed: this amendment would be adopted after seeing the data it changes the verdict on. What makes it defensible is that the two-spike formula is textbook and has no free parameter, and that the control — not the cases under test — is what exposed the defect. If she adopts it, the λ = 0 verdict becomes FIRST ORDER; if she does not, it stays INCONCLUSIVE and criterion 3 is dropped from the λ ≥ 1 verdicts as uninformative, which must also be stated in advance.

  **Not claimed.** Sizes 48–96 only; N = 128 needs a walk roughly seven times longer (3 round trips on a unit walk); 160 longer still. Whether the barrier grows like L or like N. Any connectivity observable in the valley, which the walk does not record and the pre-registration asks to have reported alongside.

  **Addendum, 2026-09-22, later: amendment 4 enacted by Emily; the verdict re-issued.** Her choice, among three put to her (adopt; drop criterion 3 as uninformative; keep as written), was to adopt: criterion 3 is now that the Binder minimum lies below 2/3 at every size, within 0.05 of the two-spike prediction at the largest size, and with the gap shrinking with N. Re-run on the same walks (`scripts/analyse_wl_lam0.py`, nothing else changed): gaps 0.120, 0.061, 0.020 at N = 48, 64, 96 — shrinking, and 0.020 at the largest size against a tolerance of 0.05 (or the 0.03 first proposed; either passes). Criterion 3 MET; criteria 1 and 2 as before. **PRE-REGISTERED VERDICT, λ = 0, sizes 48/64/96: FIRST ORDER.** Recorded with it: the rule was adopted after seeing the data it changes the verdict on; what makes that defensible is that the formula has no free parameter and that the control exposed the defect. The same criterion 3 now applies at λ ≥ 1, where the `t6c_*` reruns are still going; there the question is moot unless criteria 1 and 2 are met, and O12's one-hump result says they will not be.

- **O12 λ ≥ 1 complete at 36 / 64 / 100: no two-phase structure at the transition, the lump bounded and falling, and gate 4 failing for a reason that is not a wall.** (2026-09-22. Runs `t6b_lam1`, `t6b_lam125`, `t6b_lam15`, tempering along φ under amendment 1.)

  **The bound, which is the falsification clause's required output.** Largest latent heat that could hide in a single hump, per point:

  | λ | N = 36 | N = 64 | N = 100 |
  |---|---|---|---|
  | 1 | < 1.65 | < 1.51 | < 1.30 |
  | 1.25 | < 1.60 | < 1.47 | < 1.27 |
  | 1.5 | < 1.66 | < 1.45 | < 1.26 |

  Against 10.3, 11.3, 12.5 *measured* at λ = 0 on the clean sizes. The bound falls with N at every λ, which is how a continuous transition's energy fluctuations behave and the opposite of a latent heat, which holds its value. **Any lump at λ ≥ 1 is at least eight times smaller than the one at λ = 0 and shrinking.**

  **No two-phase structure at the geometry-forming change.** λ = 1.5: none at any coupling, size or replica. λ = 1.25: one replica at N = 64 found φ = 1.000 | 1.062 at g = 1.35 with a latent heat of 0.04 and a rung spread of 183 % — the perfect sheet against a sheet with one defect, at the cold end, not a transition. λ = 1: pairs at g_c 1.6 to 2.1, Δφ 0.08 to 0.13, rung spreads 33 to 339 % — the degenerate manifold of O10 (sheet, tube and cubes tie in energy at λ = 1, so reweighting in g cannot set their balance), at the cold end below the transition. **At every λ ≥ 1 and every size, the region where φ actually changes, g ≈ 2.5 to 5, shows one hump.**

  **Gate 4 fails at N ≥ 64, and the reason is diagnosed.** Round trips (minimum over replicas): λ = 1: 102 / 15 / 1; λ = 1.25: 32 / 11 / 3; λ = 1.5: 26 / 15 / 0 at N = 36 / 64 / 100. Not a severed ladder — swap acceptance is 0.20 to 0.74 at every link, with no collapse anywhere, and φ moves smoothly through every rung (no jump, which is the continuous transition itself). It is diffusion: eighteen rungs, a hot end coarse in 1/g (the top link accepts 0.20), and a cold tail of four to five rungs where the move acceptance is 0.001 and φ has saturated. The pre-registered rule is per run and it fails. **So no verdict is issued at λ ≥ 1 from these runs.**

  **What does not depend on round trips.** Four independent replicas, started from independent melts, agree on φ at N = 100 to **0.001 to 0.01 at every rung with g ≥ 2.2**, for all three λ, with integrated autocorrelation times of a few hundred sweeps against 60,000 measured. The only disagreement is at λ = 1's two coldest rungs (0.06 to 0.07, τ ≈ 1700 sweeps) — the degenerate manifold, below the transition, where the choice between sheet, tube and cubes is slow. For a continuous transition there are no two phases that a ladder crossing has to mix; the direct evidence of equilibration in the transition region is replica agreement, and it is there. This is why the bound in the table is stated as exploratory rather than withheld.

  **What is being done about it.** `t6c_*` runs: N = 64 and 100 at each λ ≥ 1, the ladder trimmed to fourteen rungs (hot end refined, the frozen tail below g = 2.35 cut) and the measured rounds tripled. Sampling-efficiency changes only; the same distributions. Expected to meet gate 4 as written, at which point the λ ≥ 1 verdicts follow under whatever criterion 3 Emily settles (O11). N = 36 already passes and is not re-run.

  **Not claimed.** Any verdict at λ ≥ 1. The word "continuous" (the pre-registration reserves it). Anything about λ between 1 and 1.5 other than the three values run.

- **O13 T7: the change from one order to another is a switch, by a front, and it happens twice.** (2026-09-22. `t7_lam125_n*` and the rerun `t7b_lam125_n*` with fresh seeds; `t7_lam15_n*`; PREREGISTRATION T7 and its amendments.)

  **Why this and not T6.** Emily's hypothesis was always a change from one *arrangement* to another, never from disorder (her correction of 2026-09-20; claim 3). T6 tested the disorder route because that is the transition the published work measures, and I did not re-scope when corrected. T7 tests the order → order change the published family contains: the tube, one dimension curled, 4(λ − 1) above the sheet, metastable, decaying into the sheet.

  **The three predictions, written before looking, hold at every size on two independent sets of seeds** (λ = 1.25, g = 1.5, tubes 16×4 to 48×4, thirty decays each):

  | N | wait (sweeps) | CV | vertices at d ∈ {1, 2} at half conversion | largest sheet piece | pieces |
  |---|---|---|---|---|---|
  | 64 | 871 / 660 | 0.91 / 0.84 | 0.990 / 0.998 | 0.98 / 0.99 | 1.3 / 1.1 |
  | 96 | 913 / 928 | 1.10 / 1.02 | 0.990 / 0.988 | 0.95 / 0.96 | 1.6 / 1.5 |
  | 144 | 856 / 743 | 1.01 / 0.76 | 0.997 / 0.997 | 0.92 / 0.96 | 1.4 / 1.2 |
  | 192 | 1039 / — | 0.87 / — | 0.995 / — | 0.85 / — | 1.8 / — |

  (first run / rerun; N = 192 rerun in progress.) In words: the wait is memoryless — the change starts by a rare event, not on a schedule; at the halfway point **99 % of vertices are either still tube or already sheet, with essentially none in between**; and the sheet-like vertices form **one connected front**. That is a first-order change between two orders, in the sense the pre-registration defined before the runs, at every size tried. The mean wait does not fall with N (recorded, not predicted; it refutes homogeneous per-site nucleation and was already known from Update 9).

  **The verdict is withheld by the letter, because gate 3 fails — and gate 3 found something.** The energy released was to be within 1 % of 4(λ − 1). With a fixed 300-sweep settle, half the decays read 0.5 to 0.9. Followed for 6,000 sweeps, half release 1.00 at once and half release **0.78, sit on that value, and then release the rest in a single step** — the same 0.78 every time, a specific defected sheet, a second metastable state which itself switches sharply. With the settle run until the energy stops changing (T7 amendment 1), 16 to 21 of 30 decays at each size pause on that ledge for 600 to 27,000 sweeps, and a few are still on it at the 30,000-sweep cap. **The ledge outlives the tube.** So the tube → sheet change is two sharp steps with two memoryless waits, releasing 0.78 and then 0.22 of the lump. Gate 3, as written, asks every decay to complete both steps inside the run, which no finite run can guarantee; proposed amendment 2 checks the energy exactly at whichever state the decay has reached. Emily's call; if adopted, λ = 1.25 is TWO-STATE CHANGE.

  **λ = 1.5 is the unstable case, not the metastable one.** φ = 0.95 by sweep 50 in every replica, as in the design-track pilot. No waiting time (CV = 0 by construction), 25 to 30 % of vertices at neither the tube nor the sheet value at half conversion, and the converted region in 8 pieces at N = 192. The tube there is past its spinodal: it does not switch, it falls apart everywhere at once. The pre-registration listed λ = 1.5 assuming a long-lived tube; the metastable window at g = 1.5 lies below 1.5, and where in 1 < λ < 1.5 it closes is a measurement for T8.

  **Against the claims, plainly.** Claim 4 says the change from X to space was sharp and released a lump. In this family the change from *disorder* to space is not sharp (T6, and the published work). The change from *one order* to space — the tube uncurling — is sharp in every way the pre-registration asked: it waits, it starts somewhere, it sweeps across as a front with the two orders coexisting on either side, and it releases a definite energy. Then it does it again. That is the mechanism the right way round, in the published model, with no new ingredient — at one λ, one temperature, in two dimensions, with a stand-in for X that is a curled sheet and nothing more.

  **Not claimed.** That X is a tube. Anything about the universe. The word "first order" in the thermodynamic sense (this is a decay at fixed temperature; the pre-registration defined "sharp" for that case and the data meet that definition). Where the metastable window in λ ends. What the ledge state is, structurally — only that it is one state, at 0.78, every time. What happens in a sealed box (T8).

  **Addendum, 2026-09-22, later: amendment 2 enacted by Emily, in its strict form; gate 3 still fails, and the reason is now known.** Her choice was to check the energy at whichever state the decay reached, with the ledge fixed as one ring — the lump less (24λ − 16)/N — rather than the modal ledge value first proposed. Re-run (`scripts/analyse_t7.py`, `t7b`): at the end of the settle **24 to 28 of 30 decays per size are at the sheet within 1 %, 0 to 1 on the one-ring ledge, and 2, 4, 2 and 6 at neither** (N = 64, 96, 144, 192). The rerun's ledge decays mostly finished: 16 to 21 of 30 paused, and all but the "neither" ones then completed. **Every one of the 14 "neither" decays has `settle_sweeps` = 30,000: they were still moving when amendment 1's cap ended them.** They are not resting states. Their final S is N (a sheet by square count, with surplus edges still carrying energy: released 0.28 to 0.87), N + 2, N + 4 or N + 5 (partly uncurled): defected sheets annealing slowly at g = 1.5, caught mid-way. So gate 3 as enacted fails at every size for one reason only — a minority of decays had not settled by the cap — and no rule about *which* states count could pass them, because they were not in a state. **The verdict is withheld by the letter.** Predictions (a), (b) and (c) hold at every size in both runs, as before.

  **Two ways forward, both Emily's, neither enacted.** (i) *Finish the measurement:* the fourteen decays are reproducible from their recorded seeds; replay them with the cap raised from 30,000 to 100,000 sweeps and read where they settle. This changes a protocol parameter (amendment 1's cap), not a rule: a longer settle cannot manufacture agreement, it can only reveal the resting state, and if that is neither sheet nor ring the gate fails honestly. (ii) *Amend the gate:* gate 3 applies to settled decays only, the unsettled count is reported per size and must be a minority. Proposed as T7 amendment 3 in `PREREGISTRATION.md`; my recommendation is (i) first, and (ii) only if (i) is refused or the replays still do not settle.

  **Second addendum, 2026-09-22, 10:42: amendment 3 (i) enacted by Emily and run; and a correction to the paragraph above.** All fourteen replays reproduced their originals exactly (identical waiting time and first-window release; none rejected). Two finished to the sheet after the old cap: N = 64 replica 1 at 44,400 settle sweeps (a ledge of 42,600) and N = 192 replica 10 at 84,600 (a ledge of 83,400). **Twelve reached the 100,000-sweep cap**, with released fractions 0.716 (N = 64); 0.583, 0.604, 0.792, 0.833 (N = 96); 0.842, 0.867 (N = 144); 0.766, 0.802, 0.823, 0.823, 0.958 (N = 192) — retained energies of 8 to 45 units. **Six of the twelve show the same released value to the last digit after 100,000 sweeps as after 30,000** (96/3, 96/10, 192/5, 192/8, 192/20, 192/22); the other six moved by 0.003 to 0.057 over the extra 70,000. **Gate 3 as enacted fails at every size; the verdict stays withheld.** Predictions (a), (b) and (c) are unchanged and hold.

  **The correction.** The paragraph above said the fourteen "were still moving" and "are not resting states". That was an inference from `settle_sweeps` = cap, and it was wrong for at least six of them: amendment 1's settle loop terminates only when the released energy is *both* stable *and* within 1 % of the full release, so a decay resting on any ledge runs to the cap by construction, moving or not. `settle_sweeps` = cap means "did not reach the full release", nothing more. The twelve are, mostly, **resting states that are neither the sheet nor the four-point remnant**: sheets with more, or other, defects in them — 8, 16, 20, 34, 38, 45 units and so on, in which the known 14-unit remnant and 20-unit twist (O15) may be summands, but which have not been read structurally and are not identified by their energy alone. So the ledge is not one state: the tube's decay has a family of resting states on the way down, the four-point remnant the common one and these the rare ones (12 of 240).

  **What would close it, and it is Emily's call (T7 amendment 4, proposed, not enacted).** Gate 3 was written as an energy check, and its list of allowed final states (sheet; one four-point remnant) is an assumption the data have outgrown. The honest repair is to *identify* rather than assume: replay the twelve once more with the adjacency saved at the end, read each resting state (local-dimension histogram, pieces, extra squares, surplus edges), and pass gate 3 for a decay exactly when its released energy equals the exact energy of the structure read. The alternative already written as option (ii) — gate only decays that reached the full release, report the rest — remains available and is weaker.

  **Not claimed.** What the twelve states are. That they are stable rather than slow (six unchanged over 70,000 sweeps; six drifting). Any verdict.

  **Third addendum, 2026-09-22, later: amendment 4 (a) enacted by Emily and run — the twelve read from their wiring; verdict TWO-STATE CHANGE at N = 64, 96, 192.** Replays `configs/t7d_lam125_n{64,96,144,192a,192b}.json` (same seeds, same 100,000 cap, final adjacency saved to `results/t7d_lam125_n*_adj/`), all twelve reproducing their originals exactly. Read by `scripts/analyse_t7_states.py` (tests: sheet holds 0, tube holds 1 per point and is one d = 1 piece, naming, the 1 % tolerance):

  | N | replica | held (units) | S − N, X | off the sheet | gate 3 |
  |---|---|---|---|---|---|
  | 64 | 25 | 18 | 2, 10 | two 4-point d = 1 pieces | pass |
  | 96 | 3 | 16 | 4, 16 | two 8-point d = 1 pieces | pass |
  | 96 | 10 | 38 | 2, 14 | one 8-point d = 1 piece; two d = 3 pairs; two d = 1 pairs | pass |
  | 96 | 20 | 40 | 0, 8 | two d = 1 pairs, two d = 3 pairs, a d = 1 and a d = 3 singleton | pass |
  | 96 | 23 | 20 | 0, 4 | **nothing** — every vertex at d = 2 | pass |
  | 144 | 3 | 8 (final) | 2, 8 | two 4-point d = 1 pieces | **FAIL** — held ≈ 23 units from 30,000 to nearly 100,000 sweeps, then dropped to 8 inside the last measuring window, so the recorded release is that window's average and does not match the final structure |
  | 144 | 5 | 18 | 2, 10 | two 4-point d = 1 pieces | pass |
  | 192 | 3 | 34 | 1, 10 | one 4-point d = 1 piece; two d = 3 pairs; two d = 1 pairs | pass |
  | 192 | 5 | 38 | 2, 14 | one 8-point d = 1 piece; two d = 3 pairs; two d = 1 pairs | pass |
  | 192 | 8 | 45 | 5, 25 | two 8-point and one 4-point d = 1 pieces; a 3-point d = 1 and a 3-point d = 3 piece | pass |
  | 192 | 20 | 8 | 2, 8 | two 4-point d = 1 pieces | pass |
  | 192 | 22 | 34 | 1, 10 | one 4-point d = 1 piece; two d = 3 pairs; two d = 1 pairs | pass |

  **Gate 3 under the enacted wording:** eleven pass; N = 144 replica 3 fails, so N = 144 fails gate 3 and is reported and not interpreted (`scripts/analyse_t7.py lam125 t7b t7c t7d`). **PRE-REGISTERED VERDICT, λ = 1.25, sizes 64, 96, 192: TWO-STATE CHANGE.** Predictions (a), (b), (c) hold at 144 too; only the energy gate fails there, on one decay.

  **What the rare resting states are, as far as the graph says.** Not new arrangements: combinations of small defects in an otherwise flat sheet. Four-point d = 1 pieces (the remnant's composition) appear in pairs holding 8 or 18 units together, not the 28 two isolated remnants would hold, so paired pieces are not two independent remnants — they share surplus edges or sit adjacent (*ours, unverified*; positions not yet read). Eight-point d = 1 pieces hold what two merged remnants might. Pairs of d = 1 and d = 3 vertices recur, the ingredients of O15's twist, here split into separate two-point pieces. And one state (N = 96, replica 23) holds 20 units with every vertex at d = 2: surplus squares on four edges that the local-dimension count does not see. All are fixed-size — 8 to 45 units, however large the tube — so they change nothing about O15's reading of claim 5.

  **Not claimed.** Which of the twelve are stable rather than slow beyond the six already seen unchanged; the geometry of the paired pieces; that the list of species is complete.

- **O14 T9: the sealed tube is a bonfire with a threshold; no slush; the leftover is one ring — at every size.** (2026-09-22. `t9_n{64,96,192}_C*`, 21 configs, 420 runs; `scripts/analyse_t9.py`; PREREGISTRATION T9, no amendments.)

  **The verdict as written: BONFIRE WITH A THRESHOLD.** Every run converted (the spark is still the spark, gate 2), energy conserved to the last unit in all 420 (gate 1), twenty replicas each (gate 3).

  | N | C = 1 … N/16 … N/8 | N/4 | N/2 | N | 2N |
  |---|---|---|---|---|---|
  | 64 | melted 17, 17, 12 of 20 | 3 sheet / 4 melted / 13 neither | 18 sheet | 20 sheet | 20 sheet |
  | 96 | melted 18, 18, 9 | 1 / 2 / 17 | 19 sheet | 19 sheet | 20 sheet |
  | 192 | melted 20, 19, 16 | 0 / 2 / 18 | 19 sheet | 20 sheet | 20 sheet |

  **(a) holds.** First majority-sheet C = N/2 and last majority-melted C ≤ N/8 at every size; C*/N is 0.5, 0.5, 0.5 on the grid, so it scales with N. The predicted N/3.5 lies inside the interval (N/4, N/2] at every size; the grid is too coarse to place it more finely. At C = N/4 the product is mostly "neither" — partly melted or not fully converted — at all three sizes: the crossover is a band, not a line. **(b) holds:** not one run in 420 halted with tube and sheet both present, the bath below g_melt and nothing melting. The tube has no coexistence temperature with the sheet, as argued. **(c) holds:** a ring in 83 to 100 % of sheets at C ≥ N/2.

  **The ring count, read after T10 was committed and launched** (commit 8398209 for the pre-registration, 09:38 for the launch; these counts read at 09:45). This is T9's observable 3, not a T10 result, and it is disclosed here because it bears on T10's prediction (a):

  | N | rings per sheet at C = 2N (20 runs) | at C = N | excess energy per ring |
  |---|---|---|---|
  | 64 | 0 ×1, 1 ×18, 2 ×1 | 1 ×20 | 13.8, 14.0 |
  | 96 | 0 ×1, 1 ×19 | 0 ×3, 1 ×15, 2 ×2 | 14.0, 16.3 |
  | 192 | 0 ×1, 1 ×19 | 0 ×1, 1 ×15, 2 ×4 | 14.3, 14.4 |

  **One ring, however large the tube.** In the coldest box the count is 1 in 18 or 19 of 20 sheets at 64, 96 and 192 alike, and the excess energy is 14 per ring — additive, as T10 (b) predicts. **So T10's prediction (a), that the count grows with N, is very likely to fail**, and by T10's own verdict table the outcome would be ONE RING, HOWEVER LARGE. The prediction stays as committed; T10 runs on fresh seeds and its verdict is whatever it returns. Recorded before it finishes so that it cannot be read as a surprise afterwards. If it returns that verdict, claim 5's leftover in this model is a single defect, negligible at scale, and the claim is back to bookkeeping — VISION Update 13 says so in advance.

  **Why one?** *Ours, unverified, and a follow-up worth pre-registering.* The tube is periodic. The front starts at one place (O13: anywhere, nucleus two rings) and spreads both ways; the two ends meet on the far side. A seam where two fronts meet is one place per tube whatever its length, and a ring that neither front uncurled is what a seam would leave. If that is the mechanism, the leftover ring sits at the antipode of the nucleation site, and the count is 1 by topology, 0 when the seam closes cleanly, 2 rarely. Testable with the departure positions `diagnose_ledge_and_start.py` already records plus the ring's position, at N = 64 in minutes. At warmer baths (C ≤ N/2) the count rises to 1–3 and pieces larger than a ring appear: thermal defects on top of the seam, not the front's doing.

  **Not claimed.** T10's verdict. What C means beyond "how many other places the energy can go". The seam mechanism. Anything at λ ≠ 1.25.

- **O15 T10: ONE RING, HOWEVER LARGE — prediction (a) failed, as O14 said it would; and the reading check found a second, smaller leftover.** (2026-09-22. `t10_n{64,96,192,288}`, 80 runs, fresh seeds, C = 2N; `scripts/analyse_t10.py`; PREREGISTRATION T10, no amendments.)

  | N | rings per sheet (mean ± sd) | largest d = 1 piece | 14 units per ring | bath g at end | (c) |
  |---|---|---|---|---|---|
  | 64 | 0.90 ± 0.31 | 4 | 19 of 20 | 0.49 | holds |
  | 96 | 0.85 ± 0.37 | 4 | 17 of 20 | 0.49 | holds |
  | 192 | 1.05 ± 0.22 | 4 | 19 of 20 | 0.49 | holds |
  | 288 | 0.95 ± 0.22 | 4 | 16 of 20 | 0.49 | holds |

  Gate 1 exact; gate 2 twenty each; gate 3: every replica converted, f_final = 1.0 at every size, so the 12-unit spark suffices at 288 too. **(a) fails:** slope 0.0003 ± 0.0003 rings per point (1.0 standard errors); mean(288) − mean(64) = 0.05 against a scatter of 0.31. **(c) holds:** the bath ends at 0.49 everywhere and nothing leaves. **PRE-REGISTERED VERDICT: ONE RING, HOWEVER LARGE.**

  **(b) fails on 9 of 80 replicas, and that is the check doing its job.** Each of the nine has S = N, X = 4, 20 units of excess — two vertices at d = 1 and two at d = 3 — which is not a ring (a ring is four vertices at d = 1 in one column, S = N + 1, X = 6, 14 units). A second leftover species: a twist two points wide costing 20 units, in 9 of 80 boxes (one box holds two of them, X = 8). The pre-registered count is "pieces at d = 1" and stands as written; recounting with "ring = a piece of exactly four" gives 0.85, 0.75, 1.00, 0.75, the same verdict, reported alongside.

  **Against claim 5, plainly.** In this model, in a cold box, what the change leaves behind is one ring — and rarely a twist — however large the space. A single defect, not a density: at 288 points it is 1.4 % of the points, at a universe's size it is nothing. Claim 5's leftover is back to bookkeeping here, as VISION Update 13 and section T10 said in advance it would be if this came out this way. What could change that is a leftover that is *thermal* rather than the front's: T9's warmer baths (C ≤ N/2) left one to three rings and larger pieces, which is a different question with a different prediction, and is not run. Why the front leaves exactly one is T11, running.

  **Not claimed.** T11's verdict. Anything at warmer C. That the twist is stable rather than slow.

- **O16 T11: NEITHER — the leftover sits anywhere along the tube; the seam guess of O14 is refuted. And a correction: it is not a ring.** (2026-09-22. `t11_seam_n64` (40 replicas), `t11_seam_n96` (30), cold box C = 2N, fresh seeds; `scripts/run_seam_check.py`, `scripts/analyse_t11.py`; PREREGISTRATION T11, no amendments.)

  **The data.** Single-leftover replicas 36 of 40 and 28 of 30 (gate 2 met; conservation exact). Distance, in columns along the tube, from where the change started (circular mean of the first non-tube columns) to the leftover (circular mean of its columns):

  | N | half-length | at the far side (≥ ¾ of half) | random would give | within 1.5 of the start | random | median | mean | random mean |
  |---|---|---|---|---|---|---|---|---|
  | 64 | 8 | 36 % | ≈ 31 % | 19 % | ≈ 19 % | 4.5 | 4.17 | 4.0 |
  | 96 | 12 | 32 % | ≈ 29 % | 4 % | ≈ 13 % | 6.5 | 6.38 | 6.0 |

  **PRE-REGISTERED VERDICT: NEITHER.** Not a seam, not at the seed: the position is indistinguishable from uniform. The front does not leave its remnant where its two ends meet, nor where it started. **Why the cold box ends with exactly one is open**, and O14's guess is withdrawn.

  **Correction to the record: the leftover is not a ring.** The runner filled its `dist` column only when the leftover occupied a single column, on my assumption that it is a ring *around* the tube — four vertices at one position along it. It is not: the four d = 1 vertices span one to four columns, mostly two or three, lying *along* the tube. The distance was therefore computed in `analyse_t11.py` from the recorded columns of the d = 1 vertices via their circular mean, which is the pre-registered observable as written; the runner's `dist` is blank in all but one row and is superseded (the correction is in the analysis, not the data; the result files are as run). **"One ring of the tube" in O13, O14, O15, PREREGISTRATION T10 and T11, and the page, was a geometric guess made from the count alone** — four d = 1 vertices, the tube's circumference — and was never checked until this run. What *is* established: one cluster of four tube-like points, one extra square, six surplus edges, 14 units, one per cold box, along the tube. Earlier entries are left as written; from here the word is "the four-point remnant". A second thing the departure snapshots show: the first non-tube vertices number four to six, in four to five adjacent columns — a short line along the tube, not "two adjacent rings" as O13 inferred from a count of eight at a later threshold.

  **Not claimed.** Any mechanism for the count of one. Anything at warmer baths. What the remnant is, beyond its size, energy and orientation.

- **O17 T6 at λ ≥ 1, reruns complete: gate 4 met; one hump in the transition window at every λ, size and replica; the bound stated; criterion 3 cannot be evaluated where the cold phase sits at zero energy — INCONCLUSIVE by the letter.** (2026-09-22, 10:41. `t6c_lam{1,125,15}_n{64,100}`, fourteen-rung ladders g = 2.35 to 8.00, four replicas each, rounds tripled; `scripts/analyse_t6_phi.py`; `t6b_*` at N = 36 alongside. PREREGISTRATION T6 under amendments 1–4.)

  **Gate 4, met everywhere.** Round trips per replica: λ = 1, 333–400 (N = 64) and 154–176 (N = 100); λ = 1.25, 189–251 and 62–79; λ = 1.5, 127–169 and 46–55 — against a gate of 20. Swap acceptance at least 0.33 at every link. The diffusion problem of O12 is gone.

  **What the histograms say.** λ = 1.25 and 1.5: no two-hump structure in φ at any coupling, size or replica. λ = 1: a pair at the cold end only (g ≈ 1.9–2.1, φ 1.03 | 1.12–1.14, Δe 0.21–0.23 per point) — the degenerate manifold of O10 and O12, where sheet, tube and cubes tie in energy, below the transition; its rung spreads (193 % and 234 % at N = 64; 23 % and 13 % at N = 100) fail gate 3's 10 % and 20 %. In the region where φ actually changes, g ≈ 2.5 to 5, **one hump at every λ, every size, every replica.**

  **The bound, which the falsification clause requires.** Largest latent heat that could hide in a single hump, per point: λ = 1, < 1.51 (N = 64), < 1.30 (N = 100); λ = 1.25, < 1.47, < 1.28; λ = 1.5, < 1.45, < 1.26. Falling with N at every λ, against 10.3, 11.3, 12.5 *measured* at λ = 0 on 48, 64, 96.

  **Criterion 3 cannot be evaluated here, and that is a second mis-specification exposed by data.** The Binder energy cumulant 1 − ⟨H⁴⟩/(3⟨H²⟩²) is not invariant under a shift of the energy zero, and at λ ≥ 1 the cold phase is the flat sheet at H = 0 exactly. Where the energy distribution straddles zero the cumulant collapses toward zero or below whatever the shape: at N = 36 in the transition window it reads −0.92, −1.66 and −4.18 at the three λ; at the coldest rung of N = 64 it is −0.003 ± 0.22 and 0.07 ± 0.68. Restricted to g ≥ 2.5, where H is far from zero, the minima are 0.29 → 0.53 (λ = 1), 0.32 → 0.51 (1.25) and 0.29 → 0.46 (1.5) from N = 64 to 100 — rising, consistent with an approach to 2/3 — but the window is a choice made with the data in view (the region was named in O12 before these reruns), N = 36 cannot be used, and the rules want three sizes. At λ = 0 none of this arose, because both phases sit far from zero (e₊ ≈ +4.8, e₋ = −8).

  **Verdict by the letter at λ = 1, 1.25 and 1.5: INCONCLUSIVE.** Criteria 1 and 2 come out in the direction of "no evidence" (no humps, so no Δe; no barrier), and criterion 3 cannot be read; the rules call that INCONCLUSIVE and forbid resolving it afterwards by changing the rule. The falsification clause's required output is given above: any lump at these settings is at least eight times smaller than the λ = 0 lump and shrinking with size. Not called "continuous".

  **Proposed as T6 amendment 5, for Emily, not enacted.** At λ ≥ 1, criterion 3 uses a statistic that does not depend on where the energy zero sits: the fourth-order cumulant of φ itself (the order parameter), or the energy cumulant with H measured from the hot-phase mean. Computable from the `t6c` files as they stand; nothing re-run. If not adopted, the alternative is to declare criterion 3 uninformative at λ ≥ 1 and issue NO EVIDENCE OF FIRST ORDER AT THESE SIZES on criteria 1 and 2 with the bound — also her decision, not mine.

  **Not claimed.** The word "continuous". Anything between the three λ values or above N = 100. That the λ = 1 cold-end pair is a transition (it is a degeneracy).

  **Addendum, 2026-09-22, later: amendment 5 enacted by Emily, option (a); criterion 3 still does not decide, and the enacted wording is the reason.** `scripts/analyse_t6_phi_binder.py` (tests in `tests/test_t6_phi_binder.py`: the two-spike value, a narrow single hump, the criterion's monotonicity) computes U_φ = 1 − ⟨φ⁴⟩/3⟨φ²⟩² from every rung's joint histogram, reweighted within the φ analysis's usual range, and takes the minimum per replica as the enacted wording says:

  | λ | U_min, N = 36 / 64 / 100 | 2/3 − U_min | replica spread | where the minimum sits |
  |---|---|---|---|---|
  | 1 | 0.65661 / 0.65509 / 0.65524 | 0.0101 / 0.0116 / 0.0114 | ≤ 0.0006 | g = 10.0, every replica |
  | 1.25 | 0.65673 / 0.65539 / 0.65493 | 0.0099 / 0.0113 / 0.0117 | ≤ 0.0006 | g = 10.0, every replica |
  | 1.5 | 0.65692 / 0.65542 / 0.65522 | 0.0098 / 0.0113 / 0.0114 | ≤ 0.0007 | g = 10.0, every replica |

  The gap does not shrink at each step, so criterion 3 is NOT MET as enacted and the verdict stays **INCONCLUSIVE**. But the table's last column says why, and it is not physics: **U_φ has no dip at the transition.** Read at each rung's own coupling it falls monotonically from 2/3 as g rises — at λ = 1.25, N = 100: 0.6664 at g = 2.35 (φ = 0.97), 0.6645 at 3.65 (φ = 0.82), 0.6621 at 5.5 (φ = 0.66), 0.6580 at 8.0 (φ = 0.52); N = 64 and 36 the same shape — because 2/3 − U is set by the relative width of P(φ), and that grows as the mean of φ falls. So the minimum over every coupling is always the hottest coupling the reweight admits (g = 10, 25 % above the top rung), in the random phase, and it measures how the hot-phase φ at fixed g falls with N (the drift of O5 and T9, and the 1/N random-phase floor), not the transition. The energy cumulant has a real dip because the energy fluctuations peak at the transition; the φ cumulant of a single hump has none. **This is a defect in the enacted wording, which I drafted**: it was fixed before any value was computed, as required, but I did not check the shape of U_φ first. The measurements that carry the result are untouched — one hump at every λ, size and replica, any lump below 1.30, 1.28, 1.26 per point at N = 100 and falling.

  **Decided by Emily, 2026-09-22, evening: option (i).** INCONCLUSIVE stands as the final verdict of these runs, and no further change is made to criterion 3. Her reason: the random-phase route is the published question, not the hypothesis's, and the measurements — one hump everywhere, any lump below 1.30, 1.28, 1.26 per point at N = 100 and falling — are the result whatever the label. The options as put to her:

  **What was open.** (i) Leave INCONCLUSIVE as the final word from these runs; the bound stands as the result. (ii) Option (b) of amendment 5: declare criterion 3 uninformative at λ ≥ 1 and issue NO EVIDENCE OF FIRST ORDER AT THESE SIZES on criteria 1 and 2 with the bound — now a choice made after seeing option (a) fail on a technicality, and to be recorded as such. (iii) Restrict U_min to the transition window — not recommended: it would be a third rule change for this test, and a single-hump U_φ has no feature there to read anyway.

- **O18 EXPLORATORY — where the energy went in the sealed boxes, and the author's dark-matter hypothesis.** (2026-09-22, evening. Existing T9 end states, 420 runs; `scripts/explore_t9_energy_split.py`. Not pre-registered; a first look, not a finding.)

  **The hypothesis (the author's, VISION Update 16).** Dark matter is the part of X that did not convert: made in the same change as ordinary matter, which comes from the lump, and dark because it is not made of the fields ordinary matter is made of, while still carrying energy and so gravitating. Two ways it could be abundant enough, both hers: many seeds, each leaving a scrap (TASKS T14); or a "quality of spacetime", energy kept spread through the geometry itself.

  **What the T9 end states say about the second route.** Splitting the conserved total (N · 4(λ − 1) + the 12-unit spark, conserved to 2 × 10⁻¹³ in every run) into what the network still holds above the flat sheet and what sits in the bath: clean sheets (179 runs) hold 7–20 % in the network, almost all of it the one 14-unit remnant, so the share falls with N (18 % at N = 64 with C = 2N, 7 % at N = 192); the in-between end states (87 runs, mostly at the switch-over C = N/4) hold 50–58 %; melted ones (154 runs) 66–99 %. **In this model, a geometry that keeps a large share of the released energy spread through it is one whose sheet has melted.** The split depends on C, a protocol knob, and on N, so none of these shares can be read as a predicted ratio.

  **Why a small leftover may be exactly enough** (*settled physics applied by us; unverified*). Cold matter thins out in proportion to volume, radiation faster (volume^4/3, as it also loses energy to stretching), so matter's share relative to radiation grows in proportion to 1/T. Today ρ_dm/ρ_rad ≈ 0.26 / 9.1 × 10⁻⁵ ≈ 2,900 at T₀ = 2.35 × 10⁻⁴ eV, so at temperature T the ratio was about 0.7 eV / T (ignoring changes in the number of particle species, a factor of a few). If the lump heated the new space to T, the leftover needs to hold only about 0.7 eV / T of the energy: 7 × 10⁻⁷ at 1 MeV, 7 × 10⁻¹⁰ at 1 GeV, of order 10⁻²⁵ at 10¹⁵ GeV. In model units (14 per scrap, 4(λ − 1) = 1 per point at λ = 1.25) that is one scrap per roughly 20 × (T / eV) points — a very sparse sprinkle. So the many-seed route needs few seeds, and it ties the density of seeds to the starting temperature; the dense "quality of spacetime" route would overshoot by many orders of magnitude, and in this model comes with a melted sheet.

  **Not claimed.** That dark matter is leftover X. That scraps are stable over cosmic times, slow-moving ("cold") or able to clump. How a model point maps onto a physical volume, which the scrap-per-point figure depends on. Anything beyond a first look.

- **O19 The 2025 review's text around Eq. (22), read again for what it says about Fig. 3.** (2026-09-22, the author reading the source; no run.)

  Checked because the outreach note asks which variant Fig. 3 shows. **It does not say.** What the passage does settle, and each item agrees with what we already had: the global term alone is minimised by isolated hypercubic complexes and gives a first-order transition, while "if the full Hamiltonian is used, instead the model undergoes a continuous phase transition"; triangles and pentagons are excluded from a homogeneous ground state because 9/8 + 5/8 < 2 (Q10's arithmetic, and the reason our triangles test was the right control); **bipartite graphs are explicitly allowed** as a computational convenience, so our bipartite runs are the right configuration space; the maximum per edge is 2D − 1 = 3 by regularity (Q3); configurations above 2D − 2 squares per edge are **degenerate** with the ground state at λ = 1, which is the degeneracy our own cold end runs into (O10, O12); and the random-phase floor is the formula (3⁴/4)/160 = 0.126 "for N = 160 in the example below", confirming O5 and that Fig. 3 is at N = 160.

  **What is still not stated, and it is what our disagreement turns on:** the run length and how equilibration was checked; whether the hard-core restriction of [KTB19] Sec. 4 was imposed in the Fig. 3 runs; whether the points are from cooling, heating or both. Our disagreement is not about the end values — we match 0.126 and 1 — but about *where* the rise happens, and a short or unequilibrated run moves a curve in exactly that direction. The outreach note's first question is narrowed to that.

- **O20 Concentrated energy melts space; it does not fold it.** (2026-09-22, EXPLORATORY; the author's
  picture of a black hole; TASKS T13 rung 3; `configs/sealed_sheet_budget_lam*.json`.) **A black hole is a
  sealed system** -- nothing gets out -- which is exactly the fixed-total-energy machinery of Q12. So a
  perfect flat sheet was given a budget of energy it cannot lose, and the end state was read by the local
  dimension of every vertex: below 2 is folded, above 2 is melted. **The prediction was written in the
  config first and it failed.** It reasoned from price: at λ = 1.25 an extra square on a full edge costs 4
  and a destroyed square costs 16, so folding is four times cheaper per square and small budgets should buy
  folds. **Measured** (N = 144 and 160, three replicas a point, 4000 sweeps, budgets 0.5 to 16 per point,
  λ = 1.05, 1.25, 1.5, 2.0): melted vertices outnumber folded ones at **every budget and every λ tried**.
  The folded share of the damage is 23, 22, 17, 4 % at λ = 1.05 for budgets 0.5, 1, 2, 4; 5, 7, 10, 4, 0, 0 %
  at λ = 1.25; about 2 % at λ = 1.5; and 0 to 2 % at λ = 2.0. **So price moves it in the predicted direction
  -- the cheaper folding is, the more of it appears -- and never decides it: what decides it is the number of
  ways, and there are far more ways to break a square than to add one.** At 16 per point the box cannot
  absorb its own budget (the demon still holds 192 to 384 units at the end) and every vertex is melted, which
  is the boil-off of O14 in another setting. **Reading (ours, unverified):** within this model the published
  black hole -- a region reverted to the random phase [T25] -- is what concentrated energy makes, and the
  author's re-curled region is not. **What is not tested:** energy delivered to one small patch rather than
  shared across the whole sheet. The demon is a single global store, so this is a sheet with a budget, not a
  jolt in one place; that needs the local-spark protocol of T14 and is the one route left for the author's
  version.

  **CORRECTION the same day, the author's, and it holds.** Three things were wrong with how the run above
  was read. **(1) "Melted" is not damage.** In this model the melted state is the random phase, and [T25]
  reads that phase as matter and energy, with a black hole a large region returned to it. So "the energy
  melted the space" may be nothing more than what a great deal of energy in one place looks like, which is
  close to what a singularity means; it is not obviously the opposite of the author's picture, only a
  different account of the interior. **(2) Heating at equilibrium randomises by construction**, so a sealed
  box given a large budget was always going to end in the random phase; the part of the run with real
  content is narrower and is the fair contest between two ways of absorbing the *same* energy, folded
  against melted, which folded lost at every setting. **(3) The loop does not need space to be metastable.**
  The assistant had treated "space is only stable for now" as a requirement of the author's picture and
  therefore read the floor result (Q18) as evidence against it. The author's position is that space is
  allowed to be stable and stay stable: the return leg of the loop is *paid for* by concentrated energy, not
  fallen into. Under that reading Q18 **supports** the picture rather than counting against it, and the only
  casualty is the separate idea that dark energy is space's own excess, which the author dropped on
  2026-09-22. **What survives as a test:** a jolt into one small patch with cold space around it, which is
  what gravity does and what a shared budget cannot imitate (T14).

- **O21 With braces allowed, space left alone does not refold, and a cooled hot patch jams.** (2026-09-22,
  EXPLORATORY; `configs/refold_*.json`, the chain of Q18.) Three runs, each with its prediction committed
  before it. **(1) A flat sheet left alone** at g = 1, 2 and 4 sits at exactly H = 0 with *no accepted move at
  all*; at g = 8 it climbs to +7.9 per point. So the way out of space is disorder, not folding, and folding is
  not something space does by itself -- which is the author's own point that space refolds at a singularity
  and not everywhere. Predicted, and it held. **(2) Two closed 30-point pieces** survive exactly where the
  sheet does, to g = 4, and at g = 8 they melt and merge into one. Predicted, and it held: the refolded
  arrangement is as durable as space and no more. **(3) A melted patch cooled** for 800 sweeps, six runs at g = 1 and 2, falls
  from about +5 per point to between +1.73 and +2.23 and stops there, every run one connected piece with a
  mixture of triangles, squares and pentagons (0 to 11 triangles, 34 to 52 squares, 8 to 13 pentagons) and
  acceptance 0.002. **Predicted: it would cool into closed pieces. It did not.** It jams at about +2 a point
  in a defective state that is neither space nor a knot, and the six runs agree closely enough that the level
  looks characteristic rather than accidental. That is a kinetic statement and not an equilibrium one -- at
  that acceptance the chain has nearly stopped -- and it is the third of these three predictions, so the run
  that mattered most is the one that failed.

  **WITHDRAWN the same evening, and the author called it before the check was run.** She asked whether
  anyone has ever seen such a jam and said she did not believe it exists: there should be two phases and
  nothing between them. **The check agrees with her.** From where each run stopped, the only question that
  separates a resting place from a stopped walker is whether any single valid move goes downhill, and moves
  do: 2 of the 4264 valid moves out of the first end state lower the energy, the best by 4 units, and 1 of
  4646 out of the second, by 2. A genuine dip has none by definition, which is how the tube and the sheet
  were verified. **So the jam is an artefact of a slow chain that had nearly stopped (acceptance 0.0016)
  and not a third state.** Nothing in this repository shows a stable arrangement between space and the
  random phase, and the best-sampled runs say the opposite: during a tube to sheet conversion 98.8 to
  99.8 % of points read as one order or the other with a front between them (O13). *The lesson, and it is
  the third time this project has learned it: a chain that has stopped and a state that is resting look
  identical in a plot of energy against time. Ask for the moves out.*

- **O22 Leftovers in this model attract only by touching, and that is a theorem, not a measurement.**
  (2026-09-22, EXACT, no sampling; `scripts/run_defect_interaction.py`, `configs/defect_interaction.json`,
  `tests/test_defect_interaction.py`; TASKS T13 rung 3; the author's question of the same day about gravity
  as a pull back towards symmetry.) **The measurement:** make the cheapest defect in a perfect flat sheet
  (one switch, costing 32 on a 10 x 10 torus at λ = 1 and 1.25), make the same defect again a known distance
  away, and compare the pair with twice the single. At every separation on the torus the answer is **exactly
  zero** except where the two touch, where it is **−16**: half of one defect, because the overlapping damage
  breaks a square they then pay for once. Both λ, every placement, 64 placements in all.
  **Why it has to be so, which is worth more than the measurement:** H is a sum over edges of terms that
  depend only on that edge's own squares, so two defects sharing no square contribute independently and
  their energies add exactly. **No long-range force between leftovers is possible here at fixed wiring, for
  any kind of defect, by the form of the energy.** The prediction that this would be a contact interaction
  was written in the config before the run and is what came out.
  **What follows** (*ours, unverified*): if anything like gravity exists in this model it cannot be a force
  carried by the energy between leftovers; it would have to be **entropic** -- a free-energy effect from the
  number of arrangements at a given separation, not from their energies -- which is a measurable thing and
  has not been measured. (That is the shape of Verlinde's entropic-gravity proposal, 2011; general knowledge,
  not read by us, details to verify.) It also means the defect-defect interaction of O13's third addendum is
  a contact effect and not evidence of a field.

- **O23 A long-range force does exist here, and it is between boundaries, not between points.**
  (2026-09-22, EXACT; `scripts/run_force_census.py`, `configs/force_census.json`; follows O22 and answers the
  author's question of whether O22's obstruction can be resolved.) O22's proof needs the damage to sit in a
  patch. The standard way to tell a local defect from one whose damage cannot be confined is to **price it at
  several sizes**, and both objects were priced at N = 36 to 600, at λ = 1, 1.25 and 1.5. **The point defect
  costs exactly 32 at every size**, so it is local and O22 applies to it: no force. **The gap between the two
  orders is exactly 4(λ − 1) per point at every size** -- 0, 1 and 2 -- so a boundary between sheet-order and
  tube-order pays a fixed price for every point it sweeps. **That is a force that does not fall off with
  distance at all**, which is what a constant energy per unit volume converted means, and it is far stronger
  at range than anything that decays. Both halves were predicted in the config before the run.
  **What this resolves** (*ours, unverified*): the obstruction of O22 is real but narrow. It says a *point*
  leftover cannot pull on another point leftover. It says nothing about regions, and this model's long-range
  effect is exactly the one a picture built on regions of one order inside another would want. The project has
  already watched it act: it is what drives the front in T7, at a rate set by that same gap. **What it is
  not:** it is not gravity. A constant force between phase boundaries is what drives bubble walls in a
  first-order transition; it does not fall off as an inverse square, it does not act between separated lumps,
  and nothing here derives an attraction between two regions of the *same* order. Saying "there is a
  long-range force in this model" is true and is not the same sentence as "gravity is here".

- **O24 The coarse law does not govern, by the standard set in advance (PREREGISTRATION T12,
  2026-09-22).** 64 tube decays at λ = 1.25, N = 64 to 192, two couplings, both acceptance rules,
  `configs/front_law_lam125.json`. **Verdict: NOT ESTABLISHED.** Criterion 2 passes (the cost of a front
  is one number, 11.3 ± 3.7, with no trend across sizes); criteria 1, 3 and 4 fail. Criterion 1 fails on
  both readings of its wording, per replica and per cell, and both were computed and reported. **Where it
  fails is informative:** the two coldest, largest cells recover the exact gap to 0.15 % and 1.03 %, and
  every badly failing cell is at the warm coupling, where the converted count is read from a local
  dimension that thermal noise makes flicker and where conversions start in several places at once. This
  run cannot separate a failure of the coarse law from a failure of that proxy, and saying which needs a
  cleaner measure of conversion, i.e. a new test. **Criterion 3 was mis-derived by the assistant:** it
  asked for a rate flat in N, where the counting of Q13 gives 1/N for a local front; the measured rate
  follows neither, falling about as N^−0.7, so the dynamics escape both versions. **An unregistered
  success:** runs that converted in two patches show twice the front cost of runs that converted in one,
  which is what the model says should happen when four fronts are divided by two. **What follows for the
  author's strange-loop reading** (`docs/design/strange_loop_note.md`): its item 3, that the coarse level
  has laws of its own, is not established; what stands is that the front cost is size-independent and that
  both microscopic rules agree on it to three decimals, so the part of the description that does work is
  not an artefact of one rule.

- **O25 Out of an ordered arrangement there is no move that builds. Not few: none.** (2026-09-22,
  EXACT; `scripts/run_move_census.py`, `configs/move_census.json`.) O20 was explained by counting ways
  -- more ways to break a loop than to make one -- and **that explanation was too weak and is replaced
  by this one.** Enumerating every valid single switch: out of a perfect flat sheet at N = 100 and 144,
  **zero** moves add a square and 68 400 / 149 184 lose one; out of a perfect tube at N = 96 and 144,
  **zero** add and 64 320 / 151 776 lose, the cheapest losing move costing exactly 12, which is the
  spark threshold of Q13 seen from the other side. Out of a **melted** graph the picture reverses: 10 254
  moves add a square, and the cheapest of them is **downhill by 75**. So building is not merely rarer
  than breaking; **from order it is impossible in one step, and it becomes both possible and favourable
  only out of disorder.** Curling needs squares added (a tube carries 1.25 a point against a sheet's 1),
  so the consequence for O20 is structural rather than statistical: **energy put into space cannot fold
  it, because the first step of folding does not exist; the only thing one move can do to order is break
  it.** A fold would have to go through a melted intermediate, and the quench of O21 says a cooled melt
  arrives at a jammed defective state rather than a curl. *Ours, unverified, and it is arithmetic rather
  than sampling, so it does not depend on any chain.*

  **CORRECTION to this addendum, 2026-09-23, evening, and a rewording at the author's objection.** (1) **The
  counts above include moves the chain never makes.** `run_move_census.py` enumerated every pair of edges,
  including switches between points on opposite sides; `cqg.run_chain` only swaps partners between two
  points of side 0, and `is_valid` does not check two-sidedness, so nothing refused them. Rerun with the
  chain's moves only (`configs/move_census_chain.json`, `results/move_census_chain.csv`; the original file
  stays): sheet 10 × 10 **0 add, 14 900 lose** (was 68 400); 12 × 12 0 / 34 128; tube 24 × 4 0 / 14 400; tube
  36 × 4 0 / 35 424; melted 5 127 add, 5 377 lose. **Every qualitative statement survives**: no single move
  adds a square to a perfect sheet or tube; the cheapest ways out cost 32 (sheet) and 12 (tube); out of a
  melt the cheapest adding move is downhill by 75. Only the numbers of moves change. Found while tabulating
  the tube's exit moves for the λ scan (PREREGISTRATION T8 draft), whose counts were corrected the same way.
  (2) **"Order can only be built out of disorder" overreaches, and the author's objection is right**: order
  can be built out of a different kind of order. What is exact is narrower: *a single move* out of a perfect
  arrangement cannot add a square. One order is built out of another through a thin seam where squares are
  briefly broken, and T7 measured that seam as thin (at half conversion 98.8 to 99.8 % of points belong to
  one order or the other). The seam is made by the same rule as everything else; "disorder" is the wrong
  word for it. So O20's structural reading becomes: energy put into space cannot fold it *in one step*; a
  fold would have to run through a seam, as the tube's opening does in reverse, and whether it can is the
  local-spark question (T14).

- **O26 The author's first reply, and what it moves.** (2026-09-22, night; private email, paraphrased in
  `docs/outreach/correspondence_2026-09-22_trugenberger.md`; no run.) Three things bear on this file.
  **(1) Q3's cap is disputed by the author** (addendum in the table above). **(2) His current view of the
  order of the transition at λ = 1 is a hybrid transition**: two continuous branches with a jump between
  them, in his own runs at N = 1024 (10,000 sweeps and about 10^7 attempted moves per coupling, 40
  couplings, cold ascent from the previous coupling's final state, 240 sweeps of warm-up). Our equilibrium
  runs at N ≤ 160 (O10, O12, O17) show no jump in either direction. *Ours, unverified:* either the jump is a
  large-N effect our sizes cannot reach, which is what T6's unreached sizes were for, or it is the lattice
  branch surviving past the transition on cold ascent with a short warm-up, which is metastability and
  would not appear at the same coupling on descent. The run that tells them apart is T6 at N = 4p² (196,
  484, 676), both directions, tempering; pre-register before running, with the prediction of
  `correspondence_2026-09-22_trugenberger.md` section "Actions". **(3) Sizes:** N = 4p², p prime, gives a
  unique ground state (his statement); adopt it for the disorder → order track. Of T6's sizes, 36 and 100
  are of that form and 64 is not. Not in this file's scope: S5, which is not met (he has not seen plots or
  code).

- **O27 Gate B check: [T25] Fig. 3 is not the author's continuation procedure trapping the lattice branch.
  The shape is wrong on three counts.** (2026-09-23, EXPLORATORY; a comparison of committed data, no new
  run; `scripts/compare_gate_b_gap.py`, prints only.) On 23 September the author added that starting each
  coupling from the previous coupling's final graph may accentuate the jump by trapping configurations in
  the wrong phase (paraphrased in `docs/outreach/correspondence_2026-09-22_trugenberger.md`, second note).
  If Fig. 3 was made that way, its excess over [KTB19] Fig. 8a at N = 160 should have the shape of the
  excess that our copy of his protocol (T13 protocol P) shows over equilibrium (T13 protocol E) at the
  neighbouring size N = 196. Interpolated in ln g:

  | gap | peak | at g | above 0.10 for g in |
  |---|---|---|---|
  | Fig. 3 heat − Fig. 8a (N = 160, published against published) | +0.41 | 5.6 | 2.2 to 6.2 |
  | Fig. 3 cool − Fig. 8a (N = 160) | +0.38 | 5.1 | 2.3 to 7.6 |
  | Fig. 3 heat − our N = 160 tempering | +0.40 | 5.6 | 2.8 to 6.2 |
  | P heat − E (N = 196, his protocol against equilibrium, both ours) | +0.16 | 3.2 | 2.7 to 3.5 |
  | P cool − E (N = 196) | +0.004 | — | nowhere |

  **(1) Direction.** Trapping keeps a graph in the phase it came from. On descent from a melt that is the
  random phase, which would put the cooling curve *below* equilibrium. Fig. 3's cooling curve is *above*
  Fig. 8a by up to 0.38, and our own descent under his protocol sits on equilibrium to 0.004 at every
  coupling. **(2) Extent.** Our ascent under his protocol leaves equilibrium only below g ≈ 3.5, where the
  lattice can survive, and by 0.16 at most; Fig. 3 sits above Fig. 8a across the whole transition, from
  g ≈ 2 to 6.2 on heating and to 7.6 on cooling. **(3) Position.** Fig. 3 crosses φ = 0.6 at g = 6.2
  (heating) and about 7.0 (cooling, coarsely: only two digitised points lie between g = 6.0 and 9.9);
  Fig. 8a and our N = 160 tempering both cross at 5.2, and every curve of ours at N = 196, his protocol
  and equilibrium alike, at 4.8. Fig. 3's transition is somewhere else, in both directions; it is not a
  trapped version of Fig. 8a's.

  *Ours, unverified.* What moves a whole curve by a factor of 1.2 to 1.35 in g, in both directions, is a
  different normalisation of the coupling or a different size, not a protocol: the crossover drifts *down*
  with N (5.2 at 160, 4.8 at 196 here; O10, TASKS T9), so a curve crossing at 6.2 to 7.0 would belong to a
  size *below* 160. Gate B stays open, and the question for the author narrows to the coupling axis or the
  size of Fig. 3. **What the check does support:** his continuation does at N = 196 exactly what his
  postscript says, an ascent-only tail below g ≈ 3.5 in three of four chains, which is T13's reading (b)
  and the second reading of O26, reproduced in our copy of his protocol.

- **O28 T15 rung 0: INCONCLUSIVE by the letter. Versions exist in the parts; in the whole, only while the
  world is symmetric.** (2026-09-23, exact, pre-registered the same morning with the author's predictions;
  `configs/t15_rung0.json`, `scripts/analyse_t15_rung0.py`, `results/t15_rung0.csv`; PREREGISTRATION T15
  rung 0, no amendment enacted; the table and both post-hoc readings are there.) Renamings that change no
  relationship, kept within sides as in Q15, counted for the twelve saved resting states of T7 amendment 4,
  a perfect sheet, the tube and a melt at N = 64 to 192; every whole-graph count agreed exactly between
  two isomorphism engines. **A melt has exactly one at every size** (prediction 2 holds). **A sheet with a
  defect in it has more than one on the isolated count in 11 of 11 states** (4 to 36,864) **and on the
  whole-graph count in 10 of 11**; the eleventh, three different defects at generic positions, has exactly
  one. The whole-graph renamings are the sheet's own symmetries surviving where the defects sit — they move
  every sheet point, and none but the identity fixes the sheet — so that count is a property of the
  arrangement of the world, not of the object: 2 or 4 for one symmetric defect, 16 or 224 for two identical
  loops placed symmetrically, 1 for three different things. **The leftover types, read from their wiring by
  direct isomorphism:** the four-point remnant is a closed loop of four (Laplacian 0, 2, 2, 4; 4 renamings
  within sides), the eight-point piece of O13's rare states is the 3-cube (0, 2, 2, 2, 4, 4, 4, 6; 24), and
  the rest are an open line of three, single edges and single points; the five spectra are pairwise
  distinct, and prediction 3 fails by the letter only between composition names that differ in d while
  being the same graph. A perfect sheet has 4N renamings when square and 2N otherwise; the tube 2N.

  **For VISION Update 17, plainly** (*ours, unverified*). "Superposition is the set of undetectably
  different versions of the world" survives only for symmetric worlds; the first world with three
  different things in it has one version, as the melt does. What survives is the object-level statement:
  an isolated small loop has versions, and its spectrum labels its structure. The author decided the same
  morning, before this ran, that matter is the structured leftover and not the melt (Update 19); this
  result is consistent with that decision and does not test it. **Not claimed:** that any count here is a
  superposition (rung 1); what the 224 is.

  *Addendum, the same morning, from reading the wiring* (`t7d` N = 144 replica 3, N = 64 replica 25). The
  closed loop of four is **one column of the tube that stayed curled** while the columns round it opened:
  in N = 144 replica 3 it is the original column 3 with its original eight neighbours, now a collar of
  sheet points at d = 2, with the sheet sewn together round it. Every loop edge lies in three squares, the
  loop's own and one to either side. It occurs at three energies at λ = 1.25 — **4, 9 and 14 units** —
  according to whether none, two or four collar edges carry a third square (X = 4, 5, 6 with S − N = 1);
  O16's cold-box remnant is the 14-unit form. So "the four-point remnant" of O13 to O16 is a family of
  three, distinguished by X, and the count "14 units per ring" in O15 is the cold-box member only. The
  9-unit form appears in the state that passes gate 3, the 4-unit form in the one that failed it.

- **O29 The counting picture cannot violate Bell or GHZ: a renaming of a fixed arrangement is a complete
  instruction set.** (2026-09-23, an argument, no run; PREREGISTRATION T15 rung 3a, its reading; *ours,
  unverified*, unreviewed.) Under VISION Update 17 a version is a renaming that changes no relationship
  and a measurement is an interaction that splits the versions into classes. Rung 3a was pre-registered
  with the author's prediction (strongly contextual) and the definitions were then worked through for
  what any arrangement gives. Every renaming that keeps the loops in place either fixes or swaps each
  loop's side-0 pair and each loop's side-1 pair, so it assigns an outcome to every setting of every loop
  at once; the support of a context is the set of colour triples those renamings give at that context's
  setting points; attaching detectors changes which renamings survive, hence the classes, never the
  colours. So an instruction set exists for every arrangement (**CLASSICAL** for GHZ) and, with
  equal-weight namings, every probability is a mixture over instruction sets (S ≤ 2 for CHSH). **The
  naming is a hidden variable in Bell's sense, and Bell's theorem applies.** Two smaller facts found on
  the way, both exact: two loops whose edges all carry three squares cannot be joined by an edge under
  the hard-core rule, and a symmetric triangle of loops cannot be linked by edges (parity); both are in
  the pre-registration. **What survives of Update 17:** rungs 0 to 2, which are about the counting and
  not about Bell; and interference (rung 4), which was always going to need a dynamical rule. What does
  not survive is the claim that counting the versions of a fixed arrangement reproduces quantum
  correlations; the brief's section 5 said in advance that this ends the quantum leg as stated.

- **O30 T15 rung 0b: the closed loop of four is not a resonator inside the sheet. INCONCLUSIVE by the
  letter; the prediction fails.** (2026-09-23, exact, pre-registered with the author's prediction the
  same afternoon; `configs/t15_resonator.json`, `scripts/analyse_t15_resonator.py`,
  `results/t15_resonator.csv`; PREREGISTRATION T15 rung 0b, the table is there.) The Laplacian of each
  saved state holding a loop of four, its eigenspaces, and the most weight any mode of an eigenspace can
  carry on the loop's points (the top eigenvalue of the projector restricted there). Gates pass: 1.000
  on the isolated loop at 2 and 4, 0.444 at most on a 12 × 12 sheet, below 0.5 for every random
  eight-point set. **Six states of seven: DISSOLVED**, no mode above 0.25 on the loop and most within
  twice an even spread; **one: RETUNED at the threshold** (0.511 and 0.501, where random sets reach 0.472
  in the same, 224-fold symmetric state). The loop's vibrations at 2, 2, 4 do not survive embedding;
  eigenvalues near 2 and 4 in the whole spectrum belong to the sheet. **Beside, post-hoc:** with the
  collar included the cap resonates in two states of seven (0.946 at 2.79 and 5.21 at N = 144 replica 5;
  0.670 at 0.16 and 7.84 at N = 64 replica 25), at frequencies that are not the loop's; the 3-cube reaches
  0.36 at most. **For Update 17:** "a particle is an allowed vibration of a small closed loop" fails in
  this model as stated, whatever rule combines amplitudes; if any object here is a resonator it is the
  curled column with its collar, sometimes. Whether to redefine the object is the author's call. A
  process fault is recorded in the pre-registration: the timestamp commit carried a failing test, on a
  wrong assumption about an 8 × 8 sheet, hidden by a truncated test log; the gate at 12 × 12 was never
  in doubt.

- **O31 The correlation length of [KTB19] Fig. 9a is not reproduced; nothing in the fluctuations grows
  with N.** (2026-09-23, night; PREREGISTRATION T16, a measurement at the model author's request,
  exploratory with respect to the hypothesis.) Eq. (4.15) as written (Q19), his procedure at N = 196, 484,
  676 and replica exchange at 196: **NONE** by the pre-registered reading. C(r) falls to about zero within
  two steps at every coupling from g = 12 to 1.5 and every size; the susceptibility N var(S/N) peaks at
  0.18 at every size while its position moves down with N; ξ / diameter by the formula is dominated by
  distances near the diameter and by snapshots with C(r) just below 1, which is Kelly's warning seen in
  data. Replica exchange at 36 and 100 fails the swap-rate ceiling the assistant copied from T13; dropping
  it (proposed, not enacted) changes no verdict. *Ours, unverified:* a smooth crossover at these sizes,
  neither the continuous nor the first-order signature.

- **O32 Counting with interchangeable points does not pull identical defects together.** (2026-09-24,
  EXACT, exploratory; series paper 5; `configs/exact_pair_symmetry.json`, `scripts/exact_pair_symmetry.py`,
  `results/exact_pair_symmetry.csv`; the expectation was written in the config before the run.) Two copies of
  the flat sheet's cheapest break, placed at 18 separations in a 12 x 12 torus. Every placement has the same
  energy (140 squares), so the only difference interchangeable points can make is the symmetry count A, the
  placement's weight. **A is 1 or 2 at every ordinary separation, set by orientation and not by distance (2 at
  (2,0), (4,0), (8,0), (10,0); 1 at every odd and diagonal shift), and 4 only at the three exactly opposite
  placements (6,0), (0,6), (6,6).** So the counting makes no force that grows as defects approach; its only
  preference is a factor of 2 for sitting exactly opposite, i.e. for maximum separation. *Ours, unverified:*
  this is a clean negative for the simplest version of "gravity as the wish to refold" by counting, at fixed
  wiring. **Limits, stated plainly:** one simple local defect, not the leftover column; one torus size; fixed
  wiring, so nothing here says what happens when the defects' surroundings are allowed to rearrange (that is
  an entropic force of a different kind, which the interchangeable chain of Q20 can now measure).

- **O33 T17: more seeds, more leftovers, but fewer than one each (BETWEEN).** (2026-09-24; PREREGISTRATION T17;
  `results/t17_seeds_k{1,2,4,8}.csv`; `scripts/analyse_t17.py`.) A 96 x 4 tube at λ = 1.25 in a cold sealed box,
  k seeds planted as move A at evenly spaced columns, twenty runs per k, all converting, energy exact. Leftovers
  per tube 1.10, 2.15, 2.50, 3.40 at k = 1, 2, 4, 8; slope 0.288 ± 0.039 per extra seed, BETWEEN by about one
  standard error. **For the owner's dark-matter picture (VISION Update 16), plainly:** the amount of scrap does
  depend on how the change started, which T10 alone could not show, and which "one per tube" would have ruled
  out; but it is not one scrap per seed, and the growth looks less than proportional. *Ours, unverified:* where
  fronts from neighbouring seeds meet, their leftovers may merge or anneal; that was not measured and is the
  next question (the saved end states hold the positions).

- **O34 T18: the room a new space needs grows faster than its lump (PROPORTIONAL, R = 6).** (2026-09-24.) One seed
  in a sealed 24 x 4 tube, ten bath sizes, λ = 1.10, 1.25, 1.40: the smallest bath giving a majority of clean
  sheets is 12, 36, 72 stores. The lump grows as 4(λ − 1), the room needed faster (C* / [4(λ − 1)N] = 0.31, 0.375,
  0.47). For the owner's fertile window: a larger λ gives a larger lump and a harder birth.
- **O35 T19: the leftover anneals away at fixed temperature.** (2026-09-24.) At g = 1.0, 1.25 and 1.5 every followed
  leftover was gone within 500 to 80,500 sweeps; two moved first at g = 1.5. It lasts only in a cold box (T10). For
  the owner's dark-matter picture: in this model the scrap is permanent only if its surroundings stay very cold.
- **O36 T21: a sealed sheet given energy melts, not folds, even with interchangeable points (at N = 64).** (2026-09-24.)
  The fair version of O20, run with the fast count (Q20): MELTS EITHER WAY at N = 64 under both protocols and at
  N = 36 under the single demon; at N = 36 under the bath, a fragile lean towards folding with interchangeable
  points (three damaged replicas at one budget, reversed at the next). The owner's closed-region fold is not seen
  where complete folds exist. Not tested: a local push into cold surroundings.
- **O37 T15 rung 1: the time spent in each arrangement equals its share of the count (AGREES).** (2026-09-24.)
  Validation at N = 16 and 18, both routes, total-variation distance at most 0.0125. The counting half of the
  owner's quantum picture now has a validated tool; it says nothing yet about quantum behaviour.

- **O38 T8, the λ map: sharp wherever the tube is stuck; INCONCLUSIVE by the letter.** (2026-09-24; PREREGISTRATION
  T8.) From λ = 1.05 to 1.35, at N = 64 to 192, the curled torus is stuck for now and its change is a front with
  the two orders side by side (95 to 100 % of vertices at d ∈ {1, 2} at half conversion; one piece holding 76 to
  100 % of the converted part); the release is exactly 4(λ − 1) where the flat torus is reached. It is not stuck
  at 1.40 or 1.45; the edge lies between 1.35 and 1.40. Waiting times follow Eq. (2) with nothing fitted over two
  decades, 15 to 43 % longer near λ = 1. At fixed coupling, near λ = 1 no decay leaves a leftover, and the share
  that does rises with λ. The verdict is INCONCLUSIVE because the memoryless-wait criterion was too tight at
  thirty decays per cell (about ±2 standard errors, 28 cells) and the energy gate fails at 1.35; a computed
  repair changes no verdict and is not proposed.
- **O39 T22: the first exit is on time; about a third of exits fall back, at every λ (FALL-BACKS by the letter).**
  (2026-09-24; PREREGISTRATION T22.) Counting every accepted move in forty decays per cell (λ = 1.05, 1.10, 1.25;
  N = 64, 96; g = 1.5): the time to the first exit from the perfect curled torus agrees with Eq. (2) in all six
  cells, each within one standard error. Exits per decay are 1.48 to 1.80, so a share of 0.56 to 0.68 go through
  (the transmission coefficient κ), with no trend in λ. Recrossings therefore do not explain T8's excess near
  λ = 1 (O38), and the direct measurement does not reproduce that excess at N = 64 and 96. Our reading is that the
  excess was statistical, 1 to 1.4 standard errors per cell. Our quantitative prediction failed (a share of 0.70
  to 0.87 at 1.05, and E ≈ 1 at 1.25).
- **O40 A gas of fully curled knots is not stuck at any λ > 1 in 2D (exact).** (2026-09-24;
  `scripts/knot_gas_exits.py`.) Asked before pre-registering the author's rule that all directions curl together:
  every single move out of a gas of 4-cubes (k = 2 and 4, N = 32 and 64) was listed and priced. There are two
  kinds, and the rates per sweep are the same at both sizes. A move **inside one knot** has ΔS = −2 and ΔX = −8,
  costs 32 − 32λ, and is offered 3 times per sweep: it is **downhill for every λ > 1** (−8 at λ = 1.25). A move
  **joining two knots** has ΔS = −6 and ΔX = −20, costs 96 − 80λ (−4 at 1.25; downhill above λ = 1.2), and is
  offered 32 and 96 times per sweep at the two sizes. So above λ = 1 the fully curled state has no wall at all. It
  falls apart everywhere at once, with no waiting and no seed: spinodal, not a burp. It is stuck only below λ = 1,
  where it is the ground state. **In the 2D model, the only curled state that is stuck for now above λ = 1 is the
  partial one**, the curled torus, with one direction curled and one open: the state the author's rule forbids.
  Whether the same holds in 3D is the first exact question for the six-link model (VISION Update 22).

## Provenance

Code and documents were drafted with Claude (Anthropic) in conversation with the
author and should be disclosed as such in any submission. Physics estimates marked
"Ours" originated in that conversation and have not been reviewed by a physicist.

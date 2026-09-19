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
| Q1 | Energy H = 16(N − S) once no edge carries more than two squares; general form 4·Σ_e(2 − S_e)₊. | Derived by us from the edge-curvature formula [T22] Eq. (2) at D = 2 on bipartite graphs. Matches the global term of [T24] Eq. (4) and the D = 2 mean-field action of [KTB19]. | Ours, cross-checked on two limits (random graph 16N, flat torus 0) |
| Q2 | On bipartite graphs the hard-core rule is equivalent to "no two vertices share more than two neighbours" (no K₂,₃). | Rule: [T22], [T24]. Equivalence: ours. | Ours; consistent with the text definition in [T25] ("any two cycles can share at most one edge", for triangles, squares, pentagons). Figure of excluded subgraphs ([T25] Fig. 1) not inspected. |
| Q3 | ~~No edge may carry more than 2 squares (hard cap).~~ **Superseded.** [T25] Sec. "Cycle condensation" describes the published model as using the *full* Hamiltonian, Eq. (22): the global term plus a **soft local term that penalises** edges with more than 2D−2 squares, with no hard cap. It states that the two effects "cancel exactly" so that denser configurations are "degenerate" with the torus, which confirms our Q1 coefficient and our 4-cube tie. It also states: global term only → **first-order** transition into isolated hypercubic complexes ([KTB19], [GV21]); full Hamiltonian → **continuous** transition. | [T25]; our first-look code | **Our first look simulated a third variant (global term + hard cap), which is neither of the two published cases.** Its results do not yet test the published claims. To do: implement the local term, remove the cap, rerun. |
| Q4 | Move = bipartite edge switch; symmetric proposal; invalid states rejected. Connectedness not enforced. | "Edge switches": [KTB19] Sec. 4. Details: ours. Detailed balance: [NB99]. | Ours. Ergodicity in the constrained space unproven (O2). |
| Q5 | Start from an lx×ly torus, both sides even and ≥ 6, melted at infinite temperature. A side of 4 is refused: it closes a 4-cycle around the torus, so half the edges carry three squares and S = 1.25 N. | Ours. | Ours; melting is tested (`test_melts_at_infinite_temperature`), the 16×10 case in `test_rectangular_torus`. The side-of-4 statement was checked by brute force with networkx on 4×6 and 4×10. |
| Q6 | Error bars on φ and on the fluctuation measure N·var(φ): block bootstrap over 20 blocks of sweeps, 500 resamples (columns `phi_err`, `chi_err`). Beside them, the integrated autocorrelation time τ in sweeps (`tau_int`), summed with an automatic window that stops at the first t ≥ 5τ. | Block bootstrap: same choice as A8, [NB99]. Windowing rule: [S97], **from general knowledge, not read by us**; the factor 5 is a conventional value, to verify. | Ours, tested on series with known answers (`tests/test_analysis.py`). **Limits:** the error bars hold only where a block (n_meas/20 sweeps) is much longer than τ. Where the chain is freezing they are underestimates, which would make heating and cooling look *more* different than they are, i.e. it would fake hysteresis. `tau_int` is a lower bound when the series never decorrelates, and NaN when the chain did not move at all. Twenty blocks and one replica is a first-look choice; the pre-registration (T7) must fix the production choice. |
| Q7 | Random seeds. "legacy": config seed + 100000·replica + L + step, the formula of the first look. "independent": one seed per (config seed, lx, ly, replica, step) drawn through numpy's `SeedSequence`, which is built to turn such a tuple into statistically independent streams. | Ours. `SeedSequence`: numpy documentation, from general knowledge. | Ours, tested (`test_seed_schemes`). **Known flaw of "legacy":** it reuses seeds across sizes (L = 10 at step 5 and L = 14 at step 1 get the same one), so runs at different sizes are not strictly independent. The effect on the first look is expected to be negligible, since the same random numbers drive different systems, but it is not measured. "legacy" stays the default only so that `cqg_first_look` reproduces bit for bit (T2 regression); it refuses rectangles. **Every new config should say `"seed_scheme": "independent"`.** |

### First look (2026-09-19, `configs/cqg_first_look.json`; one replica, short runs, NOT publication quality)

- A crossover from random (φ = S/N near its finite-size floor) to ordered (φ → 0.9+) exists, as published.
- **The crossover moves with system size.** Coupling at which φ = 0.5: g = 7.64, 5.51, 4.34, 3.51 for N = 100, 196, 400, 900. Against ln N, 1/g rises almost linearly with slope ≈ 0.07. The plain energy-versus-entropy count (16 energy units per node against ≈ ln N entropy per node for 4-regular graphs; same argument as [K08] Eq. (43)) predicts 1/16 = 0.0625. [T22] states the D = 2 critical coupling does not depend on N. **Until Q2–Q3 are verified and the published curve is compared directly, this is a discrepancy to investigate, not a finding.**
- No hysteresis between cooling and heating in the crossover region. Small differences appear only at g ≤ 3 where acceptance is below 1 %, i.e. the chain is freezing.
- The peak of the fluctuation measure N·var(φ) is ≈ 0.16 at every size. No sharpening with N, so at these sizes there is no sign of a first-order transition, and no sign of a sharpening critical point either.
- **Independent check passed:** the hot-phase floor of φ matches the Poisson prediction (2D−1)⁴/4 = 20.25 squares regardless of N quoted in [T25]: predicted 0.2025, 0.1033, 0.0506, 0.0225; measured 0.198, 0.106, 0.053, 0.024 for N = 100, 196, 400, 900. *(Qualified later on 2026-09-19, see O5: these were measured at g = 200, not at infinite temperature, and the agreement is a few per cent with a trend in N, measured/predicted running from 0.98 to 1.07. "Passed" overstates it.)*
- **The gate is now concrete** ([T25] Fig. 3): S/N against log g at **N = 160**, cooled from random and heated from the torus, no hysteresis, random-phase floor 0.126. Needs a rectangular torus (e.g. 16×10) and the full Hamiltonian (see Q3). **Not yet passed.**
- The published curve is for a single size, so our drift-with-N observation is neither confirmed nor contradicted by it. [T25] does not discuss N-dependence of the 2D critical coupling.

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

## Provenance

Code and documents were drafted with Claude (Anthropic) in conversation with the
author and should be disclosed as such in any submission. Physics estimates marked
"Ours" originated in that conversation and have not been reviewed by a physicist.

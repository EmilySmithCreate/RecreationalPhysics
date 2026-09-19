# Tasks, in order

Each task has an acceptance test. Do them in order; do not start a task whose predecessor's gate has not passed. When a task is done, tick it here in the same commit.

Notation: N vertices, S total squares, S_e squares on edge e, φ = S/N, g coupling (acts like temperature), λ strength of the local term. D = 2 throughout (4-regular bipartite graphs).

## T1. Rectangular torus  ☐

`torus(side)` only builds L×L. Add `torus(lx, ly)` (both even). Needed because the published curve is at N = 160 (e.g. 16×10).

Accept: tests for 16×10: 4-regular, bipartite, S = N, every S_e = 2, `is_valid` true.

## T2. Full Hamiltonian with the λ knob  ☐

Replace the hard cap by the soft local term (ASSUMPTIONS Q1, Q3; [T25] Eq. 22):

    H = 16 (N − S) + 4 λ Σ_e (S_e − 2)₊

- Make the cap optional (`cap=None` means no cap). Keep the hard-core rule (no two vertices with more than two common neighbours). With the cap off, allow small tori again (the 4×4 torus is the 4-cube Q4).
- The move changes S_e on every edge of every lost or gained square. Simplest correct approach: collect the affected edge set (edges of all squares through the two removed edges before the move, and through the two added edges after it), evaluate the local term on that set before and after.
- Offer both acceptance rules: Metropolis, and Glauber p = 1/(1 + exp(ΔH/g)) as in [T25] Eq. 28. Both satisfy detailed balance.

Accept:
- Q4 (4×4 torus, N = 16, S = 24, every S_e = 3): H = 0 at λ = 1 and H = −128 at λ = 0.
- Flat torus: H = 0 for every λ. Melted large graph: H ≈ 16N.
- Incremental ΔH equals full recomputation after 10⁴ random moves at λ ∈ {0, 0.5, 1}.
- λ = 1 with `cap=2` reproduces the existing capped results bit for bit (regression).

## T3. Connectivity observables  ☐

Number of connected components, size of the largest, and a census of isolated Q4 components. Needed to detect the published "shattering into hypercubes" at λ = 0 and to check success condition S4 (a connected space).

Accept: unit tests on hand-built graphs (one torus; two disjoint tori; a torus plus a Q4).

## GATE A. Reproduce the published λ = 0 behaviour  ☐

Published: with the global term only, the transition is first order and the graph decomposes into isolated hypercubic complexes ([T25] "Cycle condensation"; [KTB19]; [GV21]).

Accept: at λ = 0, several sizes, cooling and heating: hysteresis around the transition, and a cold phase dominated by Q4 components. If this does not appear, stop: either our model reading or our sampling is wrong.

## GATE B. Reproduce [T25] Fig. 3 at λ = 1  ☐

Published: N = 160, φ against log g, cooled from random and heated from the torus, no hysteresis, random-phase floor 0.126.

Accept: floor 0.126 ± 0.01; heating and cooling agree within errors through the crossover; cold end above 0.9 when heated from the torus. **Human step for Emily:** open arXiv:2512.17676 Fig. 3 and compare the position of the rise by eye; record the comparison in ASSUMPTIONS section D. If the figure's axis cannot be matched, write to the author rather than guessing.

## T4. Ergodicity check  ☐

For the smallest sizes that admit valid graphs, enumerate the configuration space exhaustively and confirm the move set connects it (or document which parts it cannot reach). Add the "neighbourhood swap" move of [T25] Fig. 8 if needed.

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

## Later

Scorecard against "the spot" (VISION step 4): spectral dimension, volume-growth dimension, curvature uniformity, shortcut census, stability under perturbation. Allotrope ladder of [T24]: does squares-per-vertex move in jumps with hysteresis?

## Before anything is shown to anyone

VISION S5: a physicist reads it. Draft a short, honest note to C. Kelly, F. Biancalana or C. Trugenberger once Gates A and B have passed: what was reproduced, what was not, the code link, and a request for a sanity check.

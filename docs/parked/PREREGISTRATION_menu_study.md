# Pre-registration (DRAFT – commit this before running any Phase B simulation)

The git commit that contains the final version of this file is the timestamp.
No Phase B configuration may be run before that commit. Edits afterwards must be
new commits that say why.

## Question

Graphity-type models let any vertex link to any other. That makes the disordered
phase's entropy grow like N ln N, so the transition temperature falls to zero as the
system grows ([K08] Eq. 43; [CP12] Sec. IV C). Does restricting the *allowed* links
to a fixed menu cure this, and at what price?

## Gate: Phase A must pass first

Reproduce [K08] Sec. IV A 3 with the complete-graph menu:

- G1. No state with energy per node below −12.21 is ever found at r = −2.5.
- G2. Specific-heat maxima at β = 0.13, 0.16, 0.17, 0.18 (N = 60, 120, 180, 240), each within ±0.015, averaged over ≥ 4 replicas.
- G3. Heating and cooling sweeps agree within errors above the transition (equilibration check).

If G1–G3 fail after parallel tempering is added, the project stops and the write-up
is a failed-reproduction note.

## Predictions

- **P1 (random menu, fixed K).** For K ∈ {4, 5, 6} and N from 10² to 10⁴: the lowest energy per node found shrinks roughly like 1/N at fixed K, and never exceeds the bound `random_menu_energy_bound(K) / N` (K = 4: 627/N; K = 5: 4286/N; K = 6: 21098/N, at r = −2.5, L_max = 9) by more than sampling noise. No specific-heat peak sharpens with N. Basis: ASSUMPTIONS C1–C2. Note the bound only becomes small once N ≫ (K−1)^L_max, so K ≥ 8 cannot be tested at sizes we can reach and is excluded.
- **P2 (lattice menu).** For d ∈ {2, 3, 4}: a specific-heat peak exists and its position changes by less than 5 % between the smallest and largest N, while the complete-menu peak moves by more than 25 % over the same range of N. Basis: C4.
- **P3 (interpolation).** Lattice menu plus a fraction p of random extra allowed links per vertex: β_c rises smoothly with p. No quantitative prediction; exploratory, and will be labelled as such.

## What would count against us

- P1 fails (a sharpening peak appears on a random bounded menu) → the counting argument is wrong or the move set is not sampling properly. Report it.
- P2 fails (peak still drifts on a lattice menu) → the entropy argument is incomplete. Report it.
- Ergodicity test O2 fails → Phase B results are not interpretable until the move set is fixed.

## Not claimed, whatever the outcome

Nothing about the real universe, Lorentzian time, the number of dimensions, inflation
or dark matter. The result concerns one class of Hamiltonians (rewards for cycles of
bounded length) at finite N.

## Analysis fixed in advance

Observable: C/N² from energy fluctuations; peak located by a quadratic fit to the three
highest points; errors by block bootstrap over replicas. Seeds, sizes and temperatures
are in `configs/`. Every figure is produced by a script from the archived CSV files.

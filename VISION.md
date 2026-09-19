# Vision and plan

This page is the fixed reference. Changes to it are deliberate commits that say why.
Source keys refer to `REFERENCES.bib`; assumption numbers refer to `ASSUMPTIONS.md`.

## The hypothesis (author's, in plain words)

1. Our spacetime is a stable phase of something deeper, called X.
2. We know this phase's rules well: general relativity, special relativity, quantum mechanics. Any candidate for X must end up reproducing them. *(This is the standard bar for every quantum-gravity approach; none has cleared it.)*
3. X and our spacetime are two arrangements of **one underlying system with one underlying relational quantity, F**, which says which arrangements are favoured. F need not be energy as we know it. In X it is a measure of relational pattern (closeness or connectedness among degrees of freedom, possibly built from several such measures for different classes of degrees of freedom). Energy in the familiar sense exists only in the spacetime phase, where differences in F show up as energy and mass. *(This is how the models already work: the "energy" of a graph is a count of loops, a purely relational number with no units; [T25] Introduction argues that energy, length and speed are all emergent and only a dimensionless coupling is fundamental, and its Eq. (45) converts a free-energy difference of the network into curvature and mass.)* What claims 4–6 need is only that F is a single comparable number across X and spacetime, so that "more stable", "released" and "conserved" have a meaning. They share a base, but their working descriptions need not resemble each other: between X and spacetime, degrees of freedom may merge (many act as one), split (one acts as many), convert type, freeze (hidden dimensions), or be left over (the remainder in claim 5). X is the more symmetric, higher-energy arrangement. *(Precedent for type conversion inside this model family: link variables reorganising into photon-like gauge fields, [KMS06] Sec. IV.)* The count at the base level may be fixed or may vary. What matters is that **one energy function covers every configuration**, including configurations with different counts (precedent: dynamical triangulations, where the number of building blocks varies and the cost per block plays the role of the cosmological constant; Ambjørn, Jurkiewicz and Loll, arXiv:hep-th/0105267, not read by us, from general knowledge). Claims 4–6 lose their definitions only in models that have *no* energy function and are defined purely by a growth rule (e.g. causal-set sequential growth; Rideout and Sorkin, arXiv:gr-qc/9904062, not read by us). Steps 2–3 use a fixed count because the published model does; a varying count is parked. *(Corrected 2026-09-19: an earlier version wrongly said a varying count by itself removes the meaning of claims 4–6.)*
4. A phase change in X produced our phase. It was **first order**: it released a bounded lump of energy (Δρ) that became matter and radiation.
5. What did not convert remained as hotter X, or snapped into another discrete arrangement, X2.
6. Across the transition an energy-like quantity is conserved, which is what makes "energy released" meaningful. After spacetime exists and expands there is no global energy bookkeeping, as in standard general relativity.

Claims 1–6 accepted by the author on 2026-09-19.

Status: a hobbyist's hypothesis. Items 4–6 are untested ideas. Nothing here has been reviewed by a physicist.

## What success means (author's bar)

An existence demonstration: at least one model in which the mechanism of claims 3–6 demonstrably happens, and which nobody qualified has shown to be wrong. The conditions are fixed here, before any run, so that the bar cannot move afterwards.

- **S1 No cherry-picking.** We may explore a *family* of energy functions, but only along knobs fixed in advance, and we publish the whole map: every setting run, including those that give the answer we did not want. A single member of the family is never presented on its own. *(Reworded 2026-09-19 from "No tuning", after agreeing that the useful question is which ingredients force a first-order transition.)*
- **S2 First order.** At the largest sizes we can reach, the energy histogram at the transition has two humps and the valley between them deepens as N grows; heating and cooling runs show hysteresis.
- **S3 Sealed split.** At fixed total energy the system separates into an ordered region plus a hotter remainder, and the energy released per converted node is measured.
- **S4 On the spot.** The ordered region passes the geometry and stability lines of the target below.
- **S5 Someone qualified has looked.** "Nobody has proved it wrong" only counts if a physicist has actually read it. Silence from people who never saw it is not evidence.

Precedent: [CP12] already reports a first-order transition with a nucleation barrier into a nearly two-dimensional phase with defects, so S2 has been met once in a related model. S3 and S4 have not been done in any model we have found.

If S2 fails in Trugenberger's model, that is a result too: the hypothesis does not live there, and the write-up says so.

## The working question

**Which ingredients of F force two dips (first order, latent heat), and which remove them (continuous)?**

The mathematics of "requiring two humps": if φ is the order parameter (squares per node), the probability of finding the system at φ is P(φ) ∝ exp(−N·f(φ)/g), where f is the cost per node including entropy. Two humps in P means two dips in f. The smallest f with two dips is f = aφ² − bφ⁴ + cφ⁶ with b > 0, the same potential as in the author's original 10-step plan; with the opposite sign of the φ⁴ term there is one dip and the transition is continuous. The changeover is a tricritical point. Because N multiplies the exponent, a small barrier per node becomes an overwhelming one in a large system, which is why the valley deepens with N. *(Landau theory; textbook material, e.g. Chaikin and Lubensky, not re-read by us.)*

Building a model that must give two humps and then finding two humps would prove nothing. Mapping which ingredients decide the order is a real result.

**First knob, fixed in advance: λ, the strength of the local term.** H = H_global + λ·H_local, with H_global and H_local as in [T25] Eq. (22).

- λ = 0: square count only. Published: first order, graph shatters into isolated hypercubes ([T25]; [KTB19]; [GV21]).
- λ = 1: the full Ollivier curvature. Published: continuous, a surface forms ([T25]).
- 0 < λ < 1: not a curvature any more, only an interpolation between the two. Unexplored as far as we know. The question is where the order changes, and whether any λ gives first order *and* a connected space (conditions S2 and S4 together).

Why the local term is there at all: it was not added as a design choice. It is what the Ollivier curvature does by itself. That curvature compares the cost of moving one node's neighbours onto the other's; once an edge carries 2D−2 squares every neighbour already has a partner one step away, so further squares cannot lower the cost and the curvature saturates at zero (the [·]₊ brackets of [T25] Eq. (8)). "Global plus local" is bookkeeping for "linear reward, then saturation" ([T25] Eqs. (9), (10), (22)). Ollivier curvature was chosen because it is the one graph curvature proven to converge to the Ricci curvature of general relativity ([T25], section on convergence). So in this family the ingredient that removes the two dips is the same ingredient that makes the energy faithful to general relativity.

**Preferred measurement: the entropy curve.** Instead of histograms at one temperature, measure s(φ), the log of the number of arrangements at each φ, directly (Wang–Landau sampling [WL01]). A dent (a stretch where s curves upward) means first order; the dent's width is the latent heat and its depth the barrier. No dent means continuous. One measurement covers all temperatures, and it is the natural quantity for the sealed, fixed-total picture of claim 6.

## The root question

**Does geometry form through a first-order transition with a latent heat, or a continuous one?**

Items 4 and 5 stand or fall on it. First order → a latent heat exists, so Δρ has a home. Continuous → no latent heat, and the rival picture below is the one the models support.

## How this differs from Trugenberger's combinatorial quantum gravity

Shared starting point: spacetime is a phase of graph-like degrees of freedom [Trugenberger23; KT19].

| Question | Trugenberger | This hypothesis |
|---|---|---|
| Order of the transition | Continuous; the critical point *is* the Big Bang and supplies the continuum limit [Trugenberger23 Sec. III] | First order, with latent heat |
| Where matter comes from | Matter *is* leftover bubbles of the random phase; its energy is excess curvature [Trugenberger23 Sec. I] | Matter comes from the released energy; the leftover is a separate remainder (hot X or X2) |
| What drives expansion | Geometry alone: negative curvature behaves like de Sitter space [T22; T23]. Since 2024 he also describes an inflation-like burst at emergence ("topological inflation"), caused by very high curvature near the critical point, not by released energy [T24, Dark energy section] | Released energy (inflation-like epoch, then reheating) |
| Time | An absolute universal time that is not geometric; the time of relativity emerges later, at large scales [T23] | Same choice: X has its own ordering; our time is emergent (claim 6) |
| Dark sector | Dark energy = leftover curvature of the ground state. Dark matter = long-lived metastable "allotropes": regions of spacetime stuck in a different discrete arrangement (fewer squares per vertex), like diamond surviving where graphite is stable [T24] | X2: a discrete alternative arrangement that gravitates. **Close to his allotropes.** Difference: his are *less* stable than space and left behind; X2 was proposed as *more* stable than X |
| What changes over cosmic history | The coupling runs; more and more matter turns into spacetime [Trugenberger23 Sec. I] | A sealed system with a conserved energy-like quantity |
| Entropy problem | Rescale the coupling with system size, giving an area law [KTB19 Sec. 3.1.1] | X has structure (bounded partners), so entropy is extensive (ASSUMPTIONS B1, C4) |

The two pictures make **opposite predictions about one measurable thing**, the order of the transition. The published evidence for "continuous" is one correlation-length plot at N ≈ 200, which its authors call a "reasonable indication" in 2D and say falls short of a finite-size-scaling analysis [KTB19 Sec. 4–5]. A simplified version of the same model (local terms dropped) is first order with hysteresis, per a second group [GV21, abstract only]. So the question is open, and it discriminates.

Update 2026-09-19: [T22], [T23] and [T24] have now been read in full. What they add:

- He still takes the transition to be continuous, but says so conditionally: he proceeds "assuming that its nature can be further cemented by large-scale numerical simulations presently out of reach of the available computational resources" [T22, Introduction]. His largest graphs are N = 2000 in 2D and N = 500 in 3D [T22]. So the test in step 3 is one he has named himself.
- [T24] contains no simulations ("no datasets were generated"). The allotrope picture of dark matter is an argument, not yet a numerical result.
- *Ours, unverified:* long-lived metastable domains and a free-energy minimum that switches between discrete levels (1, 2, 3, 4 squares per vertex) as the coupling falls are the usual signature of **first-order** behaviour, yet [T24] attributes them to a continuous transition. If those switches are real, each would be a first-order step with its own latent heat. That gives Δρ a possible home even if the first transition (random to geometric) is continuous.
- He states that general relativity has not yet been derived in the large-scale region [T23], and that numerical work has only been possible in 2D [T23, footnote].
- The programme is now built on the **2D** model: a negatively curved surface acting as a holographic screen, with 3+1 appearing as the large-scale random-walk dimension [T23; T24]. So D = 2 is the physically relevant case in his own terms, and it is the cheap one to simulate.

Update 2 (2026-09-19): [T25], a full review published December 2025 (arXiv version April 2026), was pointed out by the author and read in full. What it adds:

- **The order of the transition depends on one term of the energy.** Global term only: first order, but the graph breaks into isolated hypercubes, not a space. Full Hamiltonian (with the local penalty): continuous, and a surface forms [T25, Cycle condensation]. So a first-order version of this model exists, but it does not produce geometry. For this hypothesis that is a tension between success conditions S2 (first order) and S4 (on the spot) inside this model family, and it has to be faced, not avoided.
- Our first-look simulation used a hard cap instead of the local penalty, so it matches neither published case (ASSUMPTIONS Q3). Step 2 continues: implement the full Hamiltonian, reproduce [T25] Fig. 3 at N = 160.
- Black holes in [T25] are large bubbles that have reverted to the random phase. That overlaps the parked idea of black holes as phase changes.
- Einstein's equations are obtained there as constitutive relations by a uniqueness argument, "still at a qualitative level" in the paper's own words.
- The heaviest published runs (N = 2000) are reported to need months of CPU time per size.

## The target ("the spot")

What a simulated geometric phase is scored against. Measurable on a graph today:

- random-walk (spectral) dimension and volume-growth dimension at large scale
- flatness (average Ollivier curvature near zero)
- uniformity (every region looks alike)
- locality (almost no long-range shortcuts)
- stability (survives perturbation and mild heating; hysteresis width)

Partly reachable: general relativity. Trugenberger's energy function is a graph version of the Einstein–Hilbert action and converges to it on suitable graphs [KTB19 Sec. 3.1; Trugenberger23 ref. 33]. Konopka's loop-counting energy [K08] has no tie to gravity. By the hypothesis's own criterion, Trugenberger's model is the real test bed; Konopka's was the training ground.

Out of reach for now, and stated openly: special relativity / Lorentz symmetry (the models have no time; [CP12 Sec. VI]), quantum behaviour (simulations are classical).

## Plan

| Step | What | Tests which claim | Status |
|---|---|---|---|
| 1 | Learn the diagnostic (energy histogram at the transition) on the existing Konopka model | tooling only | Done at N = 60: one broad hump, inconclusive, as expected at that size |
| 2 | Build Trugenberger's model. Gate: reproduce the published square-density curve [KTB19 Fig. 8, D = 2] | none yet; establishes trust | Kernel built and tested; first look run. **Gate not yet passed**: published curve not yet compared, two model-reading assumptions (Q2, Q3) unverified. The crossover is seen to drift with ln N, which needs explaining first |
| 3 | Map the order of the transition along the knob λ (see "The working question"), using the entropy curve s(φ). Then run it sealed (fixed total energy). Does it split into an ordered region plus a hot remainder? Energy released per node? Repeat at growing N. Also: as the coupling is lowered further, does the typical squares-per-vertex move in jumps with hysteresis (the allotrope ladder of [T24]) or smoothly? | 4, 5, 6 | |
| 4 | Score the resulting phase against the spot. Do domains of a different arrangement persist, and for how long? | 1, 2, 5 | |

Rules:

- We do not move past a step until it is done.
- A new idea goes to the parked list unless it bears on steps 2–4.
- Predictions are committed before the runs that test them (`PREREGISTRATION.md`, task T7).
- Every assumption has a source or is marked "Ours".

## Parked

Lorentz symmetry; quantum behaviour; why 3+1; hidden dimensions; inflation numbers (e-folds, n_s, r); dark-sector abundance; black holes as phase changes; a varying base-level count (needs a cost-per-element term); the restricted-menu study (code kept in this repo; draft pre-registration in `docs/parked/PREREGISTRATION_menu_study.md`).

## What no outcome can show

Anything about the real universe. A toy model can show that a mechanism is possible or impossible within a class of models. That is the whole claim.

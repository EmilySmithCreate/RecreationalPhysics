# Design brief: getting a measure of gravity out of the model, at least directionally

Written 2026-09-25, afternoon, at the author's direction (VISION Update 28): "I really think we can get our model to
output the measures of gravity, at least directionally; it does not have to work every way, it has to show at one
measure of λ; we have to define how many dimensions and degrees of freedom we are working with, so that we can do
those other calculations and return values that are close to the measured results." This page fixes those definitions,
names the observable and what it is compared with, says what exists and what is missing, and gives the protocol and
its cost. Physics reasoning here is *ours, unverified*; the author's account of gravity is hers (curve-first gravity,
`docs/papers/glossary.md`).

## 1. Definitions, fixed

- **Dimensions.** Three space directions: the six-link model (`graphity.cqg_d`, D = 3), on a flat L × L × L torus, all
  sides at least 6. Time is the model's sweep clock and is not a direction of the graph; nothing here is 3+1.
- **Degrees of freedom.** The wiring: which of the 3N edges join which points, under the hard-core rule; every point has
  six links. With named points the state is the graph; with interchangeable points (the author's rule, VISION Update 12)
  it is the graph up to renaming, weighted by its number of symmetries.
- **The energy.** H = 16(3N − S) + 4λX, the published curvature plus the curling cost (Update 23). One λ, fixed in
  advance for the test.
- **Matter.** A relic: a small curled object that is a dip inside flat space (every single move out costs energy), of
  known energy E above flat space. In four links this is one column curled, 24λ − 16 (paper 2). **In six links it has not
  been shown to exist** (O56): the one-switch column costs 120 and is not a dip. Finding it is step 1 below.
- **The observable: the average pull.** Two relics at graph separation r in a flat torus, at fixed coupling g, with the
  wiring free to rearrange. The probability P(r) of finding them at separation r over a long run gives the potential of
  mean force F(r) = −g ln P(r) + const (the standard name). Its **sign** (F falling as r falls is attraction), its
  **shape** (Newton in three dimensions: F ∝ −1/r, a pull ∝ 1/r²), and its **universality** (the same F for two
  relics of equal energy but different wiring; F scaling with E₁E₂) are the three things to compare.
- **The targets ("the measured results").** In the model's own units there are no meters or kilograms; what can be
  matched is the *form*: attraction; a potential that falls as 1/r at large r in three dimensions (a logarithm in two,
  which is why the 2D model was never the place to look); proportionality to the energies; independence from the
  relics' internal wiring. That is "directionally" and then "closer". A number with units needs the model's length and
  energy set against real ones, which nothing here does.

## 2. What is exact already, and which way it points

- No energetic force at a distance, at fixed wiring: H is a sum over edges, so two relics sharing no square are exactly
  additive, with an attraction only at contact (16 in four links, 64 in six; O22, O56).
- No counting pull at fixed wiring: the symmetry count of two identical defects is flat in their separation except at
  symmetric placements (O32 in four links, O56 in six).
- The counting drive to curl exists but appears only at full curling and pays only below λ ≈ 1.02 (O55).

So a pull, if there is one, must come from the *rearranging* surroundings: the free energy of the wiring between two
relics as they move. That is what the potential of mean force measures and what nothing so far has measured.

## 3. Why λ near 1.02, and why interchangeable points

At λ = 1.10 to 1.25 flat six-link space accepts no move at all below a coupling of 8 and melts at 10 (O51); there is no
window in which the surroundings rearrange and stay space. Near λ = 1 curling moves cost almost nothing (each surplus
square 4(λ − 1) beyond the tie), so the wiring around a relic can rearrange at a cold coupling without melting (the melt
wall stays at 64). And near λ = 1.02 the counting weight of curled arrangements is comparable to their energy (O55), so
if the author's mechanism (gravity from counting) acts anywhere in this family, it acts there. λ = 1.02 and g between
0.5 and 1.0 is the pre-registered setting, chosen for that reason and stated as such.

## 4. Protocol (T35, to be pre-registered with the author's prediction before it runs)

1. **Find the relic** (exact, no run): search two- and three-switch constructions inside flat 6 × 6 × 6 space for a curled
   object that is a dip, by the nearby-partner wall search; and read T34's saved end states, if any fold. Report its
   energy E and its symmetries. If none exists, the test cannot be posed in this family, and that is the result.
2. **Mobility** (a run): one relic at λ = 1.02, g = 0.5, 0.75, 1.0, followed for 10⁵ sweeps with interchangeable points;
   does it move without annealing? (T19's question, in six links.) A relic that heals is not matter.
3. **The pull** (the test): two relics, started at every separation from 2 to L/2 along an axis, run with interchangeable
   points, the separation recorded every block; P(r) pooled over starts; F(r) with its error from blocks. A named-points
   control beside it.
4. **Reading, fixed before the run:** ATTRACTS if F falls with r falling over at least three separations by more than
   two standard errors; REPELS if it rises; FLAT otherwise. Shape: the exponent of a fit F ∝ r^(−p) over the outer half,
   reported with its error (Newton in 3D is p = 1). Universality: repeated with a relic of a different wiring and the
   same E, the two F(r) agreeing within errors.

**Compute.** The interchangeable chain counts symmetries at every valid proposal (about 1 to 10 ms at N = 216 with
igraph); a sweep is 2N attempts of which a few percent are valid: about 1 s a sweep at N = 216, so 10⁵ sweeps is a day
of one CPU, and a full T35 (three couplings, a dozen starts, two relic types, plus the named control) is of order 50
CPU-days, about $60 on the rented machines. The six-link interchangeable chain (`graphity.interchangeable` at any D) and
the igraph package in the runner image are the two pieces of machinery not yet built.

## 5. What would count against, and what this cannot show

Against: no relic that is a dip in six links; a relic that anneals before it moves; F flat or repulsive; a pull that
depends on the relic's wiring at equal energy. Cannot show: any number with units; anything about time or light; the
strength of gravity; whether the author's account or Einstein's is the cause, since the model has only one candidate
cause to test.

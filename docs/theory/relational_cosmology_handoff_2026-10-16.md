# Updated relational cosmology hypothesis and research handoff (the author's, 16 October 2026)

**What this file is.** The document the author passed to the project on 16 October 2026, kept as received.
It was drafted in a separate AI-assisted conversation of hers and is her statement of the hypothesis as of
that day; the lines marked "The user clarified" are her words put in order by that assistant. Three notes
from the record before reading it. (1) It calls the hypothesis "Omega", the name X had in an earlier version
of the theory; the record writes X (CLAUDE.md; `docs/papers/glossary.md`). (2) Its research items T1 to T8
collide with the project's own T numbers (PREREGISTRATION T1 to T66); the record refers to them as H1 to H8.
(3) It is reviewed sentence by sentence against the record in
`relational_cosmology_review_2026-10-16.md`, and the positions it decides are VISION Update 59. Nothing in
it is a registered result; its own section 13 says so.

---

OMEGA — Updated Relational Cosmology Hypothesis and Research Handoff
Date: October 16, 2026
Status: Conceptual hypothesis with existing supporting toy-model results. The cosmological interpretation has not been demonstrated.

## 1. Central hypothesis

Fundamental reality consists of relationships, not spatial points.
Spatial points, dimensionality, distances, and volumes are emergent descriptions of those relationships.
The same underlying relational structure may support different geometric arrangements:

* Open, macroscopically extended spatial directions.
* Closed, tightly curled spatial directions.
* Intermediate configurations during a transition.

An opening transition changes the geometric expression of existing relationships. It need not create new fundamental relationships or points.
The proposed mechanism for a Big Bang is an energy-driven transition from a curled configuration to an open configuration.
The hypothesis also allows daughter universes to emerge recursively from curled regions of parent universes.

## 2. Corrected geometry: The curled slab

The user's central geometric analogy is a toilet-paper roll opened along its seam.
Imagine a three-dimensional slab with two extended directions and one short, curled direction.
The simplified toy geometry is:

Curled state: L × L × 4

Open state: L × L × L₃

The value 4 is the minimum curled size in the relevant toy construction, not an established minimum length in physical reality.
A previously discussed example was L × L × 6.
The user clarified that the two extended (L) directions are those of the parent universe itself. They are not severed at the event horizon.
Instead, existing spatial relationships curl inward in a whirlpool-like configuration.
This is not a proposal involving a little, separately contained slab inside a black hole.
It is a proposal in which the parent universe's own geometry changes its relational arrangement.
The continuous-slab and discrete-graph descriptions should both remain available as mathematical representations. Neither has yet been established as physically fundamental.

## 3. Black-hole growth and the event horizon

The proposed black hole has a curled relational configuration.
As matter and energy fall inward:

1. Energy enters the black-hole system.
2. The effective excitation parameter g increases.
3. The probability of nucleating an opening front increases.
4. The arrangement remains curled while awaiting a transition.
5. Eventually, a nucleation event can initiate rapid geometric opening.

From the parent universe's perspective, the black hole's horizon may expand.
However, the user emphasized that the amount of curled space is not necessarily a fundamental quantity.
An external increase in horizon size need not imply an increase in fundamental relational degrees of freedom.
The internal configuration may retain the same mathematical form regardless of the black hole's apparent external size.
This creates an important modeling question: how should black-hole mass, energy, and horizon area be represented if internal point count and spatial volume are emergent?
No answer is assumed yet.

## 4. Universal constant lambda

The user explicitly clarified:
Lambda is a universal constant, identical in parent and daughter universes.
It is not increased by incoming matter or energy.
The value λ = 1.25 has been used for many toy-model experiments, with other values explored to investigate parameter dependence.
This does not establish that the physical universe has λ = 1.25.
In the existing graph model, the Hamiltonian is:

H = 16(N − S) + 4λX, where X = Σ_e (S_e − 2)₊

Here:

* N is graph vertex count.
* S is the number of squares.
* S_e counts squares incident on edge e.
* λ controls the local energetic penalty associated with saturation.

At λ = 1, this Hamiltonian corresponds to the combinatorial-curvature action described in the paper. For λ ≠ 1, it belongs to a deformed neighboring family and is not itself that curvature.
At λ > 1, a curled direction has excess energy per vertex:

ε = 4(λ − 1)

At λ = 1.25: ε = 1.

Thus a complete conversion of a perfect curled torus to the flat ground state can release N model energy units, provided no residual defects retain part of the energy.
This result belongs to the existing graph construction; its cosmological applicability remains unproved.

## 5. Incoming energy increases g

Unlike lambda, the user's proposed physical g changes in response to energy entering the black-hole system.
The existing toy model gives the mean waiting time for the first exit from a curled state:

τ(λ, g) = [3 e^{−(32 − 16λ)/g} + 2 e^{−(64 − 40λ)/g}]^{−1}

This expression applies to the specific graph dynamics and proposal protocol in the paper. It is an approximate two-channel first-exit formula, rather than a universal physical law.
At λ = 1.25: ΔE_A = 12, ΔE_B = 14. Therefore:

τ(1.25, g) = [3 e^{−12/g} + 2 e^{−14/g}]^{−1}

Increasing g generally decreases the expected waiting time.
The user proposes that infalling energy raises the physical counterpart of g.
Important distinction: In the existing model, g is a Metropolis excitation or heat-bath parameter. The connection between this parameter and actual infalling black-hole energy has not yet been derived.
The next mathematical task is to construct that connection rather than assume it.

## 6. Probabilistic nucleation rather than a hard threshold

The user clarified that the transition becomes increasingly likely as energy accumulates.
It is not necessarily triggered at a single deterministic energy value.
Define an illustrative instantaneous nucleation rate:

Γ(g) = 1 / τ(λ, g)

Using the existing toy expression, this is a first-exit rate in units of inverse sweeps, not a calibrated physical rate.
If g changes with time, a candidate stochastic model is:

P(nucleated by t) = 1 − exp(−∫₀ᵗ Γ[g(t′)] dt′)

This survival-law formulation assumes an effective time-dependent Poisson hazard and must be tested; it is not an established result for the evolving black-hole system.
The critical cosmological question becomes:
Under what conditions does accumulated energy make nucleation sufficiently probable within the lifetime of the black hole?
The first graph move that escapes the curled state does not automatically guarantee a sustained opening front.
The probability of successful front establishment must be studied separately.

## 7. The opening front can use two energy mechanisms

The user proposed that both mechanisms may operate:

Mechanism A — Reservoir-assisted propagation. Energy accumulated through infall can help pay the activation costs of local rearrangements.

Mechanism B — Release-driven propagation. When a region successfully uncurls into a lower-energy configuration, the energy it releases can help drive subsequent transitions.

Together they suggest a possible self-propagating phase transition.
However, the released energy may also destabilize already opened regions.

Candidate energy accounting. Introduce:

* H_curl: energy in the relational configuration.
* E_R: energy held in an available excitation reservoir.
* E_other: other explicitly modeled energy components.

For a sealed toy system: E_total = H_curl + E_R + E_other. Require ΔE_total = 0.
If a local rearrangement changes the geometric energy by ΔH, the reservoir must supply the increase or absorb the decrease, unless another modeled sector carries the difference.
An opening event can therefore consume energy to cross a barrier and subsequently release a larger amount by moving into a lower-energy state.
This is consistent with energy conservation.

Propagation stability. The user's concern is that release might occur too rapidly and disrupt the emerging geometry.
This suggests studying at least three competing timescales:

* Local front propagation.
* Energy redistribution or absorption.
* Disorder formation and relaxation.

A successful daughter-universe transition must not merely begin; it must produce a stable, predominantly open configuration.
Whether a curled structure can stretch without breaking is an additional geometric and dynamical question. Stretching, loss of graph order, and graph disconnection are distinct events and should not be conflated.

## 8. Existing energy-conserving results

The uploaded paper already implements a sealed toy model using Creutz energy stores.
Total graph-plus-reservoir energy is conserved.
At λ = 1.25:

* A local seed of 12 units initiated conversion in all tested runs with seed energy at least 12, over tested sizes N = 48 through 192.
* No tested seed below 12 initiated conversion from the specified perfect initial configurations.
* The 12-unit value matches the minimum single-switch activation barrier.
* Successfully converted configurations release approximately one model energy unit per vertex.
* When the energy reservoir is too small to absorb the released energy, the ordered opened configuration frequently melts into disorder.
* Sufficient reservoir capacity substantially improves the probability of obtaining a stable open state.

These results support further exploration of reservoir-assisted and release-driven propagation within the toy model.
They do not establish that a real black hole contains such a reservoir or undergoes this transition.

## 9. Fundamental relationships and point count

The user clarified:
Points are not fundamentally real; relationships are.
Consequently, a daughter universe is not required to be smaller than its parent because a black-hole interior appears spatially smaller or because a particular finite toy graph has fewer vertices.
The current research program must distinguish:

1. Fixed graph vertices as mathematical bookkeeping.
2. Effective spatial points emerging from relational geometry.
3. Fundamental degrees of freedom, whose definition is still unresolved.
4. Possible nucleation seeds, which need not correspond one-to-one with points.

The user raised several possibilities without selecting among them:

* Effective point count might increase.
* Increasing excitation could create additional nucleation opportunities.
* Curled remnants might be incorporated into the evolving configuration.

These should remain separate hypotheses.
No assumption of fundamental point creation is authorized by this discussion.

## 10. Parent and daughter universes

A daughter universe may emerge when curled relationships open into macroscopic three-dimensional geometry.
The daughter may have the same mathematical structure as the parent.
It need not have the same apparent physical size as measured from the parent.
The black hole might remain present in the parent universe while the daughter has its own emergent spacetime.
This remains conjectural.
The working hypothesis requires a mathematically consistent description of how the same fundamental relational structure can support both perspectives.
The earlier whole-universe-reset model may still be investigated, but it is no longer a requirement for daughter-universe formation.

## 11. Energy across universe generations

The user clarified that their intended claim is:
The energy available within any individual emergent universe may be finite, while the cumulative energy accessible through repeated relational transitions may be unbounded.
This is not a claim that any one universe possesses infinite energy.
The model must determine whether:

* Energy is transferred between generations.
* Energy is recycled through geometric changes.
* A conserved quantity exists at the more fundamental relational level.
* An unbounded succession of transitions is mathematically possible.

An unbounded sequence of energy-releasing events does not, by itself, demonstrate creation of unlimited net energy.
Conventional global energy conservation is also nontrivial in dynamical general-relativistic spacetimes; the model must define carefully what energy is being counted and under what symmetry or conservation rule.

## 12. Recommended mathematical investigations

*(The record calls these H1 to H8.)*

T1 — Fixed lambda, variable g. Hold λ = 1.25 and model gradually increasing excitation. Measure first-exit waiting distributions and successful nucleation probability separately.

T2 — Coupling absorbed energy to g. Introduce an explicit reservoir with energy E_R. Derive or measure an effective relationship g = g(E_R, configuration). Do not assume that the existing thermal parameter automatically tracks infalling energy.

T3 — Front initiation versus completion. Record three separate outcomes: first escape from curled order; establishment of a persistent propagating front; completion into a stable open configuration.

T4 — Propagation and energy redistribution. Vary reservoir capacity, reservoir locality, energy transfer rate, and front propagation rate. Measure whether energy released behind the front assists propagation, destabilizes the newly opened state, or both.

T5 — Stretching versus destruction. If supported by graph rules, introduce candidate moves allowing stretched or intermediate curled configurations. Measure topology preservation, connectedness, local order, and defects. Do not interpret every disordered graph as a physically broken spacetime.

T6 — Emergent geometry and point-count invariance. Investigate representations in which a fixed underlying relational structure produces different effective geometric sizes or spatial resolutions. Determine whether the proposed daughter geometry can be reconstructed without creating fundamental vertices.

T7 — Recursive daughter-universe structure. Only after T1–T6, examine whether a curled relational configuration can consistently give rise to a separate emergent three-dimensional region while remaining embedded in the parent's description.

T8 — Falsification criteria. Identify parameter regimes where nucleation occurs but fails to produce stable opening, where released energy necessarily causes disorder, or where the proposed relational structure cannot support the required emergent geometry. Preserve negative results.

## 13. Constraints on interpretation

* Do not present the black-hole interpretation as an established consequence of the toy model.
* Do not assume λ = 1.25 is measured from the physical universe.
* Do not equate toy graph energy units with physical joules without a scale-setting argument.
* Do not conflate stochastic first escape, sustained front propagation, and successful completion.
* Do not claim recursive topology or daughter-universe formation is demonstrated.
* Do not assume point count grows or that new fundamental relationships appear.
* Do not describe energy release as unconstrained or necessarily infinite.
* Retain the earlier O85 connectivity limitation as an unresolved issue for models requiring multiple separate curled structures to join.

## 14. Current consolidated hypothesis

Omega proposes that the fundamental substrate of reality is relational rather than spatial. Spatial dimensionality arises from the geometric expression of these relationships.
A black hole may correspond to a curled configuration of the parent universe's existing relational geometry, with two directions extended and another compact.
Energy entering the black hole may increase an effective excitation parameter g, while the universal structural coupling λ remains invariant.
As excitation increases, nucleation of a transition from curled to open geometry may become more probable.
Once nucleated, a front may propagate through a combination of available reservoir energy and energy released by local geometric uncurling.
The transition could produce a daughter spacetime whose mathematical organization resembles that of its parent. Stability would depend on how the released energy is redistributed and whether the emerging geometry remains ordered.
Recursive universe formation might therefore arise from repeated transitions of the same fundamental class of relationships, without requiring fundamental spatial points to be created.
Research priority: Establish the energy-coupled nucleation and stable propagation mechanism before attempting to demonstrate the full cosmological interpretation.
Status: The ingredients are partly motivated by exact toy-model calculations and simulation results, but the combined mechanism, physical black-hole identification, and daughter-universe interpretation remain open hypotheses.

# A quantum version of the toy: the scope (2 November 2026)

*Written at the author's request: "write a Hamiltonian on his Hilbert space whose dynamics curls and uncurls, can you
scope out this version of the toy? Sounds like we'll need to try his and Jacobson's." Ours throughout, unverified, for
her decisions under S1. Nothing here is built or run. A quantum toy is a new model (the "other models" decision of
VISION Update 28) and adopts amplitudes, which is the rule she held in Update 21; both are hers to decide. At λ ≠ 1 the
model is our family, never combinatorial quantum gravity.*

## 1. Why, in one paragraph

The classical toy has everything learned from Trugenberger's model (walls, sparks, releases, fronts, knots, the size
law) and no route to two things the hypothesis needs: Einstein's equation (claim 2) and quantum behavior (claim 2's
other half, Updates 17 to 21). Carroll's papers give a route to a spatial Einstein equation from entanglement
([CCM16]; [CC17], `docs/reading/notes/2026-11-02_carroll_space_from_entanglement.md`), and Jacobson's give the other
published route ([Jac95]; and his 2016 entanglement-equilibrium paper, not yet read). Both need a quantum state. Carroll
and Cao's paper has no Hamiltonian ("We have not posited any form of Hamiltonian or time evolution"), so it cannot by
itself curl or uncurl anything. The scope below supplies the Hamiltonian from the toy, so that nothing learned is
lost: the classical toy is the limit in which the new term is switched off.

## 2. The model, in its simplest form

- **The basis.** One basis state per valid wiring of the toy (four or six links a point, bipartite, the hard-core
  rule). The Hilbert space is the span of those wirings.
- **The diagonal part is the toy's energy, unchanged.** H₀|G⟩ = [16(N − S) + 4λX] |G⟩ at four links (the six-link form
  likewise). Every exact result of the record is a statement about H₀ and survives.
- **The off-diagonal part is the toy's move, made coherent.** H₁ = −Γ Σ over switches s |s(G)⟩⟨G|, summed over the
  valid edge switches the chain already proposes. Γ ≥ 0 is the one new constant. With the minus sign every off-diagonal
  element is non-positive, so H = H₀ + H₁ is *stoquastic*: its ground state has non-negative amplitudes and it can be
  sampled by path-integral quantum Monte Carlo, the classical toy in one more direction (imaginary time). That keeps the
  precision tools.
- **Γ = 0 is the classical toy exactly.** The limit is checkable to the last digit, which is the bridge rule 2 asks for.
- *Published relative, rule 13:* quantum graphity ([KMS06]; Konopka, Markopoulou and Severini [KMSev08]; Hamma et al.
  [HMPS09]) is a Hamiltonian on graph states with exactly this shape (a diagonal cost plus hopping between graphs).
  Read before building; the toy's version differs in its diagonal term (Trugenberger's curvature plus the curling cost)
  and its hard-core rule. Trugenberger's own [T23] and the 2023 Universe paper describe emergent quantum behavior in the
  published model; also to read first.

## 3. The two readings, which is what "try his and Jacobson's" means here

**Carroll's reader** (no new physics, a measurement on the ground state). Take each point as a factor of the Hilbert
space. In the ground state, compute the mutual information between factors, turn it into a distance with their Eq. (13)
(Φ = −ln at their choice), and read the dimension by multidimensional scaling and the curvature from how distances
respond to a local perturbation. **The test it makes possible:** does the geometry read from entanglement agree with
the geometry of the wiring the state is mostly in? On whole tori it cannot: each wrapped cycle takes two
large eigenvalues, so the sheet, the tube and the 4-cube all read four (exact, the note's section 7 as corrected); the
reading is made on open windows, and whether a direction curled to a few sites counts at all is the note's section 8. Agreement
would be the first time the toy's space and Carroll's space are the same space; disagreement would say which of the
two dimension counts is the reading of the base.

**Jacobson's reader** (also a measurement, but it tests an equation). Jacobson's entanglement equilibrium (to read in
full before this is relied on) says: in a small ball, the entanglement entropy at fixed volume is extremal in the
vacuum, and its first variation equals the variation of the modular energy; that holding everywhere is Einstein's
equation. **The test it makes possible:** in the quantum toy's ground state, perturb one region (a knot, a curled ring)
and check whether δS_ent = δ⟨K⟩ holds for small regions, and whether δS_ent tracks the change in the region's boundary
(the area term). If it does at Γ > 0, the toy has an Einstein-like response built in; if it fails, the toy's space is not
a Jacobson space.

## 4. What it keeps, what it changes, what it costs

| | Classical toy | Quantum toy |
|---|---|---|
| Exact results (floor at zero, walls, releases, no force at fixed wiring) | yes | yes, as statements about H₀; Γ adds tunneling through walls |
| The sharp change, the front, the knots | measured | to be re-measured; Γ makes walls tunnel, so "stable for now" gets a quantum lifetime as well as a thermal one |
| Bell and GHZ | counting cannot violate them (O29) | a genuine quantum state; the question becomes open again, now computable |
| The entanglement fork (gravity-mediated entanglement) | predicts none | the carrier is quantum, so it predicts entanglement, as linearized quantum gravity does; a positive Bose-Marletto-Vedral result would no longer rule it out, and a null would count against it |
| Sizes reachable | thousands of points | exact diagonalization only for the tiny class spaces of N ≤ 18; quantum Monte Carlo (stoquastic) to hundreds; entanglement readers need the state itself, so tensor networks or small sizes |
| Units | none | still none: ħ enters only through Γ in the toy's own units |

## 5. Order of work, cheapest first, each step her decision under S1

0. **Reading** (no decision needed): [KMS06] and [KMSev08] in full for the Hamiltonian; [HMPS09] for light cones in
   such a model; Jacobson 2016 (entanglement equilibrium); [T23] and Trugenberger's 2023 Universe paper for what the
   published model already says about quantum behavior. Rule 15 search for "quantum switch dynamics on graphs with a
   curvature Hamiltonian" before any claim of novelty.
1. **Exact, the smallest case.** At N = 16 and 18 the record already holds the full list of valid wirings by class
   (`results/ergodicity_small.csv`; `graphity.small_graphs`). Build H on the class space (interchangeable points; 5 and
   26 classes, so tiny matrices) with the switch counts between classes as the off-diagonal weights, diagonalize at a
   few Γ, and read the ground state's weights against the classical Boltzmann weights. This needs no new kernel and
   tests the construction.
2. **Carroll's reader on the classical toy first** (needs no Γ): feed saved wirings to the MDS estimator with a
   constant mutual information per link, as the entanglement note's section 7 proposes. It calibrates the reader on
   states whose geometry is known before any quantum state exists.
3. **Quantum Monte Carlo of the stoquastic model** at four links, the flat sheet and the tube, a few Γ: does a curled
   tube decay faster with Γ (quantum tunneling through the wall of 12), and does the opening still go as a front?
4. **Small-system states for the entanglement readers** (exact or tensor-network, tens of points): Carroll's dimension
   and Jacobson's first-law check on the ground state, flat against curled.

Each step that runs is pre-registered with her prediction and a held-out size (rules 4 and 14).

## 6. What it cannot do, said in advance

It does not give units. It does not make the hypothesis quantum in her sense of versions and loops (Update 17) without
a further identification of what a version is. It gives Einstein's equation only if Jacobson's check passes, and then
only in the toy's own units and only for small perturbations. And it changes the falsification map: the entanglement
fork flips, which the pages must say the day the decision is taken.

## 7. Questions for her

1. Adopt amplitudes (lifting Update 21's hold) for a second, quantum toy beside the classical one, or not yet?
2. Named points or interchangeable points for the quantum toy (the class space of step 1 is interchangeable)?
3. Step 0's reading first (recommended), or step 1's exact matrix straight away?

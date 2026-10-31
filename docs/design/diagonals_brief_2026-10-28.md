# Design brief: diagonals as variables, light on the body diagonals, and the γ test

Written 2026-10-28 at the author's decisions of that evening (VISION Updates 139 to 143; her words verbatim in
`sandbox/NOTEBOOK.md`). It follows `gravity_link_brief.md` (the edges) and `twist_curl_rules_2026-10-27.md` (the
particles). Everything not marked hers is *ours, unverified*; nothing here has been built or run. The model with any of it
is our family around the published model, never combinatorial quantum gravity.

## 1. Her decisions that fix the shape

1. **Gravity travels through the cube edges; light through the body-diagonal links** (Update 142).
2. **A body diagonal's length is derived from its cube's edges by geometry**, √(ℓx² + ℓy² + ℓz²): no new constant
   (Update 143, option (i)).
3. **The unit:** the loop of three white thirds, net twist −1, no fold, is the electron, 0.511 MeV, charge −1, spin ½
   (Update 139). **Mass counts looped diagonals**, 0.1703 MeV each (Update 140). **The proton is a large closed ring of
   about 5,500 diagonals** (confirmed, Update 143).
4. **The scattering bound on the electron's size is the operative one**, about 10⁻¹⁸ to 10⁻¹⁹ m (Update 143); the
   moment-based figure is model-dependent and is not used.
5. **Option B for the knot:** the diagonals are built as variables before any wiring-knot search; particles are loops of
   twisted diagonals, the wiring's knots are the scrap (Update 143).
6. From before: the edges' lengths relax from their curl with one constant α and the total length fixed near matter
   (Updates 136 to 138); the free photon is half a curl moving along a body diagonal as a smooth spiral at one link per
   tick, and a photon's excitation is of the electron's orbit (Updates 141, 142); twist in thirds on the box diagonals
   and halves on the face diagonals, sign by colour, the loop total whole, spin from the twist and charge from the twist
   plus the photons held (the sheet, as it stands after the audit).

## 2. What is built already, and what this adds

Built: `graphity.lengths` (the edges' stiffness K = 4(6I − A) per family, exact; the relaxed lengths with the total fixed;
a chain on the total energy); `graphity.u1` (Wilson's phase on every link, the light field of Update 96, on the edges).

To add, in order, each with rule-6 tests before any run:

1. **Derived diagonal lengths** (`graphity.diagonals`): for every cube, the body diagonals' lengths √(ℓx² + ℓy² + ℓz²)
   from its edges' relaxed lengths; exact first-order check: a halo δ on the edges lengthens a body diagonal by
   (δx + δy + δz)/√3. No state of its own.
2. **Light on the body diagonals**: a pulse moving along body-diagonal directions, spending ℓ ticks on a diagonal of
   length ℓ (her one link per tick, read on the diagonal's own length); the delay past a knot is the extra ticks over the
   same path far from it. First as a shortest-path reader (exact), then, if wanted, as the Wilson field moved onto the
   body-diagonal graph.
3. **Twist on the diagonals as a state**: a value on each box and face diagonal (thirds and halves, signed by colour) and
   a photon count; a loop's charge, spin and mass read by the sheet's rules; the energy of twist is the one open form
   (the sheet's κ term is ours). *Not needed for the γ test*, which uses the curl's halo alone, and so is built after it.

## 3. The γ test (the first registered test; a number with no free constant)

In Einstein's weak field one potential Φ does two things: it delays and bends light (through the space part of the
metric) and it pulls matter (through the time part), and the ratio of the two is fixed, γ = 1, measured by Cassini to
2 × 10⁻⁵ (*general knowledge, to verify*). In this family the halo δ on the edges does both too: light is delayed through
the derived body diagonals (first order in δ, coefficient fixed by geometry), and a second knot's energy changes by
α|c₂|·δ (first order in δ, coefficient α). So the toy has a γ-like ratio with α in it, and requiring the measured γ = 1
**pins α**; after that the strength of the pull between two knots, α²|c₁|ᵀK⁺|c₂|, is a prediction in lattice units, to be
set against G once a link has a length (from the electron's loop under the scattering bound, about 3 × 10⁻¹⁹ m).

**Definitions to fix before any run (ours; hers to confirm):**
- The fractional light delay past a knot of charges q: Δ = (ticks through the halo − ticks far from it) / ticks far
  from it, along a body-diagonal path at impact parameter b.
- The potential per unit mass of a test knot of charges q₂ and mass m₂ (its looped diagonals, Update 140) at the same
  b: U = α q₂ᵀδ₁ / m₂.
- The toy's γ-analogue: the ratio of Δ to U at the same b, set against the weak-field value of the same ratio in
  Einstein's gravity (the Shapiro delay against the Newtonian potential along the same path). γ = 1 fixes α.
- Then: α's value; the pull's strength; and the one check that costs nothing, whether the α so fixed is the same at two
  impact parameters and two knot sizes (if it is not, the family has no single γ and the test fails).

**Held-out size (rule 14):** fit at L = 16 and 24, predict at L = 32 before it runs. **Words:** ONE α (the fixed α agrees
across b and knots within a stated range), DRIFTS (it does not), NO DELAY (the derived diagonals carry no first-order
delay). The owner's prediction is owed before the registration is committed.

## 4. What this cannot do, said plainly

- The toy has no clocks; "ticks on a diagonal" is her rule, not a measured rate. Time dilation is not in it.
- The scale rule is decided, not derived (O166 (1)); the constrained model is hers by decision.
- The edges' halo is computed on axis links only; the diagonals enter through geometry, not as variables, which is
  option (i) and is what makes α pinnable.
- The proton as a ring of 5,500 diagonals is a statement about her picture; the toy has no object of that size yet.
- Nothing here is about reality until a physicist has looked (S5).

## 5. Order of work

1. `graphity.diagonals` and the light reader, with tests (an afternoon).
2. The γ registration with her prediction, stage 1 at L = 16 and 24, held out at L = 32.
3. The twist state on the diagonals (section 2, item 3) and the electron loop as an object with an energy, which is
   where the particle sheet becomes testable: the three-particle check (neutron, pion, photon) as the first exact test.

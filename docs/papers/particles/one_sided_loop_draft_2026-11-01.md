# The one-sided loop: what is exact about a half-twisted band of face diagonals in the toy, and what the owner's dark-matter picture asks it to show next

Emily Smith (Charlottesville); analysis drafted with Claude Fable 5.1 (Anthropic)

*Draft, 1 November 2026, for the owner's review. A paper in the particles group (the outline of 20 October is
`outline.md` in this folder). Every statement carries one of four tags: **exact** (arithmetic or complete enumeration,
checked in code), **built** (a rule put into `src/graphity/twist.py` and pinned by `tests/test_twist.py`), **hers**
(the owner's hypothesis, to be tested), **ours** (our reading, unverified). The twisted-diagonal state sits on the
six-link toy at a curling cost λ ≠ 1, which is our family around the published model and never combinatorial quantum
gravity. Every six-link statement carries the standing caveat that the published three-dimensional curve has not been
reproduced (Gate C open).*

## Abstract

The toy's twisted-diagonal state puts twist on the diagonals of a cubic lattice: thirds on the box diagonals (1, 1, 2),
halves on the face diagonals (1, 1, 0). Reading a loop's twists as the turning of a band, a closed loop is one-sided
exactly when its total twist is an odd multiple of one half. We show, exactly: no loop of thirds is one-sided; the
cheapest one-sided loop of face diagonals costs 3/4 under the twist term as built, at every length n ≥ 3, with two tied
forms at n = 3; the cheapest two-sided loop with cancelling twist (the sheet's neutrino) costs 3/2 at n ≥ 4; so the
one-sided loop costs exactly half, a property of the term's arithmetic and not a match to any measurement. Under the
owner's rule that charge rides only on thirds, it has charge 0. The owner's hypothesis, that dark matter is such a
loop and that the curled slab X is a stack of them, is stated as hers; its first registered test (T88, the pole test) is
described, with no result in this draft.

## 1. The hypothesis, in the owner's words

**Hers** (31 October and 1 November 2026; her words put in order, verbatim in `sandbox/NOTEBOOK.md`; recorded in
`docs/design/twist_curl_rules_current.md` section 1 and VISION Update 149).

- Neutrinos are not the dark matter. The neutrino is two-sided: two half-twist loops of opposite hand.
- Dark matter is a one-sided loop of surplus curl, a flaw left when space opened, which meets gravity and not light.
  "A one sided structure can hold half a loop, so a curl held in 1/2 the length that a neutrino has."
- A charge needs two sides and can only be applied on thirds. So a face diagonal's half twist is twist, not charge.
- The curled slab (X, the state before a space opens) is made of tightly lined-up dark matter: many one-sided objects
  of the same handedness stacked together. In it there is only twist and curl and no space, because nothing can move;
  matter cannot get through.
- Surplus dark matter is crushed by gravity into a shell around a zero-dimensional space at the center of the slab: the
  rod. Photons cannot get through the slab but apply their curl energy to it, and when there is enough, a big bang
  happens at one pole of the rod. The matter handedness breaches first; a new three-dimensional spacetime is born.

This is a hypothesis to test, not a result. Nothing below derives it. What the toy can do is say which parts of it are
already fixed by the rules as built, which parts are arithmetic, and which parts have nothing to test yet.

## 2. The toy's twisted-diagonal state

**Built** (`src/graphity/twist.py`; the form fixed in `docs/design/twisted_diagonals_build_2026-10-30.md` before it
was coded). The lattice is an L × L × L torus of points colored by the parity of x + y + z. Three kinds of same-color
step carry the state:

| step | displacement | count | length | twist increment | sector (hers) |
|---|---|---|---|---|---|
| box diagonal | signed permutation of (1, 1, 2) | 24 | √6 | 1/3 | ordinary matter |
| long diagonal | (1, 1, 2m), m ≥ 2 | | √(2 + 4m²) | none (curl only) | her gluon |
| face diagonal | signed permutation of (1, 1, 0) | 12 | √2 | 1/2 | dark matter, neutrinos |

Body diagonals (1, 1, 1) change color and carry the photon; they hold no twist and are not part of a loop.

A **loop** is a closed sequence of steps of one kind on the torus, with a twist τ_i on each step (a multiple of that
kind's increment, either sign), one non-zero integer curl, and a spin in {−1/2, 0, +1/2} that may be non-zero only if
some τ_i ≠ 0. A **particle** is a named set of loops. Its readers are:

- **charge** = Σ τ_i over the box-diagonal loops only (her rule of 31 October: a charge needs two sides and rides only
  on thirds); a particle on its own must have whole charge;
- **spin** = |Σ s| over its loops; **mass count** = the number of looped diagonals;
- **net twist** of a set of particles = Σ charge, conserved by construction under pair creation (a loop and its mirror,
  every τ_i, the curl and the spin reversed, sum to zero).

The **twist energy** of a loop (the build document, section 4; her decision of 30 October that the constant may differ by
kind of diagonal) is

    E(loop) = ε · [ Σ_i τ_i²  +  Σ_i (τ_{i+1} − τ_i)² ]  +  ε_w · Wr²,                       (1)

with ε the constant for box and long diagonals, ε_face in its place on face diagonals, Wr the writhe of the loop as a
closed polygon (zero for a flat loop, undefined for one that winds the torus), and the index cyclic. The first sum is
the cost of holding twist, the second the cost of a change of twist between neighboring diagonals. The writhe term does
not depend on the twists, so for a given loop shape it does not change which twist pattern is cheapest; every cost below
is quoted with it off (ε_w = 0), which is also its value on any flat loop.

**Exact, already pinned** (`tests/test_twist.py`): the electron as the sheet defines it, three white thirds
(−1/3, −1/3, −1/3) on a flat triangle of box diagonals, has charge −1, spin 1/2, mass count 3 and E = ε/3; the
two-loop dark pair on face diagonals is cheaper than the box pair exactly when ε_face < (4/9) ε.

## 3. Exact results

All of this section is **exact**: arithmetic on equation (1) with ε_w = 0, checked by complete enumeration in
`sandbox/one_sided_loop_look.py` (every pattern of twists with |τ_i| ≤ 1 at n = 3, 4, 5, 6; larger twists are excluded
by the first sum alone, since one τ_i² ≥ 9/4 already exceeds every bound below). The look was a sandbox look: its four
predictions were written before it ran, and all four held. It crowns nothing; it fixes what the rules already say.

### 3.1 The one-sidedness criterion

Read each τ_i as the number of whole turns a band makes along diagonal i (**hers**, the reading the word "twist"
carries on the sheet; the identification is hers, the consequence is arithmetic). A band carried round a closed loop
turns in total by 2π T, with T = Σ τ_i. It returns to itself when T is a whole number and returns reversed when T is a
whole number plus one half; a band that returns reversed has one side (a Möbius band). So:

> a loop is one-sided exactly when 2T is an odd integer.

Two lines: the band's normal after the circuit is the starting normal rotated by 2πT; that is the starting normal when
T ∈ ℤ and its negative when T ∈ ℤ + 1/2, and no other value closes the band at all.

### 3.2 No loop of thirds is one-sided

On box diagonals every τ_i is a multiple of 1/3, so T = k/3 for an integer k, and 2T = 2k/3. For 2T to be an odd integer,
2k must be an odd multiple of 3, which is impossible since 2k is even. The enumeration at n = 3 to 6 finds no
candidate, as it must. **Consequence**: the one-sided loop of the owner's hypothesis cannot be ordinary matter in this
toy; it lives on the face diagonals, where her assignment of 30 October had already put the dark sector.

### 3.3 The cheapest one-sided loop of face diagonals costs 3/4 at every length

On face diagonals τ_i ∈ (1/2) ℤ and one-sidedness needs T ∈ ℤ + 1/2. The minimum of (1) over such patterns is

    E_min(one-sided, n) = (3/4) ε_face      for every n ≥ 3.                                          (2)

*Lower bound.* Some τ_i is non-zero, so the first sum is at least 1/4. If all τ_i are equal to the same value v, then
T = nv ∈ ℤ + 1/2 forces v to be a half-odd number and n odd, so the first sum is at least n/4 ≥ 3/4. Otherwise the twist
changes somewhere round the loop and, the loop being closed, changes back, so at least two neighboring differences
are non-zero, each at least 1/2 in size, and the second sum is at least 2 × 1/4 = 1/2; the total is at least 3/4.

*Attained by.* A single half twist on one diagonal and none elsewhere, (±1/2, 0, ..., 0): first sum 1/4, second sum
1/2, total 3/4, at every n ≥ 3. At n = 3 and only there, the uniform band (±1/2, ±1/2, ±1/2) ties: first sum 3/4,
second sum 0. So the minimum is 3/4 at every length, with two tied forms at n = 3 and one form (up to rotation and
sign) at n ≥ 4. Nothing in (1) selects a length for the one-sided loop.

### 3.4 The two-sided neutrino costs 3/2 at n ≥ 4

The sheet's neutrino is a loop whose twists are present and cancel: T = 0 with some τ_i ≠ 0. On face diagonals it needs
at least one +1/2 and one −1/2, so the first sum is at least 1/2. The twist then rises from −1/2 to +1/2 and falls back
round the loop, a total change of 2 in each direction; the cheapest way to spend a total variation of 2 on the second
sum is in four steps of 1/2, costing 4 × 1/4 = 1, which needs n ≥ 4 (the pattern (+1/2, 0, −1/2, 0)). At n = 3 one of
the steps must be a whole jump, costing 1 on its own, and the minimum is 2. So

    E_min(two-sided, cancelling, n) = (3/2) ε_face  for n ≥ 4,   2 ε_face at n = 3.                   (3)

### 3.5 The factor one half

From (2) and (3), at every n ≥ 4,

    E_min(one-sided) / E_min(two-sided) = 1/2,

whatever the value of ε_face, since both are face loops and the constant cancels. This is what the owner's sentence
"a curl held in 1/2 the length that a neutrino has" becomes under the term as built: the half appears as a cost, not
as a length, because (1) selects no length for either loop. The ratio is a property of the arithmetic of (1), which
charges τ² per diagonal and (Δτ)² per joint; it is not a comparison with any measured mass, and the toy has no rule
that turns a twist cost into MeV. Against the electron's E = ε/3 on box diagonals, the one-sided loop costs
(9/4)(ε_face/ε) times as much, and ε_face/ε is not derived (section 4).

### 3.6 Charge 0, and the whole-charge rule

**Built.** `Particle.charge` sums net twist over box-diagonal loops only, so a particle made of one one-sided face loop
has charge 0, passes `check_whole_charge`, and is a particle on its own; the same lone half twist read as charge would
have been refused, and before her rule of 31 October it was (the look's fourth prediction named that conflict; her rule
dissolved it). Pinned by `test_charge_is_carried_only_on_thirds`. The loop's half twist is still read: it appears in the
particle's τ⁺ (twist present) and in the loop's own net twist, and spin 1/2 is allowed on it because twist is present.

**Hers, with the rule's consequence exact.** "Meets gravity and not light" is, as far as the rules reach, the statement
that the loop has charge 0 by construction. Whether it couples to light in any other way is not defined in the toy
(section 4).

### 3.7 Handedness is not priced

**Exact.** Equation (1) is even in the twists: a loop and its mirror image (every τ_i reversed) cost the same, and
`mirror` also reverses the curl and spin. So the term as built does not prefer either hand of the one-sided loop.
**Ours**: the owner's slab is a stack of one handedness; nothing in the toy yet makes a stack of one hand cheaper than
a mixed one, and a rule that does would be a new ingredient under S1.

## 4. What is not shown

- **No dynamics of twist.** The twist state is read back exactly from values put in; nothing moves a twist, creates a
  loop, or lets one loop meet another. "The matter handedness breaches first" and "nothing can move inside the slab"
  have nothing to test yet (**ours**, from the build document's section 6).
- **No derivation of the face-diagonal stiffness.** ε_face is a free constant. The one exact statement about it is the
  threshold 4/9 of section 2. The waves brief's second length field on the face diagonals (VISION Update 149, decision
  (3), read as hers and INFERRED) would supply a stiffness from the curvature's own arithmetic; it has been computed for
  the axis edges only and is owed for the face diagonals.
- **No coupling of a one-sided loop to light is defined.** The photon as built (section 7 of the build document) is an
  open path on body diagonals; its meeting with matter is one bookkeeping function, `absorb`, which takes any loop and
  does not distinguish face loops from box loops. Which loops may absorb a photon is undecided (the function's own
  docstring says so). So "does not meet light" is a rule's consequence for charge and an open question for absorption.
- **No slab of loops has been built.** The toy's curled slab is a wiring (a 4 × L × L torus with one direction curled);
  the twisted-diagonal state has never been placed on a curled torus, and the exact statement that a fully curled piece
  larger than a cube is a gas of cubes (ASSUMPTIONS O85) is about the wiring, not about loops. The five fold tests that
  found nothing curled (T34, T57 and their relatives) folded the lattice and had no loops to stack, so they do not bear
  on the stacked reading either way (VISION Update 149, item (v)).
- **Nothing about the real universe.** Every number here is a count on a toy with a put-in rule. The factor one half is
  not evidence for anything measured. A prior-work note on one-sided (Möbius) bands as particle or dark-matter
  candidates is owed under rule 15 before any sentence says what has or has not been found.

## 5. The registered test: T88, the pole test

**Why this test** (**ours**, from VISION Update 149, item (iv)). The one part of the owner's picture that the toy can
already ask is *where* the opening starts when energy is supplied at one place. In a steady bath the rod (two directions
curled, one open) opened from several places along its length (T53, SEVERAL). Her picture says the big bang fires at
one pole of the rod, fed by energy that has built up there. That is a prediction about the position of the first
opening, and it would be the first run in which where the opening starts is the verdict.

**What is run** (PREREGISTRATION T88, committed 1 November before any run; the scripts `run_rod_pole.py`,
`make_t88_configs.py`, `analyse_t88.py` and `tests/test_t88.py`). The exact six-link rod
4 × 4 × L, two directions curled and one open, named points, under her tie "all at the last", f = (0, a, 2a, 0) with
a = 4(λ − 1) per point (VISION Update 47), sealed with no leak. The whole energy E is placed at the start in the
per-vertex stores of the eight side-0 points of the first layer along the open direction (z = 0) and nowhere else;
each move pays from, or is paid into, the store of the point that proposed it, so energy a point releases stays where
it is released, the setting in which the two-dimensional tube opened as a front (T48). The rod is periodic, so the fed
end is a pole only in the sense that the energy sits there, and the far side is the layer z = L/2. Cells: λ ∈ {1.20,
1.25}; E ∈ {120, 240, 480}, that is 15, 30 and 60 a store against the rod's exact cheapest move out under the tie, 24.0 at
λ = 1.25 and 25.6 at 1.20 (every switch of the 4 × 4 × 8 rod priced; a store must hold a move's whole cost, so the
lowest energy is a control that cannot move); L = 8 and 12 in stage 1; four replicas a cell; 10,000 sweeps read every 100; final wirings
saved. Read at every block, without touching the chain: the local dimension d at every point, the count of points at
d = 3 (both curled directions open) by layer, the connected open regions of at least 16 points at d = 3, damaged points
(d > 3), and the conservation check H + T_f + stores.

**Verdict words**, fixed before any run:

- **ONE FRONT**: an open region of at least 16 points appears; at its first appearance the fed layer holds a point at
  d = 3; and at every reading up to the far side's opening there is at most one open region. The opened region is one
  connected piece containing the fed end, and the far side opens last.
- **SEVERAL**: an opening appears but not from the fed end, or a second open region appears before the front reaches
  the far side.
- **NOTHING OPENS**: no region of 16 open points in 10,000 sweeps.

The far side counts as opened at the first sweep at which at least 8 of its 16 points are at d = 3 (t_far). A cell's
word is the majority over its replicas, a tie going to SEVERAL. Damage is reported, not scored.

**Predictions.** Hers: **ONE FRONT**, inferred from her picture ("a big bang happens at one pole of the rod") and marked
INFERRED until she confirms. Ours, recorded there: NOTHING OPENS at E = 120; ONE FRONT at 240 and 480 at λ = 1.25; at λ = 1.20 ONE FRONT at 480 and a
mix at 240.

**Held-out size** (rule 14). L = 16 is held out. After L = 8 and 12 are read, t_far's cell mean at L = 16 is written as
the straight-line extrapolation of the two smaller sizes' cell means (a front at a fixed speed makes t_far grow with the
distance to the far side), with a range of twice the larger of the two standard errors, and the cell's word at L = 16 is
predicted as the word the two smaller sizes share; only then is L = 16 run, and the size claim is scored there alone.

**The result of T88 is not in this draft.** Nothing has been run. Every six-link result will carry the Gate C caveat.

## 6. Figures needed

Listed, not drawn; each is to be made by a script from the definitions or from saved results, never by hand.

1. The one-sided band: a flat loop of face diagonals (the triangle (1, 1, 0), (−1, 0, 1), (0, −1, −1) on three faces
   of one cube) drawn as a band with one half twist, a Möbius strip, beside the same loop two-sided with (+1/2, 0,
   −1/2, 0) on a four-step loop. Labeled SKETCH where placement is not data.
2. Cost against length under equation (1) with ε_w = 0: E_min for the one-sided loop (3/4 at every n), the cancelling
   two-sided loop (2 at n = 3, 3/2 at n ≥ 4) and, for scale, the electron triangle on box diagonals (1/3, with ε_face/ε
   shown as a slider or at two values). From `sandbox/one_sided_loop_look.py` extended to the lengths plotted.
3. The rod of T88: the 4 × 4 × L torus with the fed layer z = 0 marked, the far layer z = L/2, and the open
   direction; after the runs, the count of points at d = 3 by layer against sweep for one replica of each word.
4. After the runs: t_far against L at L = 8 and 12 with the held-out prediction and range drawn before L = 16 is added.

## 7. What is claimed, and by whom

- **Exact**: a loop is one-sided exactly when twice its total twist is an odd integer (given the band reading of twist).
- **Exact**: no loop of box diagonals (thirds) is one-sided.
- **Exact**: the cheapest one-sided loop of face diagonals costs (3/4) ε_face at every n ≥ 3; two tied forms at n = 3,
  one at n ≥ 4; no length is selected.
- **Exact**: the cheapest two-sided cancelling loop costs (3/2) ε_face at n ≥ 4 and 2 ε_face at n = 3.
- **Exact**: the ratio one half is independent of ε_face and ε and is a property of equation (1), not a measurement.
- **Exact**: equation (1) is even in the twists; a one-sided loop and its mirror cost the same; no hand is preferred.
- **Built**: charge is summed over box-diagonal loops only; the one-sided face loop has charge 0 and is a particle on
  its own.
- **Built**: `absorb` does not distinguish face loops from box loops; which loops may take a photon is undecided.
- **Hers**: dark matter is a one-sided loop of surplus curl, electrically neutral, meeting gravity and not light.
- **Hers**: the neutrino is two-sided, two half-twist loops of opposite hand, and is not the dark matter.
- **Hers**: a charge needs two sides and rides only on thirds.
- **Hers**: the curled slab X is one-sided dark matter of one handedness stacked tightly; the big bang fires at one
  pole of the rod.
- **Hers (INFERRED)**: T88 reads ONE FRONT.
- **Ours**: the band reading of twist is the step that turns a number into a topology; the owner adopted the word, the
  consequence is arithmetic.
- **Ours**: a stack of one handedness needs a rule the toy does not have; a coupling of the one-sided loop to light is
  not defined; the stiffness of the face diagonals is owed from the waves brief; a prior-work note on one-sided bands
  is owed under rule 15.
- **Ours**: T88's result, when read, is a statement about the toy's rod under one tie, and about nothing in the sky.

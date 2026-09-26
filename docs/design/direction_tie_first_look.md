# The direction tie, first look: walls and windows as κ grows

**EXACT, EXPLORATORY. The knob of VISION Update 30.** Written 2026-09-25, late afternoon, the same day the owner decided
the knob. Every number below is a brute-force count over every single switch out of a stated arrangement; nothing was
simulated, and no Monte Carlo was run. With κ ≠ 0 (or λ ≠ 1) this is our family around the model, never combinatorial
quantum gravity (VISION Updates 22 and 30). Every six- and eight-link result carries VISION Update 24's caveat: the
reproduction gate for more than four links is open. Readings marked *ours* are the assistant's and unreviewed.

## The answer first

- **κ = 0 reproduces O49 and O50 exactly**: all nine walls, at both λ, with the same move signatures.
- **The form fixed in Update 30, read literally, rewards damage.** `local_dimension_d` counts pairs of links that close
  no square. At the points a switch rewires, that count goes above D (up to 10 in these runs), and there d(D − d) is
  negative. So the term lowers the energy of broken points. Every move the tie turns downhill gets most or all of its
  gain from such points. The same reward breaks flat space itself at **κ = 8/11 ≈ 0.727 with six links and
  κ = 8/15 ≈ 0.533 with eight**, at both λ. Above those values, space is not stable against a single switch.
- **Is there a window where (a) the partly curled arrangements fall apart, (b) the fully curled one stays stuck, and
  (c) flat space's wall stays above the rest?** With the fixed form, only in two narrow slivers, and both are made by
  damage, not by the tie doing what it was meant to do:
  - six links, λ = 1.10: 0.650 ≤ κ < 0.727, and only in the weak sense (flat space stuck). Flat space's wall there
    (13.6 falling to 0) is below the fully curled state's (19.2).
  - eight links, λ = 1.25: 0.369 ≤ κ < 0.522. The fully curled state is held by a wall of only 4. Flat space's wall
    falls from 51 to 4 across the sliver.
  - There is none at six links with λ = 1.25 (the gas of 6-cubes has a free move at every κ) and none at eight links
    with λ = 1.10 (flat space breaks at 0.533, before the three-curled rung comes unstuck at 0.586).
- **A diagnostic variant** counts a damaged point as zero instead of negative, as if it were fully open. It is shown only
  because of the property above, and it is *not* the fixed form. With it, flat space is never affected. There is a
  window at six links with λ = 1.25 (2.0 ≤ κ < 2.83), and at λ = 1.10 in the weak sense only (κ ≥ 3.2). There is none at
  eight links: the three-curled rung gets *more* stuck as κ grows, because opening one of its directions moves its
  points from d = 1 to d = 2, which is uphill on the tie (3 to 4 per point).
- **"Three open, one curled" is never favored for κ ≥ 0, at any λ, as expected.** The reason is below: the tie makes the
  energy of the rungs a hill, so the lowest rung is always either all open or all curled.

## What was computed

The energy is H + κT, where H = 16(D(D − 1)/2 · N − S) + 4λX is the model energy (ASSUMPTIONS Q21). The tie is
T = Σ_v d(v)(D − d(v)), with d = `graphity.dimension.local_dimension_d` and D = links / 2. A point that is fully open
(d = D) or fully curled (d = 0) adds nothing. A point with some directions curled and some open adds d(D − d).

| Links | Arrangement | Points | What it is | d at every point |
|---|---|---|---|---|
| 6 | 4 × 4 × 18 | 288 | two directions curled | 1 |
| 6 | 4 × 12 × 12 | 576 | one curled | 2 |
| 6 | eight separate 4 × 4 × 4 | 512 | fully curled (gas of 6-cubes) | 0 |
| 6 | 6 × 6 × 8 | 288 | flat | 3 |
| 8 | 4 × 4 × 4 × 12 | 768 | three curled | 1 |
| 8 | 4 × 4 × 8 × 8 | 1,024 | two curled | 2 |
| 8 | 4 × 8 × 8 × 8 | 2,048 | one curled | 3 |
| 8 | four separate 4 × 4 × 4 × 4 | 1,024 | fully curled (gas of 8-cubes) | 0 |
| 8 | 6 × 6 × 6 × 6 | 1,296 | flat | 4 |

Flat 6 × 6 × 6 × 6 fit in the time: the whole eight-link set took under five minutes on the laptop.

**Method.** The script is `scripts/exact_walls_tie_d.py`. It uses `scripts/exact_walls_d.py`'s enumeration, which is
imported and not changed: one fixed point u1, every partner u2 on the same side, every pair of link slots, and the
same exclusions. There are two differences, and both make it more exact.

1. Every partner is searched, not only nearby ones. The nearby-partner shortcut was argued from squares, and the tie
   prices points.
2. Every candidate is priced from recomputations over the whole graph, before and after the switch: the hard-core rule,
   S, X, and d at every point.

So each switch has an exact signature (dS, dX, dT, and the change in how many points sit at each d), and its cost at any
(λ, κ) is −16 dS + 4λ dX + κ dT. A switch that changes none of these is counted as null and left out of the walls. The
16 × 4 test torus has one. None of the nine arrangements here has any.

**Tests** (`tests/test_exact_walls_tie_d.py`, 18 pass):
- at κ = 0 the kinds and ways match `exact_walls_d.py` on 16 × 4, 4 × 4 × 6 and 4 × 4 × 18;
- flat tori and single cubes have T = 0 at four, six and eight links;
- a torus with c directions curled has T = N(D − c)c: 2 per point for 4 × 4 × L and for 4 × 12 × 12, 3 for
  4 × 4 × 4 × 12 and 4 × 8 × 8 × 8, and 4 for 4 × 4 × 8 × 8;
- every switch out of 4 × 4 × 6 is recounted independently with networkx (its change of T, T+ and the d-histogram,
  ways included);
- the exact κ-interval logic is checked against a grid.

To reproduce: `python scripts/exact_walls_tie_d.py 4,4,18 4,12,12 6,6,8 4,4,4x8`, then the same with
`4,4,4,12 4,4,8,8 4,8,8,8 4,4,4,4x4 6,6,6,6`. The defaults are λ = 1.10 and 1.25 and κ = 0, 0.5, 1, 2, 4, 8. Add
`--json=file` to save every kind with its signature.

## Check: κ = 0 is O49 and O50

| Links | Arrangement | Formula on the record | λ = 1.10 | λ = 1.25 | Move (dS, dX) |
|---|---|---|---|---|---|
| 6 | two curled, 4 × 4 × 18 | 96 − 64λ (O49) | 25.6 | 16 | (−6, −16) |
| 6 | one curled, 4 × 12 × 12 | 96 − 48λ (O49) | 43.2 | 36 | (−6, −12) |
| 6 | gas of 6-cubes | 96 − 80λ (O49) | 8 | −4 | (−6, −20) |
| 6 | flat 6 × 6 × 8 | 64 (O51) | 64 | 64 | (−4, 0) |
| 8 | three curled, 4 × 4 × 4 × 12 | 160 − 112λ (O50) | 36.8 | 20 | (−10, −28) |
| 8 | two curled, 4 × 4 × 8 × 8 | 160 − 96λ (O50) | 54.4 | 40 | (−10, −24) |
| 8 | one curled, 4 × 8 × 8 × 8 | 160 − 64λ (O50) | 89.6 | 80 | (−10, −16) |
| 8 | gas of 8-cubes | 160 − 128λ (O50) | 19.2 | 0 | (−10, −32) |
| 8 | flat 6 × 6 × 6 × 6 | 128 (O50) | 128 | 128 | (−8, 0) |

Every entry matches. O50 used other tori for the eight-link rungs (4 × 4 × 4 × 36, 4 × 4 × 12 × 12, 4 × 6 × 8 × 12,
6 × 6 × 8 × 8). The walls are the same on these, so sides of 8 and 12 are long enough (O49's warning about short sides
does not bite here).

## The rungs with the tie (energy above flat space, per point, exact)

Each curled direction costs 4(λ − 1) per point, as before. The tie adds κ c(D − c) per point.

| Links | c curled | Energy above flat per point | λ = 1.10 | λ = 1.25 |
|---|---|---|---|---|
| 6 | 0 (flat) | 0 | 0 | 0 |
| 6 | 1 | 4(λ − 1) + 2κ | 0.4 + 2κ | 1 + 2κ |
| 6 | 2 | 8(λ − 1) + 2κ | 0.8 + 2κ | 2 + 2κ |
| 6 | 3 (6-cubes) | 12(λ − 1) | 1.2 | 3 |
| 8 | 0 (flat) | 0 | 0 | 0 |
| 8 | 1 | 4(λ − 1) + 3κ | 0.4 + 3κ | 1 + 3κ |
| 8 | 2 | 8(λ − 1) + 4κ | 0.8 + 4κ | 2 + 4κ |
| 8 | 3 | 12(λ − 1) + 3κ | 1.2 + 3κ | 3 + 3κ |
| 8 | 4 (8-cubes) | 16(λ − 1) | 1.6 | 4 |

With six links the tie is 2 per point for one curled direction and 2 for two. So it cannot tell the two partial rungs
apart. Only the ends are cheaper.

**A partial rung rises above the fully curled state itself** once κ is larger than:
- six links: 2(λ − 1) for two curled, 4(λ − 1) for one;
- eight links: 4(λ − 1)/3 for three curled, 2(λ − 1) for two, 4(λ − 1) for one.

At λ = 1.25 those values are 0.5 and 1.0, and 0.33, 0.5 and 1.0. At λ = 1.10 they are 0.2 and 0.4, and 0.13, 0.2 and
0.4. Beyond them, going from X to flat space by way of the rungs is uphill for the whole arrangement, not only at a wall.

## The walls as κ grows

A wall is the cost of the cheapest single switch out. At zero or below, the arrangement is no longer stuck.

**Fixed form (T).**

| Links, λ | Arrangement | κ = 0 | 0.5 | 1 | 2 | 4 | 8 | Wall reaches 0 at κ = |
|---|---|---|---|---|---|---|---|---|
| 6, 1.10 | two curled | 25.6 | 7.2 | −25.6 | −105.6 | −265.6 | −585.6 | 0.650 |
| | one curled | 43.2 | 7.2 | −70.4 | −230.4 | −550.4 | −1190.4 | 0.560 |
| | 6-cubes | 8 | 19.2 | 19.2 | 19.2 | 19.2 | 19.2 | never |
| | flat | 64 | 28 | −48 | −224 | −576 | −1280 | 0.727 |
| 6, 1.25 | two curled | 16 | −6 | −40 | −120 | −280 | −600 | 0.375 |
| | one curled | 36 | 0 | −80 | −240 | −560 | −1200 | 0.500 |
| | 6-cubes | −4 | 0 | 0 | 0 | 0 | 0 | never stuck |
| | flat | 64 | 28 | −48 | −224 | −576 | −1280 | 0.727 |
| 8, 1.10 | three curled | 36.8 | 6.4 | −46.4 | −158.4 | −382.4 | −830.4 | 0.586 |
| | two curled | 54.4 | −11.2 | −123.2 | −347.2 | −795.2 | −1691.2 | 0.450 |
| | one curled | 89.6 | −32 | −200 | −536 | −1208 | −2552 | 0.405 |
| | 8-cubes | 19.2 | 30.4 | 30.4 | 30.4 | 30.4 | 30.4 | never |
| | flat | 128 | 12 | −168 | −528 | −1248 | −2688 | 0.533 |
| 8, 1.25 | three curled | 20 | −14 | −68 | −180 | −404 | −852 | 0.306 |
| | two curled | 40 | −28 | −140 | −364 | −812 | −1708 | 0.333 |
| | one curled | 80 | −44 | −212 | −548 | −1220 | −2564 | 0.369 |
| | 8-cubes | 0 | 4 | 4 | 4 | 4 | 4 | stuck for every κ > 0 |
| | flat | 128 | 12 | −168 | −528 | −1248 | −2688 | 0.533 |

**What sets these walls** (the cheapest switch, from the full list; d-changes are counts of points):

- **Flat space.** Every point the move touches ends above D, so every one of them is damaged: most go to d = D + 1,
  and four go far above it. For example, with eight links: 28 points leave d = 4; 24 go to d = 5 and 4 go to d = 10,
  and dT = −360. All of the tie's gain is damage, and it is what breaks flat space at 0.727 and 0.533.
- **Partial rungs.** In every case the move opens one more direction at 12 to 28 points and damages 4. Damage supplies:
  - all of the gain for two curled with six links, where d = 1 → 2 gains nothing;
  - 67 to 88 % for one curled with six links, and for two and one curled with eight;
  - more than all of it for three curled with eight links, where d = 1 → 2 costs +24 to +28 on the tie and the damage
    pays −96 to −140.

  No move that unsticks a rung goes toward curling (d falling).
- **The fully curled state.** Its cheapest opening pays +24 (six links) or +40 (eight) on the tie, because points leave
  d = 0. That is why its wall rises at first. Then a larger switch takes over whose four damaged points exactly cancel
  that cost (dT = 0): (−10, −32) with six links, which costs 19.2 at λ = 1.10 and exactly 0 at 1.25; and (−14, −44)
  with eight, which costs 30.4 and 4. Most of that switch's ways join two cubes: all but 96 of 8,160 from one point with
  six links, and 24,576 of 27,552 with eight. So the fixed form's damage reward caps how stuck X can get.

**Diagnostic (T+, a damaged point counted as zero; not the fixed form).**

| Links, λ | Arrangement | κ = 0 | 0.5 | 1 | 2 | 4 | 8 | Wall reaches 0 at κ = |
|---|---|---|---|---|---|---|---|---|
| 6, 1.10 | two curled | 25.6 | 21.6 | 17.6 | 9.6 | −6.4 | −41.2 | 3.20 |
| | one curled | 43.2 | 27.2 | 11.2 | −20.8 | −102.4 | −294.4 | 1.35 |
| | 6-cubes | 8 | 20 | 32 | 56 | 104 | 200 | never |
| | flat | 64 | 64 | 64 | 64 | 64 | 64 | never |
| 6, 1.25 | two curled | 16 | 12 | 8 | 0 | −16 | −49 | 2.00 |
| | one curled | 36 | 20 | 4 | −28 | −112 | −304 | 1.125 |
| | 6-cubes | −4 | 8 | 20 | 44 | 92 | 188 | stuck for κ > 1/6 |
| | flat | 64 | 64 | 64 | 64 | 64 | 64 | never |
| 8, 1.10 | three curled | 36.8 | 40.8 | 44.8 | 52.8 | 68.8 | 89.6 | never |
| | two curled | 54.4 | 36.4 | 18.4 | −17.6 | −89.6 | −251.2 | 1.511 |
| | one curled | 89.6 | 53.6 | 17.6 | −56 | −248 | −632 | 1.244 |
| | 8-cubes | 19.2 | 49.2 | 79.2 | 139.2 | 259.2 | 499.2 | never |
| | flat | 128 | 128 | 128 | 128 | 128 | 128 | never |
| 8, 1.25 | three curled | 20 | 24 | 28 | 36 | 52 | 80 | never |
| | two curled | 40 | 22 | 4 | −32 | −104 | −268 | 1.111 |
| | one curled | 80 | 44 | 8 | −68 | −260 | −644 | 1.111 |
| | 8-cubes | 0 | 30 | 60 | 120 | 240 | 480 | stuck for every κ > 0 |
| | flat | 128 | 128 | 128 | 128 | 128 | 128 | never |

Even here, the two-curled rung with six links comes unstuck only through its four damaged points counted as open
(d = 1 → 2 is level on the tie).

## The window (a)–(c)

**The conditions:**
- (a) every partly curled rung has a wall of zero or less;
- (b) the fully curled state's wall is above zero;
- (c) flat space's wall stays above the others, in one of two senses:
  - weak: flat space is still stuck (its wall is above zero);
  - strong: flat space's wall is also above the fully curled state's, which is the wall a push has to pay first.

The intervals are exact: the walls are piecewise linear in κ, and every crossing was solved.

| Links, λ | Fixed form (T) | Diagnostic (T+) |
|---|---|---|
| 6, 1.10 | (a) κ ≥ 0.650; (b) every κ; flat stuck below 0.727 and above X's wall below 0.618. **Weak only: 0.650 ≤ κ < 0.727.** | (a) κ ≥ 3.2; (b) every κ; flat always stuck, above X's wall below 2.33. **Weak only: κ ≥ 3.2.** |
| 6, 1.25 | (b) fails at every κ: the gas is downhill below κ = 1/6 and has a free move above it. **None.** | (a) κ ≥ 2.0; (b) κ > 1/6; flat above X's wall below 2.83. **2.0 ≤ κ < 2.83, both senses.** |
| 8, 1.10 | (a) κ ≥ 0.586, but flat space breaks at 0.533. **None.** | (a) never (the three-curled rung). **None.** |
| 8, 1.25 | (a) κ ≥ 0.369; (b) κ > 0 (wall 4); flat stuck below 0.533 and above X's wall below 0.522. **0.369 ≤ κ < 0.522, both senses.** | (a) never. **None.** |

**So, for the form as fixed:** the window exists only as two slivers, each capped by flat space's own collapse. In both,
the rungs come apart through damaged points rather than by opening together. No κ gives the tied cascade the term was
meant to produce. For the diagnostic form: one window at six links with λ = 1.25, and none at eight links.

## Three open, one curled (eight links)

It is never favored for κ ≥ 0, at any λ. This follows exactly from the rung energies above. Per point, the energy of the
rung with c directions curled is

E(c) = 4(λ − 1)c + κ c(D − c).

For κ > 0 this is a downward-bending curve in c (its second difference is −2κ). So its lowest value over c = 0 … D is
always at an end: all open or all curled, never in between. At κ = 0 it is a straight line, and again an end wins. This
is the symmetry of d(D − d), as expected.

*Arithmetic only, not a proposal:* one curled would be the lowest rung for −4(λ − 1) < κ < −4(λ − 1)/3. That is a
negative κ, which rewards half-open points, the opposite of a tie, and lies outside Update 30's κ ≥ 0. Selecting three
is what Update 30's second constant (the size of the tied group) is for.

## What this means (*ours, unverified*)

1. **The fixed form needs one clarification before any run: what d(D − d) should mean at a damaged point.** Read
   literally, the term pays the network to break itself. Above κ ≈ 0.53 (eight links) or 0.73 (six links), even flat
   space would come apart. The two readings computed here are:
   - literal: damage is rewarded;
   - clipped (T+): damage counts as open.

   Others are possible, for example measuring d only along the directions of the lattice rather than over all pairs of
   links. Choosing among them is a change to the knob's form, so under S1 it is the owner's call and a dated decision
   before any run.
2. **A tie of this shape cannot help a cascade that steps down the rungs.** It raises the middle of the ladder. Once κ
   is past 2(λ − 1) (six links) or 4(λ − 1)/3 (eight), the first partial rung sits above X itself, so X would have to
   climb to get there. What the tie can favor is an opening that skips the rungs: fully curled on one side of a front,
   fully open on the other, with the tie paid only along the front. Single switches on uniform tori do not price that.
   The next exact question would be the cost of such a front per unit of its area, against the energy released per
   point behind it.
3. **Eight links behave worse than six under either reading.** The three-curled rung (d = 1) is on the rising side of
   the tie's hill. Its first opening is taxed (3 to 4 per point), so it gets more stuck as κ grows, which is the
   opposite of (a). Conditions (a) and (b) together ask for a tie that taxes the first step out of the fully curled
   state (d = 0 → 1) and rewards every step after it. That is a hill peaked at d = 1, next to the curled end. A
   symmetric d(D − d) peaks in the middle (d = 2 with eight links), and with six links it is level between d = 1 and 2.
4. **Nothing here says what a run would do.** These are single-switch walls on perfect arrangements. The runs of T30 and
   T33 showed that the walls a bath actually has to pay can be passes over several moves (O62). The pre-registered
   reruns named in Update 30 should wait for point 1.

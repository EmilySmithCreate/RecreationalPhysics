# Design brief: the order of opening defines the release

Written 2026-09-25, evening, after the owner's change of direction (about 18:50 ET). It replaces the typed-stores design
of VISION Update 31, which was drafted earlier the same evening as a brief, never committed, and has been withdrawn. This
is a design only: nothing is built and nothing has run on the cloud. Numbers marked **preview** come from uncommitted
scratch scripts run on the laptop while this was written (some of them read committed data); the scripts of section 6
must reproduce them before anyone quotes them. With any λ ≠ 1 or a direction tie this is our family around the model,
never combinatorial quantum gravity. Six-link statements carry VISION Update 24's caveat. Physics reasoning here is
*ours, unverified*; positions marked as the owner's are hers.

## The answer first

**Her position.** In X and in space the three directions are interchangeable, so it is chance which one opens first.
There is one kind of energy, and it pays every push. What distinguishes the directions is the *order* in which they
open, and the order sets what each release becomes: the first opening gives ordinary matter and radiation, the second
dark matter, the third dark energy.

**Recommendation.** Label each release by the order of opening at each point, read from `local_dimension_d` (d, the
number of open directions at a point), and keep the books with the state-function tally of section 3. It is exact. It
adds nothing to the dynamics, so detailed balance and conservation are untouched. It needs no labels. Because d counts
open directions without naming them, it cannot favor one direction over another. And it runs on saved graphs today.
Build first: the tally script and an exact symmetry and free-energy script (section 6). Then the first experiment
(section 7), with interchangeable points, which the validated chain of T42 already supports.

**What the model says so far.**
- **The plain energy gives equal releases, 1 : 1 : 1.** Unequal releases by order need a term that depends on d. With
  O70's shape that term gives 5 : 27 : 68, but as a fit of two constants, and it leaves every later opening needing its
  own push (section 4).
- **"The first takes the most" fails for the walls and for any single move.** The walls are 8, 25.6 and 43.2 at
  λ = 1.10. The first move out of each rung loses a similar share of the renamings.
- **It holds for the *completed* opening with interchangeable points.** At 512 points the first opening loses 81.5 in
  ln(renamings), about 10³⁵ times fewer; the later openings change the count only by a factor of six. So whichever
  direction goes first carries a symmetry-breaking cost that nothing later pays (section 5).

## 1. Her position, and what it replaces

**Her words, put in order.** Once it is space, the three directions are interchangeable, as they are before, in X, so it
is random which of the three becomes red. There are not really three types of energy: all three directions need the same
kind of energy to unfold. The directions are defined by the order in which they unfold, and the order defines the type of
matter or energy released.

**What it replaces.** There are no typed stores and no direction labels. One bath pays every push. Which direction opens
first is decided by chance. In standard language this is spontaneous symmetry breaking: the rule is symmetric and the
outcome is not (general knowledge, to verify).

*Ours:* with interchangeable points there is not even a fact about *which* direction opened. The three choices give the
same arrangement up to renaming.

## 2. Exact facts that support it

Checked while writing this brief: isomorphism with networkx; side-preserving renamings counted with `graphity.symmetry`
(igraph).

| Arrangement | What it is | Side-preserving renamings |
|---|---|---|
| 4 × 4 × 4 (X, six links) | Isomorphic to the 6-cube Q6 (C4 = Q2, so C4³ = Q6) | 23,040 = 2⁶ · 6! / 2, which includes every permutation of Q6's six coordinates |
| 4 × 4 (inside 4 × 4 × L) | Isomorphic to Q4 | 4 × 4 × 18: 6,912 = 384 × 18; 4 × 4 × 32: 12,288 |
| 4 × 12 × 12, 4 × 8 × 16 | One direction curled | 4,608; 2,048 |
| 6 × 6 × 6, 8 × 8 × 8 | Flat, all axis permutations | 5,184 = 12³ · 3! / 2; 12,288 |
| Eight separate 6-cubes | X at 512 points | 3.202 × 10³⁹ = 23,040⁸ · 8! (O55) |

**What the table shows.**
- **X does not single out three directions.** A curled direction of length 4 is two hypercube coordinates, and X's
  renamings mix coordinates freely across directions.
- **The two curled directions of 4 × 4 × L are not separate either.** They form one Q4, whose four coordinates can be
  permuted freely.
- **Flat space is isotropic.** Its renamings include every permutation of the axes.
- So the only distinction between directions that survives from X to flat space is the order in which they open.

(Preview, T30's 24 saved gas end states, λ = 1.10.) Among the 22 replicas that opened, the starting slot label with the
most open points is spread over the three: 8, 8 and 5 replicas, and one tie. But the starting labels mark only 2 to 27 %
of points as open, because after rewiring most open pairs join links of different starting labels. So a starting label is a weak record of what opened.
The count d is exact.

## 3. How the model labels a release by order

**Definitions** (D = 3 with six links):
- d(v) is the number of open directions at point v. A point with d > D is **broken**; it is not on the ladder.
- E(d) = a(D − d) + f(d) is the energy of a point on the rung with d open directions (0 ≤ d ≤ D). Here a = 4(λ − 1) is
  the curling cost per direction, and f is a direction tie that depends only on d (zero without one).
- r_k = E(k − 1) − E(k) is the energy released by the k-th opening at a point.
- m_k is the number of points with k ≤ d ≤ D, that is, the points that have made their k-th opening and are not broken.

**The tally.** Define the defect energy as H_def = H − Σ_{d ≤ D} n_d E(d), where n_d is the number of points at d. Then,
starting from X (where H = N E(0)):

    N E(0) − H(t) = Σ_k r_k m_k(t) + n_broken(t) E(0) − H_def(t).

The left side is the energy the region has given off. On the right: the releases by order (first, second, third), plus
the curling energy of points that broke instead of climbing the ladder, minus the energy now held in defects. In a sealed
run, what has been given off sits in the bath, because `sealed_d` conserves H + stores. This is an identity, so it closes
to the last unit whenever it is computed correctly. With the plain energy, r_k = a at every k, and the releases are
1 : 1 : 1 per point.

**Points and regions.**
- The order is counted per point: "the first opening here", whichever direction it was.
- `piece_labels` on the mask {d = k} gives the regions sitting on each rung. Regions at different rungs at the same time
  need no special rule, because the tally is per point.
- A point that skips a rung (0 → 2) counts as having made both the first and the second opening, since m_k counts d ≥ k.
- Re-curling lowers m_k, so the tally is net.
- Broken points are reported on their own and never given an order. They enter m_k if they later settle on a rung.
  (Preview.) Every cheapest move out of a curled rung lifts 12 points one rung and moves 4 more by several rungs or
  breaks them, and flat space's cheapest exit is all breakage. So broken points appear from the first move on, and they
  need their own bucket.

(Preview, the same 24 end states, plain energy, a = 0.4.)
- **The tally closes where the end state is a clean mixture of rungs.** H_def is exactly 0 in 10 of 24 end states, 8.8
  to 114.4 in the rest, and no point is broken at the end. This is six links repeating what Update 8 saw in two
  dimensions.
- **One replica, worked through.** It ends with 276 points at d = 2 and 236 at d = 3. Its first openings released 204.8,
  its second 204.8, and its third 94.4, which totals 504.0 = 614.4 − 110.4, exactly what the region gave off.

*Ours:* in the model the "type" is a label on the tally. Every release goes into the same bath. The model can count the
three releases; it cannot make them behave differently.

## 4. What makes releases unequal by order: a tie on d

**The key observation** (exact). d counts open pairs without naming them, so any term that depends only on d is unchanged
by every renaming. Each opening's release then depends on how many directions are already open, never on which. The
direction tie of Update 30 is therefore "order defines the type" automatically. The releases are a − f(1),
a + f(1) − f(2) and a + f(2), and their total stays 3a (O70).

**Two cases on the record.**
- **Plain curling cost (f = 0):** 1 : 1 : 1.
- **O70's budget-fitted shape** (f(1) = 0.85a, f(2) = 1.04a): 0.15a : 0.81a : 2.04a = 5 : 27 : 68.
  - It is a fit: two constants chosen to hit two ratios.
  - It uses today's dark-energy share, which changes with time. The ratio fixed at birth is ordinary : dark matter,
    about 1 : 5.4 (Planck 2018; general knowledge, to verify). Hitting that one ratio fixes one constant.
  - Its walls at λ = 1.25 are 6.2 for X, 14.9 with one direction open, 19.4 with two open, and 64 for flat space. So X
    is stuck, flat space is stable, and every later opening needs its own push.
  - *Ours:* that fits her picture if the pushes come from outside: "the remainder returns to the black hole and can
    start another burp".
  - Across λ the pushes are 12.1, 25.2 and 36.5 at λ = 1.10, and 0.32, 4.2 and 2.2 at 1.40; at 1.50 nothing is stuck.
    The first push is never the largest.
- **The "follow" form (O68) does the reverse.** The later openings follow with no push, but the first opening's release,
  a − 2κ, turns negative once κ > a/2.

**What would make it a prediction.** The model's own requirements would have to confine (f(1)/a, f(2)/a), without being
told the budget, to a narrow region that contains the fit. The requirements:
1. X is stuck.
2. Flat space's wall is at least twice the largest push (O65 (5)).
3. Each later opening either needs its own push or follows by itself, whichever her picture needs.
4. λ lies inside the window.

The tie is Update 30's knob. The exact scripts already price it (`exact_walls_tie_shape_d.py`). A run needs it in the
kernel, with a local update of d.

## 5. Interchangeable points: the first opening pays the counting

**The counts** (verified at 512 points, as ln of the number of renamings): X, the gas, 90.96; two directions curled
(4 × 4 × 32), 9.42; one curled (4 × 8 × 16), 7.62; flat (8 × 8 × 8), 9.42.
- The completed first opening loses 81.5, which is 0.159 per point, multiplied by g, in free energy.
- The second loses 1.79 (a factor of six), and the third wins the same 1.79 back.

**What this means** (*ours, unverified*). Whichever direction goes first carries the whole symmetry-breaking cost. That is
the model's counterpart of her "red takes the most, so it is the limiting factor": the first opening is the bottleneck
in free energy.
- Under the budget fit at λ = 1.25 (a = 1), the first opening releases only 0.15 per point. So at this size it runs
  uphill in free energy above g ≈ 0.94, and would not complete however large the push.
- With the plain energy (a release of 1 per point) that happens only above g ≈ 6.3.

**What counting does not do** (preview, verified). It does not make the first *move* much dearer. The first single move
out of each rung loses ln 8.95 (X), 8.03 (two curled) and 6.93 (one curled): a defect in a torus breaks its translations
too. The later openings pay that at their first move and win it back as they complete; the first opening never wins it
back. So "the first takes the most" is a statement about the whole opening, not about its wall.

**Caveat.** X here is a gas of separate cubes, and 10.6 of its 90.96 is the permutation of the cubes. Per point, the loss
grows slowly with the number of cubes, as ln(k!)/k. A connected X has not been computed.

## 6. Exact first tests (laptop, no cloud, exploratory)

- **`scripts/exact_release_order_d.py`** prints:
  - the isomorphisms and counts of section 2, as tests;
  - E(d) and r_k for f = 0 and for a given f;
  - the walls (from `exact_walls_tie_shape_d`);
  - the interchangeable free energy of each rung at given g and λ, and the counting loss of each rung's first move;
  - the couplings above which the first opening runs uphill.
- **`scripts/scan_release_tie_d.py`** scans a grid of f(1)/a, f(2)/a and λ against the requirements of section 4. It
  reports the allowed region, whether that region pins r_2/r_1 (and r_3/r_1), and where the budget point falls.
- **`scripts/tally_release_order.py`** reads saved final graphs (T30's gas and tori, T33, T34, T39, T41). For each it
  prints n_d, n_broken, R_k = r_k m_k, n_broken E(0), H_def, the bath's gain and the spread of starting labels. It is
  tested on perfect rungs (H_def = 0) and on the identity closing to the last unit.

## 7. The first experiment, in her format

**Setting.**
- Six links, sealed, interchangeable points (`graphity.interchangeable_d`, validated for T42), with the named-points
  control (`weighted: false`) beside it.
- The gas of eight 6-cubes (N = 512) at λ = 1.10: X is stuck there, with a wall of 8. The plain energy, so no new knob.
- The smallest push that starts each opening, found by bisection: E\*₁ from X, E\*₂ from the two-curled torus, E\*₃ from
  the one-curled torus.
- Recorded every block: the tally, the census and, in the control, the starting labels.

**(1) Her claim about reality.** The directions are interchangeable before and after. Which opens first is chance. One
kind of energy pays every push. The order of opening sets what the release becomes, in today's proportions. The first
opening takes the most, and so it limits the burps.

**(2) What the model must show if the claim holds.**
- (i) No direction is preferred. In the named control, the first-opened starting label is spread evenly over the three
  across replicas; in the interchangeable runs this holds automatically.
- (ii) The tally closes to the last unit in every replica.
- (iii) The releases by order stand in the budget's proportions.
- (iv) The first opening is the hardest: E\*₁ > E\*₂ and E\*₃ with interchangeable points, and less so or not at all in
  the named control, the difference being the counting.

**(3) The missing ingredient if not.**
- **If (iii) fails:** the tie on d. The plain energy gives 1 : 1 : 1, so this is expected, and the tie's shape stays a
  fit until the scan shows the requirements pin it.
- **If (iv) fails even with interchangeable points:** the counting acts on completion, not on the push. The ingredient
  would then be a term that taxes the first step out of full curling (a hill peaked at d = 1;
  `direction_tie_first_look.md`, point 3), or the multi-move pass (O62).
- **If (i) fails:** something in the start or in the moves breaks the symmetry. That is a fault to find before anything
  else.

**Ours, for the record.**
- (i) holds.
- (ii) holds where the end state is a clean mixture of rungs, with defect energy otherwise.
- (iii) comes out 1 : 1 : 1.
- (iv): with named points E\*₁ < E\*₂ < E\*₃, near the walls of 8, 25.6 and 43.2. With interchangeable points the first
  opening stalls more often without its push being larger, because the counting acts on completion.

## 8. What is not known

- Whether counting slows the first opening's completion in a run. Only the equilibrium counts are exact.
- Whether a connected X behaves as the gas does.
- Whether the three releases, which are identical in kind in the model, could ever behave differently. The model can
  count them; it cannot show that one becomes matter and another dark energy.
- Every preview number, until the scripts reproduce it.

# Soft space, stage B: lengths that charge only for curving, and the twisted ring (draft brief, 21 October 2026)

*A design brief for the author. Nothing is built or run from it until she has answered the questions at the end
(VISION S1). Kinds of statement are marked: exact, published (with its source and how much of it was read), ours
(the assistant's, unverified), and hers.*

## What is decided, and by whom

- **Hers, 20 October (VISION Updates 76, 77):** soft space in two stages; stage A, one number per point, is built and
  checked (ASSUMPTIONS Q26); stage B is the aim: a length on every link and every square's diagonal, with an energy that
  charges only for curving, in three directions, with time through the waves' momentum.
- **Hers, 21 October (Update 78):** the links carry curling energy; stage B is where that is described.
- **Hers, 21 October (Updates 85, 86):** the toy's particle is a twist carried around a closed ring of diagonal links,
  possibly braided in threes; matter and antimatter carry opposite twists; an untwisted ring is light; masses are equal
  because the energy is in the curl, not the ring's length.

## What the published work says (from `docs/reading/notes/2026-10-20_soft_space_prior_work.md` and
`docs/reading/notes/2026-10-21_matter_as_loops.md`)

- **Regge calculus** (as reviewed in [Ham09], pp. 135 to 143, read in part): space is built from flat pieces whose edges
  have lengths; curvature sits at the hinges, as the angle missing around them (the deficit angle); the energy is the sum
  over hinges of each hinge's size times its deficit angle ([Ham09] Eq. 518). Expanded about flat space on a hypercubic
  lattice it gives Einstein's gravitational waves, but only when the lattice is made rigid with its face and body
  diagonals; the extra lengths do not travel.
- **Particles as twists and braids** (Skyrme's winding number; Faddeev and Niemi's knots, read in full; Bilson-Thompson's
  braided ribbons, read in full): a twist that cannot be undone is a conserved whole number; its mirror is the
  antiparticle; the two unwind into radiation; in the braid model the unbraided state is the photon and quark colors are
  the three positions of the odd ribbon.

## What is exact already (ours, from the toy's structure and textbook geometry)

1. **Diagonals join points of one kind.** Every link joins two points of different kinds; a square's two diagonals join
   its opposite corners, one pair of each kind. So rings of one kind of point can only be made of diagonals (Update 85).
   On the flat sheet, each kind's diagonals form a square lattice of their own, turned 45° and spaced √2.
2. **In two directions, an energy that charges only for curving does nothing.** On a closed surface the deficit angles
   always add up to 2π times (2 minus twice the number of handles) (Gauss and Bonnet; textbook, to verify), whatever the
   lengths. So in a two-direction toy, Regge's energy is the same for every arrangement of one shape: it gives the
   balance of curl and uncurl for free (every positive curvature paid for by negative curvature elsewhere) and no
   dynamics at all. Dynamics, waves and a pull need the three-direction toy (six links), or in two directions an extra
   term in the square of the curvature.
3. **Counting lengths in three directions** ([Ham09]'s count carried down a dimension; ours, to derive): a metric has 6
   numbers per point; the cubic lattice's 3 edges per point cannot hold it (they stretch but cannot shear); adding the
   three face diagonals and the body diagonal gives 7 per point, one more than needed. Which of those 7 is redundant on
   the toy's own graph is the first exact calculation (item 6 of the reading note's list).

4. **The cube's counts** (ours, exact; Update 87). In the lattice each cube owns one point, three links, three squares,
   three face diagonals joining points of one kind and three joining the other, and four body diagonals inside it, not
   shared, each joining points of different kinds (the rigid lattice of [Ham09] uses one of them per point). Lengths in link lengths: √2, √3, and for larger boxes √6, 3,
   √11. Her braid of three diagonal twists per cube, and her dark loops on the faces, are built on these.

## The design, in pieces

1. **Where the lengths live.** On each link, and on one or both diagonals of each square, and (three directions) one
   body diagonal per cube. The wiring (the switches) stays as it is; lengths ride on it. When a switch removes a square,
   its diagonals go with it; when a square is made, its diagonals are born at a declared default length.
2. **The energy.** Regge's sum over hinges of size times deficit angle, plus a term for total volume (the cosmological
   term), plus or instead of the toy's present curling cost: her choice (question 3).
3. **The twist.** A ring is a closed cycle of diagonals among points of one kind. Its twist is a whole number carried
   with it: how many times a small frame, carried once around the ring, turns. Kept by every move that does not cut the
   ring; changed only where two rings meet or where the snap acts (the count that only the snap may change). A
   twisted ring is matter (+1) or antimatter (−1); an untwisted ring is light. Braids of three rings follow
   Bilson-Thompson's rules if she chooses the combination.
4. **The ring's price.** Her rule: the energy is in the curl, not the length, so a ring costs one fixed amount per unit
   of twist, whatever its length. In Regge's energy alone a ring's cost would depend on its geometry, so this is a
   declared price (question 4).
5. **Sampling and time.** As in stage A: the wiring by switches, the lengths by molecular-dynamics trajectories with
   momentum refreshes. *Ours, general knowledge, to verify:* sampling Euclidean gravity runs into a known problem, its
   energy has no lowest value (the conformal-factor problem, Gibbons, Hawking and Perry 1978), so lengths can run away;
   the published remedies are a squared-curvature term, a causal structure (causal dynamical triangulations) or a bound
   on lengths. One must be chosen before anything runs (question 5).

## Tests, cheapest first (each exact unless marked)

1. Gauss and Bonnet in code: on random length assignments of a two-direction torus, the deficit angles sum to zero to
   machine precision (rule-6 check of the deficit-angle code).
2. The three-direction count: zero modes and travelling modes of Regge's energy about the flat six-link space with
   diagonals, against [Ham09]'s four-direction count.
3. A ring's energy against its length, with and without her per-ring price; and whether any ring is stuck (every move
   out costs).
4. The twist kept: every local move that does not cut a ring keeps its twist (complete enumeration on small tori).
5. Opposite twists meeting: a +1 ring and a −1 ring brought together unwind into untwisted rings, and where the energy
   goes (measured, after 1 to 4).
6. Measured, after 1 to 5: the first registered tests of stage A carried over (a disturbance's speed; two knots' pull),
   now with waves of both shapes.

## Questions for the author

1. **Two directions or three first?** Two is cheap and gives the curl-uncurl balance exactly, but no dynamics (exact
   item 2). Three gives waves and a pull and is the aim. Our recommendation: write the deficit-angle code in two
   directions for test 1, then go straight to three.
2. **One diagonal per square or both?** One makes the squares into triangles, Regge's standard; both give a ring lattice
   for each kind of point (exact item 1). Her rings need the diagonals of one kind; if matter and antimatter are opposite
   twists on either lattice, one diagonal per kind would do.
3. **The energy:** curving only (Regge plus volume), or Regge plus the present curling cost 4(λ − 1) per surplus square?
   The burp's release lives in the curling cost today.
4. **The ring's price:** one fixed amount per unit of twist, whatever the length (her "the energy is in the curl"), or
   whatever Regge's energy gives?
5. **The runaway remedy:** a squared-curvature term, a causal structure, or bounded lengths.
6. **Braids:** single twisted rings first, braids of three after, or both from the start?

## Her answers so far (21 October; VISION Update 90)

- Question 1: three directions, six links per point.
- Question 2: the objects are the cube's corner-to-corner lines and its face diagonals; the edges' square loops are the
  dark kind, denser, with no spin. *Exact:* one kind's six face diagonals in a cube form a regular tetrahedron, whose
  faces are the smallest diagonal rings, triangles of three; a cube has four corner-to-corner lines (her "three" to be
  settled).
- Her predictions: test 4, every move that does not cut a ring keeps its twist; test 5, opposite twists meet and
  dissolve into two untwisted rings, photons, moving one link per tick.
- Later the same day (Update 91): question 1, two directions first, then three; question 2, one diagonal per square is
  matter's (the other kind's for antimatter, to confirm); question 4, a fixed price per twist set by the diagonal's length
  in proportion to the others; question 6, single rings first, the dark edge loops, then matter's braids. Question 3:
  curvature and the curling cost differ, since a tightly curled tube is flat as a surface (zero deficit, checked in
  code), so curving only would give no burp; recommendation to keep both, hers to decide. Still open: question 5 (the
  runaway remedy).
- Built: `graphity.regge` (Q27), the two-direction curvature, test 1 of the list above passed.

## What it cannot show

Anything about the real universe (VISION, "What no outcome can show"). A Regge energy on the toy's graph is our family,
never the published model; a twisted ring carried as a whole number is put in, not derived, and becomes interesting only
if what it does (binding, unwinding, which rings stay stuck) is not.

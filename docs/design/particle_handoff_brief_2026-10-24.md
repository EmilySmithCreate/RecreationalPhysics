# The particle handoff of 24 October: what checks out, the mapping onto the ring picture, and what is built (brief, 24 October 2026)

*Written for the owner and the next session. The handoff is kept as received at
`docs/geometric_particle_model_handoff_2026-10-24.md` (written for a coding assistant; her ideas are its section 1).
Kinds of statement: **exact** (arithmetic or enumeration, with its script), **published** (with its source and how much
was read), **ours** (the assistant's, unverified), **hers**. Physics from memory is marked "general knowledge, to
verify" and has a reading task in section 6. At λ ≠ 1 the toy is our family around the published model, never
combinatorial quantum gravity.*

## Current definitions (read this box first; rule 20)

The box of `docs/design/regge_stage_b_brief.md` stays the source of truth for the ring. This box holds the
refinement she chose on 24 October ("Refines it"), **proposed, to confirm as one set (section 3)**. Nothing in code
depends on it yet.

- **Strand (proposed):** ~~a face diagonal of a cube (her "tape" of 23 October)~~ one segment carrying a twist of one
  third, one way or the other; which segment is open (worksheet Q1). A lone strand is neutral (handoff idea 3;
  "charge is only spin", 23 October). *Corrected 24 October, after a check: her tape "run to its opposite corner,
  there are 4 tapes" is a cube's body diagonal, √3, joining the two kinds, not a face diagonal; and her later words
  of 23 October give the third to the longer length and the half to √2 ("short halfs and long thirds"), while her coin
  puts matter and antimatter on a square's two face diagonals. Her own statements pull Q1 both ways.*
- **Closure (proposed):** a ring closes only with a whole twist, so three thirds braid into one closed unit (her tape
  picture of 23 October; her answer of 24 October, "3 thirds"). The electron is three thirds closed, carrying a
  photon-like curl's energy (handoff idea 4).
- **Light (proposed):** the untwisted excitation travelling along links that already exist (handoff ideas 1 and 2),
  in the toy the wave of the phase field of `graphity.u1`. This refines "an untwisted ring is light" (Update 86).
  What "half-curl" means stays three variants (her answer of 24 October): A1 a pulse half a wave long, A2 a 180°
  bend, A3 a half turn of phase round a loop.
- **Unchanged and still open:** matter against antimatter (opposite thirds, or the two diagonals of one square, 23
  October); the ring's price; the twist's definition on the graph ("not yet defined", confirmed 23 October); what
  gluons carry (a bound half-curl or none; both kept).

## 1. What was decided on 24 October (hers; VISION Update 96)

1. The handoff **refines** the ring picture; it does not replace it.
2. The electron to test is **three thirds**, with her added idea: *"the 3 twists colapse 3 versions of arrangement.
   the entropy decrease of 1 becoming 3 is 1 photon."* Read (to confirm): when three strands close into an electron,
   three distinguishable arrangements become one, and the entropy given up leaves as one photon.
3. **Build the published lattice photon into the toy** (a phase on every link; the squares as its loops): a new
   ingredient under S1, `graphity.u1`, ASSUMPTIONS Q29, with its own reproduction gate before any result is read.
4. **Half-curl stays three variants.**

## 2. The exact looks (`sandbox/particle_handoff_looks.py`, about 20 s; output `sandbox/out/particle_handoff_looks_2026-10-24.txt`)

A sandbox look: it can narrow or kill, never support. Built lattices only.

1. **Her idea 1 is Wilson's lattice gauge theory, and it fits the toy's own flat lattices.** On the flat four-link
   torus the linear waves of a phase on every link have one polarisation; on the flat six-link torus, two, as light
   has. The rest are gauge modes (one per point, less one) and one holonomy per direction. Every frequency is
   2 √(Σ sin²(kᵢ/2)) to 10⁻¹⁴. The speed limit is one link per tick, reached only at long wavelengths, and is never
   exceeded; but it is one link per tick only because the field's inertia and κ were set equal (a choice, the
   handoff's "speed chosen by fiat" flag), and short waves prefer the lattice's axes (2.7 % faster along a cube
   diagonal than along an axis at |k| = 1).
2. **The three readings of half-curl under one energy.** A3: a half turn of phase round a square is the most
   expensive state a square can have (2κ), and a full turn costs exactly nothing, so only the turn modulo a whole
   turn is seen; a pulse launched with a half turn of holonomy did not travel (99 % of its energy stayed where it
   started; its links spin over the top, because the energy per square is bounded). A2: a path that turns back on
   itself carries U U⁻¹ = 1, holonomy zero for every field value, so a 180° bend is undefinable for a field on fixed
   links and needs stage B's lengths. A1: a pulse half a wave long travels at 0.90 links per tick and keeps 89 % of
   its energy together over 40 ticks, and its energy is exactly proportional to amplitude squared (9.806 at both
   amplitudes tried), so "half a cycle" fixes no unit of energy in a classical wave. *General knowledge, to verify:*
   the unit E = hν belongs to the quantum of a mode, with ν set by the wavelength.
3. **The charge ledger.** On any closed graph, each link adds to one point what it takes from another, so the charges
   (Gauss's law) add to zero: to 10⁻¹⁴ for real values, to 0 mod 3 for three-valued labels. Brute force over all
   531,441 three-valued labellings of a closed 2 × 3 grid: exactly the 243 source patterns with total 0 mod 3 occur,
   and all of them do. So a closed space cannot hold a net third, and the smallest allowed sets are a pair (one
   each way) and a same-way triple: the meson and baryon patterns, from the count alone. ~~*Ours:* this is her tape
   rule's "a loop needs a full twist to close", in the language of Gauss's law; both say a lone third is confined.~~
   *Corrected 24 October, after a check:* this is neutrality over the whole closed space, not confinement: a single
   third here with its partner far away is allowed. Confinement (a cost that grows with separation) would need an
   energy, which the ledger does not supply. Her tape rule (a loop needs a whole twist to close) is a separate
   statement about one strand, not this count.
4. **The 2π gate.** A quarter turn of the cubic lattice, applied four times, returns every link to itself with its
   own orientation (checked; the energy is unchanged by one quarter turn). So any state built on link labels (angles,
   thirds, twists) comes back with sign +1 after a full turn: a spinor's −1 cannot come out of this state space.
   It must be put in (spinor variables, assumed, not explained) or come from a configuration space with a loop that
   cannot be shrunk and a sign chosen round it (Finkelstein and Rubinstein 1968; for a framed ring, the belt trick;
   general knowledge, to verify). This is the handoff's "record the obstruction clearly", and it is recorded.
5. **Thirds against observed charges.** Every observed particle in the handoff's table obeys 3Q + t ≡ 0 (mod 3),
   with t = quarks minus antiquarks (exact arithmetic on the table). So an object carrying one of the quarks' thirds
   has charge 2/3 or −1/3 plus a whole number, never −1: the electron cannot carry a single quark-third, and three
   thirds (t ≡ 0) keep the relation, which is what she chose. *Published:* this relation is what allows the Standard
   Model's gauge group to be divided by a subgroup of Z6, and which subgroup is not decided by experiment (Tong, JHEP
   07 (2017) 104, abstract read). Three thirds per electron is the braid model's pattern ([BT05], read in full: there
   a full twist of a ribbon is one third of a charge; for her a third of a twist is not a charge, so the two differ in
   what a twist is while agreeing on the count of three).
6. **The 1 × 1 × 4 line** (handoff idea 8): length √18 = 3√2, joining two points of one kind (coordinate sum even),
   passing through no lattice point. The smallest ring of face diagonals has the same length; an arithmetic
   coincidence with no weight (rule 13).
7. **Her entropy idea.** Three ordered positions with twist labels: three equal twists have one placement, a set with
   one odd label has three (the braid model's three colours are exactly the positions of the odd strand, [BT05]
   Sec. II). So going from a coloured triple to an all-alike one gives up ln 3 = 1.099 of entropy (in units of k).
   *What checks out (general knowledge, to verify; Landauer 1961):* giving up ln 3 of entropy into surroundings at
   temperature T requires at least kT ln 3 of energy carried away, and one photon can carry it. *What does not:* that
   price is a ~~floor proportional to T, not a fixed energy, so it cannot by itself set a photon's energy or the
   electron's mass~~ minimum, not a value: even at one formation temperature (her 21 October "at a cirtain specific
   temp") it says how much at least, never how much *(corrected 24 October, after a check)*; and with interchangeable
   positions every set has one placement, so the idea needs ordered strands (the interchangeable-points rule). The
   literal words "1 becoming 3" would be a gain of entropy; read as 3 becoming 1, to confirm. *Added 24 October,
   after a check (exact, from the same output):* the triples with three placements (+ + 0, + + −) total 2 and 1 mod 3,
   so they are not neutral sets under item 3's count; three becoming one therefore needs the labels themselves to
   change on closing, not only their order. Energy leaving on closing would make the closed unit lighter than its
   parts (a mass defect, general knowledge, to verify), the opposite sign from her 21 October "connecting energy" that
   holds most of a proton's mass. And one photon per electron formed has to be squared with her 23 October account, in
   which a pair cancels into "exactly 2 photons, same as it took to create them".

## 3. The mapping onto the ring picture, read back as one set (her confirmation owed; rule 20)

| Handoff (24 Oct) | Ring picture (Updates 85 to 91; notebook of 23 Oct) | Proposed reading |
|---|---|---|
| Flat links exist without a photon | The toy's links; stage A and B fields ride on them; but 23 Oct: the edges "are not real in our model they are just helpful to visualize" | The field of `graphity.u1` lives on the toy's links (edges); **tension** with her 23 Oct line, question 7 |
| Photon = travelling half-curl | "An untwisted ring is light" | Light is the untwisted travelling excitation; on a ring, a phase running round with no net third |
| Neutral one-third twist | The tape ~~on a face diagonal~~ corner to corner (a body diagonal, √3; "4 tapes") must twist ⅓ either way (23 Oct; corrected 24 Oct) | One strand = one segment with ±⅓, neutral; which segment is worksheet Q1 |
| Electron = third + photon-curl (now three thirds) | Three come together into a braid with one full twist (23 Oct) | Electron = three thirds closed, plus curl energy |
| Charge from the whole configuration | "Charge is only spin, speed of spin matters" (23 Oct) | **Open:** which conserved quantity obeys Gauss's law and gives pairs; spin speed is not yet a count |
| Mass as stored curl | "Twist count = curling energy = mass" (23 Oct) | Same |
| Opposite twists cancel into waves | Two diagonals of one square, the coin (23 Oct) | **Open:** ⅓ clockwise against anticlockwise, or one kind's diagonal against the other's, or both |
| Gluon: confined, half-curl bound or absent | not in the ring picture | Both kept; published relative named in section 6 |

Questions, to be answered in one sitting:
1. Is a strand one segment with a third of a twist (which segment is worksheet Q1), and does a ring close only with
   three, or also as a pair, one third each way (the two-part meson route of handoff idea 6)?
2. Is "a lone third cannot close" meant as confinement, a cost that grows as a third is pulled away? (The charge
   ledger gives neutrality over the whole space, not that cost.)
3. Charge: if charge is spin speed, what in the model is counted so that charges come in cancelling pairs?
4. Matter against antimatter: opposite thirds, the square's two diagonals, or the one as the other?
5. The entropy idea: three arrangements becoming one, with ln 3 leaving as one photon?
6. Gluons: keep both readings, or choose?
7. Light on the edges: on 23 October the edges joining the two kinds "are not real in our model they are just helpful
   to visualize"; on 24 October the photon field was built on them. Do edges carry light while diagonals carry the
   twist (two jobs), or should the field ride on diagonals instead?

The loop-rule worksheet of 23 October (`docs/design/loop_rule_worksheet_2026-10-23.md`) has a dated addendum listing
what this handoff and its looks move, slot by slot; read the two together in one sitting.

## 4. What is built (ASSUMPTIONS Q29)

`src/graphity/u1.py`: a phase on every link of any of the toy's bipartite graphs, oriented from kind 0 to kind 1;
the squares (every 4-cycle, so a curled direction's ring counts too); holonomies; Gauss's law; gauge
transformations; the energy; the linear-wave matrix; velocity-Verlet evolution; Wilson-action Monte Carlo with the
detailed-balance argument in the docstring; and the exact two-direction answer for the reproduction gate. Tests
(`tests/test_u1.py`, 17): squares against networkx and `cqg_d.total_squares`; gauge invariance; charges on closed
graphs; the wave spectrum on flat tori in two and three directions; energy conservation; the local Monte Carlo update
against full recomputation; wrapped phases and same-seed reproducibility; the exact answer's limits; a short gate.
Not in this piece: the field riding on a graph whose wiring switches; twist labels; any coupling to the curling
cost.

**Gate U1** (TASKS): the average square on the flat 6 × 6 and 10 × 10 four-link tori against the exact torus answer,
at five couplings, with the acceptance written before the run. **Failed on 24 October at β = 8** (the sampler froze in one winding sector;
diagnosis and the winding move in TASKS, Gate U1's reading); Gate U1′, with a winding move, failed the same day by one point (10 × 10, β = 8,
3.65 errors against 3.5); nothing from Q29 is read until a gate passes.

## 5. Next, in order

1. Her answers to section 3, read back as one set.
2. Gate U1 run and read (`scripts/run_u1_gate.py`, `configs/gate_u1_2d.json`).
3. The handoff's test A with the field in place, pre-registered with her prediction: a launched wave on the toy's
   flat six-link space and on a curled torus (does a curl, whose ring is a square the field sees, scatter or trap
   light?).
4. Twist labels on strands (Z3 per face diagonal), switchable off, once question 1 is answered; then the handoff's
   tests B (closure census with dynamics) and E (pair creation only, on a closed space).
5. The quantum gate (test C) stays a reading task until a state space is chosen: on link labels it fails by section
   2, item 4.

## 6. Reading tasks (prior-work template; general-knowledge statements above)

| # | Task | Settles | Sources (bibliographic data checked at Crossref 24 Oct where marked) |
|---|---|---|---|
| 1 | Wilson's lattice gauge theory and the 2D character expansion | Q29's model and the gate's formula at their source | Wilson, PRD 10, 2445 (1974) ✓; Kogut, RMP 51, 659 (1979) ✓ |
| 2 | Charge and triality; the Z6 question | Section 2, item 5 beyond the abstract | Tong, JHEP 07 (2017) 104 ✓ (abstract read); Baez and Huerta, Bull. AMS 47, 483 (2010), to check |
| 3 | Spin from configuration-space loops | The 2π gate's way out | Finkelstein and Rubinstein, J. Math. Phys. 9, 1762 (1968) ✓ |
| 4 | Landauer's bound | Her entropy idea's price | Landauer, IBM J. Res. Dev. 5, 183 (1961) ✓; Bennett's review (2003), to check |
| 5 | Centre vortices: tubes of the gluon field carrying a third of a turn | The nearest published "one-third twist", neutral, belonging to the gluon field and tied to confinement; bears on her gluon question | 't Hooft (1978); Greensite's review (2003); to check |
| 6 | The handoff's own reading list (section 6 there) | Its benchmark table's sources (PDG, CODATA) | as listed there |

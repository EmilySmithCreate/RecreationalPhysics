# The loop rule: a worksheet for one sitting (prepared 23 October 2026; not yet read back)

*For the owner (Emily) and the session that reads it back to her. It decides nothing. It collects, slot by slot, what
she has said about the loop rule of her particle picture, what is exact in the toy beside each statement, where a
statement meets measured physics, and the one question each slot needs, so that her answers can be given in one sitting
and read back as one consistent set before any arithmetic (CLAUDE.md rule 20; `docs/HANDOFF_2026-10-23.md`, item 2.4).*

**Kinds of statement.** **Hers:** her words, quoted exactly (typos kept) from `sandbox/NOTEBOOK.md` with the date and
the line number as of commit 38e03057. **Exact:** arithmetic, geometry or complete enumeration, with where it was done.
**Measured:** a registered run and its verdict. **Sandbox:** a look under rule 16 (it can kill a claim, never support
one). **Published:** with how much of the source was read. **General knowledge, to verify:** a physics statement from
memory that no reading note in the repository sources yet. **Ours:** interpretation, unverified. Nothing below promotes
a statement from one kind to another.

**What was read for it.** `sandbox/NOTEBOOK.md`, every entry of 21 to 23 October (lines 1999 to 2278); VISION Updates
84 to 92 (read only); `docs/design/regge_stage_b_brief.md`; the handoff of 23 October, item 1.7 and section 3; the
handoff of 22 October, sections 2.4 and 4; `sandbox/LOG.md`, 20 to 23 October; ASSUMPTIONS O22, O107, O148 and Q27;
`docs/papers/particles/outline.md`, sections 1 to 4; `docs/reading/notes/2026-10-21_matter_as_loops.md`,
`2026-09-26_dark_charge.md` (for 5.36) and `2026-10-19_cp_violation_and_baryogenesis.md` (for the size of the excess);
`sandbox/spring_ratio_look.py` and its output.

**Terms used here (ours).** A *slot* is one part of the rule that needs her answer. A *strand* is one twisted segment
of a loop (her "tape"). A *segment* is one straight piece of the lattice: an edge (link, length 1), a face diagonal
(across one square, √2) or a body diagonal (corner to corner through a cube, √3). The *two kinds* of point are the two
sides of the toy's checkerboard: every link joins one of each.

## How to use it

1. Read the section "Contradictions and tensions to settle first" with her before the slots. Several slots cannot be
   answered until one of those is settled, and each entry says what kind of conflict it is and names the question that
   settles it.
2. Ask the questions in the order given in the last section. Write each answer in her words as a new dated notebook
   line (this file's quotations are not edited).
3. Read all the answers back to her as one set, checked against each other and against the "exact" lines here, and
   confirm every reading marked "to confirm".
4. Only then write the rule into the "current definitions" box of the stage-B brief, and only then do the arithmetic of
   the section "What arithmetic waits on these answers".

## The slots at a glance

The chat worksheet of 23 October named seven slots (NOTEBOOK.md:2263): strand, twist, braid, electron, dark loop,
energy law, survival. The record names four more the rule cannot leave open; they are slots 8 to 11 here.

The status column is ours, a reading of the record for her to confirm.

| # | Slot | Status | Latest statement of hers | Settled by |
|---|---|---|---|---|
| 1 | Strand | Open: which segment carries it | 23 October (:2274) | Q1 |
| 2 | Twist | Fixed in part (twist count is mass, not charge); open: what "1/3" is a third of | 23 October (:2265, :2274) | Q2 |
| 3 | Braid, proton, neutron | Fixed in part (three strands, one whole twist); open: is the braid a proton or a quark | 23 October (:2264, :2265) | Q3 |
| 4 | Electron | Stated once; open: its twist count against the proton's | 23 October (:2264, :2267) | Q4 |
| 5 | Dark loop | Superseded twice; current form unclear | 23 October (:2264, :2274) | Q5 |
| 6 | Energy law and binding | Fixed in part (more twists, more mass); open: is there a binding term | 23 October (:2265, :2274) | Q6 |
| 7 | Survival rule | Never defined as a slot; two meanings in her words | 23 October (:2264, :2266, :2274) | Q7 |
| 8 | Spin and charge | Spin tied to charge from 21 October, with two exceptions; latest "Charge is only spin" | 23 October (:2265) | Q8 |
| 9 | Matter against antimatter | Open: three rules on the record, a fourth phrase on 23 October | 23 October (:2264, :2266) | Q9 |
| 10 | Light | Two forms on 21 October (untwisted loop; a twist that can be undone); in tension with 23 October's rule for the tape | 23 October (:2264) | Q10 |
| 11 | Kinds and generations | Open | 23 October (:2274) | Q11 |

---

## Slot 1: the strand

**(i) Hers.**

> "i can imaging the curve completing, same type points canceling, and transforming the hypotenuce relationship from
> flat space into a circle which stores energy like mass the cost of a full curl and 2 coming together create 2
> photons." (21 October; NOTEBOOK.md:2146)

> "A ring can be longer if the space it was made of was bigger, the length of the hypotenuse freezes into the length
> of the ring and different lengths make diff subatomic particles that hold the same energy. No edge link can but these
> are hypotenuse links can. In this theory." (21 October; :2151)

> "8 square space, with 3 corner to corner hypotenuse twists per cube" (21 October; :2174)

> "let's just focus on the 3 cube throughlines and the 6 cube side diagonals and assume the link limit is the 6 of 3
> dimensions." (21 October; :2204)

> "yes I counted wrong lol good correction" (22 October, 21 October in her day, answering that a cube has four
> corner-to-corner lines, not three; :2234)

> "So imagine a piece of tape that can be stuck to the corner of the cube. But it needs to be angled flat on a cube
> wall in order to stick. This tape run to its opposite corner, there are 4 tapes. The tape also needs to stick to its
> opposite corner." (23 October; :2264)

> "I meant a twist, a 3d hypotenuse, not this whole thing. Maybe an electron, maybe a quark" (23 October; :2267)

> "how much curl in the hypotenuse loop and whether it forms a side length loop or a 45degree inner square that 3d
> opens up." (23 October, a question; :2273)

> "A ring of side-length links is the ordinary square -> my idea is that this does not exist, only the hypotenuses
> exist fundamentally: sqrt2 and 2 ((sqrt2)^2+(sqrt2)^2=c^2 , c=2 , twist_2 = 1/3, twist_sqrt2 = 1/2, twist is always
> the same), and they are either flat 3d space or they are looped on themselves and therefore matter which being energy
> held in space curves (not curl) space, gravitational waves, as the stretchy space acts as a fluid and the link
> stretch and curves through it in wave form?" (23 October; :2274 (c))

**(ii) Status.** Fixed (23 October, :2267): the curl she means is a twisted hypotenuse, not a link with an extra square.
Open: which hypotenuse. On 21 October her strands were the cube's corner-to-corner lines (:2174, :2204) and its face
diagonals, which join points of one kind (:2147, "same type points canceling"; :2204). The count of corner-to-corner
lines was corrected to four (:2234), and after that the record stopped carrying them as objects "without her saying so"
(VISION Update 92). Length never set mass in her words: her first statement already gave every length the same energy
(:2151 to 2153, "different lengths make diff subatomic particles that hold the same energy"), :2167 restates it ("the
length has no impact on mass", slot 6), and :2170 keeps lengths as the mark of a kind ("different braids of matter and
antimatter loops of different lengths", slot 11). (VISION Update 86 records :2167 as replacing Update 85's "different
lengths are different particles"; her words do not say that.) On the morning of 23 October the strand is a tape along a
body diagonal, a "3d hypotenuse", twisting by thirds (:2264, :2267). Later on 23 October she wrote that only two
hypotenuses exist, √2 and 2, with "twist_2 = 1/3" and "twist_sqrt2 = 1/2" (:2274 (c)). Read literally, that list leaves
out the body diagonal (√3). *Ours, a reading to confirm:* "2" may be a miscomputed length for her corner-to-corner tape,
since the third-twist she gives it is the one she gave the tape that morning (:2264), the half twist on √2 is the one
she gave dark matter (:2264, "Dark matter carries a half twist"), and (d) of the same message assigns the two lengths to
matter and dark matter. She did not say which she meant; that is C1.

**(iii) Exact beside it.**
- A link joins the two kinds; a face diagonal joins two points of one kind; a body diagonal joins the two kinds
  (VISION Updates 85 and 87; brute force on a 4 × 4 × 4 lattice, Update 87).
- Per cube in the lattice: 3 edges, 3 squares, 3 face diagonals of each kind, 4 body diagonals, not shared (Update 87;
  the brief's definitions box).
- One kind's six face diagonals in a cube form a regular tetrahedron. The smallest closed ring of face diagonals is a
  triangle of three (24 through each point, length 3√2 ≈ 4.24); the smallest ring of edges is the square (12 through
  each point, length 4) (`sandbox/LOG.md`, 21 October; `sandbox/diagonal_rings.py`). Body diagonals make no ring of one
  kind (the brief's definitions box).
- With one diagonal per square chosen by kind, as `graphity.regge` does (Q27), a cube is cut into five tetrahedra that
  use no body diagonal, six lengths per point (Update 92; the brief's box). So in stage B as built, the tape's body
  diagonal has no length of its own.
- Which hypotenuse a right angle makes (enumerated for this worksheet, exact). Method, given here because the scratch
  script is not in the repository: take the 6 edge directions, the 12 face-diagonal directions and the 8 body-diagonal
  directions from one point, keep every pair at right angles, and record the length of their sum and whether the two
  share a zero coordinate (that is, lie in one coordinate plane, a plane parallel to a cube face). Result: an edge and a
  face diagonal at right angles have hypotenuse √3, the body diagonal (1² + (√2)² = 3), and never lie in one coordinate
  plane; two face diagonals at right angles always lie in one coordinate plane and have hypotenuse 2, which is a straight
  line two edges long along a lattice axis, the diagonal of the 45° inner square (also the notebook's check, :2275 (c)).
  So a length-2 line, like a face diagonal, lies in a coordinate plane; of the three, only the body diagonal leaves the
  coordinate planes. No link or diagonal of the toy or of stage B's triangulation has length 2.
- In the stiff toy (no lengths) a hypotenuse joins two points of one kind that share exactly two neighbors, the same
  sharing as a tightly curled pair, so it carries one fixed amount of curl; "how much curl" is a number only in stage
  B, where a diagonal has a length and the flat value is √2 (:2273, check).
- In two directions the hypotenuses round a point form the 45° inner square, four of them (quarters); in three, one
  kind's face diagonals form the tetrahedron whose smallest ring is a triangle (thirds) (:2273, check).
- Her twisted hypotenuse has no object in the stiff toy and no twist in stage B yet (:2267; Update 92).

**(iv) Where it meets measured physics.** "different lengths make diff subatomic particles" meets the fact that every
particle of one kind has the same mass (general knowledge, to verify; Update 85). Her words never put length into mass
(every length holds "the same energy", :2153, restated at :2167), so the fact bears on lengths as kinds (:2170): a
kind's length has to be one of a fixed set, not whatever the space was where the ring formed (Update 85). Nearest
published model: Bilson-Thompson's braided ribbons of the network ([BT05], read in full;
note `2026-10-21_matter_as_loops.md`, section 3).

**(v) Question 1.** Which segments are your strands? (a) The four body diagonals of a cube, length √3, joining the two
kinds of point (21 October, "3 corner to corner hypotenuse twists per cube", :2174; and your tape of 23 October); (b)
face diagonals, √2, joining one kind (21 October, "same type points canceling", :2147; 21 and 22 October); (c) only √2
and 2, as you wrote later on 23 October (note that 2 is a straight line two edges long along a lattice axis, not a
diagonal of any cube); (d) by "2" you meant the corner-to-corner line, whose length is √3, so your two lengths are √2
and √3; (e) more than one of these, with different jobs (say which does what).

---

## Slot 2: the twist

**(i) Hers.**

> "It could have a twist in it like one point is facing the other direction (to be turned away from its closest same
> type neighbor) so matter and antimatter would hold a twist in different directions" (21 October; :2154)

> "So a photon is a twist that can be undone and a matter or antimatter particle is a twist that cannot be undone."
> (21 October; :2165)

> "charge is the twist count and the twist count spins" (23 October; :2263)

> "If it connects with no twist, it's not as far as it can be from its matched point, so rule says it must twist,
> either 1/3 clockwise or counterclockwise. But in order for the loop to close on itself it needs a full twist. So 3
> coming together somehow, 3 come together add their twists into a braid with one unit of charge, one twist." (23
> October; :2264)

> "A higher twist count holds more curling energy and has more mass, not more charge." (23 October; :2265)

> "twist_2 = 1/3, twist_sqrt2 = 1/2, twist is always the same" (23 October; :2274 (c))

> "2 degree of freedom space: twist count and clockwise/counterclockwise, and hypotenuse length (matter/dark matter)"
> (23 October; :2274 (d))

**(ii) Status.** Fixed, by her revision of 23 October (:2265 supersedes :2263 the same day): the twist count is
curling energy and mass, not charge. Fixed: the matter strand twists by a third, clockwise or counterclockwise (:2264;
"twist_2 = 1/3", :2274 (c)); the dark strand by a half (:2264, "Dark matter carries a half twist"; "twist_sqrt2 = 1/2",
:2274 (c)); a closed loop needs a whole twist. Open: what the third is a third of (C2); where the third lives, the body
diagonal or the length 2 (C1); what "twist is always the same" holds fixed (C1). Not hers to settle: the twist is not
yet defined on the graph.

**(iii) Exact beside it.**
- The three planes that contain a body diagonal and a cube edge are 60° apart (the notebook's check, :2264 answer;
  recomputed for this worksheet). A tape flat in one plane that turns to the next has turned 1/6 of a full turn, which
  is 1/3 of a flat tape's own repeat (a flat tape looks the same after a half turn, 180°). Three such steps make a half
  turn, and a tape closed after a half turn is one-sided (a Möbius band); six make a full turn (:2264 answer).
- Her √2 and 2 twists (1/2 and 1/3) stand in the ratio 3 : 2 while the lengths stand 1 : 1.41, so "twist is always
  the same" is neither the same twist per unit length nor the same total twist (:2275, check (c)).
- A frame carried round a ring (the twist) is not conserved by itself: the conserved count of a closed ribbon is its
  linking number, which is twist plus writhe (writhe: how much the ribbon's center line coils), and twist trades with
  writhe (Călugăreanu, White and Fuller; named in Update 92, to read: the handoff of 22 October, research task 2). The
  toy keeps no embedding once a switch fires, so a twist needs a framed or ribbon graph (a graph that carries a ribbon
  on each link) or lattice knots. Tests 4 and 5 of the brief, and her predictions for them, are held until this is
  defined (Update 92; the brief's box; the handoff of 23 October, item 2.2). A reading note for that item
  (`docs/reading/notes/2026-10-23_twist_on_a_graph.md`) was being written by another session when this worksheet was
  prepared, uncommitted; it was not read here, and the session that reads this worksheet back reads that note first.

**(iv) Where it meets measured physics.** Her twist "that cannot be undone", kept by every move that does not cut the
ring (her "yes" of 21 October, :2209), has the shape of a conserved charge such as baryon number (general knowledge,
to verify; paper 18's outline, section 1). Published: in Bilson-Thompson's model each ribbon carries a full twist one
way, the other way or none, and "A twist through ±2π is interpreted as an electric charge of ±e/3" ([BT05] Sec. II,
read in full by an assistant agent; as quoted in the note, section 3). There the thirds of charge come from whole
twists on each of three ribbons, not from thirds of a twist.

**(v) Question 2.** When a strand twists "1/3", a third of what? (a) A third of a full turn (120°, two of the 60°
steps between the lattice's planes), so three thirds make one full turn and the closed loop is two-sided; (b) a third
of a flat tape's own repeat (60°, one step), so three make a half turn and the loop closes one-sided like a Möbius band,
and a whole twist needs six; (c) something else (say what).

---

## Slot 3: the braid, the proton and the neutron

**(i) Hers.**

> "then these loops form particles: quarks, quarks form protons, etc etc." (21 October; :2101)

> "yes I agree, but per the braids, could be a combination" (21 October, answering the record's recommendation of "the
> twist carried around a closed loop of links, the Skyrmion's"; :2157; VISION Update 86 records it as her decision of
> the twist form)

> "these are braids, not closed curls - there are 3 diagonals in a cube so the 3 twists are made and immediately twist
> together into a braid The three quark colors are the three ways to order the strands." (21 October; :2172)

> "3 quarks to a 1 unit of positive or negative charge, based on the quark type, right?" (21 October; :2179)

> "the quarks have diff spins, they group in specific ways, etc." (21 October; :2114)

> "The proton is a braid, full twist, spins much slower, so it needs a bunch of twists, spinning together making
> protons and not spinning neutrons, to balance the 1 unit of charge in each electron." (23 October; :2264)

> "Protons weigh how much in relation to an electron? Much more. Need to think through. Protons usually need a button
> to stabally be +1 and balance an electron. Why?" (23 October; :2264)

> "Thanks for the neutron clarification. The neutron helps make the protons not repel so much." (23 October; :2265)

> "(angle/direction/color come from movement/spin)" (23 October; :2274 (d))

**(ii) Status.** Fixed: three strands come together in a braid carrying one whole twist (21 and 23 October). Fixed
(23 October, :2265): the neutron's job is to keep protons from repelling. The chat answer before it read her "button"
as the neutron and said a lone proton is stable; her reply thanks it for "the neutron clarification". Open: whether the
braid is a proton (three strands as three quarks) or a quark (on 21 October loops form quarks and quarks form protons,
:2101, which bears on Q3 (c)); whether the neutron is the same braid "not spinning" (:2264, not revised by :2265);
where color comes from: the three orders of the strands (21 October) or movement and spin (23 October; whether "color"
there means quark color or the color of light is to confirm), C8.

**(iii) Exact beside it.**
- A cube holds 3 face diagonals of each kind and 4 body diagonals (Update 87), so "three per cube" is exact for the face
  diagonals of one kind, and the triangle of three face diagonals is a definite three-strand object (LOG, 21 October).
  For body diagonals the count is four.
- The stiff toy has no binding at a distance: defects' energies add exactly unless they touch, and where they touch
  the pair costs 16 less than twice one (O22). Any energy that holds a braid together is a new ingredient.
- Braids, like twists, need an embedding the toy does not keep (Update 92).

**(iv) Where it meets measured physics.** General knowledge, to verify: a proton is two up quarks and one down
(charge +1), a neutron one up and two down (0); quark charges are +2/3 and −1/3 (Update 87 (a)); a lone proton is
stable and neutrons are needed only in nuclei with more than one proton (:2264 answer); a free neutron decays in about
a quarter of an hour; the proton is about 1,836 times the electron's mass. Published, abstract only: most of the
proton's mass is the energy of the binding field, not the quarks' masses ([Durr08], [Wil12]; note, section 1).
Published, read in full: in Bilson-Thompson's model every first-generation particle is one braid of three ribbons,
and a quark's color is the position of the odd ribbon ([BT05] Sec. II; note, section 3); so a proton, three quarks, is
three braids (the record's reading, VISION Update 86), which differs from reading one braid as a proton.

**(v) Question 3.** Is one braid of three strands (a) a proton, each strand a quark, with a neutron the same braid
not spinning (your 23 October words); (b) a proton, with a neutron a different braid (say how it differs); or (c) a
quark, so that a proton is three braids, nine strands, as in Bilson-Thompson's model?

---

## Slot 4: the electron

**(i) Hers.**

> "An electron as a single twisted strand, spinning so over time it exists looking like a sphere. Dark electron is the
> same but the single side twist. Its spin is energy turning it to a magnet with enough heat to gives it one negative
> charge in terms of its effect on other particles." (23 October; :2264)

> "If a twist is excited by a photon, it continues to spin and generates a negative electric charge and if an
> antimatter/reverse uncurl twist one does we get an anti electron, they would cancel out and release exactly 2 photons,
> same as it took to create them. Same with dark matter electrons and dark matter anti electrons." (23 October; :2264)

> "I meant a twist, a 3d hypotenuse, not this whole thing. Maybe an electron, maybe a quark" (23 October; :2267)

**(ii) Status.** Stated on 23 October only. Its charge clause is consistent with her later revision (:2265, "Charge is
only spin ... The heat is the frozen magnet analogy"). Open: how much twist the single strand carries. If a closed loop
needs a whole twist (slot 2), a single closed strand carries the same whole twist as a proton's braid; the record's
reading of 23 October was that both carry three thirds (:2263), C7.

**(iii) Exact beside it.**
- There is no strand, twist or spin object in the toy yet (:2267; Update 92), and no object for light, so "two photons"
  cannot be scored (Update 92).
- In the stiff toy a curl (a link on an extra square) and an uncurl (a missing square) are not mirror images: prices
  1 : 4 at λ = 1.25, and no one- or two-switch defect of a flat sheet carries curl alone (LOG, 21 October;
  `sandbox/out/curl_uncurl_mirror_2026-10-21.txt`). So a raw curl and a raw uncurl cannot be an electron and a positron
  of equal mass.

**(iv) Where it meets measured physics.** General knowledge, to verify: the electron's charge is −1 and its spin 1/2,
the same fixed amount for every electron; it has no measured size; it is a lepton, made of no quarks (VISION
Update 36); the electron and the positron weigh the same; an electron and a positron meeting at rest make two photons,
or three, depending on how their spins line up (note, section 1, marked general knowledge there); making a pair from
light takes at least twice the electron's mass-energy; quantum spin is not a ball turning, so "spinning so over time
it exists looking like a sphere" is a picture the measured spin does not carry (Update 87 (b), for quarks).

**(v) Question 4.** How much twist does an electron carry, compared with a proton's braid? (a) The same, one whole
twist on one closed strand, so the electron's smaller mass must come from somewhere other than its twist count (then
slot 6 says where); (b) less, one third on a single strand that does not close on itself (then what keeps it from
unwinding?); (c) something else.

---

## Slot 5: the dark loop

**(i) Hers.**

> "matter is a loop from 3d and dark matter is a loop from 2d. that's why we have dark versions of everything but they
> dont interact." (21 October; :2148)

> "dark matter could outweigh ordinary matter several times over- dark matter is the curls from the square sides of the
> cube. Middle of the cube, 3 dimensional, gets a braid. Each side of the square gets a curl loop and an uncurl loop.
> Each loop has the same mass as a single twist of the 3d braid quark. 6. They don't braid but they double against
> their neighbor cube wall. No spin, no electric charge. More energy stored because it's a tighter loop. So heavier. By
> maybe 3x? A dark matter proton has 2 dark quarks twisted. No spin no charge. Per 2cubes, 10 sides, 5 units"
> (21 October; :2185)

> "dark matter manuvers on square ends, not twisty, and is denser compared to the matter that moves through the
> diagonals." (21 October; :2195)

> "the square edge is shorter than the hypotenuse through the center of the cube. it holds more curl per link lenth,
> vs the center lines. plus there is more of them, so they hold more energy than the diagonal links. more dense, no
> diagonal spin." (21 October; :2206)

> "let's do the single rings the dark matter. they may or may not braid, different types of dark matter particles. then
> do matter's equivalent." (22 October, 21 October in her day; :2224)

> "I think 10 billion that pair their antimatter give 2 extra squares/ 6 matter (3 throu each cube) and 6 dark matter
> (each ssquare shares each side), maybe with dark matter accelerating faster because it moves on the edges not the
> diagonals and is t electrically charged" (22 October, night; :2260)

> "which slows the movement of the quark through space, compared to the dark matter as the flat sides." (23 October;
> :2262)

> "Dark matter carries a half twist, so 2 loops are needed for a dark matter Full twist. A 12 set makes 4 matter units,
> and 12 is the minimum it takes to make matter because they must combine to whole numbers. A 12 set makes 3x12 dark
> matter units, each has 6 faces shared by 2, 36. 9x as many." (23 October; :2264)

> "Dark electron is the same but the single side twist." (23 October; :2264)

> "the energy in a curl is curl energy and it is packaged in dark and regular matter each with an exact mass."
> (23 October; :2274 (b))

**(ii) Status.** Superseded in steps, and the current form is not stated. 21 October: curl and uncurl loops on the
cube's square faces, unbraided, no spin, no charge, perhaps three times heavier; the same day, "not twisty" and denser
(:2195), and loops of edges, denser, "no diagonal spin"; on 23 October, in the entry before the half twist, "the dark
matter as the flat sides" (:2262). 23 October, morning: dark matter carries a half twist, two loops per whole twist,
36 per twelve cubes; "Dark electron is the same but the single side twist". 23 October, later: side-length rings do
not exist, and the hypotenuse length marks matter against dark matter (:2274 (c), (d)), which reads as dark matter on
√2 with a half twist (reading to confirm). The later message removes the edge loop of 21 October if it is read literally;
whether she meant that is contradiction C5.

**(iii) Exact beside it.**
- The smallest ring of edges is the square (length 4); the smallest ring of face diagonals is the triangle of three
  (length 4.24) (LOG, 21 October). Per cube there are 3 edges and 3 squares against 3 face diagonals of each kind, so
  edges are not more numerous than diagonals (Update 90).
- Rings of 4 and 4.24 differ by about 6 % under a tension law or a bending law, in opposite directions; the per-cube
  counts give dark : matter between 1 and 2.3 under every simple law (the chat answer recorded at :2260). Her "curvature
  squared 12 % more" (:2262) is (4.243 / 4)² = 1.125 (arithmetic).
- Her 36 is exact as the lattice's per-cube share of faces, 3 per cube (each cube has 6 faces, each shared by 2), so
  36 per twelve cubes of an unbounded lattice; a finite set of twelve cubes has more distinct faces (a 2 × 2 × 3 block
  has 52). Her ratio of 9 with a half-twist dark unit gives 4.5 (the chat answer at :2264).
- The toy already holds curled loops of four edges on a square: the column (14 units at λ = 1.25) and the double column
  (8 units), measured as stuck knots of fixed energy (T51, T55; O107). Update 92 named them as a possible match; "Is her
  dark loop the column?" is still unanswered (the handoff of 22 October, section 2.4).
- A closed curve can be knotted only in three dimensions (note, section 2, marked general knowledge, standard
  topology), which is one exact sense in which "a loop from 3d" can carry what "a loop from 2d" cannot. A face diagonal
  lies in one face; a body diagonal does not (the right-angle enumeration under slot 1).

**(iv) Where it meets measured physics.** Dark matter outweighs ordinary matter by 5.36 (Planck 2018 densities, Ω_c h²
/ Ω_b h² = 0.120 / 0.0224, from a search summary of the abstract in `docs/reading/notes/2026-09-26_dark_charge.md`;
VISION Update 41 records the two densities checked at [Planck18]). Dark matter barely touches itself (σ/m < 0.47 cm²/g,
[Harvey15], abstract only) and has not flattened into a disk ([Schutz18], abstract only), both via the note, section 8.
It falls exactly as ordinary matter does and gravitates as three-dimensional mass (general knowledge, to verify; note,
section 8; :2260 answer), which bears on "accelerating faster". Arithmetic on general-knowledge inputs (Update 87): if
each dark loop weighed about three protons, only about one per billion photons could survive, so dark loops would have
to cancel too and leave an excess of their own.

**(v) Question 5.** What is a dark loop now? (a) A curl loop of four edges on a cube face, untwisted ("not twisty",
:2195), with no spin and no charge (21 October); (b) a face diagonal, √2, carrying a half twist, two per whole twist
(23 October); (c) the toy's own curled column of four edges (14 units) or double column (8 units); (d) something else.
In each case: does it spin?

---

## Slot 6: one energy law, with its binding term

**(i) Hers.**

> "the loops are but most of the mass isn't loops but the connecting energy ie the full metastable particle is a
> secondary force that comes to be around how to turn a curl link loop (string) into a matter particle in 3d space."
> (21 October; :2112)

> "at a cirtain specific temp, particles form, gathering curl uncurl into a proton or nuetron, each captures the
> lightforce of a 1 unit atomic bomb." (21 October; :2124)

> "which stores energy like mass the cost of a full curl" (21 October, of the loop a hypotenuse closes into; :2148,
> slot 1)

> "They have identical mass because the energy is in the curl and exact not related to how stretched space was the
> length has no impact on mass." (21 October; :2167)

> "whatever the link length the hypotenuce length as a proprtion of the lengths and steady in its proportion to the
> mass / energy of the cube points 3 curl and 3 uncurl hypotenuses. each can only cancel it's own length of
> hypotenuse. the actual link lenth is irrelevant only the relationships are real the points are not real." (22
> October, 21 October in her day, answering the brief's question 4; :2221)

> "are they different? I don't understand? more curve is curl. gravety is curve." (same entry, answering the brief's
> question 3, whether the energy should charge for curving only or keep the curling cost as well; :2235)

> "Q4, a ring's price: a fixed amount per twist: yes, for each diff link length in relation to the other hypotenuse."
> (same entry; :2236)

> "Compare the amount of energy held in a 4 unit ring and a 4.24 unit ring if made of same material." (22 October,
> night; :2260)

> "curvature squared 12 % more" (23 October; :2262)

> "Let's see where this would take the energy law, and continue to refine. Protons weigh how much in relation to an
> electron? Much more. Need to think through." (23 October; :2264)

> "A higher twist count holds more curling energy and has more mass, not more charge." (23 October; :2265)

> "the energy in a curl is curl energy and it is packaged in dark and regular matter each with an exact mass." (23
> October; :2274 (b))

**(ii) Status.** Fixed: more twists, more mass (23 October); a fixed price per twist (22 October). Still owed from the
handoff of 22 October (section 4): which of its four ring-price statements stands. *Ours, to confirm:* her 22 October
answer has a part of the third (a price set by which diagonal, independent of stretch) and a part of the fourth (a twist
cancels only a twist of its own length). Open: whether there is a binding term. On 21 October most of a particle's mass
is "connecting energy"; on 23 October mass is the twist count, with no binding named. Neither statement withdraws the
other (C4). Her mechanisms on the record for a proton's mass: the connecting energy (:2112); a proton or neutron
"gathering curl uncurl" that "captures the lightforce of a 1 unit atomic bomb" (:2124 to 2125); and :2264's slower
spin needing "a bunch of twists" for one unit of charge, which under :2265 (more twists, more mass) makes the proton
heavier (C7). Also open, to confirm: on 21 October in her day "more curve is curl" (:2235); on 23 October matter
"curves (not curl) space" (:2274 (c)), which separates the two.

**(iii) Exact beside it.**
- The stiff toy's prices, link by link: a missing square costs 4, an extra square 4(λ − 1), so 1 : 4 at λ = 1.25 and
  equal only at λ = 2; a link can miss two squares but carry only one extra (four against one with six links), so no λ
  makes the two kinds mirror images (LOG, 21 October).
- No binding at a distance in the stiff toy (O22, above).
- A tightly curled tube is flat as a surface, so an energy that charges only for curving gives no burp, and the curling
  cost has to stay beside curvature (Update 91, corrected by Update 92: textbook geometry, not a code result).
- Measured (T79, O148): in the published model's warm background a curled ring loses 5.5 to 6.0 units of entropy
  more than the line through eight flat grids gives for its size (7 to 11 σ), 1.4 to 1.5 per surplus square
  (λ_eff − 1 = +1.15 to +1.33, compared with nothing). That is a real penalty on the stiff toy's curl (a link on an
  extra square), not on her twisted diagonal (:2267).
- The record's reading of 23 October (:2263) gives the electron and the proton the same net twist, three thirds, so
  twist count alone gives them the same mass. The handoff of 23 October (item 1.7) writes that "twists alone give
  about ten" for the proton-to-electron ratio; no arithmetic behind that figure is in the record (notebook, VISION,
  handoffs and sandbox searched for this worksheet). *Ours:* it should be written out as a calculation from a stated
  rule, or withdrawn, before the sitting; it is not used here.

**(iv) Where it meets measured physics.** The proton is about 1,836 times the electron's mass (general knowledge, to
verify: no reading note in the repository sources it). Most of a proton's mass is binding-field energy ([Durr08],
[Wil12], abstract only, via the note, section 1), which matches her 21 October words. The electron, muon and tau masses
(about 0.511, 106 and 1,777 MeV; Update 85, general knowledge, to verify) are not whole multiples of one another, so a
price per whole twist alone would have to be joined by something else to make them. Published, as a method: Faddeev
and Niemi's bound that a knot's energy grows at least as its charge to the power 3/4 is a lower bound only (note,
section 2, corrected 22 October), and the binding of loops is a numerical result to be read ([BS98], abstract only).

**(v) Question 6.** Which is your mass rule? (a) The twist count only, a fixed price per twist: then an electron and a
proton with the same twist count weigh the same, and 1,836 has to come from different twist counts; (b) the twist count
plus a binding (connecting) energy holding most of a proton's mass, as you said on 21 October: then say what the
binding grows with (number of strands, number of crossings, spin speed, or the number of cubes); (c) your 23 October
mechanism: a braid that spins more slowly needs more twists to make one unit of charge, so its extra mass is extra
twists: then say what sets the two spin speeds.

---

## Slot 7: the survival rule

**(i) Hers.**

> "there could also be something where the negative curvature of the network somehow cancels some small amount of
> antimatter leaving surplus matter… although this is a bit opposite of my intuition thinking light plus almost equal
> matter and antimatter- can some light under pressure be transformed into some matter?" (21 October; :2051)

> "What that billionth is could be surplus curl or light transformed to matter or a combination." (21 October; :2068)

> "This is because matter is what the resolved black holes would be- the matter that is the extra into the hole leaves
> its uncurl back in the black hole." (21 October; :2074)

> "so the exact amount can be the released energy, we don't need to be continuing to feed or have any other ways to
> create matter in excess of antimatter." (21 October; :2102)

> "lets drop the whole extra curl on the black hole lip idea. it was never that good and the release happens faster
> than that it is the eqivalent of a MUCH bigger nuclear bomb." (21 October; :2110)

> "the uncurl left when matter was created may have created an area of negative curviture, which was added to the
> negative curviture of the background." (21 October; :2140)

> "what if due to lambda>1, the antimatter part dispurses while the matter part is trapped in atoms?" (21 October;
> :2145)

> "Evert 10 billion pairs gets an extra 6 matter quarks with nothing to cancel them. When the 2 photons per are created
> for every billion matter there is an extra one matter. Space works in base 10billion, units of 10 billion, that was
> probably the initial number of squares per seed." (21 October; :2182)

> "The extra uncurl has to heal, not just spread out. healing releases energy as matter." (21 October; :2198)

> "I may have been counting in 6's , 2 squares, as that is what you get when you add the 2 dots to the edge, one of
> each type. but we are saying the same thing." (22 October, 21 October in her day, answering the record on the excess;
> :2229)

> "Why? 7. So, let's think about the geometry when it emerges, similar to the lip idea we dropped but not exactly. So
> say we have the curls slab. The pinched edge is 10 billion long and 4 wide and L high. In that edge bumps out to 6, as
> each pair of curl/uncul points releases one new curl /uncurl point. 2 new cubes (on average) with one cube still
> connected to the original one that is still getting the energy feed. So what if that rate was such that for every 10
> b edge squares, an extra 2 cubes, 4 3-braids of matter, and the equivalent or one square's, the connected one's, the
> curl goes into the daughter universe and the uncurl stays with the mother black hole." (23 October; :2264)

> "The idea is at the edge, the curl moves into space and uncurl can't access it to cancel. Curl closes into the cube,
> uncurl is by definition away from the inside of the cube that made it. This could just be on a flaw at the lip not the
> whole lip. It just in the tiniest fraction." (23 October; :2266)

> "if the extra curl goes into the blackhole to be taken into daughter universe, then the antimatter stays in sort of a
> shell outside the edge, and when the black hole disolves, that adds to the backgound negative curviture, just the
> tiniest amount." (23 October; :2274 (f))

> "I wonder if the net network accounting for the inflation curvature close to the big bang and antimatter overage at
> the end, so at the network level matter and antimatter all cancel." (23 October; :2277 (c))

The twist slot's "a matter or antimatter particle is a twist that cannot be undone" (:2165) and slot 5's "12 is the
minimum it takes to make matter because they must combine to whole numbers" (:2264) also bear on it.

**(ii) Status.** The chat worksheet named this slot without a definition the record keeps, and her words give it two
meanings: (a) which objects last at all (a twist that cannot be undone; whole twists only), and (b) which survive the
cancellation of matter against antimatter (the excess). For (b): on 21 October, before the lip was dropped, she named
several routes to the excess: surplus curl, light turned into matter, or both (:2051, :2068); the network's negative
curvature cancelling a little antimatter (:2051); matter that goes into the hole leaving its uncurl back in the black
hole (:2074), the same shape as her 23 October "7." mechanism, written before the lip was dropped; antimatter dispersing
while matter is trapped in atoms (:2145); and the released energy alone setting the amount, with no other way needed
(:2102). None of these was withdrawn by name. The extra curl at the black hole's lip was dropped on 21 October (:2110,
Update 82); on 23 October she proposed a mechanism "similar to the lip idea we dropped but not exactly"
(curl into the daughter, uncurl left with the mother, on a tiny fraction of flaws at the lip), followed the same day by
the antimatter shell and a cancellation over the whole loop. The "7." at the head of :2264's passage is read here as her
answer to slot 7 (reading to confirm). None of the three later statements withdraws another. *Ours:* the shell's
uncurl adding to the background's negative curvature (:2274 (f)) repeats her 21 October "the uncurl left when matter
was created ... was added to the negative curviture of the background" (:2140).

**(iii) Exact and sandbox beside it.**
- In the stiff toy a curl and an uncurl cancel only in contact (O22), so one step apart they already survive (the chat
  answer at :2266).
- The kind rule cannot carry an excess: swapping the two kinds of point is an exact symmetry of the energy and the
  lattice, and the kinds are equal in number (Update 92).
- *Exact, geometry, checked for this worksheet* (the three planes through the diagonal (1, 1, 1) that contain a cube
  edge are x = y, y = z and x = z; the angles come from their normals, and the mirror's action from swapping x and y in
  each normal): the same holds for clockwise against counterclockwise. A mirror plane of the cube that contains a body
  diagonal (for example the plane x = y round the diagonal (1, 1, 1)) swaps the other two planes through that diagonal
  and keeps the third, so it reverses the order in which a tape steps round the diagonal. Any rule invariant under the
  cube's reflections therefore prices the two senses the same, which is her "Looking at a set of 12 cubes, there is no
  difference" (:2264). Naming which sense is which needs an orientation convention, and a rule that uses one is not
  mirror symmetric; an excess of one sense needs such an ingredient.
- Sandbox, two looks of 23 October (LOG, 23 October): the uncurl sits at the seams and joints, never inside the clean
  open region or the clean curled region; inside the open space of T56's slabs no closed ring of four five-square links
  formed (0 in 64 opened slab end states), only scattered single five-square links, 4 to 15 per seed. Warm-bath end
  states, not cooled. The shell half of her picture was not killed at these settings (a look can kill a claim, never
  support one, rule 16 (a)); the ring form was killed at those settings. Both looks tested the stiff toy's curl, not her
  twisted diagonal (:2267).
- Her prediction, recorded before the count: "How many extra cubes per seed in 3d. It should be less than in 2d, as it
  needs to be more messed up to not self correct with 6 squares vs 4." (23 October; :2265). In two directions about one
  stuck knot is left per three seeds (O107); in three directions T53's end states at the coldest bath hold 38 to 229
  damaged points per seed (sandbox, LOG, 23 October, look (B)). Her prediction fails on that reading, with the caveat
  that the protocols differ: T53 is a warm bath holding a half-opened rod, O107 a cooled, fully opened sheet.
- *Exact, enumerated for this worksheet* (method, since the scratch script is not in the repository: for a segment
  from the origin, test every unit cube within two steps for a point in common with the segment and for holding the
  whole of it): her "a segment toughing 2 dot types touches 12 cubes" (:2264) is exact for a link if "touches" means
  "shares at least one point with": the 8 cubes round each end, less the 4 that hold the whole link, give
  8 + 8 − 4 = 12. A body diagonal gives 8 + 8 − 1 = 15, with 1 cube holding it; a face diagonal 8 + 8 − 2 = 14, with 2.
  The segment may be her tape of the same message, which runs corner to corner and also joins the two kinds; for it the
  counts are 15 and 1, not 12 and 4. "12" may also count directions, not cubes (her clause goes on "that is all the
  directions it can move"): a point has 12 face-diagonal directions and 12 squares through it. The chat answer at :2264
  ("an edge touches 4 cubes ... (not 12)") counted only the cubes that contain the link. *Ours, a reading to confirm,
  not a derivation:* "A 12 set makes 4 matter units" is what twelve cubes give if each contributes one third-twist
  strand (12 × 1/3 = 4).

**(iv) Where it meets measured physics.** About 6 × 10⁻¹⁰ baryons per photon (note
`2026-10-19_cp_violation_and_baryogenesis.md`: general knowledge there, to check against [Planck18]), which is about 18
extra quarks per ten billion photons, not 6 (Update 87 (c)). Antimatter regions would glow in gamma rays at their
borders; none is seen short of the whole visible universe ([CDG98], abstract only; note, section 8), which bears on a
shell of antimatter outside each black hole. The proton outlives 10³⁴ years (general knowledge, to verify; the answer at
:2131). An excess needs the conditions Sakharov named, including a departure from equilibrium and a rule that treats
matter and antimatter differently (general knowledge, to verify; Update 92 adds that an unequal price is a CPT-violating
stand-in, which inherits the limits on Lorentz violation).

**(v) Question 7.** What does the survival rule decide? (a) Only which objects last (a twist that cannot be undone,
whole twists only), with the excess left to a separate rule; (b) the excess too: at the lip a tiny fraction of curl goes
into the daughter while its uncurl stays with the mother; (c) both. If (b) or (c): is the "7." in your 23 October
message your answer to this slot, and how does it differ from the lip idea you dropped on 21 October? And do the routes
to the excess you named on 21 October, before the lip was dropped, still stand beside it: surplus curl or light turned
into matter (:2068), the network's negative curvature cancelling some antimatter (:2051), matter in the hole leaving its
uncurl there (:2074), antimatter dispersing while matter is trapped in atoms (:2145), and the released energy alone
setting the amount (:2102)?

---

## Slot 8: spin and charge (moved out of the twist slot on 23 October)

**(i) Hers.**

> "They have their spins because the snapping of the braids creates the different rotations of the quark, and there is
> nothing to slow that rotation an object in motion stays in motion." (21 October; :2180)

> "interacting with other forms of the force: the quark's spin's electromagnetic fields, essentially friction compared
> to light's speed due to all the unescapable twists" (21 October; :2193)

> "but isn't rotating matter like a literally spinning quark the thing that might make the charges? same types repulse
> because the spins oppose each other but opposites would come together. imagine the quark spinning on the diagonal,
> and they ewere spinning on right angles." (22 October, 21 October in her day; :2225)

> "because of the twisted internal loops billing outward they get locked into twist braids that spin on an axis (or
> don't) which creates electromagnetism which slows the movement of the quark through space" (23 October; :2262)

> "charge is the twist count and the twist count spins" (23 October; :2263, a fragment inside an entry the record
> wrote)

> "Its spin is energy turning it to a magnet with enough heat to gives it one negative charge in terms of its effect on
> other particles." (23 October; :2264)

> "Charge is only spin, speed of spin matters. The heat is the frozen magnet analogy." (23 October; :2265)

> "(angle/direction/color come from movement/spin)" (23 October; :2274 (d))

**(ii) Status.** Spin is tied to charge or electromagnetism in her words on 21 October ("the quark's spin's
electromagnetic fields", :2193), on 22 October (a question, :2225) and on 23 October (twist braids that spin "which
creates electromagnetism", :2262; and in :2264, where the electron's spin "gives it one negative charge" and an excited
twist that "continues to spin ... generates a negative electric charge"). Two exceptions: :2263, "charge is the twist
count", a fragment inside an entry the record wrote, and one clause of :2264, "3 come together add their twists into a
braid with one unit of charge, one twist". :2265 settles it: "Charge is only spin, speed of spin matters"; the handoff
of 23 October lists it as fixed. Open: how a speed of spin gives every electron exactly −1, every proton exactly +1, and
a neutron 0 (C3).

**(iii) Exact beside it.** The toy has no spin and no speed of anything turning: its only clock is the count of moves
(Update 92; the notebook's check at :2258). The two senses of a tape's twist are mirror images (slot 7, exact), so if
charge rode on the sense alone its size would be the same for both.

**(iv) Where it meets measured physics.** General knowledge, to verify; the record's own answers (Updates 87 (b) and
91) and the attribution debts of the handoff of 22 October, section 2.3: spin is a fixed amount, one half for the
electron, the proton, the neutron and each quark, not a speed that varies; the neutron and the neutrinos have spin and
no charge; the electron and the positron have the same spin and opposite charges; like charges repel whatever way they
spin; a spinning charge is a magnet, and the neutron is a magnet with no net charge; the proton's and electron's charges
are equal and opposite to very high precision. One measured fact sits near her "spins much slower": the proton's magnet
is about 658 times weaker than the electron's although both have the same spin (general knowledge, to verify). *Ours:*
in the standard account the weaker magnet follows from the larger mass, so it cannot be used to set the mass ratio
without arguing in a circle (rule 13).

**(v) Question 8.** "Charge is only spin, speed of spin matters." Set beside it (general knowledge, to verify): measured
spin is one fixed amount, one half, for the electron, the proton and the neutron, and the neutron and neutrinos have
spin and no charge. Which should the rule carry? (a) Charge from spin, with each kind's spin speed fixed by its
structure, and the neutron uncharged because it does not spin (your "not spinning neutrons", :2264), against its
measured spin of one half; (b) charge from spin, with the neutron and neutrinos given no charge by some other feature
(say which); (c) charge from the sense of the twist (clockwise or counterclockwise) with one fixed size, and spin a
separate property; (d) charge back to the twist count in thirds, as in Bilson-Thompson's model; (e) something else.

---

## Slot 9: matter against antimatter

**(i) Hers.**

> "What the toy lacks is a rule saying which kind is matter I think curl is matter and uncurl antimatter." (21
> October; :2073)

> "gathering curl uncurl into a proton or nuetron" (21 October, later the same day; :2125, slot 6)

> "so matter and antimatter would hold a twist in different directions" (21 October; :2155)

> "one diagonal is matter: negitive curviture is a fact." (22 October, 21 October in her day; :2212)

> "possibly as the curl is the inside of the cube and the uncurl is the outside, so the curled starts doing its
> braiding and connecting of twists, and the uncurl. also the curl twist loops is then more dense which is less
> entropic, because of their spin even?" (22 October; :2258)

> "But is it a clockwise or counter clockwise twist? Looking at a set of 12 cubes, there is no difference, and we have
> to let go of the information about things moving" (23 October; :2264)

> "if an antimatter/reverse uncurl twist one does we get an anti electron" (23 October; :2264)

> "Curl closes into the cube, uncurl is by definition away from the inside of the cube that made it." (23 October;
> :2266)

**(ii) Status.** Open. The brief's definitions box lists three rules on the record: curl against uncurl (Update 80),
opposite twists (Updates 85 and 86), one kind's diagonals against the other's (Update 91). Her 23 October phrase
"antimatter/reverse uncurl twist" joins the first two (reading to confirm). On 21 October a proton or neutron forms by
"gathering curl uncurl" (:2125), which on the plain reading puts matter and antimatter in one proton (C12). Still owed
from the handoff of 22 October (section 4): whether "one diagonal is matter" means a handedness of the network or
bookkeeping, and whether the kind-0 choice in `graphity.regge` stands. Also owed from that handoff (section 2.4):
whether dropping the lip's extra curl also drops "the stores carry the parent's eaten matter" (Update 76), and if so,
"what makes curl rather than uncurl the matter kind?"

**(iii) Exact beside it.** The kind rule cannot carry an excess (Update 92). Curl and uncurl are not mirror images in
the stiff toy (prices 1 : 4 at λ = 1.25; no curl-only defect; LOG, 21 October). Clockwise and counterclockwise are
mirror images under the cube's own symmetry (slot 7, exact), so a rule invariant under the cube's reflections gives
them equal prices.

**(iv) Where it meets measured physics.** Particle and antiparticle have equal masses and opposite charges, to very
high precision (general knowledge, to verify; the handoff of 22 October, section 2.3, lists the measurement owed). So
the sense of a twist gives equal masses for free, and curl against uncurl gives unequal ones unless something evens
them.

**(v) Question 9.** Is antimatter (a) the reverse sense of the same twist, which gives equal masses but needs a
separate ingredient for the excess; (b) the uncurl, which the toy prices differently from the curl, so masses come out
unequal unless binding evens them; (c) the other kind of point's diagonals, which cannot carry an excess; or (d) your
"reverse uncurl twist", meaning (a) and (b) together, and if so which of the two sets the mass? If (b) or (d): what
does a proton "gathering curl uncurl" (:2125) gather, given that curl is matter and uncurl antimatter (:2073)?

---

## Slot 10: light (the untwisted loop)

**(i) Hers.**

> "2 coming together create 2 photons." (21 October; :2148, slot 1)

> "The matter antimatter twisted loop, they come together and become 2 untwisted loops and return to flat space, with
> the twist energy released at the speed of light. an untwisted loop is a photon and and untwisted loop loses energy
> over time like a photon." (21 October; :2158)

> "So a photon is a twist that can be undone and a matter or antimatter particle is a twist that cannot be undone."
> (21 October, the same message; :2165)

> "light can only go one speed, it travels one space link/one time unit. it slows if a space link is longer." (21
> October; :2191)

> "opposite twist is antimatter when they meet the twists desolve and 2 photons are created: untwisted loops travelinin
> one link per unit of time, the speed of light." (21 October; :2209)

> "If it connects with no twist, it's not as far as it can be from its matched point, so rule says it must twist"
> (23 October; :2264)

**(ii) Status.** Two forms on 21 October, in one message: a photon is "an untwisted loop" (:2158) and "a twist that can
be undone" (:2165), which are not the same thing; :2209 repeats the first. In tension with 23 October: a tape that
connects corner to corner with no twist "must twist" (:2264), a rule about the tape at the moment it forms (C6). Neither
statement withdraws the other.

**(iii) Exact beside it.** Light has no object in the toy and nothing moves a ring; test 5 of the brief cannot be
scored until a carrier of light is declared (Update 92; the brief's box). Stage A's waves are a field on points, with a
speed that falls at short wavelengths (Update 88, with Update 92's additions).

**(iv) Where it meets measured physics.** General knowledge, to verify: a photon has no mass and no charge, spin 1 and
two polarizations; it does not lose energy travelling through static space, only as space stretches (Update 86 (b));
two photons can make an electron and a positron (Breit and Wheeler; the handoff of 22 October, section 2.3, lists what
is owed); an electron and a positron at rest make two photons or three (note, section 1).

**(v) Question 10.** On 23 October a tape that connects corner to corner with no twist must twist ("rule says it must
twist"); on 21 October a photon is an untwisted loop, and in the same message a twist that can be undone. Which holds?
(a) (our suggestion) A photon is a loop whose twists cancel (as much clockwise as counterclockwise), not a loop with
none, which is close to your "a twist that can be undone"; (b) untwisted loops are allowed, and "must twist" applies
only to a tape as it connects corner to corner; (c) a photon is not a loop (say what it is).

---

## Slot 11: kinds and generations

**(i) Hers.**

> "different lengths make diff subatomic particles that hold the same energy." (21 October; :2153)

> "Different particles could be different braids of matter and antimatter loops of different lengths." (21 October;
> :2170)

> "(2 extra hypotenuse twists per 8 1x1x2 box, an amount from each 1x1x3 box, etc, up until any additional? Idk, more
> types of particles, fount in proportion to ratios of hypotenuse counts?)" (21 October; :2175)

> "maybe there are more types of matter through different length hypotenuses (th 1x1x2 groups, the 1x1x3 groups), or
> maybe diagonal space is diagonal space whatever the angle." (21 October; :2196)

> "only the hypotenuses exist fundamentally: sqrt2 and 2" (23 October; :2274 (c))

**(ii) Status.** Open. Length never set mass in her words (every length holds "the same energy", :2153, restated at
:2167, slot 6) and was kept as a possible source of kinds (:2170); on 23 October only two lengths exist, which would
leave two for three generations if lengths are the source.

**(iii) Exact beside it.** The box diagonals are √2, √3, √6, 3 and √11 (Update 87). One kind's diagonal network is the
face-centered cubic lattice, which has twelve preferred directions, so diagonal space is not alike whatever the angle
(Update 92's addition to Update 88).

**(iv) Where it meets measured physics.** Exactly three generations (the Z boson's width counts 2.996 ± 0.007 light
neutrinos, the 2019 reanalysis; Update 92, to read); the electron, muon and tau share one charge and weigh about 0.511,
106 and 1,777 MeV (general knowledge, to verify; Update 85).

**(v) Question 11.** Where do the three generations come from: (a) longer hypotenuses (the 1 × 1 × 2 and 1 × 1 × 3
boxes); (b) different braid patterns of the same strands; (c) not part of this rule yet, left for later?

---

## Contradictions and tensions to settle first

Two lists. The first holds conflicts between two of her own statements; each says which is later and whether she
withdrew the earlier. The second holds ambiguities in her words, and tensions between her words and something that is
not hers: an exact fact, a measurement, our reading or the record's; each says which (rule 10). Every entry names the
question that settles it. "Not withdrawn" means the record holds both and the later does not say it replaces the
earlier.

### Between two of her statements

- **C5. What a dark loop is.** *Kind: two of her statements.* Untwisted face or edge loops with no spin and no charge
  (21 October: "No spin, no electric charge", :2185; "not twisty", :2195; "no diagonal spin", :2206; and on 23 October,
  "the dark matter as the flat sides", :2262); a half twist, and "Dark electron is the same but the single side twist"
  (23 October, :2264); no side-length rings at all (23 October, :2274 (c)). Under charge-from-spin, a dark electron that
  spins as an electron does would carry charge. Not withdrawn. Settled by Q5 (with its spin clause) and Q8.
- **C6. The photon against "must twist".** *Kind: two of her statements, which may not meet.* Untwisted loop (21
  October, :2158, :2209; in the same message also "a twist that can be undone", :2165) against her rule for the tape as
  it connects corner to corner: "If it connects with no twist, it's not as far as it can be from its matched point, so
  rule says it must twist" (23 October, :2264). If the rule covers only a tape at the moment it forms, the two do not
  meet. Not withdrawn. Settled by Q10.
- **C8. Where color comes from.** *Kind: two of her statements, once a reading is confirmed.* The three orders of the
  strands (21 October, :2172) against "(angle/direction/color come from movement/spin)" (23 October, :2274 (d)). The
  23 October sentence is about "which type of quark, which photon"; if its "color" is the color of light, which motion
  shifts (the Doppler shift; general knowledge, to verify), the two do not meet. Reading to confirm. Not withdrawn.
  Settled by X3 below, after Q3.
- **C12. Curl as matter against a proton that gathers curl and uncurl.** *Kind: two of her statements, on the plain
  reading.* "I think curl is matter and uncurl antimatter" (21 October, :2073) against "gathering curl uncurl into a
  proton or nuetron" (21 October, later the same day, :2125), which on the plain reading puts matter and antimatter into
  one proton. Not withdrawn. Settled by Q9.

### Ambiguities, and tensions with an exact fact, a measurement or a reading

- **C1. Where the third-twist lives, and which lengths exist.** *Kind: an ambiguity; on its face two of her statements,
  possibly one statement with a miscomputed length.* The tape of 23 October runs along a body diagonal, √3, and twists
  by thirds (:2264). Later the same day only √2 and 2 exist, with "twist_2 = 1/3" and "twist_sqrt2 = 1/2" (:2274 (c)).
  Exact: 2 is the hypotenuse of two face diagonals at a right angle, a straight line two edges long along a lattice axis,
  and lies in a coordinate plane, as a face diagonal does; √3 is the hypotenuse of an edge and a face diagonal, the
  cube's corner-to-corner line, and the only one of the three that leaves the coordinate planes (slot 1). So if her
  matter strand is the length-2 line, no strand of hers leaves the coordinate planes, which is in tension with "matter
  is a loop from 3d and dark matter is a loop from 2d" (21 October, :2148), though a loop of planar segments can still
  turn through three dimensions. *Ours, a reading to confirm:* "2" may be a miscomputed length for the tape, since the
  third-twist and the half twist are the ones she gave the tape and dark matter that morning (:2264), and (d) of the same
  message assigns the two lengths to matter and dark matter. Stage B as built has no body diagonal. Not withdrawn.
  Settled by Q1, together with what "twist is always the same" holds fixed (X2 below).
- **C2. What a third is a third of.** *Kind: her words against our geometric reading.* "1/3 clockwise or
  counterclockwise", and "3 come together add their twists into a braid with one unit of charge, one twist" (:2264).
  Exact: the lattice's step is 60°, a third of a tape's half-turn repeat; three steps close a one-sided loop, a whole
  turn needs six (slot 2). Settled by Q2.
- **C3. What charge is.** *Kind: her statements, settled by her own revision; what remains is a tension with a
  measurement.* Spin is tied to charge or electromagnetism in her words on 21 October (:2193), 22 October (a question,
  :2225) and 23 October (:2262, :2264); charge is the twist count in :2263 (a fragment inside an entry the record wrote)
  and in one clause of :2264 ("a braid with one unit of charge, one twist"); "Charge is only spin, speed of spin
  matters" (23 October, :2265) settles it. What remains: the 23 October morning message, written before that revision,
  also has "not spinning neutrons" (:2264), which sets her words against the neutron's measured spin of one half
  (general knowledge, to verify). Within her picture it is consistent: under charge-from-spin a neutron that does not
  spin carries no charge. Settled by Q8, then Q3.
- **C4. Where mass sits.** *Kind: a gap, not a contradiction.* Most of the mass is connecting energy (21 October,
  :2112); length has no impact on mass (21 October, :2167); a fixed price per twist by the diagonal's proportion (22
  October, :2221, :2236); mass rises with the twist count (23 October, :2265). A twist-count mass does not exclude a
  binding term: the later statements do not name one, and the first is not withdrawn. Settled by Q6.
- **C7. The record's reading at :2263 against her :2264.** *Kind: the record's reading against her words.* The record
  read :2263 as giving the electron and the proton the same net twist, three thirds; with mass from the twist count
  (:2265) they would then weigh the same (slots 2 to 4). Her own :2264 gives the proton "a bunch of twists" ("spins much
  slower, so it needs a bunch of twists"), written before charge moved to spin speed and fitting it, and under :2265 more
  twists mean more mass, so in her words the proton is heavier. She also named other sources of a proton's mass: the
  connecting energy (:2112) and a proton "gathering curl uncurl" that "captures the lightforce of a 1 unit atomic bomb"
  (:2124 to 2125). Settled by Q4 and Q6.
- **C9. The corner-to-corner strand joins the two kinds.** *Kind: her words against an exact fact.* Exact: a body
  diagonal joins one point of each kind, so a twist on it would sit on both kinds at once (the handoff of 22 October,
  section 2.4, asked whether she keeps such lines; unanswered), while "one diagonal is matter" (22 October) uses one
  kind's face diagonals. Settled by Q1 and Q9.
- **C10. The lip.** *Kind: a sequence she acknowledges herself ("similar to the lip idea we dropped but not exactly",
  :2264), not a contradiction.* On 21 October, before the lip was dropped, she named routes to the excess: surplus curl,
  light turned into matter, or both (:2051, :2068); the network's negative curvature cancelling a little antimatter
  (:2051); matter that goes into the hole leaving its uncurl back in the black hole (:2074), the same shape as the
  23 October "7."; antimatter dispersing while matter is trapped in atoms (:2145); and the released energy alone setting
  the amount (:2102). The lip was dropped on 21 October (:2110, Update 82). On 23 October: "similar to the lip idea we
  dropped but not exactly" and "on a flaw at the lip" (:2264, :2266); an antimatter shell outside each black hole
  (:2274 (f)); matter and antimatter cancelling over the whole loop (:2277 (c)). The three later statements fit together
  if the shell's antimatter is the uncurl left at the lip and is cancelled at the network level at the end (ours, one
  reading, to confirm). Settled by Q7.
- **C11. The record's own count, not hers.** *Kind: the record's count against her words.* Her twelve cubes round a
  two-kind segment (:2264) were answered in chat as "an edge touches 4 cubes ... (not 12)". Exact: 4 cubes contain a
  link and 12 share a point with it; the body diagonal, her tape of the same message, which also joins the two kinds,
  lies inside 1 cube and shares a point with 15 (slot 7). "12" may also count directions ("that is all the directions it
  can move"): a point has 12 face-diagonal directions and 12 squares through it. Her "4 matter units" and "36" per
  twelve cubes rest on which she meant. Settled by X1 below.

Three clarifying questions that belong to no single slot:

- **X1.** When a segment "touches 12 cubes": which segment did you mean, a link or your corner-to-corner tape (both join
  the two kinds of point)? And does 12 count cubes or directions ("that is all the directions it can move")? For
  reference, exact: a link shares at least one point with 12 cubes and lies inside 4; the body diagonal shares a point
  with 15 and lies inside 1; a point has 12 face-diagonal directions and 12 squares through it.
- **X2.** "twist is always the same": the same per segment, per closed loop, per unit of length, or something else?
- **X3.** Do the three quark colors come from the three orders of the strands in a braid (21 October) or from movement
  and spin (23 October)? And in "angle/direction/color come from movement/spin", did "color" mean quark color or the
  color of light?

## What arithmetic waits on these answers

**The two numbers, computed together from one written rule** (the handoff of 23 October, item 2.4; rule 13).

1. **Dark to ordinary matter by mass.** Target 5.36 (Ω_c h² / Ω_b h² = 0.120 / 0.0224; Planck 2018 values from a
   search summary in `docs/reading/notes/2026-09-26_dark_charge.md`; VISION Update 41 records the two densities checked
   at [Planck18]). The rule must supply the mass of one dark object and of one proton (slots 3, 5 and 6) and how many of
   each survive (slot 7). The record holds that 5.36 compares two leftovers, not two releases (Updates 41, 42 and 87),
   so a count of loops made per cube gives the ratio only if the survival rule says the survivors stand in the same
   proportion as what was made.
2. **Proton to electron by mass.** Target about 1,836 (general knowledge, to verify; no reading note in the repository
   sources it, and a source is owed before the comparison). The rule must supply the electron (slot 4), the proton
   (slot 3) and the energy law with its binding term (slot 6). It does not depend on survival.

**Order of work.** Rule 13 sets five conditions before a numerical match counts: derived independently, input
uncertainty propagated, inputs checked for containing the target, neighbouring values tested, and the other arbitrary
combinations that would match counted. Each is a step below, marked.

1. Her answers read back as one set and confirmed.
2. The rule written into the stage-B brief's definitions box, with every constant and its value, dated and committed.
3. The rule's free constants counted: one constant fitted to one ratio leaves only the other as a test, and two leave
   none.
4. *Derived independently (rule 13).* Each number derived from the written rule, not worked back from its target.
5. *Inputs checked for the target (rule 13).* Each input checked for whether it was formed with a target in view; such
   an input counts as fitted. *Ours, from the record so far:* her count ratios 9 and 4.5 were written beside 5.36
   (slot 5); the base of ten billion and the six extra quarks per ten billion pairs were written beside the measured
   excess of about one in a billion (:2182, slot 7); and the proton's magnet, about 658 times weaker than the
   electron's, follows in the standard account from the mass ratio itself (slot 8), so it cannot be an input for 1,836.
6. *Other matching combinations counted (rule 13).* The joint count of the next paragraph, with the family fixed before
   it runs.
7. Both numbers computed in one run and printed together, and neither compared with its target until both are printed.
   This step is the handoff's (23 October, item 2.4), not part of rule 13's text.
8. *Input uncertainty propagated (rule 13).* The uncertainties of every measured input carried through to both numbers.
9. Both numbers compared with their targets.
10. *Neighbouring values tested (rule 13).* Each constant moved to neighbouring values, and how fast the agreement falls
    away reported with the result.

**What a hit is worth.** The counting step for 5.36 has been done: with the 119 closed-loop lengths the cubic lattice
offers up to twelve steps of edges, face and body diagonals, five energy laws and small loop counts, 29,101
combinations land within 2 % of 5.36, and ten random targets between 2 and 12 get 26,000 to 33,000 each
(`sandbox/spring_ratio_look.py`; `sandbox/out/spring_ratio_look_2026-10-22.txt`; LOG, 22 October, night). So a hit on
5.36 alone carries no weight. Not yet done, and owed before the two numbers are compared: the same count for 1,836, and
the joint count, how many rules of one fixed family land on both ratios at once against how many land on random pairs
of targets; the family is fixed before that count runs (sandbox, a look). One small discrepancy in the record (exact,
from the script): the LOG says loop counts "1 to 8", while the script uses 1, 2, 3, 4, 6 and 8; the output stands as
printed.

**A check that can be scored first.** The rule must give charges of exactly −1 (electron), +1 (proton) and 0 (neutron,
and whatever plays the neutrino), the same for every copy. That is pass or fail, needs no ratio, and can be read off the
rule once slots 3, 4 and 8 are answered.

**Not to be computed before the sitting.** The handoff's "twists alone give about ten" (slot 6: no arithmetic behind it
in the record), and her count ratios 9 and 4.5 (slot 5), which were already set beside 5.36 in chat; under rule 13
closeness is not a result. A paper calculation of the two ratios from her rule does not need the twist defined on the
graph (the handoff of 23 October, item 2.2); any test in the toy does.

## The questions, in the order to ask them

1. **Q1** (strand; settles C1 and, with Q9, C9). Which segments are your strands: (a) the body diagonals, √3; (b) the
   face diagonals, √2; (c) only √2 and 2; (d) by "2" you meant the corner-to-corner line, √3; (e) more than one, with
   different jobs?
2. **X2.** "twist is always the same": the same per segment, per closed loop, per unit of length, or something else?
3. **Q2** (twist; C2). "1/3" of what: (a) a third of a full turn, so three close a two-sided loop; (b) a third of a
   tape's half-turn repeat, so three close a one-sided loop and a whole twist needs six; (c) something else?
4. **Q8** (spin and charge; C3). Which should the rule carry: (a) charge from spin, each kind's speed fixed by its
   structure, the neutron uncharged because it does not spin (against its measured spin of one half); (b) charge from
   spin, the neutron and neutrinos uncharged for another reason; (c) charge from the twist's sense with one fixed size,
   spin separate; (d) charge from the twist count in thirds; (e) something else?
5. **Q6** (energy law; C4, C7). Which is your mass rule: (a) the twist count only; (b) the twist count plus a binding
   energy (and what it grows with); (c) a slower-spinning braid needs more twists for one unit of charge (and what sets
   the speeds)?
6. **Q3** (braid). Is one braid of three strands (a) a proton, with a neutron the same braid not spinning; (b) a proton,
   with a neutron a different braid; (c) a quark, so a proton is three braids?
7. **X3** (C8). Do the three colors come from the orders of the strands or from movement and spin? In "color come
   from movement/spin", did "color" mean quark color or the color of light?
8. **Q4** (electron; C7). How much twist does an electron carry against a proton's braid: (a) the same whole twist;
   (b) one third on a strand that does not close; (c) something else?
9. **Q5** (dark loop; C5). What is a dark loop now: (a) an untwisted edge loop on a face; (b) a √2 face diagonal with
   a half twist; (c) the toy's column (14) or double column (8); (d) something else? Does it spin?
10. **Q10** (light; C6). (a) (our suggestion) A photon's twists cancel; (b) untwisted loops are allowed and "must
    twist" applies only to a tape as it connects corner to corner; (c) a photon is not a loop?
11. **Q9** (matter against antimatter; C9, C12). Is antimatter (a) the reverse sense of the twist; (b) the uncurl; (c)
    the other kind's diagonals; (d) the reverse uncurl twist, (a) and (b) together, and which sets the mass? If (b) or
    (d), what does a proton "gathering curl uncurl" gather?
12. **X1** (C11). Which segment "touches 12 cubes", a link or your corner-to-corner tape, and does 12 count cubes or
    directions? (A link shares a point with 12 cubes and lies inside 4; the body diagonal 15 and 1.)
13. **Q7** (survival; C10). Does the survival rule decide (a) only which objects last; (b) the excess too, curl into
    the daughter and uncurl left at the lip; (c) both? Is the "7." of 23 October your answer here, and how does it
    differ from the lip idea dropped on 21 October? Do the routes to the excess you named on 21 October still stand
    beside it?
14. **Q11** (generations). Do the three generations come from (a) longer hypotenuses; (b) braid patterns; (c) not this
    rule yet?

---

## Addendum, 24 October 2026: what the particle handoff and its looks move

*Added by a later session; nothing above is edited. Sources: her handoff (`docs/geometric_particle_model_handoff_2026-10-24.md`,
her ideas in its section 1), her four answers of 24 October (`sandbox/NOTEBOOK.md`, last two entries), the exact looks
(`sandbox/out/particle_handoff_looks_2026-10-24.txt`), and `docs/design/particle_handoff_brief_2026-10-24.md`. Each line
was mapped by one reader and checked by a second told to refute it; claims that did not survive are left out. Kinds as
above. Three notebook lines of 23 October after this worksheet's read range bear on it and are cited by line: :2279
(c) (edges "not real"), :2283 (a) ("short halfs and long thirds"), :2285 (the coin).*

**Settled or narrowed by her own words of 24 October**
- **Q4 (electron): (b) is out.** Her answer "3 thirds" removes one third on a strand that does not close. It does not
  choose between (a) and (c), and it equals one whole twist only under Q2 (a); under Q2 (b) three thirds close a
  one-sided loop. C7 is now between two statements of hers: the three-thirds electron (24 October) and the proton's "a
  bunch of twists" (:2264); its kind line ("the record's reading against her words") is out of date.
- **Q10 (light) gains a third description of hers, kept as three variants:** "a traveling half-curl" (handoff idea 2;
  her answer "Keep all as variants"), beside the untwisted loop and the twist that can be undone. C6 is widened, not
  settled.

**Narrowed by exact results (each conditional where marked)**
- **Slot 2, the twist's definition:** in the photon field built today a whole turn of phase round a square costs
  exactly what no turn costs; only the turn modulo a whole turn is seen. So her twist (a closed loop needs a whole
  twist; twist count is mass) cannot be that field's holonomy on one square; it has to be a separate label or a
  winding counted over many squares (ours: a winding of n turns spread over A squares costs about (2πn)²/(2A)).
- **Slot 8 and C3, spin one half:** four quarter turns of the cubic lattice return every link with its orientation, so
  any state built on link labels (angles, thirds, twists, frames) comes back with sign +1 after a full turn. No
  electron, proton or neutron of this toy carries spin one half unless it is put in or comes from a loop in the space
  of configurations (Finkelstein and Rubinstein 1968, general knowledge, to verify). This bears on every Q8 option
  alike and does not tell them apart; the neutron is no longer the only place spin and measurement meet.
- **Slot 8, Q8 (d):** her handoff idea 3 (a one-third twist is not a charge) removes the reading in which each third
  carries e/3; Bilson-Thompson's form (a whole twist per ribbon is e/3) and her own "a braid with one unit of charge,
  one twist" remain.
- **Slot 8 against the observed table (conditional on her thirds being the quarks' thirds):** every observed particle
  obeys 3Q + t ≡ 0 mod 3, so whatever sets a "speed of spin" would have to give charges quantized and tied to the
  count of thirds. Her three-thirds electron is compatible with −1; one quark-third is not.
- **Slot 10, half-curl A2:** a 180° bend has no meaning for a field on fixed links (a path that turns back carries
  holonomy zero). **A3:** a half turn round a square is that square's most expensive state, and a pulse launched with
  it did not travel (a sandbox look, for that launch only).
- **Slot 6, Q6 (b) and C4:** her entropy idea cannot be the binding that holds most of a proton's mass: Landauer's
  bound is a minimum, not a value, and energy leaving on closing makes the closed unit lighter (a mass defect, general
  knowledge, to verify), the opposite sign from her 21 October "connecting energy". Q6 (b) as worded asks only about a
  binding that adds mass; if she means both, it needs a clause for a released closure energy.
- **Slot 5, Q5 (b) (conditional):** if her dark half twist were a half turn of phase on one square, two halves joined
  on that square would cost nothing, so her "exact mass" for the full dark unit could not come from this energy. Her
  half twist sits on √2, which today's field does not carry, so her own reading is untouched.

**New options the questions lack**
- **Q1:** handoff idea 8's 1 × 1 × 4 line (length √18 = 3√2, one kind to the same kind, through no lattice point), as
  "different jobs" under (e). The handoff ties it to gluons, not strands.
- **Q2 (c):** a third as a third of a count (a three-valued label per strand, counted at the points), under which the
  60° against 120° question does not arise; that it counts her twist is ours.
- **Q4 (c) / Q6:** her entropy idea as a formation step: closing three twists gives up ln 3 and one photon. Exact
  caveats: the three-placement triples (+ + 0, + + −) total 2 and 1 mod 3, so the labels must change on closing; and
  one photon per electron formed has to be squared with her 23 October "exactly 2 photons, same as it took to create
  them". Scale (general knowledge, to verify): about 1.6 × 10⁹ photons per baryon today, so closure photons cannot be
  most of the light.
- **Q7 (a):** the handoff's persistence rule (protected by a conservation law, with no allowed fast decay; spin one
  half not required) as a definition, offered by the handoff's writer and endorsed by her only in general.
- **Q7 (b):** whether a matter count obeys a whole-number Gauss law (so any surplus is balanced somewhere, though not
  necessarily by antimatter of its kind) or a mod-3 one (so whole triples need no partner). The toy now has one
  conserved Gauss-law charge, in the photon field, uncoupled to curl, uncurl or twist.
- **Q8 (e):** charge as the Gauss's-law count of the photon field (charges then come in cancelling sets on a closed
  space, which is her handoff idea 5). Caveat: a classical field's divergence is any real number, so "exactly −1 for
  every copy" needs whole-number labels.
- **Q9:** antimatter as the opposite third and the other kind's diagonal at once (the brief's proposal). Exact: the kind
  swap and the cube's reflections are both symmetries, so this carries no excess either.
- **Q10 (c):** the photon as an excitation riding existing links (handoff idea 1), now with a candidate carrier in code
  (`graphity.u1`), which has not passed its reproduction gate (below).

**Tensions created or sharpened**
- **Slot 1 / C1 / C9 / Q1:** the brief of 24 October first labelled her tape a face diagonal; corrected the same day
  (the tape is the body diagonal, "4 tapes"). Her own later statements pull Q1 both ways: :2283 (a) gives the third to
  the longer length and the half to √2, and keeps "2", not √3, which weakens reading (d); :2285 puts matter and
  antimatter on a square's two face diagonals, which would dissolve C9. :2279 (c) puts the curling cost in "same point
  type to same point type" diagonals, "surface or internal", which holds both sides of C9 in one sentence.
- **Slot 1 (e) / Q10:** the photon field was built on the toy's links, the edges; on 23 October (:2279 (c)) she called
  the edges "not real in our model they are just helpful to visualize". One reconciliation (ours): edges carry light,
  diagonals carry the twist. Brief, question 7.
- **Slot 3 with Q4:** under the brief's proposed closure, a three-thirds electron and a three-strand proton braid are the
  same object unless the strand kind, the spin speed or the curl energy separates them. Twist count alone gives a mass
  ratio of 1 (Q3 (a)/(b)) or 3 (Q3 (c)) against about 1,836 (general knowledge, to verify).
- **Slot 3, a two-strand unit:** the mod-3 count allows a pair (one third each way) as well as a same-way triple, and
  handoff idea 6 wants a two-part route for mesons; whether +⅓ with −⅓ closes has to be stated (brief, question 1).
- **Slot 9 (a) with three thirds:** under mod-3 labels three thirds one way and three the other both total 0, and as a
  phase a whole turn equals none; so the sense of a closed three-third twist must be stored as a whole-number winding
  or something else outside these labels for "reverse twist = antimatter" to work.
- **Slot 10, her "one speed" (:2191):** the lattice photon never exceeds one link per tick, but that value is put in
  (inertia and κ set equal), it is reached only for long waves, and short waves are slower and faster along a cube
  diagonal than along an axis (2.7 % at |k| = 1, 10 % at |k| = 2). Her "an untwisted loop loses energy over time"
  (:2158) has no counterpart for a small pulse in static space (energy drift 2 × 10⁻⁵).
- **X3 / C8:** if colour is the three orders of the strands (a three-valued label), the toy can reproduce the meson and
  baryon counting but not colour dynamics (the handoff's own warning: three-valued labels are not SU(3)).

**Unchanged:** Q2 (what a third is a third of; "3 thirds" closes under (a) or (b)), Q3 (her words do not narrow it),
Q5's options and its spin clause, Q7 (b) and C10 (nothing of hers today touches the lip or the excess), C12, X1, X2,
Q11 (three thirds cannot tell the electron, muon and tau apart).

**One state change to note.** Slot 8 (iii) and slot 10 (iii) say the toy has no clock but the count of moves and no
object for light. Both are now out of date for the photon field (`graphity.u1` evolves in ticks), with one caveat:
**Gate U1 failed on 24 October** at β = 8 (the sampler froze in one winding sector; TASKS, its reading), so nothing
from that field is read until Gate U1′ passes.

**Her answers of 24 October, later (VISION Update 97; her comments in the particle brief).** Q1: (e), with jobs:
matter strands are body diagonals, dark strands face diagonals. Q2: (a), a third is 120°, three make a full 360°
two-sided band. Q4: three thirds closed (a). Q5: (b), a face diagonal with a half twist. Q8: charge back to the thirds
and their handedness, read as charge = −(signed thirds)/3, with one tension open (a full twist neutral against the
electron's −1). Q9: matter against antimatter is handedness on body diagonals; dark against antidark the face
diagonals. Q10: light travels on the edges, the twist on the diagonals. Confinement of a lone third: yes. Pairs close
too, more rarely. Still open from this worksheet: Q3, Q6, Q7, Q11, X1, X2, X3.

**Later on 24 October (VISION Updates 97 to 102), what moved since the addendum above.** Q1: matter strands are body
diagonals (Update 99, after an evening on 1 × 1 × 2 diagonals, Update 98); dark strands face diagonals. Q4 and Q8:
charge is −(net signed thirds) ÷ 3 for every strand and anything free carries a whole number of twists (Update 101);
the bound half-curl reading of Update 97 is withdrawn; this reverses handoff idea 3 (asked). Q5: dark strands carry
multiples of a half, odd ones one-sided (Möbius), whole ones two-sided (Update 101). Q9: an antiparticle is the mirror
image of its strand; handedness marks matter against antimatter (Updates 99, 100). Q3: the proton is +2/3, +2/3, −1/3
(Update 100), so a braid of three strands is a proton and each strand a quark; the neutron +2/3, −1/3, −1/3. Light:
Gate U1″ passed; light keeps its speed in a curl (O151, corrected). Still open here: Q6, Q7, Q11, X1, X2, X3; new
questions 0 to 0d in `docs/design/owner_questions_2026-10-24.md`.


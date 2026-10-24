# Draft entry "The twist" for the "Current definitions" box of `docs/design/regge_stage_b_brief.md`

**Confirmed by her, 23 October 2026 ("I'll update the brief's definitions box, keeping the current "not yet defined" -
confirmed"; `sandbox/NOTEBOOK.md`).** The brief's box records the entry as confirmed and keeps its standing line: her
twist, with handedness and a count on a ring, is still not defined on the graph. The two readings marked "to confirm"
below are not settled by that word: her words of the same evening ("discrete twists in short halfs and long thirds with
handedness") give the dark half twist a handedness, which the mod-2 character cannot carry. Her prediction for the
saved-state look is still owed, and no saved state is opened before it.

*Written 23 October 2026 and revised twice the same day, after two adversarial checks by fresh read-only sessions: the
first found twelve problems in the first version, the second thirteen in the revision; each correction was checked on
built graphs or in the record before it was applied (both lists are at the end). A draft for the owner to confirm,
under rule 20: a new definition is written into the box and read back to her before any test depends on it. The brief
itself is not edited by this file. Kinds of statement are marked: **exact** (arithmetic, or a count on a built graph),
**published** (with how much was read), **measured** (a registered run, with its verdict), **exploratory reading**
(exact per graph, read from a registered run's saved wiring after that run was read by its own rule; not registered;
no verdict changes), **ours** (interpretation, unverified), **hers** (the owner's words, quoted verbatim from
`sandbox/NOTEBOOK.md`). Sources: the reading note `docs/reading/notes/2026-10-23_twist_on_a_graph.md`; the torus
reading of the same day (ASSUMPTIONS O150; `scripts/exact_torus_counting.py` with its tests); the record's readings of
the saved end states (ASSUMPTIONS O116, its last two addenda; O120; O122; the notes to T61's, T62's and T64's readings
in `PREREGISTRATION.md`); the face rule of the curvature brief (`docs/design/eq45_ratio_brief.md`: the design for
reading an object's curvature from the wiring by [T25] Sec. IV.2's geometrization; its box item 1, which that brief
itself marks "sandbox until pinned"); and the built-graph check written for this entry,
`sandbox/twist_character_check.py`, output `sandbox/out/twist_character_check_2026-10-23.txt` (956 lines, ends "done",
no errors). **Nothing in `results/` was opened.** **Rule 16, said once for the whole file:** every statement cited to
that script is a sandbox look, exact on the graph it was computed on, able to narrow a claim and never to support one.
Items 1 to 4 enter the brief's box only after the counts they rest on are promoted to a script under `scripts/` with
tests (rule 6: a networkx brute-force check, an exactness check, a same-seed check), as O150 was, with one line
saying what the sandbox showed and that two looks came before. The adversarial checks' own scratch code (outside the
repository) rebuilt the graphs and reproduced the first revision's numbers; that is a check, not a promotion.*

**Terms used below** (ours; one line each, at first use; a labelled sketch where a shape is involved, rule 21).

- *The stiff toy*: the four-link toy as it stands, links present or absent, no lengths.
- *A face*: a closed cycle of links chosen to be a tile of the surface. *A face rule*: the rule that chooses, at each
  point, which four of its corner cycles are tiles. *A completion* (ours): one way of settling everything the rule
  leaves open at a point (a tie between rotations; a corner with several shortest cycles).
- *Two-sided* (orientable): a surface on which a small clockwise arrow carried round any closed path comes back
  clockwise; *one-sided*: one on which some closed path brings it back counterclockwise. *A Möbius band*: a strip
  whose two ends are joined after a half turn, so it has one side and one edge; *an annulus*: the same strip joined
  with no turn, two sides and two edges. *A Klein bottle*: a closed surface with one side, like a tube whose end is
  joined back to its start through a mirror (sketch A).
- *A lattice torus*: the square grid wrapped up by two whole-number wraps. It is *flat* when every link lies in
  exactly two squares; the 4 × L tube is a lattice torus that is not flat (its rings of four are squares, so its ring
  links carry three). *A seam*: the junction where a wrap closes. *A presentation*: the choice of which wrap is the
  ring (its size and direction), the other wrap being the junction. *The seam shift* of a seam: how far it closes
  off the straight line, in a named presentation (sketch B).
- *The curled part* of a graph: its points with a link carrying three squares; *the opened part*: its points with
  every link in exactly two squares; *a flawed point*: any other point (a link in fewer than two squares; a point
  with a link at three and another at one counts as curled). *The lip*: the links joining a curled point to a point
  that is not curled.
- *A completion closes on a region* when every face with all its points in the region, chosen at one of them, is
  chosen at all of them; nothing outside the region is decided. *The region's band* is then its faces with all
  points in the region: a surface with boundary, unless at some point its corners are two opposite ones (*a pinch*).
  *A local failure*: a point round which no completion closes on the ball of three steps (which holds every square
  and hexagon through it).
- *A ring of diagonals*: a closed sequence of points of one kind, consecutive points being the two opposite corners
  of one face (sketch E). *A cross-handle*: a handle whose two ends are spliced into the sheet the same way round, so
  that a band carried along it comes back flipped; a handle spliced the opposite way round at one end brings the band
  back as it left (sketch D).
- *V − E + F*: points minus links plus faces; 0 for a torus and for a Klein bottle, −2 for a torus with one handle
  added. *The mod-2 class* of a cycle: two cycles are in one class when, taken together, they bound a region of the
  surface; the character depends only on the class (general knowledge, to verify; item 2).

**Sketch A: the tube and its reflected closure** (ring L − 1 joined to ring 0 straight, or through the mirror
x → 2 − x).

```
                 x = 0   1   2   3                    x = 0   1   2   3
    ring 0         o---o---o---o-(round)                o---o---o---o-(round)
                   |   |   |   |                        |   |   |   |
    ring 1         o---o---o---o                        o---o---o---o
                   :   :   :   :                        :   :   :   :
    ring L-1       o---o---o---o                        o---o---o---o
                   |   |   |   |                         \   |   /   |
    joined to      0   1   2   3                          2   1   0   3     x -> 2 - x: points 1 and 3
    ring 0 at x =                                                           stay, 0 and 2 swap
                 closed straight: the tube,           closed through a reflection: a Klein bottle,
                 a torus, two sides, every cycle 0    one side; the lines along through x = 1 and 3
                                                      are the flipped paths
```

**Sketch B: the seam shift, in the presentation "rings of four round x, junction along y".** Three lattice tori on
4L points; wraps written (round, along).

```
    the tube                        O116's end state                   the half-turn closure (O150)
    ring seam shift r = 0           ring seam shift r = 2              junction seam shift s = 2
    junction shift s = 0            junction shift s = 0               ring seam shift r = 0

    x = 0 1 2 3 (back to 0)         x = 0 1 2 3 (to 0, two along)      x = 0 1 2 3
    y   o-o-o-o-.                   y   o-o-o-o-.                      ring 0    o-o-o-o-.  rings of four
    |   .-------'                   |           '-> arrives at         ring 1    o-o-o-o-.  close straight
    y+1 o-o-o-o-.                   |               (0, y + 2):        :         : : : :
        .-------'                   |   so no four steps close;        ring L-1  o-o-o-o
    rings of four close             |   the shortest way round          joined to  2 3 0 1   ring 0 shifted by two
    straight: wraps (4, 0), (0, L)  |   is six: wraps (4, 2), (0, L)    ring 0 at x =        round: wraps (4, 0), (2, L)
    S = 1.25 N (curled)             |   S = N, X = 0 (flat), width 6    S = 1.25 N (curled); not O116's graph
```

**Sketch C: the hand-built lip** (ours; not the shape of record, item 1(c)). A stretch of tube four around joined at
both ends to a stretch of sheet six around, closed into a torus; at each joint the four tube points link to four of
the six sheet points (the pairing the two kinds of point allow) and the two sheet points left over are joined by a
chord.

```
    tube, four around            the joint                 sheet, six around
    ring l4-2   T0-T1-T2-T3-(T0)                            S0-S1-S2-S3-S4-S5-(S0)   ring 0
                |  |  |  |       T0-S1   T1-S2              |  |  |  |  |  |
    ring l4-1   T0-T1-T2-T3-(T0) T2-S5   T3-S4              S0-S1-S2-S3-S4-S5-(S0)   ring 1
                                 S0---S3 (the chord)        :  :  :  :  :  :
    the other end of the tube (ring 0) is joined to the sheet's last ring the same way, closing the torus
```

**Sketch D: the curvature brief's handle, and why as built it is a cross-handle.** A flat 14 × 14 torus; two
lattice links (u1–v1, u2–v2, two sides of one lattice square) are cut at each of two places, and the four loose ends
are tied to the four points of a ring of four; three such rings stacked make the handle, the middle one a curled
ring (its ring links carry three squares).

```
    sheet ... u1   v1 ...            layer 0   o-o-o-o   tied to u1 v1 u2 v2 at place a
              x    x   (links cut)   layer 1   o-o-o-o   the middle ring (curled)
    sheet ... u2   v2 ...            layer 2   o-o-o-o   tied to u1 v1 u2 v2 at place b
    as built: place b tied the same way round as place a  -> a band along a column comes back flipped (cross-handle)
    control:  place b tied with u1 and u2 swapped          -> it comes back as it left (a handle)
```

**Sketch E: rings of diagonals** (points of one kind, shown as o; the other kind as .; a face is a square with one
point of each kind at opposite corners).

```
    the inner square round c           the zigzag round the curl             the one-pass zigzag along
    (four faces, four diagonals)       (between rings y and y+1 of a tube)   (between columns 0 and 1)
          o                            (1,y+1)   (3,y+1)                      (0,0) . (1,1) . (0,2) . (1,3) ...
       .  |  .                             \   /   \   /                      steps right, left, right ... and
    o --- c --- o   each diagonal        (0,y)   (2,y)   (0,y)                closes through the junction after
       .  |  .      is a corner-to-     four faces, exits alternating         ONE pass: b faces; on a surface
          o         corner of a face    rings; 0 on every graph built         closed through a reflection it can
                    at c: reads 0                                             come back flipped (item 3)
```

---

## The entry (to replace the box's present line "The twist: not yet defined on the graph ...")

- **The twist (PROPOSED 23 October, revised twice the same day; ours; hers to confirm, change or refuse before any
  test depends on it; it replaces "not yet defined on the graph").** This entry defines **two twist-like quantities
  fixed by the wiring and a named face rule**, of different kinds, and says what each carries of her picture. **(1) The
  mod-2 orientation character** of a closed cycle on the surface the squares make, under the named face rule and, where
  the rule ties, our completion convention (item 1): whether a band carried once round the cycle comes back flipped
  (**1**) or as it left (**0**). It carries no direction and no count. **(2) The seam shift** of a lattice torus,
  flat or curled: how far a seam is shifted when the torus closes, a whole number in a named presentation, blind to
  mirror images (+r and −r are the same graph). It is a count, but of a whole lattice piece, not of a ring or a
  diagonal, and it carries no sign; only the pair of wraps up to the grid's own symmetries is intrinsic (item 4).
  What her picture asks beyond these (a sign; a count on a ring; thirds as angles) needs a declared label or an
  embedding, and is not defined by this entry.

  1. **The surface, the rule, and what the rule leaves open (exact on built graphs; sandbox).** Where every link lies
     in exactly two squares, the squares form a closed surface by themselves (the flat tori; the flat Klein grids of
     item 2). Where a link carries three squares they do not: on the 4 × L tube every point carries five squares and
     every ring link three, so a face rule must say which squares are the tiles. **The rule used here is the
     curvature brief's**: at each point, the rotation of four corners with the smallest angle sum. The angle sum and
     the vertex type are [T25] Sec. IV.2's (**published**; that section was read in full for that brief); choosing
     point by point on an arbitrary graph is **ours**. On the tube (L = 8, 12, 16) it picks, at every point and with
     no ties, the four squares between rings: the faces are the 4L between-ring squares, and the L ring squares (the
     curl itself) are not faces but closed cycles that go round the tube. The same holds, with no ties, on **the
     tube's zero-cost family** (O150): the reflected closure, one switch from the tube, and the half-turn closure, one
     switch from the reflected closure and so two from the tube (checked here: 2 links out and 2 in; 4 and 4; 2 and 2);
     "drop the ring squares" chooses the same faces (torus reading, L = 8 to 48).
     - **Where the rule as written is silent, and how this entry completes it (ours, proposed).** The rule says
       nothing about a tie between rotations of the *same* vertex type, nor about which shortest cycle is the face
       when a corner has several (the curvature brief's "ties" counter counts only ties between *different* types, so
       its "ties 0" hides these). This entry takes every completion (every tie broken every way, every ambiguous
       corner given each of its shortest cycles). Ties of the same type are counted and reported as ties.
     - **The local criterion (ours, proposed; it replaces the first revision's global one).** Closure is global: a
       completion closes the whole graph only if every chosen face is chosen at all its points everywhere, so one
       blocking defect anywhere would leave every cycle of the graph "undefined", which says nothing about where the
       surface fails. The entry therefore reads everything by region. (i) *The character of a cycle uses only the
       band round it*: it is defined under a completion when every link of the cycle lies in two faces chosen at
       both its ends and the faces at each of its points are corners of that point's rotation; a defect elsewhere
       does not touch it. (ii) *A completion closes on a region* (every face inside the region chosen at one of its
       points is chosen at all of them), and the region's *band* is its faces inside the region; the band is read as
       one-sided or two-sided over every completion that closes on the region, after dropping those pinched there.
       (iii) *The value of a quantity* is taken over the completions that close on the region holding the cycle's
       band and are unpinched there: if all of them agree, that is the value; if none exists, the quantity is
       undefined; if they disagree, or if it is defined under some and not others, the entry reports "defined in k of
       m, values ...", and takes a value only when all k agree. (iv) *Where a surface fails* is read from the local
       failures (points round which no completion closes on the three-step ball), which depend on the graph and the
       rule alone; the depth a backtracking search reached before failing depends on its order and is not used.
       (v) *The regions* are the curled part, the opened part and all points together; the outcome words of item 6
       are defined through their bands, so that they are exclusive: TWIST IN THE CURL means the curled part's own band
       is one-sided, TWIST IN THE OPEN the opened part's, TWIST ACROSS THE LIP that neither is while the band of all
       points together is. On the built graphs this criterion reads: the tube, the half-turn closure and the 4-cube
       ALL TWO-SIDED; the reflected closure TWIST IN THE CURL (every point of it is curled, and its band is a Klein
       bottle); the flat Klein grids TWIST IN THE OPEN; the curvature brief's handle as built TWIST ACROSS THE LIP and
       its mirrored control ALL TWO-SIDED (item 1(b)); the hand-built lip NO SURFACE AT THE LIP (item 1(c)). No local
       failure exists on any of them except the lip.
     - **(a) The 4-cube** (the 4 × 4 torus; six squares at every point): all 16 points tie three ways, between
       rotations of one type, (4,4,4,4). The curvature brief's own tie-break (slot order) closes nothing: 0 of 32 links
       lie in two chosen faces. **Each of the three axis pairings closes into a torus**: the 4-cube has four axes,
       and pairing them the same way at every point gives three completions; the full search finds exactly these
       three and no others, all tori (V − E + F = 0, two-sided). Of the three same-slot rotations only one is an axis
       pairing (slots (0, 1) with (2, 3)); the other two mix axes from point to point and close nothing. So on the
       4-cube the faces are undetermined but the surface's kind is not: every closing completion is a torus and every
       cycle reads 0 under each.
     - **(b) The curvature brief's "handle"** (a flat 14 × 14 torus with a 3-layer handle of circumference 4 spliced
       in; N = 208; sketch D): 8 points tie, the four of each end layer, between two rotations of type (4,4,4,6), and
       **each tied point has one rotation with a corner closed by two equal hexagons, so three choices per point and
       3⁸ = 6,561 completions**. Under slot order 20 points fail (4 in each of the three handle layers, the middle ring
       among them, and 8 lattice points at the splices) and a middle-ring link lies in three chosen faces. **Exactly
       one completion closes: V − E + F = −2 and one-sided.** Its middle ring reads 0; a cycle along any of the
       handle's four columns and back through the lattice reads **1**. **Control:** the same handle with one splice
       mirrored (its two same-kind ends swapped): again exactly one completion closes, V − E + F = −2, **two-sided**,
       every cycle tried 0. So the handle as built is spliced the same way at both ends, which makes it a
       *cross-handle*: the first draft's only built lip carried a twist itself, and the twist runs along the handle,
       not round it. Read by region: the curled part (the 12 handle points) closes with one distinct band, two-sided,
       bounded by the 8 ring links of the end layers; the opened part (180 lattice points) closes two-sided; all
       points together close once, one-sided as built: **TWIST ACROSS THE LIP**, and ALL TWO-SIDED for the control. (The
       curvature brief's description of this graph as "a handle" needs the same note; that file is not edited here.)
     - **(c) A hand-built lip** (sketch C; N = 68 and 96; valid, bipartite; tube interior at five squares, every
       other point at four). **Its shape is ours and is not the shape of record**: the opening's product on the
       record is the tube with its ring seam shifted by two (O116), four-point rings glued with a shift, in which no
       closed ring of six stands beside a closed ring of four; this graph joins closed rings of four to closed rings
       of six through a chord, a shape no saved state has been read to have (*ours, from the check's note, unverified:*
       a boundary between closed rings and that shifted gluing would need a dislocation-like defect, since the two
       kinds of point force an even shift). 16 points tie (the eight joint tube points and the eight paired joint
       sheet points), each between two rotations of type (4,4,4,6), each with three shortest hexagons at its hexagon
       corner (six options a point). Every one of those 36 hexagons passes a chord end, whose only option is four
       squares, so no hexagon can be chosen at all its points and **no completion closes on the whole graph**. By
       region: the curled part (the 32 or 48 tube points and the 8 paired sheet points) closes with 256 distinct
       bands, all two-sided, bounded by the 16 links to the chord ends and the sheet; the opened part (the sheet
       interior and the 4 chord ends) closes with one band, two-sided; the local failures are exactly 32 points, the
       4 chord ends, the 8 paired sheet points, the 8 joint tube points and the 12 sheet points of the rings beside
       the joints, every one on or beside the lip: **NO SURFACE AT THE LIP**, located by the criterion and not by a
       search. The second check's own code (outside the repository) found no closing completion for any of the 24
       bipartite-compatible pairings of the joint at N = 68; that is its result, not reproduced here.
     - **Where the character is defined under this rule:** on a flat region, on the tube and its zero-cost family, on
       the 4-cube (its kind, not its faces), across the handle's splices (one completion), and on either part of the
       hand-built lip taken alone; not on a cycle through its joint. Whether the lips of the saved partly opened states
       look like the splice, like the chord, or like neither is unread (item 6). A face rule that closes at such a lip
       would be a new definition with its own line here.

  2. **The character (exact in its values; the notion is published).** Carry a local orientation (a direction of the
     point's rotation) once round a closed cycle of links, through the two faces on each link. It comes back as it
     left (**0**: the band round the cycle is an annulus) or flipped (**1**: a Möbius band). Ellis-Monaghan and Moffatt
     (arXiv:0906.5557, abstract and Sections 1 to 3 read) call a loop with a non-orientable neighborhood *twisted*;
     reading that for a cycle of several links is ours (general knowledge, to verify at Gross and Tucker 1987). It is
     a property of the wiring and the named face rule alone. *Ours, general knowledge, to verify:* it depends only on
     the cycle's mod-2 class, so two cycles that can be slid into each other read alike; every value below is
     consistent with that.
     - **Tube, half-turn closure, flat tori:** closed two-sided surfaces with V − E + F = 0 (tori); every cycle tried
       reads 0 (rings round the curl, lines along, every ring of diagonals of item 3).
     - **The reflected closure** (sketch A; the tube's ring L − 1 joined to ring 0 through x → 2 − x; one zero-cost
       switch from the tube at every λ; valid, S = 1.25 N, X = N): a Klein bottle (O150 records this, pinned by
       `tests/test_exact_torus_counting.py` at L = 8, 10, 12, 24; the classification of closed surfaces is textbook,
       not re-read). **Cycle by cycle (sandbox):** the two lines of links along the tube through the points the
       reflection fixes (x = 1 and 3; length L) read **1**; the line through the other two points (length 2L) reads 0;
       **every ring of four round the curl reads 0.**
     - **The flat Klein grids**: an a × b grid whose rows wrap round and whose last row is joined to the first through
       a reflection. Two families built: x → −x with b even (6 × 6, 6 × 8, 8 × 8, 6 × 10, 8 × 12) and x → 1 − x with
       b odd (6 × 5, 6 × 7, 8 × 5, 8 × 7, 8 × 11, 8 × 13, 10 × 5, 10 × 7, 12 × 5, 16 × 5). Every one is valid under the
       hard-core rule, bipartite, with every link in exactly two squares, so S = N, X = 0 and **H = 0 at every λ**; a
       Klein bottle with all squares as faces, no rule needed. **The two families carry the flip differently.** In the
       even family the reflection fixes the columns x = 0 and x = a/2, and the lines of links through them read 1,
       the other lines 0. In the odd family the reflection x → 1 − x fixes no column: **every straight line of links
       reads 0**, and the flip sits on the smooth zigzag of diagonals along the strip the reflection maps to itself
       (between columns 0 and 1, and between a/2 and a/2 + 1), which closes after one pass, b faces, and reads **1**
       (item 3). Every ring round reads 0 in both families. Quadrangulated Klein bottles are a published family
       (Thomassen 1991, recorded in the 20 October note; not read by us).
     - **What the record already has (so none of this is new to it).** ASSUMPTIONS O116, last addendum (11 October;
       `scripts/read_flat_kind.py`, tests in `tests/test_read_shapes.py`; an exploratory reading): a Klein bottle
       built for the purpose has H = 0 at every λ, "so the toy's zero-energy states include one-sided ones"; and of
       the 9,865 exactly flat end states of T8, T23, T24 and T60, 9,676 are one torus six around, 2 one wider torus,
       182 in two to four pieces, and **39 hold a one-sided piece of 18 to 64 points, the 5 whole 64-point Klein
       bottles among them** (the reader lists every end state with any one-sided piece, whole ones included). O122
       (the outside reviewer's independent reading of T60): of T60's 3,521 reached flat end states, 3,446 narrow tori,
       73 in separate pieces and **2 Klein bottles, which are two of those 5** (O116's count covers T60, and O120
       records that the two readers give the same three counts for it). The note to T61's stage-1 reading
       (PREREGISTRATION): one end state at λ = 1.40, N = 96 is a torus of 56 points six around beside **a Klein bottle
       of 40 points**. T62's stage-1 reading: one end state exactly flat, eight around and one-sided at N = 96, and one
       one-sided at N = 192 with an eighth of its six-loop excess left (μ = 0.10, g = 2.0); T64: none holds a one-sided
       piece. So the chain does reach one-sided flat states, and that was read twelve days ago. **What is new here
       (sandbox):** which cycles carry the flip (along; through the reflection's fixed points on the reflected closure
       and the even grids, on a one-pass diagonal zigzag with no fixed point on the odd grids; never a ring round the
       curl on any built example); that the reflected closure, O150's zero-cost neighbor of every tube at every λ, is
       where a one-sided surface sits one free move from X's stand-in; the one-pass rings of diagonals along it
       reading 1 (item 3); the odd-row family of flat Klein grids; and what the face rule does where it ties (item 1).

  3. **A ring of diagonals (exact; sketch E).** A closed sequence of points of one kind, consecutive points being the
     two opposite corners of one face of the surface; that face is unique (the hard-core rule), and since a square's
     two diagonals join one same-kind pair each, a ring of diagonals is of one kind by itself (the brief's exact
     item 1). Its band is carried from face to face through the shared point's rotation, and its character is defined
     wherever every face it uses is a face of the surface under the rule. Values on the built graphs (sandbox): the
     inner square of four diagonals round a point (her "a 45degree inner square", 23 October) reads 0 everywhere,
     being the edge of that point's disc; the zigzag of diagonals round the curl between two rings reads 0 on every
     graph built, the Klein bottles included; **a ring of diagonals that runs once along the tube and closes through
     the reflected junction reads 1** on the reflected closure (the one-pass zigzags through columns 0, 1 and 2, and
     two crooked rings with unequal steps left and right) and 0 on the tube and the half-turn closure. **On the
     reflected closure and the even-family grids** the straight 45° line and the zigzag that closes smoothly wind
     twice along the surface and read 0, while the one-pass zigzags through the fixed columns (x = 0 and a/2 on the
     grids) read 1 and the one through x = 1 does not close. **On the odd-family grids** the smooth zigzag between
     columns 0 and 1 (and between a/2 and a/2 + 1) itself closes after one pass, b faces, and reads 1, with no fixed
     point anywhere; the other smooth zigzags wind twice and read 0. **The ring square's own diagonals are not on the
     surface under this rule, because the ring square is not a face: no band passes through them, so nothing is
     defined there under this rule.** (A different named rule could put the ring square on the surface, at the price
     of a hexagon face; that would be a new line.)
     - **Hers, on which segments are real (23 October, verbatim):** "the curling cost in the diaconal hypotenuse of
       the cubes surface or internal, same point type to same point type; link implies the cubes edges, connecting
       the 2 different points, the matter point with the antimatter point. which are not real in our model they are
       just helpful to visualize". *Exact, the consequence recorded in the notebook beside her words:* every same-kind
       segment keeps the kind, so same-kind diagonals alone leave the two kinds as two separate networks that never
       touch (in two directions two square lattices turned 45°; in three, each kind's face diagonals a face-centered
       cubic lattice). This entry's rings of diagonals are of one kind by construction, which fits her "same point
       type to same point type"; what joins the two kinds, in her picture, is hers to say, and nothing here decides it.
     - **Ours, to confirm:** that her "a 3d hypotenuse" ("I meant a twist, a 3d hypotenuse, not this whole thing.
       Maybe an electron, maybe a quark", 23 October) is, in two directions, the diagonal of the ring square (the
       √2 segment across the curl). The record also says the twisted hypotenuse has no object in the stiff toy
       (notebook, 23 October) and that two directions have no body diagonal (reading note, fact 5), so the
       identification is ours and waits on her.

  4. **The seam shift (exact on built graphs; already on the record; sketch B).** A lattice torus, flat or curled, is
     the grid wrapped up by two wraps. In a presentation that names the ring (a points round, in a direction) and the
     junction (L along), the wraps read (a, r) and (s, L): **r is the ring seam's shift** (a walk once round the ring
     arrives r steps along), **s the junction seam's shift** (a walk once along arrives s steps round); r is defined
     modulo L and s modulo a, each up to sign, since a mirror image is the same graph. What is intrinsic to the graph
     is only the pair of wraps up to the grid's own symmetries (*ours*); the whole numbers belong to the presentation.
     O116's end state is "the tube with its seam shifted by two": r = 2, s = 0: four points to a ring, but a walk round
     the ring arrives two steps along, so no four steps close and the shortest way round is six (wraps (4, 2) and
     (0, L)). The 20 October note, sec. 7, records the published form: the twisted grids T(n, m, r) with "a torsion of
     r squares" ([LZZ23], citing Thomassen 1991; neither read in full). Checked here (sandbox) on the 4 × 16 tube with
     its ring seam shifted by r = 0, 2, 4, 6, 8 (O116's builder): all valid and bipartite; r = 0 is the tube
     (S = 1.25 N, width 4); r = 2, 4, 6, 8 are flat (S = N, X = 0) with widths 6, 8, 10, 8; **the five are pairwise
     non-isomorphic; r = +2 and r = −2 are isomorphic** (mirror images; no absolute sign). Going from the tube to r = 2
     changes every seam link (16 out, 16 in). **The half-turn closure is the other "shift by two":** r = 0, s = 2, the
     lattice torus with wraps (4, 0) and (2, L) (`flat.graph(4, 2, L)` of O119; isomorphic, checked), that is, the
     tube with its *junction* seam shifted by two round the ring; it keeps the rings of four (S = 1.25 N) and is
     **not** O116's twisted tube (not isomorphic to r = 2, nor to the tube). **Why it is a second quantity:** the tube
     (r = 0, s = 0), the half-turn closure (r = 0, s = 2) and O116's end state (r = 2, s = 0) are three different
     graphs on which every cycle reads character 0, so the mod-2 character misses a count that the opening itself
     changes, the ring seam's shift from 0 to 2.

  5. **What this carries of her picture, and what it cannot.** **Hers** (verbatim, `sandbox/NOTEBOOK.md`):
     21 October, "It could have a twist in it like one point is facing the other direction (to be turned away from
     its closest same type neighbor) so matter and antimatter would hold a twist in different directions"; 23 October,
     "I meant a twist, a 3d hypotenuse, not this whole thing. Maybe an electron, maybe a quark"; "Dark matter carries
     a half twist, so 2 loops are needed for a dark matter Full twist."; "it must twist, either 1/3 clockwise or
     counterclockwise. But in order for the loop to close on itself it needs a full twist."; "Charge is only spin,
     speed of spin matters."; "A higher twist count holds more curling energy and has more mass, not more charge.";
     "twist_2 = 1/3, twist_sqrt2 = 1/2, twist is always the same"; "twist count and clockwise/counterclockwise".
     **Ours, which she quoted and affirmed:** "a count that only the snap can change" is the paper 18 outline's
     (`docs/papers/particles/outline.md`, labelled ours there: Sakharov's first condition said plainly; VISION
     Update 85's test (2)); she quoted it inside her message of 21 October and answered the question built on it with
     "-> yes" (VISION Update 90). Her own word for a count is "twist count" (23 October).
     - **Carried by the character (ours, to confirm as a reading of her dark half twist):** a half twist with no
       direction, as a cycle of character 1. The reflected closure is the first object in the toy that carries one,
       and the tube reaches it by one free move. *Ours:* on every built example the flipped cycles run along the tube
       (or along the handle), never round the curl, so the half twist is not where "a 3d hypotenuse" across the curl
       would put it, and the diagonal across the curl carries no band under this rule (item 3). **Not carried in her
       sense:** "2 loops are needed for a dark matter Full twist". The character is a yes-or-no: two passes round a
       flipped cycle read 0, the same as no twist at all (on the reflected closure and the even grids the straight 45°
       line and the smooth zigzag, which wind twice, read 0), so it cannot tell a full twist from no twist.
     - **Carried by the seam shift:** a whole number the wiring fixes once a presentation is named, which the opening
       changes (the ring seam's shift, 0 → 2): a count, but of a whole lattice piece. It is not her "twist count" on a
       ring or a diagonal, it is not a twist of the curl, and it has no sign.
     - **Neither carries a sign:** matter against antimatter ("hold a twist in different directions") is not told
       apart by either; a Klein bottle is one surface, and r = ±2 are one graph. *Ours, unverified:* whether two regions
       of one graph twisted opposite ways can be told apart in the wiring, which O116 raises ("whether the two
       possible twists, one each way, meeting along a tube that opened from two places, is what leaves a knot"), is
       the one place a sign could live without a label, and it is unread.
     - **Not carried by either:** a count on a ring ("A higher twist count holds more curling energy"); thirds or
       quarters as angles. A ribbon graph forgets full twists (Ellis-Monaghan and Moffatt, read in part); Tw, Wr and
       the linking number need a curve in three-dimensional space (Fuller 1971, read in full; Dennis and Hannay 2005,
       read in full). **What each would need:** for a sign or a count on a ring, a **declared label** on each diagonal
       or each ring (the framed graph of Bilson-Thompson, Markopoulou and Smolin 2007, read in part), with rules
       written before any test for its *birth* (the value a diagonal is born with when a switch makes its square), its
       *death* (lost, moved to a named neighbor, or the move refused), its *composition* round a ring (whole numbers,
       halves, quarters or her sixths) and *which moves may change it* (the snap only, the rule she affirmed); with a
       label the lip test becomes bookkeeping of the declared rules, not a measurement of the toy (rule 13). For thirds
       and quarters as angles, an **embedding**: stage B with coordinates, where a tape along a body diagonal can lie
       flat in one of three planes 60° apart (exact; notebook, 23 October); stage B's lengths alone do not supply it,
       since a Möbius band and an annulus can carry the same lengths.

  6. **The saved-state look this enables, and its guard.** **No saved state is opened, in the sandbox or otherwise,
     until two things are in the notebook: her confirmation (or change) of this entry, including the completion
     convention of item 1 and the two readings marked "to confirm" (the 3d hypotenuse, the dark half twist), and her
     answer to the prediction question below** (rule 20 for the first, rule 16 for the second).
     - **Every two-direction tube family with saved wiring, by directory name** (names and file counts only; nothing
       opened): `results/t8_*_adj` (8 directories, 960 end states), `t23_*_adj` (28; 3,360), `t24_*_adj` (28; 3,360),
       `t60_*_adj` (35; 4,200), together the 11,880 of O116; `t7d_lam125_n{64,96,144,192a,192b}_adj` (5; 12 decays);
       `t37_*_adj` (34; 340 long tubes that seeded themselves, up to 1,024 points, which O88 found melted when warm);
       `t38_*_adj` (48; 10,000 waiting-time replicas); `t51_*_adj` (91; 600 cooled sheets, O107's knots);
       `t61_*_adj` (14; 720); `t62_*_adj` (30; 720); `t63_*_adj` (10; 240); `t64_*_adj` (15; 360).
     - **Read for one-sidedness (exploratory readings; the counts in item 2):** the 9,865 exactly flat end states of
       T8, T23, T24 and T60 (O116, last addendum; O122 independently for T60); T61's 27 flat end states (its stage-1
       note); T62's flat end states (its stage-1 reading at N = 96 and 192; its held-out N = 384 had none exactly
       flat); T64's (its stage-1 reading: none one-sided; its held-out N = 384 reading reports three end states in
       pieces and no one-sided piece). `scripts/analyse_t62.py`, `analyse_t63.py` and `analyse_t64.py` read
       one-sidedness for flat end states from the wiring.
     - **Not read for one-sidedness:** the 2,014 end states of T8, T23, T24 and T60 that are converted with energy
       left (O116's 12 October addendum read their widths from clear points only) and the one end state that is still
       a tube (so 9,865 + 1 + 2,014 = 11,880); every end state of the T7 decays, T37 and T38; T51's 600 cooled sheets;
       T61's roughly 693 non-flat end states; the non-flat end states of T62 (720 saved, of which the stage-1 reading
       found a handful flat) and T64 (360 saved); and all of T63, **which stays closed under rule 16(b)**: T63 was NOT
       READ by its own rule (its rows were not read, PREREGISTRATION, the T64 reading), so none of its results may be
       opened. These are the states with curled parts, flaws or a lip, which is where the local criterion of item 1
       matters.
     - **Kept for a registered version (rule 16(c); ours, proposed):** the sandbox look opens only the T7 decays and
       the non-flat end states of T8, T23 and T24 at N = 64 to 192; the non-flat end states of T60 (whose N = 288 is
       the λ map's held-out size), T61, T62 and T64, and the whole of T37, T38 and T51, stay unopened for the registered
       version, or that version runs new seeds; T63 is closed to both. Either way, one line in the registration says
       what the sandbox showed and how many looks came before.
     - **The questions, per state, under the local criterion of item 1:** (i) on which regions does a completion
       close (the curled part, the opened part, all points), and where do the local failures lie (by region; on or
       beside the lip, or away from it); (ii) for each region that closes, is its band one-sided or two-sided, and do
       the completions agree; (iii) the outcome word; (iv) for each flat piece, its ring seam's shift in O116's
       presentation (rings round the tube's short direction). Outcome words, fixed before any state is opened, each
       defined through bands and calibrated on a built graph: ALL TWO-SIDED (all points close, every band two-sided;
       the tube, the half-turn closure, the 4-cube, the mirrored handle); TWIST IN THE OPEN (the opened part's own
       band is one-sided; the flat Klein grids; in a state with no curled part this is O116's whole one-sided flat
       piece); TWIST IN THE CURL (the curled part's own band is one-sided; the reflected closure); TWIST ACROSS THE
       LIP (neither part's band is one-sided, the band of all points together is; the cross-handle); NO SURFACE AT THE
       LIP (no completion closes on all points, every local failure on or beside the lip; the hand-built lip); NO
       SURFACE AT A FLAW (no completion closes on all points and some local failure lies away from the lip; no built
       example). Where the closing completions disagree on a region, the counts are reported and no word is given.
       What it cannot be: a kill test for "the stiff toy carries a twist by itself", which is exact already (items 2
       and 4).
     - **Counting only, no run (sandbox):** a reflected closure (N = 4L; S = 1.25 N, X = N, H = 4(λ − 1) N) and a flat
       Klein grid of the same N both exist **at least at** every even L from 10 to 48. The even family needs
       4L = a · b with a and b even and at least 6; the odd family needs 4L = a · b with b odd and at least 5 and a a
       multiple of 8 (so that a is even and a · b is a multiple of 8, as 4L is for even L), which gives L = 10, 14, 18,
       22, 26, 30, 34, 38, 42, 46 and others; at L = 8 neither family is valid at N = 32. The full list needs the
       classification (Thomassen 1991), which has not been read. The grid has H = 0 at every λ, so an opening of the
       reflected closure into it would release the tube's 4(λ − 1) per point, the same as into a flat torus; the switch
       keeps no orientability (the tube to the reflected closure is one switch), so nothing exact forbids the Klein
       bottle as an end state; whether anything exact favors the torus over it (renaming counts, wrappings) **has not
       been computed** for the Klein grids. **The chain reaches both** (item 2: 39 flat end states with a one-sided
       piece, and T61's and T62's, against thousands of tori), and the question left is where, in a state with curled
       parts, the flip sits.

  7. **Not yet defined by this entry:** the sign, a count on a ring, and the price per twist (the box's "The ring's
     price", open). Tests 4 and 5 of the brief stay held; her predictions for them (Update 90) stand as recorded and
     are not scored.

---

## Plain-language read-back for the owner

1. The toy's squares, taped together along their links, make a surface, like tiles.
2. On the tube some links carry three squares, so a rule has to say which two are the tiles there; the rule from the
   curvature brief (the one that reads curvature from the wiring) keeps the squares between the rings and leaves the
   rings themselves out.
3. On the surface, a closed path either has an ordinary band round it (an annulus, two sides) or a Möbius band (a
   strip joined after a half turn, one side); that yes-or-no is one of two twist-like things the wiring carries by
   itself, and it needs only the band round the path, so a flaw elsewhere does not spoil it.
4. That rule sometimes ties, and where it ties we try every way of breaking the tie, region by region: on the 4-cube
   every way that closes gives a torus; on the brief's handle exactly one way closes the whole; on a lip we built
   ourselves (tube four around joined to sheet six around through a chord, a shape of our own and not the shape your
   opened tubes take) the tube part and the sheet part each close by themselves, nothing closes across the joint, and
   the points where it fails all sit on or beside the joint.
5. A Klein bottle is a closed surface with one side, like a tube whose end is joined back to its start through a
   mirror (sketch A); your opened tubes already include a few: 39 of the 9,865 flat end states hold a one-sided piece,
   5 of them whole 64-point Klein bottles (O116); the second reader found 2 in T60, and they are two of those 5; T61
   has one 40-point piece, and T62 one at 96 points and one at 192.
6. One free move from the tube, costing nothing at any λ, gives the tube closed through a reflection, whose surface
   under the rule is a Klein bottle: the paths along it through two of its four lines are flipped, and rings round
   the curl never are. On the flat Klein grids with an odd number of rows no straight line is flipped; the flip sits
   on a zigzag of diagonals along the grid.
7. The yes-or-no has no direction and no count: it cannot tell your two directions of twist apart, and two trips
   round a flipped path read the same as no twist, so "2 loops are needed for a dark matter Full twist" is not
   carried in your sense.
8. The second thing is a count: how far a torus's seam is shifted when it closes, read once we name which seam is the
   ring (sketch B). The opening changes the ring seam's shift from 0 to 2 (O116's end state), but it belongs to a
   whole lattice piece, not to a ring, and +2 and −2 are the same graph.
9. The diagonal across the curl, which we read as your "3d hypotenuse" in two directions (ours, to confirm), is not
   on this surface because the ring square is left out, so nothing is defined there under this rule.
10. Your sign for matter against antimatter and your twist count on a ring each need either a declared number with
    rules for birth, death and the snap, or stage B's coordinates; your thirds as angles need the coordinates. "A
    count that only the snap can change" was our phrase, which you affirmed; your word is "twist count".
11. The test this unlocks reads only the saved end states nobody has read for one-sidedness yet (those with curled
    parts, flaws or a lip; the list is in item 6), and no state is opened until both your confirmation of this entry
    and your answer below are in the notebook. T63 stays closed whatever you answer, because it was never read by its
    own rule.
12. Tests 4 and 5 stay held until a sign or a count on a ring is declared.

## The one prediction question for the saved-state look (asked only after the entry above is confirmed)

> First, what is already known, so that you are not asked to predict it. Of the 9,865 opened tubes that ended exactly
> flat (T8, T23, T24, T60), 9,676 are one torus six around, and 39 hold a one-sided piece of 18 to 64 points, 5 of
> them being one whole Klein bottle of 64 points, a one-sided surface with no curl and no lip in it (O116). A second,
> independent reading found 2 Klein bottles among T60's 3,521 flat end states (O122); they are two of those 5. T61 has
> one flat end state with a 40-point Klein bottle beside a torus, T62 one at 96 points and one at 192, T64 none. None
> of the end states that still hold curled parts, flaws or a lip has been read for this.
>
> The unread end states are: the T7 decays (12), the 2,014 end states of T8, T23, T24 and T60 that kept some energy
> and the one that is still a tube, T37's 340 long tubes, T38's 10,000 waiting-time replicas, T51's 600 cooled sheets
> with their knots, T61's roughly 693 non-flat end states, and the non-flat end states of T62 and T64. (T63 is closed:
> it was never read by its own rule.) For those: do you expect every one of them to be two-sided, or some to be
> one-sided? If some, where do you expect the flip to sit: in the opened part by itself (as in the flat ones already
> read); in the curled part by itself; or only in the two together, across the lip? And at the lip itself, do you
> expect the surface to close under the rule, or to fail there? Say so if you expect the rule to have no surface at
> the lip at all: on the one lip we built by hand, a shape of our own that joins rings of four to rings of six through
> a chord and is not the shape your opened tubes take, it has none.

## Proposed LOG line (for `sandbox/LOG.md`; not written by this task)

2026-10-23. Twist definition draft, second adversarial check applied (thirteen corrections; `sandbox/twist_character_check.py` rerun, 956 lines, ends "done"). Seen: the first revision double-counted the one-sided end states (the 5 whole Klein bottles are among O116's 39; O122's 2 are two of the 5), left T51, T61 to T64 and the non-flat states out of the inventory, labelled an exploratory reading "measured" and our phrase "a count that only the snap can change" hers; its closure test was global and its failure point search-order dependent. Replaced by a local criterion read by region (a completion closes on a region; its band one-sided or two-sided; local failures by the 3-step ball): tube, half-turn closure, 4-cube ALL TWO-SIDED; reflected closure TWIST IN THE CURL; flat Klein grids TWIST IN THE OPEN (odd rows: no straight line flipped, the one-pass diagonal zigzag is); the brief's handle as built TWIST ACROSS THE LIP, mirrored ALL TWO-SIDED; the hand-built lip NO SURFACE AT THE LIP, with all 32 local failures on or beside the joint. All sandbox; nothing from `results/` opened; the entry waits on her confirmation and her prediction.

---

## Where each number above comes from

| Statement | Source | Kind |
|---|---|---|
| Tube: five squares per point, ring links at three; rule picks the 4L between-ring squares, no ties; torus; all cycles 0 | `twist_character_check` L = 8, 12, 16; curvature brief Sec. 2; torus reading sec. 4 | exact; sandbox look (not yet pinned by a test; can narrow, not support) |
| Zero-cost family is the chain tube – reflected (one switch) – half-turn (one more): 2/2, 4/4, 2/2 links out/in | `twist_character_check`; O150 (`test_the_zero_cost_family_of_the_tube_is_three_classes`) | exact (O150's part pinned by a test) |
| Reflected closure: valid, S = 1.25 N, X = N; Klein bottle | O150, pinned by `tests/test_exact_torus_counting.py` at L = 8, 10, 12, 24 | exact |
| Reflected closure: lines x = 1, 3 read 1, the 2L lines 0; rings 0; one-pass diagonal rings along read 1, rings of diagonals round read 0 | `twist_character_check` L = 8, 12, 16 | exact; sandbox look (not yet pinned by a test) |
| Half-turn closure: torus, all 0; = `flat.graph(4, 2, L)`, wraps (4, 0), (2, L) | `twist_character_check`; `tests/test_exact_torus_counting.py` | exact |
| Flat Klein grids, two families: valid, S = N, X = 0, Klein bottles; even family lines x = 0 and a/2 read 1; odd family no line reads 1, the one-pass diagonal zigzag between columns 0 and 1 and a/2 and a/2 + 1 reads 1 with b faces | `twist_character_check` at the 15 sizes listed in item 2 | exact; sandbox look (not yet pinned by a test) |
| 4-cube: three-way tie at every point; slot order closes nothing; each of the three axis pairings closes into a torus; one same-slot rotation is an axis pairing; 3 closing completions in all | `twist_character_check` section B | exact; sandbox look |
| Handle (N = 208): 8 tied points, 3 choices each, 6,561 completions, exactly one closes, χ = −2, one-sided; along-handle cycles read 1; mirrored control two-sided, all 0; 20 slot-order failures split 4 / 4 / 4 / 8; by region: curled band two-sided, opened two-sided, all one-sided (ACROSS) | `twist_character_check` section C | exact; sandbox look |
| Hand-built lip (N = 68, 96): 16 tied points with six options each; every hexagon passes a chord end; no completion closes on all points; curled part 256 distinct two-sided bands, opened part one two-sided band; 32 local failures, all on or beside the lip | `twist_character_check` section D | exact; sandbox look |
| No closing completion for any of the 24 bipartite-compatible joint pairings at N = 68 | the second adversarial check's own code, outside the repository | exact on its graphs; not reproduced here |
| Seam shifts 0, 2, 4, 6, 8 at 4 × 16 pairwise non-isomorphic; +2 ≅ −2; half-turn closure ≅ `flat.graph(4, 2, 16)`, not ≅ shift 2 | `twist_character_check` section E (igraph isomorphism) | exact; sandbox look |
| Sizes at which a reflected closure and a flat Klein grid coexist ("at least at"); the size conditions of the two families | `twist_character_check` section F, counting | exact; sandbox look |
| 11,880 saved end states: 9,865 flat (9,676 / 2 / 5 / 182; 39 with a one-sided piece, the 5 among them), 1 tube, 2,014 with energy left; a built Klein bottle has H = 0 | ASSUMPTIONS O116, last two addenda (`scripts/read_flat_kind.py`, which lists every end state with any one-sided piece) | exact per graph; exploratory reading of registered runs' saved wiring (not registered; no verdict changes) |
| 3,446 / 73 / 2 of T60's 3,521; the two readers agree on T60 | ASSUMPTIONS O122 (the outside reviewer); O120 | exact per graph; exploratory reading (retrospective; not registered; no verdict changes) |
| A 40-point Klein bottle beside a 56-point torus (T61); one flat one-sided end state at N = 96 and one at 192 with excess left (T62); none (T64) | PREREGISTRATION, the note to T61's stage-1 reading; T62's and T64's stage-1 and held-out readings | exact per graph; exploratory reading (nothing scored changes) |
| Saved-wiring families, directories and file counts | `results/` listed by name (`ls`, `find -name '*.npz'`); nothing opened | exact (a count of names) |
| T63 NOT READ by its own rule | PREREGISTRATION, the T64 reading ("T63's rows, which were not read") | measured status (the registration's own word) |
| "Twisted loop" = non-orientable neighborhood; ribbon graphs forget full twists | Ellis-Monaghan and Moffatt, arXiv:0906.5557, Sections 1 to 3 read | published |
| Lk = Tw + Wr; Tw, Wr need a curve in space | Fuller 1971 (read in full); Dennis and Hannay 2005 (read in full) | published |
| Integer twist as a declared label on an embedded framed graph | Bilson-Thompson, Markopoulou and Smolin 2007 (Sections I to IV, V.A read) | published |
| Angle sum and vertex type | [T25] Sec. IV.2 (read in full for the curvature brief) | published |
| Twisted grids T(n, m, r), "a torsion of r squares"; quadrangulated Klein bottles classified | 20 October note sec. 7 ([LZZ23]; Thomassen 1991, not read) | published, not read |
| Character depends only on the mod-2 class; orientability criterion | general knowledge, to verify (Gross and Tucker 1987) | ours |
| The completion convention and the local criterion (closes on a region; bands; local failures) | this entry | ours, proposed |
| "A count that only the snap can change" | `docs/papers/particles/outline.md` (labelled ours); VISION Update 85; her "-> yes", notebook 21 October, VISION Update 90 | ours, affirmed by her |
| Her words | `sandbox/NOTEBOOK.md`, 21 and 23 October (verbatim) | hers |

## The twelve corrections of the first adversarial check, and what was done with each

1. "New to the record" and "has not been looked at": deleted; O116 (last addendum), O122 and the T61 note cited by their counts; what is new restated (item 2, last bullet).
2. The seam shift added as a second quantity (head; item 4), checked on built graphs (shifts 0, 2, 4, 6, 8 pairwise distinct; ±2 one graph); the half-turn closure placed as the junction-seam shift, not O116's; what each quantity carries and what neither does (item 5).
3. The 4-cube: the failure was the tie-break, not the rule; a completion rule written; all three closing completions tori; same-type ties reported (item 1(a)).
4. The handle: the one closing completion is one-sided because both splices are made the same way (a cross-handle); the mirrored control is two-sided; a hand-built lip built, on which no completion closes; UNDEFINED AT THE LIP redefined as NO SURFACE AT THE LIP (items 1(b), 1(c), 6).
5. The 20 points: 4 in each handle layer (the middle ring included) and 8 at the splices (item 1(b)).
6. Coexistence: "exactly when" replaced by "at least at"; the odd-row family added; the classification named as unread (item 6).
7. Her quotations made verbatim; the hypotenuse identification and the dark-half-twist reading marked "ours, to confirm"; the read-back says the yes-or-no cannot tell a full twist from no twist (items 3, 5; read-back 7, 9).
8. "nothing intrinsic is defined there" replaced by "nothing is defined there under this rule" (item 3).
9. "two zero-cost neighbors" replaced by the chain, with the switch counts checked (item 1).
10. The guard sentence added; which families O116 read and which not, named by directory; which are kept for a registered version (item 6).
11. The prediction question rewritten: the record's counts first, then only the unread end states, with "a whole flat piece is one-sided, with no lip" allowed.
12. Clock time removed from the header; date only.

## The thirteen corrections of the second adversarial check, and what was done with each

Each was checked before it was applied: the record passages in `ASSUMPTIONS.md` (O116 with its addenda, O120, O122), `PREREGISTRATION.md` (the T61 note; the T62 and T64 stage-1 and held-out readings), `scripts/read_flat_kind.py`, `scripts/analyse_t62.py`, `analyse_t63.py`, `analyse_t64.py`, `docs/papers/particles/outline.md`, VISION Updates 85 and 90, `sandbox/NOTEBOOK.md` (lines of 21 and 23 October), `docs/HANDOFF_2026-10-22.md` (task 12) and `docs/design/eq45_ratio_brief.md` were read; `results/` was listed by name only; the script's output was read line by line for corrections 8 and 12.

1. **The one-sided end states were double-counted.** Confirmed: `read_flat_kind.main` appends every end state with any KLEIN piece, whole Klein bottles included, so the 5 are among the 39; O116 covers T60 and O120 says the two readers give the same three counts for it, so O122's 2 are two of the 5. Applied as written (item 2, item 6, read-back 5, the question): "39 ... the 5 among them; O122's 2 are two of those 5; T61 adds one 40-point piece"; "more" and "5 and 2 and 1" deleted.
2. **The inventory of saved states was incomplete both ways.** Confirmed by listing `results/` by name (`_adj` directories and `.npz` counts) and by reading the T62 and T64 readings (one flat one-sided end state at N = 96 and one one-sided at 192 with excess left; T64 none) and the three analysers. Applied in a modified form: every two-direction tube family with saved wiring is listed by directory with its count; T62's and T64's readings are added to "read"; T51, T61's non-flat states, T62's and T64's non-flat states and the tube end state are added to "not read"; the question is widened to all of them; and T63 is excluded explicitly, with the reason the check did not give: it was NOT READ by its own rule, so rule 16(b) closes it (item 6; read-back 11; the question).
3. **The completion rule was not well defined at the scale used.** Confirmed: closure was global, the failure point was the deepest point of a breadth-first backtrack, and the outcome words rested on representatives of a mod-2 class. Applied in a modified form, in code and text: the script now reads, by region, which completions close on the region (face agreement inside it only), the region's band and its sidedness, and the local failures (no completion closes on the 3-step ball round a point), which depend on no search order; the outcome words are defined through the bands of the curled part, the opened part and all points (item 1, the local criterion; item 6). Options differing only in faces outside the region are merged, which is exact for the band and is what made the enumeration finish (the lip's joint points carry six options each, two rotations times three hexagons, and no hexagon can be in any band). The character of a cycle is stated to use only its own band. "Where the completions that close all agree" is replaced by the k-of-m rule. The values on the built graphs are in item 1.
4. **"A count that only the snap can change" is ours.** Confirmed: the particles outline labels it ours; VISION Update 85 has it as test (2); in the notebook of 21 October it is the tail of the assistant's text quoted inside her message (line 2092) and the assistant's question with her "-> yes" (line 2208); the exact phrase is not hers anywhere. Applied as written (item 5; read-back 10; the source table); "twist count" kept as her word.
5. **"Measured" misapplied to exploratory readings.** Confirmed: O116's heading says EXPLORATORY and "which graphs were read and how they are grouped is ours and was not registered"; O122 is retrospective; the T61 note says nothing scored changes. Applied as written: those rows are "exact per graph; exploratory reading of registered runs' saved wiring (not registered; no verdict changes)", and the header defines that kind.
6. **Sandbox looks cited as support.** Confirmed: the eq45 brief marks its own face-rule look "sandbox until pinned". Applied as written: the header says once, for the whole file, that everything cited to the script is a sandbox look that can narrow and not support until promoted to a tested script under rule 6, with one line on what the sandbox showed and that two looks came before; each such row in the source table is marked.
7. **Both quantities overclaimed.** Confirmed. Applied as written: the head says "fixed by the wiring and a named face rule" (with the completion convention where the rule ties); the seam shift is defined for lattice tori flat or curled, in a named presentation with both seams' shifts (r along, s round), the intrinsic object being the pair of wraps up to the grid's symmetries (head; item 4; read-back 8; sketch B).
8. **The fixed-point sentences fail on the odd-row grids.** Confirmed in the script's own output: on every odd grid every straight line reads 0 and the smooth zigzag between columns 0 and 1 (and a/2 and a/2 + 1, now printed) closes after one pass, b faces, and reads 1 (8 × 5: 5 faces; 8 × 7: 7; 8 × 11: 11; 8 × 13: 13; 12 × 5, 16 × 5, 6 × 5, 6 × 7, 10 × 5, 10 × 7 likewise). Applied as written: the sentences are restricted to the reflected closure and the even family, and the odd family is reported where its flip sits (items 2, 3, 5; read-back 6).
9. **The hand-built lip is not the shape of record.** Confirmed from O116 (the product is the tube with its ring seam shifted by two). Applied as written: item 1(c) says the shape is ours and not the shape of record, the check's dislocation remark is recorded as its own and unverified, and the question states plainly where the hint comes from instead of steering (item 1(c); read-back 4; the question). The check's 24-pairing result is recorded as its own, not reproduced.
10. **The guard was keyed to her prediction only.** Confirmed against rule 20. Applied as written: no state is opened until both her confirmation (or change) of the entry, including the completion convention and the two "to confirm" readings, and her prediction are in the notebook (item 6; read-back 11; the question's heading).
11. **Sketches and definitions missing; read-back order.** Applied as written: sketches B (seam shift), C (the lip), D (handle and cross-handle), E (rings of diagonals) added beside A; one-line definitions of Möbius band, annulus, presentation, cross-handle, V − E + F and the mod-2 class added to the terms list; read-back items 3 and 4 swapped so the yes-or-no is defined before anything is called undefined.
12. **Small imprecisions.** (a) Confirmed in the output (the full search finds exactly 3 closing completions; of the same-slot rotations only (0, 1) with (2, 3) closes): reworded to "each of the three axis pairings closes", with the same-slot fact stated. (b) Confirmed (8 tied points, 4 corners with two shortest hexagons under the first option, 6,561 = 3⁸): reworded as the check asks. (c) Confirmed not computed: "not computed". (d) Confirmed from the counting section (the odd family appears only at a a multiple of 8 and b ≥ 5): the size conditions stated. (e) Confirmed from O116 (9,865 + 1 + 2,014 = 11,880): the tube listed separately.
13. **Two lines of the reading note.** Confirmed: the lip line was stale against fact 3, and task 12 of the 22 October handoff is a reading task (priority "Second", Hackett 2007 not read). Applied as written in `docs/reading/notes/2026-10-23_twist_on_a_graph.md` (section 6(e), second bullet; section 6(b), last rule).

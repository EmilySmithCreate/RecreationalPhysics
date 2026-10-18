# The contraction model: a design brief (draft, 18 October 2026)

*Written 18 October 2026 from the author's words of that day (`sandbox/NOTEBOOK.md`, 18 October) and her decision
"Okay let's adjust the model" (VISION Update 63). Under VISION S1 a new move set and a varying count of points are new
ingredients: their form is fixed here before any registered run, every setting run is published, and the model with
them is our family around the published one, never combinatorial quantum gravity. Each item says whose it is. Nothing in
this brief is a result; the exact facts it cites are sandbox looks (rule 16) or record entries, named as such.*

## 0. What is decided and what is ours

**Decided (the author's, 18 October):** the toy is adjusted so that points do not break but compact. Her words: "Points
don't break, they compact, kind of like 2 come together, of the 2 did types of points that can connect with the
relationship, the length of the links in flat space decreases to 0 then those points collapse and the front link is
between the points that connected to the now compacted into themselves now connect to each other." And: "no fixed count,
count increases at the rate of what comes into the black hole." And the picture it serves: "antimatter builds in black
hole until front meets threshold then everything outside of that energy release cancels leaving net matter."

**Ours, pending her confirmation (each marked below):** the exact form of the compaction move as a pair removal with
neighbour splicing and its inverse; that the whole-layer form is the one that reaches the slab; the hard-core check on
every move; keeping the square-count energy unchanged (her "keep using the square counting"); where the stores sit and
what they pay; a per-point cost of zero. Where this brief had to choose, it chose the smallest change to the toy that
holds her sentence, and says so.

## 1. Glossary (plain words first, then the toy's definition)

| Word | In plain words | In the toy |
|---|---|---|
| **point, link** | a degree of freedom and a relationship between two of them | a vertex and an edge; every point has six links (three directions) |
| **the two kinds of point** | her "two types of points that can connect" | the two sides of the bipartite graph; a link always joins one of each; the switch and the compaction both respect this |
| **square** | the smallest closed loop; the toy's unit of flatness | a 4-cycle; flat space has 3 per point and 4 through every link |
| **surplus square** | a loop closed only because a direction is curled tight | a fifth square through a link; the count X; a direction four around gives one per link along it |
| **hard-core rule** | two points may not share too many neighbours | no two points with more than two common neighbours ([T25] Fig. 1b; Q2, Q21) |
| **closed point** (hers: "4") | a point on a direction curled to four around | d(v) = 2: one of its three opposite link pairs closes a square (`local_dimension_d`) |
| **open point** (hers: "6") | a point whose three directions are all at least six around | d(v) = 3 |
| **broken point** | a point that is neither: squares missing where flat space has them | d(v) > 3; every single switch out of the slab makes four of them (notebook, 18 October) |
| **flat space** | the product; any width, any count | an L₁ × L₂ × L₃ torus with every side ≥ 6; H = 0 at every λ and every count (Q18) |
| **the slab, X** | two directions open, one curled: her X (Update 60) | the 4 × L × L torus; 4(λ − 1) per point above flat; stuck for 1 < λ < 2 against single switches (O41) |
| **curling cost** | what a tight curl costs in energy | 4(λ − 1) per surplus square (Update 23; glossary) |
| **curling energy** | energy that may only curl (Update 57) | in this model: energy in stores that pays a contraction; its stored form is the slab's curling cost |
| **compaction, pair removal** (hers) | two linked points of opposite kind collapse into nothing and their other neighbours join across the gap | remove a linked pair u (side 0), v (side 1); splice u's five other neighbours to v's five, one to one; N falls by 2, links by 6 |
| **splitting, pair insertion** | the reverse: a new pair of points opens between five links | cut five links a_i–b_i, add u linked to the five b_i, v to the five a_i, and u to v; N rises by 2 |
| **layer contraction / layer splitting** | a whole sheet of pairs compacts at once, taking a direction from six around to four | remove the layers x = 0 and x = 1 and splice x = −1 to x = 2 at every transverse position; its inverse inserts a pair at every position |
| **rim, seam** | the border between a compacted patch and the rest | the points in the two layers that lose a link into the patch and must be re-linked across it |
| **store** | where a point keeps energy it has not spent | one number per point (`sealed_d`); the stores and H together are conserved exactly |
| **feed** | what comes into the black hole | energy added to the stores at a declared rate and place (T67, T68) |
| **leak** | what is returned to the black hole | energy removed from the stores at a declared rate (Update 9's semi-permeable wall) |
| **no-break rule** | space cannot break, only curl (hers) | a store pays no move that leaves a point broken (Update 62); under the compaction move set this is a rule about which splicings are allowed |
| **pooled payment** | a move is paid by the points it touches | the cost is drawn from the stores of the points whose links moved, in proportion to what they hold; a release is credited to them evenly (Update 62) |
| **front, patch, completion** | the moving edge of the change, the region it has converted, the moment the last point converts | a connected set of converted points; completion is the whole layer |
| **the ledger** | what was paid, what came back, what is left | paid to walls and seams; refunded at completion; net = the stored curling cost |
| **per point** | the unit of every energy here | with a varying count this must say which points: per surviving point of the slab, or per point of the flat product (a flat product has 3/2 the slab's points) |

## 2. The mathematics

**2.1 The energy (unchanged; the author's "keep using the square counting").** At six links,

  H = 16(3N − S) + 4λX = 4 Σ_e [(4 − S_e) + λ(S_e − 4)₊],

with S_e the squares through link e (flat 4, at most 5; Q21). The second form is exact (Σ_e S_e = 4S; 3N links) and is
the one to read with a varying count: every link in flat space contributes 0; a link along a direction four around
carries S_e = 5, so it contributes 4[(4 − 5) + λ] = 4(λ − 1); the slab has one such link per point (each point has two
ends on the curled direction and each link two ends), so it sits 4(λ − 1) per point above flat. Flat space of **any** count sits at zero, so the energy itself puts no price
on a point. *Exact (O41; `test_sheet_tube_cube_ladder` and its six-link counterpart).*

**2.2 A cost per point (ours, a decision for her; default zero).** With the count varying, a term μ_N · N is the natural
knob (claim 3's parked "cost-per-element term", the cosmological constant of dynamical triangulations). This brief sets
μ_N = 0: adding or removing a pair in flat space changes H by nothing, and the count is set by the moves and the stores
alone. Any other value is a new knob and needs her dated decision.

**2.3 The compaction move, exactly (ours, from her words).** Let u (side 0) and v (side 1) be linked. Let A be u's five
other neighbours (all side 1) and B be v's five other neighbours (all side 0). Choose a one-to-one map σ: A → B. Remove u
and v and every link at them (eleven links), and add the five links a–σ(a). Every surviving point keeps six links, the
two sides stay separate, and N falls by 2. The move is allowed only if no link is duplicated and the hard-core rule still
holds. Its inverse, the **splitting**, chooses five links a_i–b_i (a_i side 1, b_i side 0), cuts them, and adds u linked
to the five a_i, v to the five b_i, and u to v. Every pair removal is undone by exactly one pair insertion, so the move
set is reversible. *What is free in this definition:* σ. There are 120 of them; from flat 6 × 6 × 6 five are valid, from
the slab 4 × 6 × 6 none (`sandbox/pair_moves.py`, LOG 18 October).

**2.4 The layer move, exactly.** On an L₁ × L₂ × L₃ torus, remove the layers x = 0 and x = 1 and, at every transverse
position p, link (−1, p) to (2, p). The result is the (L₁ − 2) × L₂ × L₃ torus, with no point broken and no seam. *Exact
(`sandbox/pair_moves.py`): 6 × 6 × 6 → 4 × 6 × 6 and 6 × 6 × 8 → 4 × 6 × 8 reproduce the built slabs in N, S, X, H, the
d census and validity.* Its energy:

- from L₁ ≥ 8 to L₁ − 2 ≥ 6: ΔH = 0 (flat to flat);
- from 6 to 4: ΔH = +4(λ − 1) · N_slab, with N_slab = 4 L₂ L₃.

So in her ladder "100 → 8 → 6 → 4", every compaction above six is free in H and the last one costs the whole curling
cost. Read forward, that is the black hole storing 4(λ − 1) per surviving point in the final step; read backward, the
splitting of the slab's one curled layer releases exactly that, with no climb and no refund: **gross = net**. *Exact
arithmetic on 2.1 and 2.4.* One more exact fact, reported and not claimed: the step 6 → 4 keeps the count of 3-cubes
(216 in both 6 × 6 × 6 and 4 × 6 × 6) while the steps above it do not (`sandbox/cube_price.py`, LOG).

**2.5 What a part of a layer costs (the seam).** Contract only a patch P of transverse positions (the pairs (0, p),
(1, p) for p ∈ P, with (−1, p) spliced to (2, p)); the rim points in layers 0 and 1 each lose a link into P and must be
re-linked across it, within their own side. *Exact within what was tried (`sandbox/partial_contraction.py`, 18 October;
λ = 1.25, flat 6 × 6 × 6; every side-respecting re-linking of the rim tried for the blocks, canonical ones for the
strips):*

| patch | positions | valid re-linkings | fewest broken points | ΔH from flat | ΔS | ΔX |
|---|---|---|---|---|---|---|
| 1 × 1 | 1 | 1 of 24 | 26 | 191 | −17 | 3 |
| 1 × 2 | 2 | 0 of 36 | none valid | | | |
| 2 × 2 | 4 | 16 of 576 | 48 | 284 | −38 | 12 |
| 2 × 3 | 6 | 16 of 14,400 | 56 | 426 | −57 | 18 |
| strip, 1 row | 6 | canonical | 60 | 378 | −54 | 18 |
| strip, 2 rows | 12 | canonical | 48 | 372 | −84 | 36 |
| strip, 3 rows | 18 | canonical | 48 | 396 | −114 | 60 |
| strip, 4 rows | 24 | canonical | 48 | 384 | −138 | 96 |
| whole layer | 36 | 1 | **0** | **144** | −180 | 144 |

At L = 8 the blocks cost exactly the same (26, 48 and 56 broken points; 191, 284 and 426 units), so the seam's cost is
local and does not depend on the size of the space; the strips, whose rim is two rows of L, scale with L (`partial_contraction_L8_2026-10-18.txt`).
Every partial contraction within reach leaves 26 to 80 points broken and sits **higher than the finished slab** (191
to 432 against 144 at L = 6 and 256 at L = 8), so the slab, read backward, is separated from flat space by a seam of about 230 to 280 units on
these paths, the same size as the switch path's completed patch (T54: about 225 at λ = 1.25, O118). At another λ the
same states sit at ΔH(λ) = ΔH(1.25) + 4(λ − 1.25) ΔX. Not tried: re-linkings that do not keep (−1, p)–(2, p), patches
of three or more switches of the rim at once, and sizes above L = 8. **What this says for her picture:** with the
compaction done pair by pair, points do break at the seam; the only clean compaction found is the whole layer at once.
So the model has two forms, and the choice between them is hers (section 5): a **local** form, in which the rim's
broken points are allowed and priced by the energy as it stands (a seam that the front must carry), or a **layer**
form, in which the move is the whole layer and there is no front at all, the slab splitting in one step.

**2.6 The ledger, in each form.** Layer form: paid 4(λ − 1) per slab point to compact, refunded the same to split;
nothing cancels; the hot lump and the stored curling cost are one number. Local form, from the table: compacting a
patch costs its seam (about 190 to 430 for a few positions, rising with the rim and falling to 144 only at the whole
layer), so a front advancing through the slab pays a seam that is repaid when the rim closes: paid along the front,
refunded at completion, net the curling cost, which is her sentence of 18 October ("everything outside of that energy
release cancels leaving net matter") as arithmetic. The ratio net over gross is then set by the seam's size at the
moment of completion, which the toy fixes by itself only if the rim's cost is a function of the patch and not of a
protocol setting; whether it is, is test E3. Rule 13 stands over any number that comes out of it.

**2.7 The stores and the clock.** Stores sit on points (one per point, as in T67 and T68); a removed pair's stores are
pooled into the stores of the five spliced pairs; an inserted pair's stores start empty. A move's cost is paid from the
pooled stores of the points whose links moved (Update 62); a release is credited to them evenly. The feed adds to the
stores at a declared rate and place; the leak removes at a declared rate. No temperature. A sweep is 3N proposals,
restated on the fair clock if sizes are compared (Update 41).

**2.8 Detailed balance (owed before any chain runs; code convention).** A chain over a varying count needs the
proposal of a removal at a pair and of an insertion at a cut set to be balanced: with R(G) removable pairs and I(G)
insertable cut sets, a symmetric proposal is not automatic. The module docstring must carry the argument (or the chain
must be declared a driven, non-equilibrium protocol, as the sealed feed runs are, in which case what it conserves and
what it does not is stated instead). Ergodicity: the switch connects graphs of one count (Q9 at four links, unproven at
six beyond what the exact listings reach); the pair moves connect counts; whether together they reach every valid
graph at every count is not shown and is to be checked by exhaustive listing at the smallest sizes before any result is
interpreted (rule 6).

## 3. How it differs from the published model and from the curling-energy version

| | Trugenberger's model ([T25], [KTB19]; λ = 1) | The curling-energy version (Updates 23, 57, 58, 60, 62) | The contraction model (this brief) |
|---|---|---|---|
| Energy | curvature: H = 16(DN − S) + 4X | curvature plus a curling cost: the same with λ > 1 | the same, λ > 1, and a per-point cost μ_N = 0 (decision pending) |
| Count of points | fixed | fixed | **varies**: pair removal and insertion; layer contraction and splitting |
| Moves | one switch of two links | one switch; since Update 62, two switches at once with no point left broken | **compaction and splitting**, plus the switch; two forms (local or whole layer) |
| What X is | nothing of the kind; the hot phase is a random graph | the slab 4 × L × L, likely with relics (Update 60) | the slab, reached from flat space by one layer contraction |
| The black hole's inside | a large bubble reverted to the random phase ([T25]) | the parent's geometry re-curled (Update 59); nothing has folded in any run (T21 to T57) | the parent's layers compacted, free above six around and 4(λ − 1) per point for the last step (exact) |
| What breaking is | the normal state of the hot phase | a point at d > 3; priced only by the lost squares; forbidden to the store (Update 62) | the same; in the layer form it never occurs; in the local form it occurs at the seam and is priced by the energy |
| How X opens | not a question the model asks | one clean two-switch move at a time, a climb of 4 per point opened, release at completion (sandbox, 18 October) | the slab splits a layer: whole at once (no climb) or patch by patch (a seam of 190 to 430 units, repaid at completion) |
| Where the released energy goes | a fixed coupling: an unlimited reservoir | stores, feed and leak | the same |
| What matter is | the leftover random phase | the energy of the lump (her lean, 10 October), the scrap as dark matter's best guess (Update 52) | the net of the ledger; the seam's payment and refund as the pair that cancels (her words, 18 October; an interpretation, ours and hers, unverified) |
| Status of the ingredients | published | ours; every untied verdict stands (T30 to T69) | ours; nothing registered has run |
| Validation | Gates A and B (B open); exact at N ≤ 18 | the same kernel; rule-6 tests on each addition | **owed**: rule-6 tests, detailed balance, exhaustive listing at small sizes |

What is kept from every earlier version: the curling cost 4(λ − 1), the square count, the slab as X, the stores and the
conservation of H + stores − fed + leaked, the untied rule (Update 58), and every verdict scored.

## 4. What is exact already, from this session's looks (sandbox; not evidence for any claim)

1. Every single switch out of the slab leaves four points broken; flat six-link space has no clean move within two
   switches; the slab has one, the 64-unit first opening (`sandbox/clean_moves_census.py`).
2. The clean switch path climbs 4 per point opened with no surplus shed until completion (dX = 0), so no λ makes it
   self-paying; paid 4N, refunded 4λN, net 4(λ − 1)N (`sandbox/clean_feed.py`; notebook).
3. The whole-layer contraction is exactly the slab (`sandbox/pair_moves.py`).
4. One pair removed from flat space: 5 of 120 splicings valid, every one leaving broken points; from the slab none
   valid (`sandbox/pair_moves.py`).
5. Every partial contraction within reach leaves 26 to 60 broken points and sits above the finished slab
   (`sandbox/partial_contraction.py`; the table in 2.5).

## 5. Open for the author (the brief cannot be finished without 1 and 2)

1. **Which form:** local (pairs compact one at a time; the seam's broken points are allowed and priced) or layer (the
   whole layer at once; no seam, no front, no cancellation in the ledger). Her picture of 18 October has a front and a
   cancellation, which is the local form; her "points don't break" is the layer form. The exact table says they cannot
   both hold with the compaction move as defined.
2. **The no-break rule under the local form:** forbid every move that leaves a point broken (then the slab is frozen,
   since no local pair move is clean), or let the store pay for a seam up to a stated size, or price broken points by
   the energy alone (which is the toy as it stands).
3. **The per-point cost** μ_N (ours: zero).
4. **Which splicings** σ are allowed: any valid one (120 tried), or only the layer-like one (−1, p)–(2, p) with the rim
   re-linked within its row.
5. **Where the count grows:** does the feed insert pairs into flat space (free in H, a rule for where), or does the
   count change only by compaction and splitting?
6. **The names.** "Antimatter" for the seam's payment and "matter" for the net are hers; the toy has nothing that comes
   in opposite kinds, and the brief records them as an interpretation.

## 6. Tests, in order (each exact one is cheap; nothing registered runs before her answers to 1 and 2)

**Exact, no run (sandbox, rule 16; this week):**

- **E1. The seam census, extended.** Section 2.5 at L = 8 (done: the blocks cost the same), at λ = 1.10 and 1.40 (arithmetic from ΔX), with
  re-linkings that do not keep (−1, p)–(2, p), and patches up to 3 × 3. Question: does any patch smaller than a layer
  compact with no point broken? If none does, the layer form is the only clean one and the local form always carries a
  seam. *Decides question 1's arithmetic.*
- **E2. The ledger against size and λ.** Layer contraction 8 → 6 → 4 at L = 6, 8, 10: ΔH = 0 then 4(λ − 1) N_slab; the
  cube count; the stores' balance under pooled payment. *A test of the kernel once it exists; the arithmetic is in 2.4.*
- **E3. Does the seam's cost depend only on the patch?** For the local form: the lowest-energy re-linking for each patch
  shape at two sizes; if the rim cost is a function of the rim alone (local), the net-over-gross ratio at completion is
  the toy's own number; if it depends on L it is a size effect to be held out (rule 14).
- **E4. Reach.** Exhaustive listing at the smallest six-link sizes that admit valid graphs: do the switch and the pair
  moves together reach every valid graph of every count? (The counterpart of Q9.) Owed before any chain result is
  interpreted (rule 6).

**Kernel (rule 6), after her answers to 1 and 2:** `src/graphity/contraction.py`: pair removal and insertion, layer
contraction and splitting, the no-break check, pooled stores; tests: ΔH against the full Hamiltonian, the clean
guarantee where claimed, conservation of H + stores − fed + leaked, same-seed reproducibility, networkx brute force on
the splicings, detailed balance stated in the docstring.

**Sandbox looks, after the kernel:**

- **S1. The black hole run forward.** Flat 8 × L × L, stores fed curling energy at every point, compaction moves only:
  does it compact 8 → 6 → 4, and does the energy stored at the end equal 4(λ − 1) N_slab? (Layer form: one move, trivially
  yes; local form: does a seam ever close?)
- **S2. The slab fed at every point under the local form.** Does a splitting front form and complete, and what does
  the ledger read at completion (paid, refunded, net)? Against the switch-path look of 18 October (`clean_feed.py`).
- **S3. The leak.** S2 with a leak on every store: does the front still complete when the interior drains, and what
  share of the fed energy ends as the net?

**Registered (after S1 and S2, with her prediction and a held-out size; rule 14):**

- **T70 as planned** stays the switch-path test under Update 62's knobs (the climb at L = 12, 16; completion and the
  release 4(λ − 1) per point). It tests the fixed-count form of her picture.
- **T71 (to be written): the slab splits under the contraction model.** The slab fed at every point under the form she
  chooses, λ = 1.10, 1.25, 1.40, L = 8 and 12, L = 16 held out; words per replica from the first splitting, a region
  past half, completion; the ledger at completion; the count at the end. Her prediction before launch, ours beside it.
  What would kill the model's claim: no replica completes at any λ and size, or completion releases something other than
  4(λ − 1) per slab point.

## 7. What this cannot show

Anything about antimatter, the baryon asymmetry, or the inside of a real black hole. The toy has no particles and no
opposite kinds; "antimatter" and "matter" are names for two entries in a ledger of squares. A varying count of points
is claim 3's parked decision reopened for this model only; what a point is at the base level is not touched. A number
that comes close to an observed one is not a result until rule 13's checks are done.

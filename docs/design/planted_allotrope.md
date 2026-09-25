# A planted allotrope: a finite version of the model author's dark-matter picture

*Design note, 2026-09-25, written after T36 (ASSUMPTIONS O59). Everything below is either quoted from the papers or
exact counts on fixed graphs made by `scripts/build_planted_allotrope.py`
(tests: `tests/test_planted_allotrope.py`). Nothing has been simulated. The test in section 6 is **proposed, not
pre-registered and not run**. All reasoning not quoted is ours and unreviewed by a physicist.*

## The answer first

- **His allotrope can be built as a finite graph, but not on a flat torus.** Fig. 9 of [T25] shows a background in
  which every point touches three squares and one hexagon, and one hexagon whose six corners touch only two squares.
  A graph drawn on a torus can only have square faces, so no torus can hold that background (section 2). A closed
  surface with more holes can. We built one exactly: 240 points, every one touching three squares, arranged exactly
  as in his Fig. 7.
- **We planted his allotrope in it, fused three at a time.** Cutting out one hexagon and joining its opposite corners
  (the "fold") gives 18 points that each touch two squares with Fig. 9's arrangement, and 216 untouched points. A
  single allotrope on its own is allowed by counting only when N leaves remainder 18 on division by 24, and we have not
  found a way to build it (section 3).
- **At λ = 1, his model, the energy alone does not hold the planted allotrope.** No single switch out of it is
  downhill, but one switch that costs nothing opens a downhill one, and at zero temperature the 18 low points are all
  gone after 8 switches. The background itself is held the same thin way. So if the allotrope lasts, entropy has to
  hold it. That matches his wording, a barrier in *free energy*, and only a run at finite coupling can measure it
  (section 6).
- **The same surgery on T36's flat 14 × 14 torus** gives the allotrope one rung up: 24 points of *exactly his
  three-square background type* inside four-square space. It shrinks at zero temperature too, but only to 8 points,
  and then stops.

## 1. What the allotrope is, in his words

Two papers, read from the arXiv HTML on 2026-09-25 (text searched, figures opened). [T24] is arXiv:2409.09385 v1;
[T25] is arXiv:2512.17676 v2. Fig. 9 of [T25] and Fig. 1 of [T24] are the same image file, drawn by Eryk Kopczyński.

**The background: a tiling with a fixed number of squares at every point.** [T25] Sec. IV.2:

> "Each edge of the map supports exactly two regular polygons, each vertex supports exactly four polygons. Let
> k_i, i = 1…4, be the number of edges of the 4 polygons surrounding a vertex and let us call the vector
> k = (k_1, k_2, k_3, k_4) the vertex type."

> "At each coupling, one of the four possible vertex types of the semi-regular tessellation, with one, two, three or
> four squares will characterize the minimum of the free energy, the remaining larger cycles determined by the
> detailed balance between the combinatorial energy and entropy."

> "In Figure 7. we show one example of such a tessellation with three squares and one hexagon per vertex,
> corresponding to a constant negative-curvature surface at a small but non-zero value of the coupling g."

**The allotrope.** [T25] Sec. VI.3:

> "As always when lowering the coupling in continuous phase transitions, there typically survive domains of higher
> free energy. These are metastable states, which, depending on their free energy difference to the minimum and the
> barrier in between, may be extremely long-lived. These states are called allotropes and the most famous example are
> the two states of carbon, graphite, the free energy minimum and diamond the higher free energy allotrope"

> "In the present case, we can have metastable domains characterized by a higher number □_dom than the prevailing
> configuration □ and therefore having a larger free energy than the space around them at a given g. Because of this
> higher free energy they have also a higher curvature (in the Lorentzian picture) and interact gravitationally. But
> they are neither empty space nor ordinary matter. These domains are natural candidates to represent dark matter in
> the universe."

[T25] Fig. 9, caption:

> "An allotropy region (blue) with vertices surrounded by two squares within an hyperbolic tessellation with all
> vertices surrounded by three squares. The hyperbolic tessellation represents space of a given uniform curvature; the
> blue allotropy region represents a region of dark matter, with a higher absolute curvature and free energy. For
> simplicity of presentation we are showing here only the smallest example of such a region."

[T24] Sec. V says the same, with the direction written as an inequality:

> "Such domains, characterized by 0 < s_i < s̄ are neither baryonic matter nor space but, rather, represent natural
> candidates for dark matter."

> "If, at this new value, the free-energy difference between the actual minimum and the previous minimum at higher
> couplings is sufficently small, very long-lived metastable domains of a different tiling can survive, exactly as in
> crystal allotropy …, the paramount example being unstable diamond in an environment which favours graphite as the
> stable configuration of carbon."

> "In this model, dark matter arises thus essentially as 'crystallographic' defects in the fabric of space-time."

**The direction does not agree across the texts.** [T25] Sec. VI.3's text says the domain has a *higher* number of
squares than its surroundings. Its own Fig. 9, and [T24] Sec. V (0 < s_i < s̄), give it *fewer*. So does the
curvature statement: fewer squares means more curvature ([T25] Sec. IV.2). We follow the figure and [T24]. This is a
question to put to him, not a correction.

**Why it lasts, and for how long.** His stated reason is a barrier in free energy ("the barrier in between"). No
barrier is computed. The lifetime is given only as "may be extremely long-lived" and "very long-lived". [T24] has no
simulations. His own open question is how long an allotrope lasts.

**What Fig. 9 shows, read from the picture** (ours; the figure has no list of links, so this is read from the drawing).
Red faces are squares and green faces are hexagons. Every point outside the blue region touches three squares and one
hexagon, as in Fig. 7. The blue region is one hexagonal face. Each of its six corners (circled) touches two squares and
two hexagons (the blue one and a green one), alternating square, hexagon, square, hexagon. So each link at a circled
point carries exactly one square. Every other point keeps three squares. Its links carry 1, 1, 2 and 2 squares.

## 2. Why not on T36's torus

*Exact, ours.* Draw a graph with four links per point on a torus, with every face a disk. Euler's formula for the
torus (points − links + faces = 0), with links = 2 × points, gives faces = points. The face sizes add up to twice the
links, 4 × points, so the average face has 4 sides. In a bipartite graph every face has an even number of sides, at
least 4. So **every face is a square**, and every point touches at least four squares. A point touching three squares
and a hexagon has more than 360° of corners around it (negative curvature). A patch of such points needs a surface
with more holes than a torus. This is why T36 could not test Fig. 9 directly. Its equilibrium graphs at about three
squares per point cannot be drawn on a torus without crossings: in effect, switches have added handles.

## 3. What was built

### The background: his Fig. 7, closed up

*Ours.* The tiling of Fig. 7 can be generated by two moves. Move **a** walks once around a hexagon (six steps bring
you back). Move **b** walks once around a square that touches hexagons only at its corners (four steps bring you
back). One rule ties them together: doing b backwards and then a, twice, brings you back. That rule makes the squares
along the hexagon edges. Take any two permutations with exactly these properties. Their **Cayley graph**
(points = the permutations the two moves reach; links = one move) is a finite graph in which every point has exactly
Fig. 7's surroundings, unless extra short loops appear. That is checked, not assumed.

The permutations were found by a short random search among permutations of 10 or 11 objects, and are now fixed in the
script. Both are odd, so every link joins an even permutation to an odd one, and the graph is bipartite. Sizes found:
48, 72, 120, 192, 216, 240, 384, 480, 720, 864, 1152, 1296 (always a multiple of 24). **We use N = 240** (with 720 as a
size check). Out to 5 steps from any point it looks like the larger graphs (720 to 1152 points), and so presumably
like the infinite tiling: 1, 5, 14, 31, 61 and 113 points within 0 to 5 steps. It lies on a closed orientable surface
with 11 handles (Euler characteristic −N/12 = −20).

### The allotrope: a corner square that became a hexagon

*Ours.* Read Fig. 7 as a map. The hexagons are its faces, and each square that touches hexagons only at corners is a
map vertex of degree 4, cut off. Then **Fig. 9's blue hexagon is a map vertex of degree 6**: a vertex surrounded by
six hexagons instead of four, cut off into a hexagon instead of a square. Its six corners are the points that touch
two squares. Two surgeries make degree-6 vertices while leaving every other point exactly as it was.

- **Fold (cross-cap), the primary object.** Delete one hexagon (6 points). Join the freed links at each corner to
  those at the opposite corner. Three map vertices become degree 6. That gives **18 points touching two squares, three
  Fig. 9 allotropes fused in a triangle**. N = 234. The surface loses its orientation, which the energy cannot see.
- **Handle.** Delete two hexagons as far apart as the graph allows (7 steps), and join the 24 freed links across.
  Six map vertices become degree 6. That gives **36 points touching two squares, six Fig. 9 allotropes fused in a ring
  around a new handle**. N = 228.
- **The flat analog.** The same handle surgery on the 14 × 14 torus, gluing two lattice squares at (0,0) and (6,6).
  It gives **24 points touching three squares, with exactly his background's links (1, 1, 2, 2)**, among 164 points
  touching four. N = 188. This is his allotrope idea one rung up: a patch of the three-square tiling inside flat,
  four-square space.

**Why not one allotrope alone** (*exact, ours*; the sign of a permutation). Take an orientable map whose faces are all
hexagons and whose vertices have degree 4 or 6, and cut its corners off. The number k of degree-6 vertices must
satisfy **k ≡ −N/6 (mod 4)**. The reason: going around a face equals crossing a link after going around a vertex.
Faces give N/6 six-cycles, links give N/2 swaps, and vertices give m four-cycles and k six-cycles, with 4m + 6k = N.
The signs must match, which is the same as the surface having an even Euler characteristic, −(N/6 + k)/2. The
background (k = 0) needs N ≡ 0 (mod 24). A single allotrope needs N ≡ 18 (mod 24). The handle (N = 228, k = 6) obeys
the rule. The fold breaks it, as it must, because it is non-orientable. **A lone smallest allotrope is allowed at
N = 18 (mod 24), and we have not found a way to build one.**

## 4. The exact numbers (λ = 1)

H = 16(N − S) + 4X, with S the squares and X the surplus squares on links carrying more than two (ASSUMPTIONS Q1). The
"line" is the H a graph would have if every point touched the background's number of squares. The walls cover every
switch with its first side-0 point within 1 step of the region, and a partner within 4 steps. That covers every
switch that gains a square or costs less than 32. At N = 720 the walls near each object are identical.

| object | N | points at 2 / 3 / 4 squares | H | above the line | symmetries | cheapest switch | downhill switches | after one zero-cost switch |
|---|---|---|---|---|---|---|---|---|
| background (Fig. 7) | 240 | 0 / 240 / 0 | 960 | 0 | 240 | 0 (8 per point) | 0 | a −16 switch opens |
| **fold** | 234 | 18 / 216 / 0 | 1008 | +72 | 6 | 0 (270 near it) | 0 | a −16 switch opens |
| handle | 228 | 36 / 192 / 0 | 1056 | +144 | 4 | **−12** (4) | 4 | — |
| flat torus 14 × 14 | 196 | 0 / 0 / 196 | 0 | 0 | 784 | +32 (24 per point) | 0 | — |
| flat handle | 188 | 0 / 24 / 164 | 96 | +96 | 2 | 0 (8) | 0 | a −16 switch opens |

- Every planted point in the fold and the handle has one square on each of its four links, Fig. 9's pattern. Every
  background point has 1, 1, 2 and 2. No link anywhere carries more than two squares (X = 0).
- Each allotrope point costs exactly 4: one square fewer per corner, a quarter of 16.
- The handle's exits depend on which two hexagons are glued. Of the two placements at the largest distance, one gives
  −12 (4 switches) and the other −16 (36 switches). Both are downhill.
- The flat torus's +32 is the wall already on the record (O22, O51). It is a check on the switch counter.
- Half of the background's 8 zero-cost switches create a pair of two-square points next to a pair of four-square points.
  That is where its downhill switches come from.

**Zero-temperature paths** (`--descend 12`; one path each, not all of them):

- **Fold:** 1 zero-cost switch, then 7 downhill. All 18 two-square points are gone at H = 888 (−120), below the line,
  with 14 points now touching four squares. The path keeps going downhill (a scratch run reached 548 after 60 switches,
  flattening the background).
- **Handle:** 12 downhill switches in a row, from 36 to 13 two-square points (H −196). It is still going.
- **Flat handle:** 1 zero-cost switch, then 3 downhill, leaving 8 points at three squares (H = 48). Then no downhill
  switch exists, even one zero-cost switch away, so a smaller residue stays.

## 5. How faithful is it

**Faithful:** the neighborhood of every planted point and every background point, link by link. His model at λ = 1
with no cap (the naming condition: this is CQG). Named points, as in his simulations.

**Different from Fig. 9:**
1. The region is **three fused smallest allotropes** (fold) or six (handle), not one. A lone one needs N ≡ 18 (mod 24)
   and a construction we do not have.
2. **The surface is closed and has holes**, and the allotrope sits exactly where the topology changes (a cross-cap or a
   handle). Fig. 9's lies in a plane with nothing special under it. The energy counts only squares and cannot see this,
   but the switches can: a throat puts both sides within a few steps of each other.
3. **The background is one perfect tiling, with no entropy.** His background is the free-energy minimum, "the
   remaining larger cycles determined by the detailed balance between the combinatorial energy and entropy". At no
   coupling is the perfect tiling what equilibrium looks like at our sizes. O59 found the equilibrium at about three
   squares per point to be a disordered mixture. So the test measures an allotrope in an ordered background that is
   itself relaxing, and it must measure the background's own life too.
4. **The flat analog** matches the idea (a domain with fewer squares per point than its surroundings, with the next
   tiling's exact local structure) but not Fig. 9's numbers: 3 inside 4, not 2 inside 3.

## 6. Proposed test: how long does a planted allotrope last at λ = 1?

*Proposed, not pre-registered and not run. Before any run: ASSUMPTIONS needs entries for the Cayley background and the
reading of Fig. 9 (both "Ours"). The owner's prediction must be written down.*

**Why.** It is the model's author's open question (how long an allotrope lasts), and it is the next run O59 names.
Section 4 says the energy gives no protection. So the question becomes whether entropy does, at couplings where his
picture puts three squares per point.

**Objects.** Built by the script, and the run starts from them exactly, with no warm-up: the fold (234, the scored
object), the handle (228), the Fig. 7 background (240, control), the flat handle (188) and the flat 14 × 14 torus (196,
control).

**Chain.** `graphity.cqg.run_chain`, λ = 1, `NO_CAP`, Metropolis, the random stream carried on (as T36). Couplings
g ∈ {1.0, 1.5, 2.0, 2.5, 3.0, 3.433, 3.697}. The last two are T36's, where the 14 × 14 torus touches about three
squares per point at equilibrium; the colder ones are where an ordered tiling should keep its order longest. 16
replicas per cell. 20,000 sweeps, with a snapshot every 10 sweeps for the first 2,000 and every 100 after. Named points.

**Measured at each snapshot.** The planted set R keeps its labels from the start. Record every point's square count
c(v), and:
- f_R: the share of R touching at most (background − 1) squares;
- f_B: the same share among the far points, those at least 3 steps from R in the starting graph (the chance level);
- q_R: the share of R with Fig. 9's links, (1,1,1,1) (for the flat handle, (1,1,2,2));
- q_B: the share of far points with the background's links, (1,1,2,2) (flat: (2,2,2,2));
- H.

**Survival, fixed now.**
- The region is **alive** while e = f_R − f_B ≥ 1/2. Its lifetime τ_R is the first snapshot after which e stays below
  1/2 for two snapshots in a row. A replica that never drops is censored at 20,000 sweeps.
- The background's order lifetime τ_B is defined the same way on q_B < 1/2.
- Per cell (object, g), the medians over the replicas:
  - **LASTS** if median τ_R ≥ 1,000 sweeps, ten times the memory T36 measured for low points at equilibrium (about
    100 sweeps, O59);
  - **DISSOLVES** otherwise;
  - tagged **FIRST** if median τ_R < median τ_B / 2, and **WITH ITS BACKGROUND** if not.
- **Verdict**, read on the fold at any coupling (the owner's bar, VISION Update 26: it has to happen at one setting):
  **ALLOTROPE LASTS** if the fold LASTS at some g; **DISSOLVES** if at none. Handle and flat reported beside, not
  scored.
- Reported beside: the median τ_R against g (the lifetime curve he asked about); T36's persistence excess for R at lags
  of 50, 200 and 2,000 sweeps, comparable with O59; q_R; and the energy against time.

**Predictions.**
- *Ours, unverified:* **DISSOLVES** at every coupling. At g ≥ 3.4, the whole tiling loses its order within a few
  hundred sweeps, and the region goes WITH ITS BACKGROUND. At g ≤ 2.5, the region's way out is one zero-cost switch
  and then a downhill one. At N ≈ 234 a given switch is proposed about 4 × 10⁻³ times a sweep. The fold has 270
  zero-cost switches near it, and a downhill one needs only a few specific follow-ups. We expect τ_R of order 10² to
  10³ sweeps. That is close enough to the bar that this is the less certain half. And the region should go FIRST,
  because it carries the extra energy.
- *The owner's:* not yet stated. Inferred from T36 (where her inferred prediction was ALLOTROPES) and Update 26: LASTS
  at some coupling. **To be confirmed or replaced by her before any run.**

**Named or interchangeable points.** Named, the published setting. The exact symmetry counts (side-preserving, igraph)
are: background 240, fold 6, handle 4, flat handle 2, flat torus 784. With interchangeable points, leaving the perfect
background would cost up to a factor of 240 in weight (g ln 240 ≈ 19 at g = 3.43). Leaving the fold would cost up to a
factor of 6 (≈ 6). So the background would grow stickier than the region, and the region's lifetime relative to its
background should shorten. This was not computed beyond these counts.

**What it cannot show.** Anything about the infinite hyperbolic plane. Whether a lone smallest allotrope behaves like
three fused ones. Whether the cross-cap or handle under the region changes its life. Lifetimes at other sizes (the
720-point versions are built for that follow-up).

## 7. Rebuilding

```bash
python scripts/build_planted_allotrope.py                # section 4's table, about 15 s
python scripts/build_planted_allotrope.py --neutral      # plus the last column, about 30 s
python scripts/build_planted_allotrope.py --descend 12   # plus the zero-temperature paths, about 2 min
python scripts/build_planted_allotrope.py --size 720 --flat 26
python scripts/build_planted_allotrope.py --save DIR     # the graphs, as DIR/<name>.npz (adj, part)
pytest tests/test_planted_allotrope.py                   # squares checked against networkx; about 30 s
```

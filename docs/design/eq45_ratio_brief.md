# The free-energy ratio test of Eq. (45) on the toy (design brief, 23 October 2026)

*A design brief for the owner. Nothing here is run on the toy's saved states, and nothing is registered: the test is
designed so that she can give her prediction first (handoff of 23 October, item 2.3). Kinds of statement are marked:
**published** (quoted from [T25], arXiv:2512.17676v2, the HTML text searched on 23 October 2026 and quoted with its
section; the sections named were read in full for this brief, the rest of the review was not), **exact** (arithmetic,
or an argument that holds for every graph of the kind named), **measured** (a registered run with its verdict),
**sandbox** (a look under rule 16: it can kill, not crown; this includes every count on a built graph made by
`sandbox/eq45_geometrize_check.py`, run on 23 October, until the tests of `graphity.geometrize` pin it, rule 16 (c)),
**ours** (interpretation, unverified), **hers**. Terms: "the toy" is our family at any λ; "the published model" is
Trugenberger's at λ = 1; the tube is the 4 × L lattice torus.*

*Revised 23 October, the same day, after an adversarial check by a fresh read-only session. The built-graph counts
were called exact and are now sandbox; the background of item 8 was nearly empty and made our sign prediction nearly
true by definition, and is replaced; F's zero and its orientation offset are listed as open, and the intercept and the ratio
F₁/F₂ are no longer scored; the integrated (Gauss–Bonnet) reading is added, and the scored region and the sum are
stated; the circularity control is made quantitative; the verdict words are rebuilt; Sec. 1's reading of the two signs
is corrected. Each change is made in place; the list is Sec. 12.*

---

> ## Current definitions (PROPOSED 23 October, revised the same day; not yet read back to the owner)
>
> Read this box first. Every item is marked **from the text** (with the quotation and its section) or **ours** (a choice the
> text leaves open). Under rule 20 a definition here changes only after the exact test named for it has run, or by her
> withdrawal. Nothing in this box has been applied to a saved state of the toy.
>
> **The reading being defined.** The curvature of an object in a warm graph of the published model, by the
> geometrization of [T25] Sec. IV.2: each graph cycle that is a face of the surface becomes a regular polygon of side ℓ,
> each point sits at four polygons, and the curvature at a point is set by the angle those four polygons need to close
> up to 2π.
>
> 1. **Faces (from the text, as far as it goes; the rule for an arbitrary graph is ours).** The text: "In the geometric
>    phase, graphs become the 1-skeleton of a 2-cell embedding, for which the graph cycles are homeomorphic to open disks
>    on a surface. The 2-cell embedding is called a 'map'. [...] Each edge of the map supports exactly two regular
>    polygons, each vertex supports exactly four polygons." (Sec. IV.2.) The text does not say how the map is chosen for
>    a given graph; for its homogeneous tessellations the choice is implicit. **Ours, the local rule:** at a point with
>    links to n₁..n₄, a *corner* is an unordered pair of its links; the corner's *cycle length* c is 2 plus the shortest
>    path between the two neighbours that avoids the point (breadth-first search; no path gives c = ∞). A *rotation* is one
>    of the three ways to pair the four links into two "opposite" pairs; its four corners are the other four pairs (so a
>    rotation picks four of the point's six corners as faces, as a cyclic order of the links does; any two rotations
>    share exactly two corners). The point's rotation is the one whose four corner cycles give the smallest angle sum
>    parameter α (item 3); a tie is counted and broken by the lexicographically smallest sorted type. The chosen corners'
>    cycles are the point's four faces. **The choices this rule makes (ours), listed so that none is silent:**
>    - (a) *The criterion.* Smallest α is proposed. Smallest α and least negative K can disagree (arithmetic, Eqs. 25
>      and 27): of two rotations sharing two square corners, (4,4,6,8) has α = 2.417 and K = −1.104, (4,4,4,100) has
>      α = 2.480 and K = −0.963, and the α rule takes the more negative K. A K-based rule (the rotation with the least
>      negative K) is run beside the α rule and reported; "most square corners first" is a third possible rule, not run.
>    - (b) *The tie-break.* "Lexicographically smallest sorted type" means "prefer more square faces", and it moves K:
>      at α = 7/3, (4,4,4,12) reads −0.836 and (4,4,6,6) reads −0.926, and the rule takes (4,4,4,12). The share of tied
>      points is reported per cell.
>    - (c) *Square faces are not square count.* The α rule can choose fewer square faces than another rotation offers:
>      (4,4,6,6) at α = 7/3 is chosen over (4,4,4,14) at α = 2.357, two square faces where three were available. So the
>      face-square count at a point need not equal Sec. VI.3's □_i.
>    - (d) *Chords.* A corner cycle is a shortest path avoiding the point only; it may run through the point's other
>      neighbours, so it need not be chordless. A chordless rule would be a different definition.
>    - (e) *Consistency.* The text requires that "Each edge of the map supports exactly two regular polygons". The local
>      rule meets that only where its faces agree across every link. Face consistency (item 1's share, as in Sec. 2) is
>      reported per cell; whether a cell below a stated consistency is set aside is open, and any gate is fixed before
>      registration from fresh chains, never from T78's snapshots.
>    - (f) *Exact (degree parity).* Removing a point from a 4-regular graph leaves each piece attached to it by an even
>      number of links, so the point's four neighbours lie in one piece or in two pairs, and a rotation holds 0, 2 or 4
>      corners of length ∞, never 1 or 3. Types such as (4,4,4,∞) or (4,4,6,∞) never occur at a point, and the chosen
>      rotation never has four faces of length ∞.
>
>    *Built-graph look for this choice (sandbox until pinned, Sec. 2):* on the flat torus, the tube, the 4-cube, the
>    finite Fig. 7 tiling, the handle graphs and the finite Fig. 9 builds there are no ties; on the flat torus, the tube,
>    the Fig. 7 tiling and the Fig. 9 builds the chosen faces agree across every link (consistency 1.000), so there the
>    local rule is a global map; on the 4-cube it is not (0.500) and on a sheet with a built-in handle it nearly is
>    (0.981). A different face rule is a different definition and gets its own line here.
> 2. **Vertex type (from the text).** "Let k_i, i = 1…4, be the number of edges of the 4 polygons surrounding a vertex
>    and let us call the vector k = (k₁, k₂, k₃, k₄) the vertex type." (Sec. IV.2.) Here: the sorted cycle lengths of
>    the four chosen corners; ∞ is allowed as an entry (**ours**; the text's random-phase interior "support[s] no squares
>    (apart accidental ones)", Sec. VI.1, and has no finite faces).
> 3. **Angle sum and excess angle (from the text for homogeneous maps; ours point by point).** "the tessellated surface is
>    a constant curvature surface given by the angle sum parameter α = Σ_{i=1}^{4} (k_i − 2)/k_i (25). If α < 2 the
>    surface is spherical, i.e. of positive constant curvature, if α = 2 it is the flat Euclidean plane and, finally, if
>    α > 2 it is hyperbolic, i.e. of negative constant curvature" (Sec. IV.2). The text states this "For such maps", the
>    homogeneous ones ("For simplicity, we shall consider homogeneous maps, for which the edge type is the same for all
>    vertices, so that the geometrization gives rise to semi-regular tessellations"), in the limit "N → ∞, in which the
>    emerging manifolds are the covering spaces of genus g Riemann surfaces" (Sec. IV.2). **Applying it at single points
>    of finite, inhomogeneous graphs at N = 196, in the crossover cells, is ours.** The Euclidean excess angle at the
>    point is ε = π(α − 2) (**ours**, arithmetic: a regular Euclidean k-gon's corner is π(k − 2)/k, so πα is the four
>    corners' Euclidean sum; Sec. VI.1 uses the words "a larger excess angle at the vertex"). A face of length k ≥ 6 enters
>    as (k − 2)/k; a face of length ∞ enters as 1 (**ours**: the limit of the text's formula). **Exact (arithmetic; the
>    discrete Gauss–Bonnet sum):** on any consistent map of a 4-regular graph (E = 2V), Σ_v (α_v − 2) = Σ_faces (k_f − 2)
>    − 2V = 2(V − F) = −2χ, so Σ_v ε_v = −2πχ: the integrated excess angle is topological, 0 on a torus, 2π more for each
>    cross-cap and 4π more for each handle. Since α ≥ 2 at every point of a bipartite graph, a consistent map on a torus
>    is all squares.
> 4. **K at a point, in units of 1/ℓ² (from the text for a homogeneous map in the limit N → ∞; ours point by point at
>    N = 196).** The text: "For every hyperbolic tessellation there is exactly one geodesic length so that the sum of
>    interior angles at each vertex sums exactly to 2π" and, from the cosine rule for a hyperbolic n-gon (Eq. 26),
>    "Σ_{i=1}^{4} 2 arcsin( cos(π/k_i) / cosh(ℓ/2R) ) = 2π (27), where R is the radius of curvature of the Poincaré disk
>    on which the tessellation is constructed. [...] If the length unit ℓ is held fixed, the hyperbolic radius R of the
>    Poincaré disk varies and, with it, the curvature K = −1/R². [...] The tessellation realized by the graph minimizing
>    the free energy at every coupling g determines the value of the curvature K(g) in units of 1/ℓ²." (Sec. IV.2.)
>    **Here:** at each point, solve Eq. (27) for x = ℓ/R with that point's own type, and set K(point) = −x² (units of
>    1/ℓ²); α = 2 gives x = 0 and K = 0; cos(π/∞) = 1. **Exact bounds:** in a bipartite 4-regular graph the shortest face
>    is a square, so α ≥ 2 at every point, K ≤ 0 everywhere, K = 0 exactly when all four chosen corners close squares,
>    and K > −4 [ln(1 + √2)]² = −3.107, the value for four faces of length ∞, a lower bound that is not attained (item 1
>    (f)). The text itself says the point-by-point case exists: "in the general case, the tessellation will not be
>    semi-regular, corresponding to surfaces with possibly varying negative curvature" (Sec. IV.2); applying its
>    homogeneous Eq. (27) at each point separately, in finite graphs in the crossover rather than in the N → ∞ geometric
>    phase, is ours.
> 5. **A point on links with three squares, or on five or six squares (ours; the text has no such point).** The text's
>    geometric phase has "vertex types with at least one k_i = 4 and all other k_i = 4 or k_i ≥ 6" and in Sec. VI.3
>    "each vertex i can exist in four possible states, corresponding to the number □_i = 1, 2, 3, 4 of squares surrounding
>    it"; a point of the tube lies on five squares and a point of the 4-cube on six, outside that list. Under item 1 such
>    a point still has exactly four faces, and the rule chooses them: whenever four of its squares form a rotation the
>    point reads (4, 4, 4, 4) and K = 0, and the squares not chosen are not faces of the surface (on the tube they are the
>    rings round the short direction, which are non-contractible cycles of the torus, not faces). **Pointwise, the ring's
>    own points read K = 0, and the surplus-square count X of our family has no counterpart in K** (exact for ring3's own
>    points at every sighting, Sec. 3; sandbox for the built tube, 4-cube and handles, Sec. 2). **Integrated, a handle
>    carries exactly 4π of excess angle (Gauss–Bonnet, item 3), whatever its length:** the built handles of 3 and 5
>    layers (X = 8 and 16) both read Σε = 4π, and the finite Fig. 9 allotropes read +2π (built with a cross-cap) and +4π
>    (built with a handle) over the Fig. 7 tiling (sandbox, Sec. 2). So a curl is invisible point by point at the ring and
>    visible as a handle count, located at the splice; X does not follow it (the two handles have the same 4π).
> 6. **An object's point set (from T78 and T79's registered definitions).** ring3, the curled ring: a square each of whose
>    four links carries three squares; its points are the four of the square and the eight that its nine squares touch
>    (twelve). ring2, the uncurled twin: a square each of whose links carries exactly two squares; the same twelve-point
>    pattern with five squares. A flat a × b grid: its a·b points. One sighting is one point set, as the monomorphism
>    counts of `graphity.objects` define them (`count_rings`, `count_ring2`, `count_grid`); a finder that returns the
>    point sets, not only the counts, is to be written and tested against those counts (Sec. 10).
> 7. **Gathering an object's curvature (ours): mean or sum, and over which points.** The choices: a mean or a sum; over
>    the object's own points, its one-step shell (points adjacent to the point set and not in it), the two together, or
>    a ball of radius r. **Proposed to be scored:** ΔK_X = the mean, over every sighting of X in every analyzed snapshot
>    of the cell, of Σ over the sighting's shell of (K_bg − K(v)). Why: (i) the shell holds no point whose K the object's
>    definition fixes, while the interior points of an a × b grid ((a − 2)(b − 2) of a·b: 0, 0, 0, 1/9, 2/12, 3/15, 4/16,
>    6/20 across the eight grids) and ring3's own four points read K = 0 by construction, under K and under K_sq alike
>    (Sec. 6); (ii) the text puts a bubble's curvature on its boundary vertices and ties it to F through their number
>    ("each vertex on the boundary has a lower curvature [...] Since the number of boundary vertices depends on the bubble
>    size, this lower negative curvature is associated with the higher free energy", Sec. VI.1), which is a sum; (iii) a
>    sum grows with the object, as F does, while a mean over the object's own points saturates as grids grow. **Reported
>    beside, not scored:** the mean over the shell; the mean and the sum over the object's own points (the reading first
>    proposed); own points and shell together; and the definition-only null of item 10 (c). Errors by bootstrap over
>    replicas, 1,000 resamples, with F resampled together with K in every draw (item 9).
> 8. **The background 4Λ₂ (ours; the text says only "the surrounding geometric matrix with curvature 4Λ₂", Sec. VI.1).**
>    **Proposed to be scored:** K_bg in a cell = the plain mean of K over all points of every analyzed snapshot of the
>    cell: the warm background as a whole, about three squares per point. **Reported beside, not scored:** per object,
>    the mean over the points outside its one-step shell in the same snapshots; and the background first proposed (points
>    at graph distance 2 or more from every sighted object of the ten types), with its size. Why that first proposal is
>    not scored: a 2 × 2 grid is any square with no link at three squares, so the set keeps only points that lie on no
>    flat square and have no neighbour on one. **Exact identity:** mean squares per point = 4S/N = 4 − ρ + X/N (from
>    Σ_links S_e = 4S = 4N + X − D, with ρ = D/N), at least 2.87 at T78's ρ = 0.92 to 1.13; so that set is the most
>    melted tail of a snapshot, not the matrix, and with it our sign prediction (Sec. 8) was nearly true by definition.
>    A look in the correcting session (fresh chains with new seeds at g = 3.300 and 3.697, four replicas and five snapshots each;
>    scratch code, not in the repository, so it narrows and supports nothing) found 1.6 and 0.3 points per snapshot of 196
>    at distance 2 or more from every 2 × 2 sighting alone. **Feasibility check before code depends on any background
>    (exact per snapshot, rule 20):** the number of points in each background's support, per snapshot and per cell,
>    counted on fresh chains of the four cells with new seeds, not on T78's snapshots.
> 9. **The free-energy side (measured; T78 and T79's registered estimators, unchanged), and two open choices.**
>    F_X = −g ln(⟨n_X⟩/N), the free energy of one placement of X, in the toy's units (one missing square costs 4 at
>    λ = 1); E_X = ⟨H n_X⟩/⟨n_X⟩ − ⟨H⟩; S_X = (E_X − F_X)/g. The text's F is "measured in Joule with respect to the
>    surrounding geometric matrix" (Sec. VI.1). The registered F has no zero that Eq. (45) can use, for two reasons:
>    - (i) *Orientations (open; ours to propose, hers to decide).* `count_grid` divides ordered tuples by 8 when a = b
>      and by 4 when a ≠ b, so a rectangular grid's count holds both orientations. On the built flat 14 × 14 torus, where
>      every object and the background read K = 0, n = 196 for 2 × 2, 3 × 3, 4 × 4 and ring2 (F = 0) and n = 392 for
>      2 × 3, 2 × 4, 3 × 4, 3 × 5 and 4 × 5 (F = −g ln 2, −2.3 to −2.6 at g = 3.3 to 3.7) (exact: the counts are pinned
>      by `tests/test_objects_t79.py::test_tori`). Eq. (45) needs F = 0 there for all of them.
>      **Proposed to be scored:** F_X + g ln o_X, with o_X = 1 for the square grids and the rings and 2 for the
>      rectangular grids; the registered form reported beside.
>    - (ii) *The reference (open).* Even with (i), F is the free energy of constraining one placement to be X, and its
>      zero is "X at every placement", not "X as common as the matrix makes it": a 2 × 2 grid is a typical background
>      square, yet its F is not 0 (a look in the correcting session, fresh chains with new seeds, two replicas and ten
>      snapshots each, scratch code: n_2×2/N ≈ 0.55 and 0.51, so F_2×2 ≈ +2.0 and +2.5 at g = 3.300 and 3.697; T79's
>      registered value is the number). Named nulls: (ii-a) the
>      registered one, F = 0 when X occurs once per point per orientation; (ii-b) relative to the background's own
>      object, F_X − F_2×2. **Until one is chosen, nothing that depends on F's zero is scored except the per-object sign
>      word, which is stated against (ii-a) and reported under (ii-b).**
>
>    The free energies of all ten objects, ring3's included, are already on the record (T79's reading; `python
>    scripts/analyse_t79.py results` prints them), and they were known when these definitions were drafted (Sec. 4).
> 10. **The controls (ours), each computed with the scored reading in every cell and reported.**
>     - (a) *K_sq, square count only:* the K of item 4 from min(q, 4) faces of length 4 and the rest at a filler length,
>       where q is the number of squares through the point (each corner holds at most one square, by the hard-core rule).
>       The filler is ∞ (a choice). K_sq is a function of the per-point square counts, which are functions of the
>       per-link square counts the energy is built from; it is not E_X itself.
>     - (b) *K_len, arrangement kept, lengths removed:* item 1's rotation rule with every non-square corner set to the
>       same filler (∞) before the rotation is chosen. From K_sq to K_len adds the arrangement fact of Sec. 2 (four
>       squares give K = 0 only as a rotation); from K_len to K adds the lengths of the non-square faces. The two kinds of
>       content the geometrization adds are tested one at a time.
>     - (c) *The definition-only null (exact given the sightings):* each reading of each object computed from the
>       squares the object's definition guarantees and nothing else (every other corner at the filler): the object
>       placed in a background with no squares of its own. It shows what membership alone sets. On the object's own
>       points it needs no snapshot. On the shell, where X's definition guarantees no square, it is |shell_X| × (K_bg −
>       K_fill), with K_fill = −3.107 at filler ∞: the shell's size (read from each sighting) times a constant.
>     - (d) *The independence test, quantitative:* in each read cell, over the read flat grids, F_X is regressed on
>       ΔK_sq,X and ΔK_X together (with an intercept), refitted in every bootstrap draw; z_c is ΔK's coefficient over its
>       bootstrap error. **INDEPENDENT** if Σ_c z_c² over the m read cells exceeds the 95th percentile of χ² with m
>       degrees of freedom, **NOT INDEPENDENT** otherwise. Reported beside, not scored: the same with E_X in place of
>       ΔK_sq; ΔK beyond ΔK_len (do the face lengths carry anything); ΔK_len beyond ΔK_sq (does the arrangement); and ΔK
>       beyond the null of (c).
> 11. **The quantity Eq. (45) is tested on (ours, from the text's equation).** In the toy's units with ℓ = 1 (one link),
>     Eq. (45) in the summed reading of item 7 reads ΔK_X = κ_g F_X, with one unknown constant κ_g > 0 per coupling (it
>     holds n(g), G_N, c and the joule). Since F's zero (item 9 (ii)) is not fixed, the intercept and the ratio
>     F₁/F₂ are not scored. What is scored needs no zero for F: in each read cell, the least-squares line F = a + b ΔK
>     over the read flat grids, a free and not scored; the sign of b; the flat grids' residuals; and the held-out
>     objects' residuals (ring3, and ring2) at their ΔK. What this keeps of the ratio form is the ratio of differences,
>     (F₁ − F₂)/(F₃ − F₄) = (ΔK₁ − ΔK₂)/(ΔK₃ − ΔK₄). In the summed reading K_bg enters ΔK through each shell's size,
>     so item 8's choice matters to the slope; in a mean reading it would cancel. The per-object sign (the sign of ΔK_X
>     against the sign of F_X under item 9 (ii-a)) is scored separately (Sec. 4).

---

## 1. What the text says (published; [T25], the HTML text, searched on 23 October 2026)

**Sec. IV.2, "Geometry from combinatorics".** The setting is the infinite, homogeneous limit: "We will henceforth
consider the limit N → ∞ [...] we will consider first configurations in which each vertex supports the same number □ of
squares. These correspond to a quantized constant negative curvature". The construction is items 1 to 4 of the box. What
sets the squares against the longer faces: "The geometric phase is realized by the condensation of squares and
corresponds, thus to vertex types with at least one k_i = 4 and all other k_i = 4 or k_i ≥ 6 for all vertices. At each
coupling, one of the four possible vertex types of the semi-regular tessellation, with one, two, three or four squares
will characterize the minimum of the free energy, the remaining larger cycles determined by the detailed balance between
the combinatorial energy and entropy." More squares means less curvature: "In order to maintain the total interior angle
sum as 2π, as in (27), the quantity ℓ/R has to decrease, which means the absolute value of the curvature of the
tessellated surface typically decreases, until it vanishes for four squares around each vertex." Fig. 7's caption: "The
2D tessellation geometrizing the three-square-per-vertex infinite graph via its 1-skeleton." And the closing paragraph:
"Via this construction, the purely combinatorial Ollivier curvature is mapped to geometric curvature. The value of this
curvature is determined by the statistical balance between the combinatorial energy dependent only on square cycles and
the entropy representing the possible choices of residual larger cycles. Of course, in the general case, the tessellation
will not be semi-regular, corresponding to surfaces with possibly varying negative curvature, so-called Cartan-Hadamard
surfaces [85, 86]. And finally, on scales smaller than ℓ_P, there are random microscopic degrees of freedom." The
tessellation references are [87] B. Datta and S. Gupta, Semi-regular tilings of the hyperbolic plane, Discrete Comput.
Geom. 65, 531 (2019); [88] A. Maiti, Quasi-vertex-transitive maps on the plane, Discrete Math. 343, 7 (2020); [89]
A. Maiti, Pseudo-homogeneous tilings of the hyperbolic plane, arXiv:2302.05661 (2023): none read by us.

**Sec. VI.1, the equation.** "Let us now consider a random phase bubble embedded in a constant curvature graph at low, but
finite coupling. The interior vertices of the bubble support no squares (apart accidental ones). The boundary vertices of
the bubble also support typically less squares than the surrounding graph [...] each vertex on the boundary has a lower
curvature since less squares and longer cycles imply a larger excess angle at the vertex, so that the curvature is more
negative than in the geometric phase, as explained above. Since the number of boundary vertices depends on the bubble
size, this lower negative curvature is associated with the higher free energy, but this relation is statistical in
nature since many microstates of slightly different curvature, due to long cycles entropy, characterize the ensemble with
a given free energy. The ensemble equation is thus −(⟨K⟩ − 4Λ₂) ℓ² = (κ/ℓ) F, κ = n(g) 8πG_N/c⁴, (45) in units where the
free energy F is measured in Joule with respect to the surrounding geometric matrix with curvature 4Λ₂. G_N is Newton's
gravitational constant and n(g) is a numerical factor depending on the original coupling g." The paragraph that follows
opens: "In the Lorentzian picture the curvature changes sign." (Sec. VI.1, between Eq. (45) and Eq. (46).) The sign:
with n(g) > 0, an object that costs free energy (F > 0) sits at more negative curvature than its background
(⟨K⟩ < 4Λ₂) in the Riemannian K of Eq. (45), which the Lorentzian picture calls a higher curvature. That is the deficit
case of the bubble and of Fig. 9.

**Sec. VI.3 and the Fig. 9 caption, the statements about denser and sparser regions.** The text: "each vertex i can exist
in four possible states, corresponding to the number □_i = 1, 2, 3, 4 of squares surrounding it. The number □_i
determines the quantized curvature at this vertex as shown above." And: "we can have metastable domains characterized by
a higher number □_dom than the prevailing configuration □ and therefore having a larger free energy than the space around
them at a given g. Because of this higher free energy they have also a higher curvature (in the Lorentzian picture) and
interact gravitationally." Fig. 9's caption shows the sparser case: "An allotropy region (blue) with vertices surrounded
by two squares within an hyperbolic tessellation with all vertices surrounded by three squares. The hyperbolic
tessellation represents space of a given uniform curvature; the blue allotropy region represents a region of dark matter,
with a higher absolute curvature and free energy." And after it: "Of course, for couplings g midway between values
favouring two different number of squares as the free energy minima, small domains of lower absolute curvature can form
before the whole space-time transitions to this configuration. These would correspond to antigravity domains within a
uniform metastable universe."

*Ours, corrected 23 October.* The antigravity sentence is not about the same region as the metastable denser domain of
the sentence before Fig. 9. Its domains "form before the whole space-time transitions to this configuration", within "a
uniform metastable universe": they are the coming configuration, with more squares, a smaller |K| and a lower F than the
metastable universe around them, which agrees with Eq. (45) (F below the matrix's, K above it). Fig. 9's region (fewer
squares, higher |K|, higher F) agrees with Eq. (45) as well. The one conflict is the metastable denser domain: more
squares, so by Sec. IV.2 "the absolute value of the curvature [...] typically decreases", yet "a larger free energy" and
"a higher curvature (in the Lorentzian picture)", which, read through the sentence after Eq. (45), is a more negative K.
So **Sec. IV.2's geometrization implies, through its "typically", that Eq. (45) fails in sign for metastable domains
denser than their background; Sec. VI.3 asserts the opposite without computation; the antigravity sentence is the
lower-F case and agrees with Eq. (45).** The toy's ordered objects (F > 0 under the registered null, more squares than
the warm background) are that metastable denser case, so a flipped sign for them follows from the text and is not a
finding (Sec. 4).

## 2. What the built graphs read (sandbox; `sandbox/eq45_geometrize_check.py`, 23 October; to be pinned by the tests of `graphity.geometrize` before any of it is cited as exact, rule 16 (c))

| graph | N | links at 1 / 2 / 3 squares | rings | vertex types under item 1 | K (1/ℓ²) | face consistency | Σε / π |
|---|---|---|---|---|---|---|---|
| flat torus 14 × 14 | 196 | 0 / 392 / 0 | 0 | (4,4,4,4) at all 196 | 0 everywhere | 1.000 | 0 |
| tube 4 × 36 | 144 | 0 / 144 / 144 | 36 | (4,4,4,4) at all 144 | 0 everywhere | 1.000 | 0 |
| tube 16 × 4 | 64 | 0 / 64 / 64 | 16 | (4,4,4,4) at all 64 | 0 everywhere | 1.000 | 0 |
| 4-cube (4 × 4) | 16 | 0 / 0 / 32 | 24 | (4,4,4,4) at all 16 | 0 everywhere | 0.500 | 0 (not a consistent map) |
| finite Fig. 7 tiling (240 points, three squares and a hexagon each; `scripts/build_planted_allotrope.py`) | 240 | 240 / 240 / 0 | 0 | (4,4,4,6) at all 240 | −0.48636 everywhere (x = ℓ/R = 0.6974; ε = π/6) | 1.000 | 40 |
| flat 14 × 14 torus with a 3-layer circumference-4 handle (one curled ring built in) | 208 | 20 / 388 / 8 | 1 | (4,4,4,4) at 184; (4,4,4,6) at 24 | ring's own 4 points 0; its 12-point set −0.324 (the 8 touched points are the splice's end layers); 172 lattice points beyond one step of the splice 0 | 0.981 | 4 |
| the same with a 5-layer handle (three rings) | 216 | 20 / 396 / 16 | 3 | (4,4,4,4) at 192; (4,4,4,6) at 24 | the middle ring's 12-point set 0 exactly; splice points −0.486 | 0.981 | 4 |
| finite Fig. 9 allotropes, fold (`build_planted_allotrope.build_all`: a hexagon of the Fig. 7 tiling deleted and opposite corners joined, a cross-cap) | 234 | 252 / 216 / 0 | 0 | (4,4,4,6) at 216; (4,4,6,6) at 18 | the 18 two-square points −0.92626; the rest −0.48636 | 1.000 | 42 |
| finite Fig. 9 allotropes, handle (the same: two hexagons deleted and joined across) | 228 | 264 / 192 / 0 | 0 | (4,4,4,6) at 192; (4,4,6,6) at 36 | the 36 two-square points −0.92626; the rest −0.48636 | 1.000 | 44 |
| the same handle surgery on the flat 14 × 14 torus (`build_all`'s flat handle) | 188 | 24 / 352 / 0 | 0 | (4,4,4,4) at 164; (4,4,4,6) at 24 | the 24 three-square points −0.48636; the rest 0 | 1.000 | 4 |

No ties in the rotation choice on any of these graphs. Every graph is valid under the hard-core rule, bipartite and
4-regular (checked with `graphity.cqg.is_valid`), and `count_rings` returns the expected number. The copy of the output
in `sandbox/out/` predates the last three rows and the Σε column; rerun the script to regenerate it.

What these readings show (sandbox until pinned):

- **The reading reproduces the text's own case.** The Fig. 7 tiling, which the review names as the geometrization of the
  three-square-per-vertex graph, reads one uniform type (4,4,4,6) and one uniform K = −0.486/ℓ², with the local rule a
  global map (consistency 1). That is the positive control the registered reader must pin in a test.
- **The reading reproduces Fig. 9's sign.** In both finite Fig. 9 builds, the allotrope points (two squares each, as in
  the caption) read (4,4,6,6) and K = −0.926 against the tiling's −0.486: the caption's "higher absolute curvature". A
  second positive control for the tests.
- **Curl is invisible point by point and visible as a handle.** Every point of the tube, of the 4-cube and of a ring
  built into a sheet reads (4,4,4,4) and K = 0, the same as the flat torus. A point of the tube lies on five squares;
  four of them form a rotation and are its faces; the fifth, the ring round the short direction, is a non-contractible
  cycle, not a face. In the handle graphs the ring's own four points read K = 0 in every case, and what the ring's
  twelve-point set reads comes entirely from the eight touched points, which on the built graph carry the splice's
  missing squares (at h = 3) or nothing (at h = 5). Integrated, both handles carry Σε = 4π (Gauss–Bonnet, box item 3),
  whatever their length and whatever their X (8 and 16); the finite Fig. 9 builds are made by the same kinds of surgery
  and carry +2π (the cross-cap) and +4π (the handle) over the tiling. So the curling cost 4(λ − 1)X of our family has
  no pointwise counterpart on the curvature side of Eq. (45); under the Sec. IV.2 geometrization a curl shows up as
  topology (a handle of circumference 4), located at the splice. This is the same fact as Update 91's "a tightly
  curled tube is flat as a surface" (`graphity.regge`), reached by the review's own construction rather than by Regge
  lengths.
- **Four squares at a point do not by themselves give K = 0.** A point reads K = 0 when its square-closing corners contain
  a rotation, which four squares do only when the two non-square corners are disjoint pairs (the flat lattice point) and
  not when they share a link (then the type is (4,4,4,k) with k ≥ 6). Five or six squares always contain a rotation. So
  the per-point K is not a function of the square count alone even at q = 4; this is part of what gives the reading any
  content beyond the energy (Sec. 6).
- **The uncurl is seen.** The splice of the handle, where lattice links were cut, reads (4,4,4,6) and K = −0.486 at 24
  points; missing squares make longer faces and negative K, as Sec. IV.2 says.

## 3. What is exact, what is sandbox, and what must be measured

**Exact, needing no snapshot:** the arithmetic of the box (the values and bounds of Eq. (27), item 3's Gauss–Bonnet sum,
item 1 (f)'s parity fact); and the argument that ring3's own points read K = 0 at every sighting, because the hard-core
rule forces the two extra squares on each ring link to use the point's two different non-ring links, so the four mixed
corners all close squares and form a rotation.

**Sandbox until pinned:** the built-graph readings of Sec. 2.

**Measured, needing snapshots:** ΔK_X (box item 7) for each of the ten objects, K_bg (item 8) and the controls (item 10)
in each of the four cells (g = 3.300, 3.433, 3.550, 3.697; N = 196; λ = 1; named points), which depend on the warm
surroundings of the objects' points and on how long the non-square faces are there. F_X for every object and cell is
already measured (T78 and T79's readings, PREREGISTRATION; `python scripts/analyse_t79.py results` prints F, E and S
for all ten).

## 4. The test's logic

Eq. (45) divided for two objects in the same background at the same coupling: F₁/F₂ = (⟨K⟩₁ − 4Λ₂)/(⟨K⟩₂ − 4Λ₂). Every
constant cancels: ℓ, n(g), G_N, c and the joule (the reading note of 22 October, Sec. 6). But each side needs a zero:
the curvature's is the background 4Λ₂ (box item 8), and F's is the reference against which it is "measured [...] with
respect to the surrounding geometric matrix" (Sec. VI.1). The toy's registered F has no such zero (box item 9: an
orientation offset of g ln 2 between rectangular and square grids, and a reference at "X at every placement"). So the
ratio F₁/F₂ is not defined here, and the intercept of a line of F against curvature is not scored. What survives is the
ratio of differences, in which F's zero cancels: the slope of the line and the pattern of residuals (box item 11).
Through Eq. (47) ratios of F would be mass ratios, but that step is not taken here (Sec. 7).

**Form of the test.** In each read cell, with the objects' F_X (measured; box item 9 (i) as proposed) and ΔK_X (to be
computed): the least-squares line F = a + b ΔK over the flat grids with 50 or more sightings (at least four needed), a
free; bootstrap over replicas, F and K resampled together, refitting the line in each draw; the flat grids' residuals;
then the held-out objects' residuals from that line, F_X − F_line(ΔK_X), for ring3 and ring2. Eq. (45) says b > 0
(an object costs free energy in proportion to how much more negative its shell's curvature is than the background's),
the flat grids on the line, and the held-out objects on it too. Multiplicity: about eleven tests per cell over up to four
cells means that even an exact Eq. (45) would fail "any object off by 2σ" with a probability near 0.9 (0.95⁴⁴ ≈ 0.1).
So the slope is combined over cells (Stouffer's sum of z over √m), and each family of residual tests is held to a
Bonferroni bar: two-sided level 0.05/m_r, with m_r the number of residuals tested in that family over all read cells,
printed with the result (about 3.2σ for 32 grid residuals).

**The held-out object.** The curled ring is the object the whole thread is about (the entropy penalty on curl, T79), so
its F is predicted from the flat grids' line before its ΔK is combined with its F, and the held-out part of the verdict is
scored at the ring. Said plainly: the free energies of all ten objects, ring3's included, are already on the record
(T79's reading), and the definitions of the box (mean or sum, the point set, the background, the convention for F) were
chosen with them known. Only the curvature side is unseen. The held-out discipline protects the curvature reading and
nothing else. Rule 14 is written for sizes; there is no size claim in this test (one size, N = 196), so rule 14's
held-out size is not triggered; N = 484 is named as the follow-up if the form holds, and is not part of this test.

**Sign.** For the ordered objects the direction is fixed by the text before any count (Sec. 1): they are denser than the
warm background (about three squares per point), and their F is positive under the registered null (T78, T79), which is
Sec. VI.3's metastable denser case, for which Sec. IV.2 with Eq. (45) implies the wrong sign. A per-object OPPOSITE SIGN
is therefore expected from the text and is not counted as a finding; SAME SIGN for an ordered object would be. The sign
of the slope b is a separate statement (how F varies across objects), scored by its own words.

**Stages.** Stage 1, exact per snapshot and free of any new chain: compute ΔK_X, K_bg and the controls on the saved
snapshots (Sec. 5). **Stage-1 read rule (grids alone):** a cell is read on the grids when at least four flat grids each
have 50 or more sightings in the analyzed snapshots; ring2 is scored in a read cell if it has 50 or more sightings there;
ring3 is reported with its sighting count and is not scored in stage 1 unless it reaches 50 (with 6 to 15 expected per
cell it will not). Stage 2: replay T78's four configs from their seeds (the kernel's same-seed reproducibility is a
tested property, and T79's replay matched T78 row for row) with K computed at every one of the 12,816 snapshots per cell;
a laptop job of some hours, registered as part of the same test. **Whether stage 2 runs is put to the owner in the same
sitting as her prediction, and decided before anything is registered** (Sec. 11, question 3).

**Verdict words (for the draft registration, T81).** Per object, per read cell:
- **SAME SIGN / OPPOSITE SIGN / UNDECIDED:** the sign of ΔK_X against the sign of F_X (box item 9 (ii-a); (ii-b)
  reported), decided where both differ from zero beyond the Bonferroni bar of the sign family. Summarized over objects
  and cells; OPPOSITE SIGN for an ordered object is expected from the text (above).

Over the read cells, for the flat grids' line:
- **SLOPE AS WRITTEN:** the combined slope Z_b = Σ_c z_{b,c}/√m above +2, and no read cell with z_b below −2.
- **SLOPE FLIPPED:** Z_b below −2, and no read cell with z_b above +2.
- **CELLS DISAGREE:** one read cell with z_b above +2 and another below −2.
- **NO SLOPE:** |Z_b| at most 2 and the cells do not disagree: the curvature reading does not track F across the grids.
- **LINEAR / NOT LINEAR:** whether any read flat grid lies off its cell's line beyond the Bonferroni bar.
- **RING ON / RING OFF THE LINE** (above or below), **TWIN ON / TWIN OFF THE LINE:** the held-out residuals beyond the
  Bonferroni bar of the held-out family; the ring only where it is read (stage 2, in practice).

Composite words, as written in T81:
- **EQ. 45 IN FORM, UP TO F's ZERO:** SLOPE AS WRITTEN, LINEAR, and the ring and the twin on the line. The intercept,
  which Eq. (45) sets to zero, is not tested until F's zero is fixed.
- **FLIPPED, LINEAR:** SLOPE FLIPPED, LINEAR, and the ring and the twin on the line.
- **NOT PROPORTIONAL:** SLOPE AS WRITTEN or SLOPE FLIPPED, with NOT LINEAR or a held-out object off the line.
- **NO SLOPE** and **CELLS DISAGREE**, as above.
- In stage 1, the ring not read: the slope word and LINEAR / NOT LINEAR with the twin's word, marked "ring not read".
- **NOT READ:** fewer than two cells read on the grids.
- Scored separately: **INDEPENDENT / NOT INDEPENDENT** (box item 10 (d)).

## 5. What data exist, and whether the curvature can be computed exactly on them

- **T78's saved snapshots:** `results/t78_curl_vs_flat_n196_g{3300,3433,3550,3697}_adj/`, 144 graphs per coupling (16
  replicas × 9 snapshots: blocks 0, 100, ..., 800, that is every 5,000 sweeps of the 40,000-sweep measurement, with the
  config's `save_every_snap` = 100), 576 graphs in all, each a `.npz` with `adj` and `part`. These are the same chains
  whose 12,816 snapshots per cell gave T78's and T79's F_X.
- **T79's replays saved no adjacency** (`configs/t79_curl_family_n196_g*.json`, `"save_adjacency": false`). Since every
  replayed snapshot equals T78's row for row (T79's identity check), T78's 576 saved graphs are the snapshots of both
  tests. The ten objects' sightings in them have to be found afresh (a finder returning point sets; Sec. 10). In each
  bootstrap draw F_X is recomputed from the drawn replicas' T79 rows and ΔK_X from the same replicas' saved snapshots.
- **T36's saved graphs** (`results/t36_allotropes_n196_adj/`, 160 at N = 196, λ = 1, g = 3.433 and 3.697) are from other
  chains and carry no F_X; they can only serve as a second reading of K_bg at two couplings, reported and not scored.
- **Can the curvature be computed exactly on them?** Yes, snapshot by snapshot: under the box every quantity is a
  deterministic function of the graph (breadth-first searches and a one-dimensional root find), so the per-snapshot
  values are exact. The ensemble averages are estimates with sampling error, and the sample is thin for the curled ring:
  T78 saw 1,374, 1,056, 824 and 576 ring sightings in 12,816 snapshots per cell, so the 144 saved snapshots of a cell
  should hold about 15, 12, 9 and 6 ring sightings. The sandbox look of 22 October (`sandbox/forbidden_volume.py`)
  found 54 curled rings; its LOG line says "672 saved warm graphs of T78 and T36", but its script reads every file in
  the four T78 directories and in `results/t36_allotropes_n196_adj/`, which hold 576 and 160 (directory listings,
  23 October; no file opened): 736. Its output (`sandbox/out/forbidden_volume_2026-10-22.txt`, by the look's own
  finder) gives the 54 as 10, 23, 4 and 17 at g = 3.300, 3.433, 3.550 and 3.697,
  with T36's graphs only at 3.433 and 3.697, so T78's graphs alone hold 10 and 4 at 3.300 and 3.550, against the 15
  and 9 scaled above. The twin and the flat grids are far commoner (T79 saw every flat grid thousands of times in
  12,816 snapshots per cell); which of them reach 50 sightings in 144 snapshots is what the stage-1 read rule checks
  (Sec. 4). So stage 1 can read the slope and the linearity on the flat grids, and the twin, in cells where four grids
  reach 50 sightings, and the held-out ring in none.
- **Nothing in this brief was computed on those files.** The check of Sec. 2 used built graphs only, so that the owner's
  prediction can be recorded before the data are touched (rule 16 (b) in spirit; the data belong to a registered test
  that has not been read by this test's rule).

## 6. Would any choice make the test circular? Yes, the obvious one

**What the look of 22 October used for the curvature** (`sandbox/LOG.md`, 22 October, evening; sandbox): "the curvature
side dD_X = E_X/4 (the mean excess of missing squares when the object is present)", with E_X = ⟨H n_X⟩/⟨n_X⟩ − ⟨H⟩ and
H = 4D at λ = 1. So its curvature was the energy side of the same free energy: F_X = E_X − g S_X, and its ratio F/dD
= 4(1 − g S_X/E_X) is a statement about how the entropy share of each object's free energy varies, not about any
curvature read from the graph. It found the sign wrong for every ordered object and the ratio spread from −2.1 to −4.3
with the ring at one end; what that shows is that the ring's free energy has an entropy share the others do not (T79's
penalty on curl), which was already measured. It cannot test Eq. (45), whose content is a relation between two different
readings of one object.

**Where circularity re-enters.** D = Σ_links max(0, 2 − S_e) is a function of the per-link square counts; the per-point
square count q is Σ_links at the point S_e / 2; so any curvature read from square counts alone (the review's own
per-point label □_i of Sec. VI.3, or K_sq of item 10) is a function of the energy's own variables, summed over the
object's points instead of the whole snapshot. The test would then compare F with a local piece of the same variables as
E, the 22 October look one step refined.

**Content the definitions fix.** Some of the curvature side is set by the objects' definitions, under K and K_sq alike:
the interior points of an a × b grid (a fraction (a − 2)(b − 2)/ab: 0, 0, 0, 1/9, 2/12, 3/15, 4/16, 6/20 across the
eight grids) and ring3's own four points read K = 0 by construction, and K_sq reads 0 there too. A comparison of K with
K_sq cannot see this shared content. Hence the scored region is the shell (box item 7), which the definitions fix
nowhere, and the definition-only null (item 10 (c)) shows what membership alone gives.

**What the geometrization adds, and all it adds.** Two kinds of content: the lengths of the non-square faces (6, 8, 10,
... or ∞), which the energy never sees ("the combinatorial energy dependent only on square cycles and the entropy
representing the possible choices of residual larger cycles", Sec. IV.2), and the arrangement fact of Sec. 2 (four
squares at a point give K = 0 only when they form a rotation). It is modest: at a point with three square faces the
fourth face's length moves α only between 2.167 (a hexagon) and 2.5 (the limit k → ∞), K between −0.486 and −0.965; at
two square faces, α between 2.333 and 3 and K between −0.926 and −1.734 (exact, from Eq. (27)). **So the box carries
three controls and a quantitative test (item 10):** K_sq (square count only), K_len (the arrangement kept, the lengths
removed), the definition-only null, and a regression asking whether ΔK predicts F beyond ΔK_sq. NOT INDEPENDENT means the
"independent reading" was not independent on these data, and the test has shown nothing the 22 October look did not.

**A choice that would be circular outright, and is not made:** reading 4Λ₂ from the background's mean energy, or
reading an object's K from the squares it adds, or scoring only points the definition fixes (the ring's own four points
read exactly 0 whatever happens; a test on them alone would compare F with a constant).

## 7. Rule 13's bar

This test compares toy objects with toy objects: differences of F against differences of curvature, in one toy, at one
size, in units that cancel. It never compares with a measured mass. To become a mass ratio it would need Eq. (47) (ours,
unverified reading of the review: free-energy ratios as mass ratios; the review's own words on Eq. (47) are that "the
equations hold as statistical ensemble averages" and that "these are not dynamical equations but, rather, macroscopic
constitutive equations of matter", Sec. VI.1, and its abstract says of the cosmology in general that the network model
encodes it "albeit still at a qualitative level"), a fixed zero for F (box item 9), and an identification of two toy
objects with two physical things of measured mass ratio, which [T25] does not supply and which O107's knots (energies
14, 20 to 30, 8) do not have. If one were ever proposed, rule 13's checklist applies in full: derived independently,
input uncertainty propagated, inputs checked for containing the target, neighbouring values tested, and the number of
other arbitrary combinations that would match counted (`sandbox/spring_ratio_look.py` did that count for loop lengths:
29,101 combinations within 2 % of 5.36). None of that is in this test.

## 8. Predictions

**The owner's: owed before stage 1 runs.** Her question of 22 October gave this thread its form ("how can we confirm or
further explore this?"); her prediction for Eq. (45)'s sign and form on the toy's objects is recorded in T81 before any
count.

**Ours, written before any count (23 October), revised the same day with the definitions and still before any count.**
The first version, under the earlier definitions, said FLIPPED SIGN (nearly true by definition under the first background),
NOT PROPORTIONAL (an intercept more than 2σ from zero; the ring above the flat grids' line by 10 to 25 units; the twin
below it) and NOT INDEPENDENT. In the revised words:
1. Sign: OPPOSITE SIGN for all ten objects in every read cell: the objects' shells are squarer than the warm background,
   so ΔK_X < 0, while F_X > 0 under item 9 (ii-a). By Sec. 1 this follows from Sec. IV.2 for denser-than-background
   objects with positive F, so it is recorded and not counted as a finding. Carried over from the object's own points,
   where it was nearly definitional, to the shell, where it is less certain.
2. Form: SLOPE FLIPPED (larger grids have higher F and, we expect, a more negative ΔK, their shells being larger and
   squarer) and LINEAR on the flat grids; in stage 2 the held-out ring off the line, above it by 10 to 25 units of free
   energy (T79's penalty on curl, 5.5 to 6.0 units of entropy, times g, if its shell sits near the line), because its
   extra free energy is entropy that no face length records; the twin below the line. Composite: **NOT PROPORTIONAL**
   (in stage 1: SLOPE FLIPPED, LINEAR, twin below, ring not read).
3. Independence: **NOT INDEPENDENT**, for the reason first given: at these couplings the non-square faces are long and
   nearly uniform in length, so the geometrized K at a point is set by its square count and arrangement.

If 1 fails (SAME SIGN for some ordered objects), the review's Fig. 9 reading applies to those objects and the test has
found something the look of 22 October could not see; if 2 fails (the ring on the line), the penalty on curl is
reflected in the curvature of the ring's surroundings, which would be a result about the hard-core rule's forbidden
volume (O148) and not about Eq. (45).

## 9. What would make us drop the thread, and what comes first

**As first designed the run could not decide** (the adversarial check of 23 October): stage 1 could return only NOT
READ, the sign was fixed by the text and the background, and NOT PROPORTIONAL was forced by multiplicity and F's
convention. The cheapest decisive steps therefore come first, in this order:
1. The definitional fixes of this revision (the background, F's zero and orientation, the scored region and sum, the
   rotation rule's choices, the controls, the verdict words).
2. The built-graph controls, all in seconds: the Fig. 7 tiling, the Fig. 9 positive control and the Gauss–Bonnet sums
   (now in the sandbox script, Sec. 2), to be pinned as tests of `graphity.geometrize`.
3. **A chain-free test in the review's unambiguous case (ours, a proposal, not designed):** deficit objects in an
   ordered background at low g, where F is close to E; K_bg = 0 exactly on the flat torus, and E and K are exact on
   built graphs. One exact constraint it must face (box item 3): on a torus whose faces stay consistent, Σε = 0 and ε ≥ 0
   at every point, so a built deficit with consistent faces must change the surface's topology (a handle or a
   cross-cap), as the flat handle does; the design has to say whether it reads a mean or a sum, as item 7 does.
4. The stage-2 decision and the open choices of the box, put to the owner in the same sitting as her prediction.

Only then T78's snapshots. Eq. (45) as a route from the toy's free energies to a number is dropped if, with the
geometrized reading, OPPOSITE SIGN holds for every ordered object in every read cell together with NOT INDEPENDENT, since
then the review's equation, read by the review's own geometrization, does not describe ordered objects in this toy and
its independent content is nil on these data (OPPOSITE SIGN alone is expected from the text and drops nothing). It is
also dropped on NO SLOPE, or on SLOPE AS WRITTEN with the ring off the line under both K and K_sq: Eq. (45) would then hold
for the flat grids and fail for the one object the hypothesis cares about. It stays open only on EQ. 45 IN FORM, UP TO
F's ZERO, or FLIPPED, LINEAR, either with INDEPENDENT, in which case the next step is a fixed zero for F and a pair of
objects with a known physical identification, which [T25] does not propose and the record does not have, and the rule-13
checklist before any comparison.

## 10. Code to build, with tests, before registration (nothing run on saved states until the owner's prediction is in)

1. `graphity.geometrize` (new): `corner_lengths(adj)`, `vertex_types(adj)`, `curvature(adj)` returning K per point under
   the box's items 1 to 4 (with the α rule and the K-based rule of item 1 (a), and a tie flag), `square_count_curvature`
   and `length_free_curvature` for item 10 (a) and (b), `definition_only_null` for 10 (c), and `face_consistency(adj)`.
   Tests pin the Sec. 2 table: the flat torus, the tube and the 4-cube all 0; the Fig. 7 tiling (4,4,4,6) and −0.48636 at
   every point; **the Fig. 9 positive control** (the allotrope points of both `build_all` builds read (4,4,6,6) and
   −0.92626 against the tiling's −0.48636); **the Gauss–Bonnet sums** (Σε/π = 0 on the flat torus and the tubes, 40 on
   the Fig. 7 tiling, 42 for the fold (+2π), 44 for the handle (+4π), 4 on the flat handle and on both built handles);
   the handle graphs' censuses; the parity fact (no chosen type with exactly one ∞ face, on graphs with cut points);
   Eq. (27)'s solver against the hand values ((4,4,6,8) −1.104, (4,4,4,100) −0.963, (4,4,4,12) −0.836, (4,4,6,6) −0.926,
   and the bound −3.1072 = −4 [ln(1 + √2)]²); and a brute-force check of corner lengths against networkx shortest paths
   on a chain-disordered 8 × 8 graph.
2. `graphity.objects` (extended): finders returning point sets for ring3, ring2 and the a × b grids, tested so that the
   number of point sets equals the existing counts on the flat and curled tori and on warm 8 × 8 graphs; and the shell
   of a point set.
3. A feasibility script for box item 8: each background's support per snapshot and per cell, on fresh chains of the four
   cells with new seeds.
4. `scripts/analyse_t81.py`: reads the named set of 576 saved T78 graphs and T79's registered rows, computes items 7 to
   11 of the box with the replica bootstrap (F and K resampled together), prints per cell the sighting counts, the
   consistency and the share of tied points, the background's support, the sign words, the line, the held-out residuals
   with the Bonferroni bars and m_r, the independence test and the verdict word; refuses a partial set.
5. If stage 2 is authorized: `scripts/run_curl_curvature_replay.py`, T78's runner with K computed and written per
   snapshot, with its identity check against T78's rows.

## 11. Questions for the owner (one sitting, read back as one set, rule 20)

1. Her prediction for the sign (as written in Eq. (45), or flipped, for the toy's ordered objects) and for the form (the
   curled ring on the flat grids' line or off it), before any count.
2. Whether the local face rule of item 1 is the reading she wants tested, or whether she wants a second face rule run
   beside it (for example, counting every square through a point as a face, which abandons the text's "exactly four
   polygons" and makes a curled point read positive curvature; that would be a new definition under S1, ours, not the
   review's).
3. Whether stage 2 (the replay with K at every snapshot, a laptop job of some hours) is authorized; without it the
   held-out ring is not scored at all. To be decided in the same sitting as her prediction, before registration.
4. The open choices of the box, each with its proposal: the rotation criterion, the tie-break and a consistency gate
   (item 1 (a), (b), (e)); the scored region and the sum (item 7); the background (item 8); the orientation convention
   and F's reference (item 9 (i), (ii)).

## 12. Corrections of 23 October (after the adversarial check; each made in place above)

1. Background (box item 8; Sec. 4 "Sign"; Sec. 8): the distance-2 background was nearly empty and its own most melted
   tail; replaced by the plain mean, the first version reported with its size, a feasibility check named. "A melted
   background" corrected to the warm background, about three squares per point.
2. F's zero (box items 9 and 11; Sec. 4): the orientation offset and the reference are listed as open choices; the
   intercept criterion and the ratio F₁/F₂ are no longer scored. The estimate of F_2×2 offered in the check (about +1)
   was replaced by a look's value (about +2.0 to +2.5).
3. Curl (box items 3, 5 and 7; Sec. 2): the integrated, Gauss–Bonnet reading added; "a curl is a handle, not a
   curvature" restated as pointwise invisible, integrated a handle count; mean or sum and the region listed, the shell
   sum proposed to be scored.
4. Circularity (box item 10; Sec. 6): the definitional content named; a definition-only null, a length-free control and
   a quantitative independence test added; the filler length listed as a choice; "carries only the information that the
   energy already has" corrected.
5. Verdict words (Sec. 4; T81): a stage-1 read rule for the grids; a per-object sign word; words for no slope and for
   cells that disagree; a combined slope and Bonferroni bars in place of "any object off by 2σ".
6. Sec. 1: the sentence after Eq. (45) quoted; the antigravity sentence read as the lower-F case, not the same region;
   a flipped sign for ordered objects follows from the text and is not a finding.
7. The rotation rule's choices listed (box item 1). Modified: the check's ties at α = 2.5 and 8/3 and its example of
   fewer square faces pair types that cannot be two rotations of one point (one type has exactly one face of length ∞,
   impossible by item 1 (f), or the two types share fewer than the two corners any two rotations share); examples that
   pass both conditions are given instead (whether a warm graph holds them is what the per-cell census shows). Its
   example of α against K, and its tie at α = 7/3, are kept.
8. The held-out ring's F is on the record and the definitions were chosen with it known; said in Sec. 4.
9. The bootstrap resamples F with K (box item 7; Sec. 5).
10. The built-graph counts relabelled sandbox until pinned; the Fig. 9 positive control and the Gauss–Bonnet sums added
    to the sandbox script and to the test plan.
11. "No paper fixes / supplies" and "none exists" reworded to what [T25] does not do (rule 15).
12. "Still at a qualitative level" is the abstract's sentence about the cosmology in general, not a caveat on Eq. (47);
    quoted as such.
13. The scope of Sec. IV.2 (N → ∞, homogeneous maps) stated, and its use at N = 196 in the crossover marked ours.
14. The 54 rings of 22 October: the look's script reads 736 graphs, not the 672 of its LOG line.
15. The cheapest decisive steps put first (Sec. 9), with the deficit-object test recorded as a proposal of ours.

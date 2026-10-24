# Two papers read in full: a compact U(1) field on a geometry that changes (24 October 2026)

*Reading note for `docs/design/u1_rewiring_graph_brief_2026-10-24.md` (decisions 0 to 4). Kinds of statement as in
CLAUDE.md rule 10: **published** (with a quotation and its section or equation number, from the paper's own text),
**ours, exact** (arithmetic), **ours, unverified** (a reading or inference by the assistant). This note does not repeat
the searches or summaries of `2026-10-24_prior_work_gauge_on_dynamical_graphs.md` or
`2026-10-24_prior_work_u1_curl_mass.md`; it supplies what those notes had only at abstract level.*

**Date read:** 2026-10-24 (`date`: Sat Oct 24 19:28 EDT 2026). **Who:** one assistant agent. **How:** both PDFs
downloaded from arxiv.org and converted to text locally with PyMuPDF; the text was read end to end and searched.
Quotations below are from that conversion (ligatures restored, mathematical layout flattened); equation numbers are the
papers' own. Figures were not looked at as images, only their captions and the text describing them.

---

## Paper 1. Renken, Catterall and Kogut (1993/1994): U(1) gauge fields on 3D dynamical triangulations

### Bibliographic data

- **The full paper (read):** R. L. Renken, S. M. Catterall and J. B. Kogut, "Three-Dimensional Quantum Gravity Coupled to
  Gauge Fields", arXiv:hep-lat/9304016 (submitted 27 April 1993; preprint numbers ILL-(TH)-93-7, DAMTP-93-15); published
  as Nucl. Phys. B422 (1994) 677-689 (journal reference from the arXiv listing and a search summary; the journal version
  itself was not seen). 16 pages.
- **The proceedings version (the one cited in the record):** R. L. Renken, S. M. Catterall and J. B. Kogut, "U(1) lattice
  gauge theory coupled to quantum gravity", Nucl. Phys. B (Proc. Suppl.) 34 (1994) 730-732, Lattice '93 (Dallas),
  doi:10.1016/0920-5632(94)90496-0. **No arXiv version found**: the INSPIRE record lists no e-print (INSPIRE API
  queried 2026-10-24), and a web search for the title found only hep-lat/9304016.

### Read status

- hep-lat/9304016: **read in full** (text of all 16 pages; the figures themselves not seen).
- The proceedings paper: **abstract only** (the Elsevier abstract as carried by INSPIRE: "Using the dynamical
  triangulation approach, a method of coupling lattice gauge fields to quantum gravity is presented. As a specific
  example, U(1) gauge fields and three dimensions are chosen. In this case, no new non-trivial continuum limits are
  found."). *Ours, unverified:* it reads as a three-page summary of hep-lat/9304016; whether it adds anything is not
  known.

### Summary in plain English

Terms first. A **dynamical triangulation** is a model of space as a pile of identical tetrahedra glued face to face,
where the gluing pattern is the thing summed over, as the toy's wiring is. Its two couplings are a cost per point (α,
which at fixed volume acts like Newton's constant, because more points at the same volume means different curvature)
and a reward per tetrahedron (β, the cosmological constant, which sets the size). Without matter, 3D dynamical
triangulations have two phases, a "crumpled" one where a few points touch everything (negative curvature) and an
extended one, and the change between them is first order, so it has no continuum limit of interest.

The authors put a compact U(1) phase (an angle) on every **edge** of the triangulation, with the energy on every
**triangle** (the triangle is the elementary loop, the plaquette). They hoped the extra coupling would turn the
gravitational transition into one with a continuum limit. They worked out (i) a quenched mean-field theory (the field
on a frozen geometry), (ii) exact relations between the full model and pure gravity at zero and at very large gauge
coupling, which say the field only shifts the gravitational couplings, and (iii) Monte Carlo moves that change the
geometry and the field together, in which the new edge's phase is integrated out exactly when deciding whether to make
the move. They found: the gravitational transition stays where the shift predicts; no gauge (confinement) transition at
all, though mean-field theory predicts one; the gauge sector looks strongly coupled everywhere; no new continuum limit.

### The action and how the field couples to the geometry

Pure gravity, Eq. (1): "S = αN0 − βN3 ... where N0 is the number of nodes and N3 is the number of tetrahedra (i.e. the
volume). β is therefore the cosmological constant while α acts like Newton's constant, since at fixed volume varying the
number of nodes varies the curvature." (Their sign convention: the weight is e^S.)

With the field, Eq. (2): "S = αN0 − βN3 + λ Σ_Δ cos φ_Δ, where the sum is over all triangles and φ is the sum of gauge
angles about the given triangle." So the gauge coupling is λ (not β, which is the cosmological constant here), the field
is the plain Wilson form with **no "−1"**, and the geometry enters only through which triangles exist. Every plaquette is
a triangle, all of one size, as every plaquette in the toy is a square.

### The zero of the plaquette energy, and how integrating out shifts the geometry's couplings (decision 0)

Two exact limits, quoted. Zero coupling, Eqs. (7)-(8): "Note that (using N1 = N0 + N3) Π_links ∫_0^{2π} dθ = (2π)^N1 =
e^{N1 ln 2π} = e^{(N0+N3) ln 2π} so that Z(α, β, λ = 0) = Z_pure grav(α + ln 2π, β − ln 2π) implying that the
gravitational transition is shifted to α* ∼ 1.91 − 2.16." *(Ours, exact: with weight e^S and S containing −βN3, the
factor e^{N3 ln 2π} gives −(β − ln 2π)N3, so the printed signs are consistent.)*

Large coupling, Eqs. (9)-(10): "For very large λ the theory also approaches a pure gravity theory. In this limit, (since
N2 = 2N3) Σ_Δ λ cos(φ_Δ) ∼ λN2 = 2λN3 implying Z(α, β, λ) ∼ Z_pure grav(α, β − 2λ) (λ such that cos φ_Δ ∼ 1). This final
equation suggests that the gravitational transition is only weakly dependent on λ."

So in this paper the field renormalises the geometry's couplings through two separate constants: the **measure** of each
edge's angle (2π per edge, which shifts both α and β because the number of edges is tied to N0 and N3), and the
**constant part of the plaquette energy** (λ per triangle when the field is ordered, which shifts the cosmological
constant because N2 = 2N3). Because they use cos φ with no "−1", every triangle is rewarded at strong order; with
(cos φ − 1) the large-λ shift would vanish (ours, exact, from Eq. (9)). The mean-field free energy per edge is also
written down, Eq. (4): "u(H) = ln I0(H) where I0 is a modified Bessel function", the same Bessel function the toy's
character expansion gives per square.

### Monte Carlo moves when both the geometry and the field change (decision 1)

The geometry moves are the (2,3)/(3,2) and (1,4)/(4,1) moves. The key step, Sec. "Detailed Balance": "here all the
relations are modified. First, consider the (2,3) move. Here, it is necessary to assign a value for the gauge field on a
potential new link." Detailed balance, Eq. (11): "½ (1/N3) (1/(4·2)) e^{S_A} P(A → θ) = ½ (1/l3) e^{S_θ} P(θ → A)". Then
the method:

"The acceptance rate can be increased by integrating over the possible values of θ so that it is first decided whether to
update the triangulation or not and then later the gauge field values are determined. Integrating over all possible
values of θ and assuming that P(θ → A) can be chosen independent of θ gives (l3/2N3) P(A → B) = P(B → A) ∫_0^{2π}
e^{S_θ − S_A} dθ" (Eq. (12)), with I23 the integral (Eq. (13)), "(which will turn out to be a gauge invariant function of
the loops on the surface of the cluster of the two or three tetrahedra under consideration)". Acceptance, Eqs.
(15)-(16): P(A → B) = I23/(R23 + I23), P(B → A) = R23/(R23 + I23), with R23 = l3/2N3 (Eq. (14)).

"These update probabilities tell us whether to put in or take out a link and whether to put in or take out a node. They
do not indicate what the gauge degrees of freedom should be. This is taken care of by a subsequent Metropolis or heat
bath step."

The integral is done in closed form. For the (2,3) move, Eqs. (22)-(28): S_θ − S_A = −β + λ(t1 + t2 + t3 − t0), where
t_i are the cosines round the three new triangles and the one removed; t1 + t2 + t3 = r cos(θ + ω), so "I23 = 2π
I0(λr) e^{−β−λt0}" (Eq. (28)), with r² = 3 + 2(cos z1 + cos z2 + cos z3) (Eq. (30)), "Since each of the zi is a gauge
loop, r is manifestly gauge invariant." For the (1,4) move four new angles are integrated by the character expansion
(Eq. (38): e^{SΘ−SA} = e^{α−3β} Π_{i=1}^{6} Σ_{k_i} I_{k_i}(λ) e^{i k_i p_i}); the integrals impose δ-functions (Eq. (40)),
"a consequence of gauge invariance under transformations at the center node", leaving a triple sum of products of six
Bessel functions times phases of three gauge-invariant loops on the tetrahedron's surface (Eq. (43)).

How detailed balance is kept, in one line (ours, unverified): the move is decided on the **marginal** weight of the
geometry with the new edges' phases integrated out, and the phases of an edge that is removed are simply forgotten,
which is consistent because the reverse acceptance was made independent of θ. The field on the edges that remain is
carried unchanged.

A practical number, Sec. "Results": the ratio r of gauge sweeps to geometry sweeps mattered: "As r is varied from 1 to
16, the values of all of these quantities change, but reach a plateau near r = 8 ... The expectation value of the
plaquette ... varying from 0.62 to 0.67 as r varies from 1 to 16, but varying by less than a part per thousand as r is
increased from 8 to 16. r = 8 is the value we used."

### What was measured and found

- Mean field (Eq. (6)) gives "a first order transition at λ* = 0.794 in the negative curvature phase and λ* = (1 + 1/c) ∗
  0.794 in the positive curvature phase", but they warn that on a fixed 3D lattice "Mean field theory mistakes a crossover
  for a phase transition."
- **The geometry's transition did not move beyond the predicted shift.** With ⟨N0⟩ ∼ N3^δ (Eq. (44)), at λ = 2 and volumes
  2000 to 16000: "δ for α = 1.6, α = 1.8, and α = 2.1 ... are 0.55(1), 0.84(2), and 1.007(1) ... the trend is consistent
  with a gravitational transition still in the region α = 1.91 − 2.16 of the λ = 0 transition." They note the fits were
  poor and larger lattices are needed.
- **No gauge transition.** The gauge specific heat has "a maximum ... in the region predicted by mean field theory, but
  there is no sharp peak, it does not grow with volume, and there is no evidence for critical slowing down ... This
  suggests that the gauge sector is in a strong coupling phase for all λ." Monopole density 1/3 at λ = 0, falling
  smoothly, always below percolation.
- Conclusion: "No appropriate phase transition was found in the space of actions we considered."
- On 2D, Introduction: "In two–dimensions, the analogous system is topological — quantum gravity has no interesting
  effect [8]" (ref. [8] Wheater 1989, 1991; not read by us).

---

## Paper 2. Candido, Clemente, D'Elia and Rottoli (2020/2021): compact gauge fields on 2D causal dynamical triangulations

### Bibliographic data

A. Candido, G. Clemente, M. D'Elia and F. Rottoli, "Compact Gauge Fields on Causal Dynamical Triangulations: a 2D case
study", arXiv:2010.15714 [hep-lat] (v1, 29 October 2020); JHEP 04 (2021) 184 (journal reference as recorded in the
earlier note; the journal version not seen). 13 pages in the arXiv version read.

### Read status

**Read in full** (arXiv v1 text, all pages including Appendix A; figures known only from captions and text). Supersedes
the earlier note's caveat that its strong-coupling formula came from an ar5iv summary: the formula is quoted from the
paper below.

### Summary in plain English

**Causal dynamical triangulations (CDT)** are dynamical triangulations with a time slicing imposed: space is built slice
by slice, each slice a ring of edges, the slices joined by triangles. In 2D, curvature integrates to a topological
constant, so the only coupling is a cosmological one, λ, a cost per triangle; the volume diverges as λ falls to λ_c =
log 2. The authors put a compact U(1) or SU(2) field on the links of the **dual graph** (one link between each pair of
neighbouring triangles), so the plaquettes are the loops round each vertex of the triangulation, of varying length n_b
(6 where space is locally flat). They wrote moves that change the triangulation and the field together, ran them on a
torus, and found that the field **only shifts λ_c**, by an amount a strong-coupling estimate predicts for β ≲ 1, while
the critical exponents do not change. The geometry does change the field: topological freezing (the field getting stuck
in one winding sector) is reduced by orders of magnitude, and they trace that to the geometry being uneven rather than
to its moving.

### The action and how the field couples to the geometry

Gravity, Eq. (4): "S_CDT,2D[T] = λN2[T], where N2[T] is the number of triangles in the triangulation T (i.e., the total
volume), and λ is the only free parameter, which is related to the cosmological constant."

Gauge field, Eq. (6): "S_YM ≡ −β Σ_{b∈T^(d−2)} Π̃_b / n_b, where we use the shorthand Π̃_b ≡ [(1/N) ReTr Π_b − 1]". The
division by n_b is argued in Sec. II.B: "an action which is given as a sum over bones, as the plaquette action in our
case, must include a factor n_b for each bone. Since F²_µν comes out of the plaquette with a n²_b factor attached, it is
necessary to divide by n_b the contribution from each plaquette." Where the field sits, Sec. I: "elementary parallel
transports ... are naturally associated with the links of the dual graph"; they note the alternative (links on the
triangulation's own edges, as in Ambjørn and Ipsen 2013) "is left open only in two dimensions".

### The zero of the plaquette energy, and how integrating out shifts λ_c (decision 0)

Their plaquette term carries the **"−1"**: Π̃_b = (1/N) ReTr Π_b − 1, so an untwisted plaquette costs nothing and a random
one costs β/n_b. The strong-coupling estimate, Sec. IV.B: "for β → 0 gauge links are randomly distributed and the
plaquette averages to zero. Therefore, taking into account that by the Gauss-Bonnet theorem triangulations have zero
average curvature, i.e. ⟨n_b⟩ = 6, the typical action of a gauge configuration is expected to be approximately βN0/6 =
βN2/12. That can be seen as an effective shift of the λ parameter to λ̃ ≃ (λ + β/12), so that the critical threshold is
expected to move to λ̃_c = log(2) ⟹ λ_c^(G)(β) = log(2) − β/12."

Measured, same section: at β = 1 (U(1)), "λ_c^(G) = 0.6068(1), µ = 0.357(7)" from ⟨V⟩ and "λ_c^(G) = 0.6064(2), ν =
0.53(3)" from the correlation length; log 2 − 1/12 = 0.6098 (ours, exact), so the measured shift at β = 1 is about 4 %
larger than the estimate. Fig. 7 compares log 2 − λ_c(β) with the estimate over β from 0.01 to 100, "which seems to work
perfectly until β ≲ 1." Exponents, Fig. 8: "appear to be independent of β in the whole range, suggesting that the only
effects of the gauge fields on gravity observables consist in a shift of λ_c ... µ = 0.363(3) (χ²/dof = 9/9) and ν =
0.496(7) (χ²/dof = 9.1/9)."

Why, in their words: "two-dimensional gauge fields can be easily integrated away: after a proper gauge fixing which
freezes spatial dual gauge links, one is left with a theory of plaquettes and the path integral over them can be
performed. Nevertheless, on a curved geometry one is left with a non-trivial contribution to the remaining path-integral,
depending on the coordination numbers n_b: according to our numerical results, such contribution seems to be irrelevant,
at least for what concerns the critical properties of the system."

So here, with the "−1" zero, the field is a **penalty per unit of volume** and raises the effective cosmological
constant (fewer triangles favoured at a given λ), the opposite sign from paper 1's large-coupling shift, which with no
"−1" is a reward per triangle. *Ours, unverified:* the estimate keeps only the first-order term; integrating each
plaquette exactly would give a weight e^{−β/n_b} I0(β/n_b) per plaquette (for U(1), ignoring the global constraint on a
closed surface), whose next term, +(β/n_b)²/4, is a small reward and plausibly part of why the estimate fails above β ≈ 1.

### Monte Carlo moves when both the geometry and the field change (decision 1)

Three kinds of move (Sec. III; detailed balance in Appendix A, standard Metropolis-Hastings, Eqs. (A2)-(A3)).

1. **Pure gauge move:** heat bath on one link, Eq. (7), "P(U′_l)dU′_l ∝ dU′_l exp((β/N) Re Tr[U′_l F†_l])", with the force
   F_l = Σ_{b∋l} X_b^(l)/n_b built from the staples.
2. **The (2,2) flip, the move that rewires at fixed volume — phases carried, not redrawn.** "in both the initial and the
   final configurations we can always set the value of the central link equal to the group identity 1 ∈ G. That permits
   to easily identify the final gauge configuration apart from an irrelevant gauge transformation" (Sec. III.2). Appendix
   A.1: "the gauge fixing of the central dual link variable to the group identity 1 ensures that this move, involving a
   flip of a time-like link, does not change the values of the plaquettes but only their lengths"; the field part of the
   acceptance is then only the change of the 1/n_b weights, Eq. (A4), and "the selection probabilities of the initial and
   final gauge configuration Φ and Φ′ are trivially equal ... because, given the gauge fixing, the selection procedure is
   deterministic in both directions." Acceptance, Eq. (A5): A(2,2) = min{1, e^{−ΔS_YM} P_sel,CDT[T]/P_sel,CDT[T′]}.
3. **The (2,4)/(4,2) moves, which create or destroy a plaquette — new phase drawn by heat bath, its normalisation in the
   acceptance.** "gauge transformations can set to the identity 1 at most three out of four links of the central plaquette
   Π′_0, shifting all the physical content in the remaining one ... the (2, 4) move must involve the extraction of a new
   link variable U′" (Sec. III.3). Appendix A.2: the action change splits into a part depending on U′,
   −(β/N) ReTr[U′F†] (Eq. (A8a)), and a part independent of it (Eq. (A8b)), with "F ≡ 1/4 + X2/n2"; U′ is drawn from the
   heat-bath distribution Eq. (A9), dU′ exp((β/N) ReTr[U′F†]) / Z_G(F), Eq. (A10); then "since the initial configuration
   has a unique gauge equivalence class, the gauge part of the ratio of selection probabilities turns out to be exactly
   equal to Eq. (A9)", giving Eq. (A11a): A(2,4) = min{1, [P_sel,CDT(T)/P_sel,CDT(T′)] e^{−2λ − ΔŜ} Z_G(F)}, and the
   inverse (A11b) with 1/Z_G(F). For U(1), Eq. (A12): "Z_U(1)(F) = I0(2 det(J))", J ≡ F/(2g²N) as printed. *(Ours,
   unverified: for U(1) one expects I0(β|F|); the printed form with det(J) and g² is their notation and was not checked
   further.)*
4. Their check on correctness: "we have performed a series of preliminary debugging runs in which the moves have been
   combined with different weights, in order to check for the correctness of each single move by verifying the stability
   of various average observables, like the average volume or the average plaquette, against the change in the weights."

### What was measured and found

- Gravity: λ_c(β) shifted as above; exponents unchanged, ν compatible with ½ ("a mean field behavior which could explain
  why the local fluctuations of n_b are not relevant").
- Field: topological charge Q (Eq. (10)) unfreezes. "the increase is at least exponential in the static case and becomes
  prohibitive for β ≳ 50, while it is orders of magnitudes smaller and at most exponential in the dynamical case." The
  switch-off experiment (Fig. 11) "clearly demonstrates that most of the improvement comes from the non-flatness of the
  geometry", and "vertices with a large negative curvature (large n_b) represents large holes in the lattice where
  fluctuations can happen more easily".
- Topological susceptibility in a "(wrong) continuum limit" at fixed λ: βχ_Q = 0.0758(14), "in agreement with the
  analytical prediction for the flat continuum theory [31], which, taking into account the additional factor 6 in our
  definition of β, is βχ_Q = 3/(4π²)".
- Torelons (Polyakov-like loops wrapping the torus, Eq. (11)) measured as gauge correlations; Fig. 14 shows their
  correlation length changing with λ at β = 70: "the coupling to gravity has a non-trivial effect on gauge field
  dynamics". Torelons are observables only, not terms in the action (consistent with the earlier note).

---

## What the two papers supply to the toy's brief

**Decision 0 (the zero of a square's energy).** Both papers face it, and they chose opposite zeros:
paper 1 uses λ Σ cos φ (no "−1"; Eq. (2)), paper 2 uses β Σ (cos φ − 1)/n_b (Eq. (6)). Neither argues for its choice as
physics; paper 2's "−1" is the usual flat-lattice convention (their Eq. (2)), paper 1's is the plain Wilson weight. In
both, the constant part of the plaquette energy is read, explicitly, as a **shift of the cosmological constant**
(paper 1, Eqs. (9)-(10): β → β − 2λ; paper 2: λ → λ + β/12). This is the published confirmation of the audit's point
in VISION Update 102: the direction of the field's effect on the geometry is set by where the zero sits, and the
literature does not settle it, it states it. *Ours, unverified:* what makes the choice matter in the toy, and not in
paper 1, is that the toy's square count is not tied to N: in paper 1 N2 = 2N3 exactly, so the constant only rescales a
coupling the model already has; in paper 2 the constant multiplies N0/6 = N2/12 on average; in the toy it multiplies
S, which differs between the tube and the sheet, so it moves the curling cost, not a cosmological constant. The
brief's λ_eff formula is the toy's analogue of paper 2's λ_c(β) = log 2 − β/12, and paper 2's Fig. 7 is the model for
how to test it: a leading-order shift checked against measured critical values over a range of β, with the expected
failure of the leading order above β ≈ 1.

Two further points for decision 0 (ours, exact unless marked). (i) Paper 1's other shift, the measure ln 2π per edge
(Eqs. (7)-(8)), is **absent in the toy**: a switch keeps the number of links at 2N, so the measure is a constant and
drops out of every acceptance. Only the per-square constant matters. (ii) At large β under the "−1" zero the per-square
constant vanishes and what is left is the fluctuation entropy of the field; *ours, unverified:* in a Gaussian
approximation that is about −(rank B / 2) ln(β/2π), with rank B = P − dim null(Bᵀ), which the brief's counts give as
80 − 16 = 64 for the 4 × 16 tube and 64 − 1 = 63 for the 8 × 8 sheet at N = 64, a difference of one mode. So under the
"−1" zero the field's preference between tube and sheet would be tiny at large β, whereas under the Wilson zero it grows
like β per extra square. That makes the two zeros easy to tell apart in a run, and it is worth adding to the brief's
exact step 1 (to be checked by the exact Z_U1, not taken from this estimate).

**Decision 1 (how a phase rides a switch).** Both papers show a working, published fourth option that the brief does not
list, and both use it for the moves that create links or plaquettes:

- **(d) Draw the new phases by heat bath from their local conditional distribution, and put the normalisation of that
  distribution into the geometry move's acceptance** (paper 1: integrate the new edge's angle exactly, Eqs. (12)-(16),
  (28), (43), then a separate heat-bath or Metropolis step; paper 2: draw U′ from Eq. (A9) and accept with Z_G(F),
  Eq. (A11)). Removed links' phases are forgotten; the field on every link not touched is carried unchanged. This sits
  between the brief's (a) and (c): exact detailed balance like (a), but with the acceptance of (c) computed locally
  (only the squares through the new links), so no global Z_U1(G) is needed. *Ours, unverified:* for the toy's switch, two
  links are removed and two made, and the squares through them change; the local integral is then over two angles, a
  short character sum like paper 1's Eq. (43), and the reverse move needs the matching integral over the two removed
  links. The brief's claim that (a) satisfies detailed balance with plain Metropolis is right but, as paper 1 notes for
  its own case, integrating the new phases raises the acceptance.
- **The brief's option (b), phases carried with the wiring, has a published precedent in paper 2's (2,2) flip**: gauge-fix
  the flipped link to the identity in both states, so every plaquette keeps its holonomy and only the plaquette
  weights change (Eqs. (A4)-(A5)), with a deterministic, symmetric field part of the proposal. *Ours, unverified:* this
  works there because the flip changes the lengths of the four plaquettes round it but creates and destroys none; a
  switch in the toy creates and destroys squares, so a fully carried field is not available for every switch, and (b)
  can apply at most to squares that survive the switch. A mixed rule (carry what survives, heat-bath what is new) is
  what paper 2 does across its two kinds of move.
- Paper 1's gauge-to-geometry sweep ratio (plateau near r = 8, Sec. "Results") is a method parameter to report and
  scan in the toy, and paper 2's check (vary the move weights, look for stable averages) is a cheap correctness test to
  add beside the rule-6 tests.

**Decision 2 (β fixed or tied to g).** Neither paper ties the gauge coupling to a temperature of the geometry: both treat
it as an independent bare coupling and scan it (paper 1: λ from 0 into the strong-coupling region at fixed α; paper 2:
β from 0.01 to 100). Nothing here argues for or against β = κ/g; it is a choice for the owner.

**Decision 3 (first observable).** Both papers' headline test is the one the brief proposes in kind: does the field shift
where the geometry's transition sits, and does it change its character? Paper 2's answer in 2D is "shift only, by the
leading-order amount at small β"; paper 1's in 3D is "no move beyond the predicted shift, and no new transition". The
brief's test (a) (the tube's waiting time against a known Arrhenius baseline) is the toy's version of paper 2's Fig. 7;
paper 2 also suggests a second observable for free: the field's own winding or topological charge, whose autocorrelation
fell by orders of magnitude on a fluctuating geometry.

**Decision 4 (four links or six).** Paper 1's remark that the 2D gauge-plus-gravity system is "topological" and paper 2's
"two-dimensional gauge fields can be easily integrated away" both say that in two dimensions the field's effect reduces to
a weight per plaquette. *Ours, unverified:* this supports the brief's plan to start with four links, where the exact
character expansion (Gate U1) is available and the surface terms of the brief's item 3 are the only correction; the
caveat is that the tube's extra closed surfaces (null space of Bᵀ of dimension 16 against 1) are exactly what makes the
toy's four-link case not purely "a weight per square", unlike a 2D triangulation of fixed topology.

## Where they differ from the toy

- **Where the field sits and what a plaquette is.** Paper 1: angles on the triangulation's edges, plaquettes are triangles
  (all length 3). Paper 2: angles on the dual graph, plaquettes are loops round vertices of varying length n_b, with a
  1/n_b weight. The toy: angles on the graph's own links, plaquettes are 4-cycles (all length 4), so no n_b factor is
  needed, which is closer to paper 1.
- **Volume varies; the toy's does not.** Both papers work at variable volume (grand canonical in paper 1, tuned by λ in
  paper 2), and their geometry moves change the number of simplices. The toy has fixed N and fixed link count; only the
  number of squares S varies with the wiring. The field's constant therefore cannot be absorbed into an existing coupling
  as it is in both papers (ours, exact, from N2 = 2N3 in paper 1 and from the toy's H = 16(N − S) + 4λX).
- **No curled direction, no square count as an order parameter.** Paper 2's torus is flat on average by Gauss-Bonnet;
  paper 1's sphere has no compact direction. Neither looks at a decompactification, and neither has the toy's
  over-full-edge term X. Wrapping loops (torelons) are observables in paper 2, never in the action; in the toy the tube's
  side-4 ring is itself a square in the action, which is where the brief's effect comes from.
- **Geometry's own couplings and phases.** Paper 1's geometry has a first-order crumpled-to-extended transition; paper 2's
  2D CDT has one critical point in λ. The toy's tube-to-sheet change is the decay of a stuck state at fixed coupling, not
  a phase transition in their sense, so their "shift of a critical value" maps onto a shift of a curling cost and a
  waiting time, not onto a critical point (ours, unverified).
- **Results not to be imported.** Neither paper's numbers (λ* = 0.794; λ_c(1) = 0.6068; ν = 0.496) transfer to the toy;
  only the methods (local integration of new phases, gauge-fixed carrying, leading-order shift checked against measured
  values) and the statement that the zero of the plaquette energy is a convention that sets the sign of the shift.

## Sources

- arXiv:hep-lat/9304016, https://arxiv.org/abs/hep-lat/9304016 (PDF read).
- Nucl. Phys. B Proc. Suppl. 34 (1994) 730, doi:10.1016/0920-5632(94)90496-0; INSPIRE record (abstract only).
- arXiv:2010.15714, https://arxiv.org/abs/2010.15714 (PDF read).

# Defects, curvature and "they must balance": reading notes (26 October 2026)

**Why this note.** VISION Update 105 (25 October) records the owner's hard rule: the toy keeps the total of curl and
anticurl ("uncurl" in that update) at zero, which at six links is S = 3N exactly. Her reading (Update 127): curl and
anticurl always come in pairs; a curled X that opens must carry anticurl equal to its curl; "breakage" (points with
more open directions than flat space, where most anticurl sits in the push look) may be more opening, space bent the
wrong way. A reviewer pointed to disclinations, dislocations and the combinatorial Gauss-Bonnet theorem: on a torus,
positive and negative curvature defects must balance. O156 already cautions that "Gauss-Bonnet needs an embedding"
and Update 105 (as corrected after O156) says the rule "fixes a count of squares, not a curvature integral". This note
reads the defect literature the reviewer named, says what it does and does not license, and proposes exact checks.

**How it was read, and the caveat on every quotation.** Read by an assistant agent on 26 October 2026. Unlike the
25 October notes, the main sources were **downloaded as arXiv PDFs and converted to plain text** (PyMuPDF), and the
agent read and searched that text directly; no summarizing model stands between the text and the quotations below.
The conversion mangles formulas (subscripts, sums and fractions come out flattened), so formulas are rebuilt here by
the agent from the extracted text; the words are verbatim. Section and equation numbers are those of the arXiv
versions; the journal versions may number differently. **Check against the journal PDFs before anything reaches a
paper.** The owner has not read any of these passages.

## Sources and how each was read

| Key | Source | How read, 26 October 2026 |
|---|---|---|
| [BG09] | M. J. Bowick, L. Giomi, "Two-dimensional matter: order, curvature and defects", *Adv. Phys.* **58**, 449–563 (2009), arXiv:0812.3064, DOI 10.1080/00018730903043166 (checked at Crossref) | **Read in part** (arXiv PDF text, 102 pages): abstract; Sec. 2 (2.1 to 2.4) in full; Sec. 3.3.1 to 3.3.2 opening; Sec. 3.4 (scar density, square-lattice scars, Eq. (102)); Sec. 3.5.1; Sec. 4.3 (Gaussian bump) in part; Sec. 4.4 opening; Sec. 5.2 (torus curvature, Eq. (169)); Secs. 5.5.1 and 5.5.2 in part; Sec. 6 opening. Not read: Secs. 1.3, 3.2, 3.6, 4.2, 4.5, 5.3, 5.4, 5.5.3 except by keyword search |
| [BNT00] | M. J. Bowick, D. R. Nelson, A. Travesset, "Interacting topological defects on frozen topographies", *Phys. Rev. B* **62**, 8738 (2000), arXiv:cond-mat/9911379 (reference as printed in [BG09], ref. 73; not checked at Crossref) | **Read in part** (arXiv PDF text: abstract and Sec. 1, pp. 1–5) |
| [CN93] | C. Carraro, D. R. Nelson, "Grain boundary buckling and spin glass models of disorder in membranes", arXiv:cond-mat/9307008 (submitted to *Phys. Rev. E* per its first page; journal reference not checked) | **Read in part** (arXiv PDF text: abstract and Sec. I, pp. 1–4) |
| [SN88] | H. S. Seung, D. R. Nelson, "Defects in flexible membranes with crystalline order", *Phys. Rev. A* **38**, 1005–1018 (1988), DOI 10.1103/PhysRevA.38.1005 (checked at Crossref) | **Abstract only**, from the Princeton research portal page (APS page refused access, 403; Crossref and Semantic Scholar carry no abstract) |
| [HN78] | B. I. Halperin, D. R. Nelson, "Theory of two-dimensional melting", *Phys. Rev. Lett.* **41**, 121–124 (1978), DOI 10.1103/PhysRevLett.41.121 (checked at Crossref) | **Not reached** (APS page 403; no abstract in Crossref, Semantic Scholar or PubMed). Known here only through [BG09] Sec. 2.2's mention of KTHNY and [BNT00] Sec. 1 |
| [Nel02] | D. R. Nelson, *Defects and Geometry in Condensed Matter Physics* (Cambridge, 2002) | **Not reached** |
| [Kni12] | O. Knill, "A graph theoretical Gauss-Bonnet-Chern theorem", arXiv:1111.5395 (Knill cites the published form elsewhere as *Elem. Math.* **67**, 1–17 (2012) per [DLF17]'s abstract; not checked at Crossref) | **Read in part** (arXiv PDF text: abstract, Sec. 1, pp. 1–3) |
| [Hig01] | Y. Higuchi, "Combinatorial curvature for planar graphs", *J. Graph Theory* **38**, 220–229 (2001), DOI 10.1002/jgt.10004 (checked at Crossref) | **Abstract only** (from Crossref) |
| [DLF17] | L. De Luca, G. Friesecke, "Crystallization in two dimensions and a discrete Gauss-Bonnet theorem", arXiv:1605.00034, DOI 10.1007/s00332-017-9401-6 (from arXiv; not checked at Crossref) | **Abstract only** |
| [For03] | R. Forman, "Bochner's method for cell complexes and combinatorial Ricci curvature", *Discrete Comput. Geom.* **29**, 323–374 (2003), DOI 10.1007/s00454-002-0743-x (checked at Crossref) | **Not reached** beyond the Crossref record (no abstract there) |

## 1. What exactly "must balance", and on what object

**The statement, for triangulations.** [BG09] Sec. 2.1, from Euler's theorem V − E + F = χ (Eq. (1)) "of any
tessellation of a 2−manifold M", with the topological charge "q_i = 6 − c_i, with c_i the coordination number":

> Q = Σ_{i=1}^{V} q_i = 6χ . (2)

"In the case of a sphere, with χ = 2, Eq. (2) implies any triangulation contains defective sites such that the total
topological charge of the lattice is Q = 12." For the torus, Sec. 5.2, Eq. (169): "The Gauss-Bonnet theorem requires
the total topological charge and the integrated Gaussian curvature to be zero on the torus: Σ_k q_k = ∫ d²x K(x) = 0."

**The general form.** For p-fold order (orientations defined modulo 2π/p), Eq. (3): Q = Σ q_i = pχ ([BG09] Sec. 2.1).
For a square lattice the disclination angle is 2π/4: "In this case the basic disclination has s = 2π/4" (Sec. 3.4).
*Ours, exact arithmetic (the derivation [BG09] gives for triangles, redone for squares):* for a closed surface
tessellated entirely by quadrilaterals, 4F = 2E and Σ_v c_v = 2E, so **Σ_v (4 − c_v) = 4χ**. So "4χ for square
lattices" is right, with charge 4 − c at a vertex of coordination c.

**The object.** In every case it is **a cellular decomposition of a 2-manifold** (an embedded surface in [BG09]'s
physics, but Euler's formula only needs the 2-manifold and its cells): every edge borders exactly two faces. The
discrete ancestor [BG09] names is Descartes' theorem, Eq. (57), Σ_v k(v) = 2πχ, with the angular deficit
k(v) = 2π − Σ α_i(v) (Eq. (56)), "exactly the Gauss-Bonnet theorem for the case in which the Gaussian curvature is
concentrated in a finite number of points (vertices)" (Sec. 2.4).

**On a torus nothing is required.** χ = 0, so the sum is zero, which is satisfied with no defects at all: "on a torus
(χ = 0) a vector field can be defect free" (Sec. 2.1), and Sec. 5.5.1 reviews "the construction of a defect-free
triangulated torus". The constraint is that whatever defects exist **sum** to zero, not that any must exist.

**On a surface that is flat far away, defects come in neutral sets.** For the Gaussian bump (curvature that "dies off
at infinity", Sec. 4.3), the infinite bump has χ = 0, and: "Because the infinite bump has χ = 0 disclinations must
appear in pairs and dislocations must have total Burgers vector zero: Σ_i q_i = Σ_i b_i = 0." This is the closest
sentence in the literature read to the owner's "curl and anticurl always come in pairs". Note the bump itself has
positive curvature at its top and a compensating negative skirt, with ∫ √g K = 0 when unbounded (Sec. 4.3, after
Eq. (130)).

**Graphs without an embedding.** [Kni12] Sec. 1 proves, "For any finite graph G = (V, E) without self-loops and
multiple connections, we have Σ_{p∈V} K(p) = χ(G)", with χ(G) = v₀ − v₁ + v₂ − … counting complete subgraphs
(cliques) and K(p) = 1 + Σ_k (−1)^k V_{k−1}(p)/(k + 1) (Eq. (1)), V_{k−1}(p) counted in the unit sphere of p. It also
quotes Gromov's face-based form K(p) = 1 − Σ_{j∈S(p)} (1/2 − 1/d_j), d_j the sizes of the faces at p. [Hig01]
(abstract) defines a combinatorial curvature for infinite planar graphs "corresponding to the sectional curvature".
*Ours, exact arithmetic:* the toy is bipartite, so it has no triangles and Knill's cliques are only vertices and
links; his K(p) is then 1 − deg(p)/2, which is −2 at every point of a six-link graph, whatever the squares do.
**The clique-based Gauss-Bonnet is blind to the toy's squares.** To see them, the squares must be declared 2-cells
(a square complex), and which 4-cycles count as cells is a choice the toy does not make.

**Three dimensions.** [BG09] is two-dimensional throughout and has no 3D statement. [Kni12] Sec. 1: "In three
dimensions, the Euler curvature form K vanishes identically." *General knowledge, not read here, to verify:* there is
no Gauss-Bonnet constraint on total curvature for a closed 3-manifold (its χ is 0 for any metric, and the
Gauss-Bonnet-Chern integrand exists only in even dimension); in 3D crystals the constraint on disclination lines is a
conservation law (lines close or end on surfaces, and Frank vectors add at junctions), not a fixed total charge; in
Regge calculus curvature sits on edges ("hinges") as a deficit angle. See section 5 for what this gives in the toy's
special case, which is ours.

## 2. Energies: isolated defects against bound pairs

- **An isolated disclination costs area.** [BNT00] Sec. 1: the stress of a disclination "is dominated by σ_φφ"
  (Eq. (1), σ_φφ = K₀s/4π), "This approximately constant stress arises from the stretching of material required to
  close the gap engendered by the missing wedge, and leads to the R² divergence in disclination energy with system size
  R." On the sphere [BG09] Eq. (74) has the disclination interaction energy proportional to πY R²/36 (Sec. 3.3).
- **A dislocation is a bound pair of opposite disclinations**, with logarithmic binding. [BG09] Sec. 4.3: "regarding a
  dislocation as bound pair of disclinations of opposite topological charge"; Sec. 3.4: "dislocations (each regarded as
  a disclination dipole with spacing a)"; Sec. 3.5.1: "dislocations, i.e., 5-7 pairs". [BNT00] Eq. (3): a tightly bound
  dislocation pair has E_pair = 2E_d + (K₀b²/4π) ln(Δr/a) − (K₀b/4π) s Δr, a logarithmic binding plus a Peach-Koehler
  term that tries to "ionize" the pair near a disclination. In flat elasticity the Coulomb picture holds: "Like charged
  particles, disclinations interact via a Coulomb potential, which in two dimensions is proportional to the logarithm of
  the distance in the plane" ([BG09] Sec. 2.3, after Eq. (29), for p-atics; the solid's kernel is biharmonic, Eq. (49)).
- **Neutral composites are cheaper still.** [CN93] Sec. I: the buckling length is "l = R for disclinations, and
  l = √(Rb) for a dislocation", and "This conclusion, however, does not hold for finite energy defects such as
  vacancies, interstitials, or tightly bound dislocation pairs. In this case, l is of order a lattice constant". Its
  abstract: "Unlike the case of isolated dislocations or disclinations, the energy associated with these stresses is
  finite". So the ladder is: one disclination ~R², a dipole (dislocation) ~ln R, a quadrupole (bound dislocation pair)
  finite. *The explicit "dislocation energy ∝ ln R" formula was not found in the passages read; it is standard
  (KTHNY) and follows from [BNT00] Eq. (3)'s logarithmic binding, to verify in [Nel02] or [HN78].*
- **Flexibility changes the bill.** [SN88] abstract: "Disclinations and dislocations eventually exhibit a buckling
  transition with increasing membrane radius. … The critical radius at which buckling starts to screen out internal
  elastic stresses is determined numerically. Computer simulation of buckled defects confirms predictions of the
  disclination energies and gives evidence for a finite dislocation energy."

**Does this support "pairs, and an unpaired curl is costly"?** In elastic matter, yes, and for a stated reason: the
cost of an unpaired defect comes from **long-range elastic strain**, and pairing cancels the far field. *Ours,
unverified, and the main caution of this note:* **the toy has no such strain.** Its energy is a sum over links,
H = 4 × anticurl + 4(λ − 1) × curl (VISION Update 127; ASSUMPTIONS O22: defects sharing no square are exactly additive,
"no long-range force"). An isolated curl in the toy costs 4(λ − 1) wherever it is and however far its partner is.
So the literature's energetic reason for pairing has no counterpart in the toy's energy; in the toy, pairing can only
come from a constraint (her hard rule) or from counting (entropy), not from elasticity. Using [BG09] to argue that the
toy "prefers" pairs would be a borrowed mechanism.

## 3. Which sign is which: cone, saddle, curl, anticurl

**The literature, quoted.** [BG09] Fig. 7: "Examples of 5−fold (left) and 7−fold (right) disclinations on a
triangular lattice in regions of positive and negative Gaussian curvature respectively." With q = 6 − c, a
**deficit** of neighbours (5) is positive charge and sits with **positive** curvature; an **excess** (7) is negative
and sits with **negative** curvature. The deficit angle k(v) = 2π − Σ α_i(v) (Eq. (56)) says the same: more corners
round a point than flat gives a negative deficit. "Disclinations will be attracted to regions of like-sign Gaussian
curvature" (Sec. 2.4). The cone: "no additional defects will appear if the disclination is located on the tip of a
cone with total Gaussian curvature equal to the disclination charge" (Sec. 3.4, before Fig. 18). On the torus "the
Gaussian curvature is therefore positive on the outside of the torus, negative on the inside" (Sec. 5.2), and the
low-energy pattern has "positive (5−fold) disclination on the external equator … and the negative (7−fold)
disclination on the internal equator" (Sec. 5.5.2). *That a free positive disclination buckles into a cone and a
negative one into a saddle is general knowledge, consistent with [SN88]'s abstract but not stated in what was read.*

**Mapping onto the toy** (*ours; arithmetic exact, the reading unverified*). Two readings give **opposite** answers,
which is the point to keep:

- *Excess-around-a-hinge reading.* If the toy's squares are the faces of a cube complex and a link is a hinge, then
  S_e > 4 (curl) means more than four cubes round the link: total dihedral angle above 2π, a **negative** deficit,
  saddle-like, the 7-fold side. S_e < 4 (anticurl) is a **positive** deficit, cone-like. So by the literature's sign
  rule, "curl" would be negative curvature and "anticurl" positive: the reverse of what the words suggest.
- *What curl actually is in the toy's states.* The rod's curl comes from a direction only four links round: its extra
  4-cycles wrap the short direction; they are not faces surrounding a hinge. A 4 × L torus (four links) or a
  4 × 4 × L torus (six links) is **intrinsically flat**: a cylinder has zero Gaussian curvature. So the toy's curl is
  a short circumference, a fact of topology and size, not a disclination of either sign.

So the reviewer's mapping "curl = positive curvature defect, anticurl = negative" is not supported as it stands. The
second reading is what the toy's runs contain; the first would apply only to curl that is a genuine local excess of
cells round a link.

**A sharper exact fact at four links** (*ours, exact arithmetic*). Fill every 4-cycle of a four-link (4-regular) graph
as a square cell. Then V = N, E = 2N, F = S, so χ = S − N, and since Σ_e S_e = 4S,
**Σ_e (S_e − 2) = 4χ**, i.e. curl − anticurl = 4χ of the filled square complex. For any square complex, more
generally, **4χ = Σ_v (4 − deg v) + Σ_e (S_e − 2)**: the vertex term is [BG09]'s square-lattice charge, the edge term
is zero on a closed surface (two faces per edge). In the toy the vertex term is always zero (the graph is regular), so
all of the toy's "Gauss-Bonnet" sits on links, exactly where a surface has none: curl links (S_e = 3) are seams where
three sheets meet, anticurl links (S_e < 2) are boundaries or holes. So at four links **the hard rule S = N is
"χ of the filled square complex is zero"**, a true topological statement about that complex, but the complex is a
surface only if no link is curled or anticurled. That is the precise form of O156's "Gauss-Bonnet needs an embedding".
And if a four-link graph is embedded as a surface with every face of length at least 4 (bipartite forbids odd faces
and simple graphs forbid 2-gons), Σ_f (4 − n_f) = 4χ forces χ ≤ 0, and on a torus every face is a square: there is
no room for a positive, cone-like defect in a regular bipartite square surface at all.

## 4. Screening: does curvature get absorbed by defects?

Yes, centrally. [BG09] Sec. 2.4: "an underlying non-zero Gaussian curvature couples with the defects by screening
their topological charge. As a result, topological defects, whose existence would be energetically suppressed if the
same system was lying on a flat substrate, instead proliferate." Eq. (54)/(55): the energy depends on [η(x) − K(x)],
"identical to the Coulomb energy of a multi-component plasma of charge density η in a background of charge density
−K. Like particles in a plasma, we can expect defects to screen each other's charge, thus forming clusters of zero net
charge, and matching the charge distribution of the surrounding background." Scars: "excess dislocations in the form
of grain boundary scars for spherical crystals above a minimal system size" (abstract); "5-7 pairs, arrayed around an
unpaired 5" (Sec. 3.5.1), appearing once "R/a ≳ 5 − 6" (Sec. 3.5.1). For the square lattice the scars are longer:
"The longer angular length of square lattice scars reflects the larger initial disclination charge (90°) that must be
screened" (Sec. 3.4, Eq. (102), about 0.75 R/a excess dislocations per disclination). [BNT00] Sec. 1: screening by
dislocations costs "an additional term in the energy which diverges linearly with system size R, as compared to the
R² divergence associated with an unscreened disclination." Shape change is the other screen: "if the geometry of the
substrate is allowed to change … the substrate itself changes shape in order to accommodate some preferential in-plane
order. The latter is the fundamental mechanism behind the buckling of crystalline membranes [Seung and Nelson]"
([BG09] Sec. 2.4). And defect proliferation on curvature is read as heating: it "suggests an interpretation of the
curvature as a local effective temperature" (Sec. 4.3).

*Ours, unverified:* "breakage absorbs curvature" has a literal ancestor here (scars and proliferated dislocations
absorb curvature that the lattice cannot otherwise accommodate), and the 4.3 remark that curvature acts like a local
temperature matches the push look, where broken points are also simply where the energy went. But in the literature
what is screened is a **long-range stress**, and screening lowers an energy that would otherwise grow with size; the
toy has no long-range stress to screen (section 2), so a screening reading of breakage needs a different mechanism
(counting) or the hard rule, and is not inherited.

## 5. What this suggests for a rule-obeying X, and the exact checks

**What the literature would draw** (*ours, unverified*). A curled region carried by a flat surround with zero total
charge is the Gaussian bump of [BG09] Sec. 4.3: positive curvature at the top, a compensating negative skirt,
∫K = 0, with any defects in neutral sets ("disclinations must appear in pairs"); or the Dunlap torus of Sec. 5.5.1
("an equal number of pentagonal and heptagonal disclinations", each 7 inside matched with a 5 outside). That is
Update 83's "curl inside a larger uncurl" (as corrected in Update 92), now with a picture: a cap and a ring of
opposite sign around it, or a scar. **But** by section 3 the toy's curl is a short circumference, not a cap, and a
cap of the cone kind cannot even be built in a regular bipartite square surface; so the analogy needs a translation
the literature does not supply, and the checks below are what would supply or refute it.

**The gap, stated once.** The toy's S_e counts all 4-cycles through a link in an abstract graph. The theorems read
here count faces of a cellular 2-manifold (or cliques of a graph, which the toy lacks). They apply to the toy only
after a choice of which 4-cycles are cells, and they say something about curvature only when the resulting complex is
a manifold. Nothing read shows that the toy's curl is curvature in the geometric sense.

**Exact checks, cheap, on saved states and on any X built under the hard rule** (*ours; proposed, none run*):

1. **Face or wrap-around.** Classify every 4-cycle: a face of a 3-cube subgraph (contractible, local) or not
   (wrapping a short direction). Report curl and anticurl separately for the two classes. If the rod's curl is all
   wrap-around, section 3's second reading holds and the cone/saddle analogy does not apply to it.
2. **Manifold test at six links.** Fill 4-cycles as squares and 3-cube subgraphs as cubes (C of them). Check at each
   link whether S_e equals the number of cubes round it, and whether the cells round each link form one cycle
   (manifold) or branch. *Ours, exact arithmetic:* for a closed cube 3-manifold whose vertex graph is 6-regular and
   whose every 4-cycle is a face, F = 3C, E = 3V and χ = V − E + F − C = 0 give C = V and hence
   Σ_e (S_e − 4) = 4F − 4E = 0, i.e. **S = 3N follows**. So her hard rule holds automatically for such complexes; it is
   a real constraint only for states that are not 6-regular closed cube manifolds. Equivalently, under the rule,
   χ(filled complex) = N − C, so check whether C = N.
3. **Local neutrality, not only the total.** For each point and radius r, compute Q(r) = Σ (S_e − 4) over links in
   the ball of radius r. The plasma picture of [BG09] Eq. (54) predicts |Q(r)| small beyond a screening length; a
   total of zero with large uncancelled lobes is not that picture. Compare with the same statistic for shuffled
   positions (chance), and say in advance what "small" means.
4. **Pairs in place.** For each curl link, the distance to the nearest anticurl link, against chance. (Update 127, as
   corrected by O159, found the test weak on the push-look states because nearly all links were near a broken point;
   on an X built under the rule it would have power.)
5. **Vertex charge.** At six links the graph is regular, so the analogue of the 5/7 coordination charge is identically
   zero; any "disclination" in the toy must be read from cells, which is why checks 1 and 2 come first.

## What it does not say

- Nothing read gives a Gauss-Bonnet theorem for an abstract graph's 4-cycle counts, or for a bipartite graph at all;
  the clique version is blind to squares, and the face versions need a chosen cell structure and a manifold.
- Nothing read gives a total-charge constraint in three dimensions; [Kni12] says his 3D curvature form vanishes
  identically, and the 3D disclination-line conservation law is general knowledge, not read.
- The literature's case that unpaired defects are costly rests on long-range elasticity, which the toy's per-link
  energy does not have. It does not support "an unpaired curl is costly" in the toy.
- It does not say that a curled (short) direction is a positive-curvature defect. A cylinder is flat; on the hinge
  reading, excess cells round a link is negative curvature, the opposite of the naive mapping.
- It does not say that breakage is "more opening". It says curvature can be absorbed by proliferating defects and that
  curvature acts like a local temperature; which of those, if either, the toy's broken points are is untested.
- [HN78], [Nel02] and [For03] were not reached; [SN88], [Hig01] and [DLF17] are abstract only. The cone and saddle
  shapes of buckled disclinations are general knowledge here, not quoted.

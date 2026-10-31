# Reading note: a continuous quantity carrying a whole-number invariant (Lk = Tw + Wr; Dirac's charge quantization)

A reading note on the template `prior_work_template.md`, adapted: its "where was searched" table and its read-status
discipline are kept; its verdict section is replaced by "What bears on the owner's rules", because this note backs no
"we have not found" sentence. No tracked file other than this note was changed; `REFERENCES.bib` is untouched (proposed
entries are at the end).

Kinds of statement (rule 10): **published** (with how much of the source was read), **exact** (arithmetic, ours),
**ours, unverified** (an interpretation or mapping onto the toy). "General knowledge, to verify" marks a statement from
memory, not checked at a source in this session.

**Date of the reading:** 2026-10-27, 22:17 EDT by `date` at the time of writing. The file name carries 2026-10-28, as
the task that asked for it named it.

**Who read:** one assistant agent (Claude), with no checking agent. The owner has read none of the sources below.

**Relation to the earlier note.** `2026-10-23_twist_on_a_graph.md` (section 1) already read Fuller 1971 in full,
Dennis and Hannay 2005 in full, White 1969 in part, and Călugăreanu 1961 only at its title page (it says "the formula's
page not located"). **New here:** (a) Călugăreanu's own formula, located and read from the page images (pp. 614, 616,
622, 624, 625); (b) the Möbius-band form of the relation (Denne and Larsen 2023); (c) the cubic-lattice writhe as a
quarter-sum of four linking numbers, and the lattice-ribbon result (Dagrosa, Owczarek and Prellberg; Laing and Sumners
abstract); (d) Dirac 1931 read directly; (e) one paragraph each on flux quantization and on the Z_N / lattice form,
from open sources.

## Where was searched

| Source | Terms used | Results looked at | Nearest hit |
|---|---|---|---|
| Web search (session tool) | Dennis Hannay "Geometry of Călugăreanu's theorem"; Möbius band linking number half-integer Lk = Tw + Wr; writhe of a self-avoiding polygon cubic lattice four pushoffs; Dagrosa Owczarek "Generalizing ribbons and the twist of the lattice ribbon"; Călugăreanu 1961 dml.cz; Dirac 1931 "Quantised singularities" pdf; Deaver Fairbank 1961 | 7 queries, about 9 links each | the sources in the table below |
| arXiv (PDF downloaded, converted with `pdftotext`, searched by term) | math-ph/0503012; 2208.03239; math-ph/0507039; 1410.6012; physics/0308003; 1411.5815 | 6 papers | as below |
| arXiv API (author and title search) | au:Dagrosa; ti:writhe AND ti:lattices | 3 Dagrosa records; Dagrosa and Owczarek 2014 is not on arXiv | |
| Publisher and repository pages | PNAS (403); PMC and Europe PMC (Fuller 1971 and 1978: abstracts read; PDFs behind a bot check); dml.cz (Călugăreanu 1961 scan, no text layer: pages rendered to images and read); royalsocietypublishing.org (403; the publisher's own PDF of Dirac 1931, stamped "Downloaded from royalsocietypublishing.org on 08 May 2024", read from a Westlake University course page); IOP abstract page (Laing and Sumners 2006); a Temple University course copy of Deaver and Fairbank 1961; a QMUL author page (Dagrosa et al. 2015, 2017 journal versions) | about 12 pages | |
| Crossref API | DOIs of Dirac 1931, Wegner 1971, Deaver and Fairbank, Doll and Näbauer, Laing and Sumners, Dagrosa and Owczarek 2014 | 7 records | bibliographic data below |
| `REFERENCES.bib` and earlier notes | keys White69, Fuller71, Fuller78, DH05, Calug59, Calug61, JvROSTW93/94, Wil74; notes `2026-10-23_twist_on_a_graph.md`, `2026-10-24_wilson_kogut_lattice_gauge.md`, `2026-10-24_thirds_charge_centre_vortices.md` | read the relevant entries | |
| Not searched | Google Scholar, INSPIRE-HEP (not reachable); Fatula's 2016 University of Maine thesis on Möbius ribbons (its repository has closed and moved; not located) | | |

## Sources and read status

| Proposed key | Source | Read status (this session) |
|---|---|---|
| Calug61 (in bib) | G. Călugăreanu, "Sur les classes d'isotopie des nœuds tridimensionnels et leurs invariants", Czechoslovak Math. J. 11 (4), 588–625 (1961), doi:10.21136/CMJ.1961.100486 | **Read in part**: pp. 614, 615, 616, 622, 623, 624 and the Russian summary p. 625, as page images rendered from the dml.cz scan (no text layer). The rest not read. |
| Calug59 (in bib) | G. Călugăreanu, "L'intégrale de Gauss et l'analyse des nœuds tridimensionnels", Rev. Math. Pures Appl. 4, 5–20 (1959) | **Not read** (cited by the 1961 paper as its ref. [5]). |
| White69 (in bib) | J. H. White, "Self-linking and the Gauss integral in higher dimensions", Amer. J. Math. 91 (3), 693–728 (1969), doi:10.2307/2373348 | **Not read this session** (JSTOR). Read in part on 23 October (see that note). Its content here is only as Dennis and Hannay state it. |
| Fuller71 (in bib) | F. B. Fuller, "The writhing number of a space curve", PNAS 68 (4), 815–819 (1971), doi:10.1073/pnas.68.4.815 | **Abstract only this session** (PMC page; PNAS 403, PMC PDF blocked). Read in full on 23 October from the Caltech repository (see that note); the quotations from its body below are taken from that note, not re-checked. |
| Fuller78 (in bib) | F. B. Fuller, "Decomposition of the linking number of a closed ribbon: a problem from molecular biology", PNAS 75 (8), 3557–3561 (1978), doi:10.1073/pnas.75.8.3557 | **Abstract only** (Europe PMC API). |
| DH05 (in bib) | M. R. Dennis and J. H. Hannay, "Geometry of Călugăreanu's theorem", Proc. R. Soc. A 461, 3245–3254 (2005), doi:10.1098/rspa.2005.1527, arXiv:math-ph/0503012 | **Read in full** (arXiv v2, all 10 pages, as text). |
| DL23 (new) | E. Denne and T. Larsen, "Linking number and folded ribbon unknots", J. Knot Theory Ramifications 32 (1), 2350003 (2023), doi:10.1142/S0218216523500037, arXiv:2208.03239 | **Read in part**: abstract, introduction, Definitions 8 and 14, Lemma 11, Remark 12, Lemma 13, Theorems 15 and 16, Proposition 18's statement (arXiv v1). |
| BS05 (new) | R. Balakrishnan and I. I. Satija, "Gauge-invariant geometry of space curves: application to boundary curves of Möbius-type strips", arXiv:math-ph/0507039 (2005); journal version to verify | **Read in part**: abstract and first two pages (arXiv v1). |
| Sin03 (new) | S. Sinha, "Biopolymer Elasticity", arXiv:physics/0308003 (2003); journal version to verify | **Read in part**: Box 2 ("Link=Twist+Writhe"). |
| DOP15 (new) | E. Dagrosa, A. L. Owczarek and T. Prellberg, "Writhe-induced knotting in a lattice polymer", J. Phys. A 48, 065002 (2015), doi:10.1088/1751-8113/48/6/065002, arXiv:1410.6012 | **Read in part**: abstract, Sec. 1 and 1.1 (the model and the writhe definition, Eqs. 2–4), reference list. |
| DOP17 (new) | E. Dagrosa, A. L. Owczarek and T. Prellberg, "Writhe induced phase transition in unknotted self-avoiding polygons", J. Stat. Mech. (2017) 093206, doi:10.1088/1742-5468/aa85b9, arXiv:1510.07558 | **Read in part**: Sec. 1, pp. 2–3 (journal PDF from the QMUL author page). |
| DO14 (new) | E. Dagrosa and A. L. Owczarek, "Generalizing ribbons and the twist of the lattice ribbon", J. Stat. Phys. 155 (2), 392–417 (2014), doi:10.1007/s10955-014-0941-y | **Not read** (closed; not on arXiv). Its result is known here only through DOP15 p. 2 and DOP17 p. 3. |
| LS06 (new) | C. Laing and D. W. Sumners, "Computing the writhe on lattices", J. Phys. A 39 (14), 3535–3543 (2006), doi:10.1088/0305-4470/39/14/003 | **Abstract only** (IOP page). |
| Dir31 (new) | P. A. M. Dirac, "Quantised singularities in the electromagnetic field", Proc. R. Soc. Lond. A 133, 60–72 (1931), doi:10.1098/rspa.1931.0130 | **Read in part**: §1 (pp. 60–62), the conclusion of §2 (p. 63), §3 in full (pp. 66–68, p. 68 also checked as a page image), the opening of §4 and the closing paragraphs (pp. 71–72) by term search. The publisher's PDF, from a course page. |
| DF61 (new) | B. S. Deaver Jr. and W. M. Fairbank, "Experimental evidence for quantized flux in superconducting cylinders", Phys. Rev. Lett. 7, 43–46 (1961), doi:10.1103/PhysRevLett.7.43 | **Read in part**: first paragraph (p. 43), from a course copy. |
| DN61 (new) | R. Doll and M. Näbauer, "Experimental proof of magnetic flux quantization in a superconducting ring", Phys. Rev. Lett. 7, 51–52 (1961), doi:10.1103/PhysRevLett.7.51 | **Not read** (Crossref record only). |
| Weg71 (new) | F. J. Wegner, "Duality in generalized Ising models and phase transitions without local order parameters", J. Math. Phys. 12, 2259–2272 (1971), doi:10.1063/1.1665530 | **Not read** (Crossref record; its content here only as Wegner's 2014 lecture restates it). |
| Weg14 (new) | F. J. Wegner, "Duality in generalized Ising models", Les Houches lecture notes (2014), arXiv:1411.5815 | **Read in part**: abstract, Sec. 1, Sec. 3 on the dual of the 3D Ising model (Eq. 13 and "Gauge invariance"), the Wilson-loop passage of Sec. 7, Secs. 8 and 9 (Eqs. 71–76), reference list. |
| Wil74 (in bib) | K. G. Wilson, "Confinement of quarks", Phys. Rev. D 10, 2445 (1974) | **Not read this session**; abstract only per `2026-10-24_wilson_kogut_lattice_gauge.md`. |

## 1. Lk = Tw + Wr: the published statements

### Călugăreanu 1961: the integer, and which piece is continuous (published, read in part from page images)

His setting: a knot C, class C³ with non-vanishing curvature, and a neighboring closed curve C* obtained by moving
each point M a small distance ε along a normal direction, at angle Θ(s) from the Frenet frame. His J is the Gauss
double integral of C with itself (the writhe integral, times 4π in Fuller's normalization, *ours, by comparison with
Dennis and Hannay Eq. 3.4*). The key passage, p. 614 (our translation follows each quotation):

- "La courbe C* étant fermée, (1/2π)[Θ(s)]_C est un entier, et il s'en ensuit que
  K = (1/4π) J + (1/2π) ∫_C τ ds est un entier attaché à la courbe C, indépendamment de toute autre courbe voisine."
  ("C* being closed, (1/2π)[Θ(s)]_C is an integer, and it follows that K = ... is an integer attached to the curve C,
  independently of any other neighboring curve.") τ is the torsion.
- "Posons N(C*, C) = (1/2π)[Θ(s)]_C que nous appellerons «nombre de tours relatif» de C* autour de C ... On a alors
  K = G(C, C*) − N(C*, C)." G(C, C*) is the linking coefficient ("coefficient d'enlacement") of C and C*. So, in his
  own symbols: **G = (1/4π)J + (1/2π)∫τ ds + N**, with G and N integers.
- Which term is continuous: "Le premier terme J est visiblement une fonction continue de λ tant que la courbe C_λ ne
  se traverse pas elle-même ... à chaque traversée, l'intégrale (1/4π) J augmente ou diminue de 2 unités ... Le second
  terme (torsion intégrale) n'éprouve aucune discontinuité lorsque C se traverse elle-même, mais fait un saut lorsque,
  pendant la déformation, la torsion τ(s, λ) ne reste pas bornée ... la présence de ce terme dans K assure la propriété
  de cet invariant de ne prendre que des valeurs entières, le premier terme (1/4π) J étant une fonction de ligne qui
  prend des valeurs réelles quelconques" (p. 614). ("The first term J is visibly a continuous function of λ as long as
  the curve does not pass through itself ... at each passage the integral (1/4π)J rises or falls by 2 units ... The
  second term (integrated torsion) has no discontinuity when C passes through itself, but jumps when the torsion
  becomes unbounded ... the presence of this term in K ensures that the invariant takes only whole values, the first
  term (1/4π)J being a line function taking arbitrary real values.")
- The jump, located: p. 616, on deforming a trefoil (K = 3) to a circle (K = 0): "la torsion passe nécessairement par
  un point de discontinuité" (the torsion necessarily passes through a point of discontinuity), the only explanation
  of K passing from 1 to 0 without a self-crossing.
- p. 624, closing: "le coefficient d'enlacement G(C, C*) est donné par K + (1/2π)[ω]_C", and higher-order invariants of
  the same form exist; "Le comportement de ces invariants nous est encore inconnu" (still unknown to us).

### Fuller 1971 and Dennis and Hannay 2005: the modern statement (published)

- **Lk = Tw + Wr** (Dennis and Hannay, Eq. 1.1, p. 1).
- **Lk is an integer, and why:** "Summing the signs (±1) of the crossings gives twice the linking number Lk of the
  ribbon edges ... Since the ribbon is two-sided, the total number of crossings must be even, ensuring that Lk is an
  integer." (DH05, p. 2.) Gauss's formula (DH05 Eq. 3.2):
  Lk = (1/4π) ∮_A ∮_B ds ds′ (a′(s) × b′(s′)) · (a(s) − b(s′)) / |a(s) − b(s′)|³, the degree of the map from the
  torus A × B to the sphere ("the torus 'wrapping around' the sphere an integer number of times", p. 5).
- **Tw is real and framing-dependent:** with the ribbon edge b(s) = a(s) + ε u(s), u ⟂ t,
  Tw = (1/2π) ∮_A ds (t × u) · u′ (DH05 Eq. 2.2); "Tw is local ... and clearly depends on the choice of framing
  (ribbon)" (p. 3). Fuller: "The total twist number need not be an integer" (1971, p. 815, quoted in the 23 October
  note).
- **Wr is real and belongs to the axis curve alone:** Wr = (1/4π) ∮∮ ds ds′ (a′(s) × a′(s′)) · (a(s) − a(s′)) /
  |a(s) − a(s′)|³ (DH05 Eq. 3.4); it is the average over viewing directions of the signed self-crossings of the axis
  (p. 3); the writhe mesh "may cover the direction sphere an integer number of times" plus a partial covering bounded
  by the tangent indicatrix (p. 7), which is why Wr is not an integer in general.
- **Both Tw and Wr are each continuous under smooth deformation of a ribbon that does not pass through itself; Lk is
  constant** (*ours, reading DH05 p. 2 and Călugăreanu p. 614 together*): when the axis passes through itself Wr jumps by
  ±2 and Lk by ±2 with it (Călugăreanu's "2 unités"); Tw never jumps, because it is a local integral.
- **Conditions** (published): a closed, two-sided ribbon ("If the ribbon is a closed loop (with two faces, not one as a
  Möbius band)", DH05 p. 1); narrow (ε small enough that the ribbon does not meet itself, DH05 Eq. 2.1; Fuller's "for
  sufficiently small ε"); u perpendicular to the tangent. Călugăreanu's form via the Frenet frame needs class C³ and
  non-vanishing curvature (White 1969 p. 694, as quoted in the 23 October note); Balakrishnan and Satija: "while Tw and
  Lk change discontinuously by unity whenever the curve develops an inflexion point, Tw_g and Lk_g remain unaffected"
  (BS05 p. 1, about the Frenet-based quantities).
- **A zero-Lk ribbon exists on every curve:** the writhe framing, "the twist of this ribbon compensates its writhe, so
  its linking number is always zero" (DH05 abstract); any other framing's Lk is then the integer
  Lk = (1/2π) ∮ ds arccos(u · u₀) relative to it (DH05 Eq. 4.1, as printed).

### DNA supercoiling (published)

- Fuller 1971 abstract: "For the central curve of a twisted cord the writhing number measures the extent to which
  coiling of the central curve has relieved local twisting of the cord. This study originated in response to
  questions that arise in the study of supercoiled double-stranded DNA rings."
- Fuller 1978 abstract: "A closed duplex DNA molecule relaxed and containing nucleosomes has a different linking number
  from the same molecule relaxed and without nucleosomes ... It is shown that the linking number of a closed ribbon can
  be decomposed into the linking number of a reference ribbon plus a sum of locally determined 'linking differences.'"
- DH05 p. 3: "Repeated local crossings (i.e. a high twist) are energetically unfavourable, whereas nonlocal crossings
  (represented by writhe), where the ribbon repeatedly passes over itself ('supercoiling'), are preferred elastically."
- Sinha 2003, Box 2: "Link Lk counts the number of times that one strand winds around the other. It is an integer and
  clearly a topological quantity and does not change unless you cut and paste the strands ... Both Tw and Wr can change
  so as to keep Lk unchanged."
- *General knowledge, to verify:* in DNA the reference is relaxed B-DNA, Lk₀ ≈ N_bp / 10.5, and supercoiling is
  ΔLk = ΔTw + ΔWr with ΔLk changed only by topoisomerases (which cut strands). Not read at a source in this session.

### Möbius bands (published, read in part)

- DH05 excludes them by construction (two faces), and its integrality argument needs two edges (p. 2, above).
- **Denne and Larsen 2023** define the ribbon linking number as "the linking number between the knot diagram and one
  boundary component of the ribbon" (Definition 8, p. 7; the knot diagram is the ribbon's center line). A Möbius band
  has one boundary component, which runs twice along the core. Remark 12: "When the ribbon is a Möbius band, there is a
  single boundary component and we use all crossings between the ribbon boundary and knot diagram. Thus folds
  contribute ±1 to the ribbon linking number and crossings contribute ±2," against ±½ and ±1 for an annulus.
- **Theorem 15** (p. 11): "(1) Lk(K_w,F) = Tw(K_w,F) + Wr(K_w,F) when K_w,F is a topological annulus, (2) Lk(K_w,F) =
  Tw(K_w,F) + 2Wr(K_w,F) when K_w,F is a Möbius band." Their Tw is "one-half the sum of the crossing values between the
  knot diagram and one boundary component ... computed only at folds" (Definition 14).
- Parity: for unknots whose diagram is a convex n-gon, n odd gives a Möbius band and "the possible ribbon linking
  numbers are ±1, ±3, ±5, ..., ±n" (p. 13, proof of Proposition 18), that is, always odd.
- **Half-integers: not stated in any source read.** *Ours, exact under their convention:* the single boundary is a
  double cover of the core, so dividing their Lk by 2 to compare with an annulus (core against one of two edges) gives
  an odd multiple of ½. Whether some published convention calls this "half-integer linking number" is not settled here.
- Balakrishnan and Satija study the Möbius strip's single boundary curve as a space curve (its own Tw_g, Wr, Lk_g),
  a different object from the band's linking number; not used further.

### Discrete chains and lattice polygons (published, read in part)

- **Cubic lattice, Dagrosa, Owczarek and Prellberg 2015, Eq. (2), p. 3:** "The writhe of a self-avoiding closed curve
  or polygon P [8] on the simple cubic lattice can be expressed as Wr(P) = (1/4) Σ_{j=1}^{4} Lk(P, P + σ_j), where
  P + σ_j is a copy of P translated by a vector σ_j and Lk is the linking number of the two polygons P and P + σ_j. The
  vectors σ_j can be chosen to be σ₁ = (0.5, 0.5, 0.5), σ₂ = (−0.5, 0.5, 0.5), σ₃ = (−0.5, −0.5, 0.5),
  σ₄ = (0.5, −0.5, 0.5)." Their [8] is Laing and Sumners 2006. For open walks they define an integer w as a sum of
  projected crossing counts and state "When the curve is closed then w(P) = 12 Wr(P)" (p. 4).
- *Exact, from that formula (ours):* each Lk is an integer, so **the writhe of a simple-cubic-lattice polygon is a
  multiple of ¼**.
- **Laing and Sumners 2006 abstract:** writhe as "the average of weighted projected writhing numbers of the polygon in a
  few directions. These directions are determined by the lattice geometry, the weights are determined by areas of
  regions on the unit 2-sphere ... We give a new formula for the writhe of polygons on the face centred cubic lattice and
  prove that the writhe of polygons on the body centred cubic lattice, the hexagonal simple lattice, and the diamond
  space group is always a rational number."
- **Lattice ribbons:** "the linking number of a lattice ribbon, which is a lattice version of a double-stranded
  polymer [7], is equal to the writhe of the center line of the ribbon. The center line is a restricted
  three-dimensional self-avoiding walk on the half-integer simple cubic lattice" (DOP15 p. 2, citing Dagrosa and
  Owczarek 2014; DOP17 p. 3 says the same: "the linking number of a lattice ribbon was recently proved to be equal to
  the writhe of the centre line of the lattice ribbon"). *Ours, unverified, and to check against DO14 itself, which was
  not read:* with Lk = Tw + Wr this would make the lattice ribbon's twist zero under DO14's generalized definitions;
  the paper's title ("the twist of the lattice ribbon") suggests that is its subject.

## 2. Dirac 1931: a continuous phase whose change round a loop is a whole number of turns

Read from the publisher's PDF (text layer, with p. 68 checked as an image). Dirac's h is "Planck's constant divided
by 2π" (footnote, p. 62).

- §1 (p. 62): the smallest charge "is known to exist experimentally and to have the value e given approximately by
  hc/e² = 137. (1)" The theory "is found when worked out to give a connection between the smallest electric charge and
  the smallest magnetic pole."
- §2 (p. 63), the starting condition: "The change in phase of a wave function round any closed curve must be the same
  for all the wave functions."
- §3 (pp. 66–67), the integer: "a phase is always undetermined to the extent of an arbitrary integral multiple of 2π
  ... The change in phase round a closed curve may be different for different wave functions by arbitrary multiples of
  2π." For a small loop the change must be small, by continuity, except where the wave function vanishes: "As the wave
  function is complex, its vanishing will require two conditions, so that in general the points at which it vanishes
  will lie along a line. We call such a line a nodal line ... All we shall be able to say is that the change in phase
  will be close to 2πn where n is some integer, positive or negative. This integer will be a characteristic of the
  nodal line."
- Eq. (8), p. 67, for a large loop bounding a surface: change in phase = **2π Σ n + (e/hc) ∫ (H, dS)**, "the summation
  over all nodal lines that pass through it ... a part (e/hc)∫(H, dS) which must be the same for all wave functions and
  a part 2πΣn which may be different for different wave functions."
- p. 68, closed surfaces: "Σn, summed for all nodal lines crossing a closed surface, must be the same for all wave
  functions and must equal −e/2πhc times the total magnetic flux crossing the surface ... the end points of nodal lines
  must be the same for all wave functions. These end points are then points of singularity in the electromagnetic
  field." The flux out of one is 4πμ = 2πnhc/e, so "a magnetic pole of strength μ = ½ nhc/e", with quantum μ₀:
  **hc/eμ₀ = 2 (9)**.
- The charge statement, p. 68: "The theory also requires a quantisation of electric charge, since any charged particle
  moving in the field of a pole of strength μ₀ must have for its charge some integral multiple (positive or negative)
  of e, in order that wave functions describing the motion may exist."
- p. 72: with (1), "μ₀ = 137/2 · e", so like poles would be far more strongly bound than charges.
- Conditions, as Dirac states them: the wave function is continuous ("except in very special circumstances which can be
  disregarded here", p. 66); it is complex (two conditions to vanish, hence lines, not surfaces); the integer lives on a
  nodal line and the quantization of charge follows only if at least one pole exists.
- *General knowledge, to verify:* in today's Gaussian units with ħ written explicitly, Dirac's condition reads
  e g = n ħ c / 2.

**Flux quantization** (one paragraph). Deaver and Fairbank 1961, p. 43: "We have observed experimentally quantized
values of magnetic flux trapped in hollow superconducting cylinders. That such an effect might occur was originally
suggested by London and Onsager, the predicted unit being hc/e. The quantized unit we find experimentally is not hc/e,
but hc/2e within experimental error." Doll and Näbauer 1961 (same volume, p. 51) not read. *General knowledge, to
verify:* the argument is the same single-valuedness of a phase round a loop through the superconductor, and the 2e is
the charge of a Cooper pair; here h is Planck's constant itself.

**The lattice and Z_N form** (one paragraph). Wegner 1971 and Wilson 1974 were not read (Wilson 1974's abstract was
read for the 24 October note). Wegner's own 2014 lecture (arXiv:1411.5815) restates the construction: Ising spins on
the links of a cubic lattice with "the interaction as a product of the spins surrounding an elementary square called
plaquette" (Sec. 3, Eq. 13), which "has a local gauge invariance. Turning all spins around the corner of a cube does not
change the energy of the configuration"; such models have "no local order parameter" (Sec. 7), and "the order appears
in the expectation value of the product of the spins along a loop, called Wilson-loop. It shows in the limit of large
loops an area law at high temperatures and a perimeter law at low temperatures" (Sec. 1). Sec. 8 generalizes to
link variables U_ij in a group ("finite or a continuous group ... Abelian or non-Abelian") with action
g⁻² Σ_plaquettes (1 − (1/N) tr(U_ij U_jk U_kl U_li)) (Eq. 71) and gauge transformations U_ij → G_i U_ij G_j⁻¹
(Eq. 73), and says of the SU(3) case: "Generally the difference between the number of quarks and antiquarks has to be
a multiple of three." Sec. 9: for electromagnetism U_ij = exp(i ∫_j^i A_μ dx^μ) (Eq. 74), the plaquette product being
exp(i a² F_μν) to leading order (Eq. 75). The Z(N) duality paper of Korthals Altes (1978) is cited there and not read.

## What bears on the owner's rules

### What the sources say (published)

1. **In Lk = Tw + Wr the whole number is Lk, not the twist.** Lk is an integer for a closed two-sided ribbon (DH05 p. 2);
   Tw "need not be an integer" (Fuller 1971); Wr takes "arbitrary real values" (Călugăreanu p. 614, of (1/4π)J). Tw
   depends on the framing; Wr on the axis curve only.
2. **What can change the integer:** a strand passing through the other (Lk, Wr jump together by ±2 at an axis
   self-crossing; Călugăreanu p. 614), or cutting (DNA: Sinha, Box 2). Smooth deformation only trades Tw against Wr.
3. **Călugăreanu's own split is three-way:** G = (1/4π)J (real, continuous) + (1/2π)∫τ ds (real, continuous, jumps where
   torsion is unbounded) + N (integer: the turns of the neighbor curve relative to the Frenet frame).
4. **One-sided closures change the formula, not just the values:** Lk = Tw + 2Wr for a Möbius band in Denne and Larsen's
   convention (linking of the core with the single boundary), and that Lk is always odd for their Möbius unknots.
5. **On a lattice the continuous terms become fractions:** on the simple cubic lattice Wr is a quarter-sum of four
   integer linking numbers (DOP15 Eq. 2), and on several other lattices Wr is rational (LS06 abstract). For lattice
   ribbons Lk equals the center line's writhe (DO14, via DOP15 and DOP17).
6. **Dirac:** a continuous phase is single-valued only up to 2π, so the change round a loop is 2πΣn + (continuous flux
   term), with n an integer carried by a nodal line where the amplitude vanishes; a pole's flux is then a whole
   number of quanta, and if one pole exists every charge is a whole multiple of e (pp. 67–68).
7. **Lattice gauge form:** link variables in a group (finite, such as Z_2, or continuous, such as U(1)), plaquette
   products as the curvature, gauge invariance at each vertex, and the loop product (Wilson loop) as the observable
   (Weg14 Secs. 1, 3, 8, 9).

### Our reading (ours, unverified)

- **The mapping "curl continuous, twist discrete" does not line up with Tw and Wr as published.** In the published
  relation both Tw and Wr are continuous and only their sum is whole. If the owner's whole-number "charge round a closed
  loop" is meant to be conserved under the toy's moves, its published counterpart is **Lk** (or Dirac's n), and the
  pair (Tw, Wr) is the counterpart of how a fixed charge is shared between local twisting and the path's shape. On that
  reading, "curl" (extra squares on links, whole turns) and the continuous half would both sit on the Tw/Wr side, and
  the discrete twist would be the Lk side; whether her diagonals' signed steps add up to something that only a cut can
  change is the question a definition on the graph would have to answer (compare the 23 October note, sections 5 to 7).
- **Steps of ½ and ⅓ need care.** The published halves come from one-sidedness (Möbius bands; Denne and Larsen's odd
  Lk) and the published quarters from the cubic lattice's four push-off directions (DOP15). Neither source gives thirds;
  in the sources read, thirds appear only as a group statement (Wegner's SU(3) "multiple of three"; the Z_3 centre,
  `2026-10-24_thirds_charge_centre_vortices.md`). A step of ⅓ in a twist would need a three-fold rotation in the
  framing or a Z_3 link variable; it does not come out of Lk = Tw + Wr by itself.
- **Dirac's structure fits "charge as a whole number of twist round a loop" more closely than CWF does,** with one
  condition the owner's rules would have to meet: Dirac's integer exists because the phase is a continuous angle that
  is undefined somewhere (a nodal line) or on a loop that cannot be shrunk; a variable that takes only N values on each
  link (Z_N) gives a winding only modulo N (general knowledge, to verify). So a twist in steps of ½ or ⅓ summed round
  a loop can give a conserved count modulo 2 or 3, or a whole-number count if each step is a piece of a continuous
  angle; which one the owner means decides what is conserved.
- **The bipartite color as a sign** has a published echo only in the sense that crossing signs and orientation
  conventions fix the sign of Lk and Tw (DH05 p. 2; Denne and Larsen Lemma 11); no source read signs a twist by the
  color of a vertex.
- **What would test it cheaply:** compute, on saved toy states, the sum of the owner's signed diagonal steps round
  closed loops, and check whether the toy's zero-cost moves can change it without a cut (the CWF analogue of "only
  strand passage changes Lk"); and for Möbius closures, whether the sum comes out an odd multiple of ½, as Denne and
  Larsen's parity would suggest.

## Proposed BibTeX entries (not added to `REFERENCES.bib`)

Calug61's note there could be updated to: "read in part (2026-10-27, assistant): pp. 614–616, 622–625 as page images;
p. 614 has K = (1/4π)J + (1/2π)∫τ ds integer and K = G(C, C*) − N(C*, C)".

```bibtex
@article{DL23,
  author  = {Denne, Elizabeth and Larsen, Troy},
  title   = {Linking number and folded ribbon unknots},
  journal = {Journal of Knot Theory and Its Ramifications},
  volume  = {32},
  number  = {1},
  pages   = {2350003},
  year    = {2023},
  doi     = {10.1142/S0218216523500037},
  eprint  = {2208.03239},
  note    = {read in part (2026-10-27, assistant): Defs. 8, 14; Lemma 11; Remark 12; Thms. 15, 16 (arXiv v1). Journal data from the arXiv listing. Lk = Tw + 2Wr for a Moebius band (Thm. 15).}
}

@misc{BS05,
  author  = {Balakrishnan, Radha and Satija, Indubala I.},
  title   = {Gauge-invariant geometry of space curves: application to boundary curves of {M}{\"o}bius-type strips},
  year    = {2005},
  eprint  = {math-ph/0507039},
  note    = {read in part (2026-10-27, assistant): abstract and pp. 1--2. Journal version to verify.}
}

@misc{Sin03,
  author  = {Sinha, Supurna},
  title   = {Biopolymer Elasticity},
  year    = {2003},
  eprint  = {physics/0308003},
  note    = {read in part (2026-10-27, assistant): Box 2, Link = Twist + Writhe for DNA. Journal version to verify.}
}

@article{DOP15,
  author  = {Dagrosa, E. and Owczarek, A. L. and Prellberg, T.},
  title   = {Writhe-induced knotting in a lattice polymer},
  journal = {Journal of Physics A: Mathematical and Theoretical},
  volume  = {48},
  number  = {6},
  pages   = {065002},
  year    = {2015},
  doi     = {10.1088/1751-8113/48/6/065002},
  eprint  = {1410.6012},
  note    = {read in part (2026-10-27, assistant): abstract, Secs. 1, 1.1 (Eqs. 2--4). Cubic-lattice writhe as a quarter-sum of four linking numbers with translated copies.}
}

@article{DOP17,
  author  = {Dagrosa, E. and Owczarek, A. L. and Prellberg, T.},
  title   = {Writhe induced phase transition in unknotted self-avoiding polygons},
  journal = {Journal of Statistical Mechanics: Theory and Experiment},
  pages   = {093206},
  year    = {2017},
  doi     = {10.1088/1742-5468/aa85b9},
  eprint  = {1510.07558},
  note    = {read in part (2026-10-27, assistant): Sec. 1, pp. 2--3. Volume field: the journal numbers by year (2017); to verify.}
}

@article{DO14,
  author  = {Dagrosa, E. and Owczarek, A. L.},
  title   = {Generalizing ribbons and the twist of the lattice ribbon},
  journal = {Journal of Statistical Physics},
  volume  = {155},
  number  = {2},
  pages   = {392--417},
  year    = {2014},
  doi     = {10.1007/s10955-014-0941-y},
  note    = {not read (closed; not on arXiv). Its result (lattice-ribbon Lk equals the center line's writhe) known only via DOP15 p. 2 and DOP17 p. 3. Bibliographic data from Crossref, 2026-10-27.}
}

@article{LS06,
  author  = {Laing, Christian and Sumners, De Witt},
  title   = {Computing the writhe on lattices},
  journal = {Journal of Physics A: Mathematical and General},
  volume  = {39},
  number  = {14},
  pages   = {3535--3543},
  year    = {2006},
  doi     = {10.1088/0305-4470/39/14/003},
  note    = {abstract only (2026-10-27, assistant), IOP page. Bibliographic data from Crossref. Second author's given name as usually written (De Witt); to verify.}
}

@article{Dir31,
  author  = {Dirac, P. A. M.},
  title   = {Quantised singularities in the electromagnetic field},
  journal = {Proceedings of the Royal Society of London. Series A},
  volume  = {133},
  number  = {821},
  pages   = {60--72},
  year    = {1931},
  doi     = {10.1098/rspa.1931.0130},
  note    = {read in part (2026-10-27, assistant): Secs. 1 and 3 in full, end of Sec. 2, closing paragraphs; publisher PDF from a course page. Eq. (8) phase change 2 pi sum n + (e/hc) flux; Eq. (9) hc/(e mu_0) = 2; charge quantization, p. 68. Bibliographic data from Crossref; issue number 821 to verify.}
}

@article{DF61,
  author  = {Deaver, Bascom S., Jr. and Fairbank, William M.},
  title   = {Experimental evidence for quantized flux in superconducting cylinders},
  journal = {Physical Review Letters},
  volume  = {7},
  number  = {2},
  pages   = {43--46},
  year    = {1961},
  doi     = {10.1103/PhysRevLett.7.43},
  note    = {read in part (2026-10-27, assistant): first paragraph. Unit found hc/2e, not hc/e.}
}

@article{DN61,
  author  = {Doll, R. and N{\"a}bauer, M.},
  title   = {Experimental proof of magnetic flux quantization in a superconducting ring},
  journal = {Physical Review Letters},
  volume  = {7},
  number  = {2},
  pages   = {51--52},
  year    = {1961},
  doi     = {10.1103/PhysRevLett.7.51},
  note    = {not read. Bibliographic data from Crossref, 2026-10-27.}
}

@article{Weg71,
  author  = {Wegner, Franz J.},
  title   = {Duality in generalized {I}sing models and phase transitions without local order parameters},
  journal = {Journal of Mathematical Physics},
  volume  = {12},
  number  = {10},
  pages   = {2259--2272},
  year    = {1971},
  doi     = {10.1063/1.1665530},
  note    = {not read; content known via Weg14. Bibliographic data from Crossref; issue number to verify.}
}

@misc{Weg14,
  author  = {Wegner, Franz J.},
  title   = {Duality in generalized {I}sing models},
  year    = {2014},
  eprint  = {1411.5815},
  note    = {read in part (2026-10-27, assistant): Secs. 1, 3, 7 (Wilson loop), 8, 9 (Eqs. 71--76). Les Houches lecture notes, August 2014.}
}
```

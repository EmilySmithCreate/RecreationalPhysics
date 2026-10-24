# Prior-work search: can a twist be defined on the toy's graph, and what do the published moves keep?

CLAUDE.md rule 15, on the template `prior_work_template.md`. Reading half of handoff item 2.2
(`docs/HANDOFF_2026-10-23.md`; research task 2 of `docs/HANDOFF_2026-10-22.md`, section 2.2). It settles what the
published mathematics says before any twist is defined on the graph. **It does not draft the definition** (a later
stage does that, into the "Current definitions" box of `docs/design/regge_stage_b_brief.md`, rule 20). The brief, the
box and every other tracked file are untouched by this note.

Kinds of statement (rule 10): **published** (with how much was read), **exact** (arithmetic or enumeration, ours),
**measured** (a registered run), **ours** (interpretation, unverified), **hers** (the owner's). "General knowledge, to
verify" marks a physics or mathematics statement from memory, not checked at a source in this session.

**The sentence it backs.** None is written yet. Two candidates it would back or forbid: (i) the brief's box, which now
says "The twist: not yet defined on the graph. A frame carried round a ring is the twist Tw, which is not conserved
(Lk = Tw + Wr); the conserved count is a linking number, and it needs either an embedding or a framed-graph label"
(`docs/design/regge_stage_b_brief.md`, "Current definitions"); (ii) any future sentence of the form "we have not found
a published twist defined on a square complex whose links may carry three squares". For (i) this note is the reading
behind it, and it holds with two additions. First, a mod-2 twist (the orientation character of a cycle) exists without
any label or embedding, given a named face rule where links carry three squares, and the toy's zero-cost moves already
make it non-zero on cycles of links, and on rings of diagonals, that run once along the tube, never on a ring round the
curl (sections 5 and 6). Second, a lattice torus, flat or curled (the tube is one, with rings of four), carries a
whole-number seam shift once a presentation is named (which seam, which direction), the torsion r of section 7 of
the 20 October note, already on the record as O116's "tube with its seam shifted by two"; it is a count the wiring
fixes, blind to mirror images (section 6(a); candidate D0 in section 7). For (ii) the verdict is UNCLEAR (section 8):
the specific combination was not searched. *Revised 23 October, the same day, after an adversarial check of the draft
definition built on this note: the record's own readings of one-sided end states (ASSUMPTIONS O116, last addendum;
O122; the note to T61's stage-1 reading in PREREGISTRATION) are now cited where facts 4 and 6 discuss them, the seam
shift is added, the lip paragraph of fact 3 reports what the built-graph check found, and the owner's words are quoted
verbatim where a slot summary had stood in quotation marks. Revised again the same day after a second check: the
one-sided end states are counted once (the 5 whole Klein bottles are among the 39; O122's 2 are two of the 5), every
tube family with saved wiring is listed with what has and has not been read of it (section 6(e)), the character is
defined on the band round a cycle and a surface's failure is located by region and not by a search order (fact 3),
the odd-row Klein grids' flip is reported where it sits (fact 4), "a count that only the snap can change" is ours
and not hers (section 6(b)), and a line that read a reading task as a holding of the record is corrected (6(b)).
Where this note cites `sandbox/twist_character_check.py` the statement is a sandbox look (rule 16): exact on the graph
it was computed on, able to narrow a claim and not to support one, until it is promoted to a tested script.*

**Date of the search:** 2026-10-23; revised the same day (rule 17: the date, not the clock).

**Who searched:** an assistant session (Fable), working from the worktree; the owner has read none of the sources
below.

## Where was searched

| Source | Terms used | Results looked at | Nearest hit |
|---|---|---|---|
| Web search (the session's search tool; US results) | "Geometry of Calugareanu's theorem" Dennis Hannay arXiv; Fuller 1971 "The writhing number of a space curve"; Fuller 1978 "Decomposition of the linking number of a closed ribbon"; White 1969 "Self-linking and the Gauss integral in higher dimensions"; Calugareanu 1959 1961 "Sur les classes d'isotopie des noeuds tridimensionnels"; Ellis-Monaghan Moffatt "Twisted duality for embedded graphs" signed rotation system; Bollobás Riordan 2002 "A polynomial of graphs on surfaces"; rotation system edge signature "orientable if and only if" every cycle even number negative edges Gross Tucker; Janse van Rensburg Whittington 1991 "The BFACF algorithm and knotted polygons"; "lattice ribbons" Janse van Rensburg Orlandini Tesi Whittington; "The writhe of a self-avoiding polygon" 1993; Berg Foerster 1981 "Random paths and random surfaces"; Aragão de Carvalho Caracciolo Fröhlich 1983; Lacher Sumners "Data structures and algorithms for computation of topological invariants"; Pachner 1991 "P.L. homeomorphic manifolds are equivalent by elementary shellings"; Lickorish "Simplicial moves on complexes and manifolds" | about 15 queries, 8 to 10 links each | every source named in the task was located; see sections 1 to 4 |
| arXiv (direct download of the PDF, converted to text with PyMuPDF, then searched by term) | math-ph/0503012 (Dennis and Hannay); 0906.5557 (Ellis-Monaghan and Moffatt); math/9911256 (Lickorish); 1011.3847 (Janse van Rensburg and Rechnitzer, which quotes the 1991 ergodicity theorem and cites the BFACF originals); hep-th/0603022 (Bilson-Thompson, Markopoulou and Smolin, for the framed-graph definition) | 5 papers | the four published definitions this note rests on |
| Publisher and repository pages (fetched for bibliographic data and abstracts) | dml.cz (Călugăreanu 1961, full scan); PMC and the Caltech repository (Fuller 1971 and 1978); IOP (Janse van Rensburg and Whittington 1991; the 1993 writhe paper); Edinburgh's copy of White 1969 (JSTOR scan); Lacher's publication page; the Padua repository (lattice ribbons; blocked, 403); in the correction pass of the same day, Crossref DOI metadata and the arXiv API (journal references) | 8 pages; 15 Crossref records, 3 arXiv records | confirmed volumes, pages and DOIs below; AC83's paper is J. Physique 44, 323 (PRB 27, 1635 is another paper) |
| Google Scholar | not used (not reachable from this session's tools) | 0 | |
| INSPIRE-HEP | not used | 0 | |
| Papers citing the closest source (forward citations) | the 2010 BFACF paper's reference list, read; Dennis and Hannay's reference list, read; Ellis-Monaghan and Moffatt's reference list, read (Gross and Tucker 1987 and Mohar and Thomassen 2001 are cited from there) | 3 lists | |
| `REFERENCES.bib` and earlier notes in this folder | keys listed; `2026-10-20_soft_space_prior_work.md` (twisted grids, [LZZ23]); `2026-10-21_matter_as_loops.md` ([BT05], [BTMS07]); VISION Update 92 (the "Named: twist is not the conserved quantity" bullet); the notebook's entries of 21 to 23 October on twist, tape, hypotenuse, diagonal, ring and thirds | all read | none of the keys proposed in section 9 is in `REFERENCES.bib` yet; [BTMS07] is used in the 21 October note without a bib entry |

**Not searched, and it matters for the verdict (section 8):** the literature on twist or orientation on a 2-complex
that is not a surface (where a link carries three faces: "pseudomanifold", "branched surface", "non-manifold
2-complex"), and on moves for quadrangulations rather than triangulations (diagonal rotations and face contractions in
quadrangulations of surfaces; general knowledge, to verify: Nakamoto, J. Graph Theory, 1996); and quadrangulations of
the Klein bottle (Thomassen 1991, recorded in the 20 October note, sec. 7, not read), the published family the toy's
flat Klein grids belong to (fact 4).

## 1. Călugăreanu, White and Fuller: Lk = Tw + Wr

### What each source says (published)

**Fuller 1971** (read in full: the five journal pages, from the Caltech repository's PDF, converted to text; the
right margin of page 816 is cut in the scan and the bracketed words below are reconstructed from context; the figures
were not seen; the "any" on p. 816 and the quotations from p. 817 were checked on 23 October against the PMC page
scans, which are complete). F. B. Fuller, "The writhing number of a space curve", Proc. Natl. Acad. Sci. USA 68 (4), 815 to 819
(April 1971).

- The object is a *strip*: "By a strip (X, U) is meant a smooth curve X together with a smoothly varying unit vector
  U(t) perpendicular to X at each point" (p. 815). Pushing the curve a little way along U gives a second curve X + εU.
- **Lk is an integer and topological.** "Since X and X + εU are disjoint closed curves, their linking number
  Lk(X, X + εU) is defined [11]. For sufficiently small ε the linking number is independent of ε, hence for such ε we
  may call Lk(X, X + εU) the linking number of the strip (X, U). The linking number of (X, U) is an integer
  independent of the direction of travel along X and does not change if (X, U) is deformed smoothly through simple
  closed strips." (p. 815.)
- **Tw is real and depends on the strip.** The twist is the rate at which U turns about the curve: "we call ω₁ the
  twist of the strip at each point of the curve. Define the total twist of the strip (X, U) to be the integral of ω₁
  with respect to arclength over the curve and, in order to obtain a quantity comparable to the linking number,
  define the total twist number Tw(X, U) to be the total twist divided by 2π ... The total twist number need not be
  an integer." (p. 815.)
- **Wr is defined as the difference, and belongs to the curve alone.** "If the curve X is a simple plane curve then
  the linking number Lk(X, X + εU) and the total twist number Tw(X, U) are equal. For a space curve this equality does
  not in general hold. However, it can be verified that for any two strips (X, U) and (X, U*) based on [the] same
  space curve X the equation Lk(X, X + εU) − Tw(X, U) = Lk(X, X + εU*) − Tw(X, U*) holds. [The] difference
  Lk(X, X + εU) − Tw(X, U) is thus a g[eo]metric invariant of the space curve X itself, which [we] call the writhing
  number Wr(X)." Then Eq. (1): "Wr(X) = Lk(X, X + εU) − Tw(X, U)." (pp. 815 to 816.)
- **What changes Wr, and what does not.** "The writhing number is invariant under rigid moti[ons] and dilatations; it
  is independent of the direction [of] travel along X; reflection across a plane changes [the] signs of Wr, Lk and
  Tw." (p. 816.) It is zero for any curve on a sphere: "giving the result that the writhing number of any smooth
  simple closed curve located on a sphere is zero" (p. 816). It is an average of integers: "we may define the
  directional writhing number of X in the direction d by Wr(X, d) = Lk(X, X + εd). The directional writhing number is
  an integer which is unchanged if the direction of travel along X is reversed or if d is replaced by −d" (p. 816),
  and "The writhing number of a space curve X is equal to the average of all its directional writhing numbers, the
  average being taken with respect to area on the unit sphere" (p. 816).
- **The Frenet case.** "If the curvature of X never vanishes, so that the principal normal P is everywhere defined,
  then the twist of the strip (X, P) is the torsion of the curve X [7, 8, 10]" (p. 816). Reference [7] is
  Călugăreanu, [8] Pohl.
- **Why it was wanted.** "This study originated in response to questions that arise in the study of supercoiled
  double-stranded DNA rings" (abstract, p. 815). Section 4 gives the elastic energy of a twisted closed rod as
  E = ½∫₀^ℓ (Aκ² + Cω₁²) dx and notes "When X has zero writhing number Lk(X, X + εU) is the total twist number of the
  rod; for a general closed space curve X the total twist number of the rod is equal to Lk(X, X + εU) − Wr(X)"
  (p. 817).

**Dennis and Hannay 2005** (read in full: arXiv:math-ph/0503012 v2, 10 pages; the journal version is Proc. R. Soc. A
461 (2062), 3245 to 3254, DOI 10.1098/rspa.2005.1527, per the arXiv listing and the Southampton repository). M. R.
Dennis and J. H. Hannay, "Geometry of Călugăreanu's theorem".

- The theorem and its names: "A fundamental result in the geometry of twisted, closed ribbon loops is Călugăreanu's
  theorem (Călugăreanu 1959, 1961; Moffatt & Ricca 1992) (also referred to as White's formula (White 1969; Pohl 1980;
  Kauffman 2001; Eggar 2000), and the Călugăreanu-White-Fuller theorem (Adams 1994; Hoffman et al. 2003), which is
  expressed as Lk = Tw + Wr." (p. 1, Eq. 1.1.)
- **Which term is topological and which are geometric, in one sentence:** "Lk is the topological linking number of
  the two edge curves; it is the classical Gauss linking number of topology ... The theorem states that this
  topological invariant is the sum of two other terms whose proper definitions will be given later and which
  individually depend on geometry rather than topology: the twist Tw is a measure of how much the ribbon is twisted
  about its own axis, and the writhe Wr is a measure of non-planarity (and non-sphericity) of the axis curve." (p. 2.)
- **Tw depends on the framing (the ribbon), Wr does not:** Tw = (1/2π)∫_A ds (t × u)·u̇ (Eq. 2.2, p. 3), and "Tw is
  local in the sense that it is an integral of quantities defined only by s on the curve, and clearly depends on the
  choice of framing (ribbon)" (p. 3).
- **Why Lk is an integer, and what a one-sided ribbon would do to it:** "Summing the signs (±1) of the crossings gives
  twice the linking number Lk of the ribbon edges ... Since the ribbon is two-sided, the total number of crossings must
  be even, ensuring that Lk is an integer." (p. 2.) *Ours:* for a one-sided (Möbius) band there is one edge, not two,
  and this count is not available; that is the mod-2 obstruction of section 2.
- The crossing picture: local crossings (the ribbon seen edge-on) average to twice the twist, nonlocal crossings
  (the axis crossing itself) average to twice the writhe: "The sum of local plus nonlocal crossings is independent of
  the choice of projection direction, and is twice the linking number Lk of the two curves. So, averaging the
  crossings over the direction sphere, Lk = Tw + Wr." (p. 5.)
- A ribbon with zero Lk exists on every curve: "the 'writhe framing' ribbon. By definition, the twist of this ribbon
  compensates its writhe, so its linking number is always zero" (abstract, p. 1).

**White 1969** (read in part: the introduction, pp. 693 to 695, and the start of Appendix B, p. 721, from the
Edinburgh-hosted JSTOR scan converted to text; the theorems of Sections 2 to 10 were only grepped). J. H. White,
"Self-linking and the Gauss integral in higher dimensions", Amer. J. Math. 91 (3), 693 to 728 (July 1969); "This
paper is essentially a dissertation submitted ... at the University of Minnesota, 1968" (p. 693, footnote).

- The origin of the question: "Gauss himself used the integral in his investigation of electromagnetic theory to give
  a formula for the linking number of two space curves ... (If C₁ and C₂ are not disjoint, however, the linking
  number is indeterminate.) In [2] Călugăreanu raised the question of the significance of the Gauss integral for this
  last map" (p. 693, the map from the curve to itself).
- What Călugăreanu found, in White's words: "He found that if C is differentiable of class C³ and has non-vanishing
  curvature then [the Gauss double integral of C with itself plus (1/2π) times the total torsion] is an integer,
  where τ is the torsion. He also worked out a number of geometric interpretations for this integer. In [12] Pohl gave
  a much simplified proof of Călugăreanu's results using the space S(C) of secants of C, and he called the integer SL,
  appropriately, the self-linking number of the curve C." (p. 694; the displayed formula is garbled in the scan and
  the bracketed description is ours, consistent with Fuller's statement that the Frenet strip's twist is the torsion.)
- Its invariance: "Section 10 deals briefly with deformation theory, showing the invariance of the self-linking number
  under non-degenerate isotopy" (p. 695); "Since SL is an integer and since [the integral] varies continuously, SL
  remains an integer and is thus invariant under non-degenerate isotopy" (p. 719).

**Călugăreanu 1961** (read in part: the title page and p. 588, viewed as images; the dml.cz PDF is a scan with no text
layer, so the body was not read and the page of the formula was not located). G. Călugăreanu, "Sur les classes
d'isotopie des noeuds tridimensionnels et leurs invariants", Czechoslovak Math. J. 11 (4), 588 to 625 (1961);
received 22 June 1960; author given as "G. Călugăreanu, Cluj". Its summary (p. 588, in French): "On étudie les classes
d'isotopie des noeuds et leurs approximations par des noeuds algébriques. On construit certains invariants
d'isotopie, exprimés par des intégrales curvilignes dans lesquelles figurent la courbure et la torsion aux points de
la courbe représentant le noeud." **Călugăreanu 1959** (not read; not seen): "L'intégrale de Gauss et l'analyse des
noeuds tridimensionnels", Rev. Math. Pures Appl. (Bucharest) 4, 5 to 20 (1959), as the 1961 paper cites it (per a
search summary quoting that reference) and as Dennis and Hannay cite it. The 1959 paper is in a Romanian journal, not
the Czechoslovak one.

**Fuller 1978** (abstract only, from the PMC page). F. B. Fuller, "Decomposition of the linking number of a closed
ribbon: A problem from molecular biology", Proc. Natl. Acad. Sci. USA 75 (8), 3557 to 3561 (August 1978). "It is
shown that the linking number of a closed ribbon can be decomposed into the linking number of a reference ribbon plus
a sum of locally determined 'linking differences.'" (abstract.) Named here because it is the form Dennis and Hannay
cite for the crossing picture, and because "a reference ribbon plus local differences" is the shape any declared
label on the toy would take (section 6, candidate D3).

### What this settles (ours, from the quotations above)

- **Lk is the topological invariant:** an integer, defined for a *framed* closed curve (a strip or ribbon, in
  3-space), unchanged by any deformation that keeps the strip simple and closed (never passes it through itself).
- **Tw and Wr are geometric and real.** Tw needs the framing and changes with it and with bending; Wr belongs to the
  curve alone, changes continuously as the curve is deformed, is zero for a plane or spherical curve, and flips sign
  under reflection. Both need an actual curve in three-dimensional space; neither is defined on an abstract graph.
- **What changes each:** on a fixed closed curve the twist is fixed by the linking number, Tw = Lk − Wr(X) (Fuller
  p. 817: "for a general closed space curve X the total twist number of the rod is equal to Lk(X, X + εU) − Wr(X)").
  So re-framing changes Tw only when it changes Lk, by the same whole number (the ribbon cut and rejoined with added
  full twists), and never touches Wr; turning the frame continuously changes neither. Bending the curve moves Wr and
  Tw in opposite directions with Lk fixed (the "supercoiling" of DNA; Fuller's section 4; "Once the ends of the rod
  have been joined, deformations of the rod cannot change the linking number Lk", p. 817). Lk changes only when the
  ribbon passes through itself, or is cut and rejoined. *Ours, to verify:* from Fuller's averaging formula, passing
  the axis curve through itself reverses the sign of one crossing in every projection, so Wr jumps by 2; nothing in
  what was read states this in so many words.
- **For the brief's box:** its present sentence is right. "A frame carried round a ring is the twist Tw, which is not
  conserved (Lk = Tw + Wr); the conserved count is a linking number." One addition from section 2: without any
  embedding there is still a *mod-2* twist, the orientation character.

## 2. A twist on an abstract graph with no embedding: ribbon graphs, signed rotation systems, framed graphs

**Ellis-Monaghan and Moffatt** (read in part: the abstract and Sections 1 to 3 of arXiv:0906.5557, the version
titled "Twisted duality for embedded graphs"; the journal version is Trans. Amer. Math. Soc. 364 (3) (2012), 1529 to
1569, per the arXiv journal reference and Crossref). J. A. Ellis-Monaghan and I. Moffatt.

- Four equivalent ways to say "graph in a surface": "We may think of an embedded graph as any of: (a) a cellularly
  embedded graph, that is, a graph embedded in a surface such that every face is a 2-cell; (b) a signed rotation
  system; (c) a ribbon graph, also known as a band decomposition; (d) an arrow presentation." (Section 2.)
- **The signed rotation system is the combinatorial object:** "a signed rotation system consists of an abstract graph
  G, a cyclic ordering of the half-edges at each vertex, and a + or − sign at each edge. Signed rotation systems are
  considered up to equivalence under vertex flips, that is, reversing the cyclic order at a vertex and simultaneously
  reversing the signs on the incident edges (twice in the case of a loop). Under this equivalence, signed rotation
  systems correspond to cellularly embedded graphs." (Section 2; they refer to Mohar and Thomassen [23] for the
  details.)
- **A twisted loop is a loop with a non-orientable neighborhood** (their definition is for a loop, an edge at one
  vertex; reading it for a cycle of several edges, as this note does from here on, is ours, the standard extension;
  general knowledge, to verify at Mohar and Thomassen): "We will say that a loop (i.e. an edge that is incident
  to exactly one vertex) in an embedded graph is non-twisted if a neighbourhood of it is orientable, and we say that
  the loop is twisted otherwise." (Section 2.)
- **The ribbon graph, Definition 2.1:** "a ribbon graph G = (V(G), E(G)) is a (possibly non-orientable) surface with
  boundary, represented as the union of two sets of topological discs: a set V(G) of vertices, and a set E(G) of
  edges such that (1) the vertices and edges intersect in disjoint line segments; (2) each such line segment lies on
  the boundary of precisely one vertex and precisely one edge; (3) every edge contains exactly two such line
  segments." And: "A ribbon graph is orientable if it is orientable as a surface."
- **A ribbon graph forgets full twists.** "Two ribbon graphs are said to be equivalent or isomorphic if there is a
  homeomorphism between them that preserves the vertex-edge structure. (In particular, up to this equivalence, the
  embedding of a ribbon graph in three-space is irrelevant.)" (Section 2.) *Ours:* a band with one full twist is
  homeomorphic to a band with none, so the only twist a ribbon graph records on an edge is its parity (the ± sign), a
  half twist or not.
- **The half-twist as a move:** "The half-twist of the ith edge is (τ, i)(G, ℓ) = (H, ℓ) where H is obtained from G
  by reversing the direction of exactly one of the e_i-labelled arrows of the arrow presentation" (Section 3.1);
  "Note that the half-twist operation does not change the number of vertices nor the cyclic order of incident
  half-edges at a vertex in a graph, but the dual operation may change either." (Section 3.1); "τ adds a half-twist
  to the edge e, and δ forms the partial dual at the edge e" (Section 3.2). In the proof of their Proposition 3.11
  (Section 3.3), on a bouquet B of loops: "If ξ_i = τ then ξ(B, ℓ) is non-orientable (as (ξ_i, i)(B, ℓ) is
  non-orientable)"; and, for any embedded graph G: "If G contains a cycle then there exists a set of edges A of G
  such that adding a half-twist to each of the edges in A will change the orientability of G."
- Their references for the standard facts: "J. L. Gross, T. W. Tucker, Topological graph theory, Wiley-interscience
  publication, 1987" and "B. Mohar and C. Thomassen, Graphs on Surfaces, Johns Hopkins University Press, 2001"
  (their [13] and [23]).

**The orientability criterion** (general knowledge, to verify at Gross and Tucker 1987; a search summary of recent
arXiv papers citing that book states it as: an embedding given by a rotation system with edge signatures is
non-orientable exactly when some cycle contains an odd number of negative edges). *Ours:* that is the sense in which
a twist on an abstract graph is "defined only mod 2": the sum of the edge signs round a cycle, modulo 2, is the
cycle's orientation character, invariant under vertex flips; the signs themselves are not invariant.

**Bollobás and Riordan 2002** (not read; cited from Ellis-Monaghan and Moffatt's reference [4] and a search summary).
"A polynomial of graphs on surfaces", Math. Ann. 323 (1), 81 to 96 (2002). Per the search summary: the embedding "can
be specified by providing a sign for each edge and a rotation scheme for the set of half edges at each vertex. A
negatively signed edge corresponds to a ribbon with a half-twist." (summary wording, to verify).

**Framed graphs in a 3-manifold: Bilson-Thompson, Markopoulou and Smolin 2007** (read in part, this session:
Sections I to IV and V.A of arXiv:hep-th/0603022 v2; the 21 October note read other parts). Class. Quantum Grav. 24
(16), 3975 to 3993 (2007), DOI 10.1088/0264-9381/24/16/002, per Crossref (the arXiv journal reference gives 3975 to
3994; to verify at IOP).

- Their states are "the embedding, up to diffeomorphisms, of a framed, or ribbon, graph in a three manifold and in
  which the allowed evolution moves are the standard local exchange and expansion moves [6, 7]" (p. 2).
- "the graphs which comprise the states are framed, so they are represented by the embedding of a two surface in the
  spatial manifold. This is known to be required when the cosmological constant is non-zero [9, 10]" (p. 2).
- The integer twist is a *declared interpretation on an embedded ribbon*: "Twist is interpreted as U(1) charge, so
  that a ±2π twist in a ribbon represents charge ±e/3" (p. 4, Sec. IV).
- What their moves keep: "The braiding content of states in H remains invariant under the action of A_evol. Thus,
  any physical information encoded in the braiding will be conserved under this evolution. As the quantum geometry
  evolves the conserved structure represented by the braiding will not necessarily remain localized with respect to
  the graph." (pp. 3 to 4.) The tool: "Let L[Γ] denote the the [sic] link of a ribbon graph embedding. This is the set
  of curves in Σ obtained by considering each edge of the ribbon graph as a curve in Σ. We define the reduced link of a
  ribbon graph embedding, denoted RL[Γ], to be L[Γ] minus any unlinked unknotted closed curves." (p. 5, Sec. V.A,
  "The reduced link invariant".)

### What this settles (ours)

- **Mod 2 without any embedding:** on a graph embedded in a surface, which is the same thing as a signed rotation
  system, every cycle has an orientation character (annulus or Möbius neighborhood), computable from the combinatorial
  data. Where the toy's square complex is a surface, that data is the complex itself (section 5).
- **An integer twist is not a ribbon-graph quantity.** A ribbon graph is a surface up to homeomorphism, and a full
  twist is invisible to it. To count full twists one needs either (a) an embedding of the ribbon in three-dimensional
  space, where the count is the linking number of the ribbon's two edges (section 1), or (b) a declared label (an
  integer per edge or per cycle) with rules for what each move does to it; (b) is what "framed graph" means in
  Bilson-Thompson, Markopoulou and Smolin, where the embedding in a 3-manifold supplies the integer and the moves are
  chosen so that braiding and twisting are conserved.
- **When a label is needed:** whenever the quantity must be a sign, or a count on a ring (matter against antimatter;
  "A higher twist count holds more curling energy and has more mass, not more charge", hers, 23 October, verbatim).
  The mod-2 character carries neither a sign nor a count; the seam shift of section 6(a) is a count without a label,
  but of a whole flat torus and without a sign.

## 3. Lattice knots, BFACF moves, lattice ribbons and the writhe of lattice polygons

**Janse van Rensburg and Rechnitzer 2010** (read in part: abstract, Sections 1 and 2, the move definitions of
Section 3.1, and the reference list; arXiv:1011.3847). "BFACF-style algorithms for polygons in the body-centered and
face-centered cubic lattices".

- The moves: "The BFACF algorithm [1, 2, 5] is a Metropolis style Monte Carlo algorithm [17] that samples
  self-avoiding walks with fixed endpoints in the grand canonical ensemble in the hypercubic lattice Zᵈ. The
  algoritm uses the local elementary moves in Figure 1" (p. 2); "Moves of type I are positive elementary moves when 2
  edges are added, and negative elementary moves when 2 edges are removed. Moves of type II do not change the length
  of the polygon, and are called neutral elementary moves." (Figure 1 caption, p. 2); "A type I move on the simple
  cubic lattice [is] performed by replacing a single edge incident on an atmospheric plaquette P in the polygon by
  the 3 edges in the alternative path around the boundary of P ... Similarly, a type II move on the cubic lattice
  replaces a pair of edges ... incident on an atmospheric plaquette P with the other two edges in P." (Section 3.1.)
- A lattice polygon is a knot because it sits in space: "A polygon in the simple cubic lattice (SC), or the BCC
  lattice, or the FCC lattice, is a piecewise linear embedding of S into R³. Any such embedding of S is a knot, and
  if the embedding is a lattice polygon, then the embedding is a lattice knot." (Section 2.)
- **The 1991 theorem, as its author restates it:** "Theorem 1 (Thm 3.11 from [16]) The irreducibility classes of the
  BFACF algorithm, when applied to unrooted polygons [in the simple cubic lattice], are the knot types of the polygons
  as piecewise linear embeddings in R³." And why: "for every pair of (oriented) polygons (ω, ν) of the same knot type,
  there exists a finite sequence of elementary moves of either type I or II in Figure 1, such that these moves change
  ω into ν. Each move is a local deformation of the polygon and the ambient space around it, and is itself an
  isotopy." (Section 2.) Their extension: "We prove that the ergodicity classes of these new elementary moves
  coincide with the knot types of unrooted polygons in the BCC and FCC lattices" (abstract).
- Their reference [16]: "Janse van Rensburg E J and Whittington S G 1991 The BFACF Algorithm and Knotted Polygons. J
  Phys A: Math Gen 24 5553-5567"; [8]: "Janse van Rensburg E J 1992 Ergodicity of the BFACF Algorithm in Three
  Dimensions. J Phys A: Math Gen 25 1031-1042"; [1]: "Aragão de Carvalho C and Caracciolo S 1983 A New Monte Carlo
  Approach to the Critical Properties of Self-Avoiding Random Walks. Phys Rev B27 1635-1645" (sic; see the bib entry
  AC83); [2]: "Aragão de
  Carvalho C, Caracciolo S and Fröhlich J 1983 Polymers and g|φ|⁴-theory in Four Dimensions. Nucl Phys B215 [FS7]
  209-248"; [5]: "Berg B and Foester D 1981 Random Paths and Random Surfaces on a Digital Computer. Phys Lett 106B
  323-326" (sic, "Foester"; the search summaries give Foerster).

**Janse van Rensburg and Whittington 1991** (abstract only, from the IOP page; the page is paywalled). "The BFACF
algorithm and knotted polygons", J. Phys. A: Math. Gen. 24 (23), 5553 (to 5567 per the 2010 reference list), DOI
10.1088/0305-4470/24/23/021. Abstract, as the fetch returned it in fragments: "The BFACF algorithm applied to polygons
involves sampling on a Markov chain whose state space is the set of all polygons" ... "In three dimensions, for the
simple cubic lattice" ... "The authors prove that the ergodic classes of this Markov chain are the knot classes of
the polygons." A Padua repository record cites a different 1991 paper by the same authors as "J. Phys. A: Math. Gen.
24 3935"; that is not the BFACF paper (title unknown to us; to verify), and the page 5553 is the one.

**The BFACF originals** (none read; bibliographic data from the 2010 reference list and search summaries, checked at
Crossref on 23 October): Berg and Foerster, Phys. Lett. B 106, 323 to 326 (1981); Aragão de Carvalho and Caracciolo,
J. Physique 44, 323 to 331 (1983) (the 2010 list's "Phys Rev B27 1635-1645" is another paper, Amit, Parisi and
Peliti's; Crossref); Aragão de Carvalho, Caracciolo and Fröhlich, Nucl. Phys. B 215, 209 to 248 (1983).

**Lattice ribbons** (none read; abstracts and search summaries only; the Padua repository blocked the fetch).
Janse van Rensburg, Orlandini, Sumners, Tesi and Whittington, "Lattice ribbons: A model of double-stranded polymers",
Phys. Rev. E 50, R4279 (1994), DOI 10.1103/PhysRevE.50.R4279 (the APS listing confirms the DOI; a Rapid
Communication received 24 August 1994): a ribbon on the simple cubic lattice made of a sequence of plaquettes, open
or closed, with Monte Carlo estimates of its dimensions, the writhe of its backbone, and, for orientable closed
ribbons, the linking number of its two boundary curves (summary wording). The same five authors, "Entanglement
complexity of lattice ribbons", J. Stat. Phys. 85 (1 to 2), 103 to 130 (1996) (from one bibliographic index;
confirmed at Crossref): the centerline and the boundary of a closed ribbon are almost surely knotted as the plaquette count grows,
and for orientable ribbons the expected absolute linking number of the boundary curves grows at least as fast as the
square root of the plaquette count (summary wording). The sampler: Orlandini, Janse van Rensburg and Whittington,
"A Monte Carlo algorithm for lattice ribbons", J. Stat. Phys. 82, 1159 to 1198 (1996) (the 2010 reference list;
not read). *Ours:* the lattice ribbon is the published object closest to "a tape stuck to the cube" (hers,
23 October): a ribbon of plaquettes in Z³, whose twist, writhe and linking number are all read from its embedding;
"orientable closed ribbons" are the ones with two boundary curves, so the summary's restriction is exactly the
two-sided condition of Dennis and Hannay.

**The writhe of lattice polygons.** Janse van Rensburg, Orlandini, Sumners, Tesi and Whittington, "The writhe of a
self-avoiding polygon", J. Phys. A: Math. Gen. 26 (19), L981 to L986 (1993), DOI 10.1088/0305-4470/26/19/002 (abstract only,
IOP page): "We discuss the writhe of a self-avoiding polygon on a lattice, as a geometrical measure of its
entanglement complexity"; then a rigorous result on how |Wr| depends on the number of edges and Monte Carlo estimates
of its distribution, including for trefoils (summary wording). Lacher and Sumners, "Data structures and algorithms
for computation of topological invariants of entanglements: link, twist and writhe", in *Computer Simulation of
Polymers*, ed. R. J. Roe, Prentice Hall, Englewood Cliffs, 1990, pp. 365 to 373 (not read; data from Lacher's own
publication page, which dates the book 1990, not 1991 as the task had it). *General knowledge, to verify:* for a
polygon on the cubic lattice the writhe is computed as an average of linking numbers with a few translated copies
of the polygon (Lacher and Sumners; Laing and Sumners), which is the lattice form of Fuller's directional average.

### What this settles (ours)

- **Knot type is kept by BFACF moves and nothing less is claimed:** the moves are isotopies of an embedded polygon,
  and within a knot type they reach everything (the 1991 theorem). Writhe is a geometric number that the same moves
  change. Linking number between two polygons is kept by moves that never pass one through the other. BFACF moves
  act on polygons, which carry no framing, so they say nothing about a twist; a ribbon's twist and linking number
  under lattice moves belong to the lattice-ribbon sampler (Orlandini, Janse van Rensburg and Whittington 1996, not
  read).
- **All of it lives in Z³ (or the BCC and FCC lattices).** A lattice polygon is a knot *because* it is "a piecewise
  linear embedding of S into R³". The toy's graph has no coordinates once a switch has fired, so none of these
  quantities transfers as they stand (section 6).
- **One exact match worth keeping:** the face diagonals of one kind in the cubic lattice are the nearest-neighbor
  bonds of a face-centered cubic lattice (the 20 October note; VISION Update 92's "one kind's diagonal network is the
  face-centred cubic lattice"). So, on a region that still has its lattice coordinates, a ring of one kind's face
  diagonals is an FCC lattice polygon, and the 2010 paper's Theorem 10 (BFACF-style moves in the FCC lattice have the
  knot types as their ergodicity classes) applies to it. The triangle of three and the 45° square of four are both
  the unknot, so knot type says nothing about her smallest rings; it would matter only for long rings.

## 4. Pachner moves against the toy's switch

**Lickorish 1999** (read in part: Sections 1, 2 and 5, pp. 299 to 303 and 313 to 318; arXiv:math/9911256).
"Simplicial moves on complexes and manifolds", Geometry & Topology Monographs 2 (1999), 299 to 320.

- The setting: "A combinatorial n-manifold is a simplicial complex M such that, for every vertex v of M, lk(v, M) is a
  combinatorial (n − 1)-ball or a combinatorial (n − 1)-sphere." (Definition 2.2.)
- The move: "Suppose that A is an r-simplex in an abstract simplicial complex K and that lk(A, K) = ∂B for some
  (n − r)-simplex B ∉ K. The bistellar move κ(A, B) consists of changing K by removing A ⋆ ∂B and inserting ∂A ⋆ B.
  When n = 2, the three types of bistellar move are shown, for dim A = 2, 1, 0, in Figure 1." (Definition 2.3.)
  *Ours:* for a surface those three are: split a triangle into three (dim A = 2), flip the diagonal of a quadrilateral
  made of two triangles (dim A = 1), and merge three triangles round a point into one (dim A = 0).
- **Pachner's theorem:** "Theorem 5.9 (Newman [9], Pachner [11], [12]) Two closed combinatorial n-manifolds are
  piecewise linearly homeomorphic if and only if they are bistellar equivalent." With boundary: "Theorem 5.10
  (Newman [9], Pachner [12]) Two connected combinatorial n-manifolds with non-empty boundary are piecewise linearly
  homeomorphic if and only if they are related by a sequence of elementary shellings, inverse shellings and a
  simplicial isomorphism."
- Pachner's own paper (not read): U. Pachner, "P.L. homeomorphic manifolds are equivalent by elementary shellings",
  European J. Combin. 12 (2), 129 to 145 (1991), DOI 10.1016/S0195-6698(13)80080-7 (bibliographic data from a search
  summary of the Wikipedia entry and of citing arXiv papers; to verify at Elsevier).

### What this settles (ours; the toy's facts are exact and are stated in section 5)

- A bistellar move is defined on any abstract simplicial complex in which its condition lk(A, K) = ∂B holds
  (Lickorish, p. 302, after Definition 2.3: "Note that the definition is given for abstract complexes"). On a
  combinatorial manifold it swaps one ball, A ⋆ ∂B, for another, ∂A ⋆ B, with the same boundary, so the result is a
  PL-homeomorphic manifold (ours, from the definition). The theorem says such moves are *enough* to connect any two
  triangulations of the same closed manifold. Every link stays in exactly two faces throughout.
- The toy's switch is a different kind of operation. It removes two links and adds two, keeping degrees and the two
  kinds of point; it is not required to keep the square complex a surface (a link may come to carry three squares,
  which is the tube, or one, or none), it changes the number of pieces (shattering into 4-cubes at λ = 0, Gate A;
  O85 in three directions) and the handle count (VISION Update 92, the look of 19 October), and, at zero cost at every
  λ, orientability: one switch takes the 4 × L tube to the reflected closure, whose non-ring squares (the faces the
  eq45 brief's face rule chooses) form a Klein bottle (exact, built graphs; the torus reading of 23 October, sec. 4;
  fact 4 below). So it is not a Pachner move and keeps no topology by theorem. Nothing in Pachner's result bears on
  it except as a contrast: if one wanted a move set on the toy that keeps a surface's topology, the published set to
  copy is the bistellar one on a triangulation (one diagonal per square, which stage B has already chosen, Q27), or
  its quadrangulation analogue (general knowledge, to verify: diagonal rotations in quadrangulations, Nakamoto 1996;
  not searched here).

## 5. The toy's square complex: what is exact (ours; short arguments, no run)

Facts about the four-link toy that the candidates below depend on. Each is arithmetic on the rules in `cqg.py` (the
hard-core rule Q2: two points share at most two neighbors) and could be pinned by a test.

1. **Where every link lies in exactly two squares, the square complex is a surface.** At a point with four links,
   count each square at that point as an edge of a small graph whose four vertices are the point's links (a square
   uses two of them). If every link lies in exactly two squares, every vertex of that small graph has degree 2, so it
   is a union of cycles on four vertices: one 4-cycle, or two 2-cycles. Two 2-cycles would mean two squares on the
   same pair of links a–x, a–y, so x and y would share three neighbors (a and the two far corners), which the
   hard-core rule forbids. So the squares at every such point form one 4-cycle, which is the condition for the
   complex to be a surface there. On the flat lattice torus this holds everywhere and the surface is the torus.
2. **On the tube the complex of all squares is not a surface at any point.** On the 4 × L torus the two links round
   the short way carry three squares each and the two along carry two, so each point carries (3 + 3 + 2 + 2)/2 = 5
   squares (which is the known 1.25 squares per point, VISION Update 7: 4 × 1.25 = 5). Five squares on four links
   cannot form one cycle. Along a three-square link the complex is a "book" with three pages. So neither a rotation
   at a tube point nor an orientation character through it is defined without choosing two of the three pages.
   A face rule repairs it, with no free choice among square faces on the tube: at a tube point the only rotation made
   of four squares is the one through the four between-ring squares (the other two rotations each need the corner
   between the two links along the tube, which closes no square). Dropping the L ring squares leaves 4L faces that
   form a closed orientable surface with V − E + F = 0, the torus (the torus reading of 23 October, sec. 4; fact 4).
   The face rule of the eq45 brief (`docs/design/eq45_ratio_brief.md`, box item 1: at each point, the rotation of four
   corners with the smallest angle sum α; α and the vertex type are [T25] Sec. IV.2's, the point-by-point choice is
   ours) chooses exactly those faces at every point: vertex type (4,4,4,4), no ties, and the ring square is a
   non-contractible cycle, not a face (exact, built graphs: the eq45 brief's Sec. 2, and independent checks at L = 8,
   12 and 16). So once a face rule is named, a rotation at a tube point and an orientation character through it are
   defined, and on the tube the two rules agree.
3. **A diagonal lies in exactly one square** (it joins that square's opposite corners), so a ring of diagonals is a
   chain of squares glued corner to corner, not edge to edge. Whether the squares along the ring make a band (and
   whether that band is an annulus or a Möbius band) is decided at the shared corners, by the rotation there, which
   exists only at surface points (fact 1, or fact 2 under a named face rule). Inside an opened region every point is
   a surface point under each rule named here. At the lip, the boundary between opened points (four squares) and tube
   points (five squares), the all-squares complex is not a surface. Checked on built graphs on 23 October
   (`sandbox/twist_character_check.py`, revised the same day after an adversarial check): the eq45 brief's rule as
   written is silent at such points, because it ties between two rotations of the *same* vertex type, (4,4,4,6), and
   the brief's "ties" counter counts only ties between different types (its 98.1 % was that silence read as a
   failure). Taking every completion of the rule (every tie broken every way, every corner with several shortest
   cycles given each): on the brief's spliced handle (N = 208; 8 tied points, each with one rotation whose corner is
   closed by two equal hexagons, so 3⁸ = 6,561 completions) exactly one closes the whole graph into a surface, and it
   is one-sided because the builder splices both ends the same way, a cross-handle; with one splice mirrored, exactly
   one closes and it is two-sided. Closure of the whole graph is global, so it says nothing about *where* a surface
   fails; the second revision reads the surface by region instead (the local criterion of the draft entry, item 1): a
   completion *closes on a region* when every face inside the region chosen at one of its points is chosen at all of
   them, the region's *band* is its faces inside the region, read as one-sided or two-sided, and a point is a *local
   failure* when no completion closes on the three-step ball round it, which depends on no search order. The character
   of a cycle needs only the band round it (two faces on each link, chosen at both ends), so a defect elsewhere never
   undefines it. By this reading the handle's curled part (its 12 points) and its opened part (180 lattice points)
   each close two-sided and all points together close one-sided as built: the twist is across the lip, in neither part.
   On a hand-built lip (a stretch of tube four around joined at both ends to a stretch of sheet six around through a
   ring with a chord; N = 68 and 96; 16 tied points with six options each, two rotations times three shortest
   hexagons) no completion closes on the whole graph, because every one of those hexagons passes a chord end whose only
   option is four squares; the curled part (the tube and the eight paired joint sheet points) closes with 256 distinct
   bands, all two-sided, the opened part (the sheet interior and the four chord ends) with one, two-sided, and the 32
   local failures (the 4 chord ends, the 8 paired sheet points, the 8 joint tube points and the 12 sheet points of the
   rings beside the joints) all lie on or beside the lip: no surface at the lip, located by the criterion. The lip's
   shape is ours and is not the shape of record: O116's opening product is the tube with its ring seam shifted by two,
   with no closed ring of six beside a closed ring of four, while this graph joins the two through a chord. Whether
   the saved partly opened states' lips look like the splice, the chord or neither is unread.
4. **On every lattice torus the character of every cycle is 0; off the lattice tori it need not be, and such states
   exist under the toy's rules.** A quadrangulated torus is orientable, and the twisted grids T(n, m, r) of the
   20 October note are tori. So every cycle has an annulus neighborhood on a flat lattice torus (all squares as
   faces), and on the tube and the half-turn closure (the tube closed through a half turn of its ring, itself a
   lattice torus; torus reading of 23 October, sec. 6) with the non-ring squares as faces, or the eq45 brief's face
   rule (fact 2). A value of 1 needs a non-orientable square complex, and two are exact on built graphs.
   (i) **The reflected closure** is one switch from the 4 × L tube, at zero cost at every λ (dS = dX = 0; the torus
   reading of 23 October, `sandbox/out/torus_zero_cost_switches_2026-10-23.md`, secs. 3 and 4, from
   `scripts/exact_torus_counting.py`). It is valid (4-regular, bipartite, hard-core) with five squares at every
   point. With the non-ring squares as faces, or under the eq45 brief's face rule (they agree, with no ties), it is a
   closed surface with V − E + F = 0 that cannot be oriented: a Klein bottle (the torus reading at L = 8 to 48;
   pinned by `tests/test_exact_torus_counting.py` at L = 8, 10, 12 and 24). (ii) **The flat Klein grid** is an a × b grid whose rows wrap round and
   whose last row is joined to the first through a reflection. Two families were built: x → −x with b even (6 × 6,
   6 × 8, 8 × 8, 6 × 10, 8 × 12) and x → 1 − x with b odd (6 × 5, 6 × 7, 8 × 5, 8 × 7, 8 × 11, 8 × 13, 10 × 5, 10 × 7,
   12 × 5, 16 × 5). Every one is valid, bipartite, has every link in exactly two squares (S = N, X = 0, H = 0 at every
   λ), and is a Klein bottle with all squares as faces, so no face rule is needed. In the reflected closure and in the
   even family, every ring round the short way keeps character 0; of the straight lines along the long direction, the
   two through the points the reflection fixes have character 1, and each of the others joins two lines the reflection
   swaps into one of twice the length, with character 0. In the odd family the reflection x → 1 − x fixes no column:
   every straight line of links reads 0, and the flip sits on the smooth zigzag of diagonals along the strip the
   reflection maps to itself (between columns 0 and 1, and between a/2 and a/2 + 1), which closes after one pass,
   b faces, and reads 1. A ring of diagonals that runs once along the reflected
   closure and closes through its junction reads 1 too, while the zigzag of diagonals round the curl reads 0 on every
   graph built (section 6(a)). The characters, the eq45 rule's choice on the reflected closure and the Klein grids were
   checked on built graphs by `sandbox/twist_character_check.py` and by two independent scripts outside the repository
   (one of them using `cqg.total_squares`, `cqg.surplus` and `cqg.is_valid` for S, X and validity; the reflected closure
   at L = 8, 12 and 16, the grids at the sizes above); they are not yet pinned by a test. Quadrangulated Klein bottles
   are a published family (Thomassen 1991, as recorded in the 20 October note, sec. 7; not read by us). **The record
   already holds all of this in kind.** ASSUMPTIONS O116, last addendum (11 October; `scripts/read_flat_kind.py`,
   `tests/test_read_shapes.py`), states that a Klein bottle built for the purpose has H = 0 at every λ, so the toy's
   zero-energy states include one-sided ones, and reads the saved flat end states of T8, T23, T24 and T60: of 9,865,
   9,676 are one torus six around, 2 one wider torus, 5 one Klein bottle of 64 points, 182 in two to four pieces, and 39
   contain a one-sided piece of 18 to 64 points, **the 5 whole ones among the 39** (the reader lists every end state
   with any one-sided piece, whole ones included). O122 (the outside reviewer's independent reading) finds 2 Klein
   bottles among T60's 3,521 reached flat end states (3,446 narrow tori, 73 in separate pieces); **they are two of the
   5**, since O116's count covers T60 and O120 records that the two readers give the same three counts for it. The note
   to T61's stage-1 reading (PREREGISTRATION) records a 40-point Klein bottle beside a 56-point torus in one end state
   at λ = 1.40, N = 96; T62's stage-1 reading one end state exactly flat, eight around and one-sided at N = 96 and one
   one-sided at N = 192 with an eighth of its six-loop excess left (μ = 0.10, g = 2.0); T64's reading none. So the chain
   does reach flat Klein bottles, and that was read on 11 October. What this note adds is which cycles carry the flip
   (along; through the reflection's fixed points on the reflected closure and the even-row grids, on a one-pass zigzag
   of diagonals with no fixed point on the odd-row grids; never a ring round the curl on any built example), that the
   reflected closure of O150 is one free move from the tube at every λ, and the odd-row family.
5. **In two directions there is no body diagonal.** The objects are the face diagonal (length √2 on the lattice) and
   the straight two-step line (length 2, the diagonal of the 45° inner square). The four face diagonals round a point
   join its four neighbors into the 45° square of four; its symmetry is four-fold (quarters). The tetrahedron's
   triangle of three, and the three planes 60° apart through a body diagonal (her thirds, exact in the notebook,
   23 October), exist only in three directions. (Notebook, last entry of 23 October; VISION Updates 87 and 90.)

## 6. Answers for the toy

The task's questions (a) to (e), each answered from sections 1 to 5. "Diagonals" here are the added objects of the
brief's exact item 1: a line joining the two same-kind corners of a square.

**(a) Which twist-like quantities are defined intrinsically, with no embedding and no label?**

Two, of different kinds. The first is the **mod-2 orientation character** of a cycle (of links, or of diagonals) in
the square complex, wherever the complex is a surface along the cycle. Where every link lies in two squares it is a surface by itself
(fact 1); where links carry three, only through a named face rule (the eq45 brief's face rule, or dropping the ring
squares, which agree on the tube and its zero-cost neighbors; fact 2). It says whether a band carried round the cycle
comes back flipped (a Möbius neighborhood; "twisted" in the sense Ellis-Monaghan and Moffatt define for loops,
extended to cycles, ours) or not. It is a property of the wiring and the named rule alone. It carries no sign and no
count: a cycle is twisted or it is not. In two directions it is 0 for every cycle on every lattice torus and lattice
patch (fact 4). Off them it is not: the reflected closure, one zero-cost switch from the tube at every λ, and the
flat Klein grids carry cycles of character 1 (fact 4). So a non-orientable state is something the toy's rules allow,
one free move reaches it from the tube, and the chain reaches flat ones: 39 flat end states of T8, T23, T24 and T60
hold a one-sided piece, the 5 whole 64-point Klein bottles among them (O116, last addendum); O122's independent
reading of T60 found 2 Klein bottles, which are two of those 5 (O116's count covers T60, and O120 records that the two
readers give the same three counts for it); T61 adds one 40-point piece beside a torus, T62 one flat one-sided end
state at N = 96 and one one-sided at N = 192 with excess left, and T64 none (fact 4; section 6(e) for the full
inventory). The end states that still hold curled parts, flaws or a lip have not been read for it.

The second is the **seam shift** of a lattice torus, flat or curled (the tube is one, with rings of four): how far
a seam is shifted when the torus closes, read in a named presentation (which seam is the ring, its size and
direction; the other seam the junction), the torsion r of the twisted grids T(n, m, r) (the 20 October note, sec. 7,
citing [LZZ23] and Thomassen 1991, neither read in full). It is a whole number read off the wiring in that
presentation, and it is already on the record:
O116's end state of the opening is "the tube with its seam shifted by two" (four to a ring, a walk round the ring
arriving two steps along; wraps (4, 2) and (0, L)). Checked on built graphs (`sandbox/twist_character_check.py`,
23 October; exact): the 4 × 16 tube with its ring seam shifted by r = 0, 2, 4, 6, 8 gives five pairwise non-isomorphic
valid graphs (r = 0 the tube; r = 2, 4, 6, 8 flat, widths 6, 8, 10, 8), and r = +2 and r = −2 are isomorphic, so the
shift has no absolute sign. The half-turn closure of the tube (O150) is the *other* shift by two: the lattice torus
with wraps (4, 0) and (2, L), the junction seam shifted by two along the ring, which keeps the rings of four and is
isomorphic to neither the tube nor O116's end state; so the whole number depends on which seam is named, and what is
intrinsic is the pair of wraps up to the grid's own symmetries (ours). It is a count, which the mod-2 character misses:
the tube, the half-turn closure and O116's end state are three different graphs on which every cycle reads 0. It is a
property of a whole flat piece, not of a ring or a diagonal, and it carries no sign. Nothing else is intrinsic: Tw and
Wr need a curve in space; Lk needs a two-sided ribbon in space; knot type needs an embedding; a full-twist count on a
ring is invisible to a ribbon graph (section 2).

**(b) Which need a declared label, and what rules the label then needs?**

Any sign, and any count on a ring or a diagonal: a half twist with a direction (clockwise against counterclockwise),
a full twist, her "A higher twist count holds more curling energy and has more mass, not more charge" (23 October,
verbatim) read as a count carried by a ring, thirds and quarters as numbers. (The seam shift of (a) is a count the
wiring fixes without a label, but of a whole flat torus, and it carries no sign.) The published form is the framed graph (Bilson-
Thompson, Markopoulou and Smolin): an integer on each ribbon, interpreted by declaration. On the toy the label would
sit on each diagonal (or on each ring), and the rules it needs before any test are:

- *birth:* the value a diagonal is born with when a switch makes its square (the brief already says "born at a
  declared default length"; a twist label needs the same);
- *death:* what happens to the label when a switch destroys the square: lost, or moved to a named neighbor, or
  forbidden (the move refused);
- *composition:* whether the ring's twist is the sum of its diagonals' labels, and in what group (Z, Z/2, Z/4 for
  quarters, Z/6 for her sixths);
- *the moves that may change it:* the rule "a count that only the snap can change" is ours (paper 18's outline,
  `docs/papers/particles/outline.md`, where it is labelled ours: Sakharov's first condition said plainly; VISION
  Update 85's test (2)), which she quoted and affirmed ("-> yes", notebook, 21 October; VISION Update 90); her own word
  for a count is "twist count" (23 October, verbatim). The published analogue is the braiding content conserved under
  exchange and expansion moves, which works there because the moves are chosen to act on untwisted, unbraided pieces;
  that under those moves braids propagate but do not interact is general knowledge, to verify (reading task 12 of the
  22 October handoff, Hackett 2007, not yet read);
- *a reference:* Fuller 1978's shape, a reference ribbon plus locally determined differences, is what makes a label
  comparable between two states; on the toy the natural reference is the lattice region's own flat framing.

With a label the test "does an opening move carry a twisted diagonal across the lip" becomes bookkeeping of the
declared rules, not a measurement of the toy, and the write-up must say so (rule 13: put in, not derived).

**(c) Which need an embedding in three-dimensional space?**

Tw, Wr and Lk as real and integer numbers (section 1); knot type and the BFACF results (section 3); the lattice
ribbon's twist and linking number (section 3); and **her fractions as angles**: a tape lying flat in one of the
three lattice planes through a body diagonal, 60° apart (a sixth of a turn per segment, her thirds), or in the
planes through a face diagonal (her halves and quarters), are statements about planes in the cubic embedding. Stage
B's lengths do not supply this: lengths on links and diagonals are intrinsic (Regge) and fix angles inside each
triangle, but not how the complex sits in space; a Möbius band and an annulus can carry the same lengths. The
lattice coordinates exist only on regions that no switch has touched; the toy drops them at the first switch.

**(d) What the literature says is kept by which moves**

| Quantity | Kept by | Changed by | Source |
|---|---|---|---|
| Lk of a two-sided ribbon | any deformation through simple closed strips (never passing through itself) | the ribbon passing through itself; cutting it and rejoining with added full twists | Fuller 1971 pp. 815, 817; Dennis and Hannay p. 2 |
| Tw | on a fixed closed curve, every framing with the same Lk (Tw = Lk − Wr) | bending the curve (traded against Wr at fixed Lk); a re-framing that changes Lk, by the same whole number | Fuller 1971 pp. 815 to 817; Dennis and Hannay p. 3 |
| Wr | rigid motions, dilatations | any bending of the curve; sign under reflection | Fuller 1971 p. 816 |
| Self-linking SL (Frenet framing) | non-degenerate isotopy | isotopies through zero curvature (not read in detail) | White 1969 pp. 694 to 695, 719 |
| Orientation character of a cycle (mod 2) | vertex flips; any move keeping the band | a half-twist τ on one edge of the cycle (from the edge-sign criterion, general knowledge, to verify at Gross and Tucker; Ellis-Monaghan and Moffatt state the graph-level form, proof of Prop. 3.11 (2)) | Ellis-Monaghan and Moffatt, Sections 2 and 3.1 to 3.3 |
| Seam shift of a lattice torus, flat or curled (the torsion r), in a named presentation; intrinsic only as the pair of wraps up to the grid's symmetries | nothing among the toy's moves is known to keep it: the opening changes the ring seam's shift from 0 (the tube) to 2 (O116's end state), and every seam link changes between them; +r and −r are one graph | the switch | O116; the 20 October note sec. 7 ([LZZ23]; Thomassen 1991, not read); `sandbox/twist_character_check.py` (built graphs, 23 October; a sandbox look, not yet pinned by a test) |
| Knot type of a lattice polygon in Z³, BCC, FCC | BFACF type I and II moves (isotopies); within a knot type they reach everything | passing a strand through another (not a BFACF move) | Janse van Rensburg and Whittington 1991 Thm 3.11, as restated in the 2010 paper; the 2010 paper's Theorems 6 and 10 |
| Writhe of a lattice polygon | nothing: geometric | BFACF moves | Janse van Rensburg et al. 1993 (abstract) |
| Twist or Lk of a lattice ribbon | not addressed by BFACF (polygons carry no framing) | — | Orlandini, Janse van Rensburg and Whittington 1996 (not read) |
| PL type of a closed combinatorial manifold | bistellar (Pachner) moves | nothing among them; they are complete | Lickorish Thm 5.9 (Pachner 1991) |
| Braiding and twisting content of a framed graph in a 3-manifold | the exchange and expansion moves (noiseless subsystem) | moves that cut through a braid (not allowed there) | Bilson-Thompson, Markopoulou and Smolin pp. 3 to 5 |
| The toy's square count, surplus count, pieces, handles, surface-ness, orientability (tube to reflected closure, zero cost) | not kept by the switch in general; energy is conserved sealed | the switch | the record (Gate A; O85; Update 92; Q12); the torus reading of 23 October and fact 4 |

**(e) What this means for the exact test the handoff names: "whether any opening move carries a twisted diagonal
across the lip", now on the tube's saved end states in two directions**

- *What exists to test on, and what the record has read already.* Every two-direction tube family with saved wiring,
  by directory name (names and file counts only; nothing opened): `results/t8_*_adj` (8 directories, 960 end
  states), `t23_*_adj` (28; 3,360), `t24_*_adj` (28; 3,360) and `t60_*_adj` (35; 4,200), together the 11,880 of O116
  (`.npz` files with `adj` and `part`, 120 per cell at N = 64 to 288; read by `scripts/exact_exchange_sign.py` and
  `scripts/read_flat_kind.py`); `t7d_lam125_n{64,96,144,192a,192b}_adj` (5; 12 decays); `t37_*_adj` (34; 340 long
  tubes that seeded themselves, up to 1,024 points); `t38_*_adj` (48; 10,000 waiting-time replicas); `t51_*_adj`
  (91; 600 cooled sheets, O107's knots); `t61_*_adj` (14; 720); `t62_*_adj` (30; 720); `t63_*_adj` (10; 240);
  `t64_*_adj` (15; 360). **Read for one-sidedness** (exploratory readings, exact per graph): the exactly flat end
  states of T8, T23, T24 and T60 (9,865 of 11,880; O116, last addendum; O122 independently for T60): 39 hold a
  one-sided piece of 18 to 64 points, the 5 whole 64-point Klein bottles among them, and O122's 2 are two of those 5;
  T61's 27 flat end states (one 40-point Klein bottle beside a torus); T62's flat end states (one one-sided at N = 96,
  one at 192 with excess left; none exactly flat at its held-out N = 384); T64's (none one-sided; its held-out reading
  reports three end states in pieces and no one-sided piece). `scripts/analyse_t62.py`, `analyse_t63.py` and
  `analyse_t64.py` read one-sidedness for flat end states from the wiring. **Not read for it:** the 2,014 end states of
  T8, T23, T24 and T60 converted with energy left (O116's 12 October addendum read their widths only) and the one
  still a tube; every end state of the T7 decays, T37 and T38; T51's 600 cooled sheets; T61's roughly 693 non-flat
  end states; the non-flat end states of T62 and T64; and all of T63, which was NOT READ by its own rule
  (PREREGISTRATION, the T64 reading: "T63's rows, which were not read") and so stays closed under rule 16(b). No saved
  state is opened for this, in the sandbox or otherwise, until both the owner's confirmation of the draft entry (its
  completion convention and its two "to confirm" readings included, rule 20) and her prediction are in the notebook
  (the draft definition's item 6 names which families a sandbox look would open and which stay unopened for a
  registered version, rule 16(c)).
- *"Twisted diagonal" is not defined across the lip until a face rule is named.* In the complex of all squares, a
  ring of diagonals crossing the lip passes through five-square points where its band is undefined (facts 2 and 3).
  Under the eq45 brief's face rule the tube's points are surface points, so the band is defined on the tube and on the
  opened region. At the lip the rule ties between two rotations of one type, and the character of a ring through the
  lip is defined only under a completion that closes on the band round it; on the one lip built by hand (fact 3) no
  completion closes across the joint, the tube part and the sheet part each close two-sided by themselves, and every
  local failure lies on or beside the joint, so nothing is defined across that lip, while the lip's shape is ours and
  not the shape of record. The test as named therefore needs first a named face rule under which (a) is defined at
  the lips the saved states actually have, or a label (b), or an embedding (c).
- *What can be run now, exact and cheap, and what it would show.* On a lattice patch the answer is 0 everywhere
  (fact 4). An intrinsic mod-2 twist is already exact on built graphs: the reflected closure (zero cost from the
  tube) and the flat Klein grid carry character-1 cycles (fact 4). So a scan of saved end states cannot be a kill
  test for "the stiff toy carries a twist by itself", nor for "the chain reaches a one-sided state" (O116, O122, T61).
  What it can decide is where a twist sits in a state that still holds curled parts or a lip. On the reflected closure
  and the even-row Klein grids it sits on cycles along the tube through the points the reflection fixes, and on the
  odd-row grids, where the reflection fixes no column, on a one-pass zigzag of diagonals along the strip the
  reflection maps to itself; on no built example does it sit on a ring round the curl: cycles of links were computed,
  and so were rings of diagonals (the zigzag of diagonals round the curl reads 0 on every built graph, the Klein
  bottles included; a ring of diagonals that runs once along the reflected closure and closes through its junction
  reads 1; the one-pass zigzags through the fixed columns of the even Klein grids read 1; the smooth zigzag between
  columns 0 and 1 of the odd grids reads 1 with b faces; `sandbox/twist_character_check.py`, 23 October, a sandbox
  look). Read by region, the brief's cross-handle carries its twist in neither its curled part nor its opened part but
  across the splices: its middle ring reads 0 and a cycle along the handle reads 1. *Ours, to confirm:* her "I meant a
  twist, a 3d hypotenuse" (23 October) is read here as the diagonal across the curl, which is on the ring square, not
  along the tube, and under the eq45 rule that square is not a face, so nothing is defined on its diagonals under this
  rule. The scan should report, per state, under the local criterion of the draft entry: on which regions (the curled
  part, the opened part, all points) a completion closes and where the local failures lie; whether each region's band
  is one-sided or two-sided, and whether the completions agree; the outcome word defined through those bands (all
  two-sided; a twist in the opened part, in the curled part, or across the lip; no surface at the lip, or at a flaw);
  and each flat piece's ring seam shift in O116's presentation. If no curled part's band is one-sided in any saved
  state under the named rule, her twisted diagonal goes to a label (b) or to stage B with an embedding (c). Either way
  it is a sandbox look under rule 16 before it is anything else, after her confirmation of the entry and with her
  prediction first.
- *What the candidates can and cannot carry of her picture.* Hers, verbatim (`sandbox/NOTEBOOK.md`, 23 October):
  "I meant a twist, a 3d hypotenuse, not this whole thing. Maybe an electron, maybe a quark"; "Charge is only spin,
  speed of spin matters."; "A higher twist count holds more curling energy and has more mass, not more charge.";
  "Dark matter carries a half twist, so 2 loops are needed for a dark matter Full twist."; "it must twist, either 1/3
  clockwise or counterclockwise. But in order for the loop to close on itself it needs a full twist."; and, 21 October,
  "so matter and antimatter would hold a twist in different directions". Of these, the half twist is what (a) carries
  (one Möbius flip), with no sign (ours, to confirm, as a reading of her dark half twist); but (a) is a yes-or-no, and
  two passes round a flipped cycle read 0, the same as no twist, so "2 loops are needed for a dark matter Full twist"
  is not carried in her sense. The count: the seam shift (D0) is a count the wiring fixes, but of a whole flat torus
  and without a sign; a count on a ring, and the sign of matter against antimatter, need (b); the thirds and quarters
  as *angles* need (c), and in two directions the thirds do not exist at all (fact 5), only the quarters of the 45°
  square. The published "thirds" closest to hers are not angles: they are Bilson-Thompson's declared charge of e/3 per
  full twist of one ribbon among three (section 2), a label with a rule, which is candidate (b) with the braid model's
  interpretation.
- *Which stand-in.* The handoff moved this work from the slab to the tube because the six-link track waits on her
  decision (item 2.0). Nothing above depends on that: in three directions facts 1 to 3 hold with six links and
  "surface" replaced by the cubical complex's manifold condition, and her thirds become available as angles, still
  under (c).

## 7. The candidate definitions, listed (not drafted)

What each needs and what each can carry. The definition itself is for a later stage and the brief's box.

| # | Candidate | Needs | Carries | Cannot carry | Published form |
|---|---|---|---|---|---|
| D0 | Seam shift of a lattice torus, flat or curled (the torsion r), read in a named presentation: which seam is the ring, its size and direction | a piece that is a lattice torus (the flat tori; the tube itself, with rings of four); nothing declared; only the pair of wraps up to the grid's symmetries is intrinsic | a whole number the opening changes (0 → 2, O116): a count, for a whole flat piece | a sign (+r and −r are one graph); anything on a ring or a diagonal; the curled part; whether two regions of one graph are twisted the same way or opposite ways (O116 raises it; unread) | the twisted grids T(n, m, r) ([LZZ23]; Thomassen 1991, not read); helical boundary conditions (the 20 October note, sec. 7) |
| D1 | Orientation character of a ring of diagonals in the square complex (mod 2) | surface points along the ring (fact 1; where links carry three squares, a named face rule, fact 2; where the rule ties, a completion that closes) | a half twist or none (her dark half twist, without its direction; ours, to confirm) | a sign; a count (two passes read as none); thirds or quarters; matter against antimatter | the twisted loop of Ellis-Monaghan and Moffatt; the edge signature of Gross and Tucker |
| D2 | A declared half-twist sign (±) per diagonal or per link, composed round a ring | birth and death rules under the switch | the same as D1 plus a per-diagonal bookkeeping; still only parity round a ring | a count; thirds | the signed rotation system; the half-twist move τ |
| D3 | A declared integer (framing) per diagonal or per ring | birth, death, composition and "only the snap may change it" rules; a reference framing | a sign and a count (matter and antimatter as ±; "twist count is mass"); thirds and quarters as declared units (Z/6, Z/4) | anything derived rather than put in; conservation is by fiat unless the rules force it | the framed ribbon graph of Bilson-Thompson, Markopoulou and Smolin; Fuller 1978's reference ribbon plus local differences |
| D4 | Tw, Wr, Lk of a ring read from an embedding in 3-space | coordinates for every point of the ring and a normal field (a tape); stage B's lengths are not enough | everything of section 1, including her fractions as angles (sixths and quarters) | survival of the embedding past a switch (the toy has none) | Fuller 1971; Dennis and Hannay; the lattice ribbon |
| D5 | Knot type and linking of rings as lattice polygons (FCC for one kind's diagonals) | lattice coordinates; a move set of BFACF type | which rings are knotted or linked, kept under BFACF-style moves | twist of any kind; the triangle and the 45° square are unknots | Janse van Rensburg and Whittington 1991; Janse van Rensburg and Rechnitzer 2010 (FCC) |

## 8. Verdict

**FOUND, for the mathematics the box needs.** The pieces exist in print and were read: Lk = Tw + Wr with Lk the
only topological term (Fuller 1971; Dennis and Hannay 2005; White 1969 for the Frenet case); the twist that an
abstract graph can carry without any embedding, a mod-2 orientation character via signed rotation systems or ribbon
graphs, and the statement that a ribbon graph forgets full twists (Ellis-Monaghan and Moffatt); the integer twist as
a declared label on an embedded framed graph (Bilson-Thompson, Markopoulou and Smolin); the moves that keep knot type
on a lattice (BFACF; the 1991 theorem) and the moves that keep a manifold's topology (Pachner, via Lickorish). The
record's memory of the matter (the brief's box; VISION Update 92) matches the sources, with two additions: the mod-2
character, which where links carry three squares needs a named face rule and which one zero-cost switch from the tube
already makes non-zero (fact 4); and the seam shift of a lattice torus, flat or curled, read in a named presentation, which the record already carries under
other names (O116's "seam shifted by two"; the torsion r of the 20 October note). This is the desirable outcome for
the programme: nothing here has to be invented.

**UNCLEAR, for any future "we have not found" about a twist on a complex that is not a surface.** The toy's tube
has links with three squares, and a definition of twist across such links was not searched (pseudomanifolds,
branched surfaces, orientation of non-manifold 2-complexes; quadrangulation move sets). Until that search is done,
no sentence of that kind may be written.

**What would change the verdict:** reading Gross and Tucker 1987 (the orientability criterion at its source) and
Mohar and Thomassen 2001; a search on orientation characters of cycles in 2-complexes with non-manifold edges; the
Padua repository's full texts of the lattice-ribbon papers (blocked this session); Pachner 1991 at Elsevier; the
JvR–Whittington 1991 paper in full, for the exact statement of Theorem 3.11 (here quoted through the 2010 paper); and
Thomassen 1991 on quadrangulations of the Klein bottle (recorded in the 20 October note, sec. 7, not read), the
published family the toy's flat Klein grids belong to.

## Proposed bibliography entries (not yet in `REFERENCES.bib`)

Keys checked against the current key list (none collides). Bibliographic data checked where the "checked at" field
says; "to verify" marks data taken from a secondary source only. The `note` field records how much was read.

```bibtex
@article{Calug59,
  author  = {C{\u{a}}lug{\u{a}}reanu, Gheorghe},
  title   = {L'int{\'e}grale de {G}auss et l'analyse des n{\oe}uds tridimensionnels},
  journal = {Revue de Math{\'e}matiques Pures et Appliqu{\'e}es},
  volume  = {4},
  pages   = {5--20},
  year    = {1959},
  note    = {not read; not seen. Bibliographic data as the 1961 paper cites it (search summary quoting that reference) and as Dennis and Hannay 2005 cite it; to verify. The first statement of the self-linking formula (White 1969, p. 694).}
}

@article{Calug61,
  author  = {C{\u{a}}lug{\u{a}}reanu, G.},
  title   = {Sur les classes d'isotopie des n{\oe}uds tridimensionnels et leurs invariants},
  journal = {Czechoslovak Mathematical Journal},
  volume  = {11},
  number  = {4},
  pages   = {588--625},
  year    = {1961},
  doi     = {10.21136/CMJ.1961.100486},
  note    = {read in part (2026-10-23, assistant): title page and p. 588 (summary and introduction) viewed as images from the dml.cz scan, which has no text layer; the formula's page not located. Checked at dml.cz (volume, issue, pages, received 22 June 1960).}
}

@article{White69,
  author  = {White, James H.},
  title   = {Self-linking and the {G}auss integral in higher dimensions},
  journal = {American Journal of Mathematics},
  volume  = {91},
  number  = {3},
  pages   = {693--728},
  year    = {1969},
  doi     = {10.2307/2373348},
  note    = {read in part (2026-10-23, assistant): the introduction, pp. 693--695, and the opening of Appendix B, from the JSTOR scan hosted at Edinburgh, converted to text; the theorems of Sections 2 to 10 grepped only. Checked at the scan's JSTOR header (volume, issue, pages, July 1969); DOI from Crossref (23 October 2026). Călugăreanu's integer and Pohl's name for it (self-linking number) quoted from p. 694.}
}

@article{Fuller71,
  author  = {Fuller, F. Brock},
  title   = {The writhing number of a space curve},
  journal = {Proceedings of the National Academy of Sciences of the USA},
  volume  = {68},
  number  = {4},
  pages   = {815--819},
  year    = {1971},
  doi     = {10.1073/pnas.68.4.815},
  note    = {read in full (2026-10-23, assistant): the five pages from the Caltech repository's PDF (record 0wq4z-dv964), converted to text; the right margin of p. 816 is cut in the scan, figures not seen. Checked at PMC (PMC389050) and Caltech. Defines the strip, the linking number of a strip (integer, deformation invariant), the total twist number (real, strip dependent) and the writhing number as their difference, Eq. (1); the directional writhing number and its sphere average.}
}

@article{Fuller78,
  author  = {Fuller, F. Brock},
  title   = {Decomposition of the linking number of a closed ribbon: A problem from molecular biology},
  journal = {Proceedings of the National Academy of Sciences of the USA},
  volume  = {75},
  number  = {8},
  pages   = {3557--3561},
  year    = {1978},
  doi     = {10.1073/pnas.75.8.3557},
  note    = {abstract only (2026-10-23, assistant), from the PMC page (PMC392823); the PDF download was blocked. Linking number of a closed ribbon as a reference ribbon's linking number plus locally determined linking differences.}
}

@article{DH05,
  author  = {Dennis, M. R. and Hannay, J. H.},
  title   = {Geometry of {C}{\u{a}}lug{\u{a}}reanu's theorem},
  journal = {Proceedings of the Royal Society A},
  volume  = {461},
  number  = {2062},
  pages   = {3245--3254},
  year    = {2005},
  doi     = {10.1098/rspa.2005.1527},
  eprint  = {math-ph/0503012},
  note    = {read in full (2026-10-23, assistant): arXiv v2 (10 June 2005), 10 pages, converted to text. Journal data from the arXiv listing and the Southampton repository (eprints 29395); Crossref agrees (23 October 2026). Lk topological, Tw and Wr geometric (p. 2); Tw depends on the framing (p. 3); Lk integer because the ribbon is two-sided (p. 2); the writhe framing (abstract).}
}

@article{EMM12,
  author  = {Ellis-Monaghan, Joanna A. and Moffatt, Iain},
  title   = {Twisted duality for embedded graphs},
  journal = {Transactions of the American Mathematical Society},
  volume  = {364},
  number  = {3},
  pages   = {1529--1569},
  year    = {2012},
  doi     = {10.1090/S0002-9947-2011-05529-7},
  eprint  = {0906.5557},
  note    = {read in part (2026-10-23, assistant): abstract and Sections 1 to 3 of the arXiv PDF (32 pages), converted to text. Journal volume, issue and pages per the arXiv journal reference and Crossref (23 October 2026). Signed rotation systems, ribbon graphs (Definition 2.1), twisted loops, the half-twist move; "the embedding of a ribbon graph in three-space is irrelevant" up to equivalence.}
}

@article{BR02,
  author  = {Bollob{\'a}s, B{\'e}la and Riordan, Oliver},
  title   = {A polynomial of graphs on surfaces},
  journal = {Mathematische Annalen},
  volume  = {323},
  number  = {1},
  pages   = {81--96},
  year    = {2002},
  doi     = {10.1007/s002080100297},
  note    = {not read. Cited from Ellis-Monaghan and Moffatt's reference [4] and a search summary (a negatively signed edge is a ribbon with a half-twist; summary wording, to verify). Volume, issue, pages and date (May 2002) checked at Crossref (23 October 2026).}
}

@book{GT87,
  author    = {Gross, Jonathan L. and Tucker, Thomas W.},
  title     = {Topological Graph Theory},
  publisher = {Wiley-Interscience},
  year      = {1987},
  note      = {not read. Cited from Ellis-Monaghan and Moffatt's reference [13]. The source to read for the orientability criterion (an embedding scheme is orientable if and only if every cycle carries an even number of negative edges; general knowledge, to verify there).}
}

@book{MT01,
  author    = {Mohar, Bojan and Thomassen, Carsten},
  title     = {Graphs on Surfaces},
  publisher = {Johns Hopkins University Press},
  year      = {2001},
  note      = {not read. Cited from Ellis-Monaghan and Moffatt's reference [23] as their source for signed rotation systems.}
}

@article{BTMS07,
  author  = {Bilson-Thompson, Sundance O. and Markopoulou, Fotini and Smolin, Lee},
  title   = {Quantum gravity and the standard model},
  journal = {Classical and Quantum Gravity},
  volume  = {24},
  number  = {16},
  pages   = {3975--3993},
  year    = {2007},
  doi     = {10.1088/0264-9381/24/16/002},
  eprint  = {hep-th/0603022},
  note    = {read in part twice: 2026-10-21 (abstract, Secs. I, VIII B to D, IX; docs/reading/notes/2026-10-21_matter_as_loops.md) and 2026-10-23 (Secs. I to IV, V.A, from the arXiv v2 PDF converted to text). Pages 3975--3993 per Crossref (23 October 2026), 3975--3994 per the arXiv journal reference; to verify at IOP. States as embeddings of framed (ribbon) graphs in a 3-manifold; twist of +-2pi read as charge +-e/3; braiding content conserved under the exchange and expansion moves; the reduced link invariant.}
}

@article{BF81,
  author  = {Berg, B. and Foerster, D.},
  title   = {Random paths and random surfaces on a digital computer},
  journal = {Physics Letters B},
  volume  = {106},
  number  = {4},
  pages   = {323--326},
  year    = {1981},
  doi     = {10.1016/0370-2693(81)90545-1},
  note    = {not read. Bibliographic data from the reference list of Janse van Rensburg and Rechnitzer 2010 (which spells the second author "Foester") and search summaries; checked at Crossref (23 October 2026), which gives Foerster. The B of BFACF.}
}

@article{AC83,
  author  = {Arag{\~a}o de Carvalho, C. and Caracciolo, S.},
  title   = {A new {M}onte-{C}arlo approach to the critical properties of self-avoiding random walks},
  journal = {Journal de Physique},
  volume  = {44},
  number  = {3},
  pages   = {323--331},
  year    = {1983},
  doi     = {10.1051/jphys:01983004403032300},
  note    = {not read. Checked at Crossref (23 October 2026). Janse van Rensburg and Rechnitzer 2010 cite it as "Phys Rev B27 1635-1645" (their [1]); that is Amit, Parisi and Peliti, Asymptotic behavior of the "true" self-avoiding walk (Crossref). The AC of BFACF.}
}

@article{ACF83,
  author  = {Arag{\~a}o de Carvalho, C. and Caracciolo, S. and Fr{\"o}hlich, J.},
  title   = {Polymers and $g|\phi|^4$ theory in four dimensions},
  journal = {Nuclear Physics B},
  volume  = {215},
  number  = {2},
  pages   = {209--248},
  year    = {1983},
  doi     = {10.1016/0550-3213(83)90213-4},
  note    = {not read. From the 2010 paper's reference [2]; an INSPIRE record found in the search gives the same pages; checked at Crossref (23 October 2026). The ACF of BFACF.}
}

@article{JvRW91,
  author  = {Janse van Rensburg, E. J. and Whittington, S. G.},
  title   = {The {BFACF} algorithm and knotted polygons},
  journal = {Journal of Physics A: Mathematical and General},
  volume  = {24},
  number  = {23},
  pages   = {5553--5567},
  year    = {1991},
  doi     = {10.1088/0305-4470/24/23/021},
  note    = {abstract only (2026-10-23, assistant), from the IOP page (paywalled): "The authors prove that the ergodic classes of this Markov chain are the knot classes of the polygons." Pages 5553--5567 from the 2010 paper's reference [16]; the IOP page shows 5553. Its Theorem 3.11 is quoted through Janse van Rensburg and Rechnitzer 2010, Theorem 1.}
}

@article{JvR92,
  author  = {Janse van Rensburg, E. J.},
  title   = {Ergodicity of the {BFACF} algorithm in three dimensions},
  journal = {Journal of Physics A: Mathematical and General},
  volume  = {25},
  number  = {5},
  pages   = {1031--1042},
  year    = {1992},
  doi     = {10.1088/0305-4470/25/5/012},
  note    = {not read. From the 2010 paper's reference [8], cited there for the "non-trivial ergodicity properties" of the BFACF moves in the cubic lattice; checked at Crossref (23 October 2026).}
}

@article{JvRR10,
  author  = {Janse van Rensburg, E. J. and Rechnitzer, A.},
  title   = {{BFACF}-style algorithms for polygons in the body-centered and face-centered cubic lattices},
  journal = {Journal of Physics A: Mathematical and Theoretical},
  volume  = {44},
  number  = {16},
  pages   = {165001},
  year    = {2011},
  doi     = {10.1088/1751-8113/44/16/165001},
  eprint  = {1011.3847},
  note    = {read in part (2026-10-23, assistant): abstract, Sections 1, 2 and 3.1, the reference list, from arXiv v1 (16 November 2010), converted to text. Journal volume, issue and article number checked at Crossref (23 October 2026; published 28 March 2011). Restates the 1991 theorem (Theorem 1), defines the type I and II moves, and proves the ergodicity classes of its FCC moves are the knot types (Theorem 10), which applies to rings of one kind's face diagonals while lattice coordinates exist.}
}

@article{JvROSTW93,
  author  = {Janse van Rensburg, E. J. and Orlandini, E. and Sumners, D. W. and Tesi, M. C. and Whittington, S. G.},
  title   = {The writhe of a self-avoiding polygon},
  journal = {Journal of Physics A: Mathematical and General},
  volume  = {26},
  number  = {19},
  pages   = {L981--L986},
  year    = {1993},
  doi     = {10.1088/0305-4470/26/19/002},
  note    = {abstract only (2026-10-23, assistant), from the IOP page: writhe as a geometrical measure of a lattice polygon's entanglement; a rigorous result on |Wr| against the number of edges; Monte Carlo distributions, including trefoils. Closing page from Crossref (23 October 2026).}
}

@article{JvROSTW94,
  author  = {Janse van Rensburg, E. J. and Orlandini, E. and Sumners, D. W. and Tesi, M. C. and Whittington, S. G.},
  title   = {Lattice ribbons: A model of double-stranded polymers},
  journal = {Physical Review E},
  volume  = {50},
  number  = {6},
  pages   = {R4279--R4282},
  year    = {1994},
  doi     = {10.1103/PhysRevE.50.R4279},
  note    = {not read; search summaries of the abstract only (a ribbon of plaquettes on the simple cubic lattice, open or closed; Monte Carlo estimates of the backbone's writhe and, for orientable closed ribbons, the linking number of the two boundary curves). DOI from the APS listing; author order, issue and pages confirmed at Crossref (23 October 2026).}
}

@article{JvROSTW96,
  author  = {Janse van Rensburg, E. J. and Orlandini, E. and Sumners, D. W. and Tesi, M. C. and Whittington, S. G.},
  title   = {Entanglement complexity of lattice ribbons},
  journal = {Journal of Statistical Physics},
  volume  = {85},
  number  = {1--2},
  pages   = {103--130},
  year    = {1996},
  doi     = {10.1007/BF02175557},
  note    = {not read; search summaries of the abstract only (closed ribbons almost surely knotted as the plaquette count grows; for orientable ribbons the expected absolute linking number of the boundary curves grows at least as the square root of the count). Volume and pages from one bibliographic index; confirmed at Crossref (23 October 2026).}
}

@article{OJvRW96,
  author  = {Orlandini, E. and Janse van Rensburg, E. J. and Whittington, S. G.},
  title   = {A {M}onte {C}arlo algorithm for lattice ribbons},
  journal = {Journal of Statistical Physics},
  volume  = {82},
  number  = {3--4},
  pages   = {1159--1198},
  year    = {1996},
  doi     = {10.1007/BF02179807},
  note    = {not read. From the 2010 paper's references [18] and [19] (listed twice there); checked at Crossref (23 October 2026). The sampler for lattice ribbons; the move set that keeps or changes a ribbon's twist is to be read here before any lattice-ribbon analogue is built.}
}

@incollection{LS90,
  author    = {Lacher, R. C. and Sumners, D. W.},
  title     = {Data structures and algorithms for computation of topological invariants of entanglements: link, twist and writhe},
  booktitle = {Computer Simulation of Polymers},
  editor    = {Roe, R. J.},
  publisher = {Prentice Hall},
  address   = {Englewood Cliffs, NJ},
  pages     = {365--373},
  year      = {1990},
  note      = {not read. Data from Lacher's own publication page, which dates the book 1990 (the task said 1991; no source for 1991 was found).}
}

@article{Pachner91,
  author  = {Pachner, Udo},
  title   = {P.L. homeomorphic manifolds are equivalent by elementary shellings},
  journal = {European Journal of Combinatorics},
  volume  = {12},
  number  = {2},
  pages   = {129--145},
  year    = {1991},
  doi     = {10.1016/S0195-6698(13)80080-7},
  note    = {not read. Bibliographic data from a search summary of the Wikipedia entry "Pachner moves" and of citing arXiv papers; to verify at Elsevier. The theorem is quoted from Lickorish 1999, Theorems 5.9 and 5.10.}
}

@incollection{Lick99,
  author    = {Lickorish, W. B. R.},
  title     = {Simplicial moves on complexes and manifolds},
  booktitle = {Proceedings of the Kirbyfest},
  series    = {Geometry \& Topology Monographs},
  volume    = {2},
  pages     = {299--320},
  year      = {1999},
  eprint    = {math/9911256},
  note      = {read in part (2026-10-23, assistant): Sections 1, 2 and 5 (pp. 299--303, 313--318) from the arXiv PDF, converted to text. Checked at the arXiv listing and the journal page (msp.org/gtm/1999/02/p016). Definition 2.2 (combinatorial manifold), Definition 2.3 (bistellar move; the three moves on a surface), Theorem 5.9 (closed manifolds), Theorem 5.10 (with boundary).}
}
```

# Reading notes: loop and exchange rules, and which ones give gapless modes

> **Status of these notes:** written by an assistant agent on 2026-09-25 from fetched copies of the papers. Some passages
> were read through a tool that summarizes a page, so every quotation must be checked against the paper itself before it is
> used in a paper or a letter. Inferences marked *ours* are unreviewed.


Written 2026-09-25 by an assistant agent (Claude) for VISION Updates 28 and 29 and `docs/design/loop_exchange_brief.md`.
Method: each paper was downloaded from arXiv as a PDF and converted to text, and the passages cited below were read in
that text. Section and equation numbers are the papers' own. "Abstract only" means exactly that. No physicist has checked
anything here. Inferences about this project are marked *ours, unverified*. No run was made for these notes.

---

## (a) The answer in one paragraph

Across the papers read, a local loop rule gives a **gapless** mode, and so a force that falls off as a power of distance
rather than exponentially, when three things hold together. First, the variable on the loops is **continuous** (a U(1)
phase or rotor on each link, or an angle per point), or the rule leaves an **extensive family of zero-cost local
rearrangements** (close-packed dimers flipped around squares). Second, a **local conservation law** protects the mode (a
Gauss law, which in dimer models comes from the lattice being **bipartite**). Third, the dimension is high enough to
escape confinement. The published gapless cases are these. The U(1) rotor model on the cubic lattice, with a plaquette
(4-cycle) term, gives photons in 3+1 dimensions (Levin and Wen, *Quantum ether*, Sec. II; Gu and Wen 2006, Eq. 1). The
pyrochlore and cubic quantum dimer models near their soluble point have a gapless linear photon, and their charges
interact as 1/r (Hermele, Fisher and Balents, abstract and Sec. II.C). **Classical** hard-core dimers on the bipartite
cubic lattice sit in a critical Coulomb phase with dipolar correlations, and opposite-sublattice defects attract with an
**entropic** inverse-square force (Huse, Krauth, Moessner and Sondhi). The Goldstone modes of any broken continuous
symmetry make fluctuation-induced forces long-ranged (Kardar and Golestanian, Sec. II.C and III.B). Loop gases in 2D are
critical when each loop is weighted n ≤ 2 (Troyer et al.). At the linearized level only, gravitons come out of a lattice
of compact rotors (Gu and Wen 2006), though the model Gu and Wen 2009 can treat reliably disperses as k³, not k. The
**gapped** cases are these. Every discrete-group loop rule is gapped at its fixed point: the toric code (Kitaev, Eq. 4,
gap at least 2, correlations decaying exponentially) and the commuting-projector string-net models of Levin and Wen, whose
topological phases are "gapped" (their Sec. I). Compact U(1) confines at every coupling in 2+1 dimensions (Polyakov, as
cited by Moessner, Sondhi and Fradkin). A classical U(1) plaquette rule on three-dimensional graphs is therefore gapped
unless the microscopic rules forbid monopoles. Dimer models on non-bipartite lattices have only exponential correlations.
Decisively for this project, **exchange phases themselves** are gapped in the sense that matters: quantum statistics is a
*flat* connection, and "the flatness of the connection ensures that there are no classical forces associated with it"
(Maciążek and Sawicki 2019, Sec. 1). *Ours, unverified:* the exchange sign adopted in Update 29 can select arrangements but
cannot by itself produce a pull. A long-range pull needs a new continuous or constrained field living on the loops. The
one structural fact already in the project's favor is that its graphs are bipartite.

---

## (b) Paper by paper

### 1. Quantum statistics on graphs and graph braid groups

**[HKRS14] J. M. Harrison, J. P. Keating, J. M. Robbins, A. Sawicki, "n-particle quantum statistics on graphs",
Commun. Math. Phys. 330 (2014) 1293; arXiv:1304.5781.** Read: abstract, Sec. 1, Sec. 2.1 to 2.4, Sec. 3 (Theorem 1),
Sec. 4.2 (Theorem 4), Sec. 4.3 (Eqs. 17 to 19), Sec. 5 (Theorem 5), and the openings of Sec. 6 and 7.
- Statistics is the first homology H1 of the configuration space of n unlabeled particles on the graph (Sec. 1). For
  points in R^N it is Z when N = 2 (anyons) and Z2 when N ≥ 3 (bosons or fermions only).
- **Theorem 4:** for a 3-connected simple graph, H1(D2) = Z^β1 ⊕ A, where A = Z2 if the graph is non-planar and A = Z
  if it is planar. In words (Sec. 2.1): non-planar 3-connected graphs allow only Bose or Fermi exchange (phase 0 or π),
  and planar ones allow one anyon phase. The Z^β1 part is one Aharonov–Bohm phase per independent cycle (Sec. 2.4).
- Sec. 2.1, Fig. 1: a large square lattice becomes non-planar, and loses its anyons, when a single local K5 defect is
  inserted.
- **Theorem 5:** on 2-connected graphs the statistics does not depend on the number of particles. Sec. 2.2 and Fig. 3: a
  chain of 3-connected pieces can hold bosons in one piece and fermions in the next.
- Sec. 2.3, 4.4 and 6: 1-connected graphs (those with a cut vertex) have more phases, and the number depends on n (the
  star-graph formula).
- Theorem 1 (Abrams): the discrete configuration space D_n is equivalent to the continuous one when the graph is
  "sufficiently subdivided". For n = 2 every simple graph qualifies.

*Bearing (ours, unverified).* This paper is about **particles hopping on a graph**. The project's rule signs **renamings
of the graph's own points**, which is a different object. Two consequences still follow. (i) Every simple bipartite graph
with four or more links per point is non-planar: a planar graph with no triangles has at most 2V − 4 edges, while these
have E = kV/2 ≥ 2V. So on any 3-connected piece of any arrangement the project uses (the flat sheets are 4-connected),
particles hopping on the network could only be bosons or fermions. Anyon phases would need low connectivity, meaning pieces
joined through a single point or a pair of points, as leftovers attached to the sheet by a narrow neck would be. (ii) On
graphs, the statistics of a particle is a property of the local wiring rather than of the particle, and this is a
published fact (Fig. 3).

**[MS19] T. Maciążek, A. Sawicki, "Non-abelian quantum statistics on graphs", arXiv:1806.02846 (journal reference
not checked).** Read: abstract and Sec. 1 (pp. 1 to 3).
- All possible statistics are the unitary representations of the fundamental group π1(C_n(X)). For X = R² this group is
  the braid group; for R^k with k ≥ 3 it is the permutation group S_n (Sec. 1, p. 2).
- "The flatness of the connection ensures that there are no classical forces associated with it and the resulting
  physical phenomena are purely quantum" (Sec. 1, p. 2). *Bearing (ours):* an exchange rule alone cannot deliver the
  gravity leg.

**[Mac19] T. Maciążek, "Non-abelian anyons on graphs from presentations of graph braid groups", Acta Phys. Pol. A
136 (2019); arXiv:1909.02098.**
Abstract and first page only. Single author. Moduli spaces of flat bundles encode all unitary representations of graph
braid groups, and for 2-connected graphs they stabilize as the number of particles grows.

**[KP11] K. H. Ko, H. W. Park, "Characteristics of graph braid groups", Discrete Comput. Geom. (2012);
arXiv:1101.2648.** Read: abstract, Sec. 1, and the statement of Corollary 3.6. A graph is planar if and only if H1 of its
n-braid group is torsion-free (abstract). Any torsion is 2-torsion, and how much of it there is does not depend on n
(Cor. 3.6). This is the structure theorem that [HKRS14] re-proves.

**[Ghr99] R. Ghrist, "Configuration spaces and braid groups on graphs in robotics", arXiv:math/9905023.** Read: abstract
and the Sec. 2 statements (Theorem 2.3, Corollary 2.4, Theorem 2.5). Configuration spaces of graphs are K(π, 1) spaces
(Cor. 2.4 for trees; the abstract says so in general), with homological dimension bounded by the number of essential
vertices, and graph braid groups are torsion-free. Abrams's thesis (2000) was not read.

**What "anyons on graphs" means**, from the four papers above: a phase attached to a *path* along which two particles on
the network trade places, classified by the braid group of the network's configuration space. It belongs to histories,
not to a fixed arrangement.

### 2. Loop and string-net models with emergent gauge fields or gravitons

**[LW05] M. A. Levin, X.-G. Wen, "String-net condensation: a physical mechanism for topological phases", Phys. Rev. B
71, 045110 (2005); arXiv:cond-mat/0404617.** Read: abstract, Sec. I, the Fig. 1 caption, the opening of Sec. II, Sec. IV.B
(Hamiltonian 10 and its properties), and Sec. VII.
- Degrees of freedom: string types on the links of the honeycomb lattice. Rule: H = −Σ_I Q_I − Σ_p B_p (Eq. 10). Q_I
  enforces the branching rules at vertices, and B_p (acting on the 12 spins around a hexagon) makes the strings
  fluctuate. All terms commute, so the model is exactly soluble.
- Fig. 1: when string tension beats string kinetic energy, the vacuum is nearly empty. In the opposite limit, large
  fluctuating string-nets fill space (condensation), with a transition at t/U of order one.
- Topological phases are gapped (Sec. I), and the 2D models are gapped. In 3D and higher, string-net condensation
  "naturally gives rise to both gauge interactions and Fermi statistics" (abstract; Sec. VII).

**[LW05b] M. Levin, X.-G. Wen, "Quantum ether: photons and electrons from a rotor model", Phys. Rev. B 73, 035122 (2006);
arXiv:hep-th/0507118.**
Read: abstract, Sec. II.A to II.C (Eqs. 1 to 3), and Sec. III.A to III.C (Eqs. 6 to 10).
- Degrees of freedom: a quantum rotor on each **link of the 3D cubic lattice**. Rule (Eq. 1):
  H = V Σ_I Q_I² + J Σ_i (L^z_i)² − g Σ_p (B_p + h.c.), with B_p = L⁺₁L⁻₂L⁺₃L⁻₄ around each **square plaquette** and
  Q_I = (−1)^I Σ_legs L^z. The alternating sign is the bipartite (sublattice) sign.
- J acts as a string tension and g as a string kinetic term. For g ≫ J the strings condense (Sec. II.B). The low-energy
  theory is compact U(1) gauge theory (Eq. 2): string fluctuations are **gapless photons** and string endpoints are gapped
  charges. The "fine structure constant" is of order J/g and the speed of light of order gJa² (Sec. II.C). At large
  coupling the theory confines and has no photons.
- Sec. III: a **"twisted" plaquette term**, B̃_p = B_p × (−1)^(sum of L^z on the legs next to the plaquette) (Eq. 9),
  keeps the photons and turns the charges into **fermions**. *Bearing (ours):* this is the published way to put an
  exchange sign on loop moves. The sign sits on the move and depends on the local occupation; it is not a symmetry of the
  whole arrangement. It lives in a quantum Hamiltonian, and in a classical Monte Carlo weight it would become a sign
  problem.

**[GW06] Z.-C. Gu, X.-G. Wen, "A lattice bosonic model as a quantum theory of gravity", arXiv:gr-qc/0606100.** Read in
full (four pages).
- Warm-up (Eq. 1): an angle a_ij on each link of the cubic lattice, with energy −g Σ cos(a_ij + a_jk + a_kl + a_li)
  over the square faces. It has two linear gapless helicity ±1 modes (photons). The helicity-0 mode is gapped by
  compactness and discreteness.
- Graviton model (Eqs. 3 to 6): six compact variables per vertex and two per square face of the cubic lattice, with a
  finite Hilbert space per site. At large n_G the helicity ±2 modes are gapless, with ω ∝ √(gJ)|k| near k = (π, π, π),
  and all other modes are gapped (Eqs. 7 to 9). The low-energy theory is linearized Einstein gravity. Interactions
  consistent with Einstein gravity are not shown ("possibly (f)"). The Weinberg–Witten theorem is evaded because the
  energy-momentum tensor is not invariant under linearized diffeomorphisms.

**[GW09] Z.-C. Gu, X.-G. Wen, "Emergence of helicity ±2 modes (gravitons) from qubit models", Nucl. Phys. B 863 (2012) 90;
arXiv:0907.1203.**
Abstract and the Sec. I conditions only. **This qualifies [GW06].** In the model the authors can treat reliably (L-type),
the gapless helicity ±2 modes disperse as ω ∝ k³, not linearly. Linear dispersion is argued for a second model (N-type)
by a method the authors say is not reliable. *Bearing (ours):* gapless spin-2 modes from a lattice loop rule are shown; a
graviton with the right dispersion is not.

**[HFB04] M. Hermele, M. P. A. Fisher, L. Balents, "Pyrochlore photons: the U(1) spin liquid in a S = 1/2
three-dimensional frustrated magnet", Phys. Rev. B 69, 064404 (2004); arXiv:cond-mat/0305401.** Read: abstract, Sec. I,
Sec. II.A, **Sec. II.B (the cubic model, Eq. 12)**, and Sec. II.C, including its review of the phases of compact U(1).
- Sec. II.B: a quantum dimer model on the **cubic lattice with three dimers touching every site**. The dynamics rotates
  the configuration on square plaquettes that have two dimers on opposite sides (Eq. 12, a 4-site ring exchange), plus
  a Rokhsar–Kivelson potential that counts flippable squares. The model has an exact U(1) gauge invariance.
- Sec. II.C: in the Coulomb phase, static charges interact through a 1/r potential and the photon is gapless and linear,
  with two polarizations. In the confined phase "all excitations are gapped", and charges are bound by a linear potential.
- The U(1) spin liquid is stable to all zero-temperature perturbations (abstract).
- *Bearing (ours):* of the published models we found, this is the closest to the project's own move set. It has a
  bipartite graph of fixed degree, a fully packed edge configuration, and moves that rotate a pair of edges around a
  4-cycle. The project's switch is that same move made on the complete bipartite host, which has no geometry. So the
  Coulomb physics would have to live on a *second* field placed on the emergent graph, not on the graph itself.

**[HKMS03] D. A. Huse, W. Krauth, R. Moessner, S. L. Sondhi, "Coulomb and liquid dimer models in three dimensions",
Phys. Rev. Lett. 91, 167004 (2003); arXiv:cond-mat/0305318.** Read in full.
- The model is **classical** close-packed hard-core dimers, weighted by counting alone. On a bipartite lattice the field
  B_i(x) = ε_x(n_i(x) − 1/z) is divergence-free (Eq. 1): a magnetic field without monopoles. A monomer (an unmatched
  site) is a monopole whose charge, ±1, is set by its sublattice.
- On the bipartite cubic lattice the dimers sit in a critical Coulomb phase, P[A] ∝ exp(−(K/2)∫(∇×A)²) (Eq. 3), with
  dipolar correlations (Eq. 4). Monte Carlo up to L = 128 gives the exponent 3.00 ± 0.02. Polyakov's confinement is evaded
  because "the microscopics explicitly forbid the monopoles", and gauge invariance protects the masslessness.
- "The interaction between two monomers is an **attractive entropic force** with the same form as that between oppositely
  charged monopoles, i.e. an inverse squared force."
- On the non-bipartite FCC and Fisher lattices the dimers are confined or exponentially deconfined, never critical. The
  authors conjecture that extended critical phases occur only on bipartite lattices, in higher dimensions too. On 2D
  bipartite lattices, monomer pairs are confined: their free energy grows logarithmically or linearly with separation
  (introduction).
- *Bearing (ours, unverified):* this is the cleanest published instance of what O56 found missing, a long-range pull
  between defects that comes **from counting alone**, in a classical model with no energy at all. It needs three
  dimensions and a bipartite lattice, and the six-link flat torus is both. Its sign depends on the sublattice charge (like
  charges repel), so it behaves like electromagnetism, not like gravity.

**[MSF01] R. Moessner, S. L. Sondhi, E. Fradkin, "Short-ranged RVB physics, quantum dimer models and Ising gauge
theories", Phys. Rev. B 65, 024504 (2001); arXiv:cond-mat/0103396.** Read: abstract, the "Other lattices" and
"Charge-2 Higgs scalars" passages, Sec. C (d > 2), and the closing comparison of bipartite and non-bipartite lattices.
Quantum dimer models develop a local U(1) invariance. On bipartite lattices they behave like the square lattice: critical
classical correlations through the height model, and confinement once quantum fluctuations are added. On non-bipartite
lattices the gauge group falls to Z2, and a gapped deconfined liquid is possible. Polyakov: pure compact U(1) gauge theory
confines at all couplings in 2+1 dimensions. In d > 2 "little is known" (as of 2001).

**[Kit97] A. Yu. Kitaev, "Fault-tolerant quantum computation by anyons", Ann. Phys. 303 (2003) 2;
arXiv:quant-ph/9707021.** Read: abstract, Sec. 1
(Eqs. 1 to 4 and the stability discussion), and Sec. 2 (abelian anyons). Qubits sit on links, with star operators A_s
and plaquette operators B_p (Eq. 1), and H0 = −Σ A_s − Σ B_p (Eq. 4). All excited states lie at least ΔE = 2 above the
ground state, and correlations decay exponentially. The construction works on "an arbitrary irregular lattice" on any
surface, with 4^g ground states on a surface of genus g, and its excitations are abelian anyons with mutual phase −1
(Sec. 2). **This is the gapped counterpart:** discrete (Z2) loop variables, no massless mode, so no long-range force.

**[TTSN08] M. Troyer, S. Trebst, K. Shtengel, C. Nayak, "Local interactions and non-Abelian quantum loop gases",
Phys. Rev. Lett. 101, 230401 (2008); arXiv:0805.2177.** Read in full. A quantum loop gas in which each loop has weight d
maps to the classical O(n) loop model with n = d² (Eq. 2), which is critical for n ≤ 2 in its low-temperature (dense)
phase. The local loop-gas Hamiltonian is gapless for d ≠ 1. For d = 1 (the toric code), local surgery terms can open a gap
(Eq. 4). Gapped non-Abelian loop gases need non-local interactions. *Bearing (ours):* in 2D, rules that weight each loop
are critical when the weight is at most 2. This is the loop-counting analog of a gapless mode.

### 3. Link variables becoming gauge fields in graph models of emergent geometry

**[KMS06] T. Konopka, F. Markopoulou, L. Smolin, "Quantum graphity", arXiv:hep-th/0611197** (the project's [KMS06]).
Read: abstract, Sec. II.B (on a frozen cubic lattice the loop term reduces to Levin and Wen's rotor model), **Sec. IV
(Eqs. 27 to 33)**, and Sec. VI.
- Sec. IV: set the valence to 6 and freeze the links into a regular 3D lattice of four-sided plaquettes. The m variables
  on the links (m ∈ {−1, 0, 1}), with the plaquette operator W_a = M⁺M⁻M⁺M⁻ around each 4-cycle (Eqs. 28, 29), then give
  the Kogut–Susskind Hamiltonian of U(1) lattice gauge theory (Eq. 30), with a weak coupling g² = (2β)^(−1/2) (Eq. 32).
  Photon-like excitations are *expected* ("should exhibit"), not shown.
- Sec. VI: gravitons were not attempted.
- *Bearing (ours):* this is the precedent the project cites, and it is literally a **six-link, 4-cycle** rule. It is
  quantum (a Hamiltonian), and its gauge field lives on a frozen lattice.

**[KMS08] T. Konopka, F. Markopoulou, S. Severini, "Quantum graphity: a model of emergent locality", Phys. Rev. D 77,
104029 (2008); arXiv:0801.0861.** Read: abstract, the end of Sec. IV, and Sec. VI. The string-condensed ground state is
"difficult" to characterize, but its excitations are expected to be those of a U(1) gauge theory (end of Sec. IV). It
differs from Levin and Wen's model in two ways: the lattice is dynamical and the plaquettes are hexagons. Sec. VI names an
open problem: **extending string-net condensation to irregular graphs**, which is "of interest independently of this
work". *Bearing (ours):* the project's graphs are irregular exactly near its defects, so any loop rule it adopts runs into
this open question.

**[HMPS08] A. Hamma, F. Markopoulou, I. Prémont-Schwarz, S. Severini, "Lieb–Robinson bounds and the speed of light from
topological order", Phys. Rev. Lett. 102, 017204 (2009); arXiv:0808.2495.** Abstract and the model paragraph only. In a 2D
rotor model whose low-energy theory is light, the maximum speed of interactions is bounded above by less than √2 e times
the emergent speed of light.

*Not read, found in search:* F. Caravelli, A. Hamma, F. Markopoulou, A. Riera, "Trapped surfaces and emergent curved space
in the Bose–Hubbard model", arXiv:1108.2013. Only the abstract, as quoted in search results, was seen: highly connected
subgraphs trap matter. Of the quantum-graphity papers, it is the one closest to "matter moved by the shape of space", and
it is worth reading next.

### 4. Automorphism-weighted and sign-weighted ensembles of graphs

**[DQM25] K. Betre, N. Lewis, "Dynamical quantum multigraphs", arXiv:2509.08296** (already in `REFERENCES.bib`; the
owner's reading covered Sec. 4 and Appendix A). Read here: **Sec. 3 up to Lemma 3.1 (Eqs. 46 to 53)** and the opening of
Sec. 4.
- Sec. 3: unlabeled quantum graphs are defined by projecting labeled ones with the symmetrizer S or the antisymmetrizer
  A = (1/N!) Σ_σ sgn(σ) σ (Eqs. 46, 49). "For N ≥ 2 there are only two 1D irreducible representations of the symmetric
  group, the trivial representation and the sign representation", and the Pauli principle follows from A.
- Their antisymmetric sector uses antisymmetric pair kets, |n⟩_[ij] = −|n⟩_[ji] (Sec. 2.C, Eq. 10). Sec. 4 then states
  that "after antisymmetrizing the unlabeled quantum graph basis kets are enumerated simply by unlabeled graphs". In their
  convention, **nothing is forbidden**.
- *Bearing (ours, unverified):* O57's rule (symmetric edges, with the sign taken on the points alone) is a different
  convention, and it forbids a few per cent of damaged sheets. The two are consistent. A renaming reverses as many
  point-pairs as its inversion count, and the parity of that count is sgn(σ), so antisymmetric pair kets taken over all
  pairs cancel the sign on the points exactly. **Which sign representation is chosen decides what is forbidden.** That
  makes it a choice to be dated under S1, not a derived fact.

**[Wil10] T. Willwacher, "M. Kontsevich's graph complex and the Grothendieck–Teichmüller Lie algebra", arXiv:1009.1654
(journal reference not checked).** Read: the Sec. 3 definitions (the operads Gra_n with sign representations on edge orderings or
vertex labels, fGC_n as (anti)invariants, Remark 3.2) and the caption of Fig. 5. A graph in the complex is a signed sum
over its labelings, divided by its symmetry count (Remark 3.2), and "some of these graphs (depending on n) are zero by
symmetry" (Fig. 5). *Bearing (ours):* this is the mathematical precedent for "an arrangement with an odd symmetry has
weight zero". There, the sign is carried by an ordering of the edges (n even), or by an ordering of the vertices together
with the edge directions (n odd).

**Searched, not found:** we have not found a physics paper that uses a signed sum over a graph's automorphisms as a
statistical weight on an ensemble of graphs. This rests on one web search; the nearest are [DQM25] and the graph complex.

---

## (c) Candidate rules for the project's graphs

The project's graphs are k-regular and bipartite (k = 4, 6, 8), the energy counts 4-cycles, and the moves are
degree-preserving switches. Each candidate below adds a new ingredient, so under S1 each needs a dated VISION decision
before any run. Each first test is made at **fixed wiring** (the flat torus with one or two saved relics), so it cannot
disturb any verdict on record.

**First, three exact points about rule A's next step, the "anyonic form"** (ours; each rests on a source read above):
1. A phase attached to each renaming of a fixed arrangement cannot be anyonic. Renamings are elements of S_N, whose only
   one-dimensional representations are the trivial one and the sign ([DQM25] Sec. 3). And whatever one-dimensional
   character χ is used on a finite group H, Σ_{h∈H} χ(h) is either |H| or 0 (orthogonality of characters, textbook). So
   the sum over the automorphisms of one arrangement can only select; it can never cancel partly.
2. Anyonic phases live on the braid group of a configuration space, that is, on **paths** of exchanges ([MS19] Sec. 1).
   An anyonic rule is therefore a rule over histories, the reformulation that VISION Update 20 already named as a
   different claim.
3. For particles hopping on the project's own networks, which are non-planar, 3-connected pieces allow only phases of ±1
   ([HKRS14] Theorem 4). Richer phases need pieces joined through one or two points ([HKRS14] Sec. 2.2, 2.3). And exchange
   phases are flat, so they carry no classical force ([MS19] Sec. 1).

### Candidate 1. A massless phase on the points, summed out exactly (the cheapest test)

**Rule.** Give each point an angle φ_i, with energy (J/2) Σ_edges (φ_i − φ_j)². This is the spin-wave limit of an XY
rule. Summing over all angles gives each arrangement the extra weight det′(L)^(−1/2), where L is the arrangement's graph
Laplacian and det′ leaves out the zero mode. By the matrix-tree theorem (textbook, not read for these notes),
det′(L) = N × (the number of spanning trees), so this weight is again a pure count.

**Source.** [KG99] M. Kardar, R. Golestanian, Rev. Mod. Phys. 71, 1233 (1999), arXiv:cond-mat/9711071 (read: abstract and
Sec. I, II.A, II.C, III.B). The range of a fluctuation-induced force is the correlation length of the medium. Goldstone
modes of a broken continuous symmetry make the force long-ranged (Sec. II.C; their Eq. 3 is exactly this energy).
On a membrane, the interaction between inclusions falls off as 1/R⁴ whenever their rigidity differs from the membrane's.
For much stiffer inclusions it is attractive, with an energy scale of k_BT. Such forces are not pairwise additive
(Sec. I and III.B). O. Kenneth, I. Klich, Phys. Rev. Lett. 97, 160401 (2006), arXiv:quant-ph/0601011
(**abstract only**): the Casimir force between two bodies related by a reflection is always attractive (proved for
electromagnetism).

**Prediction (ours, unverified).** Place the relics of O56 in the flat six-link torus. The pull that comes from counting,
ΔF(r) = −(T/2)[ln det′L₁₂ − ln det′L₁ − ln det′L₂ + ln det′L₀], falls off as a power of r, and for two identical relics
it is attractive. Adding a mass term m² to L must make it fall off exponentially, with a length of about 1/m. That is the
gapped control, and it should reproduce O56's null.

**Cost.** Exact, with no Monte Carlo. An 8 × 8 × 8 torus is a 512 × 512 determinant, milliseconds each, so a scan over
every separation takes seconds, and 16³ still takes only minutes. The project already computes Laplacian spectra (O30).
**What would kill it:** exponential decay without a mass term, or a repulsive sign between identical relics.
**Caveat:** a pull that comes from a change in stiffness is van der Waals-like and falls off much faster than Newton's
1/r². A 1/r potential would need a relic that acts as a *source* of the field (a term linear in φ), and this rule does
not supply one.

### Candidate 2. A close-packed dimer field on the flat sheet (a Coulomb phase from counting alone)

**Rule.** On each arrangement, place a second configuration: a set of links with exactly one link per point (a perfect
matching). All such sets get equal weight, and they move by rotating two parallel links around a 4-cycle (the project's
switch, applied to the second field). The arrangement's weight then becomes its number of perfect matchings, or the
matching field is sampled alongside the arrangement.

**Source.** [HKMS03] (read in full). On the bipartite cubic lattice this is a critical Coulomb phase with dipolar
correlations (exponent 3.00 ± 0.02 at L up to 128). An unmatched point is a charge of ±1 according to its side, and
opposite charges feel an **attractive entropic inverse-square force**. Non-bipartite lattices are never critical, and 2D
bipartite lattices confine. See [HFB04] Sec. II.B (the cubic model, with ring moves on squares) and [MSF01] for the quantum
and bipartite context. Recent: J. Walkling, R. Moessner, "Fractal deconfinement and confinement in Sierpinski ice",
arXiv:2608.02741 (**abstract only**: the four-coordinated ice model on a fractal confines its charges entropically); and
T. Ben-Ami, M. Heyl, R. Moessner, "Breakdown of multipole expansion in emergent electromagnetism", arXiv:2609.12063
(**abstract only**: in hardcore dimer and U(1) spin-1/2 link models, dense charge configurations break the superposition
principle in the far field).

**Prediction (ours, unverified).** The gate comes first: reproduce the dipolar exponent of 3 on the six-link flat torus,
which is a cubic lattice. Then: a relic that leaves points unmatched acts as a charge and feels an entropic 1/r potential
from another such relic, while a relic that keeps a perfect matching is neutral and feels only a short-range or dipolar
pull. On four links (2D), charges are confined. On eight links the Coulomb phase should persist, since the conjecture of
[HKMS03] extends to higher dimensions. **What would kill it:** no power law on the flat torus, or relics that always turn
out neutral. **Caveat:** Coulomb charges come in two signs, one per side, so a universally attractive, gravity-like pull
does not come out of this rule.

**Cost.** Modest. Classical dimer Monte Carlo on L = 16 to 32 (4k to 33k points) needs a loop update (worm or pocket),
because flipping squares alone does not change the flux sector; minutes to hours on a laptop. It reproduces a published
number before it asks anything new, as rule 2 requires.

### Candidate 3. A compact U(1) phase on each link, with its energy on the 4-cycles

**Rule.** Put an angle θ_e on every link, oriented from side 0 to side 1 (the bipartite structure supplies the
orientation, as the (−1)^I does in [LW05b] Eq. 1), and add −K Σ_squares cos(θ_ab − θ_cb + θ_cd − θ_ad). The squares that
the energy already counts then become the plaquettes of a gauge field, so curvature and field live on the same objects.
A curled region carries extra squares, so it is locally stiffer.

**Source.** [KMS06] Sec. IV, Eqs. 27 to 33 (six links, four-sided plaquettes, Kogut–Susskind U(1)); [LW05b] Sec. II
(rotors on the links of the cubic lattice, photons); [GW06] Eq. 1; and [HFB04] Sec. II.C for what the Coulomb and
confined phases look like (a 1/r potential against a linear one; gapless against fully gapped).

**Prediction (ours, unverified).** As a classical weight at fixed wiring, this is Euclidean compact U(1) in D dimensions.
On six links (D = 3) it confines at every K by Polyakov's argument (as cited in [MSF01]), so it is gapped and its Wilson
loops follow an area law. That makes it a useful negative control, and it means the six-link version cannot supply a
long-range pull. On eight links (D = 4), the standard expectation is a Coulomb phase with a massless photon at weak
coupling (Guth 1980; Fröhlich and Spencer 1982; general knowledge, **not read**, to verify before citing). A quantum
version with Hamiltonian dynamics on six links would have photons ([LW05b]), but the project does not simulate
Hamiltonian dynamics. **What would kill it:** an area law at weak coupling on the eight-link torus. **Cost:** the heaviest
of the three: heat-bath Monte Carlo on a 6⁴ to 8⁴ flat eight-link torus (1,296 to 4,096 points), taking hours.
**Naming:** at any λ this is not CQG.

**Suggested order (ours):** 1, then 2, then 3. Candidate 1 is exact and takes an afternoon, candidate 2 has a published
gate, and candidate 3 is informative mainly in the eight-link case.

---

## (d) Who to ask, with one narrow question each

Each recipient's 2024 to 2026 work was checked on arXiv on 2026-09-25. Per the outreach preferences, each letter carries
one question and the project's standard AI disclosure, and each question is checked against the recipient's recent papers
before sending.

1. **Gia-Wei Chern, University of Virginia, Physics** (Associate Professor; UVA faculty page and Shannon Center page).
   His 2026 work includes Abelian lattice gauge models in the Wilson-loop representation (A. Rayat, G.-W. Chern,
   arXiv:2605.03901, abstract read; also arXiv:2604.20797, title only) and deconfined spinons (arXiv:2608.26347, title
   only), and earlier he worked on Coulomb phases and diluted spin ice. **Question:** "Does a classical close-packed dimer
   (or ice) Coulomb phase on a bipartite cubic lattice survive a finite density of *local* lattice defects, such as a few
   sites where the wiring is rearranged locally while the lattice stays bipartite and 6-regular, or does such disorder
   confine the charges?"

2. **Israel Klich, University of Virginia, Physics.** He is already on the outreach list for a different question
   (`docs/outreach/outreach_letters_2026-09-23.md`, 5.3), so this question would replace that one or wait. Said plainly,
   the fit comes from Kenneth and Klich 2006 (abstract read), not from his 2024 to 2026 papers, which are on Metropolis
   and Mpemba dynamics on graphs, thermalization, and learning. **Question:** "For a massless Gaussian field on a finite
   regular graph, is the fluctuation-induced free energy between two identical local defects related by a reflection
   guaranteed to be attractive, as your theorem shows for the electromagnetic case?"

3. **Roderich Moessner, Max Planck Institute for the Physics of Complex Systems, Dresden.** He co-authored [HKMS03] and
   [MSF01], and his 2026 work includes Sierpinski ice (arXiv:2608.02741) and the breakdown of the multipole expansion in
   emergent electromagnetism (arXiv:2609.12063); both abstracts were read. **Question:** "Your 2003 conjecture ties
   critical dimer phases to bipartite lattices. Is anything known about whether it holds on bipartite graphs that are
   regular in degree but are not lattices, for example a cubic lattice rewired locally in a few places?"

*Alternative for the exchange-phase question:* Jonathan Harrison (Baylor), lead author of [HKRS14]. His 2024 papers are
on the spectra of quantum graphs, including circulant (regular) graphs, not on statistics. A narrow question for him: "For
two particles hopping on a 4-connected, non-planar, 4-regular bipartite graph, is the answer of Theorem 4 (bosons or
fermions only, plus Aharonov–Bohm phases) the complete classification?"

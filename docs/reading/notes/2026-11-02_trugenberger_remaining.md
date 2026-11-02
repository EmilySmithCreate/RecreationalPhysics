# Reading note: the rest of Trugenberger's work, read before the quantum toy

Date: 2026-11-02. By an assistant agent (Claude Opus 5.5). The owner has not read these passages. Every quotation is
from the arXiv PDFs (1610.05934v3, 1710.00221v1, 1501.01408v2, 1507.01820v2, 1610.05339v1, 1811.12905v1,
2102.02356v3, 2311.17526v1, 2512.17676v2), downloaded from arxiv.org on 2026-11-02 and extracted with PyMuPDF, with
typographic ligatures written out and line-break hyphens joined. Journal versions were not read and may differ.
Figures were not seen; what is said about them is what the text says. Everything that is not a quotation, a cited
equation or a stated arithmetic check is ours, unverified.

Why this was read: `docs/design/quantum_toy_brief.md` (step 0) and
`docs/reading/notes/2026-11-02_quantum_graphity_reading.md` (section 6.2) both say that [T17] and [DT17] must be read in
full before anything says the quantum toy's construction is new, and the record cites [T17] as the model's origin
without ever having read it. Rule 13 applies: these papers are targets and benchmarks, never evidence for the owner's
hypothesis.

## 0. The answers, in short (ours, unverified)

1. **The quantum toy is not in [T17] or [DT17].** In [T17] "quantum" means a Euclidean partition function over
   classical graphs, Z = Σ exp(−S_EH/ℏ), with ℏg playing the part of a temperature. There is no Hilbert space of
   graphs, no Hamiltonian with off-diagonal terms and no tunneling between graphs; the "quantum phase transition" is the
   thermal transition of that statistical model. [DT17] builds a quantum state out of one fixed classical graph (two
   copies of a vertex register entangled by the adjacency matrix); the graph itself is never in superposition. The
   nearest thing in the papers of his listing that were read or term-searched is a sentence in [T15net] (2015) that names the missing ingredient and does
   not add it: "If no transverse magnetic fields are applied, model (1) is identical at the classical and quantum
   levels".
2. **No paper of his that was read or term-searched treats the two sides as two kinds of point**, each kind interchangeable. Bipartiteness is
   introduced in [T17] as "just a mathematical simplification", the entropies of [DT17] are invariant under every
   relabeling of the points (no side is singled out), and [T17]'s count of graphs, Eq. (12), counts labeled graphs.
3. **λ appears only at 0, 1 and as a cap.** [T25] runs the global term alone (our λ = 0) and the full Hamiltonian (our
   λ = 1); [KT19] Sec. "The classical limit and the mean field action" uses the square count with configurations above
   2d − 2 squares per edge excluded (our cap). [T17] drops the saturation bracket altogether on the strength of a bound,
   Ns(ij) ≤ 2d − 2, that [KT19] itself withdraws two years later and that the 4-cube breaks. The λ3 and λ4 of [T16lw]
   are different coefficients (of Tr w³ and Tr w⁴) and are not our λ.
4. **For Carroll's reader, [DT17] is a calibration, not a test.** Its state is built from the adjacency matrix, so the
   mutual information between its parts reproduces the wiring by construction (computed below: a constant background
   with a bump exactly at graph distance 1 across the copies and 2 within a copy). Its one number, the "topological
   network entanglement" γ, separates random from ordered graphs but ranks a gas of 4-cubes (γ = 1) above the flat sheet
   (0.887 to 0.899) and barely separates the sheet from the tube. [T25] and [Trugenberger23] state that his programme
   does not take the entanglement route: quantum mechanics is to emerge from classical bits.

## 1. Step 1: the author listing against the record

Search: arXiv API, `search_query=au:Trugenberger`, all years, 2026-11-02; 93 entries returned (totalResults = 93).
Every identifier below was then searched for in `REFERENCES.bib`. Most of the 93 are condensed-matter papers
(superinsulators, Josephson arrays, the quantum Hall effect, confining strings) or quantum memories and do not bear on
the model; they are not listed. The ones on combinatorial quantum gravity, emergent geometry, networks or quantum
behavior of networks:

| arXiv | Year | Title (as on arXiv) | Authors | Record status before today | After today |
|---|---|---|---|---|---|
| 2512.17676 | 2025 | Networks as the fundamental constituents of the universe | Trugenberger | [T25] read in full | term-searched again (sec. 4) |
| 2409.09385 | 2024 | Dark matter and dark energy in combinatorial quantum gravity | Trugenberger | [T24] read in full | term-searched |
| 2311.17526 | 2023 | Combinatorial quantum gravity and emergent 3D quantum behaviour | Trugenberger | [Trugenberger23] read in full | term-searched |
| 2211.01002 | 2022 | Effective de Sitter space, quantum behaviour and large-scale spectral dimension (3+1) | Trugenberger | [T23] read in full | term-searched |
| 2112.03778 | 2021 | Emergent time, cosmological constant and boundary dimension at infinity in combinatorial quantum gravity | Trugenberger | [T22] read in full | term-searched |
| 2102.12329 | 2021 | Enhanced Forman curvature and its relation to Ollivier curvature | Tee, Trugenberger | not in the bib | abstract only |
| 2102.02356 | 2021 | Convergence of Combinatorial Gravity | Kelly, Trugenberger, Biancalana | not in the bib | abstract and Sec. I passage; term-searched |
| 2009.04306 | 2020 | Ollivier-Ricci curvature of random geometric graphs converges to Ricci curvature of their Riemannian manifolds | van der Hoorn, Lippner, Trugenberger, Krioukov | not in the bib | abstract only |
| 2008.11779 | 2020 | Emergence of the Circle in a Statistical Model of Random Cubic Graphs | Kelly, Trugenberger, Biancalana | [KTB20] abstract only | unchanged |
| 2008.01209 | 2020 | Ollivier-Ricci curvature convergence in random geometric graphs | van der Hoorn, Cunningham, Lippner, Trugenberger, Krioukov | not in the bib | abstract only |
| 1901.09870 | 2019 | Self-Assembly of Geometric Space from Random Graphs | Kelly, Trugenberger, Biancalana | [KTB19] read in full | term-searched |
| 1811.12905 | 2018 | Combinatorial Quantum Gravity: Emergence of Geometric Space from Random Graphs | Kelly, Trugenberger | [KT19] read in full | the 2026-10-10 quotation checked against the PDF (sec. 4) |
| 1710.00221 | 2017 | Topological Network Entanglement as Order Parameter for the Emergence of Geometry | Diamantini, Trugenberger | [DT17] abstract only | **read in full** |
| 1610.05934 | 2016 | Combinatorial Quantum Gravity: Geometry from Random Bits | Trugenberger | [T17] not read | **read in full** |
| 1610.05339 | 2016 | Random Holographic "Large Worlds" with Emergent Dimensions | Trugenberger | not in the bib | in part (abstract, Sec. II, Eqs. 1 and 5) |
| 1507.01820 | 2015 | Critical Space-Time Networks and Geometric Phase Transitions from Frustrated Edge Antiferromagnetism | Trugenberger | not in the bib | in part (abstract, Sec. II, the T = 0 passage) |
| 1501.01408 | 2015 | Quantum Gravity as an Information Network: Self-Organization of a 4D Universe | Trugenberger | not in the bib | in part (abstract, Sec. II, end of Sec. III) |

Notes on the listing. The PDF of 1501.01408v2 is titled "Quantum Gravity as a Network Self-Organization of a Discrete
4D Universe", which differs from the API title; the journal reference on arXiv is Phys. Rev. D 92, 084014 (2015). The
other journal references are from the arXiv records and are given in sec. 7. Kelly's thesis [Kelly22] is not on arXiv
and is already in the record. Papers by others in the same programme (for example Gorsky and Valba [GV21]) were not
part of this search.

## 2. [T17] arXiv:1610.05934v3, "Combinatorial Quantum Gravity: Geometry from Random Bits", read in full

Four pages, a letter without section headings, Eqs. (1) to (14) and one figure. JHEP 09 (2017) 045 per the arXiv DOI.

**What "quantum" means.** The abstract: "I propose a quantum gravity model in which geometric space emerges from random
bits in a quantum phase transition driven by the combinatorial Ollivier-Ricci curvature and corresponding to the
condensation of short cycles in random graphs." The model is Eq. (1), Z = Σ_CS exp(−S_EH/ℏ), S_EH = −(1/2g) Tr w⁴,
"where w denotes the adjacency matrices of the graphs in CS, ℏ is the Planck constant and g is the gravity coupling
constant with dimension 1/action. The dimensionless quantity ℏg will play the role of effective “temperature” in this
statistical field theory model." Eq. (10) writes the same thing as a Boltzmann probability over graphs. That is the
whole of the quantum structure: a sum over classical graphs with a weight that contains ℏ. There is no Hilbert space,
no state vector, no operator acting between graphs and no time. [KT19] says the same in its section "The classical
limit and the mean field action": "The classical limit ℏ→0 corresponds to the weak coupling limit of small g. In the
quantum regime ℏg ≫1 the Boltzmann probability becomes uniform over all configuration space". *Ours:* "quantum phase
transition" here is the Euclidean-path-integral usage (a transition in a coupling that multiplies 1/ℏ), which is, as a
calculation, a classical thermal transition in the coupling ℏg. It is the same kind of object our toy samples (at λ = 0, the same object), with our g in
place of his ℏg up to normalization.

**The configuration space.** "a simplified toy model in which the configuration space CS is restricted to diluted random
regular bipartite graphs." "By “diluted” graphs I mean graphs in which two different elementary squares can share
maximally one edge. This is a loop-equivalent of a hard core requirement in a classical gas: the elementary constituent
can touch but not overlap. Note that this restriction of the configuration space has nothing to do with any fundamental
requirement, it is just a mathematical simplification that makes the toy model easily tractable." The degree is even,
k = 2d. *Ours, exact:* in a bipartite graph two distinct squares sharing two edges must share two adjacent edges i-j,
j-k, which gives i and k three common neighbors; so "squares share at most one edge" is the same rule as the record's
hard-core rule (no two points with more than two common neighbors; ASSUMPTIONS Q2).

**The energy.** Eq. (5) is the Ollivier curvature for bipartite regular graphs with the [·]₊ bracket; Eq. (6) reduces it
to κ(i, j) = −(1/d)[(2d − 2) − Ns(ij)] with the bracket dropped: "Note also that I have left out the subscript “+”.
This is because, for squares sharing maximally one edge Ns(ij) ≤ (2d −2), as I now show." The argument that follows
counts the squares of "the uniform configuration with maximum square density" and concludes "Ns(ij) ≤ 2d − 2". Eq. (7)
integrates the curvature, Σ κ(i) = −(4/d²)[d(d − 1)N/2 − Ns]; Eq. (8) relates Ns to Tr w⁴; Eq. (9) is S_EH as the
curvature sum plus a constant.

*Ours, exact:* the bound in Eq. (6) does not hold edge by edge. The argument is about the average of a uniform
configuration. The 4-cube is 4-regular (d = 2), bipartite and obeys the hard-core rule, and every one of its edges
carries 3 squares, more than 2d − 2 = 2 (the record's `test_four_cube_energies`). [KT19] withdraws the bound in so many
words: "The number of squares based on an edge, however, can be larger than (2d −2) even for graphs with hard core
squares, indeed it can reach up to (2d −1)." [T17]'s model is defined by Eq. (1), S_EH = −(1/2g) Tr w⁴, which on regular graphs is the square count plus a
constant, so the action of its Fig. 1 is our λ = 0 end of the knob with the hard-core rule by definition; Eq. (6) only
misidentifies it with the full curvature. *Ours, arithmetic:* Eq. (8) as printed, Ns = (1/8)(Tr w⁴ − 8Nd² + 2dN), checks out (4-cube:
Tr w⁴ = 640 = 8·24 + 8·4·16 − 2·2·16; 8 × 8 torus: 2304 with 64 squares).

**The simulation and the claimed transition.** Fig. 1: "Monte Carlo simulation of the average number of squares for
d = 4 and N = 300, N = 400 and N = 500 as a function of the rescaled coupling ℏg/√N." So the only published run of the
origin paper is at d = 4, eight links a point, the record's D = 4, not the four-link case. The rescaling ℏg/N^(1−2/d)
comes from the continuum argument of Eq. (14). The claim: "The correct scaling is evident and this result strongly
suggests a second-order transition with critical point ξc ≃ 500 − 1000, which would define the model
non-perturbatively." The size of the evidence is three sizes and no stated run lengths. On entropy: "the numerical
evidence is that, at finite ζ = O(1) the entropy scales with a power of N smaller than one", and from the scaling, "the
graph entropy in the geometric phase scales as S(N) ∝ N^(2/d)", which the paper calls "a combinatorial version of the
celebrated entropy area law". On time: "there is nothing fundamental about time."

**Counting.** Eq. (12) gives the number of 2d-regular bipartite graphs on N vertices, (dN)! e^(−(2d−1)²/2)/((2d)!)^N,
cited to O'Neil and Wormald. *Ours:* that formula counts labeled graphs, so the entropy of [T17] is the named-points
entropy.

## 3. [DT17] arXiv:1710.00221v1, "Topological Network Entanglement as Order Parameter for the Emergence of Geometry", read in full

Four pages, a letter, Eqs. (1) to (14), one figure. New J. Phys. (2017), DOI 10.1088/1367-2630/aa8f08.

**The model it uses** is [T17] verbatim: Eq. (1) is [T17] Eq. (1) on "dilute random regular bipartite graphs", Eqs. (2)
and (3) are [T17] Eqs. (9) and (7). On the transition it is more cautious than [T17]: "Present data are, however not
yet sufficient to definitively conclude that the crossover region for finite N develops into a second-order phase
transition when N →∞, although this picture looks very suggestive."

**What entanglement is computed, of what state.** Not the entanglement of a quantum state of the graph. Each classical
graph is turned into a state: "Every classical graph, however can be viewed as the entanglement in the quantum
superposition of two disconnected quantum states [12]." Eq. (4): |w⟩ = (1/‖w‖_F) Σ_{i,j} w_ij |i⟩|j⟩ on two copies of
C^N, one basis vector per vertex. "This state can be considered either as the quantum state of two N-level systems or
the quantum state of two N-qubit states each constrained to the one-excitation manifold." Copy 2 is traced out, Eq. (5):
ρ = w wᵀ / Tr wᵀw. Its entropies depend only on the spectrum of w: "Note that these are insensitive to all re-labelings
of the vertices and depend thus only on the isomorphism class of the particular graph." Rényi entropies behave as
S_k = log₂N − γ_k + O(1/n) (as printed; N is meant), Eq. (8); γ₂ and γ₃ are written through the densities of squares and hexagons, Eq. (10); the
von Neumann limit gives Eq. (14), γ = Tr(w² log₂ w²)/Tr w² − log₂ 2d, "the topological network entanglement". Fig. 1
plots γ against d = 2 to 6 in the geometric and random phases, computed by starting from a torus (a circulant graph),
measuring γ, then running Metropolis at large g until the square count falls to the random value and measuring again.
The claim: "the emergence of geometric order increases the topological network entanglement, thereby decreasing the
overall entanglement entropy. This effect is largest in four dimensions, where the entanglement entropy of the geometric
phase has a local minimum." The "mixed quantum state" of the abstract is ρ.

**The reference to Carroll.** "It is this beautiful equivalence, first established in [12] that permits to interpret
emergent space, as encoded in the ordering of random graphs, as a quantum entanglement pattern, an approach also
recently suggested in [17]." [17] is "C. Cao, S. M. Carroll and S. Michalakis, Phys. Rev. D95 (2017) 024031", our
[CCM16]. [12] is Garnerone, Giorda and Zanardi, our [GGZ12] (abstract only), spelled "Garneroni" in [DT17]'s list.

**Two checks of ours, exact (computed 2026-11-02 with NumPy and networkx, not part of the record's code):**

- *A misprint in Eq. (9).* It gives Tr w⁴ = 8Ns + d²N − 2dN. For a 2d-regular graph the closed four-step walks give
  Tr w⁴ = 8Ns + 8d²N − 2dN, as in [T17] Eq. (8); for the 8 × 8 torus Eq. (9) gives 512 where the trace is 2304. The
  printed γ₂ of Eq. (10) inherits the misprint (ours, exact): γ₂ = log₂(Tr w⁴/(4d²N)) = log₂(2Ns/(d²N) + (4d − 1)/(2d)),
  not the printed constant (d − 2)/(4d); on the 8 × 8 torus the printed form gives log₂ 0.5 = −1 where the trace gives
  log₂ 2.25.
- *γ on the toy's states* (four links, d = 2, from Eq. (14)): 4-cube, or any gas of 4-cubes, 1.000; flat sheet 8 × 8,
  0.899; 16 × 16, 0.887; tube 4 × 16, 0.887; 4 × 64, 0.885; random bipartite 4-regular graphs, 0.603 to 0.611 at
  N = 256 and 0.596 to 0.598 at N = 1024 (five each). So γ is high for ordered graphs and low for random ones, as
  [DT17] says, but it ranks the shattered knots above flat space and separates the sheet from the tube by 0.012 at N = 64
  and 0.002 at N = 256. As a detector of "geometry" in the hypothesis's sense it reads closed knots as the most geometric
  state there is.

## 4. Other papers, briefly

**[T15net] arXiv:1501.01408v2** (Phys. Rev. D 92, 084014). Abstract, Sec. II "The model", the end of Sec. III. Spins
s_i = ±1 on N points and link bits w_ij = 0, 1 on all pairs, Eq. (1): H = (J/2) Σ w_ik w_kj − (1/2) Σ s_i w_ij s_j, a
ferromagnetic Ising term on points and an antiferromagnetic one on links; ground states are regular graphs with degree
set by J. The paragraph that matters for the quantum toy: "the Hamiltonian (1) appears at first sight as a purely
classical one. ... If no transverse magnetic fields are applied, model (1) is identical at the classical and quantum
levels since all σ3 Pauli matrices attached to vertices and edges commute. The graph configurations of minimal energy
that survive in the T = 0 partition function can thus be taken to represent the residual zero-temperature quantum
fluctuations." And: "Typically, a Hamiltonian H = H0+JH1 can display non-analiticity in its ground state if H0 and H1
commute, exactly as in the present model, leading to level-crossings at particular values of J while the wave functions
remain the same [32]." *Ours:* his "quantum phase transitions" are level crossings of commuting terms; the transverse
field that would make links quantum is named and explicitly not applied. The quantum toy's −Γ term is a transverse
field of that kind, constrained to switches.

**[T15af] arXiv:1507.01820v2** (Phys. Rev. E 92, 062818). Abstract and Sec. II. A mean-field solution of the edge part
of [T15net] on a bipartite 2d-regular graph; edges are split into "light and dark colours" by König's theorem, the
"staggered magnetization" is between those two edge classes, and at T = 0 "the quantum phase transition is of
first-order", again a level crossing. The two colors are of edges, not points.

**[T16lw] arXiv:1610.05339v1** (Phys. Rev. E 94, 052305; [T17]'s ref. [16]). Abstract and Sec. II. [T15net]'s model
plus Eq. (5), H1 = (λ3/3) Tr w³ − (λ4/4) Tr w⁴, "a small perturbation ... that favours the formation of squares, while
suppressing the triangles", with λ3 = 0.01. These λs are coefficients of cycle counts, not the toy's λ; the record
should not mix them up. The square-counting argument later reused in [T17] (each edge "shared by 2d − 2 squares" in the
uniform configuration) appears here first.

**[KTB21conv] arXiv:2102.02356v3** (DOI 10.1103/PhysRevD.105.124002, so published 2022). Abstract and Sec. I. A
discrete Einstein-Hilbert action that converges on random geometric graphs, "for a slightly different action to the one
adopted in [81–83]". On the name: "calling the associated Ollivier curvature based model combinatorial quantum gravity
due to a formal analogy with Einstein gravity", and the convergence "is of course necessary if we wish to pursue a
putative dynamical quantum model." Configurations are "sequences of (unlabelled weighted) graphs". No coefficient other
than the action's own was seen in the passages read; the paper was term-searched, not read.

**[TT21] arXiv:2102.12329v2** (DOI 10.1209/0295-5075/133/60006), **[vdH21] arXiv:2008.01209v2** (Phys. Rev. Research 3,
013211) and **[vdH23] arXiv:2009.04306v2** (Discrete Comput. Geom. 70, 671). Abstract only. The first relates Forman and
Ollivier curvature on a class of graphs (relevant to [T25]'s remark that the global term is the Forman Hamiltonian); the
other two are the convergence theorems of Ollivier to Ricci curvature that [T25]'s section on convergence relies on.

**Term searches of the papers already read** ([T22], [T23], [Trugenberger23], [T24], [T25], [KTB19], [KT19]) for
"transverse", "Hilbert space", "superposition", "off-diagonal", "wave function", "quantum state", "density matrix",
"entangle", "mutual information", "unlabel", "two colo(u)r", "bipartition": no Hilbert space of graphs and no
off-diagonal term in any of them. Two sentences state the programme's position. [Trugenberger23], Introduction: "This
idea is the basis for emergent quantum gravity models in which space-time emerges from entanglement of microscopic
quantum degrees of freedom [18]. Contrary to this approach, as we will see, in the present model gravity and quantum
mechanics emerge simultaneously from classical bits." [T25], Introduction: "We would also like to stress that
(undirected) graphs can always be interpreted as quantum entanglement patterns [20], although this is not the route we
will pursue here." ([20] is [GGZ12].) [T25] abstract: "In this model, both gravity and quantum mechanics are macroscopic
statistical effects reflecting the free energy minimization of fundamental binary degrees of freedom."

**[KT19]'s sentence on the cap, checked against the PDF** (the 2026-10-10 bib note asked for this). The section "The
classical limit and the mean field action" of 1811.12905v1 reads: "Having established that the hard-core condition is
sufficient to stabilize space and obtain the correct (formal) continuum limit we can adopt the simpler mean field action
expressed in terms of the total number of squares provided we explicitly exclude configurations with more than (2d −2)
squares per edge." The HTML-derived quotation in the bib agrees with the PDF word for word.

## 5. The four questions (ours, unverified)

**(1) Is the quantum toy already in [T17] or [DT17] in some form?** No. [T17]'s "quantum" is ℏ in a Euclidean weight
over classical graphs (Eq. (1); "ℏg will play the role of effective “temperature”"); its configuration sum is the
classical toy's ensemble, with the bracket dropped. [DT17] puts a quantum state on top of one fixed graph (Eq. (4)) and
never superposes graphs or moves between them. Neither has a −Γ switch term, a ground state over graphs, or anything
about stoquasticity or quantum Monte Carlo. The closest statement anywhere in his listing is [T15net]'s "If no
transverse magnetic fields are applied, model (1) is identical at the classical and quantum levels", which identifies
the off-diagonal term as what would make his models quantum and leaves it out. Search behind this answer: his arXiv
listing (93 entries, 2026-11-02), all CQG and network papers read in full or term-searched for the terms above. This
covers his own work only; the wider search for the construction is the quantum graphity note's section 4.1, and a rule
15 note on the template is still owed before any page says the construction has not been found in print.

**(2) Black and white points as distinguishable kinds, each kind identical?** Not in any paper read. The bipartite
choice is a convenience in every case: [T17] "just a mathematical simplification"; [T25] "To make numerical simulations
less computationally intensive one can use bipartite graphs". [DT17]'s quantities are invariant under all relabelings,
which includes swapping the sides, so they treat all points as interchangeable, not two kinds. [T17] Eq. (12) counts
labeled graphs, so his entropy is the named-points one. [KTB21conv] calls its configurations "unlabelled weighted
graphs" in the sense of metric spaces, not as a statistical ensemble. [T15af]'s two classes are classes of edges, not
of points. So the record's T10 knob (interchangeable points) and any two-kind version of it are ours.

**(3) λ other than 1?** Only 0, 1 and the cap, as the 2026-09-23 literature check found. [T25], section "The emergence
of hyperbolic manifolds", around Eq. (22): "If only the global term is retained, the model undergoes a first-order phase
transition ... If the full Hamiltonian is used, instead the model undergoes a continuous phase transition", and on the
tie at λ = 1: "these two effects cancel exactly when a configuration with D(D-1)/2 squares per vertex and (2D-2) squares
per edge is reached. Configurations with a higher number of squares (the maximum per edge is (2D-1) by regularity) are
degenerate with this one." [KT19]: the cap. [T17]: the bracket dropped on a bound that does not hold edge by edge, so
its text is silently at λ = 0 while it believes it is at the full curvature. The paper that founded the model thus
treats the λ question as absent rather than as a choice. [T16lw]'s λ3 and λ4 are unrelated coefficients.

**(4) What these papers add to reading the toy with Carroll's mutual-information geometry.**

- [DT17] is the one place in his work where a CQG graph is read through entanglement, and it cites [CCM16]. But its state
  is built from the adjacency matrix. *Ours, computed on the 8 × 8 torus in the one-excitation reading of Eq. (4):* the
  mutual information between vertex qubit i of copy 1 and qubit j of copy 2 is 1.17 × 10⁻² bits when i and j are
  neighbors and 3.6 × 10⁻⁴ (a constant background from the single excitation) otherwise; within copy 1 it is
  6.3 × 10⁻³ for distance-2 pairs with two common neighbors (diagonal) and 1.8 × 10⁻³ for those with one (straight),
  4.0 × 10⁻³ on average, and the same background elsewhere. Carroll's reader on this
  state returns the wiring, or its distance-2 graph, because that is what was put in. That makes [DT17]'s state a ready
  calibration for step 2 of the brief (a state whose geometry is known), and nothing more: it cannot test whether a
  dynamics produces the geometry.
- γ is a single spectral number per graph, not a geometry. It sorts random from ordered and ranks knots above space
  (sec. 3), so it is no substitute for multidimensional scaling of a mutual-information matrix; it could be recorded
  alongside, cheaply, on every saved wiring.
- The quantum toy's ground state, unlike [DT17]'s state, is a superposition of wirings, and the factors Carroll's reader
  needs (one per point) are not the [DT17] factors (one vertex register per copy). Which factorization to use remains the
  open choice named in the quantum graphity note (its point 4: on the exact, rename-invariant ground state, pair mutual
  information takes at most two values).
- The programme's own position, quoted in sec. 4, is that quantum mechanics emerges from classical bits and that the
  entanglement route "is not the route we will pursue". A quantum toy therefore departs from the published model's
  stance as well as from its rule, and any page should say so; at λ ≠ 1 it is our family in any case.
- [T17]'s area-law remark (geometric-phase entropy ∝ N^(2/d)) and [T17]'s ref. [15], which cites Jacobson 1995 and 2016
  beside Bekenstein, are the only contact between his work and Jacobson's route that these papers show; neither is
  developed.

## 6. Read-status table

| Key | arXiv | Status after 2026-11-02 | By |
|---|---|---|---|
| [T17] | 1610.05934v3 | read in full (all of it: Eqs. 1 to 14, Fig. 1 caption) | assistant agent |
| [DT17] | 1710.00221v1 | read in full (Eqs. 1 to 14, Fig. 1 caption) | assistant agent |
| [T15net] (new) | 1501.01408v2 | in part: abstract, Sec. II, end of Sec. III | assistant agent |
| [T15af] (new) | 1507.01820v2 | in part: abstract, Sec. II, the T = 0 passage | assistant agent |
| [T16lw] (new) | 1610.05339v1 | in part: abstract, Sec. II (Eqs. 1, 5) | assistant agent |
| [KTB21conv] (new) | 2102.02356v3 | in part: abstract, Sec. I passage; term-searched | assistant agent |
| [TT21] (new) | 2102.12329v2 | abstract only | assistant agent |
| [vdH21] (new) | 2008.01209v2 | abstract only | assistant agent |
| [vdH23] (new) | 2009.04306v2 | abstract only | assistant agent |
| [KT19] | 1811.12905v1 | read in full (unchanged); cap quotation checked against PDF | earlier; check today |
| [T22], [T23], [T24], [T25], [Trugenberger23], [KTB19] | | read in full (unchanged); term-searched today | earlier |
| [KTB20] | 2008.11779 | abstract only (unchanged) | |

## 7. Lines for REFERENCES.bib

Replace the note of **[T17]** with:

```
note    = {read-full (2026-11-02, by an assistant agent, arXiv v3 PDF extracted with PyMuPDF; the owner has not read it): docs/reading/notes/2026-11-02_trugenberger_remaining.md. Title, authors and DOI 10.1007/JHEP09(2017)045 checked against the arXiv record that day. "Quantum" is a Euclidean weight exp(-S_EH/hbar) over classical graphs, hbar g acting as temperature; no Hilbert space of graphs. "Diluted" = squares share at most one edge = our hard-core rule. Eq. (6) drops the [.]_+ bracket on a bound N_s(ij) <= 2d-2 that does not hold edge by edge (the 4-cube; withdrawn in KT19). The one simulation, Fig. 1, is at d = 4 (eight links), N = 300 to 500. Eq. (12) counts labeled graphs.}
```

Replace the note of **[DT17]** with:

```
note    = {read-full (2026-11-02, by an assistant agent, arXiv v1 PDF; the owner has not read it): docs/reading/notes/2026-11-02_trugenberger_remaining.md. Supersedes "Abstract only". Entanglement of a two-copy state built from one classical graph's adjacency matrix (Eq. 4), not of a superposition of graphs; gamma (Eq. 14) is a spectral number per graph. Cites Cao, Carroll and Michalakis [CCM16] as its ref. [17]. Eq. (9) misprints Tr w^4 (d^2 N for 8 d^2 N; ours, exact). Journal reference on arXiv is a manuscript number ("NJP-106741.R3 (2017)"); volume and page to verify.}
```

New entries (fields from the arXiv API on 2026-11-02; journal fields to verify against the publisher before citing):

```
@article{T15net,
  author  = {Trugenberger, Carlo A.},
  title   = {Quantum Gravity as an Information Network: Self-Organization of a 4D Universe},
  journal = {Phys. Rev. D}, volume = {92}, pages = {084014}, year = {2015},
  doi     = {10.1103/PhysRevD.92.084014}, eprint = {1501.01408}, archivePrefix = {arXiv},
  note    = {Read in part (abstract, Sec. II, end of Sec. III) by an assistant agent, 2026-11-02: docs/reading/notes/2026-11-02_trugenberger_remaining.md. The v2 PDF's title differs from the API title ("Quantum Gravity as a Network Self-Organization of a Discrete 4D Universe"). States that without transverse fields the model is identical at the classical and quantum levels.}
}
@article{T15af,
  author  = {Trugenberger, Carlo A.},
  title   = {Critical Space-Time Networks and Geometric Phase Transitions from Frustrated Edge Antiferromagnetism},
  journal = {Phys. Rev. E}, volume = {92}, pages = {062818}, year = {2015},
  doi     = {10.1103/PhysRevE.92.062818}, eprint = {1507.01820}, archivePrefix = {arXiv},
  note    = {Read in part (abstract, Sec. II, the T = 0 passage) by an assistant agent, 2026-11-02: same note.}
}
@article{T16lw,
  author  = {Trugenberger, Carlo A.},
  title   = {Random Holographic "Large Worlds" with Emergent Dimensions},
  journal = {Phys. Rev. E}, volume = {94}, pages = {052305}, year = {2016},
  doi     = {10.1103/PhysRevE.94.052305}, eprint = {1610.05339}, archivePrefix = {arXiv},
  note    = {Read in part (abstract, Sec. II, Eqs. 1 and 5) by an assistant agent, 2026-11-02: same note. Its lambda_3 and lambda_4 multiply Tr w^3 and Tr w^4; they are not the toy's lambda.}
}
@article{KTB21conv,
  author  = {Kelly, Christy and Trugenberger, Carlo and Biancalana, Fabio},
  title   = {Convergence of Combinatorial Gravity},
  doi     = {10.1103/PhysRevD.105.124002}, eprint = {2102.02356}, archivePrefix = {arXiv},
  note    = {Read in part (abstract, a Sec. I passage; term-searched) by an assistant agent, 2026-11-02: same note. Journal volume from the DOI only; year and pages to verify.}
}
@article{TT21,
  author  = {Tee, Philip and Trugenberger, C. A.},
  title   = {Enhanced Forman curvature and its relation to Ollivier curvature},
  doi     = {10.1209/0295-5075/133/60006}, eprint = {2102.12329}, archivePrefix = {arXiv},
  note    = {Abstract only, by an assistant agent, 2026-11-02: same note. Journal from the DOI only, to verify.}
}
@article{vdH21,
  author  = {van der Hoorn, Pim and Cunningham, William J. and Lippner, Gabor and Trugenberger, Carlo and Krioukov, Dmitri},
  title   = {Ollivier-Ricci curvature convergence in random geometric graphs},
  journal = {Phys. Rev. Research}, volume = {3}, pages = {013211}, year = {2021},
  doi     = {10.1103/PhysRevResearch.3.013211}, eprint = {2008.01209}, archivePrefix = {arXiv},
  note    = {Abstract only, by an assistant agent, 2026-11-02: same note.}
}
@article{vdH23,
  author  = {van der Hoorn, Pim and Lippner, Gabor and Trugenberger, Carlo and Krioukov, Dmitri},
  title   = {Ollivier curvature of random geometric graphs converges to Ricci curvature of their Riemannian manifolds},
  journal = {Discrete Comput. Geom.}, volume = {70}, pages = {671--712}, year = {2023},
  doi     = {10.1007/s00454-023-00507-y}, eprint = {2009.04306}, archivePrefix = {arXiv},
  note    = {Abstract only, by an assistant agent, 2026-11-02: same note.}
}
```

And append to the note of **[KT19]**: "2026-11-02: the Sec. IV quotation on excluding configurations with more than
(2d − 2) squares per edge checked against the v1 PDF and found word for word (heading there: 'The classical limit and
the mean field action'); the same section says the squares on an edge 'can reach up to (2d −1)' with hard-core squares,
withdrawing [T17]'s bound."

Verified against the sources by a second agent on 2026-11-02 (every load-bearing quotation found; the Eq. (9) misprint confirmed by exact traces; every γ reproduced); its corrections applied the same day, including the distance-2 mutual information, which has two values, not one.

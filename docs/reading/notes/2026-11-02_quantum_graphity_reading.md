# Reading note: quantum graphity, the published relative of the quantum toy

Date: 2026-11-02. By an assistant agent (Claude Opus 5.5). The owner has not read these passages. Every quotation is
from the arXiv text (hep-th/0611197v1; 0801.0861v2; 0808.2495v2; 1008.1340v3; 0911.5075v3; 1108.2013v3; 1203.5367v2;
1506.07588v1; 1808.05632v1), extracted from the PDFs with PyMuPDF on 2026-11-02, with typographic ligatures ("fi",
"fl") written out. The journal versions were not read and may differ in wording. Equation and section numbers are the
arXiv PDFs'. Figures were not seen; what is said about them is what the text says. Everything that is not a quotation
or a cited equation is ours, unverified, unless marked otherwise.

Why this was read: step 0 of `docs/design/quantum_toy_brief.md`, which names quantum graphity ([KMS06]; [KMSev08];
[HMPS09]) as the published model with the brief's shape (a diagonal cost plus hopping between graphs) and asks for it
to be read before anything is built.

Rule 13 applies throughout: these papers are targets and benchmarks for the quantum toy, never evidence for the owner's
hypothesis. Where a result here resembles one of the toy's, that is a resemblance between two models, recorded so that
it can be checked, and nothing more.

## 0. The answer in five lines (ours, unverified)

1. In the quantum graphity papers read, the graph-changing term is written down ([KMSev08] Eqs. 27, 28) or only
   drawn ([KMS06] Fig. 1), its coupling's sign is never fixed, and it is never studied as a quantum term: the low phase
   is argued from the diagonal energy with the graph frozen. Nothing read here says anything about stoquasticity or
   quantum Monte Carlo, and no paper read samples a superposition of graphs beyond four vertices.
2. The brief's H = H0 + H1 is the same shape as [KMSev08]'s "free" terms plus its exchange term, with three differences
   that matter: Trugenberger's curvature in place of the valence-plus-all-loops energy; qubit (hard-core) edges with a
   fixed negative sign in place of fermionic edges with an unfixed sign; and switches between any two edges in place
   of a local exchange.
3. The last difference is physics, not bookkeeping. With switches between any two edges the hopping term has of order
   N squared terms per state against an energy of order N, so a quantum transition would sit at a coupling that
   falls like 1/N, the quantum form of the zero-temperature transition that quantum graphity papers report.
4. The exact ground state at any Γ > 0 is invariant under renaming the points, so the mutual information between two
   points takes at most two values, one for pairs on the same side and one for pairs on opposite sides: Carroll's reader
   on the exact ground state sees a complete (bipartite) pattern, not a lattice.
   The reader needs a state in which that symmetry is broken, or a different choice of factors.
5. Path-integral quantum Monte Carlo of a stoquastic model gives equilibrium (imaginary time), not real-time decay, so
   the brief's step 3 question "does a curled tube decay faster with Γ" has to be restated before it is pre-registered.

## 1. Konopka, Markopoulou and Smolin, "Quantum graphity" [KMS06], read in full

All sections (I to VI), Eqs. (1) to (34). Fourteen pages; no simulation of any kind.

### 1.1 Hilbert space

Classical model (Sec. II.A): the complete graph on N points, each edge carrying labels "(J, M) ∈ {(0, 0), (1, −1),
(1, 0), (1, 1)}" (Eq. 1), (0, 0) meaning the link is off. Quantum model (Sec. II.B): "On each edge we put a four state
Hilbert space, Hspin" spanned by |j, m⟩ (Eq. 9), and the whole space is the tensor product over the N(N − 1)/2 edges
(Eq. 10). The operators J, M, M± act on each edge (Eqs. 11, 12); they "annihilate the |0, 0⟩ state" (Eq. 14) "and ...
all non-zero matrix elements have unit magnitude" (text after Eq. 14).

### 1.2 The Hamiltonian, term by term

H = Hlinks + Hvertices + Hloops + Hhop + HLQG (Eq. 2; quantum form Eq. 15).

- **Valence, Hlinks = V Σ_a (v0 − Σ_b J_ab)²** (Eq. 3). "The minimum of Hlinks occurs when the number of 'on' links
  adjacent to every node in the graph is v0."
- **Vertices, Hvertices = C Σ_a (Σ_b M_ab)² + D Σ_ab M_ab²** (Eq. 4). C favors the m values at a point summing to zero
  (ours: the analogue of Gauss's law); D is a string tension.
- **Loops, Hloops = −Σ over minimal loops (1/L!) B(L) Π M_i** (Eq. 5), with B(L) = B0 B^L (Eq. 7). The weight B^L/L!
  peaks at a "preferred loop length" L* (Eq. 8). In the quantum model the product is M⁺_ab M⁻_bc ... M⁺_yz M⁻_za (Eqs.
  16, 17), so only even lengths L = 4, 6, 8, ... enter. "Note that Hloops has an overall minus sign."
- **Hhop and HLQG are not given.** "We will not need to specify these in detail, except to say that Hhop allows the M
  variables to propagate from an on edge to other edges adjacent to the same vertex, and the term HLQG generates local
  moves that turn edges on and off" (Sec. II.A, after Eq. 8; restated in other words in Sec. II.B). And the assumption that governs the
  whole paper: "We assume that the couplings characterizing these terms are such that they do not significantly alter
  the equilibrium and ground states of the model."
- Constants: "four dimensionful coupling constants (V, C, D, and B0) and three dimensionless numbers (N, B and v0)",
  with "N ≫ 1, C ≫ D, and V ≫ 1" (end of Sec. II).

### 1.3 Phases and how geometry emerges

- **High temperature** (Sec. III.A): with the M terms ignored, Z_N ≈ Z_1^N (Eq. 18), f(v) = V(v − v0)² − v kT ln 3
  (Eq. 21), so the typical valence grows linearly with T, v = v0 + kT ln 3/(2V) (Eq. 22). The graph is random with edge
  probability p ∼ T/(NV) (Eq. 23); "When the temperature T is on the order of NV, almost all edges in the complete
  graph will be 'on.'"
- **Low temperature** (Sec. III.B): valence frozen at v0; "we assume that the amplitudes of the LQG terms are very small
  so that any low lying excitations do not change the patterns of 'on' and 'off' links." The loop term selects the
  lattice: with L* = 4 a square lattice, with L* = 6 the diamond lattice (Fig. 2). String condensation on the square
  lattice requires 2D − (1/4!) B0 B⁴ < 0 (Eq. 24), written 48γD = B0 B⁴ with γ > 1 (Eq. 25). Whether these lattices are
  the ground states: "We cannot fully answer this question at this point." The argument offered is that the moves
  "do not disconnect graphs and act equally on all possible edge configurations", so the ground state "should be
  connected and homogenous".
- **Gauge fields** (Sec. IV): with the links frozen in a cubic pattern (v0 = 6) the low-energy Hamiltonian is
  H_lowT ∼ D Σ M_ab² − (1/4!) B0 B⁴ Σ Π M± (Eq. 27), rewritten with plaquette operators W as
  D Σ M_ab² − (1/3!) B0 B⁴ Σ (W + h.c.) (Eq. 29), compared with the Kogut-Susskind Hamiltonian (Eq. 30), giving
  g² = (2γ)^(−1/2), a weak coupling (Eq. 32). *Ours: the prefactor changes from 1/4! in Eq. 27 to 1/3! in Eq. 29 with no
  stated reason; recorded as read, not judged.* The correspondence "is not exact because ... the m labels in our model
  can only take three values".
- **Cosmology** (Sec. V): a transition from the hot phase, where the graph diameter is about log N, avoids the horizon
  problem.

### 1.4 Sign structure, Monte Carlo, light cones, matter, gravity

- **Signs.** No statement anywhere about the sign of off-diagonal terms or about Monte Carlo. *Ours, unverified:* in the
  |j, m⟩ product basis every M± element is non-negative (Eq. 12, "unit magnitude"), so the loop term with B0 > 0 and
  B > 0 has non-positive off-diagonal elements; Hhop and HLQG are unspecified, so the whole Hamiltonian's sign structure
  is undetermined.
- **Matter**: the m labels give "photons coupled to massive charged particles" (Sec. I), by string-net condensation as
  in Levin and Wen ([LW06] among their refs. 4 to 6).
- **Gravity, stated as not done**: "Apart from constructing a geometry, we have not attempted to reproduce features of
  gravitational physics such as gravitons in our model" (Sec. VI). And the matter cannot be switched off: "the matter
  degrees of freedom play an essential role in organizing the links into a regular lattice structure" (Sec. VI).
- **Light cones**: not discussed.

## 2. Konopka, Markopoulou and Severini, "Quantum graphity: a model of emergent locality" [KMSev08], read in full

All sections (I to VI), Eqs. (1) to (58), Table I. Twenty-six pages.

### 2.1 Hilbert space

Degrees of freedom on edges only: "The basic Hilbert space associated with an edge is chosen to be that of a
fermionic oscillator", H_edge = span{|0⟩, |1⟩} (Eq. 4), and the total space decomposes as a direct sum over all
subgraphs G of K_N (Eq. 6). "Since we treat the vertices as distinguishable, there may be many blocks in the sum that
correspond to isomorphic graphs" (after Eq. 6): named points, in the toy's language. Edge operators a, a† obey
{a, a†} = 1 (Eq. 8). Path counts come from normal-ordered powers of the number operators, :N^(L)_ab: (Eqs. 11 to 14),
so that "the eigenvalues of operators :N^(L)_ab: for each a, b return the number of nonoverlapping paths between
vertices a and b".

### 2.2 The Hamiltonian, term by term

- **Valence, H_V = g_V Σ_a exp[p (v0 − Σ_b N_ab)²]** (Eq. 17); the penalty per point "scales roughly with the
  exponential of the valence difference squared" (Eq. 19).
- **Closed paths, H_B = Σ_a H_Ba, H_Ba = −g_B Σ_b δ_ab exp(r N_ab)** (Eqs. 20, 21), so that
  E_B(G) = −Σ_a Σ_L g_B(L) P(a, L) with g_B(L) = r^L g_B/L! (Eqs. 23, 24), P(a, L) the closed nonoverlapping paths
  of length L at a. Terms start at L = 3. With r negative "even cycles can lower the energy of a graph while odd cycles
  incur it a positive energy penalty" (end of Sec. II.C.2).
- **Interaction terms, the graph-changing part.** "The previous terms H_V and H_B can be thought of as being terms in a
  'free' graph model - they are eigenoperators of graph states and do not change the linking structure between
  vertices" (Sec. II.C.3). Two are written:
  - Exchange (Fig. 1a, "Exchange moves preserve the valence of each vertex"):
    H(exch) = g(exch) Σ' N_ab (a†_ad a†_bc a_bd a_ac) (Eq. 27), over distinct a, b, c, d: removes edges ac and bd and
    adds ad and bc, "if and only if the link between vertices a and b is on".
  - Addition and subtraction (Fig. 1b, "type III"): H(add) = g(add) Σ' N_ab N_ac (a_bc + a†_bc) (Eq. 28), which
    toggles edge bc when ab and ac are both on.
  - "The couplings gexch and gadd determine how likely the interactions are to happen. In the next section, we mainly
    study static or equilibrium configurations of links and therefore ignore the interactions." No sign is given for
    either coupling.
- **Matter extension** (Sec. IV): the on state splits into |1, m⟩, m = −1, 0, +1 (Eqs. 41, 43);
  H = H_V + H_B + H_C + H_D + H± (Eq. 48), with H_C = g_C Σ_a (Σ_b M_ab)² (Eq. 49), H_D = g_D Σ M_ab² (Eq. 50) and
  H± = −Σ over cycles g±(L) Π M± (Eq. 51), g±(L) = r^L g±/L! (Eq. 53). "Actually, the original quantum graphity was
  written only with the H± term, without the HB term. Both are included here because this makes it easier to separate
  the graph-forming role of HB from the matter propagation role of H±."

### 2.3 What was computed, and how

- No simulation. Cycle counts up to length 20 on four hand-built candidate 3-regular graphs (hexagonal, "braided
  line", "braided tree", heptagonal; Figs. 2, 3), at r = 7.3; the hexagonal lattice wins only once cycles up to about
  20 are counted, for |r| ≳ 7.1 (Eq. 32).
- **A curled state wins**: "If an arrangement of hexagons as in Fig. 2 is wrapped in a tube or torus, then the energy
  per node can be set up to be lower than that shown in the plot even by a factor of 2 if the circumference of the tube
  is about 8 edges. ... it seems that among the various examples considered, it is a locally hexagonal tube that
  corresponds to the lowest energy state of the system" (Sec. III.A).
- Single exchange-move defects on the honeycomb (Figs. 4, 5): with r = −7.1 both defect types raise the energy, so
  "the reference lattice is stable under deformations when the parameter r is negative" (Sec. III.B).
- Free energy (Sec. III.C): δF ∼ constant − T ln n for a single defect (Eq. 34), so "small defects are likely to be
  present in the system at nonzero temperatures"; δF ∼ Ω(m) − T ln n for m-point perturbations (Eqs. 35, 39), so "the
  reference lattice describes a stable thermodynamic phase".
- Sec. V compares the dynamics with random-graph processes (Erdős-Rényi, d-processes, scale-free) and concludes that
  "a mathematical description of a graph process mimicking our dynamics is elusive".

### 2.4 What it says it cannot do

- "A general proof of the statement that a locally hexagonal lattice is the true ground state of the model is at this
  moment beyond reach and so we can only phrase it as a conjecture" (Sec. III.A).
- "Besides the definition of the Hamiltonian term HB that depends on quantum mechanical features, our study of the
  model is limited to stationary states and is thus mostly classical" (Sec. VI).
- On temperature: "This could be a problem if the graph is to be interpreted as the entire Universe" (Sec. VI).
- Three dimensions "left for future work" (Sec. I), perhaps with v0 = 4 (Sec. VI).
- Einstein's equations: "It has been conjectured elsewhere that such a relation can give rise to the Einstein
  equations [20, 33]. It will be interesting to investigate this possibility in the context of our model" (Sec. VI).
- **Signs and Monte Carlo**: not mentioned.

## 3. Hamma, Markopoulou, Prémont-Schwarz and Severini, Lieb-Robinson bounds [HMPS09], read in full

Four pages; every paragraph and equation read. The model is **not** a dynamical graph: it is Wen's rotor model on a
fixed square lattice. H_rotor = U Σ_i (Σ_α S^z_{i,α})² + J Σ (S^z)² + Σ (t e^{i(θ − θ)} + h.c.) (unnumbered, Sec.
"Topological Order and Artificial Light"); for t, J ≪ U the low-energy theory is H_eff = J Σ (S^z_ij)² − g Σ_p (W_p +
h.c.)/2 (Eq. 1), with W_p the plaquette string operator and continuum speed of light "c = √(2gJ)". The bound: summing
over paths alternating link and plaquette operators gives a_n ≤ N′_PQ(n, d)(gJ)^(n/2) (Eq. 4) and, optimizing,
v_LR = √2 e √(2gJ) ≡ √2 e × c (text after Eq. 4; checked numerically with an exact, unnumbered formula for N'(n, d); Eq. 5 is the resulting bound on the commutator). In D
dimensions "the Lieb-Robinson speed is conjectured to increase linearly with the dimension itself" (abstract; Ref. 15:
"Evaluating N_D(n, d) exactly is a non-trivial combinatorial problem"). Cosmology: a hypercubic lattice whose dimension
falls in time, D(t) = D_in(1 − αt), gives light cones "with parabolic sides".

What bears on the brief:
- The bound needs a local Hamiltonian on a fixed graph, "a sum of local observables". And on fermions: "Fermionic
  models are not really local because fermionic operators do not generally commute even at distance" (Sec.
  "Topological Order and Artificial Light"). *Ours:* that sentence applies to [KMSev08]'s fermionic edges.
- Stated limits: "it is easy to construct a different model where there is emerging light and other faster
  particles"; tightening the bound for a frustrated model is left open (Conclusions).
- *Ours, unverified:* in the S^z basis the plaquette term −g(W_p + h.c.)/2 has non-positive off-diagonal elements, so
  H_eff is stoquastic in that basis; the paper does not say so.

## 4. Later quantum-graphity work

### 4.1 The search (rule 15)

arXiv API, 2026-11-02: title search "quantum graphity" (8 results, 2006 to 2018); abstract search "quantum graphity"
(18 results, to 2019); abstract search graphity AND quantum, newest first (18 results; the newest is 2019, so
**nothing with "graphity" in a title or abstract after 2019 was returned**); "combinatorial quantum gravity" in
abstracts (7); Ollivier AND "quantum gravity" (10); "dynamical graph" AND "quantum Monte Carlo" (0); stoquastic AND
graph AND gravity (0); "edge switch" AND quantum AND hamiltonian (0); "superposition of graphs" AND hamiltonian (2,
loop quantum gravity, unrelated); "quantum graph dynamics" AND geometry (0). Query strings as sent (arXiv API, max_results = 50): ti:"quantum graphity"; abs:"quantum graphity"; abs:graphity AND
abs:quantum (sortBy = submittedDate); abs:"combinatorial quantum gravity"; abs:Ollivier AND abs:"quantum gravity";
abs:"dynamical graph" AND abs:"quantum Monte Carlo"; abs:stoquastic AND abs:graph AND abs:gravity; and the remaining three
in the same form. Not searched: INSPIRE, Google Scholar,
journals without arXiv copies. The papers below came from these searches and from the reference lists of [CM11] and
[HMLCSM10].

### 4.2 Read in part or by abstract

- **Caravelli and Markopoulou, 1008.1340 [CM11]. Read in full.** Edge qubits only (Eq. 1); H = H_V + H_L +
  "interaction terms", the last "will not be used in the following, but in a generic model these terms produce
  Alexander moves on the graph" (Eq. 3 and after). Expanding H_V to first order in p maps the model onto an Ising model
  on the line graph of K_N (Eq. 30, with A = p g_V, B = 2 g_V p v0, C = g_L r³/6, Eq. 31). Method: mean field only. The
  order parameter is the mean valence d(T) (Eq. 38), which at T = 0 is v0 corrected by the triangle term (Eqs. 42,
  43); its slope in T diverges as N → ∞ (Eq. 41), read as a transition at zero temperature. Stated limit: "Since v0 is
  assumed to be never zero, the model has no phase transition and at T = 0 the system goes to the ground state as
  expected" (Sec. VI). Uses H_L with "r ≤ 1, so that higher length loops contribute less" (after Eq. 5), unlike the
  r ≈ ±7 of [KMSev08].
- **Hamma, Markopoulou, Lloyd, Caravelli, Severini and Markström, 0911.5075 [HMLCSM10]. Read in part: Secs. I, II
  (II.A to II.C), III.A, the opening and end of IV with Fig. 5, V.** The only paper found in which the graph is a quantum variable that is
  actually evolved. Hilbert space: bosons on the N points tensored with a spin one half on every edge of K_N (Eqs. 1,
  5, 6). Hamiltonian H = H_link + H_v + H_ex + H_hop (Eq. 19): H_link = −U Σ σ^z (Eq. 15); H_v = −Σ μ_i b†_i b_i (Eq.
  2); **matter hopping H_hop = −t Σ P_ij ⊗ (b†_i b_j + b_i b†_j)** with P_ij the projector on edge (i, j) being on
  (Eqs. 11, 12); **edge-matter conversion H_ex = k Σ [S⁻_ij P^L_ij ⊗ (b†_i b†_j)^R + h.c.]** (Eq. 18), allowed only when
  i and j are already joined by another path of length L (L = 2 used). So "an edge is the bound state of 2R quanta",
  and the total of edges and particles is conserved (Sec. IV). Computation: exact diagonalization, "the system with 4
  vertices and hard core bosons" (Sec. II.B; Sec. III.A), which is six edge qubits (the edges of K4) and four sites, ten qubits in all (Fig. 2's initial state); and a classical
  Markov-chain version run from K_36 to K_400 (Fig. 5), which ends in random graphs with Poisson degree distributions.
  What it says of itself: "The Hamiltonian of [16] is not unitary: the universe starts at a high energy configuration
  (non-local) and evolves to a low energy one (local)" (Sec. V, of [KMS06]); and "there is nothing in the Hamiltonian
  to encourage the system to settle in metastable states that are regular graphs" (Sec. V). Claims: entanglement between
  matter and graph; a highly connected region as a toy trapped surface, argued with Lieb-Robinson speeds and Snell's
  law (Sec. II.C), with an evaporation and information picture. *Ours, unverified:* with t ≥ 0 the hopping elements are
  non-positive; H_ex changes the number of edges by one, so the diagonal sign (−1)^(number of edges) flips the sign of
  k while leaving H_hop alone, which makes the model stoquastic in the occupation basis whatever the sign of k. The
  paper does not discuss this and does not use Monte Carlo on the quantum model.
- **Caravelli, Hamma, Markopoulou and Riera, 1108.2013 [CHMR12]. Read in part: Sec. II, Sec. VI, Sec. VII.** The model
  of [HMLCSM10] with "U = k = 0" (Eq. 15), that is, a Bose-Hubbard model on a fixed but unusual graph, "the equivalent
  of ignoring the backreaction of the matter on the geometry". For foliated, rotationally invariant graphs it reduces
  to a one-dimensional Bose-Hubbard chain; the one-particle density obeys a wave equation in which the vertex degree
  sets the local speed (abstract; Sec. VII), and a completely connected region traps a particle behind a gap growing
  linearly with its size (Figs. 10, 12; sizes N up to about 100 in the one-particle sector). Stated limits: the Gordon
  connection to general relativity "cannot be made in 1+1-dimensions, the case we considered", and "How do our results
  change if we include the backreaction of the matter on the graph?" is left open (Sec. VII).
- **Quach, Su, Martin and Greentree, 1203.5367 [QSMG12]. Read in part: Secs. II and III.A.** Adds an **edge-hopping
  term H_X = g_X Σ m_rs b†_rq b_qs** (Eq. 5, Fig. 3): edge (r, q) is replaced by (q, s) when r and s are joined, which
  does not preserve valence. Sign of g_X not fixed. Treated "semi-classical[ly]": zero-temperature Metropolis quenches
  on a torus of 100 by 9 points, 300 samples, at v0 = 3, r = 7.2, p = 1, g_V/g_P = 10⁵ (Sec. III.A), finding domain
  walls frozen into local minima; then single-boson tight-binding propagation across them (scattering, double imaging).
- **Wilkinson and Greentree, 1506.07588 [WG15]. Read in part: Secs. I, II, the opening of III, IV, V.** Same energy
  with shortest-path loops only, r = 6.5, cut at L_max. Hhop is "a kinetic term that allows edges to propagate", whose
  form is not given; "Since we neglect matter in this work, the evolution of the graph is a non-unitary process" (Sec.
  II). Method: the "epitaxial approximation" (one edge at a time, greedy), N = 24 and 36. **Result: the original
  energy favors small disjoint pieces.** "While isolated cubes were found to have lower energy than a connected
  honeycomb lattice in the original model, the honeycomb lattice does become a lower energy state and a potential
  ground state when the hypervalence term is considered" (Sec. V); the hypervalence term penalizes deviations in the
  numbers of points at distance 1, 2 and 3 (Eq. 7). On the transition: the zero-temperature limits of [CM11] and others
  may mean "that geometrogenesis is a quantum phase transition, rather than a thermal phase transition, and must be
  modelled accordingly" (Sec. I).
- **Spector and Schwartz, 1808.05632 [SS18]. Read in part: abstract, Secs. on the dynamics, connectivity, the
  directional term, and defects.** Classical Metropolis, single edge on or off per step (p. 5), N = 100, valence Z = 4.
  The simple quantum graphity energies are "highly degenerate, having multiple ground states that are not lattices"
  (abstract). Connectivity imposed as a hard rejection of disconnecting moves. New term H_D ∝ Σ_i (Σ_{j≠k} A_ij A_ik
  δ(B_jk, 1) − 2d)² with B = A² (Eq. 17), minimal when each point has exactly 2d pairs of neighbors joined by a single
  path of length 2, as in a d-dimensional hypercubic lattice. Then: "We ran Metropolis simulations with the above
  Hamiltonian for d=2, and failed to reach a ground state". Defects (a missing edge) have additive energy when far
  apart and lower energy when close: "the defects from the perfect lattice seem to behave like particles of quantized
  mass that attract one another" (abstract; Sec. "Attraction of defects", Fig. 9).
- **Abstract only:** Wilkinson and Greentree 1409.2557 [WG14] (energetics from the complete or the empty graph; exact
  energy curve for small N; epitaxial approximation); Caravelli and Markopoulou 1201.3206 (quantum foam with non-local
  links, corrections to Lorentz dispersion); Caravelli 1110.3278 (review of [CHMR12]); Chen and Plotkin 1210.3372 [CP12]
  ("the entropy of the graphs are super-extensive ... which results in a transition temperature of zero in the limit
  of infinite system size", abstract); Mandrysz and Mielczarek 1804.10793 (complete graph as the ultralocal limit;
  Ising matter on the graph); Requardt and Rastgoo 1501.00391 (review and comparison); Markopoulou 1201.3398; Mielczarek
  1404.0228; Crowther 1410.0345 (philosophy).
- **Found by the same searches, abstract only, and bearing directly on the brief** (not quantum graphity):
  Diamantini and Trugenberger 1710.00221 [DT17]: "in discrete models of quantum gravity, emergent geometric space can be
  viewed as the entanglement pattern in a mixed quantum state of the 'universe'", worked out for the CQG model ("the
  condensation of 4-cycles in random regular bipartite graphs"); "the emergence of geometric order decreases the
  entanglement entropy of random configurations". Trugenberger 1610.05934 [T17]: "geometric space emerges from random
  bits in a quantum phase transition driven by the combinatorial Ollivier-Ricci curvature". Neither was read beyond the
  abstract; whether either defines a Hamiltonian with hopping between graphs is not known to us.

## 5. Extraction table

| Paper | Hilbert space | Graph-changing term | Stoquastic? | Sizes and method | Geometry, light cones, matter, gravity claimed |
|---|---|---|---|---|---|
| [KMS06] | ⊗ over K_N edges of a 4-state |j, m⟩ | HLQG, Fig. 1 only, unspecified | not stated; loop term non-positive off-diagonal (ours) | none; analytic | low-T lattice conjectured; U(1) photons; no gravity |
| [KMSev08] | ⊗ over K_N edges of a fermionic mode; Sec. IV adds m | H(exch) Eq. 27, H(add) Eq. 28; sign unfixed; ignored | not stated; fermionic signs (ours) | cycle counts to L = 20 on hand-built graphs | honeycomb, or a tube, conjectured; string-net matter; Einstein left open |
| [HMPS09] | rotors on a fixed square lattice | none | effective H is, in S^z basis (ours) | analytic bound, numerical path sums | v_LR ≈ √2 e c; grows with D (conjectured) |
| [CM11] | edge qubits | not used | not addressed | mean field | average valence as order parameter; transition only at T = 0 |
| [HMLCSM10] | bosons ⊗ edge qubits on K_N | edge-matter conversion H_ex Eq. 18 | yes up to a sign gauge (ours) | exact diagonalization, N = 4; classical chain K_36 to K_400 | matter-graph entanglement; trapped-surface analogue; random graphs at late times |
| [CHMR12] | as above, graph frozen | none (k = 0) | hopping −t, yes (ours) | 1D reduction, one particle, N to about 100 | wave equation with degree as local speed; trapping |
| [QSMG12] | as above | edge hopping H_X Eq. 5 | sign unfixed | Metropolis, T = 0, 100 × 9 torus | domain walls; lensing-like scattering |
| [WG15] | classical graph | unspecified | n/a | epitaxial, N = 24, 36 | disjoint cubes win; hypervalence restores honeycomb |
| [SS18] | classical graph | single-edge flips | n/a | Metropolis, N = 100, Z = 4 | degenerate non-lattice ground states; attracting defects |

## 6. Against the brief (ours, unverified throughout)

### 6.1 Term by term

| Brief | Quantum graphity counterpart | Comment |
|---|---|---|
| Basis: valid wirings, four or six links, bipartite, hard-core rule | Basis: all subgraphs of K_N ([KMSev08] Eq. 6) | The brief's space is a constrained subspace of the same edge-qubit product. Regularity is a hard constraint in the brief and a soft term (H_V, g_V → ∞) in quantum graphity. |
| H0 = 16(N − S) + 4λX | H_V + H_B (valence plus closed paths of every length, weights r^L/L!) | Different energies. The brief counts squares with Trugenberger's saturation and the curling cost; quantum graphity rewards all cycles with factorial weights. Both are diagonal in the graph basis. |
| H1 = −Γ Σ over valid switches | H(exch) = g(exch) Σ' N_ab a†a†aa ([KMSev08] Eq. 27); HLQG ([KMS06]); H_X ([QSMG12]) | Same role. Three differences below. |
| Sign: −Γ, Γ ≥ 0, stoquastic | sign never fixed; fermionic edges | With qubit (hard-core) edges and g(exch) ≤ 0 the exchange term is stoquastic; with fermionic edges as written, the Jordan-Wigner string can attach state-dependent signs (not checked). |
| Switch between any two edges | exchange only when a and b are joined (local) | See 6.3. Also: as written, Eq. 27 removes ac, bd and adds ad, bc with a joined to b; in a bipartite graph a and d then sit on the same side, so that local exchange does not preserve bipartiteness. A local bipartite switch needs a different condition (for example, the two edges' endpoints on one side sharing a neighbor); a design choice under S1. |
| no matter | m labels and string nets ([KMS06], [KMSev08] Sec. IV); bosons hopping on on-edges and converting to edges ([HMLCSM10]) | The brief lacks a matter sector. The classical toy's sealed bath is the classical shadow of [HMLCSM10]'s edge-matter conversion, which is the published way to make the graph's energy go somewhere unitarily. |
| no vertex valence term, no edge addition | H_V; type III add/subtract move | The brief's fixed degree is the g_V → ∞ limit with no type III move. |
| no connectivity term | [WG15] hypervalence; [SS18] hard connectivity | The brief's hard-core rule and square energy already shatter into 4-cubes at λ = 0 (Gate A), which is [WG15]'s "isolated cubes" result in another energy. |

**What the brief has that quantum graphity lacks:** an energy tied to a curvature with a convergence result behind it
(Trugenberger's, via Ollivier); the hard-core rule; bipartiteness; the curling cost λ and the exact ladder; a fixed sign
for the hopping term; an exact Γ = 0 limit that is a validated classical model with exact enumeration at N ≤ 18; and a
dimension census read from the wiring, whose nearest published relative found here is [SS18]'s H_D (pairs of neighbors
joined by a single path of length 2, Eq. 17).

**What quantum graphity has that the brief lacks:** a matter sector (U(1) string nets; hopping bosons); a unitary
energy-conserving graph-matter exchange ([HMLCSM10] Eq. 18); variable valence; a Lieb-Robinson treatment of signal
speed ([HMPS09], fixed lattice only); and one quantum computation with the graph in superposition (N = 4).

### 6.2 Is the brief's construction already published?

Not in what was found. The search is stated in 4.1. The closest pieces are [KMSev08]'s exchange term (written, sign
unfixed, fermionic, never studied as a quantum term), [QSMG12]'s edge hopping (simulated semi-classically) and
[HMLCSM10] (a graph in superposition, at N = 4, with edge-matter conversion and no switch). We have not found a
stoquastic switch Hamiltonian on regular graphs with a curvature energy, or quantum Monte Carlo of any
graph-in-superposition model. Two things could still contain it and were read only by abstract: [T17] ("a quantum phase
transition driven by the combinatorial Ollivier-Ricci curvature") and [DT17]. Both must be read in full before the
brief or any write-up says the construction is new; a rule 15 note on the template is owed if it is ever said.

*General knowledge, not read, to verify:* the brief's structure, a classical energy on a constrained configuration space
plus a kinetic term −Γ over local moves, is the structure of quantum dimer and quantum loop models in condensed matter
(Rokhsar and Kivelson, 1988), and there is a known family of such Hamiltonians, the "stochastic matrix form" or
Rokhsar-Kivelson construction (Castelnovo, Chamon, Mudry and Pujol, 2005), whose ground state has amplitudes equal to
the square roots of the classical Boltzmann weights. Such a variant of the brief (diagonal term built from
exp(−ΔH0/2g) for each move) would have the classical toy's ensemble at coupling g as its exact ground state, which would
make step 1's comparison exact by construction. Proposed for her choice, not adopted; the papers must be read first.

### 6.3 What quantum graphity's results predict for the brief's model

**Small Γ.** Quantum graphity assumed this regime throughout ("do not significantly alter the equilibrium and ground
states", [KMS06]). Expect the classical ground state dressed by virtual switches, energy shifts of order −Γ²/(cost of a
switch), and the classical phases intact. Two cautions specific to the toy. (a) The tube's wall of 12 is a single
switch, so H1 couples the tube to the first opened state directly, at first order in Γ; there is no barrier to tunnel
through at the single-move level, and any exponentially slow quantum process is the collective one (a whole tube
converting, many switches). (b) With named points the classical ground state is degenerate over relabelings, and H1
connects those copies only at high order through excited states, so finite-size splittings will be tiny; the exact
ground state is their symmetric superposition (see 6.4).

**Large Γ.** H1 dominates; the ground state approaches the Perron vector of the "graph of graphs" (valid wirings joined
by switches, which T4 showed connected at N = 16, 18), weighted toward wirings with more valid switches. We expect that
to be spread over the random (melted) wirings that dominate by number: the quantum analogue of quantum graphity's hot,
permutation-symmetric phase. So a quantum transition in Γ between a geometric and a random phase is the expected shape,
which is [WG15]'s and [T17]'s "quantum phase transition" reading of geometrogenesis.

**Where the transition sits, and why the move set matters.** With switches between any two of the 2N edges (four
links), each wiring has of order N² valid switches, so the kinetic scale at large Γ is of order ΓN² while H0
differences are of order N: the transition would sit near Γ_c ∼ 1/N and vanish as N grows. That is the quantum form of
the result that [CM11] (mean field, Eq. 41) and [CP12] (abstract: super-extensive entropy) report, and [WG15]
summarizes, for the thermal transition (it is driven to zero temperature as N → ∞). With local switches (of order N per wiring) the scales match and Γ_c can stay finite.
In the classical chain the move set only sets the dynamics; in H1 it sets the physics, so it is a decision under S1,
to be made before step 1. Step 1 can compute both at N = 16 and 18.

**Light cones.** [HMPS09]'s bound needs H to be a sum of terms local on a fixed graph. With global switches there is no
Lieb-Robinson cone at all; with local switches a cone relative to the current wiring is plausible but unproven for a
graph in superposition. The toy's measured front speeds (T47) are classical and say nothing about this.

**Disjoint pieces.** [WG15] found the original quantum graphity energy prefers isolated cubes, as CQG does at λ = 0
([GV21]; Gate A). At λ > 1 the toy's ground state is connected (the flat sheet), so this failure need not carry over;
the quantum model should still be checked for it at small λ.

### 6.4 Does anything here change the brief's order of work?

Yes, in four places (ours, for her decision):

1. **Step 0 grows.** Add [HMLCSM10] (in part already), [T17] and [DT17] in full. [DT17] computes entanglement in this
   very model and must be read before Carroll's reader is designed (step 2), since it may already be that reader or a
   competitor to it.
2. **Before step 1: fix the move set of H1** (global switches as the chain uses, or a local bipartite switch), for the
   reason in 6.3, and fix whether edges are qubits (stoquastic, as the brief says) and never fermions (as [KMSev08]
   wrote them).
3. **Steps 1 and 4 do not connect as written.** The class space of step 1 (interchangeable points) has no tensor
   factors at all, so no reader can be applied to its ground state. With named points, H0 and H1 are both invariant
   under renaming the points within a side, the exact ground state is too (it is unique by Perron-Frobenius when the
   graph of graphs is connected), and so the reduced state of every pair of points, and their mutual information, is
   the same for every pair of the same kind (same side, or opposite sides). Carroll's reader on the exact ground state
   would then read a complete (bipartite) pattern, not a lattice,
   at every Γ. This is [KMSev08]'s symmetry breaking ("Permutation invariance of the state breaks to translation
   invariance", Sec. VI), which in a finite system happens only with a pinning term, by conditioning on a classical
   wiring, or in the limit N → ∞. Step 4 has to name which of these it uses, and also what the factors are: the brief
   says "each point as a factor", but the Hilbert space is a constrained subspace of a product over **edges** (as in
   [KMS06] Eq. 10), not over points.
4. **Step 3's question changes form.** Stoquastic path-integral quantum Monte Carlo samples the equilibrium state in
   imaginary time; it does not give a real-time decay rate. "Does a curled tube decay faster with Γ" can be asked as an
   equilibrium question (does the curled-to-flat crossover move with Γ; the gap to the first excited state from
   imaginary-time correlations) or as a real-time question at tiny sizes by exact diagonalization, as [HMLCSM10] did at
   N = 4. It should be restated before it is pre-registered.

Nothing here argues against the brief's core choice: H0 unchanged as the diagonal and Γ = 0 exactly the classical toy.
That bridge is the one thing quantum graphity never had, and it is what makes the quantum model checkable.

## 7. Read status

| Key | arXiv | Status, 2026-11-02 |
|---|---|---|
| [KMS06] | hep-th/0611197 | Read in full (all sections, Eqs. 1 to 34) |
| [KMSev08] | 0801.0861 | Read in full (all sections, Eqs. 1 to 58, Table I) |
| [HMPS09] | 0808.2495 | Read in full (four pages, Eqs. 1 to 5) |
| [CM11] | 1008.1340 | Read in full (Secs. I to VI, Eqs. 1 to 49) |
| [HMLCSM10] (proposed) | 0911.5075 | Read in part: Secs. I, II.A to II.C, III.A, opening and end of IV with Fig. 5, V |
| [CHMR12] (proposed) | 1108.2013 | Read in part: Secs. II, VI, VII |
| [QSMG12] | 1203.5367 | Read in part: Secs. II, III.A |
| [WG15] | 1506.07588 | Read in part: Secs. I, II, opening of III, IV, V |
| [SS18] (proposed) | 1808.05632 | Read in part: abstract, dynamics, connectivity, H_D (Eqs. 11, 17, 18), defects (Eq. 19, Fig. 9) |
| [WG14] (proposed) | 1409.2557 | Abstract only |
| [CP12] | 1210.3372 | Abstract only (this session) |
| [T17] | 1610.05934 | Abstract only (this session) |
| [DT17] (proposed) | 1710.00221 | Abstract only |
| others in 4.2 | | Abstract only; no keys proposed |

## 8. REFERENCES.bib entries owed

Read-status lines to append to the existing notes (proposed text):

- **KMS06**: "Read in full by an assistant agent, 2026-11-02 (all sections, Eqs. 1 to 34): docs/reading/notes/2026-11-02_quantum_graphity_reading.md. Hhop and HLQG are not specified; the graph-changing couplings are assumed small enough not to alter the ground state; no simulation."
- **KMSev08** (replace "unread"): "Read in full by an assistant agent, 2026-11-02 (all sections, Eqs. 1 to 58): docs/reading/notes/2026-11-02_quantum_graphity_reading.md. Fermionic edge modes; exchange and add/subtract moves written (Eqs. 27, 28) with unfixed signs and then ignored; no simulation; the study is 'mostly classical' by its own account. Settles the Hamiltonian part of assumptions A3 and A5 (to be checked against ASSUMPTIONS)."
- **HMPS09**: "Read in full by an assistant agent, 2026-11-02: docs/reading/notes/2026-11-02_quantum_graphity_reading.md. The model is Wen's rotor model on a fixed square lattice, not a dynamical graph; v_LR = sqrt(2) e c, c = sqrt(2gJ)."
- **CM11** (replace "abstract-only"): "Read in full by an assistant agent, 2026-11-02: docs/reading/notes/2026-11-02_quantum_graphity_reading.md. Mean field only; journal reference not rechecked."
- **QSMG12**: append "Secs. II and III.A read again by an assistant agent, 2026-11-02 for the edge-hopping term H_X (Eq. 5): docs/reading/notes/2026-11-02_quantum_graphity_reading.md."
- **WG15** (replace the note): authors confirmed against the arXiv record on 2026-11-02 (Samuel A. Wilkinson, Andrew D. Greentree); journal Phys. Rev. D 92, 084007 (2015), doi 10.1103/PhysRevD.92.084007 (from the arXiv listing). "Read in part by an assistant agent, 2026-11-02 (Secs. I, II, III opening, IV, V): docs/reading/notes/2026-11-02_quantum_graphity_reading.md."

New entries (fields from the arXiv API records of 2026-11-02; to check at Crossref):

- **HMLCSM10**: Hamma, Alioscia and Markopoulou, Fotini and Lloyd, Seth and Caravelli, Francesco and Severini, Simone
  and Markström, Klas; "A quantum Bose-Hubbard model with evolving graph as toy model for emergent spacetime"; Phys.
  Rev. D 81, 104032 (2010); doi 10.1103/PhysRevD.81.104032; eprint 0911.5075. Status: read in part (as in Sec. 7).
- **CHMR12**: Caravelli, Francesco and Hamma, Alioscia and Markopoulou, Fotini and Riera, Arnau; "Trapped surfaces and
  emergent curved space in the Bose-Hubbard model"; Phys. Rev. D 85, 044046 (2012); doi 10.1103/PhysRevD.85.044046;
  eprint 1108.2013. Status: read in part.
- **SS18**: Spector, Yoav and Schwartz, Moshe; "Study of potential Hamiltonians for quantum graphity"; arXiv preprint
  (no journal reference on the arXiv record); eprint 1808.05632. Status: read in part.
- **WG14**: Wilkinson, Samuel A. and Greentree, Andrew D.; "Energetics of the Quantum Graphity Universe"; Phys. Rev. D
  90, 124003 (2014); doi 10.1103/PhysRevD.90.124003; eprint 1409.2557. Status: abstract only.
- **DT17**: Diamantini, M. C. and Trugenberger, C. A.; "Topological Network Entanglement as Order Parameter for the
  Emergence of Geometry"; New J. Phys. (2017), doi 10.1088/1367-2630/aa8f08 (volume and page not on the arXiv record);
  eprint 1710.00221. Status: abstract only; to read in full before step 2 of the quantum toy brief.

Existing keys used here and not changed: [LW06], [GV21], [CP12], [T17], [QSMG12].

Verified against the sources by a second agent on 2026-11-02 (six PDFs; every checked quotation found; six of the ten searches rerun with the stated counts); its corrections applied the same day, including one of our own: the renaming-invariant ground state gives two values of mutual information (same side, opposite sides), not one.

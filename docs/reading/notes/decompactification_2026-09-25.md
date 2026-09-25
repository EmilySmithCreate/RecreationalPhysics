# Reading notes: how curled directions open (2026-09-25)

> **Status of these notes:** written by an assistant agent on 2026-09-25 from fetched copies of the papers. Some passages
> were read through a tool that summarizes a page, so every quotation must be checked against the paper itself before it is
> used in a paper or a letter. Inferences marked *ours* are unreviewed.


Literature review for the six- and eight-link work (VISION Updates 22 to 27; ASSUMPTIONS O41, O49, O50, O54, O55).
Four questions: (1) dynamical decompactification and why some directions grow while others stay small (string gas
cosmology and its critics); (2) the bubble of nothing and transitions between different numbers of large dimensions;
(3) dimensional phases and the order of transitions in causal and Euclidean dynamical triangulations; (4) whether
several compact directions are expected to open together or one after another.

**How this was read.** Each entry marked "read" was fetched as full text (arXiv HTML or ar5iv) and searched with
targeted questions. Passages in quotation marks were returned verbatim by that search. They should be checked against
the PDF before they go into a paper, because the search tool can garble mathematics. The Tables quoted from [GKM13] were
reproduced twice, and the second reproduction is used. "Abstract only" means exactly that. Nothing here comes from
memory. Where a paper is described but was not fetched, this is said. Inferences about this project are marked
*ours, unverified*.

---

## (a) The short answer

**Nothing we read predicts that several curled directions must open at the same moment unless something ties them
together, and the published mechanisms that tie them are specific ingredients that the graph model does not have.**

In string gas cosmology the dimension-counting argument of [BV89] sets a ceiling: winding strings can find each other
and annihilate in at most three large space directions. It does not say that the three open together. The models that
compute anything almost all assume it, by giving the growing directions one shared scale factor ([GKM10], [DFM04],
[GM04]). Where the directions are allowed to differ, three patterns appear:

- **All or nothing.** The anisotropic 9-torus simulation of [EGJK05] finds that either every direction stays small or
  every direction opens. Three large directions need fine-tuned starting conditions.
- **One push at a time.** [GKM13] reaches three large directions only through *successive* fluctuations: first one or
  two directions grow, then later pushes open the rest. Success falls steeply as the delay between pushes grows.
- **Stages set by what blocks each group.** In [ABE00], membranes open five directions first, and strings then open
  three of those five.

[WB03] shows that directions which start at different sizes can still even out in expansion rate. In the Lorentzian
matrix model, three of nine directions start to expand at one "critical time" ([KNT12]; [AAHNPT26], N up to 128). There
the three are tied by an SU(2) commutator structure, and [AHINT19] argues that this structure is partly an artifact of
an approximation. In the landscape papers, compact directions that form a sphere change together in one step
([CJR09], [BSV10]). That is by construction, since a sphere has no separate directions. In contrast, [GHR10] and
[BPS10] treat the opening of one direction at a time, from a 2+1 parent to our 3+1, as a live possibility with a
signature that could be observed: the curvature would differ from one direction to another.

Witten's bubble of nothing ([W82], read through [GMSV20]) collapses one circle. The torus bubble of [GMSV20] instead
pinches a two-torus fiber at isolated points. The triangulation literature reads dimension globally, from how volume
and random walks scale, not direction by direction. It has no phase with an intermediate number of large directions
that we found. What it does have is the conjecture of [AGGN22] that transitions which change topology are first order,
together with the observation that one CDT transition is second order with spherical space and seemingly first order
with toroidal space.

**Against the project's results** (*ours, unverified*):

- The six-link result, FIRST ONLY (O54), fits the successive-push picture of [GKM13] and the staged picture of [ABE00]
  better than [EGJK05]'s all or nothing. The one-direction-at-a-time transitions of [GHR10] and [BPS10] are its closest
  landscape counterpart.
- We found no published barrier for opening k of n compact directions as a function of k. The ordered walls of O50,
  lowest for the most curled state, therefore have no published comparison that we have found.
- **A caution on the word "double".** From O50's own formulas, the walls are 160 − 112λ, 160 − 96λ and 160 − 64λ. They
  are exactly 20, 40, 80 only at λ = 1.25. At λ = 1.10 they are 36.8, 54.4, 89.6. The six-link walls, 96 − 64λ and
  96 − 48λ, are 16 and 36 at 1.25 and 25.6 and 43.2 at 1.10. So the *ordering* holds for every λ > 1, but the factor of
  two, and with it O55's "halving", belongs to λ = 1.25. This is arithmetic on O49 and O50, not a new result.
- The owner's "tied together" rule would need an ingredient that plays the part of windings plus the dilaton, or of the
  SU(2) structure. Every mechanism we read that produces simultaneous opening has one, and the graph energy's ladder is
  additive (O41), with nothing coupling the directions.

---

## (b) Paper by paper

### String gas cosmology and its critics

**[BV89]** R. Brandenberger and C. Vafa, "Superstrings in the early universe", Nucl. Phys. B316 (1989) 391. No arXiv
id (earlier than arXiv).
- *Read:* not read. The argument is taken from its restatement in [EGJK05] Sec. 1 and [GKM10] Sec. 2.
- *What it establishes (as restated):* winding strings keep a direction small, and to let it grow they must annihilate.
  Two string worldsheets (2 + 2 dimensions) generically meet only in at most 4 spacetime dimensions, "leading to argue
  that at most three spatial dimensions will shed their windings" ([EGJK05] Sec. 1).
- *Bearing:* this is a ceiling on the number of large directions, not a claim that they open simultaneously.

**[TV92]** A. A. Tseytlin and C. Vafa, "Elements of string cosmology", Nucl. Phys. B372 (1992) 443, hep-th/9109048.
- *Read:* abstract only.
- *What it establishes:* the dilaton has to be included. "Winding modes, even though contribute to energy density,
  oppose expansion and if not annihilated will stop the expansion."
- *Bearing:* the source of the rolling-dilaton dynamics that [EGJK05] later found fatal to the counting argument.

**[Sak96]** M. Sakellariadou, "Numerical experiments in string cosmology", Nucl. Phys. B468 (1996) 319, hep-th/9511075.
- *Read:* full text, searched.
- *Model:* classical Nambu-Goto strings on a lattice in a D-dimensional box with periodic boundaries (a torus),
  D = 3, 4, 5. The box is static, the intercommutation probability is 1, and the shortest loops have two links.
- *What it establishes:*
  - A sharp Hagedorn transition. Below the critical density there are "no long loops". Above it, the density in short
    loops is pinned at ρ_H, all extra energy goes into long winding loops, and "the phase transition is a generic
    property independent of the space dimensionality".
  - "Only if the space dimensionality is equal to three, long winding string modes decay in the low-energy density
    regime, while these modes … persist indefinitely in a higher dimensional space" (conclusions).
- *Bearing:* the closest published method to this project: a lattice Monte Carlo on a torus with a sharp transition,
  with the dimension dependence measured directly. It does not let the torus change shape, so it says nothing about
  the order in which directions open.

**[ABE00]** S. Alexander, R. Brandenberger and D. Easson, "Brane gases in the early universe", Phys. Rev. D62 (2000)
103509, hep-th/0005212.
- *Read:* full text, Sec. III searched.
- *What it establishes:*
  - "The winding modes of p-branes can interact in at most 2p+1 large spatial dimensions."
  - The branes with the largest p carry the most energy at large volume, so "the 2-branes will have an important effect
    first. They will only allow 5 spatial dimensions to become large. Within this distinguished T⁵, the 1-brane winding
    modes will only allow a T³ subspace to become large" (Sec. III, with the energy scaling in its Eq. 13).
  - The abstract adds that this "may lead to a hierarchy in the sizes of the extra dimensions".
- *Bearing:* the clearest published statement of **staged** opening, where groups of directions open in an order set
  by the energy of whatever holds each stage back. *Ours, unverified:* this is the same shape as the graph model's
  ladder, where each rung is held by its own wall. The difference is that in [ABE00] the stages come from different
  kinds of object, while in the graph they come from one energy with ordered walls.

**[WB03]** S. Watson and R. Brandenberger, "Isotropization in brane gas cosmology", Phys. Rev. D67 (2003) 043510,
hep-th/0207168.
- *Read:* full text, searched.
- *Model:* anisotropic metric with one scale factor per direction; the worked case is 2 + 1 split directions with
  strings.
- *What it establishes:*
  - Expansion rates even out because annihilation depends on how many winding modes remain: "as the number of winding
    modes decreases in one direction, the other direction should have a larger rate of annihilation".
  - Conclusion: "for an arbitrary amount of initial anisotropy, the anisotropy will reach a maximum early in the
    evolution and then approach zero at later times."
  - The extracted text also says the *ratios* of the scale factors keep growing while the rates equalize. That should
    be checked against the PDF before it is quoted.
- *Bearing:* directions that start opening at different times can end up equivalent, so a sequential start does not
  imply an anisotropic end. *Ours:* the graph model has no feedback of this kind, since its walls are independent (O41).

**[DFM04]** R. Danos, A. R. Frey and A. Mazumdar, "Interaction rates in string gas cosmology", Phys. Rev. D70 (2004)
106010, hep-th/0409162.
- *Read:* full text, searched.
- *Setup:* "some dimensions grow due to some thermal or quantum fluctuation which acts as an initial expansion
  velocity". The growing d directions share one scale factor and the other 9 − d stay at string size.
- *What it establishes:* "the interaction rates of strings are negligible, so the common assumption of thermal
  equilibrium cannot apply", and the gas falls out of equilibrium "almost immediately". Conclusion: "it seems unlikely
  that string gas cosmology in totally compact spaces provides an explanation for the number of macroscopic
  dimensions." Among the proposed repairs is "a stochastic version of the BV scenario".
- *Bearing:* a central critique. It also shows that the standard setup builds in simultaneous growth by assumption.

**[EGJK05]** R. Easther, B. R. Greene, M. G. Jackson and D. Kabat, "String windings in the early universe", JCAP 0502
(2005) 009, hep-th/0409121.
- *Read:* full text, Secs. 1, 2, 6 and 7 searched.
- *Model:* a homogeneous but anisotropic 9-torus (Eq. 1: nine independent λ_i(t)), dilaton gravity, and Boltzmann
  equations for winding and momentum annihilation (Eqs. 29, 31) with rates proportional to e^φ. The initial λ_i are
  random, with thermal fluctuations of the winding numbers about their means. Fig. 4 uses 10³ runs per histogram.
- *What it establishes:*
  - Sec. 2 (Eqs. 14 and 15): a late-time solution with m growing directions and 9 − m frozen exists for any m.
    "If the string winding dynamics … favors m = 3 … one could naturally explain" three large directions.
  - Sec. 7, the numerical result: "the expansion of the universe has an 'all or nothing' character. If initial
    conditions are such that one begins with many wrapped strings, the strings typically freeze out and keep all
    dimensions small. On the other hand if one begins with few wrapped strings, the strings typically annihilate and
    all dimensions decompactify. Between these extremes there are initial conditions that lead to three large
    dimensions, but such initial conditions are not generic."
  - The cause: "due to the rolling dilaton the string annihilation cross section becomes weaker than previously
    realised."
  - No percentages are given, and nothing is said about the order in time in which directions open.
- *Bearing:* the main numerical critique. The outcome is bimodal (all or none), which is the opposite of FIRST ONLY.
  *Ours:* here the directions are coupled through the shared dilaton and a shared pool of strings. The graph model has
  no such shared pool, which may be why it behaves differently.

**[GKM10]** B. Greene, D. Kabat and S. Marnerides, "Dynamical decompactification and three large dimensions", Phys.
Rev. D82 (2010) 043528, arXiv:0908.0955.
- *Read:* full text, searched.
- *What it establishes:*
  - Winding-string interaction rates are exponentially suppressed for d > 3. The impact-parameter amplitude carries
    exp[−b²/(4Yα′)] (Eq. 5), which suppresses interactions in the transverse directions.
  - The model grows d isotropic directions while "the remaining 9−d dimensions were kept frozen at the self-dual
    radius" (Sec. 3.3).
  - Results (Sec. 4): for many initial conditions the system stays "forever trapped" in the Hagedorn regime. If it
    fluctuates out into the radiation regime, leftover windings freeze out for d > 3, while for d = 3 they "may
    annihilate efficiently".
- *Bearing:* support for three as the maximum, but only if the three are assumed to grow together.

**[GKM13]** B. Greene, D. Kabat and S. Marnerides, "On three dimensions as the preferred dimensionality of space via the
Brandenberger-Vafa mechanism", Phys. Rev. D88 (2013) 043527, arXiv:1212.2115.
- *Read:* full text, searched; tables reproduced.
- *Model:* two scale factors. ν belongs to the d₁ < 3 directions "initially unwound and growing". λ belongs to the
  "d₂ = 3 − d₁ dimensions subsequently expanding after a fluctuation, but wrapped with winding modes" (Sec. 2). The
  first fluctuation is at t = 0 and the second at t_f; the initial size is ν₀ (Sec. 3).
- *What it establishes:* "Suppose an initial fluctuation causes at least one dimension to grow, and suppose successive
  fluctuations occur on timescales of order α′^{1/2}. If the string coupling is sufficiently large … such fluctuations
  are likely to push a three-dimensional subspace to large volume" (abstract and introduction).
- *Table 2, percentage of cases that end with three large directions:*

  | | t_f = 1 | t_f = 10 | t_f = 100 |
  |---|---|---|---|
  | d₁ = 1, ν₀ = 3 | 82 | 53 | 20 |
  | d₁ = 1, ν₀ = 5 | 65 | 47 | 17 |
  | d₁ = 2, ν₀ = 3 | 70 | 26 | 1 |
  | d₁ = 2, ν₀ = 5 | 43 | 13 | 0.1 |

- *Caveat (Sec. 5):* "a more careful study of the dynamics and statistics of fluctuations is needed." The paper relies
  on [WB03] for isotropy and does not prove it.
- *Bearing:* **the closest published analogue of FIRST ONLY.** In this paper, directions open one push at a time, and
  a later push succeeds less often.
  - *Ours, unverified:* the graph model's T30 gives one push, sees one direction open, and never gives a second push.
  - [GKM13] predicts that a second push given soon after the first should open further directions more often than a
    late one. In their model this is because windings dilute and freeze out.
  - The graph model has a candidate mechanism of its own: soon after the first rung opens, its released energy is
    still in the bath.

**[KR05]** A. Karch and L. Randall, "Relaxing to three dimensions", Phys. Rev. Lett. 95 (2005) 161601, hep-th/0506053.
- *Read:* full text, searched.
- *What it establishes:* a "relaxation principle": "the configuration with the biggest filling fraction is the
  likeliest". In a nine-dimensional expanding space with equal numbers of branes and antibranes of every dimension,
  3-branes and 7-branes come to dominate. Branes of dimension 4 or more generically intersect in 9 space dimensions
  and annihilate; 3-branes are the largest that do not, and they dilute least.
- *Bearing:* it assumes that all nine directions are already large, so it explains why three are *singled out* rather
  than how curled directions open. Useful as a second route to "three" that has no windings at all.

### Matrix models (the only numerical results we found where several directions open at once)

**[KNT12]** S.-W. Kim, J. Nishimura and A. Tsuchiya, "Expanding (3+1)-dimensional universe from a Lorentzian matrix
model for superstring theory in (9+1)-dimensions", Phys. Rev. Lett. 108 (2012) 011601, arXiv:1108.1540.
- *Read:* full text, searched. The figure itself was not inspected.
- *What it establishes:*
  - The extent of space is measured by the eigenvalues of T_ij(t) = (1/n) tr(Ā_i Ā_j) (Eq. 8).
  - Abstract: "three out of nine spatial directions start to expand at some 'critical time', after which the space has
    SO(3) symmetry instead of SO(9)".
  - Fig. 2 caption: "After the critical time t_c, three eigenvalues become larger". The simulations use N = 16.
  - The stated reason for three: maximizing tr F² at fixed tr A² is achieved by SU(2), which has d = 3.
- *Bearing:* three directions open at one critical time, a *tied* opening. What ties them is an algebraic structure
  (SU(2)), not an energy barrier.

**[AHINT19]** T. Aoki, M. Hirasawa, Y. Ito, J. Nishimura and A. Tsuchiya, "On the structure of the emergent 3d expanding
space in the Lorentzian type IIB matrix model", PTEP (2019), arXiv:1904.05914.
- *Read:* full text, searched.
- *What it establishes:*
  - Abstract: "the expanding part of the space is described essentially by the Pauli matrices". Only two eigenvalues of
    each spatial matrix grow, satisfying [X_i, X_j] = i c ε_ijk X_k (Sec. 3.4, Eq. 3.9), so the space is singular.
  - The cause is an approximation that "amounts to replacing e^{iS_b} by e^{βS_b}".
  - Complex Langevin results "suggest … clear deviations from the Pauli-matrix structure without losing the (3+1)d
    expanding behavior".
- *Bearing:* the tied opening of [KNT12] is partly an artifact. It is the published example of a result that looked like
  "three together" and needed a second look.

**[BP24]** R. Brandenberger and J. Pasiecznik, "On the origin of the SO(9) → SO(3) × SO(6) symmetry breaking in the IKKT
matrix model", arXiv:2409.00254 (2024).
- *Read:* full text, searched.
- *What it establishes:* "A spatial dimension can only become large if the D1-strings winding that direction can
  annihilate … a process which is highly suppressed if more than three dimensions of space are large" (abstract). It
  does not discuss whether the three directions grow at the same time. It lists open issues: justifying the ansatz and
  showing that the D1 strings are stable (Discussion).
- *Bearing:* [BV89]'s ceiling carried into the matrix model. It leaves the timing question open, which makes it the
  right paper to ask about (section (d)).

**[AAHNPT26]** K. N. Anagnostopoulos, T. Azuma, M. Hirasawa, J. Nishimura, S. Papadoudis and A. Tsuchiya, "The emergence
of (3+1)-dimensional expanding spacetime from complex Langevin simulations of the Lorentzian type IIB matrix model with
deformations", arXiv:2604.19836 (April 2026).
- *Read:* full text, searched.
- *What it establishes:*
  - Complex Langevin simulation with N up to 128. The spatial extent is again read from the eigenvalues of T_ij(t)
    (Eq. 2.21).
  - "Only three out of nine directions start to expand"; "the remaining eigenvalues are found to stay comparatively
    small".
  - The deformed model has "a phase" in which smooth, real 3+1 spacetime emerges. The bosonic model does not break
    SO(9), and instability at m_f = 8 hints at a phase boundary.
  - The order of that boundary is not stated. Whether the three directions start at the same time is not stated
    explicitly.
  - Caveats: the deformation's effects still have to be examined, and the method "is not powerful enough to sample
    all the relevant saddle points".
- *Bearing:* the most recent numerical evidence that three directions open as a block. It is also the natural place
  for the timing question.

### The bubble of nothing and changes in the number of large dimensions

**[W82]** E. Witten, "Instability of the Kaluza-Klein vacuum", Nucl. Phys. B195 (1982) 481. No arXiv id.
- *Read:* not read. The publisher's page refused access, so this is taken from the restatement in [GMSV20] Sec. 2.1.
- *What it establishes (as restated):*
  - The Euclidean bubble is ds² = r² dΩ₃² + dr²/(1 − ℛ²/r²) + R_KK² (1 − ℛ²/r²) dθ², so the compact circle shrinks to
    zero at r = ℛ.
  - "The condition ℛ = R_KK needs to be imposed to avoid … a conical singularity."
  - The rate is Γ ~ e^{−S} with S = π R_KK² / (8 G₄).
  - A zero-energy "hole in space that simply pops up and starts expanding at the speed of light."
- *Bearing:* the decay goes through one curled circle, with a barrier that grows as the square of its radius.
  *Ours:* in the graph model, "curled" has only one size (a side of 4), so there is no radius to vary and this scaling
  has no direct counterpart.

**[GMSV20]** I. García Etxebarria, M. Montero, K. Sousa and I. Valenzuela, "Nothing is certain in string
compactifications", arXiv:2005.06494; JHEP 12 (2020) 032 per the search listing (not checked on the journal page).
- *Read:* full text, Secs. 2.1 and 3 searched.
- *What it establishes:*
  - Whether a bubble of nothing can exist is set by a bordism group. The circle with periodic spin structure is
    protected (Ω₁^spin = ℤ₂), but "Ω₃^spin = 0", so T³ is not protected even with a supersymmetry-compatible spin
    structure.
  - Their explicit T³ bubble (in Einstein-dilaton-Gauss-Bonnet) is an elliptic fibration in which "a T² fiber pinches
    off" at up to 12 isolated points, which are Kaluza-Klein monopoles (Sec. 3.3). So what collapses is not a single
    circle.
  - Asked directly whether a torus bubble shrinks one circle while the others are spectators, the text has no such
    statement.
- *Bearing:* for a torus with several circles, the published decay need not go one circle at a time. *Ours:* this is a
  counterpoint to FIRST ONLY in the *collapse* direction (O55's fold), though it comes from very different physics.

**[GM04]** S. B. Giddings and R. C. Myers, "Spontaneous decompactification", Phys. Rev. D70 (2004) 046005,
hep-th/0404220.
- *Read:* full text, searched.
- *What it establishes:*
  - Positive vacuum energy together with extra dimensions makes our 4D vacuum unstable to decompactification, and
    "either quantum tunneling or thermal fluctuations carry one past a barrier" (abstract).
  - Only the overall volume modulus is dynamical: all other moduli are assumed fixed (Sec. 2.1), so the extra
    dimensions grow together by assumption.
  - The potential has a metastable minimum and then a runaway to large volume (Sec. 2.2).
- *Bearing:* the canonical "decompactification over a barrier" paper, but it is silent on the order of opening because
  it has only one modulus. (The extracted rate formula was garbled and is not recorded here.)

**[CJR09]** S. M. Carroll, M. C. Johnson and L. Randall, "Dynamical compactification from de Sitter space", JHEP 0911
(2009) 094, arXiv:0904.3115.
- *Read:* full text, searched.
- *What it establishes:*
  - "D-dimensional de Sitter space is unstable to the nucleation of non-singular geometries containing spacetime
    regions with different numbers of macroscopic dimensions" (abstract).
  - The q compact dimensions form a q-sphere held by flux, under an assumed "q-dimensional spherical symmetry" (Sec. II).
    There is no treatment of partial or toroidal compactification.
  - The reverse process is noted as "the inverse of the 'spontaneous decompactification'" of [GM04].
  - Abstract: "the dimensionality of the vacuum plays a key role" in the rates.
- *Bearing:* compactification of several directions in one step, where the directions form a sphere by construction.
  *Ours:* a published picture of a region *curling up* (compare O55's fold run backwards, and the black-hole piece of
  VISION Update 27), but with the "all together" built into the ansatz.

**[BSV10]** J. J. Blanco-Pillado, D. Schwartz-Perlov and A. Vilenkin, "Transdimensional tunneling in the multiverse",
JCAP 1005 (2010) 005, arXiv:0912.4082.
- *Read:* full text, searched.
- *What it establishes:*
  - In 6D Einstein-Maxwell theory the vacua are dS₆, dS₄ × S², AdS₄ × S² and AdS₂ × S⁴.
  - dS₆ → dS₄ × S² goes "through nucleation of spherical, magnetically charged black 2-branes" (Sec. IV), so both
    compact directions curl in one step, as a sphere.
  - Decompactification, dS₄ × S² → dS₆, proceeds by bubbles (Sec. V).
  - There is no comparison of rates for transitions that change the number of large directions by different amounts,
    and no sequential cascade.
- *Bearing:* as for [CJR09]: several directions curl in one step, as a sphere.

**[GHR10]** P. W. Graham, R. Harnik and S. Rajendran, "Observing the dimensionality of our parent vacuum", Phys. Rev.
D82 (2010) 063524, arXiv:1003.0236.
- *Read:* full text, searched.
- *What it establishes:*
  - Starting from a 2+1 parent, "one of the previously compactified spatial dimensions becomes decompactified". Our
    universe is then Bianchi III: ds² = dt² − a(t)²(dr²/(1 − kr²) + r²dφ²) − b(t)² dz², with curvature in two
    directions and not the third.
  - The curvature is therefore different in different directions. This "causes different dimensions to expand at
    different rates" and gives a CMB quadrupole.
  - "If isotropic curvature is observed it may be evidence that our parent vacuum was at least 3+1 dimensional"
    (abstract).
  - Likelihoods are set aside: "We will ignore the subtle issues of the likelihood of populating those vacua."
- *Bearing:* opening one direction at a time is treated in print as a live scenario with an observable signature that
  points the opposite way to the owner's "all three together".

**[BPS10]** J. J. Blanco-Pillado and M. P. Salem, "Observable effects of anisotropic bubble nucleation", JCAP 1007
(2010) 007, arXiv:1003.0663.
- *Read:* abstract only.
- *What it establishes:* the parent "may have a compact dimension … which subsequently grows to become one of our three
  large spatial dimensions". This is "equivalent to anisotropic initial conditions", and it gives anomalous multipole
  correlations.
- *Bearing:* the same scenario as [GHR10], from another group.

**[BEHS24]** J. J. Blanco-Pillado, J. R. Espinosa, J. Huertas and K. Sousa, "Bubbles of nothing: the tunneling potential
approach", arXiv:2312.00133; JCAP 03 (2024) 029 per the search listing.
- *Read:* abstract only.
- *What it establishes:* a four-dimensional treatment of bubbles of nothing through a size modulus, which finds "four
  different types of BoN, characterized by different asymptotic behaviours".
- *Bearing:* a single size modulus; no multi-direction result seen.

### Dynamical triangulations: which phases, what order, how dimension is read

**[AJ95]** J. Ambjørn and J. Jurkiewicz, "Scaling in four dimensional quantum gravity", Nucl. Phys. B451 (1995) 643,
hep-th/9503006.
- *Read:* abstract only.
- *What it establishes:* in 4D Euclidean DT, one phase has internal Hausdorff dimension 2 ("elongated", branched
  polymers) and in the other it "seems to be infinite (the crumpled phase)". The measured exponents were read as
  showing "that the transition is continuous".
- *Bearing:* see [dB96].

**[BBKP96]** P. Bialas, Z. Burda, A. Krzywicki and B. Petersson, "Focusing on the fixed point of 4D simplicial gravity",
Nucl. Phys. B472 (1996) 293, hep-lat/9601024.
- *Read:* full text, searched.
- *What it establishes:*
  - At N₄ = 32000 the vertex-count histogram has "two clearly separated peaks", and "the change occuring as one moves
    from N₄ = 16000 to N₄ = 32000 is striking".
  - The authors "started this study persuaded, as everybody, that in 4d the transition is continuous".
  - "If the discontinuity … is an intrinsic feature of the model then the latter is not an acceptable model of quantum
    gravity."

**[dB96]** B. V. de Bakker, "Further evidence that the transition of 4D dynamical triangulation is 1st order", Phys.
Lett. B389 (1996) 238, hep-lat/9603024.
- *Read:* full text, searched.
- *What it establishes:*
  - A double peak in N₀ at N₄ = 64000. The peak separation is 160 at 32000 and 301 to 366 at 64000, and it is constant
    per simplex.
  - The system "stays in one of these states for a long time and occasionally … flips".
  - The earlier volumes of 8000 or less were "apparently too small".
- *Bearing:* the same story as this project's T6 caution and [RdF15] (already in `REFERENCES.bib`). A transition that
  was read as continuous at small size turned out first order at larger size.

**[AJL05]** J. Ambjørn, J. Jurkiewicz and R. Loll, "Spectral dimension of the universe", Phys. Rev. Lett. 95 (2005) 171301, hep-th/0505113.
- *Read:* full text, searched.
- *What it establishes:*
  - D_S(σ) = −2 d log P(σ)/d log σ, from the return probability of a random walk.
  - D_S(∞) = 4.02 ± 0.1 and D_S(0) = 1.80 ± 0.25, from the fit D_S = 4.02 − 119/(54 + σ).
  - Up to about 181,000 simplices, time extent 80, walks of up to 400 steps. Odd and even step counts differ at short
    walks.
- *Bearing:* the standard way to read a dimension in a lattice ensemble. It is global and does not count directions.
  This corrects the `REFERENCES.bib` note on AJL05 (currently "unread") and gives it an arXiv id.

**[AJJL12]** J. Ambjørn, S. Jordan, J. Jurkiewicz and R. Loll, "Second- and first-order phase transitions in CDT",
Phys. Rev. D85 (2012) 124044, arXiv:1205.1229.
- *Read:* full text, searched.
- *The phases (Sec. 3):*
  - A: "essentially uncorrelated sequence of spatial slices".
  - B: "almost the entire volume … concentrated around a single spatial slice".
  - C: "a genuinely four-dimensional universe", de Sitter-like.
- *The criteria (Sec. 4):* double peaks, flipping between two states, a Binder cumulant, and the shift exponent ν̃.
- *The results:*
  - A–C (Sec. 4.1): ν̃ = 1.11(2). The double peak emerges at N₄ = 100k and grows, and "the vertical gap … clearly
    increases, while the mutual distance of the peaks stays approximately the same". **First order.**
  - B–C (Sec. 4.2): ν̃ = 2.39(3), or 2.51(3) with one point dropped. The peaks are "merging when the volume is
    increased … roughly like 1/N₄". **Second order.**
- *Bearing:* a worked model of telling first from second order at a few sizes. It uses the same criteria this project
  pre-registered (gap, valley, Binder, shift), and a double peak that closes with size is what they call second order.

**[Loll19]** R. Loll, "Quantum gravity from causal dynamical triangulations: a review", Class. Quantum Grav. (DOI
10.1088/1361-6382/ab57c7), arXiv:1905.08669.
- *Read:* full text, searched for phases, dimension and topology.
- *What it establishes:*
  - There are four phases: C_dS, C_b (bifurcation), and the unphysical A and B.
  - In C_dS the time extent scales as N₄^{1/4} and the spatial volume as N₄^{3/4} (this is how the Hausdorff dimension
    is read), and the spectral dimension falls from 4 to about 2 at short distances.
  - A–C is first order, B–C_b second order, and C_b–C_dS "second or higher order".
  - Euclidean DT shows "still no evidence of higher-order phase transitions". Baby universes "are by definition
    disallowed in CDT, but they are generically present in DT".
  - With toroidal slices, "the number, location and broad characteristics of the phases are not" sensitive to topology,
    while the volume profile is constant in time.
- *Bearing:* "baby universes" are the same name [KTB19] uses for the λ = 0 pieces. *Ours:* the causal restriction that
  removes them in CDT is a published example of a constraint that changes which phases exist.

**[ADGGJN21]** J. Ambjørn, Z. Drogosz, J. Gizbert-Studnicki, A. Görlich, J. Jurkiewicz and D. Németh, "CDT quantum
toroidal spacetimes: an overview", arXiv:2103.15610.
- *Read:* full text, searched.
- *What it establishes:*
  - Massless scalar fields with a jump around each cycle serve as coordinates on the torus.
  - Made dynamical, "when δ > δ_c, a transition occurs: the scalar field pinches the geometry to a spatial volume which
    is small". The order of that transition is not characterized ("currently being explored").
- *Bearing:* the closest published lattice-gravity result in which **one cycle of a spatial torus is singled out and
  pinched**. It is driven by a field added along that cycle, not by the geometry alone.

**[AGGN22]** J. Ambjørn, J. Gizbert-Studnicki, A. Görlich and D. Németh, "Topology induced first-order phase transitions
in lattice quantum gravity", JHEP 04 (2022) 103, arXiv:2202.07392.
- *Read:* full text, searched.
- *What it establishes:*
  - With T³ space, A–B is first order (the shift exponent is close to 1), and "the B−C phase transition was also a
    first-order transition" with a modified fit.
  - Introduction: "The C−C_b transition was found to be a second-order transition in the case where the spatial
    topology was S³ and (seemingly) a first-order transition when the spatial topology was T³."
  - The conjecture: "phase transitions which involve a change in topology will be first-order transitions."
- *Bearing:* *ours, unverified.* The graph model's rungs change what the torus looks like at large scale: a curled
  direction becomes an open one. If that counts as a change of topology in their sense, their conjecture predicts that
  each rung's change is first order. That fits T7's two-state change in 2D and T32's fixed wall in 3D. Whether "change
  in topology" covers a change in which cycles are short is exactly the question to ask them (section (d)).

**[ADGGNR25]** J. Ambjørn, Z. Drogosz, J. Gizbert-Studnicki, A. Görlich, D. Németh and M. Reitz, "Machine learning in
phase transition analysis of lattice quantum gravity", JHEP (2026) 150, arXiv:2510.02159.
- *Read:* abstract only. Recorded to show that the group is active in 2025 and 2026.

**Seen but not read:**
- Battefeld and Watson's string gas review (hep-th/0510022).
- Brandenberger's 2026 "Multi-matrix quantum mechanics, collective fields and emergent space" (arXiv:2605.13972),
  title only.
- Blanco-Pillado et al., "Tunneling potentials to nothing" (arXiv:2311.18821), title only.
- Chou, Nishimura and Wang, "Monte Carlo studies of the emergent spacetime in the polarized IKKT model"
  (arXiv:2507.18472), title only.

---

## (c) Predictions from the literature that the six- and eight-link runs could test

Each is a published pattern translated into the graph model. **The translations are ours and unverified.** None is a
pre-registration: each would need its own entry, with the owner's prediction, before any run (rule 4).

1. **All or nothing against one at a time** ([EGJK05] Sec. 7). From a fully curled start with random baths across the
   window, histogram the number of directions that end open. [EGJK05] predicts a bimodal distribution, nearly all
   closed or all open, with intermediate counts rare. FIRST ONLY predicts a peak at one. T30's single-bath runs already
   lean one way; a scan over bath energies would say whether that holds everywhere or only below some energy.
2. **Successive pushes, and the delay between them** ([GKM13] Table 2). Give two sparks to a 4 × 4 × L torus, the second
   after a delay of Δt sweeps. Measure how often the second direction opens as a function of Δt. [GKM13]'s pattern, by
   analogy, is that success falls with delay. In the graph the mechanism would be the first rung's released energy
   leaking or spreading out of reach. Cheap: the sealed machinery and the spark exist (Q12, Q22).
3. **Stages ordered by the height of what holds each one** ([ABE00] Sec. III). Directions open in order of rising wall,
   with a plateau at each intermediate rung whose lifetime tracks that rung's wall. This is already the project's own
   prediction for T33; [ABE00] is the published precedent to cite beside it.
4. **Isotropization after a staggered start** ([WB03]). When two or more directions do open, measure whether the final
   flat torus has equal sides or keeps the shape of the order in which it opened (for example 8 × 8 × 8 against
   4 × 8 × 16 at N = 512). [WB03] predicts isotropy through a feedback that the graph lacks. O55's symmetry counts give
   8 × 8 × 8 and 4 × 4 × 32 equal weight, so without such a feedback nothing favors the cube. A measurable difference,
   and cheap: read the side lengths from the saved final wiring.
5. **First order at each rung, because each changes the large-scale shape of the torus** ([AGGN22] conjecture). Each
   rung change should show two-state coexistence (seed and front, nothing in between) with a barrier that does not grow
   with N. T32 (FIXED WALL) and T30 (a front) already point this way for the first six-link rung. The eight-link rungs
   in T33 are the next place to check.
6. **A barrier that depends on the number of directions** (no published counterpart found). The literature treats the
   compact space as a sphere or a single volume modulus ([GM04], [CJR09], [BSV10]), so it offers no law for the barrier
   against k. The project's exact walls are its own prediction. Their ordering holds at every λ > 1, and their exact
   factor of two holds at λ = 1.25 only (section (a)). If a note to a physicist calls the walls "doubling", it should
   say "at λ = 1.25".
7. **Three as a ceiling, not a tie** ([BV89], [Sak96], [GKM10], [BP24]). In string gas cosmology, three is the most
   directions whose windings can annihilate. *Ours:* the graph model has no winding objects, so it has no reason to
   stop at three, and the eight-link run (T33) can open a fourth. If it does, that is a difference from string gas
   cosmology worth one sentence in the eight-link write-up.
8. **The signature of opening one at a time** ([GHR10]). In the cosmological version, one direction opened last leaves
   curvature that differs between directions. *Ours:* the model's counterpart is the local-dimension census over time
   during T33. A "singleton plus three" or a strictly sequential pattern is the model's version of the anisotropic
   parent, and a single tied step is the version of the isotropic one.

---

## (d) Who to ask, one narrow question each

**UVA first, and the honest answer is that nobody there works on this.** We checked the recent arXiv listings of Diana
Vaman: worldline QFT, composite gravity (2512.06132) and higher-derivative black holes (2605.31331, with Kent Yagi). Her
nearest paper is 2020, "Probing compactified extra dimensions with gravitational waves" (2004.03051, with Yagi and
others), where the compact dimensions are fixed. A coffee question to her would be a request for a pointer, not a
question inside her work. Peter Arnold's listing could not be fetched. The web search found no UVA faculty with
2024–2026 work on decompactification. The three below are outside UVA. Each letter would carry the project's standard
AI-disclosure sentence and follow `outreach-preferences`.

1. **Jun Nishimura (KEK; the Lorentzian type IIB matrix model).** His 2026 papers (2604.19836, and 2604.25564 by title)
   are the most recent numerical results in which several directions open. *Question:* "In your complex Langevin runs
   (arXiv:2604.19836), do the three large eigenvalues of T_ij(t) separate from the other six at the same time, or does
   one separate first and the others follow?" Answerable from his own data. We read neither paper stating it.
2. **Robert Brandenberger (McGill; string gas and matrix cosmology).** 2409.00254 (2024, read) and 2605.13972 (2026,
   title only). *Question:* "In the D1-string argument of arXiv:2409.00254, is there any reason the three directions
   that become large must do so together, or could each open after its own windings annihilate, one at a time, as
   [GKM13] assumes? In a toy graph model we see curled directions open one at a time, each behind its own barrier, and
   one push opens only one of them. Does string gas cosmology predict an order we could test?" His answer would
   settle whether the owner's "tied" rule has a string-gas counterpart.
3. **Jakub Gizbert-Studnicki (Jagiellonian University, Kraków; toroidal CDT).** 2202.07392 (read), 2408.07808 and
   2411.02330 (titles), and 2510.02159 (2025, JHEP 2026, abstract). *Question:* "Your 2022 conjecture says that
   transitions which involve a change in topology are first order. Would it cover a transition in which one cycle of a
   spatial torus shrinks to lattice size while the others stay large, and has any CDT phase shown the three cycles of
   the spatial T³ behaving differently without an added scalar field?" This is the question closest to his work, and
   it bears directly on prediction 5.

*An alternative, if a bubble-of-nothing specialist is wanted:* José Juan Blanco-Pillado (Bilbao). His published work on
bubbles of nothing and on transdimensional tunneling is from 2010 to 2024 ([BSV10], [BPS10], [BEHS24]). His 2025–2026
listing is on domain walls and cosmic strings, so a question on decompactification would sit outside his current work.

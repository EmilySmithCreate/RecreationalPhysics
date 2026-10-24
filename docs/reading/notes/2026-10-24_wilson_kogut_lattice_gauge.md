# Reading note: Wilson (1974) and Kogut (1979) on lattice gauge theory, and the compact U(1) facts the record uses

*Kinds of statement as in CLAUDE.md rule 10. Written 24 October 2026 (`date`: Sat Oct 24 19:33 EDT 2026) by one
assistant agent, with no checking agent. It backs ASSUMPTIONS Q29 and O151, `src/graphity/u1.py` and decision 0 of
`docs/design/u1_rewiring_graph_brief_2026-10-24.md`. Every quotation below is from text extracted locally from a PDF
with PyMuPDF; equation and section numbers are as printed in those PDFs.*

## The two papers asked for

| Key | Bibliographic data | Read status (exact) |
|---|---|---|
| [Wil74] | K. G. Wilson, "Confinement of quarks", Phys. Rev. D 10, 2445–2459 (1974), doi:10.1103/PhysRevD.10.2445; preprint CLNS-74-262; reprinted in C. Rebbi (ed.), *Lattice Gauge Theories and Monte Carlo Simulations*, pp. 45–59 (INSPIRE record 89145). | **Abstract only.** No legal open copy of the full text was found. The APS page returned HTTP 403. The abstract was read twice: from INSPIRE's API (APS source) and from a scan of the paper's first page shown on slide 3 of C. Davies, "50 years of Lattice QCD" (Higgs–Maxwell meeting, February 2024; conference.ippp.dur.ac.uk, attachment 6834), which shows only the title block and abstract. Also read in part: Wilson's own retrospective, "The Origins of Lattice Gauge Theory", arXiv:hep-lat/0412043, Sec. 1–2 (the bullet list describing the 1974 formulation). The body of [Wil74] (its action, its equation numbers, its strong-coupling expansion) has **not** been read. |
| [Kog79] | J. B. Kogut, "An introduction to lattice gauge theory and spin systems", Rev. Mod. Phys. 51, 659–713 (1979), doi:10.1103/RevModPhys.51.659; preprint ILL-TH-79-4 (INSPIRE record 140498). | **Abstract only.** No legal open copy was found (searched: arXiv, INSPIRE, APS, course pages including the SLAC lattice course bibliography, which lists it without a link). The APS page returned HTTP 403. The abstract was read from INSPIRE's API (APS source). Nothing in its body has been read. |

So neither paper can be cited for any specific equation. Both stay "Not read" for their bodies in `REFERENCES.bib`
(their notes there say "Not read"; this note would allow "abstract read" to be added, which is the owner's or the main
session's edit, not this note's).

What the two abstracts do say, verbatim:

- [Wil74]: "It is shown how to quantize a gauge field theory on a discrete lattice in Euclidean space-time, preserving
  exact gauge invariance and treating the gauge fields as angular variables (which makes a gauge-fixing term
  unnecessary). The lattice gauge theory has a computable strong-coupling limit; in this limit the binding mechanism
  applies and there are no free quarks."
- [Kog79]: "The renormalization group of the two dimensional planar model is presented as an illustration of a phase
  transition driven by the condensation of topological excitations. Parallels are drawn to Abelian lattice gauge theory
  in four dimensions."

A correction for the brief that asked for this note: arXiv:hep-lat/0208009 is **not** a Kogut review. Its abstract
page gives G. Andronico, A. Coniglio and S. Fortunato, "A Geometrical Interpretation of Hyperscaling Breaking in the
Ising Model" (Lattice 2002). It was not used.

An open textbook exists: H. J. Rothe, *Lattice Gauge Theories: An Introduction*, 4th ed. (World Scientific, 2012),
open access through OAPEN (SCOAP3). Its PDF sits behind a bot check on library.oapen.org and was **not** read.

## The open sources used instead (all arXiv; read as stated)

| Short name | Bibliographic data | Read status |
|---|---|---|
| Gupta | R. Gupta, "Introduction to lattice QCD", Les Houches lectures, arXiv:hep-lat/9807028 | Sec. 7.1 (Eqs. 7.1–7.4), Sec. 14.2.2 (Eqs. 14.18–14.19 and the paragraph after), Sec. 15 (first two pages) read in full |
| Loan et al. | M. Loan, M. Brunner and C. Hamer, "Static quark potential and string tension for compact U(1) in (2+1) dimensions", arXiv:hep-lat/0208047 | Sec. I, Sec. II (Eqs. 1–8) and Appendix A (Eqs. A7–A15) read in full |
| Gattringer et al. | C. Gattringer, T. Kloiber and M. Müller-Preussker, "Dual simulation of the 2-dimensional lattice U(1) gauge-Higgs model with a topological term", Phys. Rev. D 92, 114508 (2015), arXiv:1508.00681 | Sec. II.B (Eqs. 4–5, 12) and Sec. III.A (Eqs. 21–24) read in full |
| Albandea et al. | D. Albandea, P. Hernández, A. Ramos and F. Romero-López, "Topological sampling through windings", Eur. Phys. J. C 81, 873 (2021), arXiv:2106.14234 | Sec. II.A (Eqs. 4–9) read in full |
| Arnold et al. | G. Arnold, B. Bunk, Th. Lippert and K. Schilling, "Compact QED under scrutiny: it's first order", Lattice 2002 proceedings, arXiv:hep-lat/0210010 (related DOI 10.1016/S0920-5632(03)01704-3) | Read in full (3 pages) |
| Vadacchino et al. | D. Vadacchino, M. Caselle et al., "Effective string description of the interquark potential in the 3D U(1) lattice gauge theory", arXiv:1410.7436 | Introduction only (the sentence quoted below) |
| Kaplan–Stryker | D. B. Kaplan and J. R. Stryker, "Gauss's law, duality, and the Hamiltonian formulation of U(1) lattice gauge theory", Phys. Rev. D 102, 094515 (2020), arXiv:1806.08797 | Introduction and Sec. I (Eqs. 1–5, Fig. 1 and its caption) read in full |
| Wilson 2004 | K. G. Wilson, "The Origins of Lattice Gauge Theory", arXiv:hep-lat/0412043 | Sec. 1 and the formulation list in Sec. 2 read |

Journal references were taken from the arXiv abstract pages on 24 October 2026. Works cited *inside* these sources
(Polyakov 1977; Göpfert and Mack; Kogut and Susskind 1975) were not read and are named only as those sources cite them.

## The facts, one by one

### (a) The Wilson action for compact U(1), and the constant per plaquette

**The record says** (Q29; `u1.py` docstring): a phase θ on every link, the holonomy round each square φ_p, energy
κ Σ_p (1 − cos φ_p), Monte Carlo weight exp(β Σ_p cos φ_p), "the standard Wilson action".

**The sources.**

- Loan et al., Sec. II, Eqs. (1)–(3): "S = β Σ_{r,μ,ν} Re Tr P_{μν}", with "P_{μν}(r) = [1 − Re Tr{U_μ(r) U_ν(r+μ̂)
  U†_μ(r+ν̂) U†_ν(r)}]" and "U_μ(r) = exp[ieaA_μ(r)] = exp[iθ_μ(r)]" (θ ∈ [0, 2π], "the gauge field on the directed
  link r → r + μ̂"); Eq. (4) β = 1/g². They cite Wilson for the action (their ref. [2]). So in this source the action is
  **β Σ (1 − cos θ_p)**.
- Gupta, Sec. 7.1, Eq. (7.3): "Re Tr(1 − W^{1×1}_{μν}) = (a⁴g²/2) F_{μν}F^{μν} + terms higher order in a", and the U(1)
  sum "(1/g²) Σ_x Σ_{μ<ν} Re Tr(1 − W^{1×1}_{μν}) → (1/4) ∫ d⁴x F_{μν}F^{μν}"; Eq. (7.4) the SU(3) Wilson action
  "S_g = (6/g²) Σ_x Σ_{μ<ν} Re Tr (1/3)(1 − W)". Again with the "1 −".
- Arnold et al., Sec. 2: "4d pure U(1) gauge theory with Wilson action S = −β Σ_{n,ν>μ} cos(θ_{μν}(n))". **Without**
  the constant.
- Gattringer et al., Eq. (5): "S_G[U] = −(β/2) Σ_x (U_{x,p} + U*_{x,p})", that is −β Σ cos θ_p. Albandea et al.,
  Eq. (4): the weight "e^{(β/2) Σ_p (U_p + U_p†)}". Also without the constant.
- Wilson 2004, Sec. 2, describing the 1974 formulation: gauge variables "located on nearest neighbor links" and
  "unitary matrices from the gauge group itself", "plaquette-type couplings of the gauge variables with a coefficient of
  order 1/g²", "a separate gauge invariance of the theory for each lattice site", and finite results "without any
  requirement for gauge fixing terms".

**Verdict: confirms, with a qualification.** The form (phases on directed links, holonomy round the plaquette, a
cosine of it, coupling β = 1/g²) is confirmed at four independent open sources. On normalisation, **both conventions
are in standard use**: β Σ (1 − cos θ_p) (Loan et al.; Gupta) and −β Σ cos θ_p (Arnold et al.; Gattringer et al.;
Albandea et al.). None of these sources comments on the difference; on a fixed lattice it multiplies Z by e^{−βP}
and cancels from every expectation value, which is why it is treated as a convention (ours, elementary). **None of
them discusses a lattice whose number of plaquettes changes**, so no source read here says which zero is right when P
varies. What Wilson's own 1974 equation is cannot be said from this reading.

The record's own two zeros (energy κ Σ (1 − cos φ) and Monte Carlo weight exp(β Σ cos φ)) are each one of the two
standard conventions; on the fixed graphs of Q29 they give the same physics (ours, elementary).

### (b) The character (Bessel) expansion in two dimensions

**The record says** (Q29; `u1.py`, `exact_mean_cos_2d`): on a closed two-direction torus with P squares,
Z = Σ_n I_n(β)^P and ⟨cos φ⟩ = Σ_n I_n^{P−1} (I_{n−1} + I_{n+1})/2 / Σ_n I_n^P; on an infinite lattice the plaquettes are
independent and ⟨cos φ⟩ = I₁(β)/I₀(β). Q29 calls this "ours, textbook, to verify at its source".

**The sources.**

- Loan et al., Appendix A, Eq. (A7): "e^{−β(1−cos θ(r))} → Σ_{l=−∞}^{∞} e^{ilθ} e^{−β} I_l(β)", "where I_l(β) is the
  modified Bessel function and exp(ilθ) is the character of the plaquette variable in the lth irreducible
  representation of the compact U(1) group". This is the single-plaquette character expansion, written for the
  (1 − cos) normalisation, so each character carries the factor e^{−β}.
- Gattringer et al., Sec. III.A, Eq. (23), pure gauge ("quenched") on a 2D N_t × N_s periodic lattice:
  "Z = Σ_{q=−∞}^{+∞} [ I_{|q|}(2√(ηη̄)) (√(η/η̄))^q ]^{N_s N_t}", with Eq. (12) η, η̄ = β/2 ∓ θ/4π. At vacuum angle
  θ = 0 this is **Z = Σ_q I_q(β)^{N_s N_t}**, N_s N_t being the number of plaquettes. Their reason: the flux constraints
  "force the plaquette occupation numbers p_x ∈ Z to have the same value q at each lattice site"; and "The modified
  Bessel functions I_n decay faster than exponentially with the index n and thus the series (23) converges rapidly."
- Albandea et al., Sec. II.A, Eq. (7): "P = Σ_n I′_n[β] I_n[β]^{V−1} / Σ_n I_n[β]^V" for the plaquette ⟨Re U_p⟩ at
  finite β and V (V the number of plaquettes, periodic boundary conditions), and Eq. (9): "lim_{V→∞} P = I₁(β)/I₀(β)".

**Verdict: confirms, exactly.** Since I′_n = (I_{n−1} + I_{n+1})/2, Albandea et al.'s Eq. (7) is term for term the
formula in `exact_mean_cos_2d`, and their Eq. (9) is the record's infinite-lattice value. Gattringer et al.'s Eq. (23)
at θ = 0 is the record's Z. Q29's "to verify at its source" can become "sourced: Albandea et al. 2021, Eqs. (7) and
(9); Gattringer et al. 2015, Eq. (23)". Two cautions: (i) these are 2D square lattices; the toy's four-link torus with
every side ≥ 6 is that lattice, but a side-4 curl adds the ring as an extra square, which these sources do not cover;
(ii) the Q29 addendum's point that the torus constraint is on an alternating-sign sum is consistent with Gattringer et
al.'s derivation, where fluxes on each link must cancel between the two plaquettes sharing it, and the answer does not
depend on the signs because I_{−n} = I_n (ours, from their Eq. (22)).

### (c) Free photons: lattice dispersion and d − 1 polarisations

**The record says** (Q29; O151): the linearised field on a flat torus gives waves with ω² = Σ_i 4 sin²(k_i/2), d − 1
polarisations, and zero modes (N − 1) gauge plus d holonomies (tested in `tests/test_u1.py`).

**The sources.**

- Loan et al., Sec. II: "If one takes the 'naive' continuum limit at a fixed energy scale, one regains the simple
  continuum theory of non-interacting photons" (for compact U(1) in 2+1). Appendix A, Eqs. (A14)–(A15): the
  three-dimensional lattice massless propagator,
  G(k) = Δτ / [4 sin²(k₀/2) + Δτ² (4 − 2 cos k₁ − 2 cos k₂)], with 4 − 2 cos k = 4 sin²(k/2) for each direction.
- Kaplan–Stryker, Sec. I, Fig. 1 caption, for n sites and nd links on a periodic lattice in d space dimensions:
  "The (n − 1) = 15 links on a maximal tree ... are eliminated via Gauss's law. The d = 2 links ... are eliminated by
  constraining the net electric flux ... to equal the topological quantum numbers ν_{x,y}. The remaining (n−1)(d−1)
  = 15 black links represent the physical variables of the theory. This procedure generalizes to arbitrary d, n."

**Verdict: confirms in substance; the explicit formula is ours.** The count is confirmed exactly: nd links minus
(n − 1) gauge minus d topological (holonomy) variables leaves (n − 1)(d − 1), i.e. d − 1 physical variables per site,
which is the record's zero-mode count and its d − 1 polarisations. The 4 sin²(k/2) kernel is confirmed as the lattice
massless operator. The record's ω² = Σ 4 sin²(k_i/2) is not printed in these sources in that form; it is the pole of
(A15) in the limit of continuous time, Δτ → 0 with k₀ = iωΔτ (ours, unverified, elementary), and it is tested in
code.

### (d) Confinement in three dimensions and the transition in four

**The record says** (the brief for this note): compact U(1) in 3D (2+1) confines at all couplings (Polyakov,
monopoles); in 4D there is a transition, β_c ≈ 1.01, between a confined and a Coulomb phase.

**The sources.**

- Loan et al., Sec. II: "if one renormalizes or rescales in the standard way so as to maintain the mass gap constant,
  then one obtains a confining theory of free massive bosons. Polyakov [26] showed that a linear potential appears
  between static charges due to instantons in the lattice theory; and Göpfert and Mack [27] proved that in the
  continuum limit the theory converges to a scalar free field theory of massive bosons." Eqs. (5)–(6): mass gap
  am_D = √(8π²/g²) exp(−π² v(0)/g²) and string tension bounded by a²σ = c √(g²/2π²) exp(−π² v(0)/g²), with Eq. (7)
  v(0) = 0.2527 (isotropic lattice); "The theory has a non-vanishing string tension for arbitrary large β". Eq. (8):
  at small β, a²σ = −ln β/2 + ...
- Vadacchino et al., introduction: "A semi-classical analysis shows that this theory is confining for all values of β,
  and that it reduces to a theory of free massive scalars for β ≫ 1."
- Gupta, Sec. 14.2.2 after Eq. (14.19): "Thus all gauge theories, including U(1), confine in the strong coupling limit.
  What distinguishes U(1) from non-abelian gauge theories is that the U(1) gauge theory has a phase transition at
  g² ∼ 1 (see Section 15), and the physical theory (electrodynamics) lies in the weak coupling region which is
  analytically disconnected from the confining strong coupling limit." Sec. 15: "there should exist a phase transition
  separating the strong coupling and weak coupling phases of non-confining theories like U(1). This has been
  established for U(1), both analytically [130] and by Monte Carlo simulations [131]." (4D.)
- Arnold et al., abstract and Sec. 4: 4D compact pure U(1) with the Wilson action, lattices L = 6 to 18: "strong
  evidence for a first-order phase transition"; "an average infinite volume transition coupling
  β_T = 1.0111331(21)"; Sec. 6: "the phase transition in compact 4d U(1) theory with Wilson action is first-order".
- [Kog79], abstract: "Parallels are drawn to Abelian lattice gauge theory in four dimensions" (to the 2D planar model's
  transition "driven by the condensation of topological excitations"). That is all that can be taken from Kogut here.

**Verdict: confirms, with two qualifications.** (i) 3D (2 + 1): confining at every β is confirmed (semi-classical,
Polyakov; proved in the continuum limit by Göpfert and Mack, as cited by Loan et al.); the string tension falls as
exp(−π² v(0) β) at large β, so it is exponentially small but not zero. Polyakov's paper itself was not read.
(ii) 4D: β_c "about 1.01" is confirmed and sharpened, β_T = 1.0111331(21) for the Wilson action on the isotropic
hypercubic lattice, and the transition is first order by that study. The value is specific to the Wilson action on that
lattice (Gupta's "g² ∼ 1" is the same statement roughly); it does not carry over to a different graph or to the
Hamiltonian (continuous-time) limit (ours, general knowledge, to verify).

### (e) Gauss's law and gauge invariance on the lattice

**The record says** (Q29; `u1.py`): gauge transformation θ(uv) → θ(uv) + α_u − α_v leaves every holonomy unchanged;
charge at a point Q_x = Σ E over outgoing links minus incoming, E conjugate to θ; on a closed graph the charges add to
zero.

**The sources.**

- [Wil74] abstract: the lattice formulation preserves "exact gauge invariance" with gauge fields as "angular variables
  (which makes a gauge-fixing term unnecessary)". Wilson 2004, Sec. 2: "a separate gauge invariance of the theory for
  each lattice site".
- Kaplan–Stryker, Sec. I: the electric field E_ℓ on each link is conjugate to the link variable, Eq. (2)
  "[Ê_ℓ, Û_ℓ′] = δ_{ℓ,ℓ′} Û_ℓ", and "has integer eigenvalues ε_ℓ, analogous to the angular momentum of a particle on a
  circle"; "The physical subspace H_phys ⊂ H consists of those states obeying the Gauss law constraint ∇·E = 0, i.e.,
  those states invariant under spatial gauge transformations. On the lattice, the analogue constraint is that at each
  lattice site the product of the Q̂ on each outgoing link and Q̂† on each incoming link must equal the unit operator",
  Eq. (5), with Q̂_ℓ = e^{iξÊ_ℓ}. The Kogut–Susskind Hamiltonian is their Eq. (3) in the limit ξ → 0.

**Verdict: confirms, with a qualification.** The lattice Gauss law is the outgoing-minus-incoming divergence at each
site, as the record has it, and it generates the site-by-site gauge transformation. The qualification: in the quantum
compact theory E has **integer** eigenvalues (Kaplan–Stryker, after Eq. (2)), so charges are integers; the record's
field is classical, E = θ̇ real-valued, and its "charges add to zero, real-valued or mod 3" is a property of any
divergence on a closed graph (ours, elementary), not a quantisation. Nothing in the sources read says how charge mod 3
would arise.

## What it supplies to the toy

1. **Q29's Gate U1 formula is now sourced** (fact (b)): Albandea et al. Eqs. (7), (9) and Gattringer et al. Eq. (23)
   give exactly what `exact_mean_cos_2d` computes, for the two-direction torus with every side ≥ 6. It remains ours for
   a graph with a side-4 ring.
2. **Decision 0 (the zero of a square's energy) gets no answer from the literature, and the reason is stated** (fact
   (a)). Both zeros are standard; every source read works on a lattice with a fixed number of plaquettes, where the zero
   cancels. *Ours, unverified:* when the number of squares varies, a constant per square is the same thing as a shift
   of the toy's own reward per square (the 16 in H = 16(N − S) + ...), so decision 0 is equivalent to choosing that
   bare coefficient; the physics sits in the combination, as the cosmological constant absorbs the gauge field's
   per-face weight in dynamical triangulations (Candido et al. 2021, as recorded in
   `2026-10-24_prior_work_gauge_on_dynamical_graphs.md`, not re-read here). Loan et al.'s Eq. (A7) shows the factor
   e^{−β} I_l(β) per character that the brief's "e^{−β} I₀(β) < 1" uses, so the brief's arithmetic for the (1 − cos)
   zero is consistent with a published expansion.
3. **Is the toy's photon confined?** *Ours, unverified, and the most useful consequence.* It depends on which object is
   meant:
   - The **Monte Carlo** of `u1.py` samples exp(β Σ cos φ) on the spatial graph treated as a Euclidean lattice. On the
     four-link torus that is 2D compact U(1): exactly solvable and confining at every β (Wilson loops fall with area;
     general knowledge, to verify; consistent with the factorised Z of fact (b)). On the six-link torus it is a 3D
     Euclidean theory, i.e. the (2 + 1) theory of fact (d): **confining at every β, with a string tension of order
     exp(−π² × 0.2527 × β)**, tiny at large β but not zero. So a six-link Monte Carlo has no Coulomb phase to find,
     and any measured "photon" there is the Polyakov photon made massive by monopoles at long distance.
   - The **classical waves** of `u1.py` (θ̇ dynamics, continuous time, three space directions on the six-link torus)
     are a (3 + 1)-dimensional theory. Linearised they are free photons with d − 1 = 2 polarisations (fact (c));
     confinement in (2 + 1) is an effect of instantons (monopoles) in Euclidean time and does not show in classical
     linear waves. The relevant quantum statement for 3 + 1 is the 4D one: a Coulomb (massless photon) phase at weak
     coupling beyond a first-order transition, at β_T ≈ 1.011 for the isotropic Wilson lattice. Where that transition
     sits for the toy's graphs, or in continuous time, is not known from this reading.
   - On the four-link toy (2 + 1 in the wave picture) the quantum theory would be confining at all couplings (fact (d)),
     so a "photon" of the two-dimensional toy is, quantum mechanically, never free at long distance.
4. **O151's mass is consistent in kind with the counting of fact (c).** The side-4 ring adds plaquettes that pin one
   of the d topological holonomies (Kaplan–Stryker's ν), which is why the record finds D − (number of side-4 axes)
   holonomy zero modes. The literature read here does not treat a ring of length 4 as a plaquette; that remains the
   toy's own rule (Q29, ours), as O151 already says.
5. **Read next, if wanted:** Rothe's open textbook (4th ed., OAPEN), chapters on compact U(1) and the strong-coupling
   expansion, which would let [Wil74] and [Kog79]'s standard content be cited from a read source; and Polyakov (1977)
   for fact (d), which no open copy was sought for here.

# Reading: Jacobson, entanglement equilibrium and the Einstein equation (2016), with two follow-ups, and what it becomes on the quantum toy

*Date of the reading: 2026-11-02 (clock checked: 17:52 UTC). Who read: an assistant agent (Claude Opus 5.5), on the
instruction of the session scoping the quantum toy (`docs/design/quantum_toy_brief.md`, section 3, "Jacobson's
reader", and step 0 of section 5). The owner has not read these passages. Each paper was fetched as the arXiv PDF and
its text extracted with PyMuPDF; quotations are from that extraction with ligatures restored and are to be checked
against the PDF before any of them appears in a paper or a letter. Section 1 to 4 are "published" (the papers' own
text, or a close paraphrase with the section or equation number). Section 5 is ours throughout, unverified by a
physicist. Rule 13 applies: these papers define what a quantum toy would have to reproduce; nothing here is evidence
that it does. Jacobson's 1995 paper [Jac95] is summarized in
`docs/reading/notes/2026-10-05_dark_energy_and_entropic_gravity.md` and is not repeated here.*

## Read status, paper by paper

| Key | Paper | How read |
|---|---|---|
| [Jac16] | T. Jacobson, "Entanglement Equilibrium and the Einstein Equation", arXiv:1505.04753v4 (25 Jun 2016); Phys. Rev. Lett. 116, 201101 (2016), DOI 10.1103/PhysRevLett.116.201101 (arXiv abstract page, checked 2026-11-02) | **Read in full** from the PDF: 8 pages, Secs. I to VI, Eqs. 1 to 27, Appendices A to D (Eqs. A1 to A5, B1 to B5, C1, D1 to D7), Fig. 1 by its caption, the reference list. |
| [JV19] | T. Jacobson, M. Visser, "Gravitational Thermodynamics of Causal Diamonds in (A)dS", arXiv:1812.01596v3 (13 Dec 2019); SciPost Phys. 7, 079 (2019), DOI 10.21468/SciPostPhys.7.6.079 (arXiv abstract page, checked 2026-11-02) | **Read in part**, for the first-law statement and its link to [Jac16]: Abstract; Sec. 1 (Eqs. 1.1 to 1.5); Sec. 4.2 (quantum corrections, Eqs. 4.6 to 4.17); Sec. 4.3 (entanglement equilibrium, Eqs. 4.18 to 4.24, with footnotes 26 to 28); Sec. 4.4 opening (Eqs. 4.25 to 4.28); Sec. 6 (discussion). The Smarr formula (Sec. 3.1), the derivation of the first law (Sec. 3.2 and 3.3), the limiting cases (Sec. 5) and the appendices were not read. |
| [BMSV17] | P. Bueno, V. S. Min, A. J. Speranza, M. R. Visser, "Entanglement equilibrium for higher order gravity", arXiv:1612.04374v1 (13 Dec 2016); Phys. Rev. D 95, 046003 (2017), DOI 10.1103/PhysRevD.95.046003 (arXiv abstract page, checked 2026-11-02) | **Read in part**: Abstract; Sec. I and I.A (Eqs. 1 to 7); the opening of Sec. II (Eq. 8); Sec. III.B (Eqs. 51 to 55); the end of Sec. IV; Sec. V's opening and its Sec. V.D ("Future work") items on higher order perturbations, nonconformal matter, nonminimal couplings and gauge fields, and nonspherical subregions. The derivation of the generalized volume (Sec. II) and the JKM analysis (Sec. III.A) were not read. |
| [CR16] (exists) | S. M. Carroll, G. N. Remmen, "What is the Entropy in Entropic Gravity?" | **Not re-read**: its verdict on [Jac16] is taken from `docs/reading/notes/2026-11-02_carroll_compactification_and_entropic.md`, section 2.5, where it was read in full. |

---

## 1. [Jac16]: the hypothesis and the one assumption about the ultraviolet (published)

**The hypothesis**, which [Jac16] calls the maximal vacuum entanglement hypothesis (MVEH), in its words (Sec. I):
"When the geometry and quantum fields are simultaneously varied from maximal symmetry, the entanglement entropy in a
small geodesic ball is maximal at fixed volume." It is "formulated in the context of semiclassical gravity, i.e.
quantum fields on a classical spacetime".

**The ultraviolet assumption** (Sec. I): "The area density of vacuum entanglement entropy η is finite and universal."
It "involves UV aspects of quantum gravity that are not currently understood, so it remains an assumption." In Sec. IV:
"we are assuming that, as a result of the UV physics, the entanglement entropy in a spatial region is finite in any
state, with a leading term ηA", η "a universal constant with dimensions [length]^(2−d)"; "The scaling with area is
natural in any theory with a large density of states at short distances. The assumption that η is universal is
motivated by the idea that the UV structure of the vacuum is common to all states in the class being considered."
Footnote 2 adds that this picks a conformal frame, "the one for which η is constant in spacetime", which "turns out to
satisfy the Einstein equation".

**What the abstract claims, and at what strength.** "A qualitative argument suggests that the Einstein equation
implies validity of the hypothesis. A more precise argument shows that, for first-order variations of the local
vacuum state of conformal quantum fields, the vacuum entanglement is stationary if and only if the Einstein equation
holds. For nonconformal fields, the same conclusion follows modulo a conjecture about the variation of entanglement
entropy."

## 2. [Jac16]: the steps, with equation numbers (published)

### 2.1 Geometry only: the area deficit at fixed volume (Sec. II, App. A)

A geodesic ball Σ of radius ℓ about a point o, orthogonal to a timelike unit vector u, in a spacetime of dimension d,
with ℓ ≪ L_curvature (Eq. 2). To lowest order, the volume and area changes at fixed radius relative to flat space are
Eqs. 3 and 4, δV|_ℓ = −Ω_(d−2) ℓ^(d+1) R / [6(d−1)(d+1)] and δA|_ℓ = −Ω_(d−2) ℓ^d R / [6(d−1)], with R the spatial Ricci
scalar at o. Adjusting the radius so the volume is unchanged gives the **area variation at fixed volume** (Eq. 5):
δA|_V = δA − [(d−2)/ℓ] δV = −Ω_(d−2) ℓ^d R / [2(d²−1)], "smaller by the factor 3/(d+1) than the variation at fixed
radius". Since R = 2G_00 (Eq. 6), δA|_V = −Ω_(d−2) ℓ^d G_00 / (d²−1) (Eq. 7), and with Einstein's equation (Eq. 1),
δA|_V = −8πG Ω_(d−2) ℓ^d T_00 / (d²−1) (Eq. 8). "Conversely, this simple geometrical relation contains the full content
of Einstein's equation, if it holds at all spacetime points and for all timelike unit vectors." App. A traces the
geometric relations to Pauli's 1921 review (Sec. 17) and Feynman's statement of the Einstein equation as a radius
excess of GM/3c² for a small sphere.

### 2.2 The diamond and its conformal Killing vector (Sec. III, App. B)

The causal diamond D(Σ) of a flat ball has a unique spherically symmetric conformal Killing vector preserving it,
ζ = (1/2ℓ)[(ℓ² − u²)∂_u + (ℓ² − v²)∂_v] (Eq. 9; in t, r, Eq. 10), with L_ζ η_ab = −(2t/ℓ) η_ab (Eq. 11). It vanishes on
∂Σ, which is therefore a bifurcation surface, and its surface gravity is 1 with this normalization.

### 2.3 The split δS = δS_UV + δS_IR and the area term (Sec. IV)

"Under a simultaneous variation of the geometry and the state of the quantum fields, (δg_ab, δ|ψ⟩), the diamond
entanglement entropy variation will consist of two contributions, a state-independent UV part δS_UV from the area
change induced by δg_ab, and a state-dependent IR part δS_IR from δ|ψ⟩." With the assumption of Sec. 1,
**δS_UV = η δA** (Eq. 12), so **δS_tot = η δA + δS_IR** (Eq. 13). The MVEH "implies that the total entropy variation (13)
is zero at first order, and negative for finite variations, when comparing to a maximally symmetric spacetime with the
volume of Σ held fixed." The motivation offered is that of a free energy F = E − TS minimized at fixed volume, "but
with the additional feature that the energy vanishes" (compared with de Sitter space in App. C; the fixed volume is
traced in App. D to ζ being only a conformal Killing vector).

### 2.4 The modular Hamiltonian and the conformal-field-theory assumption (Sec. IV)

The vacuum restricted to the diamond is written "(formally)" as ρ = Z^(−1) exp(−K/T), T = ħ/2π (Eq. 14), K "the
'modular Hamiltonian'", normalized to generate boosts at the edge; for an infinite diamond (the Rindler wedge) T is the
Unruh temperature. Since ρ minimizes the modular free energy F_K = ⟨K⟩ − TS (Eq. 15), any small δρ gives
**δS = (2π/ħ) δ⟨K⟩** (Eq. 16), "just the usual Clausius relation for a 'thermal' state".

"In general K in (14) is not a local operator, and does not generate a geometric flow. **For a CFT, however, K is equal
to H_ζ**, the Hamiltonian generating the flow of the conformal boost Killing vector (9) [29]" (Hislop and Longo), "conformally
related to the better-known version that holds for any Poincaré invariant QFT restricted to the Rindler wedge [30]"
(Bisognano and Wichmann). So H_ζ = ∫_Σ T^ab ζ_b dΣ_a (Eq. 17). For an excitation with length scale much longer than the
diamond (Eq. 18), ⟨T_ab⟩ is constant over it and δ⟨H_ζ⟩ = Ω_(d−2) ℓ^d δ⟨T_00⟩ / (d²−1) (Eq. 19).

**Non-conformal fields, the δX term.** For a QFT with a UV fixed point and a diamond much smaller than any QFT length
scale (Eq. 20), "we conjecture, and we shall assume, that δ⟨K⟩ has the form of (D2) with an additional term δX that is
a spacetime scalar" (dashes in the original replaced by commas): δ⟨K⟩ = [Ω_(d−2) ℓ^d / (d²−1)] (δ⟨T_00⟩ + δX) (Eq. 21). Calculations by Casini, Galante and Myers
[31] and Speranza [32] "indicate that for a class of theories and states, this is the case, although in general δX may
carry ℓ dependence and can dominate at small ℓ." Footnote 3: an earlier draft had conjectured X = −(1/d)⟨T⟩.
*(A small observation of ours: "the form of (D2)" here appears to mean the form of Eq. 19; Eq. D2 is the symplectic
form in App. D. To check against the published version.)*

### 2.5 The result (Sec. V)

Equilibrium is postulated for the vacuum with the curvature of a maximally symmetric spacetime (MSS), G^MSS_ab = −λ g_ab,
"a local state parameter that is effectively constant in a small diamond but may depend on the diamond". Then
δA|_(V,λ) = −Ω_(d−2) ℓ^d (G_00 + λ g_00) / (d²−1) (Eq. 22), and
δS_tot|_(V,λ) = [Ω_(d−2) ℓ^d / (d²−1)] × [−η(G_00 + λ g_00) + (2π/ħ)(δ⟨T_00⟩ + δX)] (Eq. 23). Requiring it to vanish
"at all points and with all timelike unit vectors" gives G_ab + λ g_ab = (2π/ħη)(δ⟨T_ab⟩ + δX g_ab) (Eq. 24). The
Bianchi identity and energy conservation tie λ to δX, λ = (2π/ħη) δX + Λ (Eq. 25), **Λ "a spacetime constant"**, and so

**G_ab + Λ g_ab = (2π/ħη) δ⟨T_ab⟩** (Eq. 26), "Einstein's equation with an undetermined cosmological constant Λ",
with **G = 1/(4ħη)** (Eq. 27). "Stronger vacuum entanglement implies weaker gravity, i.e. greater spacetime rigidity."
The consistency check the paper emphasizes: with this G, ηA is the Bekenstein-Hawking entropy A/4ħG, and "The
coefficient would have been off by the factor (d + 1)/3 had we used the area variation at fixed radius (4) rather than
at fixed volume (5)."

**A correction from the follow-up.** [JV19] footnote 28: their Eq. 4.24 "agrees with the result in Ref. [21] after
correcting the sign error there of the δX term in (25), which appears due to an error in equation (24)." *Ours, from the footnote:* the sign of
δX in [Jac16] Eqs. 24 and 25 is wrong in the arXiv v4 text; the structure (Λ an integration constant) is unaffected.

### 2.6 What [Jac16] says it does not show (Sec. VI)

- **Only first-order variations.** "Strictly speaking the 'first-order variation' refers to the derivative with respect
  to a parameter labeling the state, evaluated at the vacuum. To be physically applicable, however, the result should
  apply to finite but small variations."
- **Coherent states are a counterexample to the converse at finite size.** A coherent state "can have nonzero energy
  density while leaving entanglement entropy unchanged [34, 35]. That is, not all energy registers as a change of
  entanglement. ... Unless a further consequence of that hypothesis is found, or the hypothesis is refined and
  strengthened in some way, **the Einstein equation does not appear to follow from it in all generality.**"
- **The scale window.** ℓ "much smaller than the local curvature length, the wavelength of any excitations of the
  vacuum, and the scales in the matter field theory, but much larger than the UV scale at which quantum gravity effects
  become strong."
- **The non-conformal assumption** (Eq. 21) "concerns only standard QFT, and is either true or false."
- **Gravitons** do not enter: "The UV part of the entanglement entropy S = ηA is inscrutable at this level, and the IR
  part does not include gravitons."
- **Higher curvature terms**: "Maybe", with the scale argument that the diamond would have to be smaller than the
  higher-curvature length ℓ₁, where geometry and QFT probably do not apply.
- **Non-equilibrium**: left as a question ("According to our derivation the Einstein equation is a property of vacuum
  equilibrium. Does this suggest how to include nonequilibrium effects?").

---

## 3. [JV19]: the first law of causal diamonds (published, read in part)

- **The classical first law** for Einstein gravity with fluid matter (Sec. 1): **δH_ζ = −(κ/8πG) δA** (Eq. 1.1), with
  H_ζ the total Hamiltonian along ζ, split as δH^m_ζ + δH^Λ_ζ + δH^g_ζ: matter δH^m_ζ = ∫_Σ δ(T^a_b) ζ_a u^b dV (Eq. 1.2);
  cosmological constant δH^Λ_ζ = V_ζ δΛ / 8πG with the "thermodynamic volume" V_ζ = ∫_Σ |ζ| dV (Eq. 1.3); and gravity
  δH^g_ζ = −(κk/8πG) δV (Eq. 1.4), k the trace of the extrinsic curvature of ∂Σ in Σ, a term that "arises because ζ fails
  to be a true Killing vector". The right-hand side is −T_H δS_BH, "Unlike for black holes, however, there is a minus
  sign in front, indicating that the temperature is negative."
- **The semiclassical first law**, for any quantum matter in a small diamond: −(κk/8πG) δV + (V_ζ/8πG) δΛ = T δS_gen
  (Eq. 1.5), T = −ħκ/2π, S_gen = S_BH + S_matter. "At fixed volume V and cosmological constant Λ this implies that the
  generalized entropy is stationary in a maximally symmetric vacuum. This coincides with the entanglement equilibrium
  condition of [21]" ([Jac16]). Footnote 4: for conformal matter this holds "for any sized diamond", for non-conformal
  matter it rests on the assumption (4.13).
- **The first law of entanglement** in their notation: for a CFT vacuum on a ball, the matter Hamiltonian equals the
  modular Hamiltonian K (Eq. 4.7), and δ⟨K⟩ = T_H δS_matter (Eq. 4.8): "If the variation is to a global pure state
  δS is purely entanglement entropy, which is why this is known as the 'first law of entanglement'."
- **The δX conjecture restated**: δ⟨H^m_ζ⟩ = δ⟨K⟩ − V_ζ δX (Eq. 4.13), "checked in [37, 38]" (the same two papers as
  [Jac16]'s [31, 32]), with the finding that "δX may depend on the radius R of the ball, and can dominate at small R
  (depending on the conformal dimension of the operator that deforms the CFT)." The δX is absorbed into a net
  δΛ := δλ − 8πG δX (Eq. 4.16).
- **Entanglement equilibrium as derived, not postulated**: δS_gen|_(V,Λ) = δS_BH|_(V,Λ) + δS_matter = 0 (Eq. 4.18),
  "deduced ... from the conjecture (4.13) together with the quantum corrected first law of causal diamonds (4.6), which
  itself was derived from the semiclassical gravitational equations of motion. In this sense the semiclassical
  Einstein equation is equivalent to the quantum corrected first law for small, and therefore maximally symmetric
  diamonds." Sec. 4.3 then aligns the two ways of varying (Eqs. 4.19 to 4.24), with the cosmological constant again
  "one overall spacetime constant Λ".
- **The fixed volume can be traded for a free energy**: F = H_ζ − T S_BH (Eq. 4.25) is stationary at fixed temperature;
  "the Einstein equation is implied by stationarity of the free energy at fixed cosmological constant, without fixing
  the volume" (Sec. 6). Whether the free energy is a maximum or a minimum is "left for future work" (Sec. 4.4); footnote
  29 expects a maximum, because the temperature is negative.
- **Why a conformal Killing vector suffices** (Sec. 6): it is "an 'instantaneous' Killing vector at the maximal volume
  slice", "behaves at the edge as a boost-like Killing vector, with a well-defined surface gravity", and "in a maximally
  symmetric diamond the vacuum of a conformal matter field restricted to the diamond is thermal with respect to the
  Hamiltonian that generates the conformal Killing flow." Open question (i): non-spherical regions and
  non-maximally-symmetric spacetimes, where "the conformal Killing Hamiltonian variation may have no particular
  geometric significance"; and "the thermodynamics might be a property of the ball rather than the full diamond."

## 4. [BMSV17] and [CR16]: what sharpens it and what survives (published)

**[BMSV17], higher curvature.** The entanglement entropy is UV divergent, S_EE = c₀ A/ε^(d−2) + {subleading divergences}
+ S_finite (Eq. 1); the subleading divergences "take the form of a Wald entropy evaluated on the entangling surface"
(Abstract). Their hypothesis replaces fixed volume by a fixed "generalized volume" W′ (Eqs. 5, 6): "the entanglement
entropy of a spherical region with fixed generalized volume W′ is maximal in vacuum" (Sec. I.A). With a conformal
modular Hamiltonian H_mod = (2π/κ) H^m_ζ (Eq. 52) and the first law of entanglement δS_EE = δ⟨H_mod⟩ (Eq. 53), "Note
that this equation holds for a fixed geometry and entangling surface", the main result is (κ/2π) δS_EE|_(W′) = ∫_Σ δC_ζ
(Eq. 55), "valid for minimally coupled, conformally invariant matter fields": equilibrium is equivalent to the
**linearized** constraint equations. Three limits they state:

- "the fully nonlinear higher curvature equations cannot be derived from the linearized equations applied to small
  balls, in contrast to the situation encountered in Einstein gravity" (Abstract), which makes "general relativity
  unique in that regard" (Sec. I.A).
- Gluing the small balls into one solution is a subtlety: "errors in the linearized approximation could accumulate as
  one moves from point to point" (Sec. V, footnote 10).
- Open (Sec. V.D, "Future work"): maximal rather than merely extremal entanglement would need second order and "will
  likely invoke the positivity of relative entropy"; coherent states remain "a puzzle", their effect on the energy
  density appearing "only ... at second order"; for non-conformal matter the local cosmological constant is "one
  possible solution" and "some other resolution" may exist; gauge fields bring edge modes and gravitons are "even more
  problematic"; and non-spherical regions "present a challenge because there is no longer a simple relation between the
  modular Hamiltonian and the matter stress tensor".
- They also say what the principle is about: "It hinges on the assumption that divergences in the entanglement entropy
  are cut off at short distances, so it is ultimately a statement about the UV complete quantum gravity theory. ... if
  true, maximal vacuum entanglement provides a low energy constraint on any putative UV completion" (Sec. V).

**[CR16]'s verdict, from the record's note** (section 2.5 of
`docs/reading/notes/2026-11-02_carroll_compactification_and_entropic.md`). The holographic route ("HG", which is
[Jac16]'s) survives: "the vacuum-subtracted von Neumann entanglement entropy (the Casini entropy), evaluated on the null
surfaces of the causal diamond, provides an appropriate formulation" (their Sec. 4), on four postulates: separability
(S = S_UV + S_IR), equilibrium at fixed volume, the area-entropy relation δS_UV = η δA|_V, "the crucial substantive
assumption underlying holographic gravity", and the CFT form of the modular energy, which "need not be separately
postulated, but can be justified by examining the null limit". The thermodynamic route of [Jac95] does not survive
(no self-consistent entropy). And one limit on HG: "the HG approach does not allow gravity to truly emerge as an
equation of state, since the area and entropy variations are not dynamical changes within a single background
spacetime".

**In one paragraph, what a reader of the programme should take from sections 1 to 4** (a summary of the published
statements, not a new claim): given (a) a finite, universal entanglement entropy per area η from the ultraviolet,
(b) a modular Hamiltonian that is the local boost (conformal Killing) generator, exact for conformal fields and
conjectured with a scalar correction δX otherwise, and (c) extremal entanglement at fixed volume in every small ball in
every frame, the linearized-in-the-ball Einstein equation follows at every point, with G = 1/4ħη and Λ an integration
constant. It is a first-order, extremality statement; the full nonlinear equation follows only for Einstein gravity
and only via the small-ball limit; coherent states show that not all energy registers as entanglement.

---

## 5. What it becomes on the quantum toy (ours, unverified)

*Everything in this section is the agent's proposal for the brief's "Jacobson's reader". It is not adopted; the quantum
toy itself waits on the owner's decisions under S1 (`quantum_toy_brief.md`, section 7). Facts about lattice entanglement
marked "general knowledge" were not read by us and are to verify before they are cited.*

### 5.1 The objects, translated

| [Jac16] | On the quantum toy (H = H₀ + H₁ of the brief, section 2) |
|---|---|
| A small geodesic ball Σ of radius ℓ about o | A ball of radius r in graph distance about a point o, **taken in the background wiring** (the flat torus the ground state is mostly in). On the four-link flat sheet (a square lattice) it holds 2r² + 2r + 1 points and is cut by 8r + 4 links (ours, arithmetic; r = 1: 5 points, 12 links). |
| Fixed volume | A fixed number of points V. The simplest version fixes the **labeled point set** B itself; then V is fixed in every branch of the superposition, and the subsystem is a fixed tensor factor. Re-centering a geodesic ball of V points in each perturbed wiring (closer to [Jac16]) makes the subsystem depend on the branch, so it is not a tensor factor; it can be used only on single classical wirings (5.3, step A). |
| Area A of ∂Σ | The operator Â = number of links joining B to its complement, diagonal in the wiring basis; the area of a state is ⟨Â⟩. (Whether "area" should count cut links, or links with one end in B, or squares crossing ∂B is a choice; fix one before any run.) |
| The vacuum, maximally symmetric | The ground state of H at given (λ, Γ) on a flat torus. At Γ = 0 it is a single wiring, a product state: S_B = 0, K undefined, and the check is empty. **So the reader needs Γ > 0 by construction.** |
| δS_tot = η δA + δS_IR | There is only one entropy on the lattice, the von Neumann entropy S_B = −Tr ρ_B ln ρ_B of the ball's reduced state. The split into a geometric part and a state part has to be **tested, not assumed** (5.2). |
| The modular Hamiltonian K | K_B = −ln ρ_B of the ground state, which is exact but not local, and not known in closed form on a lattice. Three standard stand-ins (general knowledge, to verify): (i) the **Bisognano-Wichmann form** for a half space, K ≈ 2π Σ_x x_⊥ h_x / v, the local energy density weighted by distance from the cut, which lattice studies find accurate near a Lorentz-invariant critical point (Giudici, Mendes-Santos, Calabrese, Dalmonte 2018; Dalmonte, Vermersch, Zoller 2018); (ii) the **CFT ball form** of [Jac16] Eq. 17, weight (ℓ² − r²)/2ℓ; (iii) an **entanglement Hamiltonian fitted numerically**, K ≈ Σ_j β_j h_j over local terms, either by entanglement Hamiltonian tomography (Kokail et al. 2021) or by matching ρ_B directly on small systems. For free fields it is exactly quadratic and follows from correlation matrices (Peschel 2003), which does not apply to the toy, an interacting constrained model. |
| T_00, matter | The toy has no separate matter field. A knot or a curled ring is **both geometry and energy**: its H₀ energy is the action of the wiring itself. What plays T_00 has to be decided (5.4, item 3). |
| A first-order variation of state and geometry | A one-parameter family H(ε) = H + ε V_x, with V_x a local term that favors a defect at x (for example lowering the curling cost or the knot's energy at x, λ → λ − ε in a patch), and derivatives d/dε at ε = 0 by finite differences. Inserting a whole knot is a finite variation, outside [Jac16]'s first-order statement. |

### 5.2 What would count as "Einstein-like" (to be pre-registered with the owner's prediction)

Three readings, cheapest first, each with its failure stated in advance:

1. **The first law with a local modular Hamiltonian.** δS_B = δ⟨K_B⟩ holds identically to first order when K_B is the
   exact −ln ρ_B of the unperturbed ground state (general knowledge: it is the first-order expansion of the relative
   entropy). So the identity is not a test. The test is whether a **local** stand-in reproduces it:
   |δS_B − δ⟨K_loc⟩| / |δS_B| below a tolerance written in advance (for example 10 %), with K_loc of form (i), (ii) or a
   one-parameter fit β Σ w(x) h_x, across several perturbations V_x and radii r. Failing this means the toy's ball is not
   "thermal with respect to a local boost generator", which is the ingredient [JV19] Sec. 6 names as what makes the
   conformal Killing vector suffice.
2. **One area coefficient.** Write ΔS_B = η Δ⟨Â⟩|_V + Δ⟨K⁰_B⟩, where K⁰_B is the background modular Hamiltonian (the
   state-at-fixed-geometry part, by the first law) and Δ⟨Â⟩ the change in cut links at fixed V. "Einstein-like" means
   **one η, positive, fits every perturbation and every r**, with residuals below the pre-registered tolerance; η may then
   be quoted as the toy's G = 1/4η in its own units. Different η for a ring and a knot, or an η that drifts with r
   beyond its error, fails.
3. **Equilibrium (the MVEH itself).** At fixed V, the ground state's S_B is extremal under every local perturbation
   (dS_B/dε = 0 to tolerance) and maximal under finite ones (ΔS_B ≤ 0). [Jac16] needs only the first; [BMSV17] notes
   that maximality is a second-order statement tied to relative entropy. A perturbation that raises S_B at fixed V,
   to first order, falsifies the hypothesis on the toy.

Two structural limits are known before anything runs:

- **No boosts, so only the 00-component.** [Jac16] gets the tensor equation by requiring Eq. 23 "with all timelike unit
  vectors", and its K is a boost generator ([Jac16] Sec. IV, Refs. 29, 30). The quantum toy has a Hamiltonian and so a
  time, but a preferred frame (the lattice's) and no Lorentz symmetry unless one emerges at long distance. At best the
  check gives the scalar statement "area deficit at fixed volume tracks enclosed energy" in that frame, Eq. 8's
  00-component, not Eq. 26. Whether a light cone emerges in this class of models is what [HMPS09] is listed in the brief
  to read for.
- **The scale window does not exist at small sizes.** [Jac16] needs the ball much larger than the ultraviolet scale and
  much smaller than the curvature length and the system. On the toy the ultraviolet scale is one link, so r of 3 or more
  and a torus several times wider than the ball, N of order (4 × 2r)² ≈ 600 at r = 3 (ours, rough). Every size that can
  be done exactly (5.3) has r = 1 or 2: a calibration of the reader, not a test of [Jac16].

### 5.3 Feasibility, size by size

- **The class space at N = 16 and 18 (step 1 of the brief): not feasible.** A ball is a set of labeled points and a
  reduced state needs a tensor factor; with interchangeable points the Hilbert space is spanned by isomorphism classes,
  which have no subsystems. Two further facts from the record make it moot even with labels. At N = 16 no flat wiring
  exists: the five classes have S = 20 to 24 against N = 16 (`results/ergodicity_small.csv`), and at λ = 1 all five classes
  tie at H = 0, while for λ > 1 the lowest are classes 3 and 4 (S = 20, X = 16), neither a sheet. At N = 18 three classes have S = 18 and X = 0, so H₀ = 0 (classes 0, 1, 25), but a flat torus
  needs both sides at least 6 (ASSUMPTIONS Q5), so these are not 6 × 6 sheets and are at most a few links across: a
  ball of r = 1 already holds 5 of 18 points and r = 2 essentially all. There is no small ball. **What replaces it at
  these sizes:** only the ground state's weights against the Boltzmann weights, which is what the brief's step 1
  already does, and Carroll's mutual-information reader does not need labels either if it is read off a labeled
  representative, which is a separate choice.
- **A labeled flat torus, N = 36 (6 × 6) to 64 (8 × 8), perturbatively or in a truncated basis: feasible for r = 1, 2.**
  Fix one labeled flat torus. Factorize the Hilbert space as **one qubit per possible link** (a point of one side to a
  point of the other: (N/2)² qubits, 324 at N = 36), restricted to valid wirings; ρ_B is then the reduced state on the
  links that touch B. Constrained Hilbert spaces have the edge-mode ambiguity of lattice gauge theory (general
  knowledge, to verify: Casini, Huerta and Rosabal 2014; Donnelly 2012): which links count as "inside" changes S_B by a
  boundary term, which is an area term itself, so the choice must be fixed in advance and η is defined only relative to
  it. The ground state lives on wirings near the torus; every switch out of a flat sheet costs at least 32 (the record's
  four-link wall), so the support within k switches is of order 10³ to 10⁴ wirings at k = 1 and 10⁶ to 10⁷ at k = 2 at
  N = 36 (ours, rough count of edge pairs). Sparse exact diagonalization of the truncated H, then ρ_B from the sparse
  amplitudes (its rank is at most the number of distinct inside configurations), is a laptop job for k ≤ 2.
  The catch: for Γ ≪ 32 the state is nearly a product, the entanglement is of order Γ² ln Γ, and K_B has huge
  eigenvalues; [Jac16]'s regime is the opposite, entanglement dominated by many short-distance modes. Γ comparable to
  the wall needs larger k, and convergence in k must be shown.
- **Quantum Monte Carlo (the stoquastic route of the brief, step 3).** Reaches hundreds of points, but path-integral
  Monte Carlo gives Rényi entropies (S₂, by the replica or "swap" method, general knowledge, to verify), not the von
  Neumann entropy. The first law δS = δ⟨K⟩ is a von Neumann statement; the Rényi entropies do not obey it in general.
  So Monte Carlo can test reading 2 (an area law for S₂ and its response to a defect) but not readings 1 or 3.
- **Tensor networks.** Two-dimensional tensor networks on a Hilbert space of wirings, where the "lattice" is itself the
  dynamical variable, are not an off-the-shelf method; a fixed-background encoding (link qubits on the possible links)
  is all-to-all between the two sides and is not a local tensor network. Not feasible without design work.

### 5.4 Order of work, cheapest first (each step pre-registered; nothing here is decided)

- **Step A, classical, no Γ, today's toy: the geometric identity.** [Jac16] Eq. 5 is pure geometry. Its lattice analog
  can be checked on saved wirings now: for flat, knot and curled-ring wirings, take the V points nearest a center (ties
  broken by a fixed rule) and count cut links, Δ(cut)|_V, against the enclosed curvature (squares against 2 per edge, or
  the Ollivier curvature) and the enclosed H₀ energy, across V and positions. A relation of [Jac16]'s form,
  Δ(cut)|_V ∝ −(enclosed curvature), with the coefficient's dependence on V set beside the continuum Ω₁ ℓ³/(2(d²−1)) at
  d = 3, is the prerequisite: if the toy's geometry does not have Eq. 5, Jacobson's reader has nothing to read.
  *A red flag to check here first:* H₀ = 16(N − S) + 4λX charges both a deficit of squares (negative curvature, area
  excess) and a surplus beyond 2 per edge (positive curvature, area deficit), and has its floor at zero (CLAUDE.md,
  "zero is the floor"). In [Jac16], positive energy goes with an area deficit only (Eq. 8). If defects of both curvature
  signs carry positive H₀, then "H₀ energy" cannot be T_00 with one sign of η, and reading 2 fails before it is run
  unless something other than H₀ plays matter.
- **Step B, quantum, r = 1 and 2, N = 36 and 64, truncated basis:** readings 1 to 3 as a calibration, labeled as such.
- **Step C, Monte Carlo, larger r:** reading 2 for S₂ only.
- **Before any of it is written up:** a rule-15 note. We have **not** searched for published lattice tests of
  entanglement equilibrium or of the first law of entanglement with a local modular Hamiltonian on graph-valued
  Hilbert spaces; the nearest named relatives here are the lattice Bisognano-Wichmann studies above and the brief's
  quantum-graphity papers [KMS06], [KMSev08], [HMPS09], none read for this question.

### 5.5 Questions this raises for the owner (for the brief's section 7)

1. In the quantum toy, what is "matter": the knots (which are also geometry), a separate field on the points, or
   nothing (pure geometry, in which case the check is [Jac16]'s with T_00 = 0 and only the extremality survives)?
2. Is a 00-only, preferred-frame version of the check worth running, given that [Jac16]'s tensor equation needs
   boosts the toy lacks?

---

## REFERENCES.bib entries (added 2026-11-02)

Entries added to `REFERENCES.bib` (Jac16, JV19, BMSV17) on 2026-11-02. `note` fields to record the read
status above and point to this file.

- **[Jac16]** Jacobson, T., "Entanglement Equilibrium and the Einstein Equation", Phys. Rev. Lett. 116, 201101 (2016),
  DOI 10.1103/PhysRevLett.116.201101, arXiv:1505.04753. Read in full.
- **[JV19]** Jacobson, T. and Visser, M. R., "Gravitational Thermodynamics of Causal Diamonds in (A)dS", SciPost Phys.
  7, 079 (2019), DOI 10.21468/SciPostPhys.7.6.079, arXiv:1812.01596. Read in part. (The PDF's author line gives "Manus
  Visser"; the arXiv abstract page and [BMSV17] give "Manus R. Visser".)
- **[BMSV17]** Bueno, P., Min, V. S., Speranza, A. J. and Visser, M. R., "Entanglement equilibrium for higher order
  gravity", Phys. Rev. D 95, 046003 (2017), DOI 10.1103/PhysRevD.95.046003, arXiv:1612.04374. Read in part.

Named in section 5 from general knowledge or from the papers' reference lists, **not read by us**; an entry is owed
only if one is cited, with its details checked at the source first: Casini, Galante, Myers, JHEP 03, 194 (2016),
arXiv:1601.00528 and Speranza, JHEP 04, 105 (2016), arXiv:1602.01380 (the δX checks; from [Jac16]'s list); Varadarajan,
Gen. Rel. Grav. 48, 35 (2016), arXiv:1602.00106 (coherent states; from [Jac16]'s list); Bisognano and Wichmann,
J. Math. Phys. 17, 303 (1976) and Hislop and Longo, Commun. Math. Phys. 84, 71 (1982) (from [Jac16]'s list); and,
from general knowledge only, Peschel (2003), Giudici, Mendes-Santos, Calabrese and Dalmonte (2018), Dalmonte,
Vermersch and Zoller (2018), Kokail et al. (2021), Casini, Huerta and Rosabal (2014), Donnelly (2012).

Verified against the sources by a second agent on 2026-11-02 (every quotation checked was found; equation numbers and the lattice ball counts confirmed); its small corrections applied the same day.

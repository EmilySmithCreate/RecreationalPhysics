# Reading: Carroll on dynamical compactification (2009), the entropy in entropic gravity (2016), and emergence (2021, 2024)

*Date of the reading: 2026-11-02 (clock checked: 17:05 UTC). Who read: an assistant agent (Claude Fable 5.1), on the
instruction of the session that built the Carroll inventory (`docs/reading/notes/2026-11-02_carroll_inventory.md`,
entries 5, 7, 13, 19). The owner has not read these passages. Every paper was fetched as the arXiv PDF and its text
extracted with PyMuPDF; quotations are from that extraction with ligatures restored, and are to be checked against the
PDF before any of them appears in a paper or a letter. Everything marked "published" is the papers' own text or a close
paraphrase with the section or equation number; everything marked "ours" is the agent's and is unverified by a
physicist. Rule 13 applies throughout: these papers are targets the hypothesis must reproduce or answer, never evidence
that it does. American spelling; "programme" as the record writes it.*

## Read status, paper by paper

| Key (proposed; CJR09 exists) | Paper | How read |
|---|---|---|
| [CJR09] | S. M. Carroll, M. C. Johnson, L. Randall, "Dynamical compactification from de Sitter space", arXiv:0904.3115v2 (25 Sep 2009); JHEP 0911:094 (2009), DOI 10.1088/1126-6708/2009/11/094 (arXiv journal reference) | **Read in full** from the PDF: 41 pages, Secs. I to IX and Appendix A, Eqs. 1 to 117 and A1 to A22, Figs. 1 to 24 by their captions, the reference list. |
| [CR16] | S. M. Carroll, G. N. Remmen, "What is the Entropy in Entropic Gravity?", arXiv:1601.07558v3 (22 Jun 2016); Phys. Rev. D 93, 124052 (2016), DOI 10.1103/PhysRevD.93.124052 (arXiv journal reference) | **Read in full** from the PDF: 25 pages, Secs. 1 to 4, Eqs. 1 to 49, Figs. 1 to 4 by their captions, the reference list. |
| [Car21] | S. M. Carroll, "Reality as a Vector in Hilbert Space", arXiv:2103.09780v1 (17 Mar 2021); invited contribution to *Quantum Mechanics and Fundamentality*, V. Allori (ed.), per the paper's front matter; publication details to verify | **Read in part** as asked: pp. 6 to 11 (the emergence program, quantum mereology, the local factorization, the entanglement metric and its limits) closely; pp. 2 to 5 (the ontological argument) skimmed; reference list used for the sources named. |
| [Car24] | S. M. Carroll, A. Parola, "What Emergence Can Possibly Mean", arXiv:2410.15468v1 (20 Oct 2024); submitted to a volume on Real Patterns, T. Milhouse (ed.), MIT Press, per the paper's front matter | **Read in part** as asked: Introduction, Overview, Setup, the definitions of Types 0 to 3 and the subsystem-decomposition section closely (pp. 1 to 11, 14 to 19); the examples skimmed. |

Earlier record of [CJR09]: `REFERENCES.bib` says "Full text searched by an assistant agent, 2026-09-25 (notes as
[GM04])", and `docs/reading/notes/decompactification_2026-09-25.md` section (a) summarizes it in one line (compact
directions that form a sphere change together in one step). This note supersedes that read status; the one-line summary
stands and is filled out below.

---

## 1. [CJR09]: the mechanism, the accounting, the rate, the reverse process, the dimensionality

### 1.1 The setting (published)

The theory is "D-dimensional Einstein gravity (with and without a cosmological constant) coupled to a q-form field
strength" (Sec. II, Eq. 6): a positive Λ in D dimensions and a magnetic q-form flux of charge Q threading a q-sphere
(Eq. 9). "The only ingredients in the simple models we consider are a positive cosmological constant in the original
D-dimensional background space and a q-form gauge field strength" (Introduction). Assuming q-dimensional spherical
symmetry, D = p + 2 + q (Eq. 8), the theory is reduced to p + 2 dimensions with one scalar, the radion R(x), the radius
of the q-sphere at each point (Eqs. 7, 10 to 20). The radion potential in the p + 2 Einstein frame (Eq. 17, and Eq. 20
for the canonical field φ) has three terms: the sphere's curvature, negative; the D-dimensional Λ, positive; the flux
Q², positive.

What the potential looks like (Sec. II.B, Fig. 3, Eqs. 21 to 26): "For Λ = 0, the vacua are always negative,
decreasing in depth with increasing charge. For Λ > 0, the vacua are negative for small Q, but eventually reach zero
and then become positive as Q increases. For large enough Q, the minimum disappears completely." With Λ > 0 there is a
minimum φ− (a stabilized sphere) and a maximum φ+ (Eq. 25, R+ ≃ sqrt((p+q)(q−1)/2Λ)), as long as Q is below the bound
of Eq. 24. The minimum's energy is bounded above by roughly the maximum's (Eq. 26), and "this bound ensures that the
entropy associated with solutions at the positive potential minima is always greater than the entropy associated with
a D-dimensional de Sitter space with cosmological constant Λ."

### 1.2 The compactified region and the "non-singular big bang" (published)

The compactified state is a Freund-Rubin product, AdS, Minkowski or dS in p + 2 dimensions times a q-sphere of
constant radius (Sec. III.B; Sec. V). The object that does the compactifying dynamically is the "interpolating
solution" (Sec. V.A, Fig. 13): the radion starts at large φ (the D-dimensional de Sitter region), passes under the
barrier in a region where τ is spacelike, and lands in the basin of the minimum. The regions are matched across
surfaces where the scale factor a vanishes and the radion is stationary, and "from the perspective of the full
D-dimensional spacetime correspond to event horizons" (Sec. III.B). Hence: "The regions evolving in the basin of
attraction of the radion potential are p + 2-dimensional open FRW universes with a non-singular big-bang surface. This
is extremely interesting from the standpoint of cosmology, since there exists a pre-big bang epoch in which the
effective dimensionality of spacetime changes" (Sec. V.A). The finding of the interpolating solution is Coleman's
undershoot/overshoot argument: "there will always be a critical point at which the traversal time of φ matches the
period of the scale factor. This is essentially Coleman's undershoot/overshoot argument for finding instantons in a
scalar field potential [25]" (Sec. V.A). The limit of zero charge is "nothing other than empty D-dimensional de Sitter
space" (Sec. V.A), so the flux is what makes the compactified region exist at all.

### 1.3 The energy accounting (published, with what is absent said plainly)

There is no latent heat in this paper and no bookkeeping of "energy released". What there is:

- The p + 2 vacuum energy after compactification is V(φ−), which is negative, zero or positive depending on Q
  (Sec. II.B); it is "determined by a cancellation between the curvature, flux, and higher-dimensional cosmological
  constant contributions to the radion potential Eq. 20" (Sec. VII). For small Q it is deep and negative (Eq. 23); near
  Qmax it is small and positive.
- What happens to the radion's energy after the transition: if V(φ−) < 0, "Evolution away from the stationary point of
  the interpolating solution always results in a singularity as the non-zero kinetic energy of the field blue-shifts in
  the negative vacuum energy background" (a big crunch, Sec. V.A); if V(φ−) > 0, "the field will simply experience
  damped oscillation around the positive minimum while the scale factor grows monotonically. The solution in this case
  is completely non-singular" (Sec. V.A). So the radion's surplus is damped away by expansion, not converted into
  matter: the paper has no matter sector.
- Inflation and anything like reheating need an added field: "both of which require the addition of a scalar field ψ
  into the D-dimensional theory" (Sec. VIII), coupled to the D-dimensional curvature and flux so that its mass squared
  turns negative in the compactified region (Eqs. 107 to 113). The compactification "triggers" slow roll by setting the
  initial conditions; the energy of inflation is ψ's potential (one worked model gives about 110 e-folds, Fig. 23).
- The role of Λ: it supplies the maximum of the potential and the de Sitter background that fluctuates; its size sets
  the size of the nucleated patch and the rate (Secs. VI.A, VI.B). The role of the flux: it stabilizes the sphere and
  indexes the landscape ("one vacuum per value of the charge Q", Sec. VII).
- The cosmological constant problem is addressed as Bousso and Polchinski do: many fluxes with incommensurate charges
  and many compact dimensions make the lower-dimensional vacuum energy scan finely (Sec. VII, Eqs. 101 to 106).

### 1.4 The nucleation rate and what it depends on (published)

The rate per unit D-volume is Γ = A exp[−(S_inst − S_dS^(D))] (Eq. 73), with A "of order Λ^(D/2)" and S_dS^(D) the
Euclidean action of the D-dimensional de Sitter space (Eq. 74), negative and large unless Λ is of order M_D². With
α ≡ S_inst / S_dS^(D) (Eq. 79), Γ = A exp[S_dS^(D)(1 − α)] (Eq. 80), always suppressed since α < 1 for every solution
they build. Two instantons mediate the transition (Sec. VI, Fig. 15): the Euclideanized compactification solution,
"very similar to that of the Hawking-Moss instanton", in which "a roughly horizon-sized patch of the D-dimensional de
Sitter space fluctuates into a solution very close to the Lorentzian compactification solution at the maximum of the
radion potential" and then falls either way; and the Euclideanized interpolating solution, "similar to the Coleman-de
Luccia instanton", which "when it exists, will always have a single negative mode" and "always makes the dominant
contribution to the decay rate" (Figs. 17, 18). The summary of Sec. VI.A:

- "The value of α at a fixed normalized charge Q/Qmax is maximized for a particular p or range of p depending on the
  total dimensionality."
- "For fixed p and q, the rate is highest for small Q, and therefore the lowest (negative) energy vacua."
- "When it exists, the rate is higher at fixed Q, p, and q for the interpolating solution than the compactification
  solution."
- "Because the instanton action is finite as the vacuum energy of the minimum goes to zero, the rate into a p + 2-
  dimensional vacuum with a small (positive) vacuum energy is much higher than the rate out. p + 2-dimensional
  Minkowski vacua are completely stable."

The nucleated patch is about one horizon volume of the parent: "a nucleation event corresponds to taking roughly one
horizon volume of the background dS space and replacing it with the post-nucleation spacetime" (Sec. VI.B).

### 1.5 The reverse process (published)

"In addition to dynamical compactification, the inverse process can also occur, whereby a p + 2 dimensional vacuum can
undergo a 'decompactification transition' to a region that empties out into D-dimensions [2, 29]. This is mediated by
the same instantons responsible for dynamical compactification [2]" (Sec. VI; [2] is Giddings and Myers, the record's
[GM04]; [29] is Giddings 2003). The rate out is Eq. 85 with β ≡ S_inst / S_dS^(p+2) (Eq. 87, Fig. 20): "As V(φ−) → 0,
S_dS^(p+2) → −∞. Because the instanton action approaches a constant in this limit, β → 0, and the tunneling rate out of
the p + 2-dimensional dS space is extremely suppressed ... In the limit of a vanishing p + 2-dimensional cosmological
constant, the vacuum is completely stable." Globally: "If the lower-dimensional vacua have positive vacuum energy, they
are metastable, with local regions eventually transitioning back to the D-dimensional de Sitter space. This recycling
process continues indefinitely" (Sec. VI.B), and the steady-state weight P_j / P_dS ~ exp[|S_dS^(p+2)| − |S_dS^(D)|]
(Eq. 100) "is in accord with the qualitative expectation that a statistical system spends most of its time in the state
of highest entropy." A second step is noted: after compactifying to M × S^q1 "a second transition could produce a
product compactification M × S^q1 × S^q2" (Sec. VI.B).

### 1.6 Relation to [W82] and [BV89] (published)

[W82] (Witten's bubble of nothing) is not cited: the reference list has no Witten entry. [BV89] is reference [3],
named once: "Brandenberger and Vafa [3], who used the properties of intersecting strings to suggest that three spatial
dimensions could naturally expand while others remained compact. Karch and Randall [4] argued that a gas of branes with
various dimensionalities would relax to one dominated by three-branes. Our proposal starts from a dramatically
different initial state: empty de Sitter space in higher dimensions" (Introduction). The closest ancestor named is
Giddings and Myers [2]: "This process is the inverse of the 'spontaneous decompactification' studied by Giddings and
Myers [2], and was first suggested therein."

### 1.7 Which dimensionality is selected (published)

For the Euclidean compactification instanton at small Q, α depends on p and q only through unit-sphere volumes
(Eq. 84, Fig. 16): "Relevant for our universe is that for D = 8, the nucleation rate for Euclidean compactification
solutions with p = 2 (and therefore four non-compact dimensions) is largest. There are also marginal cases: for D = 7,
the rate for p = 1 and p = 2 are identical while for D = 9, the rate for p = 2 and p = 3 are identical." For the
interpolating instanton in D = 8 at fixed Q/Qmax, "the solutions for p = 2 always have the largest value of α" (Fig. 19),
but "to zero energy p + 2 dimensional vacua ... the p = 2 and p = 3 solutions have comparable values for α", and "In
general the comparison of nucleation rates between solutions is complicated, since there is a value of Q at each p for
which the nucleation rate is the same ... It is necessary to determine some physical criterion for making the
comparison" (Sec. VI.A). Under the comoving-volume measure "vacua with the largest possible values of α are
exponentially favored" (Eq. 94), with the caveat that "we are comparing infinities and there is no unique regulator
(notwithstanding the fact that one must compare volumes in vacua of different effective dimensionality)" (Sec. VI.B).
Two caveats they state themselves: "Finding vacua of the correct dimensionality requires that there exists a
(D − 4)-form field strength" (Sec. IX), and the dS × S^q solutions have a known instability for q ≥ 4 (Sec. IX, their
Ref. [33]).

---

## 2. [CR16]: what the paper argues, and what it does not contain

### 2.1 First, a correction to the brief (ours, from the text)

The brief asked for "the 2016 paper's argument against entropic gravity: exactly which entropy Verlinde's derivation
needs ... their worked objections (neutron interference, the equivalence principle, the temperature)". **None of those
three objections is in this paper**, and Verlinde is not its target. Verlinde is cited once, as [17], in one sentence:
"While these approaches are similar in spirit, Verlinde [17] emphasizes the existence of an entropic force from the
gradient of the entropy, while Jacobson [16] derives the Einstein equation directly as a local equation of state"
(Sec. 1). The paper then says "For definiteness, we will focus on Jacobson's version of HG in Ref. [15] and of TG in
Ref. [16]." The words "neutron", "interference", "equivalence principle" and "Unruh temperature as an objection" do not
occur as objections anywhere in the 25 pages. The neutron-interference objection to Verlinde belongs to Kobakhidze
(general knowledge: A. Kobakhidze, "Gravity is not an entropic force", Phys. Rev. D 83, 021502 (2011), arXiv:1009.5414;
to verify before citing), which the record's [Ver11] note already lists as "not read by us". That reading is still owed;
this note does not supply it.

### 2.2 The two approaches and the one they reject (published)

Two families: holographic gravity (HG), "in which Einstein's equation arises from keeping entropy stationary in
equilibrium under variations of the geometry and quantum state of a small region", and thermodynamic gravity (TG), "in
which Einstein's equation emerges as a local equation of state from constraints on the area of a dynamical lightsheet in
a fixed spacetime background" (Abstract). Verlinde, Padmanabhan, Tian and Wu, and Cai and Kim are grouped with Jacobson
1995 under TG (Sec. 1, Refs. [16] to [20]). The verdict: "For thermodynamic gravity, on the other hand, we find that it
is difficult to formulate a self-consistent definition of the entropy, which represents an obstacle for this approach"
(Abstract); "We will argue that there does not exist any self-consistent definition of entropy in this approach"
(Sec. 3).

### 2.3 Exactly which entropy TG needs (published)

TG's two postulates (Sec. 3.1): the Clausius relation δS = δQ/T (Eq. 30), with δQ the heat flux through a small
lightsheet segment H (Eq. 28) and T the Unruh temperature ħκ/2π of the associated Rindler trajectory; and local
holography, δS = η δA (Eq. 31) for a universal η, expected to be 1/4Għ. With the Raychaudhuri equation these give
Einstein's equation (Eqs. 32 to 35). The key sentence on what the entropy must be: "Formally, the only role of δS in
this derivation is to motivate equating η δA with δQ/T; once that happens, δS disappears from the discussion. But if we
were simply to assume η δA = δQ/T from the start, that would be tantamount to assuming Einstein's equation. The
substantive content of TG, therefore, rests on the existence of a consistent and well-defined local construction for
the entropy δS associated with lightsheet segments anywhere in spacetime" (Sec. 3.1, p. 16).

### 2.4 Why the ordinary candidates do not do the job (published, in their order)

1. **Von Neumann entropy on a spacelike region fails by extensivity.** "while the von Neumann entropy is subextensive,
   energy-momentum is extensive ... the masses of A and B, and hence the concomitant first-order area decrements of a
   lightsheet passing through them, add linearly. Thus, the use of the von Neumann entropy on spacelike surfaces cannot
   provide a consistent formulation of thermodynamic gravity" (Sec. 3.2).
2. **The UV-regulated von Neumann entropy in the null limit fails in vacuum.** It "is still large [29, 30], going as
   A/ε²", while "δA ... must vanish in the Minkowski vacuum"; "no such effect could reconcile a finite value of δS with
   an exactly vanishing δA" (Sec. 3.2). So the entropy must be Casini's vacuum-subtracted one (Eq. 21).
3. **The null Casini entropy of the segment gives the wrong Newton's constant.** By Bousso, Casini, Fisher and
   Maldacena (their [21, 22]), ΔS_H = ΔK_H = (2π/ħ) ∫dA ∫₀^ε dλ g(λ, ε) T_μν k^μ k^ν (Eq. 37), where the weight g rises as
   λ at one end and falls as ε − λ at the other (Fig. 4), so that ∫₀¹ ḡ dλ̄ < 1/4. Matching to the area decrement
   (Eq. 40) forces G_S = G_N / (2 ∫ḡ) ≥ 2 G_N (Eq. 43), that is η ≤ 1/8G_Nħ (Eq. 44): "This is inconsistent, by an
   order-unity factor, with the area-entropy coefficient from black hole thermodynamics, which would be η = 1/4G_Nħ."
   The cause: "a crucial factor-of-g difference" between the Rindler form, right for a semi-infinite lightsheet, and
   the finite segment TG must use so that the expansion and shear stay subdominant (Sec. 3.2, p. 20).
4. **Hidden quantum-gravity degrees of freedom cannot repair it.** "attaining η = 1/4Għ would require |dḡ/dλ̄| to
   exceed unity. It is shown in Ref. [22] that this is impossible on very general grounds ... exceeding this limit would
   violate strong subadditivity of von Neumann entropy or monotonicity of quantum relative entropy" (Sec. 3.3).
5. **A difference of Casini entropies of two overlapping semi-infinite lightsheets** comes out "second-order rather
   than linear in the curvature and therefore in the area decrement δA" (Eq. 49), so it "is fundamentally incompatible
   with the local holographic postulate (31)" (Sec. 3.3).

"Hence, neither the null-limit Casini entropy of a small null region nor the difference in null-limit Casini entropies
of two large null regions provides an acceptable definition of entropy in the thermodynamic formulation of entropic
gravity" (Sec. 3.3).

### 2.5 What a successful entropic account would have to supply (published)

For TG: an entropy "for a system that can be locally defined" (Sec. 3.1), vanishing in vacuum, linear in T_μν, with the
Bekenstein-Hawking coefficient; or else "a justification, independent of Einstein's equation, of why the local
holography postulate must take precisely this modified form" with the coefficient of Eq. 43 (Sec. 3.2, p. 20). For HG,
which they say works: four postulates (Sec. 2.2): entanglement separability (S_B = S_UV + S_IR); an equilibrium
condition (δS_B = 0 under joint variation of state and metric at fixed volume, in a maximally symmetric diamond); the
area-entropy relation δS_UV = η δA|_V, "the crucial substantive assumption underlying holographic gravity"; and the CFT
form of the modular energy, which they show "need not be separately postulated, but can be justified by examining the
null limit" (Sec. 2.3). Their answer to their own title: "In what we have called 'holographic gravity,' the
vacuum-subtracted von Neumann entanglement entropy (the Casini entropy), evaluated on the null surfaces of the causal
diamond, provides an appropriate formulation" (Sec. 4). And a limit they state on HG: "the HG approach does not allow
gravity to truly emerge as an equation of state, since the area and entropy variations are not dynamical changes within
a single background spacetime" (Sec. 3).

---

## 3. [Car21] and [Car24]: his criteria for "emergent" and for locality

### 3.1 [Car21] (published)

- **What emergence is for.** "The search for emergent levels is precisely the search for higher-level, non-fundamental
  descriptions that approximately capture some of the relevant dynamics, perhaps on the basis of incomplete information
  about the fundamental state" (p. 6). "Emergent structures that accurately describe the dynamics of part of a system
  using only information accessible within the emergent description itself have every right to be thought of as
  'real,' even if they are not 'fundamental' (Dennett, 1991; Wallace, 2012)" (p. 7).
- **Two marks of a natural description.** "The first is that the internal dynamics of the system are more easily
  interpreted in the N-particle language ... The second is that the system looks like N particles" (pp. 6 to 7), and
  "The ontology that seems most natural for us to ascribe to a physical subsystem thus depends on how that subsystem
  interacts with the rest of the world" (p. 7).
- **Quantum mereology.** Factorize H = H_S ⊗ H_E (Eq. 6); the right factorization is the one in which "localized wave
  packets in H_S ... stay relatively localized and follow classical equations of motion under Ĥ_S, but also for
  unentangled states in H_S ⊗ H_E to remain relatively unentangled" (p. 8); operationally, "The correct factorization is
  the one that minimizes both" the rate of delocalization and of entanglement growth (p. 8). Generic Hamiltonians have
  neither property in any factorization.
- **Locality in a Hilbert-space factorization.** With H = ⊗_α H_α (Eq. 9) and Ĥ expanded in self terms, two-point,
  three-point terms and so on (Eq. 10): "A necessary requirement for the emergence of a structure recognizable as
  'space,' with local dynamics therein, is that the series (10) does not continue indefinitely when the factorization
  (9) corresponds to local regions ... Happily, this requirement is also essentially sufficient. As shown by Cotler et
  al. (2019), generic Hamiltonians admit no local factorization at all, and when such a factorization exists, it is
  unique up to irrelevant internal transformations" (p. 9).
- **Distance and metric from entanglement.** Mutual information I(α:β) = S_α + S_β − S_αβ (Eq. 11) falls with
  distance in the vacuum, so one defines "a distance metric depending inversely on the mutual information", recovers a
  best-fit geometry by multidimensional scaling (Cao, Carroll, Michalakis 2017), and, "under certain optimistic
  assumptions (most notably, the eventual emergence of approximate Lorentz invariance)", Einstein's equation in the
  weak-field limit from δA ∝ δS (Eqs. 12, 13; Cao and Carroll 2018). The limits he states: "we haven't shown that it is
  the emergent metric, the one whose geodesics define the motion of localized test particles" (p. 10 to 11); "What
  strictly emerges from entanglement in this story is the metric on space, not on spacetime"; "we need to imagine that
  time itself is fundamental, rather than emergent" (p. 11); Lorentz invariance can only be approximate in a
  finite-dimensional factor; the Lieb-Robinson bound is named as the route to light cones.

### 3.2 [Car24] (published)

- **The setup.** A theory is "a specified space of states and some (possibly probabilistic) evolution rule" (Overview,
  item 1); evolution is Markovian; the emergence relation Φ: A → B is time-independent ("Otherwise emergence would be
  trivial"), may be a relation rather than a map, and may have a restricted domain of applicability (Setup).
- **The criterion.** "Type-0 (featureless) emergence: A map Φ (within a specified domain of applicability) from
  states a ∈ A in a micro theory α to states b ∈ B in a macro theory β, such that Φ commutes with the corresponding
  time-evolution operators E_α and E_β" (the commuting diagram of Fig. 2). "The defining feature of emergence is the
  existence of an effective macroscopic theory, where 'effective' means that the dynamics of the macrostates can be
  described (at least to a good approximation) in terms of those macrostates alone, without reference to the
  lower-level micro-theory."
- **Subsystems and locality.** A decomposition is a Cartesian product (Eq. 3) that counts as "appropriate" when "(1)
  we can imagine turning off the interactions with other subsystems, either by 'moving them far away' or by setting
  some coupling constants to zero, and (2) when those interactions are turned off, the data in the subsystem state
  a_i(t) is sufficient to determine the evolution of that subsystem." Locality: "A decomposition into subsystems allows
  us to think of the space of states as a network, with subsystems as nodes and interactions between subsystems
  represented by weighted edges ... This hierarchy of dynamical relevance can be thought of as a notion of locality."
- **The types.** Type-1 (local): Type-0 plus "subsystems in the macro theory consist of localized collections of
  subsystems in the micro theory", split into 1a (compressible map) and 1b (incompressible map, in Kolmogorov's sense);
  Type-2 (nonlocal): macro entities "defined globally, in terms of many dispersed parts" or interacting nonlocally,
  with Eq. 7's filter function; Type-3 (augmented): "new variables that are independent of micro states, but which
  become dynamically relevant only in certain macroscopic situations" (Eq. 8), their version of strong emergence.
  Types 0 to 2 are weak emergence; "The existence of an emergent description implies that it is possible to
  coarse-grain states of the micro theory and throw away an enormous amount of information about the microstate, and
  nevertheless retain somewhat accurate predictive power at the macro level."

---

## 4. Against the record (ours, unverified; each line says what kind of statement it rests on)

### 4.1 (a) [CJR09]'s compactification against the toy's ladder and the owner's direction

**Is his bubble the toy's fold run forward?** In shape, partly; in sign, no, at the λ the hypothesis uses.

- *The shape.* His transition is a seed (a horizon-sized patch, Sec. VI.B) that converts a region, with an event
  horizon as the non-singular edge of the new cosmology, and the same instantons run it both ways (Sec. VI). The toy's
  tube opening (T7, two directions) is a seed and a front with an exact release; the toy's fold tests (T34, O69; T57,
  O114) asked for the reverse, a region of flat six-link space curling one direction under concentrated energy, and
  found none: "582 read MELTED, 58 HEALED and none FOLDED" (O114). So the toy has the forward (uncurling) process
  measured and the backward (curling) process not seen. His paper has the backward process (compactifying) as the
  instanton with the larger rate and the forward one (decompactifying) suppressed or stable (Sec. VI.A, last bullet).
- *The sign of the energy, which is the whole difference.* In his model the compactified vacuum is favored: for small Q
  its energy is negative (Eq. 23), and for small positive V(φ−) it holds vastly more entropy than the parent (Eq. 100),
  so "a statistical system spends most of its time" compactified. In the toy at λ > 1 the curled state sits 4(λ − 1)
  per point per curled direction *above* flat space (exact, O41: "flat is 0, one curled 4(λ − 1), two 8(λ − 1), and
  all three (the 6-cube) 12(λ − 1)"), and the owner's decision is that X is curled and the change uncurls (VISION
  Update 13). So the toy's accounting at λ > 1 is the opposite of his: his lower state is the curled one, the toy's is
  the open one. **The two agree only below λ = 1**, the "rehearsal" of Update 8 where folding pays, or within about 2 %
  of λ = 1 with interchangeable points, where the counting drive beats the curling cost (O55, O72; "λ about 1.02", VISION
  Update 41). On that reading the five fold tests' finding nothing curled is consistent with his accounting rather than
  against it: at λ = 1.10 and 1.25 nothing in the toy's energy favors the curled state, so there was nothing for a fold
  to run on. (Update 149 (v) adds that none of those tests had loops to stack, so they do not bear on her newer
  reading either.)
- *What holds the curled direction shut.* His: a flux Q threading the sphere, without which "The spacetime ... is
  nothing other than empty D-dimensional de Sitter space" (Sec. V.A). The toy's: the hard-core rule's wall, 96 − 64λ
  on the long two-curled torus and 96 − 48λ on the one-curled rung (O49), 20, 40, 80 at eight links and λ = 1.25 (O50),
  a fixed number of units offered a fixed number of times a sweep. There is no counterpart of the flux in the toy, and
  no counterpart of the wall in his continuum model, where the barrier is the radion potential's maximum.
- *Several directions at once against one at a time.* His compact directions form a sphere by construction and change
  together; the toy's ladder is additive with one wall per rung and nothing tying the directions (O41, O50; the
  decompactification note's section (a) already says this). His Sec. VI.B names the staged product compactification
  M × S^q1 × S^q2 as a possibility and does not compute it, which is the one place his paper and the toy's "one at a
  time" meet.
- *The rate.* His is a semiclassical tunneling rate whose exponent is a fraction (1 − α) of the parent's de Sitter
  action, enormous unless Λ is near M_D² (Eq. 80); it falls with Q, rises with smaller Λ at fixed dimension (Abstract),
  and depends on p and q through sphere volumes (Eq. 84). The toy's is a thermal activation over a single-move wall,
  exp(−wall/g), with the wall fixed with size (T32 FIXED WALL; O54). The nearest object in the toy to his instanton is
  T54's critical patch, a barrier quadratic in the patch size whose top is the "smallest patch that grows by itself":
  that is the undershoot/overshoot structure of his Sec. V.A, in the toy's discrete form. No number from his paper
  transfers to the toy (rule 13): the two rates are functions of different things.
- *Energy released.* He has none in the toy's sense: the radion's surplus is damped by expansion (V(φ−) > 0) or
  crunches (V(φ−) < 0), and inflation is paid by an added field ψ. The owner's burp, "a bounded lump of energy (Δρ)
  that became matter and radiation" (claim 4), has no counterpart here; what his model offers claim 4 is the
  non-singular big bang at a horizon and the "pre-big bang epoch in which the effective dimensionality of spacetime
  changes" (Sec. V.A), which is the dimensional change of claim 4 stated in continuum language with the opposite
  direction.

**Benchmarks hers must meet, read off his paper (rule 13):** (i) a rate for the change with its dependence on the
energies of the two states and on the number of directions stated, as Eqs. 80 and 84 state his; (ii) the reverse
process priced and its suppression explained, as his Eq. 85 does (the toy has the two walls, O41 and O50, and flat
space's gap, 32, 64, 128, exact); (iii) a statement of which dimensionality is favored and by what criterion, with the
ties and the "physical criterion" still owed named as he names them; (iv) the measure problem carried openly, as his
Sec. VI.B carries it ("we are comparing infinities and there is no unique regulator"), which is what O101 and VISION
Update 43 already do; (v) the stability of the curled product against the known instability for q ≥ 4, which has no
toy counterpart and is a question for the continuum version only.

### 4.2 (b) [CR16] against the programme's entropic route

**Which of his objections the toy's finding already meets.** The toy's entropic route (O87; the carriers note of
1 November; the sandbox look `sandbox/out/pair_handles_look_2026-11-01.txt`) is Verlinde's form F = T dS/dr with S a
classical count: of wirings hidden behind a cut (O87) or of valid switches available to the surroundings of two relics
(the pair look). It is not a von Neumann entropy, so [CR16]'s objections 1 to 5 of section 2.4, which are about which
quantum field-theoretic entropy on a null segment can satisfy δS = η δA with the Bekenstein-Hawking coefficient, do
not address it: the toy's count is extensive (objection 1 does not arise), has no vacuum divergence to subtract
(objection 2 does not arise), and has no lightsheet, no Unruh temperature and no Newton's constant to get wrong
(objections 3 to 5 do not arise). The published objection that does bite the toy is Verlinde's own, already on the
record: information stored at lattice points without duplication gives no holography and no gravity ([Ver11], as the
5 October note records it).

**What the record's own argument does that his paper does not.** The route is closed in the record by measurement and
exact arithmetic, not by his argument: flat space is gapped (O22, O50, O51), the warm model's correlation length is
about two links at every coupling and size to 676 (O31), and the one-step look finds two curled relics have fewer
valid moves together than apart by 524, 132, 42, 4 at separations 2 to 5 and exactly 0 from 6 on, with the energy
exactly additive (O22): a contact-range repulsion from the hard-core rule's forbidden volume, nothing beyond. **His
paper does not close the toy's route more firmly than that; it closes a different route**, the continuum one in which
a local entropy flux through null surfaces yields Einstein's equation, and it leaves open the holographic one (HG,
Sec. 2), which the toy cannot use at all: HG needs a factorized Hilbert space, an entanglement entropy and an area,
and the toy is classical with no Hilbert space.

**What his paper adds that the record should keep.** One sentence (Sec. 3.1, p. 16): assuming η δA = δQ/T from the
start "would be tantamount to assuming Einstein's equation." That is rule 13 in his words: if a pull of Newton's shape
is ever obtained in the toy by choosing a coefficient so that count times temperature equals a force, the shape has
been put in. The carriers note's candidate A and B (a scalar on the points; the link-length field) carry Newton's
shape by construction (the graph's Green's function), so any 1/r they give is a shape check and not a prediction, as
O166 (5) already says of the Green's function.

**What is still owed on this piece.** The objections the brief expected (neutron interference, the equivalence
principle, the temperature) are Kobakhidze's and others', listed in [Ver11]'s note as "not read by us"; they are still
unread. If the warm-bath pull is ever run, that reading comes first, not this paper's.

### 4.3 (c) His emergence criteria against rule 10's four kinds of statement

Rule 10 sorts *statements* (exact; measured; interpretation; the hypothesis's claim). [Car24] sorts *relations between
theories* (a map Φ that commutes with time evolution; whether the subsystems are local; whether the map is
compressible; whether new variables are added). The two are not rivals; the second is a test a statement of the third
kind would have to pass before it could become one of the first two. Applied to the record's sentences:

- "Spacetime is a stable phase of X" (claim 1) and "space emerges from the wiring" (the public pages). In [Car24]'s
  terms the micro theory is the graph with its energy; the macro description is the local-dimension census, the square
  count and curvature (`graphity.dimension`), an exact and compressible map (Type-1a) on every arrangement. What has
  **not** been shown is the commuting diagram: the toy has no macro evolution rule for the census to commute with,
  because the Monte Carlo chain is a sampler and its sweep is not a time (O93; the fair clock, O90). So by his
  criterion the record has an emergence *map* and no emergence *claim* yet; the record should say "a map from wiring
  to local dimension, exact" rather than "space emerges", until a macro rule exists and is checked against the chain.
  This is a fifth kind of statement rule 10 does not name: a definition of what would count, which [Car24] supplies.
- "Energy in the familiar sense exists only in the spacetime phase" (claim 3). Under [Car24] this would be Type-3
  (augmented) only if energy were a macro variable with no micro counterpart; in the toy H = 16(N − S) + 4λX is
  defined on every arrangement, so there is no augmentation and the claim as the toy holds it is Type-0 or Type-1: one
  F covers everything, which is what claim 3 says. The claim's "may merge, split, convert type, freeze" is his Type-2
  (macro entities defined from dispersed parts), and nothing in the toy has been checked for it.
- Locality. [Car21]'s criterion is that the Hamiltonian be a sum of few-body terms over a factorization *found from the
  spectrum*, not put in. The toy's H is a sum of per-edge terms (O22's theorem), so it is local in his sense, but its
  locality is in the links, which the model puts in; the toy derives nothing from a spectrum. His entanglement
  distance (Eq. 11 of [Car21]) has a classical cousin, the correlation length, which O31 measured at about two links at
  every coupling. By his own construction an emergent geometry needs the mutual information to fall with distance over
  many steps; the warm published model's falling to zero within two steps is, in his vocabulary, no emergent geometry
  beyond two links, the same fact the carriers note states.
- "Real." [Car21] and [Car24] both take Dennett's line that an emergent description that predicts on less information
  is real. The record's tube, sheet and knot are real patterns in that sense once a macro rule predicts them; today they
  are exact readings of fixed arrangements.

---

## 5. The one narrow question for a letter (ours)

To Carroll, on [CJR09], tied to the record's open question of whether curled directions open together or one at a
time (O54, O103 (i), the decompactification note): *Does the nucleation calculation of Sec. VI go through for a
toroidal fiber with independent radii in place of the q-sphere, so that the rate to compactify (or decompactify) k of
q directions could be set beside the rate for all q at once; and if the interpolating instanton does not exist for a
torus, is the staged product compactification of Sec. VI.B the only route to a partial opening in that setting?* One
question, answerable from his own framework, with the toy's exact additive ladder (O41, O50) as what prompted it. The
owner's outreach rules apply (one narrow question, disclose the AI drafting, check his recent papers first: the
inventory lists the 2026 cyclic-universe paper as the first to read).

A reserve question on [CR16], only if the warm-bath pull is ever run: whether the no-go of Sec. 3 has any bearing on a
classical configuration count of the kind Verlinde dismisses in one sentence, or whether that case is simply outside
both HG and TG.

---

## 6. REFERENCES.bib entries owed

[CJR09] exists; its note should be replaced by: "Read in full by an assistant agent from the PDF, 2026-11-02
(docs/reading/notes/2026-11-02_carroll_compactification_and_entropic.md). D-dimensional de Sitter with Λ > 0 and a
q-form flux nucleates regions in which q directions compactify on a flux-stabilized sphere, by a Hawking-Moss-like or
a Coleman-de Luccia-like instanton (Sec. VI); rate Γ = A exp[S_dS(1 − α)], highest for small Q and, at D = 8, for four
non-compact dimensions (Eq. 84, Fig. 16); the reverse (decompactification) is mediated by the same instantons and is
suppressed as the lower vacuum energy goes to zero (Eq. 85); no latent heat and no matter sector; inflation needs an
added scalar (Sec. VIII); [W82] not cited, [BV89] cited as a different starting point."

Three new entries, bibliographic details to verify against the catalogue:

```
@article{CR16,
  author  = {Carroll, Sean M. and Remmen, Grant N.},
  title   = {What is the Entropy in Entropic Gravity?},
  journal = {Physical Review D},
  volume  = {93},
  pages   = {124052},
  year    = {2016},
  eprint  = {1601.07558},
  archivePrefix = {arXiv},
  note    = {Read in full by an assistant agent from the PDF, 2026-11-02 (docs/reading/notes/2026-11-02_carroll_compactification_and_entropic.md). Holographic gravity (Jacobson 2016, entanglement equilibrium) is made consistent with the Casini entropy on a causal diamond's null boundary; thermodynamic gravity (Jacobson 1995, and by grouping Verlinde) has no self-consistent entropy: the null Casini entropy gives eta <= 1/(8 G hbar), not 1/(4 G hbar) (Eq. 44), hidden degrees of freedom cannot repair it (strong subadditivity), and a difference of lightsheet entropies is second order in curvature (Eq. 49). Contains none of the neutron-interference, equivalence-principle or temperature objections to Verlinde; those are Kobakhidze's and others', still unread.}
}

@incollection{Car21,
  author  = {Carroll, Sean M.},
  title   = {Reality as a Vector in {H}ilbert Space},
  booktitle = {Quantum Mechanics and Fundamentality: Naturalizing Quantum Theory Between Scientific Realism and Ontological Indeterminacy},
  editor  = {Allori, Valia},
  year    = {2021},
  eprint  = {2103.09780},
  archivePrefix = {arXiv},
  note    = {Read in part by an assistant agent from the PDF, 2026-11-02: pp. 6 to 11 closely (quantum mereology; locality as a Hilbert-space factorization in which the Hamiltonian is a finite sum of few-body terms, unique when it exists, Cotler et al. 2019; distance from mutual information; weak-field Einstein from dA proportional to dS under assumed emergent Lorentz invariance, with its limits stated: the metric is on space not spacetime, time is taken fundamental, and the entanglement metric is not shown to be the one test particles follow). Book publication details to verify; year is the arXiv year.}
}

@incollection{Car24,
  author  = {Carroll, Sean M. and Parola, Achyuth},
  title   = {What Emergence Can Possibly Mean},
  booktitle = {Real Patterns},
  editor  = {Milhouse, Tyler},
  publisher = {MIT Press},
  year    = {2024},
  eprint  = {2410.15468},
  archivePrefix = {arXiv},
  note    = {Read in part by an assistant agent from the PDF, 2026-11-02: the setup and the definitions of Types 0 to 3 closely, the examples skimmed. Emergence as a time-independent coarse-graining map that commutes with the micro and macro evolution rules (Fig. 2); subsystems as a Cartesian product whose factors evolve on their own data when interactions are switched off; locality as a hierarchy of dynamical relevance; Type-3 adds macro variables that do not supervene. The second author is "Achyuth Parola" on the arXiv abstract page; the PDF title page prints "Achyth", taken here as a typo. Book details to verify; year is the arXiv year.}
}
```

Verified against the sources by a second agent on 2026-11-02 (about forty quotations, equation numbers and placements; all matched but the co-author's spelling); its corrections applied the same day.

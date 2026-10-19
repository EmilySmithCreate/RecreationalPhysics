# Reading note: Gell-Mann and Hartle (2021) and Hartle (2020), mapped against the observer-relative-histories handoff

**Date:** 2026-10-12. **Written by:** an assistant agent (Claude), reading for the owner. Physics readings marked "Ours, unverified" are the agent's and have not been checked by a physicist.
**Mapped against:** `docs/theory/observer_relative_histories_research_handoff.md` (12 October 2026), read in full first.
**Read status:** both papers read **in full** (every page, including footnotes, figure caption and reference lists). The handoff lists them under "skim selective sections"; nothing was skimmed. Neither paper is in `REFERENCES.bib` yet; this note does not touch that file.

**How the texts were obtained.** The arXiv abstract pages were fetched; the PDFs were downloaded from `https://arxiv.org/pdf/<id>` and their text extracted with `pypdf` (the PDF renderer is not installed here); the LaTeX sources were downloaded from `https://arxiv.org/e-print/<id>` and used to verify every equation and quotation below. Where the LaTeX source contains text that is commented out (not in the published PDF), the note says so explicitly.

**Plain-language glossary for this note.** *Density matrix* ρ: the general description of a quantum state, including states of incomplete knowledge; a *pure* state is one with complete knowledge, ρ = |Ψ⟩⟨Ψ|. *Coarse graining*: following some variables and ignoring the rest. *History*: a sequence of coarse-grained "yes/no" alternatives at a series of times. *Projection operator* P: the mathematical object for one such yes/no question. *Decoherence*: negligible quantum interference between the alternative histories in a set, which is what lets probabilities be assigned to them. *Condition of indifference*: a final density matrix proportional to the identity, meaning nothing at all is specified about the end. *Quasiclassical realm*: the set of coarse-grained histories in which the world looks classical (Moon orbits, fission tracks, galaxies).

---

## 1. Gell-Mann and Hartle (2021)

### 1.1 Bibliographic details

Murray Gell-Mann and James B. Hartle, "Decoherent Histories Quantum Mechanics and Copenhagen Quantum Mechanics", arXiv:2110.15471 [quant-ph; also gr-qc, physics.hist-ph], v1 submitted 29 October 2021 (one version). Affiliation: Santa Fe Institute (Hartle also UC Santa Barbara). No journal reference. arXiv comments: "4 pages. arXiv admin note: substantial text overlap with arXiv:quant-ph/0609190, arXiv:2012.05229". The PDF as downloaded is 3 pages.

**Important for citing it:** the paper's own first footnote says it is "The conclusion from the authors' paper *Quasiclassical Coarse Graining and Thermodynamic Entropy*, Phys. Rev. A, 76, 022104 (2007), arXiv:quant-ph/0609190 modestly edited and reformatted. The references have not been updated." So it is a 2007 text reissued in 2021, not a new argument, and its four references are from 1958 to 1994. It has no section headings and **no numbered equations**; its content is in prose and a bulleted list.

URLs read: https://arxiv.org/abs/2110.15471 (abstract page), https://arxiv.org/pdf/2110.15471 (full PDF text), https://arxiv.org/e-print/2110.15471 (LaTeX source, file `cop-ext2-copy-copy.tex`).

### 1.2 Key definitions and claims (in the paper's words where short)

- **What Copenhagen does.** It "*postulates* (implicitly for most authors or explicitly in the case of Landau and Lifshitz [1]) a classical world and a quantum world, with a movable boundary between the two" (p. 1).
- **Why it cannot be fundamental.** "it seems to require a physicist outside the system making measurements (often repeated ones) of it. That would seem to rule out any application to the universe, so that quantum cosmology would be excluded. Also billions of years went by with no physicist in the offing." (p. 1)
- **The classical world is derived, not postulated.** The quasiclassical realm "is not *postulated* but rather is *explained* as an emergent feature of the universe characterized by the Hamiltonian H, the quantum state |Ψ⟩, and the enormously long sequences of accidents (outcomes of chance events) that constitute the coarse-grained decoherent histories." (p. 1)
- **Definition of a measurement situation.** "a 'measurement situation' exists if some variables (including such quantum-mechanical variables as electron spin) come into high correlation with a quasiclassical realm." (p. 1) The examples are fission tracks in mica, the Moon's positions, and density fluctuations in the early universe; "It makes no difference if a physicist or other human or a chinchilla or a cockroach looks at the tracks." (p. 1)
- **Collapse is conditioning.** "The idea of 'collapse of the wave function' corresponds to the notion of variables coming into high correlation with a quasiclassical realm ... The collapse of the probabilities that occurs in their construction is no different from the collapse that occurs at a horse race when a particular horse wins and future probabilities for further races conditioned on that event become relevant." (pp. 1 to 2) The "second law of evolution" (state reduction by a projection, then renormalization) "is thus not some mysterious feature of the measurement process. Rather it is a natural consequence of the quantum mechanics of decoherent histories" (p. 2).
- **How Copenhagen is recovered.** "Copenhagen quantum theory is an approximation to the more general theory that is appropriate for the special case of measurement situations. Decoherent histories quantum mechanics is rather a *generalization* of the usual approximate quantum mechanics of measured subsystems." (p. 2)
- **Irreversibility.** "It is not an absolute concept but context-dependent like so much else in quantum mechanics and statistical mechanics. It is highly dependent on coarse graining, as in the case of the document shredding" (p. 3; the one- against two-dimensional shredding example). "Irreversibility is evidently not absolute but dependent on the effort or cost involved in reversal." (p. 3)
- **What is external to the wave function.** "The founders of quantum mechanics were right in pointing out that something external to the framework of wave function and Schrödinger equation *is* needed to interpret the theory. But it is not a postulated classical world ... Rather it is the initial condition of the universe that, together with the action function of the elementary particles and the throws of quantum dice since the beginning, explains the origin of quasiclassical realm(s) within quantum theory itself." (p. 3) Note the plural "realm(s)".

### 1.3 Stated assumptions and limitations

- "Decoherence may fail if the graining is too fine. Predictability is limited by quantum noise and by the major branchings that arise from the amplification of quantum phenomena as in a measurement situation. Finally, we cannot expect a quasiclassical description of the universe in its earliest moments where the very geometry of spacetime may be undergoing large quantum fluctuations." (p. 2)
- The Copenhagen characterizations of measurement ("irreversible act of amplification", "the creation of a record", "a connection with macroscopic variables") "are not false, but true in an approximation that need not be exactly defined." (p. 2) In other words, how long a record must last, or how much entropy must rise, has no sharp answer and does not need one.
- The paper is a conclusion section lifted from a longer paper; the arguments it summarizes (the relation between the coarse graining of quasiclassical realms and thermodynamic entropy) are in quant-ph/0609190, which was not read for this note.

### 1.4 Criticisms the paper cites or responds to

- The Copenhagen postulate of a classical world (Landau and Lifshitz, ref. [1]) and its need for an outside observer; this is the criticism the paper is built to answer.
- The imprecision of "irreversible", "record" and "macroscopic" as foundations for a measurement-based theory (p. 2).
- Not addressed here (general knowledge, to verify): the "set selection" objection that decoherent-histories theory admits many mutually incompatible decoherent sets with no rule for choosing among them (Dowker and Kent, 1996, and later papers by Kent). The 2021 text's plural "realm(s)" acknowledges the possibility of several realms without discussing it.

---

## 2. Hartle (2020)

### 2.1 Bibliographic details

James B. Hartle, "Arrows of Time and Initial and Final Conditions in the Quantum Mechanics of Closed Systems Like the Universe", arXiv:2002.07093 [gr-qc], v1 submitted 17 February 2020 (one version; the PDF is dated February 18, 2020). Affiliations: UC Santa Barbara and Santa Fe Institute. No journal reference listed. 21 pages, one figure (Fig. 1: "A simple model of a closed quantum system is a universe of quantum matter fields inside a large closed box (say, 20,000 Mpc on a side) ..."), 35 references. Sections: I Introduction; II The classical arrow of time of retarded electromagnetic radiation; III A model quantum universe in a closed box (A very large experiment; B coarse grained histories of the universe; C coarse-grained histories); IV A time neutral decoherent histories quantum mechanics of the universe (A histories; B decoherence and probabilities); V Final condition limitations on the number of decoherent histories (A indifference; B pure final state; C general case; D decoherence requires time asymmetry; E causality); VI A note on quantum and classical spacetime; VII Conclusion. The published text has many typographical slips ("universe universe", "arrows ot time", "disapation"); quotations below are verbatim.

URLs read: https://arxiv.org/abs/2002.07093, https://arxiv.org/pdf/2002.07093 (full text), https://arxiv.org/e-print/2002.07093 (source `infin4.tex` and the figure `ubox1.pdf`).

### 2.2 Key definitions and equations, numbered as in the paper

**The inputs.** The theory is the triple (H, ρ_I, ρ_F): a time-neutral Hamiltonian H, an initial density matrix ρ_I at time t_I ("usually assumed pure", ρ_I = |Ψ⟩⟨Ψ|) and a final density matrix ρ_F at time t_F. "The conditions ρ_I and ρ_F, enter this formalism symmetrically so there are no built in quantum arrows of time. Differences between ρ_I and ρ_F can lead to physical arrows of time." (p. 5)

**What an arrow of time is, in this framework.** "The universe displays an arrow of time when the probabilities are high for histories that describe the systematic growth (or decay) of a physically interesting quantity defined at a series of times. A suitably coarse grained entropy, or the amount of retarded electromagnetic radiation are examples." (p. 3)

**Section II, the electromagnetic arrow (unnumbered equations (R) and (A)).** Any solution of Maxwell's equations for sources j^μ can be written either as a free field from the past plus retarded fields,

$$A^\mu(x) = A^\mu_{\rm in}(x) + \int d^4x'\, D_{\rm ret}(x - x')\, j^\mu(x') \qquad (R)$$

or as a free field from the future plus advanced fields,

$$A^\mu(x) = A^\mu_{\rm out}(x) + \int d^4x'\, D_{\rm adv}(x - x')\, j^\mu(x') \qquad (A).$$

"we could say that the electromagnetic arrow of time emerges from the special initial condition of A^in_μ(x) ≈ 0 and a final condition of indifference as to what A^out_μ(x) turns out to be." (p. 8) This is the classical template for the quantum argument.

**Section IV.A, histories.** Coarse-grained yes/no alternatives at one time are an exhaustive set of exclusive Heisenberg-picture projection operators {P_α(t)}:

$$P_\alpha(t) P_{\alpha'}(t) = \delta_{\alpha\alpha'} P_\alpha(t), \qquad \sum_\alpha P_\alpha(t) = I. \qquad (4.1)$$

The same alternative at different times is connected by unitary evolution,

$$P_\alpha(t') = e^{iH(t'-t)/\hbar}\, P_\alpha(t)\, e^{-iH(t'-t)/\hbar}. \qquad (4.2)$$

An individual history α ≡ (α_1, ..., α_n) is the chain of projections

$$C_\alpha \equiv C_{\alpha_n \alpha_{n-1} \cdots \alpha_1} \equiv P^n_{\alpha_n}(t_n) \cdots P^1_{\alpha_1}(t_1). \qquad (4.3)$$

**Section IV.B, decoherence and probabilities.** A set decoheres when the off-diagonal elements of the decoherence functional D are negligible; the diagonal elements are then the probabilities:

$$D(\alpha', \alpha) \approx \delta_{\alpha'\alpha}\, p(\alpha). \qquad (4.4)$$

"Eq. (4.4) is the central equation in any decoherent histories formulation of quantum theory ... Decoherence is a necessary condition for the p(α) defined by (4.4) to be *consistent* with the usual rules of probability theory [5]." (p. 13)

**The time-neutral decoherence functional with initial and final conditions** (boxed in the paper; Hartle attributes it to Gell-Mann and Hartle 1994, his ref. [1]):

$$D(\alpha', \alpha) \equiv \mathcal{N}\, {\rm Tr}\big[ C^\dagger_{\alpha'}\, \rho_F\, C_\alpha\, \rho_I \big], \qquad 1/\mathcal{N} \equiv {\rm Tr}(\rho_I \rho_F). \qquad (4.5)$$

"This decoherence functional is time neutral in the sense that using the cyclic property of the trace ρ_I and ρ_F can be interchanged. Thus they enter the formalism symmetrically so that there is no built in arrow of time as there is in the textbook quantum mechanics of measurement situations." (p. 13)

For a pure initial state ρ_I = |Ψ⟩⟨Ψ|, with branch state vectors

$$|\Psi_\alpha\rangle \equiv C_\alpha |\Psi\rangle, \qquad (4.7)$$

this becomes

$$D(\alpha', \alpha)/\mathcal{N} \equiv \langle \Psi | C^\dagger_{\alpha'} \rho_F C_\alpha |\Psi\rangle = \langle \Psi_{\alpha'} | \rho_F | \Psi_\alpha \rangle, \qquad (4.6)$$

and the decoherence condition (boxed) is

$$\langle \Psi_{\alpha'} | \rho_F | \Psi_\alpha \rangle = \delta_{\alpha'\alpha}. \qquad (4.8)$$

"We can think of ρ_F as a positive metric on the space of histories. A set of histories decoheres if their branch state vectors are mutually orthogonal in the metric supplied by the final condition ρ_F." (p. 14; Craig's "geometry of consistency", ref. [32])

**Section V.A: the condition under which the usual forward-time quantum mechanics is recovered.** When ρ_F ∝ I,

$$D(\alpha', \alpha)/\mathcal{N} \equiv \langle \Psi | C^\dagger_{\alpha'} C_\alpha |\Psi\rangle = \langle \Psi_{\alpha'} | \Psi_\alpha \rangle \approx \delta_{\alpha'\alpha}. \qquad (5.1)$$

(The published equation carries a stray fragment "⟩χ|⟨χ|" before it and repeats "= ⟨Ψ_α'|Ψ_α⟩" after it; both are in the author's LaTeX source and are typos.) This is the ordinary decoherence condition on branch state vectors, the one the handoff writes as D(α, β) = Tr(C_α ρ_0 C_β^†) with p_α = D(α, α); the handoff's index order is the transpose of Hartle's, which changes nothing. "If the dimension of the Hilbert space is N we can have a maximum of N histories in a decohering set. A final condition ρ_F ∝ I allows the maximum number of decohering histories consistent with the dimension of the Hilbert space. If the Hilbert space is infinite dimensional there is no restriction at all." (p. 14)

**Section V.B: a pure final state kills prediction.** With ρ_F = |χ⟩⟨χ|,

$$D(\alpha', \alpha)/\mathcal{N} = \langle \chi | C_{\alpha'} |\Psi\rangle^* \langle \chi | C_\alpha |\Psi\rangle. \qquad (5.2)$$

"a pure final state allows only sets with one history (and its negation) to decohere. Assuming a pure final state results in only a single history being predicted with unit probability which is no prediction at all." (p. 15) **Section V.C, the general case:** if ρ_F has K < N nonzero eigenvalues, "the theory (H, ρ_F, ρ_I) can predict probabilities for K different histories." (p. 15)

**Section V.D: decoherence requires time asymmetry.** "if the initial density matrix is pure ρ_I ≡ |Ψ⟩⟨Ψ| then the final state cannot be also pure and support non-trivial sets of decohering histories. In particular the final density matrix ρ_F cannot be the same as the initial one ρ_I. Time asymmetry between initial and final conditions is thus necessary for decoherence." (p. 15) Footnote 3 adds that even for a mixed ρ_I "there are still stringent conditions" for equal initial and final density matrices (ref. [1], Sec. VI.B).

**The statement about records** (p. 4, repeated p. 6; in the author's source the word *records* is italicized): "Decoherence requires coarse graining — following some variables describing the universe but ignoring others. Interaction of the followed variables with the 'environment' of the ignored variables produces the decoherence of sets of histories in the followed variables as in many discussions of environmental decoherence show e.g [17–20]. The interaction creates *records* that are strongly correlated with the individual histories in the environment but orthogonal to each other. That orthogonality produces decoherence. It is a remarkable fact that in DH quantum theory it is necessary to lose some information in order to have any information at all." (verbatim apart from the paper's own doubled words "records are that are strongly correlated by with"). Records here are the physical *mechanism* of decoherence, not an arrow in their own right; the phrase "arrow of records" does not occur in the paper.

**Section V.E / III.A: causality.** A nontrivial final selection "will necessarily influence what histories are predicted between t_I and t_F. That is acausal — the action taken in the future that influences what occurs in the present and past. Or we could say that by an analysis of what doesn't occur in the present we could predict what does have to happen in the future." (pp. 9 to 10) "Causality could be assumed were ρ_F ∝ I because then there is no final selection at all." (p. 10) "To build in causality to the basic theory restrict ρ_F ∝ I because then there is no final selection at all." (p. 16)

**The three findings as stated in the Introduction (pp. 3 to 4).** (1) "There is no decoherent set of histories in which the ρ_F is the same as a pure initial state ρ_I. Decoherence requires time asymmetry in the boundary conditions for prediction in closed quantum systems." (2) ρ_F ∝ I "allows a finer-grained description of the universe in terms of decoherent histories than any other final state." (3) "In quantum mechanics arrows of time do not generally arise just from special initial conditions alone as has sometimes been suggested. Rather the arrows arise by differences between initial and final conditions. Some arguments emphasizing the role of special initial conditions can be interpreted as implicitly assuming a particular initial condition ρ_I and a final condition of indifference ρ_F ∝ I".

### 2.3 Stated assumptions and limitations

- Time-neutral dynamics assumed ("A familiar example is a CPT invariant quantum field theory coupled to a classical cosmological geometry", p. 2); the universe spatially closed (p. 3); everything inside one box with "no influence of the outside on the inside or the inside on the outside" (p. 5).
- **Classical spacetime is assumed.** "We assume a fixed, flat, background spacetime inside our model box thus neglecting quantum gravity. This an excellent approximation in the realistic universe for times later than a very short interval ∼ 10⁻⁴³ sec. after the big bang. As a consequence there is a well defined notion of time in any particular Lorentz frame." (p. 8) Section VI says what this leaves out: "the singularity theorems of classical cosmology show that there is no classical spacetime near the big bang", "The classical behavior of anything is not a given in a quantum universe. It is a matter of quantum probabilities", and for formalisms that do not assume classical spacetime "the kind of analysis represented in this paper remains to be carried out for these cases." (pp. 16 to 17)
- **Not a complete explanation of the arrows.** "The purpose of this paper is not to present a complete explanation of the emergence of the universe's time asymmetries. Rather it is to exhibit a prerequisite for such discussions for a model quantum universe." (p. 4) Footnote 1: "Note that we are not claiming that all arrows of time exhibited by the universe arise by this mechanism. See, e.g. [13]." (ref. [13] is Barbour, Koslowski and Mercati's gravitational arrow of time, 2014.)
- **Which arrows are listed.** Thermodynamic; retarded electromagnetic radiation; the expansion of the universe; the growth of fluctuations (p. 2). The psychological arrow and the arrow of records are *not* in the list. (In the LaTeX source two further bullets are commented out and so absent from the published paper: "The psychological arrow of time --- we remember the past, we predict the future." and the CP-violation arrow. The author chose to leave them out; this note records the fact and reads nothing more into it.)
- **The final condition is a choice, not a theorem.** "the initial and final conditions and the theory of dynamics and the quantum framework in which they are applied are not decided by such theoretical argument. They are discovered by of comparing the predictions of different theories (H, ρ_I, t_I, ρ_F, t_F) with large scale observations of our universe." (p. 18) The two reasons offered for ρ_F ∝ I are theoretical attractiveness only: causality (Sec. V.E) and finest graining (Sec. V.A).
- On the textbook assumption that reduction runs in the thermodynamic direction: "The author knows of no compelling justification for this assumption, and the experimental evidence for it is limited at best." (p. 5)

### 2.4 Criticisms cited or responded to

- The view that arrows come from special initial conditions alone (finding (3); the source has a commented-out Boltzmann quotation next to the conclusion bullet, with the remark that Boltzmann "was assuming classicality").
- The built-in time asymmetry of Copenhagen state reduction (p. 5), which disqualifies it as a frame for *deriving* arrows.
- Acausality of final conditions: the Aharonov–Vaidman two-state vector formalism and weak measurements (ref. [26]) and Craig's "Observation of the Final Boundary Condition" (ref. [27]) are cited as examples where a final condition would show up in the present. Hartle's response is to restrict ρ_F ∝ I.
- Environmental decoherence mechanisms "assume disapation and therefore an arrow of time" (p. 3, refs. [15, 16]), which he uses to make finding (1) "less surprising".
- Not addressed (general knowledge, to verify): the set-selection problem (Dowker and Kent, 1996); whether a time-neutral two-boundary formalism is empirically distinguishable from the ordinary one when ρ_F ∝ I (by Sec. V.A it is not: the predictions coincide).

---

## 3. Mapping table against the handoff

Verdict key: **STANDARD** = stated in the paper (location given); **SIMPLIFYING ASSUMPTION** = a modeling choice the paper also makes or allows, not a result; **NOVEL** = not in either paper (it may be elsewhere in the literature; where a nearer source is known it is named, "to verify"). "Not addressed" means the paper is silent.

| # | Handoff statement | Verdict | Where, and what the paper actually says |
|---|---|---|---|
| 1 | §1 item 4: "No objectively advancing universal now." | **NOVEL relative to these two papers** (not addressed by either). | Hartle 2020 Sec. III assumes "a well defined notion of time in any particular Lorentz frame" as a model convenience; Sec. VI says classical spacetime "is not a given". Neither paper discusses a "now" or its passage. The nearest source is Hartle's own "The Physics of Now" (Am. J. Phys. 73, 101, 2005; his ref. [25]), cited in 2020 only for adaptive wavelength selection; not read for this note, to verify. |
| 2 | §1 item 4: "Apparent temporal passage is associated with ordered observer states, memories, and the arrow of records." | **NOVEL relative to these papers**; the explanatory order is the reverse of Hartle's. | Hartle 2020 never uses "arrow of records"; records appear only as the mechanism of decoherence (pp. 4, 6). The psychological arrow is absent from his list (and was removed from the draft; Sec. 2.3 above). No sentence in either paper connects experienced passage to records. |
| 3 | §1 item 4: cosmic time is "a useful model coordinate ... not a preferred global present". | **STANDARD in spirit** (Hartle 2020 Sec. III and VI). | The box model uses a Lorentz-frame time as a coordinate for convenience; Sec. VI insists classical spacetime is emergent and the analysis without it "remains to be carried out". No claim of a preferred present anywhere. |
| 4 | §3 class operator C_α and decoherence functional D(α, β) = Tr(C_α ρ_0 C_β^†), p_α = D(α, α). | **STANDARD**, as the special case ρ_F ∝ I. | Eqs. (4.1) to (4.4); the handoff's D is eq. (4.5) with ρ_F ∝ I, i.e. eq. (5.1), up to the index order. The handoff should say that it assumes a final condition of indifference; Hartle makes that assumption explicit and gives two reasons for it (Sec. V.A, V.E). |
| 5 | §1 item 5: probabilities only for an appropriately decoherent family; amplitudes interfere. | **STANDARD**. | 2020 eq. (4.4) and "Decoherence is a necessary condition for the p(α) ... to be consistent with the usual rules of probability theory" (p. 13); 2021 p. 2: "Without projections, there are no questions and no probabilities." |
| 6 | §3 and Stage B/C: "Stable classical records are emergent and approximate"; decoherence approximate. | **STANDARD**. | 2020 eq. (4.4) is written with ≈ and "negligible"; 2021 p. 2: "Decoherence may fail if the graining is too fine" and measurement-as-record-creation is "true in an approximation that need not be exactly defined." |
| 7 | §6 check: "Do not assert permanent classical histories through all time in generic systems." | **STANDARD / consistent**, with a gap. | 2021 p. 2: no quasiclassical description "in its earliest moments"; irreversibility "not absolute" (p. 3). 2020 Sec. VI: no classical spacetime near the big bang or a big crunch. **Gap:** neither paper discusses quantum-eraser recoherence; the handoff's eraser counterexample and the "permanence of the past" caveat come from Gell-Mann and Hartle 1995 (handoff item 3), not from these two. |
| 8 | Research question: "apparently directional histories inside a time-neutral, unitary quantum universe". | **STANDARD**, with one correction to the wording. | This is exactly Hartle 2020's frame: time-neutral (H, ρ_I, ρ_F), unitary eq. (4.2), arrows as high-probability growth histories (p. 3), arising "from time asymmetries between initial and final conditions and not just just special initial conditions" (p. 17). **Correction:** in his terms the handoff's one-boundary setup is time-neutral only because it silently takes ρ_F ∝ I; finding (3) is precisely that such arguments "can be interpreted as implicitly assuming ... a final condition of indifference". |
| 9 | §1 item 2: "Everett / no fundamental collapse ... All decohered alternatives remain in the global state." | **PARTLY STANDARD.** No collapse: STANDARD. "All alternatives remain": an interpretive addition the papers neither make nor deny. | 2021 pp. 1 to 2: collapse is conditioning, "no different from ... a horse race". 2020 p. 5: reduction has "a built in time asymmetry" and is dropped. But both papers speak of "which occurs", "accidents", "throws of quantum dice" (single-outcome language); Everett is not named in either, and a "Many Worlds?" reference in the 2020 source is commented out. |
| 10 | §1 item 3: observers are physical subsystems; no external selector. | **STANDARD**. | 2021 p. 1 (fission tracks, chinchilla, cockroach; "All those other variables are effectively doing the 'observing'"). 2020 Sec. III.B: measurements are correlations between subsystems inside the box and "play no preferred role in the formulation of its quantum mechanics". |
| 11 | §6 check: no unique, naturally preferred exact branch partition. | **STANDARD in spirit; the hard version not addressed.** | 2021 p. 3 "realm(s)"; 2020 Sec. V.A: with ρ_F ∝ I "a maximum of N histories in a decohering set" and no restriction in infinite dimensions, so many decoherent sets exist. The set-selection objection (Dowker and Kent, general knowledge, to verify) is answered in neither paper. |
| 12 | §6 check: entropy and record surprisal are not equivalent. | **Not addressed**; consistent. | 2021 relates the coarse graining of quasiclassical realms to thermodynamic entropy (its parent paper's subject) and says nothing about surprisal of a record. |
| 13 | §1 item 1: fixed laws λ; the handoff fixes ρ_0 and (implicitly) ρ_F ∝ I. | **SIMPLIFYING ASSUMPTION**, with Hartle's two grounds. | 2020 Sec. VII.B: the boundary conditions "are not decided by such theoretical argument"; ρ_F ∝ I is "simple, generally consistent with causality, and familiar from the text book" (p. 6). He hopes for a unification that would fix H, ρ_I, ρ_F together (p. 18). |
| 14 | Stage B: "Evolve unitarily, with no collapse"; two observer-record registers. | **STANDARD** as a modeling template. | 2020 Sec. III.A "A very large experiment" and Sec. IV: unitary Heisenberg evolution, records as environment states "orthogonal to each other". The papers do not model observer registers themselves. |

---

## 4. The arrow-of-records question, answered from Hartle 2020

**Does Hartle attribute the arrow of records to the special initial condition alone?** No. He attributes every arrow he derives to the *difference* between the initial and final conditions, and says so three times:

- Introduction, finding (3): "In quantum mechanics arrows of time do not generally arise just from special initial conditions alone as has sometimes been suggested. Rather the arrows arise by differences between initial and final conditions. Some arguments emphasizing the role of special initial conditions can be interpreted as implicitly assuming a particular initial condition ρ_I and a final condition of indifference ρ_F ∝ I" (p. 4).
- Conclusion: "In a quantum theory arrows of time arise from time asymmetries between initial and final conditions and not just just special initial conditions as sometimes assumed." (p. 17)
- Section V.D: "Time asymmetry between initial and final conditions is thus necessary for decoherence." (p. 15)

Records enter one step earlier than any arrow: they are what decoherence consists of ("The interaction creates records that are strongly correlated with the individual histories in the environment but orthogonal to each other. That orthogonality produces decoherence", p. 4), and decoherence itself is only possible because ρ_F ≠ ρ_I (finding (1)). So in his framework the chain is: boundary-condition asymmetry → decoherence possible → records exist and histories have probabilities → high-probability histories of growing entropy or radiation = the arrows. He does not name an "arrow of records" and does not discuss the psychological arrow at all (it is in the list only in commented-out source).

**Does a time-symmetric formulation with a final condition change anything about records?** With ρ_F ∝ I, nothing: eq. (5.1) is the ordinary decoherence condition, the number of decoherent histories is maximal, and causality holds "because then there is no final selection at all" (p. 10). With any other ρ_F, records are *fewer*, not reversed: a rank-K final condition allows at most K decoherent histories (Sec. V.C), a pure one allows one history "which is no prediction at all" (p. 15), and the final selection is acausal: "the final condition in the future would influence what occurs in the present and past" (pp. 15 to 16). Nothing in the paper describes records being erased or running backward.

**The handoff's item 3 ("persistent observer records explain the apparent direction and continuity of experienced time without a collapse mechanism"), judged in Hartle's framework: PARTLY STANDARD, and an overreach as worded.**

- "without a collapse mechanism": STANDARD (2021: collapse is conditioning; 2020: the time-neutral formulation drops reduction and its "built in time asymmetry").
- "persistent observer records" exist and are physical correlations in the environment: STANDARD (p. 4), with the 2021 caveat that how long a record must last is "true in an approximation that need not be exactly defined."
- "records explain the apparent direction": OVERREACH relative to this paper, for two reasons. First, the explanatory order is reversed: for Hartle the asymmetry of boundary conditions explains why records (and arrows) can exist; records are an output of that asymmetry, not the explanation of direction. Second, the paper is silent on experienced or psychological time and on "continuity"; it treats arrows only as "the probabilities of appropriately coarse grained sets of histories of quantities like entropy that grow or decay" (abstract). A defensible restatement in his terms would be: "records are oriented because the boundary conditions are asymmetric; an observer's sense of direction, if it tracks its records, inherits that orientation", and even that last step is not taken in either paper (nearest candidate: Hartle 2005, "The Physics of Now", to read).

*Ours, unverified:* the practical consequence for the handoff is that its Stage C model, which has only ρ_0, cannot by itself demonstrate anything about time neutrality; to make the "time-neutral" claim testable in the model one would implement eq. (4.5) with an explicit ρ_F, check that ρ_F ∝ I reproduces the one-boundary results (eq. (5.1)), and check that a rank-deficient ρ_F reduces the number of decoherent histories as Sec. V.C says.

---

## 5. What contradicts or complicates the handoff

1. **"Time-neutral" needs a final condition to mean anything.** The handoff's formalism (§3) has one boundary, ρ_0. Hartle 2020 shows that this is the ρ_F ∝ I special case and that arrows then come from ρ_I ≠ ρ_F, not from ρ_0 alone (finding (3)). The handoff should either add ρ_F ∝ I as a named assumption or drop "time-neutral" from the research question.
2. **The arrow of records is not Hartle's phrase, and the psychological arrow is not in his list.** Item 4 of the handoff's §1 and item 3 of the owner's task rest on a link (records → experienced passage) that neither paper makes (Sec. 4 above).
3. **Decoherent histories is not Everett.** Both papers use single-outcome language ("which occurs", "throws of quantum dice") and name no interpretation; Everettian talk of all branches remaining in the global state is the handoff's gloss. Not a contradiction, but §1 item 2 should not be cited to these papers.
4. **The 2021 paper is a 2007 text.** Its closing attribution of the quasiclassical realm to "the initial condition of the universe ... and the throws of quantum dice" is, by Hartle 2020's own finding (3), an argument that implicitly assumes ρ_F ∝ I. The two papers are consistent once that is said; the handoff should cite the 2020 paper, not the 2021 one, for anything about time direction.
5. **Classical spacetime is assumed throughout Hartle 2020**, and he says the analysis without it "remains to be carried out". The handoff's §6 check "Do not assume all histories share a common four-dimensional cosmic foliation in exact GR" is stricter than anything either paper does; it is consistent with Sec. VI, but no result in these papers supports a model without a background time.
6. **Records can only be reduced, not reversed, by a final condition** (Sec. V). If the handoff ever models a nontrivial ρ_F, it should expect fewer decoherent histories and acausal correlations, not a reversed arrow.
7. **Neither paper addresses set selection** (which decoherent family is "the" one). The handoff's refusal to assume a preferred partition is in the spirit of "realm(s)" but is not backed by an argument in these papers.

---

## 6. Provenance

Texts read: `2110.15471.pdf` (3 pages, 9,341 characters extracted) and its source `cop-ext2-copy-copy.tex` (79 lines); `2002.07093.pdf` (21 pages, 45,871 characters extracted) and its source `infin4.tex` (711 lines) with the figure `ubox1.pdf` (not opened; its caption is in the text). Downloaded files were kept in their own empty scratchpad folders and treated as data. Every equation and quotation above was checked against the LaTeX source; the two equation typos noted in Sec. 2.2 are the author's. General-knowledge items (Dowker and Kent; the content of Hartle 2005; quant-ph/0609190's body) were not read and are marked "to verify".

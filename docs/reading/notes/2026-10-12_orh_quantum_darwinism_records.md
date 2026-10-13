# Reading note: quantum Darwinism and redundant records, mapped against the observer-relative-histories handoff

**Date:** 2026-10-12. **Purpose:** Stage A of `docs/theory/observer_relative_histories_research_handoff.md` (the "literature-to-math map"): read the three Zurek-group papers the handoff names (its items 4, 8 and 12), transcribe their definitions and equations exactly, record their stated assumptions and limitations, and say for each statement of the handoff's sections 3 and 4, its Stage B list and two of its methodological checks whether it is STANDARD, a SIMPLIFYING ASSUMPTION or a NOVEL CONJECTURE.

**Status of this note.** Written by an AI reading agent (Claude) from the papers' text. Everything attributed to a paper is quoted or closely paraphrased from it with section or equation numbers; everything else is marked "Ours, unverified." Nothing here has been reviewed by a physicist. The labels [Zurek09], [ZZ17], [Zurek03] are local to this note; they are not keys in `REFERENCES.bib`, which this note does not touch.

**How the papers were read.** The arXiv abstract pages were fetched to confirm identity; the PDFs were downloaded from arxiv.org and their text extracted (pypdf); in parallel the ar5iv HTML renditions (ar5iv.labs.arxiv.org) were converted to text with every formula's LaTeX kept. Equation numbers below are the papers' own, checked against the PDF text where the HTML dropped a label. [Zurek09] and [ZZ17] were read in full. [Zurek03] was read in part; the exact list of sections read and skipped is in section 3.1.

---

## 0. Verdicts in one screen

| Handoff statement | Verdict | Where |
|---|---|---|
| S3: visibility $V=\lvert\langle E_B\lvert E_A\rangle\rvert$ controls interference of the reduced system | STANDARD, for a *balanced* interferometer (equal amplitudes); the general case has $V=2\lvert a\rvert\lvert b\rvert\,\lvert\langle E_B\lvert E_A\rangle\rvert$ (ours, textbook) | [Zurek03] Eqs. (4.11)–(4.12); [Zurek09] Eq. (5) |
| S3: interference recoverable if information is recombined or erased; decoherence not an absolute ban | STANDARD in principle, with the papers' emphasis that it is practically unattainable | [Zurek03] II.1.3 footnote 3, VII.3.1; [Zurek09] Sec. II |
| S3: stable classical records are emergent and approximate | STANDARD | [Zurek03] VII.3, VII.3.1 ("relatively objective"); [Zurek09] Sec. III |
| S4: many observers agree by reading one redundant record | STANDARD; it is the defining claim of quantum Darwinism | [Zurek09] Sec. II and Fig. 2; [Zurek03] VII.1.1, VII.3.1; [ZZ17] abstract |
| S4: use joint, not independent, probabilities for observers' records | STANDARD in content (branch structure makes readings of pointer-basis fragments perfectly correlated); the explicit joint-distribution bookkeeping is the handoff's own framing | [Zurek09] Eq. (6); [Zurek03] Eq. (7.1), VII.3.1 |
| Stage B: reduced density matrices, coherence, $V$, $I(S{:}F)$ | STANDARD | [Zurek09] Eqs. (1)–(3); [Zurek03] Eqs. (4.11), (7.11)–(7.12) |
| Stage B: redundancy | STANDARD quantity, but two inequivalent definitions exist and $\delta$ must be fixed: a SIMPLIFYING ASSUMPTION the handoff has not yet made | [Zurek09] Eq. (4); [ZZ17] Eqs. (4)–(5), (11), (15) |
| Stage B: agreement/disagreement rates of observer reports | NOVEL as a named quantity; not defined in these papers (closest: "consensus", and the bound "number of observers ... bounded from above by $\mathcal R_{\mathcal J}$") | [Zurek03] VII.3.1 |
| Stage B: quantum eraser / controlled recoherence | STANDARD in principle (recurrences; measuring the record in the conjugate basis); a small toy will show recurrences as a *size artifact* | [Zurek03] II.1.3 footnote 3, VII.3.1 |
| Check: do not assert permanent classical histories | STANDARD and shared by the papers, which say it in stronger words | [Zurek09] Sec. V; [Zurek03] VII.3.1 |
| Check: do not infer consciousness from a qubit record | STANDARD practice; the papers model memory as an open quantum register and use "aware" "in a down-to-earth sense" | [Zurek03] VI.2, VII.2 |
| S2–S3: record surprisal $I(R_n)=-\log_2\mu(\mathcal C(R_n))$ | NOVEL relative to these papers: nothing like it appears (nearest neighbors are algorithmic complexity of records, Eqs. (7.3)–(7.4), and redundancy, which are different quantities) | [Zurek03] VII.1.1 |

Two complications the handoff should carry (details in section 6): [Zurek09] is explicitly *not* Everettian ("our discussion is interpretation-free ... Treating [the universal state vector] as if it really existed seems unwarranted"), and [Zurek03] VII.3 argues that consistent histories are "both not enough and too much" and that einselection, not consistency, is what picks the histories; the handoff's Stage C rests on the decoherence functional.

---

## 1. [Zurek09] W. H. Zurek, "Quantum Darwinism"

**Bibliographic.** Nature Physics **5**, 181–188 (2009), DOI 10.1038/nphys1202. Read as arXiv:0903.5082 (v1, 29 March 2009), https://arxiv.org/abs/0903.5082 and https://arxiv.org/pdf/0903.5082, plus the ar5iv rendition. **Identity check:** the arXiv page's journal-reference field reads "Nature Physics, vol. 5, pp. 181-188 (2009)" and the title, author and abstract match the journal paper as described in the handoff; whether the arXiv text differs from the published text in detail was not checked (to verify). Six pages, five sections (I Decoherence and einselection; II Environment as a witness; III From copying to quantum jumps; IV Probabilities from entanglement; V Discussion) plus a Box. **Read in full.**

**Setting.** A system $\mathcal S$, an environment $\mathcal E$ made of subsystems, and fragments $\mathcal F$: "non-overlapping collections of subsystems of $\mathcal E$" whose only requirement is that each "should be individually accessible to measurements; observables of different subsystems commute" (Fig. 1 caption). The claim: "Observers eavesdrop on the environment. Vast majority of our data comes from fragments of $\mathcal E$. ... We never access all of $\mathcal E$. Tiny fractions suffice" (Sec. II).

**Definitions and equations, numbered as in the paper.**

$$\rho_{\mathcal S}=\mathrm{Tr}_{\mathcal E}\,|\Psi_{\mathcal{SE}}\rangle\langle\Psi_{\mathcal{SE}}| \qquad (1)$$

with von Neumann entropy $H_{\mathcal S}=H(\rho_{\mathcal S})=-\mathrm{Tr}\,\rho_{\mathcal S}\lg\rho_{\mathcal S}$ (unnumbered, Sec. I). Pointer states are those that "result in smallest entropy increase"; sorting pure states by the entropy of the evolved $\rho_{\mathcal S}$ is the "predictability sieve" (Sec. I).

$$\rho_{\mathcal{SF}}=\mathrm{Tr}_{\mathcal E/\mathcal F}\,|\Psi_{\mathcal{SE}}\rangle\langle\Psi_{\mathcal{SE}}| \qquad (2)$$

$$I(\mathcal S{:}\mathcal F)=H_{\mathcal S}+H_{\mathcal F}-H_{\mathcal S,\mathcal F} \qquad (3)$$

"the difference between entropies of two systems ... treated separately and jointly." Fig. 2 (the partial-information plot): $I(\mathcal S{:}\mathcal F_f)$ against the fraction $f$ of $\mathcal E$ intercepted. For states produced by decoherence it rises "bit for bit" at small $f$ and then levels off at $H_{\mathcal S}$: "the redundancy plateau at $H_{\mathcal S}$, where additional bits only confirm what is already known"; "The redundancy plateau is a classical plateau." For a pure global state the plot is antisymmetric about $\{H_{\mathcal S},f=\tfrac12\}$ and rises to $2H_{\mathcal S}$ as $f\to1$, which "can be obtained only through global measurements on $\mathcal S$ and nearly all $\mathcal E$"; for a Haar-random pure state of $\mathcal{SE}$ there is "little mutual information ... smaller than half of $\mathcal E$" and then everything at $f=\tfrac12$: "such random states ... exhibit no redundancy" (Fig. 2 caption; refs. [13], [14] = Blume-Kohout and Zurek 2005, 2006). With Shannon entropies of local observables instead, "such Shannon $I(\mathcal S{:}\mathcal F_f)$ never exceeds $H_{\mathcal S}$, antisymmetry is lost, and the plateau continues until the end at $f\sim1$" (Sec. II).

$$R_\delta=1/f_\delta \qquad (4)$$

where $f_\delta$ is the fraction of $\mathcal E$ that holds "all but $\delta$" of the information, $(1-\delta)H_{\mathcal S}$; "$R_\delta$ is the number of times one can acquire $(1-\delta)$ of the information about $\mathcal S$ independently (from distinct $\mathcal F$'s) and indirectly – without perturbing $\mathcal S$." "Large redundancy implies objectivity: The state of the system can be found out indirectly and independently by many observers, who will agree about their conclusions" (Fig. 2 caption).

The copying argument (Sec. III). If states $|u\rangle,|v\rangle$ of $\mathcal S$ imprint on a subsystem $|e_0\rangle$ without being perturbed ($|u\rangle|e_0\rangle\Rightarrow|u\rangle|e_u\rangle$, $|v\rangle|e_0\rangle\Rightarrow|v\rangle|e_v\rangle$), unitarity gives

$$\langle u|v\rangle=\langle u|v\rangle\langle e_u|e_v\rangle \qquad (5)$$

so either $\langle e_u|e_v\rangle=1$ (no copy) or $\langle u|v\rangle=0$: "only sets of orthogonal states ... can be so copied." The paper stresses this "relies on just two values of the scalar product – 0 and 1 – and, thus, does not appeal to Born's rule." The branching state:

$$|\Psi_{\mathcal{SE}}\rangle=\sum_k^n\psi_k|s_k\rangle|e^{(1)}_k\rangle\cdots|e^{(\mathcal N)}_k\rangle=\sum_k^n\psi_k|s_k\rangle|\varepsilon_k\rangle \qquad (6)$$

with branch fragments nearly orthogonal, $\prod_{j=1}^J\langle e^{(j)}_k|e^{(j)}_{k'}\rangle\simeq\delta_{kk'}$ for $J$ large but $J\ll\mathcal N$. "Branching state is, to a good approximation, a multi-system Schmidt decomposition ... $|s_k\rangle$ implies $|\varepsilon_k\rangle$ (and, vice versa), and measuring a branch fragment $\mathcal F$ can reveal the whole branch." Collapse is read as this transition from uncertainty to certainty: "brief compared to the ensuing period of certainty about the outcome, as $f_\delta\ll1$, but, nevertheless, not instantaneous." A theorem (refs. [12], [24] = Ollivier, Poulin and Zurek 2004, 2005) is cited: "only pointer states can be discovered from fractions of $\mathcal E$."

Envariance (Sec. IV): a unitary $u_{\mathcal S}$ on $\mathcal S$ whose effect can be undone by $u_{\mathcal E}$ on $\mathcal E$,

$$u_{\mathcal S}\otimes\mathbf 1_{\mathcal E}|\Psi_{\mathcal{SE}}\rangle=|\Phi_{\mathcal{SE}}\rangle;\quad \mathbf 1_{\mathcal S}\otimes u_{\mathcal E}|\Phi_{\mathcal{SE}}\rangle=|\Psi_{\mathcal{SE}}\rangle \qquad (7)$$

From it the paper derives equiprobability for equal $|\psi_k|$ and then Born's rule $p_k=|\psi_k|^2$ by "finegraining" (the Box; a controlled-not from $\mathcal E$ onto an ancilla $\mathcal C$). Note the paper's rule for its own derivation: "Born's rule and standard tools of decoherence are off limits – using them courts circularity."

Models quoted (Sec. II, Fig. 3). Spin $\mathcal S$ with $N=50$ environment spins, $\mathbf H_{\mathcal{SE}}=\sum_{k=1}^N g_k\,\sigma_z^{\mathcal S}\otimes\sigma_y^{\mathcal E_k}$, initial state $\tfrac1{\sqrt2}(|0\rangle+|1\rangle)\otimes|0\rangle^{\otimes N}$, couplings random in $(0,1]$; redundancy $R_{\delta=0.1}$ "is sharply peaked around the pointer observable" (ref. [12]). In the spin family "the same number of spins suffices to reach the plateau: Adding more spins to $\mathcal E$ only extends length of the plateau ... redundancy is then proportional to the number of the environment subsystems that interact with the system." Quantum Brownian motion (underdamped): $I(\mathcal S{:}\mathcal F)\approx H_{\mathcal S}+\tfrac12\ln\frac{f}{1-f}$ and $R_\delta\approx s^{2\delta}$ for squeeze factor $s$ (refs. [15], [16], to verify the numbers against those papers).

**Stated assumptions and limitations, in its words.**
- Fragments must be "individually accessible"; "observables of different subsystems commute" (Fig. 1).
- "Quantum Darwinism does not require pure $\mathcal E$. Mixed environment is a noisy communication channel ... a bit gained from $\mathcal E$ yields only $1-h$ of a bit about $\mathcal S$. So, a completely mixed $\mathcal E$ ($h=1$) is useless (even though it can still induce decoherence!)." A partly mixed $\mathcal E$ "can still climb the same redundancy plateau at $H_{\mathcal S}$" but needs "a proportionally larger fragment."
- The channel must give "direct and easy access to the records": photons are ideal because "they interact with various systems, but, in effect, do not interact with each other"; air molecules "scatter from one another, so that whatever record they may have gathered becomes effectively undecipherable."
- "Correlations that reveal coherence can be usually detected only by such global measurements of whole $\mathcal{SE}$. We intercept small fractions of $\mathcal E$, and never have the luxury of perfect global measurements needed to undo decoherence."
- For the Born-rule derivation, three explicit "facts of life" are assumed: (1) a system not acted on by a unitary keeps its state; (2) predictions about $\mathcal S$ follow from the state of $\mathcal S$; (3) the state of $\mathcal S$ is determined by the state of $\mathcal{SE}$ (Sec. IV).
- On interpretation: "Relative states of Everett come to mind. One could speculate about reality of branches with other outcomes. We abstain from this – our discussion is interpretation-free, and this is a virtue. ... there is only one copy of the Universe. Treating its state as if it really existed seems unwarranted and 'classical'" (Sec. III, end).
- On permanence (Sec. V): "as the Universe has a finite memory, old events will be eventually 'overwritten' by new ones, so that some of the past will gradually cease to be reflected in the present record. And if there is no record of an event, has it really happened?"

**Criticisms cited.** On envariance: "Discussion of the implications of envariance has already started, with [36, 37], and [5] providing insightful commentary": Schlosshauer and Fine, Found. Phys. 35, 197 (2005); Barnum, arXiv:quant-ph/0312150 (2003); Schlosshauer's 2007 book. The paper does not state what they object to; not read by us (to verify).

---

## 2. [ZZ17] M. Zwolak and W. H. Zurek, "Redundancy of einselected information in quantum Darwinism: The irrelevance of irrelevant environment bits"

**Bibliographic.** Phys. Rev. A **95**, 030101(R) (2017), DOI 10.1103/PhysRevA.95.030101. Read as arXiv:1703.10096 (v1, 29 March 2017, "5 pages, 0 figures"), https://arxiv.org/abs/1703.10096 and https://arxiv.org/pdf/1703.10096, plus the ar5iv rendition. **Read in full.**

**Question.** If many environment subsystems carry no information about $\mathcal S$ ("chaff"), does mixing them with the informative ones ("wheat") dilute redundancy? Model (ref. Blume-Kohout and Zurek 2005): $\sharp\mathcal E_G$ "good" spins each holding a perfect record and $\sharp\mathcal E_B$ "bad" spins holding none,

$$\Big(\tfrac1{\sqrt2}|0\rangle_{\mathcal S}\,\overbrace{|0\cdots0\rangle}^{\mathcal E_G}+\tfrac1{\sqrt2}|1\rangle_{\mathcal S}\,\overbrace{|1\cdots1\rangle}^{\mathcal E_G}\Big)\overbrace{|0\cdots0\rangle}^{\mathcal E_B}. \qquad (1)$$

Generated by "pure decoherence": $\mathbf H=\mathbf H_{\mathcal S}+\hat\Pi_{\mathcal S}\sum_k\Upsilon_k+\sum_k\Omega_k$ with $[\hat\Pi_{\mathcal S},\mathbf H_{\mathcal S}]=0$ and product initial state $\rho(0)=\rho_{\mathcal S}(0)\otimes\bigotimes_k\rho_k(0)$; e.g. a $g_k\sigma^z_{\mathcal S}\sigma^z_k$ coupling with $g_k=1$ on $\mathcal E_G$, $0$ on $\mathcal E_B$. "Under pure decoherence, no transitions occur between the pointer states."

**Definitions and equations.**

$$I(\mathcal S{:}\mathcal F)=H_{\mathcal S}+H_{\mathcal F}-H_{\mathcal{SF}} \qquad (2)$$
$$I(\mathcal S{:}\mathcal F)=\chi(\Pi_{\mathcal S}{:}\mathcal F)+\mathcal D(\Pi_{\mathcal S}{:}\mathcal F) \qquad (3)$$

"The Holevo quantity, $\chi(\Pi_{\mathcal S}{:}\mathcal F)$, gives the maximum classical information available about $\Pi_{\mathcal S}$ in $\mathcal F$, while the quantum discord $\mathcal D(\Pi_{\mathcal S}{:}\mathcal F)$ is what remains." Redundancy is defined on the Holevo quantity of the pointer basis $\hat\Pi_{\mathcal S}$: the fragment size $\sharp\mathcal F_\delta$ such that

$$\langle\chi(\hat\Pi_{\mathcal S}{:}\mathcal F)\rangle_{\sharp\mathcal F_\delta}\simeq(1-\delta)H_{\mathcal S}, \qquad (4)\qquad\qquad R_\delta=\frac{\sharp\mathcal E}{\sharp\mathcal F_\delta}. \qquad (5)$$

"The information deficit, $\delta$, is the amount of information that observers are prepared to forgo." Asymptotics:

$$\chi(\hat\Pi_{\mathcal S}{:}\mathcal F)\sim H_{\mathcal S}-H(P_e), \qquad (6)\qquad P_e\sim\exp[-\bar\xi_{QCB}\,\sharp\mathcal F], \qquad (7)$$
$$\bar\xi_{QCB}=-\ln\big\langle\mathrm{tr}\big[\rho^{\,c}_{k|1}\rho^{\,1-c}_{k|2}\big]\big\rangle_{k\in\mathcal E} \qquad (8)\qquad\Rightarrow\qquad R_\delta\simeq\sharp\mathcal E\,\frac{\bar\xi_{QCB}}{\ln 1/\delta}. \qquad (9)$$

$P_e$ is the error probability for distinguishing the fragment's conditional states $\langle\hat s|\rho_{\mathcal{SF}}|\hat s\rangle/p_{\hat s}$; $\bar\xi_{QCB}$ is the "typical" Chernoff information; for pure-decoherence spin models $c=\tfrac12$. **Main result.** In the worst case $\sharp\mathcal E_B\gg\sharp\mathcal E_G,\sharp\mathcal F$, Eq. (10) gives $\bar\xi_{QCB}\simeq\sharp\mathcal E_G/\sharp\mathcal E$ and

$$R_\delta\simeq\frac{\sharp\mathcal E_G}{\ln 1/\delta}, \qquad (11)$$

valid when $\sharp\mathcal E_G\ge\ln(1/\delta)$. The exact calculation agrees: the probability that a fragment of $\sharp\mathcal F$ spins contains only bad bits is

$$P_B=\frac{\sharp\mathcal E_B}{\sharp\mathcal E}\cdot\frac{\sharp\mathcal E_B-1}{\sharp\mathcal E-1}\cdots\frac{\sharp\mathcal E_B-(\sharp\mathcal F-1)}{\sharp\mathcal E-(\sharp\mathcal F-1)}, \qquad (12)$$
$$\big\langle\chi(\hat\Pi_{\mathcal S}{:}\mathcal F)\big\rangle_{\sharp\mathcal F}=H_{\mathcal S}(1-P_B)=1-\frac{\sharp\mathcal E_B!\,(\sharp\mathcal E-\sharp\mathcal F)!}{(\sharp\mathcal E_B-\sharp\mathcal F)!\,\sharp\mathcal E!}\quad(H_{\mathcal S}=1), \qquad (13)$$

and with Stirling, $\ln\delta\simeq-\sharp\mathcal F_\delta\,\sharp\mathcal E_G/\sharp\mathcal E_B$, so

$$R_\delta=\frac{\sharp\mathcal E}{\sharp\mathcal F_\delta}\simeq\frac{\sharp\mathcal E_G}{\ln 1/\delta}. \qquad (15)$$

The alternative definition, "the maximum number of disjoint fragments for which $\chi\simeq(1-\delta)H_{\mathcal S}$," gives $R_\delta=\sharp\mathcal E_G$ for any $\delta\ne1$. The two "are thus not equivalent. However, they only differ by a factor of $\ln 1/\delta$." Imperfect records: good spins with decoherence factor $|\gamma_G|^2$, bad with $|\gamma_B|^2$,

$$R_\delta\simeq\frac{\sharp\mathcal E\,\ln\!\big[\frac{\sharp\mathcal E_B}{\sharp\mathcal E}|\gamma_B|^2+\frac{\sharp\mathcal E_G}{\sharp\mathcal E}|\gamma_G|^2\big]}{\ln\delta}, \qquad (16)$$

using $\mathrm{tr}\,\rho^{c}_{k|1}\rho^{1-c}_{k|2}=|\gamma_k|^2$ for pure states. For $|\gamma_B|^2=1$: $R_\delta\simeq\sharp\mathcal E_G(1-|\gamma_G|^2)/\ln(1/\delta)$ (18) against $R_\delta\simeq\sharp\mathcal E_G\ln|\gamma_G|^2/\ln\delta$ (19) from the maximization; their ratio (20) is at least $(1-\delta)/\ln(1/\delta)$ (22), "essentially $1/\ln 1/\delta$." Also stated (unnumbered, for pure states with $p_0=p_1=\tfrac12$): $\chi(\hat\Pi_{\mathcal S}{:}\mathcal F)=H\!\Big(\tfrac{1+|\gamma_G|^{\sharp\mathcal F-\sharp\mathcal F_B}|\gamma_B|^{\sharp\mathcal F_B}}{2}\Big)$ with $H$ the binary entropy; the $p_0\ne p_1$ form is in Zwolak, Quan and Zurek, PRA 81, 062110 (2010) (not read).

**Stated assumptions and limitations.** Pure decoherence with $[\hat\Pi_{\mathcal S},\mathbf H_{\mathcal S}]=0$ and a product initial state ("approximate the case where decoherence is strong compared to the natural dynamics of the system"); permutational invariance of $\mathcal E_G$ for the QCB shortcut (extension to mixed or non-invariant states is "straightforward" but changes the exponent); Eq. (9) "is an asymptotic lower bound to the redundancy, but ... within a factor of 2 of the exact result" (footnote 2); Eq. (11) fails when $\sharp\mathcal E_G<\ln(1/\delta)$; the maximization definition is "more appropriate" when $\delta$ is close to 1. Generality claim: "except for states of measure zero (i.e., completely mixed initial environment states or ones that commute with the Hamiltonian), redundancy is always present." **Criticisms cited:** none; Brandão, Piani and Horodecki, Nat. Commun. 6, 7908 (2015) is cited as support that "the emergence of the classical, objective reality is unavoidable."

---

## 3. [Zurek03] W. H. Zurek, "Decoherence, einselection, and the quantum origins of the classical" (in part)

**Bibliographic.** Rev. Mod. Phys. **75**, 715–775 (2003), DOI 10.1103/RevModPhys.75.715. Read as arXiv:quant-ph/0105127 v3 (19 June 2003; the comments field calls it the final version, matching the RMP text "apart from editorial changes"), https://arxiv.org/abs/quant-ph/0105127 and https://arxiv.org/pdf/quant-ph/0105127 (71 pages), plus the ar5iv rendition. Equation numbers are section-style, as the paper cross-references them.

### 3.1 Sections read and skipped

**Read:** I (Introduction, all of I.1–I.4: Hilbert space is big; Copenhagen; Many Worlds; decoherence and einselection; envariance preview; existential interpretation and quantum Darwinism); II.1 (quantum conditional dynamics: II.1.1 controlled-not, II.1.2 controlled shifts, II.1.3 amplification, including footnote 3 on recurrences); IV intro, IV.1 (models of einselection: IV.1.1 single qubit, IV.1.2 classical domain and quantum halo, IV.1.3 controlled shifts), IV.2 and IV.2.1 (selective loss of information; mutual information and discord), IV.4 (predictability sieve); VI.1 (objective existence), VI.2 (measurements and memories); VII in full (environment as a witness: VII.1–VII.1.4 quantum Darwinism, redundancy, redundancy rate; VII.2 observers and the existential interpretation; VII.3 events, records and histories; VII.3.1 relatively objective past); IX (concluding remarks).

**Skipped:** II.2–II.3 (information transfer; classical "collapse" analogue); III (chaos and loss of correspondence); IV.3 (decoherence, entanglement, dephasing, noise); V (einselection in phase space, quantum Brownian motion); VI.3–VI.4 (axioms of measurement; probabilities from envariance); VIII (decoherence in the laboratory). Figure captions were not recoverable from the compressed PDF; Fig. 4 is described below only through the body text that refers to it.

### 3.2 The preferred-basis problem (I.1, I.3)

The premeasurement $|\Psi_t\rangle=\sum_i a_i|s_i\rangle|A_i\rangle=\sum_i b_i|r_i\rangle|B_i\rangle$ (Eqs. (2.1)–(2.2)) can be rewritten in any basis: "basis ambiguity." On Everett: "the original MWI does not address the 'preferred basis question' ... And as long as it is unclear what singles out preferred states, perception of a unique outcome of a measurement and, hence, of a single Universe cannot be explained either" (I.1.2, with DeWitt's own admission quoted in footnote 2). "MWI is incomplete: It does not explain what is effectively classical and why." The review's position: "Decoherence and einselection fit comfortably in the context of the Many Worlds Interpretation where they define the 'branches' of the universal state vector. Decoherence makes MWI complete"; and "Einselection fits either MWI or CI framework" (I.3). Critics of MWI it points to: Wheeler 1983, Stein 1984, Bell 1981/1987, Kent 1990.

### 3.3 The measurement model: c-not and controlled shift (II.1)

Classical c-not, Eq. (2.3); quantum c-not, $(\alpha|0_c\rangle+\beta|1_c\rangle)|a_t\rangle\to\alpha|0_c\rangle|a_t\rangle+\beta|1_c\rangle|\neg a_t\rangle$ (2.4), "a 'bit by bit measurement' (Zurek, 1981; 1983)." In the conjugate basis $|\pm\rangle=(|0\rangle\pm|1\rangle)/\sqrt2$ (2.6) the roles reverse: $|\pm\rangle|+\rangle\to|\pm\rangle|+\rangle$, $|\pm\rangle|-\rangle\to|\mp\rangle|-\rangle$ (2.7)–(2.8): "the apparatus is measured by the system"; phases "are not really destroyed, but, rather ... become 'shared property'." Hamiltonian $H_{int}=g|1\rangle\langle1|_{\mathcal S}|-\rangle\langle-|_{\mathcal A}$ (2.9), c-not at $gt=\pi/2$; the measured observable commutes with $H_{int}$ (2.10). Controlled shift: $|s_j\rangle|A_k\rangle\to|s_j\rangle|A_{k+j}\rangle$ (2.13); conjugate basis $|B_k\rangle=N^{-1/2}\sum_{l=0}^{N-1}e^{2\pi ikl/N}|A_l\rangle$ (2.14a); $H_{int}=g\hat s\hat B$ (2.19) with $\hat s=\sum_l l|s_l\rangle\langle s_l|$ (2.20), $\hat B=\frac{iN}{2\pi}\frac{\partial}{\partial\hat A}$ (2.21); for action $\iota=gt/\hbar=G\cdot2\pi/N$ (2.23a), $e^{-iH_{int}t/\hbar}|s_j\rangle|A_k\rangle=|s_j\rangle|A_{\{k+Gj\}_N}\rangle$ (2.23b), $G$ the gain. Reversibility (footnote 3): entangling time $t_e=2\pi\hbar/(gN)$, recurrence $t_{Rec}=Nt_e=2\pi\hbar/g$ for a c-shift, "$\sim N!\,t_e$" for irregular spectra; undoing needs isolation from further environments, $g_{\mathcal{EE}'}<g/N'$ (regular) or $g/(N!N')$ (random): "keeping it from spreading further ranges between very hard and next to impossible."

### 3.4 Einselection, exactly solvable (IV.1–IV.2, IV.4)

The $\mathcal{SAE}$ "triangle": $\mathcal S$ and $\mathcal A$ entangle, then "$\mathcal A$ and $\mathcal E$" interaction turns entanglement into classical correlation. Three one-bit systems: $|\!\uparrow\rangle|A_0\rangle\to|\!\uparrow\rangle|A_1\rangle$, $|\!\downarrow\rangle|A_0\rangle\to|\!\downarrow\rangle|A_0\rangle$ (4.1); then

$$(\alpha|\!\uparrow\rangle|A_1\rangle+\beta|\!\downarrow\rangle|A_0\rangle)|\varepsilon_0\rangle\to\alpha|\!\uparrow\rangle|A_1\rangle|\varepsilon_1\rangle+\beta|\!\downarrow\rangle|A_0\rangle|\varepsilon_0\rangle=|\Psi\rangle \qquad (4.3)$$

and if $\langle\varepsilon_0|\varepsilon_1\rangle=0$ (4.4), $\rho_{\mathcal{AS}}=\mathrm{Tr}_{\mathcal E}|\Psi\rangle\langle\Psi|=|\alpha|^2|\!\uparrow\rangle\langle\uparrow\!||A_1\rangle\langle A_1|+|\beta|^2|\!\downarrow\rangle\langle\downarrow\!||A_0\rangle\langle A_0|$ (4.5a), "containing only classical correlations"; the pre-decoherence $|\Phi\rangle\langle\Phi|$ (4.5b) has the off-diagonal terms $\alpha\beta^*|\!\uparrow\rangle\langle\downarrow\!||A_1\rangle\langle A_0|+$ h.c. Pointer basis: $[H_{\mathcal{AE}},\hat A]=0$ (4.6), generally $[H_{\mathcal{AE}}(A),A]=0$ (4.22).

**The single-qubit model (IV.1.1; Zurek 1982).** $H_{\mathcal A}=0$,

$$H_{\mathcal{AE}}=(|\!\Uparrow\rangle\langle\Uparrow\!|-|\!\Downarrow\rangle\langle\Downarrow\!|)\otimes\sum_k g_k(|\!\uparrow\rangle\langle\uparrow\!|-|\!\downarrow\rangle\langle\downarrow\!|)_k, \qquad (4.7)$$
$$|\Phi(0)\rangle=(a|\!\Uparrow\rangle+b|\!\Downarrow\rangle)\prod_{k=1}^N(\alpha_k|\!\uparrow\rangle_k+\beta_k|\!\downarrow\rangle_k) \qquad (4.8)$$
$$|\Phi(t)\rangle=a|\!\Uparrow\rangle|\mathcal E_\Uparrow(t)\rangle+b|\!\Downarrow\rangle|\mathcal E_\Downarrow(t)\rangle, \qquad (4.9)\qquad |\mathcal E_\Uparrow(t)\rangle=\prod_{k=1}^N(\alpha_ke^{ig_kt}|\!\uparrow\rangle_k+\beta_ke^{-ig_kt}|\!\downarrow\rangle_k)=|\mathcal E_\Downarrow(-t)\rangle \qquad (4.10)$$
$$\rho_{\mathcal A}=|a|^2|\!\Uparrow\rangle\langle\Uparrow\!|+ab^*r(t)|\!\Uparrow\rangle\langle\Downarrow\!|+a^*br^*(t)|\!\Downarrow\rangle\langle\Uparrow\!|+|b|^2|\!\Downarrow\rangle\langle\Downarrow\!| \qquad (4.11)$$
$$r(t)=\langle\mathcal E_\Uparrow|\mathcal E_\Downarrow\rangle=\prod_{k=1}^N\big[\cos2g_kt+i(|\alpha_k|^2-|\beta_k|^2)\sin2g_kt\big] \qquad (4.12)$$

"The coefficient $r(t)$ ... determines the relative size of the off-diagonal terms." At large times $|r(t)|^2\simeq2^{-N}\prod_k[1+(|\alpha_k|^2-|\beta_k|^2)^2]$ (4.13); in general $r(t)=\sum_{j=1}^{2^N}p_j e^{-i\Delta\omega_jt}$ (4.14), $\langle|r(t)|^2\rangle\sim\sum_jp_j^2\sim2^{-N}$ (4.16): "decoherence is exponentially effective." Caveat in its words: "the effectiveness of einselection depends on the initial state of the environment: When $\mathcal E$ is in the $k$'th eigenstate of $H_{\mathcal{AE}}$, $p_j=\delta_{jk}$, the coherence in the system will be retained. This special environment state is, however, unlikely in realistic circumstances." Decoherence "does not affect $|a|$ or $|b|$."

**Controlled shifts (IV.1.3).** $(\sum_j\alpha_j|s_j\rangle|A_j\rangle)|\varepsilon_0\rangle\to\sum_j\alpha_j|s_j\rangle|A_j\rangle|\varepsilon_j\rangle$ (4.18); einselection when $\langle\varepsilon_i|\varepsilon_j\rangle=\delta_{ij}$ (4.19); $\rho^D_{\mathcal{SA}}=\sum_j|\alpha_j|^2|s_j\rangle\langle s_j||A_j\rangle\langle A_j|$ (4.20). Fig. 4 (per the text) is "the idealized decoherence process" as "a sequence of c-shifts" that leaves $\mathcal A$ "a noiseless classical communication channel"; the caveats: real decoherence is continuous, the record "is usually distributed over many degrees of freedom," and self-Hamiltonians may rotate pointer states. "Instantaneous diagonality [of the Schmidt basis] should not be used the sole criterion for classicality ... ability of certain states to retain correlations in spite of the coupling to the environment is decisive."

**Selective loss of information (IV.2.1).** Mutual information falls from $\mathcal I^P(\mathcal S{:}\mathcal A)=-2\sum_i|\alpha_i|^2\lg|\alpha_i|^2$ (4.30a) to $\mathcal I^D=-\sum_i|\alpha_i|^2\lg|\alpha_i|^2$ (4.30b), "at most half its initial value," the loss equal to the entropy increase (4.31). The asymmetric form $\mathcal J_{\mathcal A}(\mathcal S{:}\mathcal A)=H(\rho_{\mathcal S})-H(\rho_{\mathcal S|\mathcal A})$ (4.32) would need a negative conditional entropy before decoherence; the discord $\delta\mathcal I_{\mathcal A}(\mathcal S|\mathcal A)=\mathcal I-\mathcal J_{\mathcal A}$ (4.36) "must vanish: Unless $\delta\mathcal I_{\mathcal A}=0$, probabilities of the distinct apparatus pointer states cannot exist." (This is the von Neumann vs. locally accessible split that [ZZ17] Eq. (3) uses.)

**Predictability sieve (IV.4).** Exact pointer states when $[H_{\mathcal A}+H_{\mathcal{AE}},P_A]=0$ (4.41); otherwise rank pure states by entropy or purity $\varsigma_\Psi(t)=\mathrm{Tr}\rho^2_\Psi(t)$ (4.42) and take the top: "The idea of the 'sieve' ... is novel and only partly explored." "There is no a priori reason to expect that all of these criteria [entropy, purity, redundancy] will lead to identical sets of preferred states."

### 3.5 Objective existence, memories, the existential interpretation (VI.1–VI.2, I.4, VII.2)

Operational definition (VI.1): a record keeper R and a spy S; a state "exists objectively" when S "can consistently find out the state of the system without changing it," which einselection makes possible, and "indirect measurements ... is in fact more or less the only strategy employed by the observers." After einselection, projections onto the pointer basis leave the density matrix unchanged: $\rho^D_{after}=\sum_iP_i\rho^D_{before}P_i$ (6.1). Memory (VI.2) is "an open quantum $\mathcal A$" coupled by $H_{int}=-g\hat s\hat B$ (6.2); "Only the einselected memory states (rather than their superpositions) will be useful for (or, for that matter, accessible to) the observer," with the timescale ordering decoherence $\ll$ consultation $\ll$ relaxation. Existential interpretation (I.4, VII.2): "What the observer knows is inseparable from what the observer is"; "there can be no information without representation in physical states"; "Distinct memory states label and 'inhabit' different branches of the Everett's 'Many Worlds' Universe"; and the limit on the claim: "Here we are using aware in a down-to-earth sense: Quite simply, observers know what they know"; "The 'higher functions' of observers – e.g., consciousness, etc. – may be at present poorly understood, but it is safe to assume that they reflect physical processes in the information processing hardware of the brain."

### 3.6 Environment as a witness; records and histories (VII)

$$|\psi_{\mathcal{SE}}\rangle=a|\!\uparrow\rangle|00\ldots0\rangle+b|\!\downarrow\rangle|11\ldots1\rangle=a|\!\uparrow\rangle|\mathcal E_\uparrow\rangle+b|\!\downarrow\rangle|\mathcal E_\downarrow\rangle \qquad (7.1)$$

In the Hadamard-rotated basis $\{|\odot\rangle,|\otimes\rangle\}$ of $\mathcal S$ the same state is (7.2), with environment states that "are typically not even orthogonal, $\langle\mathcal E_\odot|\mathcal E_\otimes\rangle=|a|^2-|b|^2$," and whose record is "fragile: Only one relative phase distinguishes" them. Three fitness measures: algorithmic simplicity of the record, $K(\langle\mathcal E_n|0,1\rangle)\ll n$ against $K(\langle\mathcal E_n|+,-\rangle)\simeq n$ (7.3)–(7.4); action distance, $\Delta(|\mathcal E_\uparrow\rangle,|\mathcal E_\downarrow\rangle)=N[\tfrac\pi2\hbar]$ against $1[\tfrac\pi2\hbar]$ (7.5)–(7.6), a metric (7.7)–(7.9); and redundancy. For perfect correlation the redundancy ratio is $\mathcal R=\lg(\mathrm{Dim}\,\mathcal H_{\mathcal E})/\lg(\mathrm{Dim}\,\mathcal H_{\mathcal S})=N$ (7.10). Generally, with $\mathcal I_k=\mathcal I(\mathcal S{:}\mathcal E_k)=H(\mathcal S)+H(\mathcal E_k)-H(\mathcal S,\mathcal E_k)$ (7.11), $\rho_{\mathcal{SE}_k}=\mathrm{Tr}_{\mathcal E/\mathcal E_k}\rho_{\mathcal{SE}}$ (7.12), and in the example $\rho_{\mathcal{SE}_k}=|a|^2|\!\uparrow\rangle\langle\uparrow\!|\,|0\rangle\langle0|+|b|^2|\!\downarrow\rangle\langle\downarrow\!|\,|1\rangle\langle1|$ for every bit (unnumbered),

$$\mathcal R_{\mathcal I}=\sum_k\mathcal I(\mathcal S{:}\mathcal E_k)/H(\mathcal S) \qquad (7.13)$$

maximized over partitions (7.14); the basis-dependent version uses $\mathcal J_k$ (7.15), $\mathcal R_{\mathcal J}(\{|s\rangle\})$ (7.16), and pointer states are those with $\mathcal R_{\mathcal J\max}=\mathcal R_{\mathcal J}(\{|p\rangle\})\gg\mathcal R_{\mathcal J}(\{|s\rangle\})$ (7.18); $\mathcal R_{\mathcal J\max}\le\mathcal R_{\mathcal I\max}$ (7.19); redundancy rate $\dot{\mathcal R}=\frac{d}{dt}\mathcal R$ (7.20), which in the c-not model is the number of c-nots per unit time; after one c-not "$\mathcal R_{\mathcal I}$ will jump immediately from 0 to 2 bits, while the basis-specific $\mathcal R_{\mathcal J}$ will increase from 0 to 1" (discord), reconciled after the second. "The record size – the number $N$ of the subsystems of the environment involved – does not affect the density matrix of the system $\mathcal S$." Consensus: "many ($\sim N/n$) can independently measure fragments of the environment" (VII.1.1).

Histories (VII.3). A record $000\ldots0111\ldots1000\ldots0111\ldots$ "justif[ies] inference of the history of the system"; other observers "will infer (more or less) the same history." Consistent histories are defined through

$$D([P_\alpha],[P_\beta])=\mathrm{Tr}\big(P^n_{\alpha_n}(t_n)\cdots P^1_{\alpha_1}(t_1)\,\rho\,P^1_{\beta_1}(t_1)\cdots P^n_{\beta_n}(t_n)\big) \qquad (7.21)$$

with Griffiths' condition $\mathrm{Re}\,D=p_\alpha\delta_{\alpha\beta}$ and Gell-Mann and Hartle's $D=p_\alpha\delta_{\alpha\beta}$. The review's critique: "the resulting histories are very subjective: Given an initial density matrix of the Universe it is in general quite easy to specify many different, mutually incompatible consistent sets of histories" (citing d'Espagnat 1989, 1995; Dowker and Kent 1996); "consistency is both not enough and too much – it is too easy to accomplish, and does not necessarily lead to classicality"; "What is needed instead is the objectivity of events and their time-ordered sequences – histories. As we have seen above, both can appear as a result of einselection." Relatively objective past (VII.3.1): "The number of observers who can examine evidence etched in the environment can be of the order of, and is bounded from above by $\mathcal R_{\mathcal J}$"; an observer who records the right observable adds to $\mathcal R_{\mathcal J}$; "A measurement reveals to the observer 'his' branch of the universal state vector ... He will share it with other observers who examined the same set of observables, and who have recorded compatible results." A "stubborn observer" measuring the phase between the two branches leaves the bits' correlations and so the evidence of the past, but "measurement of all the environment bits in the $\{|+\rangle,|-\rangle\}$ basis will obliterate evidence of such a past." "relative objectivity tends to absolute objectivity in the limit $\mathcal R\to\infty$." Closing dictum (Wheeler's): "The past exists only insofar as it is recorded in the present."

### 3.7 Limitations and criticisms in the review's own words

"Many conceptual and technical issues (such as what constitutes 'a system') are still open" (IX). On acceptance: being called "the new orthodoxy" (Bub 1997) "suggests that the interpretation ... is both complete and widely accepted. Neither is certainly the case" (IX). Critics of decoherence it names: d'Espagnat 1989, 1995; Bub 1997; Leggett 1998, 2002; Stapp 2001; Adler 2001 (I.2). The quantum-Darwinism and envariance material is labeled "rather new, and a subject of research, hence the word 'preview'" (IX). The review's own cautions: einselection depends on the environment's initial state (IV.1.1); recurrences exist and are only rare for large $N$ (II.1.3); different sieves need not agree (IV.4).

---

## 4. The benchmark model for Stage B

**Model (from [Zurek03] IV.1.1, Eqs. (4.7)–(4.12); the c-not limit is [Zurek03] Eq. (7.1) and [Zurek09] Eq. (6)).** One qubit $\mathcal S$ (the review calls it $\mathcal A$) coupled to $N$ qubits by Eq. (4.7) from the product state (4.8). Everything is closed-form:

- Global state: Eq. (4.9) with branch states (4.10).
- Reduced state of the qubit: Eq. (4.11), with decoherence factor (4.12). Coherence is $|ab^*r(t)|$; the interference visibility of a balanced interferometer on $\mathcal S$ is $V=|r(t)|=|\langle\mathcal E_\Uparrow|\mathcal E_\Downarrow\rangle|$, the handoff's formula; for $|a|\ne|b|$ it is $V=2|a||b||r(t)|$ (ours, textbook; to verify).
- Perfect record at a single environment qubit $k$ when $\alpha_k=\beta_k=1/\sqrt2$ and $2g_kt=\pi/2$ (its factor in (4.12) is $\cos(\pi/2)=0$); with all $g_k=g$ this is the c-not time, giving the GHZ-type state (7.1) up to local rotations (ours, from (4.10)).
- Exact recoherence: with all $g_k=g$ (any $\alpha_k,\beta_k$), Eq. (4.12) gives $r(\pi/2g)=(-1)^N$, so $|r|=1$: the toy recoheres completely at $t=\pi/(2g)$. This is the review's footnote-3 recurrence ($t_{Rec}=2\pi\hbar/g$ for a c-shift). Ours, exact from (4.12). A Stage B toy with commensurate couplings *will* show this; it is a size and spectrum artifact, not the quantum eraser.

**Mutual information and redundancy, closed form.** Write the state as $a|0\rangle\bigotimes_k|e^k_0\rangle+b|1\rangle\bigotimes_k|e^k_1\rangle$ with per-qubit overlaps $\gamma_k=\langle e^k_0|e^k_1\rangle$ and $\Gamma_X=\prod_{k\in X}\gamma_k$ (so $r(t)=\Gamma_{\mathcal E}$ in (4.12)). Let $p=|a|^2$ and $h(x)=-x\lg x-(1-x)\lg(1-x)$. Then (ours, unverified; a two-line Schmidt argument, to verify against Blume-Kohout and Zurek 2005, which treats this model):

$$\lambda^{\mathcal S}_\pm=\tfrac12\Big(1\pm\sqrt{(2p-1)^2+4p(1-p)|\Gamma_{\mathcal E}|^2}\Big),\quad \lambda^{\mathcal{SF}}_\pm=\tfrac12\Big(1\pm\sqrt{(2p-1)^2+4p(1-p)|\Gamma_{\mathcal E/\mathcal F}|^2}\Big),\quad \lambda^{\mathcal F}_\pm=\tfrac12\Big(1\pm\sqrt{1-4p(1-p)(1-|\Gamma_{\mathcal F}|^2)}\Big),$$
$$I(\mathcal S{:}\mathcal F)=h(\lambda^{\mathcal S}_+)+h(\lambda^{\mathcal F}_+)-h(\lambda^{\mathcal{SF}}_+).$$

Checks the toy must pass: $\mathcal F=\varnothing$ gives $I=0$; $\mathcal F=\mathcal E$ gives $I=2H_{\mathcal S}$ ([Zurek09] Fig. 2); perfect records ($\gamma_k=0$) and $1\le|\mathcal F|\le N-1$ give $I=H_{\mathcal S}=h(p)$ exactly, the classical plateau, and $\rho_{\mathcal{SE}_k}$ as in the unnumbered example after (7.12); the Holevo part at $p=\tfrac12$ is $\chi=h\big(\tfrac{1+|\Gamma_{\mathcal F}|}{2}\big)$, which is [ZZ17]'s unnumbered formula (with $|\gamma_G|$, $|\gamma_B|$ for two kinds of bit); redundancy of perfect records is $\mathcal R=N$ ([Zurek03] Eq. (7.10)), and under [ZZ17]'s averaged definition $R_\delta\simeq\sharp\mathcal E_G/\ln(1/\delta)$ (Eq. (15)) against $R_\delta=\sharp\mathcal E_G$ by maximization, with the exact averaged Holevo quantity (13) as the function to reproduce. For nontrivial *disagreement* between observers reading different fragments, the records must be imperfect ($\gamma_k\ne0$); the error probability is [ZZ17] Eqs. (6)–(7), and the agreement rate the handoff wants is then a derived quantity of this model (ours; not defined in the papers).

---

## 5. Mapping table against the handoff

| # | Handoff | Verdict and basis |
|---|---|---|
| 1 | §3 "visibility ... controlled by $V=\lvert\langle E_B\lvert E_A\rangle\rvert$" | **STANDARD** for equal amplitudes: the off-diagonal of $\rho_{\mathcal A}$ is $ab^*r(t)$ with $r=\langle\mathcal E_\Uparrow\lvert\mathcal E_\Downarrow\rangle$ ([Zurek03] (4.11)–(4.12)); copying forces $\langle e_u\lvert e_v\rangle$ to 0 only for orthogonal $\lvert u\rangle,\lvert v\rangle$ ([Zurek09] (5)). "Balanced" is a **SIMPLIFYING ASSUMPTION**; general $V=2\lvert a\rvert\lvert b\rvert\lvert r\rvert$ (ours). |
| 2 | §3 "when information is suitably recombined or erased, interference may be recovered ... not a literal absolute ban" | **STANDARD** in principle: recurrences at $t_{Rec}$ and the conditions to undo them ([Zurek03] II.1.3 fn. 3); undoing needs "global measurements of whole $\mathcal{SE}$" ([Zurek09] II). The papers add what the handoff should keep: realistic undoing is "next to impossible," and a measurement that recovers coherence can "obliterate evidence of such a past" (VII.3.1). |
| 3 | §3 "stable classical records are emergent and approximate" | **STANDARD**: "relatively objective existence ... an operational notion ... not some 'absolute objectivity'" (VII.3.1); collapse "not instantaneous" ([Zurek09] III). |
| 4 | §4 "two observers read and agree on one redundant environmental record ... perfectly correlated even though the global underlying result is probabilistic" | **STANDARD**: the Schmidt structure of (6) means "$\lvert s_k\rangle$ implies $\lvert\varepsilon_k\rangle$"; every bit of (7.1) agrees; observers who record the pointer observable "attach" to the branch and share it (VII.3.1); "many observers can independently deduce the pointer state ... and reach consensus" ([ZZ17] intro). |
| 5 | §4 "Use joint distributions $P(R_A,R_B\mid\alpha)$, not products" | **STANDARD** in content, **SIMPLIFYING** in form: the papers never write a joint distribution over observer registers; they say "consensus." Casting it as $P(R_A,R_B\mid\alpha)$ is the handoff's bookkeeping, correct and not contradicted. |
| 6 | §4 "Quantum Darwinism supplies a framework for ... widely accessible, redundant records ... without independent fundamental collapses" | **STANDARD**: [Zurek09] abstract ("effective 'wave-packet collapse' arises as a result of proliferation ... of imprints"). Caveat: the author is not committing to Everett (section 6, item 1). |
| 7 | Stage B: reduced density matrices, coherence | **STANDARD**: [Zurek09] (1)–(2); [Zurek03] (4.5a), (4.11), (4.20). |
| 8 | Stage B: $I(S{:}F)$ | **STANDARD** ([Zurek09] (3); [Zurek03] (7.11)); the handoff must choose von Neumann (rises to $2H_{\mathcal S}$ at $f\to1$) or Holevo/Shannon (plateaus): a **SIMPLIFYING ASSUMPTION** still to be made ([Zurek09] II; [ZZ17] (3)). |
| 9 | Stage B: "redundancy of copied records" | **STANDARD** quantity; the **choice** of $\delta$ and of definition (averaged (4)–(5) against maximization) changes the number by $\ln(1/\delta)$ ([ZZ17] (11), (15), footnotes 2–3). For perfect records the two agree up to that factor and the simple count is $N$ ([Zurek03] (7.10)). |
| 10 | Stage B: "agreement/disagreement rates of observer reports" | **NOVEL** as a named observable: not in these papers. Nearest: consensus "$\sim N/n$" observers (VII.1.1); the bound by $\mathcal R_{\mathcal J}$ (VII.3.1); the per-fragment error probability $P_e$ ([ZZ17] (6)–(7)), from which such a rate can be built. |
| 11 | Stage B: "controlled recoherence/quantum eraser scenarios" | **STANDARD** in principle (item 2). Two cautions: in a small toy with commensurate couplings recoherence is automatic ([Zurek03] (4.12), section 4 above), so the eraser must be a *designed* operation (e.g. measuring the record bits in the $\{\lvert+\rangle,\lvert-\rangle\}$ basis, VII.3.1), and the papers note that erasing the record also erases the evidence that bears on the handoff's §2 ("if $R_{n+1}$ extends rather than erases"). |
| 12 | Check: "Do not assert permanent classical histories through all time" | **STANDARD**, and the papers go further: "if there is no record of an event, has it really happened?" ([Zurek09] V); "The past exists only insofar as it is recorded in the present" (VII.3.1). |
| 13 | Check: "Do not infer consciousness from a qubit record" | **STANDARD** practice: memory is "an open quantum $\mathcal A$" (VI.2); "aware in a down-to-earth sense"; higher functions "poorly understood" (VII.2). The review's "observer is what he knows" (VII.2) is a stronger philosophical claim the handoff does not need and should not borrow as a result. |
| 14 | Stage D: "duplicating an observer/register changes the assumed anthropic count but not the underlying branch's Born weight" | **STANDARD** in these papers' terms: "Every interaction that increases the number of the records also increases $\mathcal R_{\mathcal J}$" (VII.3.1) while "The record size ... does not affect the density matrix of the system" (VII.1.3). |
| 15 | §2–§3: record surprisal $I(R_n)=-\log_2\mu(\mathcal C(R_n))$; nested compatible sets | **NOVEL CONJECTURE** (or bookkeeping) relative to these papers: nothing like it appears. Do not cite them for it. |
| 16 | §3: decoherence functional $D(\alpha,\beta)$ and Stage C | **STANDARD** definition ([Zurek03] (7.21), Gell-Mann and Hartle), but the review's **critique** of consistency as a criterion (VII.3) is a known position the handoff's Stage A must record (section 6, item 2). |

---

## 6. What contradicts or complicates the handoff

1. **Interpretation.** The handoff commits to Everett (§1.2). [Zurek09] declines: "We abstain from this – our discussion is interpretation-free ... Treating [the universal state vector] as if it really existed seems unwarranted." [Zurek03] I.3 is friendlier ("Decoherence makes MWI complete") but says einselection "fits either MWI or CI framework." So quantum Darwinism may be cited for *how* records become redundant and shared, not for *the reality of other branches*; the handoff's §4 sentence "both outcomes occur across branches" is the handoff's commitment, not the papers'.
2. **Consistent histories.** [Zurek03] VII.3: consistent sets are "very subjective," "consistency is both not enough and too much," and classicality comes from einselection and redundancy instead. The handoff's Stage C is built on $D(\alpha,\beta)$ and its §3 already warns against a unique preferred branch partition; it should add this critique and its later reconciliation (general knowledge, to verify: Riedel, Zurek and Zwolak, "Objective past of a quantum universe: Redundant records of consistent histories," Phys. Rev. A 93, 032126 (2016), which defines histories by redundant records).
3. **Born's rule.** [Zurek09] IV derives it from envariance and forbids itself the use of reduced density matrices beforehand. The handoff takes Born as given and uses $\rho$ throughout (fine for Stage B), but Stage A must not say quantum Darwinism "derives probabilities" without citing envariance together with the commentaries it names (Schlosshauer and Fine 2005; Barnum 2003).
4. **Which mutual information.** Von Neumann $I(S{:}F)$ is antisymmetric and reaches $2H_{\mathcal S}$ at $f\to1$; the Holevo/Shannon version plateaus at $H_{\mathcal S}$ ([Zurek09] II; [ZZ17] (3)). Redundancy read off the von Neumann curve near $f=1$ is misleading. Stage B must declare which it computes.
5. **Two redundancies.** Averaged (fix $\delta$, find $\sharp\mathcal F_\delta$) and maximized (count disjoint sufficient fragments) differ by $\ln(1/\delta)$ ([ZZ17]). Any number the handoff reports needs $\delta$ and the definition stated.
6. **Mixed environments.** Decohere but inform less: a bit of a mixed $\mathcal E$ yields $1-h$ bits about $\mathcal S$; fully mixed yields none ([Zurek09] II). A Stage B register prepared mixed will show decoherence without records.
7. **Recurrences in small toys.** Exact for commensurate couplings ([Zurek03] II.1.3 fn. 3; Eq. (4.12)). A toy of a few qubits overstates impermanence; the realistic statement is $t_{Rec}\sim N!\,t_e$. "Do not assert permanent classical histories" is right, but the toy's reason for impermanence is not the universe's.
8. **Agreement rates need imperfect records.** With perfect records and pointer-basis readout, agreement is exactly 1 within a branch ((7.1)); disagreement arises only from imperfect overlaps $\gamma_k\ne0$ or wrong-basis readout (VII.3.1). The Stage B design should include $\gamma_k\ne0$ or the rate is trivially 1.
9. **Erasure versus the handoff's §2.** The handoff says a record that is erased need not shrink the compatible set and that the surprisal "need not increase if accessible records are erased." [Zurek03] VII.3.1 distinguishes an erasure that leaves the environment's correlations (phase measurement) from one that destroys them (conjugate-basis measurement of all bits). The handoff's Stage C "retained, erased, and shared records" should model both kinds.

---

## 7. Criticisms of quantum Darwinism from outside these papers (general knowledge, to verify; none read)

Named only so the caller can search for them; each is "to verify" and unread. (a) Circularity or extra assumptions: Fields, "Quantum Darwinism requires an extra-theoretical assumption of encoding redundancy" (Int. J. Theor. Phys., 2010); Kastner, "Einselection of pointer observables: The new H-theorem?" (Stud. Hist. Phil. Mod. Phys., 2014). (b) Refinements of the objectivity criterion: "strong quantum Darwinism" and "spectrum broadcast structure" (Le and Olaya-Castro, PRL 2019; Horodecki, Korbicz and Horodecki, PRA 2015), which argue that mutual-information redundancy alone can misdiagnose objectivity. (c) Later closed-form work on the qubit-plus-$N$-qubits model: Touil, Yan, Girolami, Deffner and Zurek, "Eavesdropping on the decohering environment: Quantum Darwinism, amplification, and the origin of objective classical reality," PRL 128, 010401 (2022). (d) The decoherence program's older critics are those [Zurek03] I.2 lists.

---

## 8. Reading record

Files read (scratchpad, not tracked): `agent_zurek/zurek2009/0903.5082.pdf` (6 pp.), `agent_zurek/zwolak2017/1703.10096.pdf` (5 pp.), `agent_zurek/zurek2003/0105127.pdf` (71 pp.); their pypdf text; and ar5iv HTML renditions converted to text with LaTeX kept. Quotations are from the arXiv versions; journal pagination was not checked (to verify). Not read: Blume-Kohout and Zurek 2005, 2006, 2008; Ollivier, Poulin and Zurek 2004, 2005; Zwolak, Quan and Zurek 2009, 2010; Zwolak, Riedel and Zurek 2014, 2016; Schlosshauer and Fine 2005; Barnum 2003; Brandão, Piani and Horodecki 2015; the review's sections listed as skipped in 3.1.

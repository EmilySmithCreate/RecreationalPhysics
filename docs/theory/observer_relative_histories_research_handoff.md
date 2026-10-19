# Observer-Relative Histories in a Level-2 Everettian Universe
**Working theory and coding-bot research handoff — 12 October 2026**

## 0. Purpose and scientific status

**Purpose:** Formalize an intuition about quantum interference, emergent observers, the apparent passage of time, the specificity of recorded histories, and the cosmic-time distribution of observer experiences. Identify which claims already follow from Everettian quantum mechanics and decoherent-histories theory, and which require extra modeling assumptions or yield distinct predictions.

**Status:** A conceptually coherent *interpretive synthesis and proposed modeling program*, not a demonstrated new physical theory. Do not claim a new derivation of the Born rule, consciousness, the arrow of time, or a novel prediction unless calculations independently establish one.

## 1. Explicit scope and core commitments

1. **Level 2 only.** Fix the physical laws, constants, and quantum framework of our universe, denoted by \(\lambda\). A hypothetical larger collection of universes with different laws (Level 1) is outside this analysis. No quantum interference between different-law universes is assumed.
2. **Everett / no fundamental collapse.** The universal quantum state obeys unitary dynamics. All decohered alternatives remain in the global state; records correlate a particular observer state with a particular outcome. An observer does not destroy or select other branches.
3. **No external selector or privileged consciousness.** Observers evolve from physical subsystems within the universe. They acquire, store, process, and exchange records by ordinary physical interactions.
4. **No objectively advancing universal now.** The idea that all complete histories can be represented in a single mathematical structure is a *block-history interpretive picture*, not an experimentally demonstrated extra dimension. Apparent temporal passage is associated with ordered observer states, memories, and the arrow of records. Cosmic time is a useful model coordinate in approximately FLRW cosmologies, not a preferred global present in arbitrary spacetime.
5. **Amplitudes matter.** Quantum possibilities are not equiprobable configurations to be counted. Coherent alternatives have complex amplitudes and can interfere. Probabilities for histories are assigned only for an appropriately decoherent family.
6. **Observers coexist and interact within histories.** They have shared environments, imperfectly shared records, causal encounters, births, deaths, and changing internal states. Their observations are generally correlated; their probabilities must never be multiplied as if independent without justification.
7. **Cosmic time domain.** Start near the Big Bang, currently approximately 13.8 billion years ago, and extend into the era in which ordinary observer-supporting conditions become negligible. Do not require literally all matter to disappear. Use a probabilistic 99.99%-sterility threshold *only if* the history measure and endpoints make it well-defined; it may never be reached under some assumptions.

## 2. Key intuition, stated precisely

An observer exists as a physical subsystem with accumulated records. As an observer acquires and retains distinguishable records, the set of complete decoherent histories compatible with that observer's full recorded sequence becomes a nested subset of its prior compatible set. Its **unconditional Born measure relative to the initial history ensemble** is nonincreasing. **No global branch is destroyed or assigned a lower intrinsic existence because of this conditioning.**

This is not literally a sequence of 'smaller infinities' in the sense of cardinality: strictly nested sets can all remain uncountably infinite. It is a statement about nested subsets and their nonincreasing measure. Normalized **conditional measure within the remaining set** always sums to one.

A decrease in the measure of a particular recorded history does **not** by itself imply that observer-moments are more probable at early cosmic times. Earlier and later distributions require an explicit observer reference class, observer-production model, spacetime sampling domain, and self-location/typicality assumption.

## 3. Quantum foundation

Let \(\mathcal H_\lambda\) be the Hilbert space associated with fixed physical laws \(\lambda\). For initial density operator \(\rho_0\), time evolution is unitary:

\[
\rho(t)=U(t,t_0)\rho_0 U(t,t_0)^\dagger.
\]

For a coarse-grained sequence of alternatives \(\alpha=(\alpha_1,\ldots,\alpha_n)\), introduce a class operator constructed from time-ordered Heisenberg projectors:

\[
C_\alpha=P_{\alpha_n}(t_n)\cdots P_{\alpha_1}(t_1).
\]

Define the **decoherence functional**:

\[
D(\alpha,\beta)=\operatorname{Tr}(C_\alpha\rho_0 C_\beta^\dagger).
\]

Where off-diagonal terms \(D(\alpha,\beta)\) are negligible for \(\alpha\ne\beta\), the coarse-grained family approximately satisfies classical probability sum rules, and can be assigned

\[
p_\alpha=D(\alpha,\alpha),\qquad \sum_\alpha p_\alpha\approx1.
\]

Do **not** assume arbitrary complete fine-grained trajectories are simultaneously decoherent or form a unique physically preferred branch partition. Do not treat \(\sum c_i|h_i\rangle\) as a rigorous generic decomposition into complete classical histories.

For an observer with full retained record sequence \(R_n\), define compatible history labels:

\[
\mathcal C(R_n)=\{\alpha:\alpha\text{ is consistent with }R_n\}.
\]

If \(R_{n+1}\) extends rather than erases \(R_n\), then

\[
\mathcal C(R_{n+1})\subseteq\mathcal C(R_n),\qquad
\mu(\mathcal C(R_{n+1}))\le \mu(\mathcal C(R_n)),
\]

where \(\mu(A)=\sum_{\alpha\in A}p_\alpha\), using a common decoherent history family. To represent the specificity or surprisal of a record, define

\[
I(R_n)=-\log_2 \mu(\mathcal C(R_n))
\]

for a nonzero measure event. **This is the surprisal of a record relative to a specified prior ensemble, not automatically the entropy of the observer's brain, the number of memories, or physical thermodynamic entropy.** It need not increase if accessible records are erased or if the history family is redefined. The complete sequence of earlier retained events can still be used for conditional analysis, even if the current observer forgets them.

### Interference and record formation

For two paths of a system entangled with environmental states \(|E_A\rangle, |E_B\rangle\), interference visibility in a balanced idealized interferometer is controlled by

\[
V=|\langle E_B|E_A\rangle|.
\]

When environmental states become distinguishable, interference in the reduced subsystem is suppressed. When information is suitably recombined or erased, interference may be recovered in an appropriate experiment. Decoherence is not a literal absolute ban on recombination. Stable classical records are emergent and approximate.

## 4. Within-history observers and their interactions

A history \(\alpha\) may contain many observers \(i=1,\ldots,N_\alpha(t)\) simultaneously. They are not independent particles outside the universe; their physical states can become correlated through conversation, observation, shared instruments, and shared environments. Record exchange changes future observer states and the future pattern of correlations.

Use joint distributions \(P(R_A,R_B\mid\alpha)\), not \(P(R_A\mid\alpha)P(R_B\mid\alpha)\) unless conditional independence is demonstrable. For example, when two observers read and agree on one redundant environmental record, their reports can be perfectly correlated even though the global underlying result is probabilistic.

An interaction can change which subsequent observer records exist, their content, the number of observer-moments, or even whether observers survive. The **whole interacting history** must be modeled jointly, not inferred by multiplying independent observer probabilities.

Quantum Darwinism supplies a framework for emergence of widely accessible, redundant records. It is essential to study because it addresses how many observers can agree about a stable macroscopic reality without independent fundamental collapses.

## 5. Cosmic-time measure of observer experiences

Let \(t\) be cosmological proper time in a suitable approximately homogeneous model. Fix a **finite comoving reference region** to avoid automatic divergences from infinite spatial volume; extend later only with a justified regulator.

Let \(n_{\rm obs}(\alpha,\mathbf x,t)\) denote an explicitly defined density or rate of observer-moments in the *physical* volume element in history \(\alpha\). This density should be generated from processes such as habitable environments, origin/evolution of observers, duration of life, behavior, and within-history interactions. It must not be defined solely as number of planets.

One provisional weighted rate is

\[
W(t)=\sum_{\alpha\in\text{decoherent family}}p_\alpha
\int_{V(t)} n_{\rm obs}(\alpha,\mathbf x,t)\,dV_{\rm phys}.
\]

Equivalently, for identified observers \(i\) in each history:

\[
W(t)=\sum_\alpha p_\alpha\sum_{i\in O_\alpha(t)}r_i(\alpha,t),
\]

where \(r_i\) must have a clear meaning, such as observer-moments per unit cosmic time, and may account for each worldline's proper time. A *choice of reference class and observer-moment weighting* is an additional assumption, not a Born-rule theorem. When observers interact, their joint physics affects \(O_\alpha(t)\) and \(r_i\), but their moments need not be statistically independent to sum them as a descriptive rate.

When \(\int W(t)dt\) is finite and the chosen reference class is clear, define

\[
p(t\mid\text{sampled observer-moment})=\frac{W(t)}{\int W(s)ds}
\]

and the probability that such an observer-moment falls at or before today's cosmological age \(t_0\approx13.8\,\mathrm{Gyr}\):

\[
F(t_0)=\frac{\int_0^{t_0}W(t)dt}{\int_0^{\infty}W(t)dt}.
\]

**Important:** A uniformly sampled observer-moment is a *proposed xerographic/self-location distribution*, not an automatic consequence of our knowing that we are observers. Compare results under competing reference classes and do not present any one as established.

### Cosmological end criterion

Instead of demanding all matter vanish, define \(T_{\rm support}(\alpha)\), a *model-dependent last time of ordinary observer-supporting conditions* in the finite reference region of history \(\alpha\). Then

\[
F_{\rm sterile}(t)=\sum_\alpha p_\alpha\,\mathbf{1}[T_{\rm support}(\alpha)\le t],
\]

and (if it exists)

\[
t_{99.99}=\inf\{t:F_{\rm sterile}(t)\ge0.9999\}.
\]

Use observer-supporting conditions as the explicit operational criterion; state how long-term artificial habitats, nonstellar energy sources, exotic observers, and rare thermal fluctuations are treated. A finite sterility cutoff need not exist, especially in models allowing arbitrarily late observers/Boltzmann-brain-type events.

### Core modeling scenarios

- **Baseline stellar-life scenario:** Star formation, metallicity, habitable rocky planets, delays to biology/complexity, stellar lifetime, and observer-duration assumptions.
- **Red-dwarf-friendly scenario:** Habitability remains possible around long-lived low-mass stars; weight may peak far in the future (published models suggest order \(10^{13}\) years for *potential life emergence*, not proven observer-moment dominance).
- **Red-dwarf-suppressed scenario:** Radiation/planetary retention/habitability filters strongly reduce future opportunities.
- **Interactions & civilizations sensitivity:** Interaction networks influence information access, reproduction, migration, longevity, and observer-moment counts. Treat these as parameterized speculative assumptions, not empirical estimates.
- **Late-time stress test:** Examine whether the assumed distribution is normalizable, and report what happens when exotic or extremely late observers are included or excluded.

## 6. Coding milestones and falsifiable checks

**Stage A — literature-to-math map.** For each formula, annotate whether it is standard, a simplifying assumption, or a novel conjecture. Cite the reference and precise equation/section where applicable. List physics limitations explicitly.

**Stage B — exact small Hilbert-space model.** Implement a two-path system plus measuring ancilla, environment fragments, and two observer-record registers. Evolve unitarily, with no collapse. Calculate reduced density matrices, coherence, \(V\), mutual information \(I(S:F)\), redundancy of copied records, and agreement/disagreement rates of observer reports. Include controlled recoherence/quantum eraser scenarios. Compare with analytically solvable examples.

**Stage C — history-measure model.** Implement class operators and decoherence functional for a small consistent family. Check approximately vanishing off-diagonal terms; calculate \(p_\alpha\), nested compatible sets, relative prior measure, and record surprisal. Demonstrate that **sum of exhaustive history weights stays one**, even as one record's compatible set shrinks. Compare retained, erased, and shared records.

**Stage D — within-history observers.** Build a simple interacting-observer process: at least two observer agents can receive the same record, communicate, lose memories, be born/die, or act on others. Track joint, not presumed independent, probabilities. Include a case where \(P(A\text{ records }0,B\text{ records }1)=0\) because they share an error-free source, even though both outcomes occur across branches. Check that duplicating an observer/register changes the assumed anthropic count but not the underlying branch's Born weight.

**Stage E — separate cosmological toy population model.** Do NOT claim a full quantum-gravity simulation. In one fixed cosmic background, parameterize stellar and planet formation, habitability, evolutionary delay, observer duration, observer interactions, and eventual cessation. Generate \(W(t)\), \(F(13.8\,\mathrm{Gyr})\), and \(t_{99.99}\) where defined. Report sensitivity under different reference-class rules. Label synthetic parameters prominently; only import observational data if it is verified and documented.

**Stage F — comparison & output.** Produce at least: (1) interference visibility vs environment overlap; (2) diagonal/off-diagonal decoherence functional; (3) decreasing measure of one compatible-history set vs conserved total measure; (4) joint observer correlations; (5) observer-moment distribution across cosmic time on logarithmic time axis; (6) today's percentile under each explicit population/typicality scenario. Include exact tests, uncertainty analysis, code provenance, and clear reasons any model fails.

### Nonnegotiable methodological checks

- **Do not count 'worlds' and call that Born measure.** There is no unique, naturally preferred exact branch count in generic Everettian dynamics.
- **Do not multiply correlated observer probabilities.** Joint records emerge from the same unitary dynamics.
- **Do not confuse one history's decreasing prior measure with a decreasing total history measure.**
- **Do not infer early-time typicality from nested subsets alone.** Early/late likelihood depends on \(W(t)\) and self-location assumptions.
- **Do not assume entropy and record surprisal are equivalent.**
- **Do not assert permanent classical histories through all time in generic systems.** Decoherence is approximate; quantum eraser counterexamples exist.
- **Do not infer consciousness from a qubit record.** Qubit registers are information-processing proxies, not conscious observers.
- **Do not assume all histories share a common four-dimensional cosmic foliation in exact GR.**
- **Do not advertise rediscoveries of Everett, decoherent histories, quantum Darwinism, or anthropic observer weighting as new.** Identify overlap first.

## 7. Priority reading — READ IN FULL

Read these before or during implementation. Take equations, assumptions, limitations, and known criticisms into the technical notes.

1. **Hugh Everett (1957), “Relative State” Formulation of Quantum Mechanics.** Foundation for relative observer states and no fundamental collapse. https://doi.org/10.1103/RevModPhys.29.454
2. **Murray Gell-Mann and James B. Hartle (2018), Quantum Mechanics in the Light of Quantum Cosmology.** Closest overarching comparison: decoherent histories, emergent quasiclassical domains, and observers as information-gathering and utilizing systems (IGUS). https://arxiv.org/abs/1803.04605
3. **Murray Gell-Mann and James B. Hartle (1995), Strong Decoherence.** Essential for durable physical records and the 'permanence of the past' caveat. https://arxiv.org/abs/gr-qc/9509054
4. **Wojciech H. Zurek (2009), Quantum Darwinism.** Why environment records can be redundantly available to multiple observers. https://doi.org/10.1038/nphys1202
5. **Charles T. Sebens and Sean M. Carroll (2018 journal / 2014 preprint), Self-Locating Uncertainty and the Origin of Probability in Everettian Quantum Mechanics.** The exact philosophical/probabilistic difficulty in saying 'which observer/branch am I?', and why branch counting is not Born probability. Their derivation is a debated argument; distinguish claims and criticisms. https://arxiv.org/abs/1405.7577
6. **Mark Srednicki and James B. Hartle (2010 journal / 2009 preprint), Science in a Very Large Universe.** Multiple observer copies, xerographic distributions, and why a sampling rule is required for typical-observer claims. https://arxiv.org/abs/0906.0042
7. **Abraham Loeb, Rafael A. Batista and David Sloan (2016), Relative Likelihood for Life as a Function of Cosmic Time.** Starting point for cosmic-time habitability distribution; distinguish life *emergence* from the number/duration of conscious observer moments. https://arxiv.org/abs/1606.08448

## 8. Priority reading — SKIM SELECTIVE SECTIONS

8. **W. H. Zurek (2003), Decoherence, einselection, and the quantum origins of the classical.** Large technical review: focus on pointer states, environment-induced decoherence, objective records; dig deeper only when implementing. https://arxiv.org/abs/quant-ph/0105127
9. **Gell-Mann and Hartle (2021), Decoherent Histories Quantum Mechanics and Copenhagen Quantum Mechanics.** Focus on measurement, irreversibility, and how classical worlds are derived rather than postulated. https://arxiv.org/abs/2110.15471
10. **Hartle (2020), Arrows of Time and Initial and Final Conditions in the Quantum Mechanics of Closed Systems Like the Universe.** Review how time-neutral dynamics can coexist with a directional history of records. https://arxiv.org/abs/2002.07093
11. **Hartle and Srednicki (2007), Are We Typical?** Challenge the assumption that we were randomly sampled from all observers; apply as critique of proposed anthropic weights. https://arxiv.org/abs/0704.2630
12. **Zwolak and Zurek (2017), Redundancy of einselected information in quantum Darwinism.** Shared environmental records and agreement among observers. https://arxiv.org/abs/1703.10096
13. **Bousso, Freivogel and Yang (2008), Boltzmann babies in the proper time measure.** Cautionary example: seemingly natural time/observer cutoffs can predict pathological typicality or youngness. https://arxiv.org/abs/0712.3324
14. **Gell-Mann and Hartle (1992/1993), Classical Equations for Quantum Systems.** Mathematical framework for quasiclassical histories; reference if the 2018 overview is insufficient. https://arxiv.org/abs/gr-qc/9210010

## 9. What should count as success?

A first successful result is **not** proof that time is emergent, that our world is early, or that one unique history has been selected. It is a technically correct, reproducible demonstration that:

1. Unitary entangling dynamics reproduces local interference suppression and shared recorded outcomes;
2. Persistent records create nested observer-relative compatible-history subsets and increasing *record surprisal* without losing global Born norm;
3. Multiple interacting observers can be represented by joint histories rather than assumed independent branches;
4. A clearly declared observer weighting, habitability model, and spacetime cutoff yields a cosmic-time observer distribution, with sensitivity to assumptions;
5. The implementation identifies whether anything here is a new prediction or is only a consistent Everett/decoherent-histories interpretation.

**Research question:** Can one build a minimal unified formalism in which emergent, interacting record-bearing observers have mutually consistent experiences and apparently directional histories inside a time-neutral, unitary quantum universe—and then quantitatively model when such observers are likely to exist—without adding a collapse law or conflating history conditioning with anthropic typicality?

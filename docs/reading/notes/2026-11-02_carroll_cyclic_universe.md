# Carroll, Diachenko and Dulani (2026), the quantum cyclic universe, and its parent (Carroll 2023): read in full and set against the owner's turn of the loop

Date: 2026-11-02. By an assistant agent (Claude Fable 5.1). The owner has not read these passages. Both papers were
read in full from the arXiv PDFs (text extracted with PyMuPDF; equation numbers and section numbers are the papers'
own; page numbers refer to the PDF). Every statement in the first part is theirs, quoted or closely paraphrased with
its location. Everything in the second part is ours, unverified, and tied to the record by Update and O numbers. Under
rule 13 a published theory is a target the owner's hypothesis must reproduce or beat, never evidence for it.

Papers:

- **[CDD26]** Sean M. Carroll, Nadiia Diachenko, Saakshi Dulani, "Toward a Phenomenologically Acceptable Quantum
  Cyclic Universe", arXiv:2605.30405 [gr-qc], submitted 28 May 2026 (v1). 23 pages, 112 references. No journal
  given.
- **[Car23]** Sean M. Carroll, "Completely Discretized, Finite Quantum Mechanics", arXiv:2307.11927 [quant-ph],
  v2 of 1 November 2023; published as Found. Phys. 53, 90 (2023) according to [CDD26] reference [79]. 8 pages.

## Part 1. What the papers say (theirs)

### 1.1 The model

One vector in a finite-dimensional Hilbert space, evolving unitarily, with the theory fixed by the spectrum alone.
[CDD26] Sec. II: "a purely unitary (Everettian) picture of quantum mechanics [87, 88], in which the theory is
entirely specified by a Hilbert space H of finite dimension dim H = D, an initial state vector |ψ(0)⟩, and a
Hamiltonian H. Aspects such as observers, measurements, probabilities, and all of the familiar classical structures
are to be derived from this simple list of ingredients" (p. 3 to 4). "The choice of spectrum entirely defines the
quantum theory" (after Eq. (2)). Space, fields and observers are to come out by "quantum mereology", the search
for a factorization of Hilbert space with the right properties (Sec. I, p. 2; Sec. V, p. 14). The authors say
plainly that this map does not exist yet: "At this time we do not have a well-defined map from states |ψ⟩ in our
finite-dimensional Hilbert space to a semiclassical spacetime" (Sec. V, p. 14).

The size: "we would expect the dimensionality of Hilbert space to be D ∼ e^{S_dS}, where the de Sitter entropy for
observed parameters is S_dS ∼ 10^122" (Sec. I, p. 2); [Car23] Eq. (22) writes D ≈ 10^{10^122}. Both papers say
holography is the motivation and then set it aside: "In this work we are putting aside any inspiration from
holography and quantum gravity and simply considering the evolution of a state vector in a finite-dimensional
Hilbert space for its own sake" ([CDD26] Sec. I, p. 2).

### 1.2 Exact periodicity, and the period

Schrödinger evolution in the energy eigenbasis is straight-line motion on a torus of phases: with shifted energies
Ẽ_k = E_k − E_0 ([CDD26] Eq. (4)), "Schrödinger evolution can be thought of as straight-line motion on a (D − 1)-
dimensional torus, with coordinates given by θ̃_k(t) = Ẽ_k t" (Sec. II, p. 4). Generic (incommensurable) energies
give a trajectory "dense in the (D − 1)-dimensional torus, consistent with the recurrence theorem" (p. 4). The
special case: if every ratio Ẽ_k/Ẽ_j is rational, Ẽ_k = p_k ω_* with coprime integers p_k (Eq. (6)), and after

    T_* = 2π/ω_*            ([CDD26] Eq. (7); [Car23] Eq. (15), there written T_recur = 2π/ε)

"the state vector will return to precisely where it started, describing periodic evolution with period T_*" (p. 5).
Two remarks the authors attach: the condition means "our spectrum is just that of (some subset of) a simple harmonic
oscillator" (p. 5; and in the introduction, "the theory of everything is essentially a big harmonic oscillator with a
very specific initial condition", p. 3); and the condition is approachable to any precision, since any finite set
of reals is approximated arbitrarily well by integer multiples of some ω_* (p. 5).

The period against the recurrence time: "T_* is set by the fiducial energy ω_*, with no explicit dependence on the
size of the overall Hilbert space. By contrast, the recurrence time to enter a macrostate represented by a Hilbert
subspace of dimension d is expected to be T_recur ∼ e^{c(D−d)/δE}" (Sec. II, p. 5), which with D ∼ exp(10^122) is
"clearly much longer than T_*".

[Car23] adds the discrete step. With N the least common multiple of the p_k (Eq. (16)), δt = T_recur/N (Eq. (17)),
and "The overall evolution of this discretized model is periodic in time, with precisely N distinct states realized
along the way. The evolution of the universe is cyclic, repeating after N timesteps" (Sec. II, p. 4). The step "is
presumably much shorter than the Planck time" (p. 4). [Car23] also notes that the amplitudes can be made integers
by rescaling the norm (Eq. (21) and the paragraph after it), so "once again we only really need a finite set of
integers" (p. 4). [CDD26] does not use the discretization; it keeps continuous t and uses only the periodicity.

### 1.3 What plays the Big Bang, and why it is an entropy excursion

Entropy is a coarse-grained quantity they define in Sec. III: partition Hilbert space into macrostate subspaces,
H = ⊕_a H_a (Eq. (10)), with d_a = dim H_a, p_a = ⟨ψ|Π_a|ψ⟩ (Eq. (11)), and

    S_QB = Σ_a p_a log d_a            ([CDD26] Eq. (12), "quantum Boltzmann entropy")

The von Neumann entropy is rejected for this purpose because for a closed system it "is conserved" and for a pure
state "vanishes" (p. 6). The "Quantum Past Hypothesis" is that "the global state at some initial time is
concentrated wholly in the lowest entropy macrostate; p_a = 1 for minimal d_a entails that all branches start out in
the smallest subspace" (p. 9). They argue, Eqs. (18) to (20), that S_QB grows because entropy grows within branches,
not because branches multiply.

The Big Bang is the minimum of S_QB on the periodic curve. "it is possible to choose an 'initial' state of low
entropy, and the system will with high probability increase in entropy toward both the past and future from that
point; it is natural to identify that moment as the bounce separating a crunch and bang" (Sec. I, p. 2). In the
spacetime sketch of Sec. V: "The low-entropy minimum represents a bounce connecting a Big Crunch on one side to a
Big Bang on the other. Call the bounce phase B" (p. 15), and "B corresponds to the entropic minimum of the evolution
of |ψ⟩, S_QB = 0" (p. 17). They do not claim a semiclassical description of B: "we would expect the system to be in a
regime where quantum-gravity effects are important, and we shouldn't be too insistent on the universe obeying the
classical Einstein equation at that moment" (p. 17).

The illustration (Sec. IV, Figs. 1 and 2): D = 111, three macrostates of dimensions 1, 10 and 100, Haar-random with
respect to the energy eigenstates, energies random integers between 1 and 1000 times ω_*, the state started inside
the one-dimensional macrostate (S_QB = 0). "The evolution of this periodic system, therefore, includes one enormous
entropy fluctuation per cycle, and a relatively small number of smaller fluctuations" (p. 11).

### 1.4 How the excursion's probability compares with exp(−ΔS)

The standard expectation is stated and then set aside: fluctuations "are expected to have probabilities P(ΔS) ∝
exp(−ΔS), so small fluctuations are enormously more likely than large ones" (Sec. I, p. 2). The loophole: "with
commensurable eigenvalues, the evolution describes a closed one-dimensional curve, and is highly non-ergodic. The
long-term trajectory does not sample the whole torus fairly. As a result, if we choose to start in an (admittedly
non-generic) low-entropy initial condition, we can return exactly to that initial condition well before we sample a
large number of Boltzmann-Brain-like fluctuations" (Sec. IV, p. 10 to 11). And: "the repetition frequency of the
large fluctuations is much greater than we would expect on the basis of P(ΔS) ∝ exp(−ΔS)" (p. 11). Said plainly:
the big excursion is not a fluctuation that happens with probability exp(−ΔS); it is the initial condition coming
round again, once per period, by construction. The paper is explicit that this is not generic: "We do not claim that
our model is in any way generic; quite the opposite. We invoke non-generic features in two ways" (Sec. VI, p. 18):
commensurable eigenvalues, and a minimal-S_QB initial condition.

### 1.5 Boltzmann brains

The problem as they state it ([Car23] Sec. III, p. 5 to 6): even conditioning on observers "macroscopically
indistinguishable from ourselves", it is "overwhelmingly likely for them to be random fluctuations rather than
ordinary observers", which is "cognitively unstable". [Car23] offered two ways out (p. 6): a "non-generic,
fine-tuned kind of evolution, featuring a single enormous downward fluctuation in entropy with the rest of the
evolution staying in a high-entropy state with no fluctuations", or emergent time with a finite number of clock
ticks. [CDD26] builds the first.

The count ([CDD26] Sec. IV, p. 13): with N_OO the ordinary observers per cosmological history, estimated in [75] as
10^11 ≤ N_OO ≤ 10^124 ("the precise value will be essentially irrelevant"), and

    N_BB = Γ_BB T_* H_*^{−3}          (Eq. (26))
    Γ_BB ∼ e^{−S_BB} ∼ e^{−M_BB/T_dS} ∼ e^{−10^66}    (Eq. (27); a brain of about Avogadro's number of baryons,
                                                          T_dS = 10^{−33} eV)

the condition N_BB < N_OO is

    T_* = 2π/ω_* ≤ e^{10^66}          (Eq. (28))

With a lower bound from ω_* no larger than a Hubble-wavelength photon ("a period of not much more than a Hubble
time, T_* ∼ 10^10 yr", which "implies a Big Crunch at a future time that is relatively soon, cosmologically speaking,
but this is only a lower bound on the period", p. 14), the allowed range is

    10^10 yr ≤ T_* ≤ e^{10^66}         (Eq. (29))

Footnote 2 (p. 13) says why one cycle, one branch suffices for the count: observers on all branches "should also be
weighted by the amplitude-squared of the branches that they are on, which compensates, so a standard expectation
value in a single stochastic universe is what we want". The paper does not say the Boltzmann brains vanish: "there
can still be Boltzmann Brains ... in the near-equilibrium phase. Such fluctuated observers will be relatively rare
... just because the time between exactly returning to the low-entropy state is much smaller than the ordinary
recurrence time" (p. 13). It notes that a stricter notion of observer, after [77] (Banks, Fischler and Paban), "could
loosen the bound in (29), perhaps by an appreciable amount; we do not take up this challenge here" (p. 14).

### 1.6 What observers see, and when in the cycle

Three phases (Sec. V, p. 15, Fig. 3): B the bounce; Λ± "conventional cosmological evolution from the high-
temperature/low-entropy phase toward an asymptotically de Sitter phase" on each side; E "a high-entropy equilibrium
phase whose closest spacetime interpretation is empty de Sitter", which "lasts for much longer than is suggested by
the pictures" (Fig. 3 caption). Observers exist in Λ+ and Λ−, and in E only as the rare fluctuations of Sec. IV.
In E "there are no observers or test particles moving on an emergent metric. There is only (aside from possible rare
fluctuations) the equilibrium quantum state itself"; the branches "have essentially recohered into a single state ...
because the 'system' part of the wave function is simply empty de Sitter spacetime in every branch" (p. 17).

Observers on the two sides cannot see each other: they "will characterize each other as having reversed arrows of
time (a fact which is of course completely unobservable, as we cannot see through the Big Bang)" (Sec. IV, p. 13).
The universe each sees is the causal diamond of one observer: the diagonal edges in Fig. 3 are "the edge of the
causal diamond accessible to an observer at the origin" (caption), and "different observers describe (within the
same finite-dimensional H) different causal diamonds, all related by unitary transformations of each other"
(p. 16, after Banks and Fischler [62]).

### 1.7 What is conserved

Unitary evolution with a time-independent Hamiltonian (Sec. VI, p. 17): the norm, the von Neumann entropy ("since the
universe is evolving unitarily (i.e., it is a closed system), S_vN is conserved", p. 6), the energy expectation
value, and the amplitudes themselves: "The amplitudes stay constant while the phases move linearly in time" (p. 4).
What is not conserved is S_QB, which is the point. There is no matter, no energy density and no geometry in the
fundamental description to be conserved; those are emergent and unmapped (Sec. V).

### 1.8 The same every cycle, or different

Exactly the same. "Exact t → t + T_* symmetry over eternity leads to an infinite number of identical copies of the
universe in its expansion and contraction phases (though the expansion and contraction phases are not identical to
each other in the absence of exact t → −t symmetry). As Nietzsche envisioned [1], everything you do has already been
done infinitely many times in the past, and will be done infinitely many times in the future" (Sec. VI, p. 19). The
Nietzsche epigraph (p. 1) and the Poincaré close (p. 19) frame the paper that way. The asymmetry between the two
halves of a cycle is derived: S_QB(t) = S_QB(−t) requires the reality condition of Eq. (25), "This will not be
satisfied for an arbitrary choice of a low-entropy initial condition and macrostate projectors, so the entropy curve
is not precisely symmetric around the minimum" (p. 13). And since the evolution is periodic and not merely
recurrent, "opens the door to thinking of time as only lasting for a finite interval, simply by quotienting out the
evolution by T_*. Choosing to consider time in this model as defined on a circle rather than on a line is somewhat a
matter of taste" (p. 19).

### 1.9 The arrow of time within a cycle

Two arrows, pointing away from the bounce. "the classical thermodynamic entropy will increase on typical branches as
we move away from the low-entropy point toward either the past or the future. Ordinary observers will be able to
come into existence on both sides of the bounce; either set of observers (t > 0 and t < 0) will experience
conventional thermodynamic evolution, labeling 'the past' as the direction in which the entropy of the universe is
smaller" (Sec. IV, p. 13). The crunch is the bang played backward: "it is simply the evolution from Λ+ to E ... played
backward in time. That is, it appears as if the vacuum gradually 'excites' to include a gas of ultra-long-wavelength
photons of increasing density ... The photons form white holes that expel particles and larger objects, which
eventually form (time-reversed) galaxies and stars ... explained by the existence of an effective Future Hypothesis
of low entropy at B" (Sec. V, p. 16 to 17). There is no phase transition at the turnaround: "The universe in this
picture does not undergo a sudden phase transition when it evolves from the equilibrium phase E to Λ−" (p. 16); the
apparent contraction is a change of slicing of de Sitter (static patch, Eq. (30); ansatz Eq. (31)).

### 1.10 Stated predictions or tests

None observational. What the paper offers are bounds and reinterpretations: the period window Eq. (29); a Big Crunch
at least a Hubble time away (p. 14); the cosmological constant as an input tied to the Hilbert-space dimension,
"Λ ≈ π/[G log(dim H)]. This doesn't solve the cosmological constant problem, but turns it into an entirely different
question: why is the dimensionality of Hilbert space so large?" (Sec. VI, p. 19; the paper's own dash is rendered as
a colon here); and a pointer that "the 'first entangled qubit' should have been created not much more than 70
e-folds before the end of inflation, raising the prospect of some kind of information persisting through the bounce
phase" (p. 18). The model's main claim is of possibility: "For now we are confining ourselves to the more modest goal
of verifying that this kind of scenario can possibly work" (p. 18).

### 1.11 Their list of open problems (Sec. VI)

1. Why the spectrum should be commensurable, and why the initial condition should be minimal entropy: "We have no
   idea" (p. 18).
2. The emergence map from branches to semiclassical quantities with positive Λ; whether a commensurable spectrum can
   also carry an emergent local factorization ("It might seem unlikely ... but it's reasonable to expect that
   approximate locality is broadly achievable", p. 18).
3. Homogeneity, isotropy and density fluctuations in this framework (p. 18).
4. Whether a stricter definition of observer loosens the period bound (Sec. IV, p. 14).
5. The semiclassical description of the bounce phase B (Sec. V, p. 17).
6. Whether the equilibrium phase is really de Sitter, given that nothing decoheres there (Sec. V, p. 17).
7. Finitism and the moral implications of exact repetition (p. 19), left to the reader.

[Car23] adds (Sec. IV): whether Presburger arithmetic suffices (it tentatively concludes no, because of multiplying
amplitudes by basis vectors, p. 7), and the two cosmological ways out listed in 1.5, "neither of them is truly
compelling at the moment" (p. 6).

## Part 2. Set against the owner's turn of the loop (ours, unverified)

The owner's picture, as the record states it: spacetime is one turn of a strange loop (Update 23, the count per
turn; Update 26, the strange-loop measure; glossary: Hofstadter's term, used with credit). A turn ends when all
matter and energy have gathered into black holes and nothing moves through space, so there is no time (Update 44,
her conjecture, "not an established mechanism"); the loop measure paper words the end as "when its last black hole
has dissolved" (`docs/papers/loop_measure/paper.tex`, Sec. "The measure as decided", citing Updates 44 and 59). New
universes are born inside black holes, from accumulated curl energy that goes over a wall (Updates 42, 59, 149; the
exact barrier of T54; claim 4). Each universe runs "an exact copy" of one clock from its birth to its heat death,
with no clock across universes (Update 68). The measure counts once per civilization, weights ages by the comoving
volume of the causal diamond, and defines an observer as a civilization in which at least one intelligent being asks
this question (Update 71; loop measure paper Eq. (1)). Chance-assembled brains are not observers because they cannot
evolve (Update 43). The leftover of a birth is a sprinkle of knots of fixed energy, set at the opening (O107, paper 2).

### 2.1 Periodicity: his exact recurrence against her turn with waste

- **His** cycle is one closed curve in the space of states: the same state, to the last phase, every T_*. Nothing is
  left over from one cycle to the next, because there is nowhere for a leftover to be; the equilibrium phase E
  erases the branch structure ("the branches have essentially recohered into a single state", p. 17), and the
  Future Hypothesis at B is the Past Hypothesis seen from the other side.
- **Hers** is not a return of a state. A turn is one universe's life, birth to heat death; the next turn is a
  daughter born inside one of its black holes, and there are many daughters per parent (Update 59: "every black hole
  births many daughters"; Update 149: twins, then more). What repeats is the rule and the clock (Update 68, "an
  exact copy"), not the arrangement. And the birth leaves waste: knots of fixed energy whose number is set at the
  opening and not by cooling (O107), and in Update 149's picture surplus matter at the pole. So her loop is a tree of
  near-copies with scrap, his a single circle with none.
- **Consequence for the measure.** His count is per cycle and the cycle is the same each time, so "per cycle" and
  "over eternity" agree up to a factor (footnote 2, p. 13; the quotient by T_* on p. 19). Hers has no common clock
  across universes and the number of universes grows each generation, which is why Update 67 and 68 had to decide
  how generations combine; his model never faces that choice. His periodicity therefore does not reproduce her
  multiplying, and her multiplying does not reproduce his exact return. They are different shapes, not the same
  shape with different words.
- **One place they touch.** His "time ... defined on a circle rather than on a line" (p. 19) and her "the loop needs
  no beginning or end, and its turns need not differ; all of them are equally real" (Update 33, position 4) are the
  same philosophical move. In his model it is exact and derived from the spectrum; in hers it is asserted.

### 2.2 What starts a cycle: his entropy minimum against her black hole's accumulated curl with a wall

- **His** birth is not caused; it is the initial condition coming round. The entropy excursion has no trigger and no
  barrier; its probability is not exp(−ΔS) because the trajectory is a closed loop that passes through the minimum
  once per period (1.4). Asked why, the paper answers "We have no idea" (p. 18).
- **Hers** is a decay with an activation cost: a specific stable-for-now arrangement (X, the slab or tube) goes over a
  wall when something pays the cost, and the released energy is the burp (claim 4; S2′; the 12-unit spark of
  Update 9; T54's exact barrier, a quadratic in the patch size; Update 59, "nucleation is a rising chance, not a
  threshold"). In Update 149 the push is curl energy that photons deposit in the slab until "there is enough".
- **Where they differ in kind.** His is a global event (the whole state passes through S_QB = 0) that is the
  cheapest thing possible because it is exact. Hers is local (one pole of one rod, inside one black hole, while the
  parent persists, Update 59), and it has a stated cost that the record has priced (O106, T54). His model has
  nothing to say about a local birth inside a parent; her model has nothing that returns the parent to its start.
- **Where his result is a target for hers (rule 13).** He gives a reason the big excursion is far more frequent than
  exp(−ΔS): non-ergodicity. Her hypothesis needs its own reason that births are frequent enough to populate the
  tree, and today the record has only the toy's barrier (T54) and a bath that opens the first direction and not the
  second (T53, O105). The number she owes is a birth rate per black hole per unit of the parent's clock, with the
  wall and the accumulation rate in it, and the same comparison against exp(−ΔS) that he makes on p. 11. Nothing in
  the toy gives it yet.
- **A caution from his Sec. V.** His crunch is the bang run backward, with white holes expelling matter (p. 17). Her
  black holes run the other way: they gather matter and then give birth. In his picture the end of a universe is
  time-reversed birth; in hers it is the birth of others. A reader coming from his paper will ask whether her black
  holes are the time reverse of her births; the record's answer (Update 27, the fold run backward, with the walls
  priced from both sides, O55) is that the fold and the opening share a barrier but are not each other's reverse in
  what they release.

### 2.3 The measure: his Boltzmann-brain avoidance against her once-per-civilization count

- **His** measure is the Born expectation over one cycle in one Hubble volume (footnote 2), and the only thing it has
  to get right is N_BB < N_OO, Eqs. (26) to (28). It counts brains that fluctuate, with a stated rate (Eq. (27)) and
  a stated size (Avogadro's number of baryons), against ordinary observers whose number he takes from his own 2017
  paper, and it reaches a window for the period, Eq. (29). It is a calculation with one free scale, ω_*, and it says
  what range of that scale is allowed.
- **Hers** counts civilizations once each at their birth, weighted by the causal diamond's comoving volume, per
  universe by its own age (Update 71; loop paper Eq. (1)), and excludes chance brains by definition: "Brains that
  assemble by chance in space are not real observers: they cannot evolve" (Update 43). The exclusion is a rule about
  what counts, not a calculation that they are rare. [CDD26] does the opposite: it keeps them in the count and shows
  they are outnumbered.
- **What his result demands of hers (rule 13).** A number like Eq. (28). In her universe the late phase is a de
  Sitter-like cold period (the loop paper's diamond closes because dark energy is a true constant), and that is
  exactly the phase in which his Γ_BB ∼ e^{−10^66} per spacetime volume applies. Her turn lasts until the last black
  hole dissolves, which on standard numbers is of order 10^100 years, far longer than his lower bound on T_* and far
  shorter than his upper bound e^{10^66}. So on his arithmetic her turn would pass the Boltzmann-brain test by a wide
  margin, and the exclusion by definition in Update 43 is not needed for that purpose. That is good news of the kind
  the owner wants (existing math that applies), and it is ours, unverified: it uses his rate, his N_OO, and the
  standard black-hole evaporation time, none checked by us beyond this paper.
- **The published objection he cites and does not resolve.** His own 2016 paper with Boddy and Pollack ([78] in
  [CDD26]; the description is [Car23]'s, p. 6) argues that a stationary de Sitter vacuum does not fluctuate at all. [CDD26] keeps Γ_BB non-zero in the
  finite-dimensional case and says only that a Banks-Fischler-Paban-style analysis "could loosen the bound" (p. 14).
  The record's own position, that chance brains are excluded because they cannot evolve, is the third option; the
  review of [Freivogel11] names it (Update 43). None of the three is hers to claim as support.
- **Causal diamond.** Both use it. His: the universe one observer describes is one diamond, and different observers'
  diamonds are unitarily related (p. 16). Hers: the diamond's comoving volume is the weight on ages (Update 71). His
  use is kinematic (what one observer can describe); hers is a measure weight ([BHKP07]'s). The same object, two
  roles; the loop paper should say which it means when it cites the diamond, since his paper is now the nearest
  published cyclic model and it uses the word differently.

### 2.4 The arrow of time

- **His** arrow is thermodynamic and double: entropy rises away from the bounce in both directions (1.9), with no
  arrow at all in the equilibrium phase, where nothing decoheres and there are no observers (p. 17). Time itself is
  fundamental and continuous ([Car23] keeps the Schrödinger t; its discretization is an option).
- **Hers** has time as an outcome of motion in open space (Update 33 position 5; Update 41), a moving front with the
  present as its edge (Update 36), and no time in X, where nothing moves (Update 42, "with one direction open nothing
  moves, so there is no time"); a turn ends when nothing moves (Update 44).
- **The point of contact.** His equilibrium phase E and her end-of-turn are the same kind of state described two
  ways: no observers, no decoherence, nothing happening. He says there is still time there (the Schrödinger t runs on
  through E, for most of the period); she says there is no time once nothing moves. If her "no time" is read as "no
  clock" (nothing that could measure t), the two agree; if read as "t does not advance", they disagree, and his model
  is explicit that t advances through E for most of the cycle. The record should say which it means (the open item
  (b) of Update 44 is this question).
- **The point of difference.** His arrow needs a low-entropy condition at B and nothing else; it reverses on the far
  side of B. Hers has one direction per universe, by construction (the daughter's clock starts at her birth and runs
  to her heat death, Update 68); there is no reversed half. And her X is itself a specific arrangement (claim 1), so
  her birth starts from low entropy for a structural reason (one arrangement, not many), which is close to what his
  Quantum Past Hypothesis puts in by hand ("all branches start out in the smallest subspace", p. 9). That is the one
  place where her hypothesis supplies something his paper says it lacks: a reason the initial condition is special.
  It is a reason in words; in the toy the tube is a dip of the energy (T7), not a one-dimensional macrostate, and no
  count of its "versions" was taken as an entropy (Q15 counts renamings; O28 found that a whole world with three
  different defects has exactly one).

### 2.5 What each predicts

- **His:** a period in the window of Eq. (29); a Big Crunch at least a Hubble time ahead, with no sign of it until
  the turnaround, which is a change of slicing and not an event; that the cosmological constant is set by log dim H;
  that some information may persist through the bounce. Nothing an observation now can check, by the paper's own
  account (1.10).
- **Hers:** the loop measure paper's one separable claim, that dark energy is a true constant so the diamond closes
  and our age is typical, against the published model's running coupling in which it is not; and a measured equation
  of state decides (loop paper abstract). Plus the toy's measured verdicts (a sharp change, a bounded release, a fixed
  activation, knots of fixed energy), none of which bears on the real universe (VISION, "What no outcome can show").
- **A shared prediction, stated by neither.** Both pictures have a cold, empty, de Sitter-like late phase lasting far
  longer than the matter era. In his it ends in a crunch that is the bang reversed; in hers it ends when the last
  black hole dissolves and daughters have already been born. Neither predicts anything different from ΛCDM for the
  next 10^10 years. The discriminator, if there is one, is at the end, and nobody will be there.

### 2.6 Benchmarks hers must meet (rule 13)

1. **A stated rate against exp(−ΔS).** He states why births are more frequent than a fluctuation (non-ergodicity,
   p. 11). She owes the equivalent: a birth rate per black hole from the wall and the accumulation, compared with
   the fluctuation rate over the same wall. T54 (the barrier) and the "rising chance" of Update 59 are the inputs;
   the number does not exist.
2. **The Boltzmann-brain count, Eqs. (26) to (28).** Her late phase is de Sitter-like and long; his arithmetic applies
   to it directly and gives a wide pass (2.3, ours). The record should run that arithmetic once with sources, instead
   of excluding chance brains by definition, so that Update 43's rule is a conclusion and not an axiom.
3. **Conservation across the cycle.** His is exact (unitarity). Hers is claim 6: an energy-like quantity conserved
   across the transition, and in the toy to the last unit in every sealed run (Update 13). What hers must add is the
   book across generations: what a daughter carries out of a parent and what the parent keeps (Update 30 and 41's
   "the remainder is returned to the black hole"). His model has no such transfer because it has no daughters.
4. **A defined end of the turn.** His period is exact and its length is bounded (Eq. (29)). Hers has two wordings in
   the record: "when all of it has [gathered into black holes], nothing moves ... the turn ends" (Update 44) and "when
   its last black hole has dissolved" (loop paper, citing Updates 44 and 59). Those are different moments, of order
   10^14 and 10^100 years on standard numbers, and the diamond weight depends on which. O101 asked for "a stated
   end"; it now has two.
5. **Why the start is special.** He puts it in and says so ("We have no idea", p. 18). Hers has a reason in words
   (X is one arrangement). To meet his bar the reason has to become a count: the entropy of X against the entropy of
   the space it becomes, in the toy, by Q15's renaming count or by the hidden count (O87). Nothing in the record has
   done that for the slab.
6. **The two arrows.** His model forces a time-reversed half-cycle. Hers has none. If she keeps one arrow per
   universe, she needs to say what, in her picture, plays the Future Hypothesis's role, or why none is needed: his
   answer is that exact periodicity with one minimum makes the far side of the minimum a second bang; hers is that
   the daughter is a new universe and the parent runs on. That is a structural difference, not a gap, and the page
   that compares the two should name it as such.

### 2.7 The one narrow question for a letter

His Sec. IV counts Boltzmann brains in the equilibrium phase at the de Sitter rate of Eq. (27), and the bound on the
period (Eq. (28)) follows from that count. His Sec. V then says that in the equilibrium phase "there is no dynamical
decoherence process that branches the state", "there are no observers or test particles moving on an emergent
metric", and only "(aside from possible rare fluctuations) the equilibrium quantum state itself" (p. 17); and his
2016 paper with Boddy and Pollack argued that a stationary de Sitter vacuum has no dynamical fluctuations at all. A
non-physicist can ask:

> In the finite-dimensional, exactly periodic model, does the equilibrium phase E make Boltzmann brains at the rate
> of your Eq. (27) at all? If the argument of Boddy, Carroll and Pollack (2016) carries over to a periodic state
> with commensurable energies, N_BB would be zero in E and the upper bound on the period in Eq. (28) would not be
> needed; if it does not carry over, what about the finite dimension or the periodicity restores the fluctuations?

It is narrow (one equation against one paragraph), it is his own open thread (p. 14 says the challenge is not taken
up), and the owner's interest in it is honest: her late phase is the same kind of state, and whether chance brains
are rare by rate or absent by structure decides whether Update 43's exclusion is a calculation or an axiom.

A second question, if one is wanted, is closer to her picture and less narrow: whether a low-entropy initial
condition that is one specific arrangement (a single macrostate of dimension 1, as in his Fig. 1 simulation) could
be a structured state with few symmetries rather than a point, and what that does to the symmetry of the entropy
curve (his Eq. (25)). Not recommended for a first letter.

### 2.8 Consistency notes for the record

- Update 43's annotation of 19 October already says "per turn, times how the turns multiply" is superseded by the
  per-universe count. The comparison above uses the per-universe count (Updates 67, 68, 71). Nothing in [CDD26]
  bears on multiplying; it is single-universe.
- The owner's "strange loop" is Hofstadter's term and the glossary says so. [CDD26] never uses the phrase; its word
  is "cyclic", and its loop is literal (a closed curve on the torus of phases). The public pages should not describe
  his model as a strange loop.
- The inventory note of 2 November (`2026-11-02_carroll_inventory.md`) called [CDD26] "the closest published relative
  of the owner's turn of a loop with a birth in it". After reading: it is the closest published relative of the
  *count per turn* and of the *empty late phase*, and a distant relative of the birth, which in his model is not an
  event with a cause. The inventory's sentence should be narrowed when it is next edited.

## Read status

| Paper | Key | Read status | How |
|---|---|---|---|
| Carroll, Diachenko, Dulani (2026), arXiv:2605.30405 | CDD26 | **In full** (Secs. I to VI, Figs. 1 to 3 captions, references list) | PDF text extracted with PyMuPDF; figures not viewed as images |
| Carroll (2023), arXiv:2307.11927 | Car23 | **In full** (Secs. I to IV) | PDF text extracted with PyMuPDF; Fig. 1 caption only |
| Boddy, Carroll, Pollack (2016), [78] in CDD26 | not in bib | Not read; cited here from [Car23] p. 6 and the title given in [CDD26] ref. [78] | |
| Banks, Fischler, Paban (2002), [77] in CDD26 | not in bib | Not read; cited here from [CDD26]'s description only | |
| Carroll (2017), "Why Boltzmann Brains Are Bad", [75] in CDD26 | not in bib | Not read; the N_OO range is quoted from [CDD26] p. 13 | |

The owner has read none of these passages. Quotations are from PDF-to-text conversion and were checked for sense but
not against the rendered pages; equation numbers were read from the extracted text and are to be confirmed against
the PDF before any is cited in a paper.

## REFERENCES.bib entries owed

```bibtex
@article{CDD26,
  author  = {Carroll, Sean M. and Diachenko, Nadiia and Dulani, Saakshi},
  title   = {Toward a Phenomenologically Acceptable Quantum Cyclic Universe},
  journal = {arXiv e-prints},
  year    = {2026},
  eprint  = {2605.30405},
  archivePrefix = {arXiv},
  primaryClass = {gr-qc},
  note    = {Read in full by an assistant agent, 2026-11-02 (docs/reading/notes/2026-11-02\_carroll\_cyclic\_universe.md); the owner has not read it. Exactly periodic finite-dimensional quantum cosmology; the Big Bang as the minimum of a coarse-grained entropy; Boltzmann-brain bound on the period, Eqs. (26) to (29). A target under rule 13, not evidence.}
}

@article{Car23,
  author  = {Carroll, Sean M.},
  title   = {Completely Discretized, Finite Quantum Mechanics},
  journal = {Foundations of Physics},
  volume  = {53},
  pages   = {90},
  year    = {2023},
  eprint  = {2307.11927},
  archivePrefix = {arXiv},
  primaryClass = {quant-ph},
  note    = {Read in full by an assistant agent, 2026-11-02; the owner has not read it. Journal reference taken from [CDD26] reference [79], to verify. Commensurable spectrum gives exact periodicity, Eq. (15); discrete timestep, Eq. (17); the two cosmological ways out, Sec. III.}
}
```

Verified against the sources by a second agent on 2026-11-02 (both papers extracted in full; every quotation checked was found); its page and year corrections applied the same day.

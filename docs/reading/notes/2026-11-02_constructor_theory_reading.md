# Reading: constructor theory, the witness theorem, and what they ask of the loop

Date: 2026-11-02. Written by an assistant agent (Claude Fable 5.1). **The owner has not read these passages.** The
papers were fetched from arXiv on 2026-11-02 and read from their text (the arXiv HTML render where one exists, the PDF
through PyMuPDF otherwise; the "which route" column of the table at the end says which for each). Quotations are
verbatim from those texts with section or equation numbers; where a quotation came through an HTML-to-text conversion
it is marked in the table at the end, and the usual caution applies (formulas and bold face can be mangled). Physics
reasoning in sections A to C is ours, unverified by a physicist. Under rule 13 every published result here is a target
the owner's hypothesis has to meet or be ruled out by, never evidence for it. Nothing here is a result about reality or
about the toy.

Why this note exists: on 2026-11-02 the owner pasted an FQxI article announcing a review, "Tests of Constructor Theory"
(Marletto, Deutsch, Vedral), and asked "anything useful here?" (`sandbox/NOTEBOOK.md`, 13:53 UTC). The reply named
three things of possible use and five sources to read before any of them is cited. This is that reading.

---

## 1. Deutsch, "Constructor theory" (arXiv:1210.7439; Synthese 190, 4331 (2013)). Read in full (PDF, 40 pages).

**Task, constructor, possible and impossible (Sec. 1.1).** "almost all require a constructor, which I shall define
as anything that can cause transformations in physical systems without undergoing any net change in its ability to do
so. I shall call those physical systems the constructor's substrates" (Sec. 1.1, before Eq. (1)). A task: "I
provisionally define a construction task (or 'task', for short) as a set of pairs such as (2), each designating a
legitimate input state for the task and associating that with a legitimate output state for that input." Possible:
"A task A is possible (which I write as A✓) if the laws of nature impose no limit, short of perfection, on how
accurately A could be performed, nor on how well things that are capable of approximately performing it could retain
their ability to do so. Otherwise A is impossible (which I write as A✘)."

**The cycle, and what may change (Sec. 1.1).** "The definition of a constructor for a task A requires it to be a
constructor for A again after performing an instance of A. Its other attributes may change, but what the user must do
in order to cause it to perform the task must remain the same." And the battery: "If a machine stops being capable of
performing a task A after its N'th run because its battery has run down, then it is not a constructor for A after the
(N − 1)'th run either, because the N'th run does not end with it being such a constructor – and so it follows by
induction that it never was one. However, the same machine excluding the battery could still be a constructor for a
related task whose substrates include a battery whose legitimate input states specify enough charge to perform A at
least once." So a thing that runs down is not a constructor; a thing plus its fuel, with the fuel counted as a
substrate, can be.

**Waste (Sec. 1.1 and Sec. 2.1).** "The specification of a task includes all its necessary inputs and unavoidable
outputs, hence the need to specify such things as what energy sources and waste products are permitted. Thus, a
constructor is characterised by the effect it would have if it and its substrates jointly constituted a closed
system." The life-cycle example, Eq. (6): "small molecules + light → cell + waste products" with the cell as the
constructor. Waste is therefore part of the task's output specification, not a failure of the constructor.

**A black hole as an energy sink is disqualified (Sec. 2.2).** On why a constructor cannot be an unlimited sink of a
conserved quantity: "to increase the energy of any system S1 without limit, the actions that the user needs to
perform keep changing, thus disqualifying S1 from being a constructor. For instance, even if S1 incorporated the most
compact possible means of sequestering energy, namely a black hole, its size and gravitational effects would increase
whenever it was used, requiring increasing resources to prevent it from impairing its users' functionality." The
stronger conservation law: "every task that would change the (overall) Q of its substrates is impossible."

**Locality (Sec. 3.10).** "Expressed as a principle of constructor theory, it is: for any two substrates S1 and S2,
there is a way of describing their states such that if S1 is in state x and S2 is in state y, the state of S1 ⊕ S2
is the ordered pair (x, y)." And: "The principle of locality holds unproblematically in classical physics but quantum
entanglement is often claimed to violate it. However, there exist formally local formulations of quantum theory
(Deutsch & Hayden 2000; Deutsch 2012), which are compatible with constructor theory."

**Laws of motion and the initial state as emergent (Secs. 2.5, 3.1).** "In the constructor-theoretic conception,
the initial state is not fundamental. It is an emergent consequence of the fundamental truths that laws of physics
specify, namely which tasks are or are not possible." And Sec. 3.1: "the distinction between ordinary and pharaonic
tasks corresponds roughly to that in the prevailing conception between laws of motion and the initial state at the Big
Bang." The 2026 review states the stronger form (Sec. 1): "its principles supplement the dynamical laws and the
initial condition theories, which become emergent consequences of the principles". Deutsch's own word in 2012 is
"conjecture"; the paper's Sec. 4 opens "The principles of constructor theory that I have proposed may be false."

**What counts as a test (Secs. 2.10, 2.11).** Principles are tested through the laws that obey them: "if there is a
phenomenon for which there is a good explanation that violates a principle P, and the phenomenon falsifies all known
object-level explanations conforming to P, then the methodology of science mandates rejecting P. Thus P is just as
exposed to falsification by experiment as any object-level theory." And every test is of an impossibility: "every
experimental test is of some prediction that performing certain transformations on given substrates is an impossible
task." (Sec. 2.11, with the ammonia example, Eq. (10).)

**Time (Sec. 3.12).** "In the constructor-theoretic conception, it is both natural and unavoidable to treat both time
and space intrinsically: they do not appear in the foundations of the theory but are emergent properties of classes of
tasks whose substrates include 'rods' and 'timers'." The 2025 paper "Constructor theory of time" (arXiv:2505.08692,
abstract only) takes this up; not read here.

## 2. Deutsch and Marletto, "Constructor theory of information" (arXiv:1405.5563; Proc. R. Soc. A 471, 20140540 (2015)). Read in part: Secs. 3 to 5 (computation, information, measurement), Sec. 6 (principle III), Secs. 7 and 8.1 to 8.4 and 8.9 (superinformation), from the PDF.

**Computation medium (Sec. 3).** "A reversible computation CΠ(S) is the task of performing a permutation Π over some
set S of at least two possible attributes of some substrate ... It is then natural to define a computation variable as
a set S of two or more possible attributes for which CΠ✓ for all permutations Π over S, and a computation medium as a
substrate with at least one computation variable."

**Information medium (Sec. 4).** Cloning, their Eq. (3), is the task of copying an attribute onto a second instance
prepared with a receptive attribute x0. "An information variable is a clonable computation variable. It is then
natural to define an information attribute as one that is a member of an information variable, and an information
medium as a substrate that has at least one information variable." And "a substrate S instantiates classical
information if some information variable S of S is sharp, and if giving it any of the other attributes in S was
possible."

**Distinguishability and measurement (Sec. 5).** A set X of attributes is distinguishable if the task of mapping each
x to ψx is possible "where the {ψx} constitute an information variable. Since 'information variable' is defined above
without reference to distinguishability, this definition is, as promised, not circular." Measurement is their Eq. (5),
cloning into an information medium prepared with a receptive attribute.

**Interoperability, principle III (Sec. 6).** "The combination of two substrates with information variables S1 and S2
is a substrate with information variable S1 × S2". With a line that touches the hypothesis's dark sector directly:
"Note that this principle requires certain interactions to exist in nature. For instance, it would rule out theories of
dark matter in which dark information media exist but interactions between the dark and normal sectors do not allow
information to be copied arbitrarily accurately between them."

**Superinformation, the "classical" against "quantum" line (Sec. 7).** "A superinformation medium M is an information
medium with at least two information observables that contain only mutually disjoint attributes and whose union is not
an information observable. For example, in quantum physics any set of two orthogonal states of a qubit constitutes an
information observable, but no union of two or more such sets does: its members are not all distinguishable." From
this one prohibition they derive (Sec. 8) that not all attributes are distinguishable (8.1), that sharpness cannot be
measured (8.2), no cloning (8.3), that two such observables cannot be jointly prepared or measured (8.4), and (8.9)
"locally inaccessible information", their word for what underlies entanglement: "some combined system S1 ⊕ S2 has
information variables that cannot be measured by measuring Cartesian products (nor subsets thereof) of variables of S1
and S2." Note also 8.9's last sentence: "the failure of local distinguishability is possible because superinformation
media obey the principle of locality II, not disobey it as has been supposed."

## 3. The two 2017 proposals

### Marletto and Vedral, PRL 119, 240402 (arXiv:1707.06036v2). Read in full (arXiv HTML).

**The argument.** "Suppose that C is 'classical', by which we mean that C has only a single observable T. This notion
of classicality is information-theoretic [21, 22] and sharply differs from other existing ones – e.g. the field being
in a coherent state, or its being a decoherent channel [28]." If C is classical the most general state of Qi ⊕ C is
their displayed ρ (one unnumbered equation), "This state, when interpreted as a two-qubit state, is separable ... Hence,
if Q1 and Q2 are found in an entangled state and if that entanglement has been mediated by the interaction with C, C
must have itself at least another observable complementary to T." The assumption: "The only assumption here is that the
interactions must be local – namely, there cannot be any action at a distance between Q1 and Q2 – and that Q1
interacts with C only, and so does Q2."

**The setup and numbers.** Two masses, each in a Mach-Zehnder interferometer; the joint state before the final
beam-splitters is their Eq. (1); the phases "φi = (m² G / ħ di) Δt" with Δt = L/v. Extremes: maximal entanglement at
φ1 = 2nπ, Δφ = π, p0 = p1 = 1/2 (their Eq. (2)). "For example, two coupled nano-mechanical oscillators of mass 10⁻¹²
kg interacting for a Δt = 10⁻⁶ s would achieve the extreme phase shifts, over distances d ≈ 10⁻⁶ m."

**What a null result means (their words).** "Failing to detect entanglement would not imply that gravity is not
quantum. It could be that our model is inadequate ... It could also be that the field is quantum, as defined above,
but it is a decoherent channel". And in the supplement: "our analysis implies that semi-classical versions of quantum
gravity (such as the one in quantum field theory in curved space-time) would not lead to any spatial entanglement
between the two masses." The supplement models the field as a coherent state displaced by the masses; the
field-to-mass entanglement is "1 − exp(−ξab) ≈ ξab" (their Eq. (3)) with αab = (m/mP)², "assuming that m = 10⁻¹² kg,
the degree of entanglement between the masses and the field could be 10⁻¹²", and this smallness does not stop the two
masses from becoming maximally entangled with each other.

### Bose et al., PRL 119, 240401 (arXiv:1707.06050v1). Read: abstract, the entanglement section, the Stern-Gerlach scheme and "An Explicit Scheme" (arXiv HTML).

Principle: "entanglement between two systems cannot be created by Local Operations and Classical Communication
(LOCC) [24]. ... Thus it immediately follows that if the mutual gravitational interaction entangles the state of two
masses, then the mediating gravitational field is necessarily quantum mechanical in nature." Their one assumption:
"the gravitational interaction between two masses is mediated by a gravitational field (in other words, it is not a
direct interaction-at-a-distance)."

Numbers (their Sec. "An Explicit Scheme" and the paragraph before Eq. (3)): masses "m1 ∼ m2 ∼ 10⁻¹⁴ kgs", micro-crystals
of radius "R ∼ 1 μm"; superposition size "Δx ∼ 250 μm" from a field gradient "∼ 10⁶ T m⁻¹" over "τacc ∼ 500 ms"; traps
"d ∼ 450 μm" apart; closest approach "d − Δx ∼ 200 μm", chosen so the Casimir-Polder potential is "∼ 0.1 of the
gravitational potential"; hold time "τ ∼ 2.5 s"; phases "Δφ_LR ∼ −0.2 and Δφ_RL ∼ 0.7"; the spin witness
W = |⟨σx⊗σz⟩ − ⟨σy⊗σz⟩| with "W ∼ 1.16" (entangled if W > 1); pressure "10⁻¹⁵ Pa" and internal temperature "0.15 K".
Their Eq. (3): the sum of the two phase differences should be of order one. Their last sentence of the abstract: the
entanglement "is shown to certify the presence of non-zero off-diagonal terms in the coherent state basis of the
gravitational field modes."

## 4. Marletto and Vedral, "Witnessing nonclassicality beyond quantum theory" (arXiv:2003.07974v3; Phys. Rev. D 102, 086012 (2020)). Read in full (arXiv HTML).

This is the General Witness Theorem in the form the record should cite. Its definitions, in order.

**States, attributes, locality.** "We will assume that M obeys a theory endowed with a set of allowed states for
physical systems and a partition of the whole universe into subsystems." "An attribute n of a substrate is the set of
all states where the substrate has a given property. A variable is a set of disjoint attributes of a substrate."
Principle 1 (Locality): "The state of a substrate is a description of it that satisfies two properties: 1) Any
attribute of a substrate, at any given time t, is a fixed function of the substrate's state; 2) Any state of a
composite substrate S1 ⊕ S2 is an ordered pair of states (s1, s2) of S1 and S2, with the property that if a task is
performed on S1 only, then the state of the substrate S2 is not changed thereby." They note that quantum theory
satisfies this in the Heisenberg picture and that it "implies no-signalling".

**Constructor.** "a constructor for it, which is defined as a substrate that, whenever presented with the substrates
in any of the input attributes of the task, delivers them in one of the corresponding output attributes, and,
crucially, retains the property of being capable of performing the task."

**Information medium (their Eqs. (4), (5)).** Copying and all permutations possible on an information variable X.
Principle 2 (Interoperability): "If S1 and S2 are information media, respectively with information variable X1 and X2,
their composite system S1 ⊕ S2 is an information medium with information variable X1 × X2".

**Superinformation and non-classicality.** "A superinformation medium is an information medium with at least two
information observables, X and Z, such that their union is not an information variable." The theorem needs less of
the mediator: "By a substrate being non-classical we shall mean an information medium M, with maximal information
observable T, that has a variable V, disjoint from T and with the same cardinality as T" satisfying three conditions
(their list 1 to 3: an entangled-type variable E on S1 ⊕ M exists; V ∪ T is not a distinguishable variable; E is
distinguishable only by measuring incompatible observables of a composite superinformation medium). Informally, in
their words at the top: "the mediator M must have at least two variables that cannot be measured to arbitrarily high
accuracy simultaneously (i.e. by the same measuring system)."

**Assumptions and theorem (Sec. 3).** "The mediator M is an information medium with a maximal information observable
T." "The two systems to be entangled, QA and QB, are qubits." Theorem 1: "If M can entangle QA and QB, by locally
interacting with each, then M is non-classical." The proof uses the copy task T_M (their Eq. (8)), in which "one can
think of z0 and z1 as two distinct locations of a mass; and of t0 and t1 as two distinguishable configurations of the
gravitational field, induced by two different mass distributions ... It is also possible to think of t0 and t1 as two
distinguishable spacetime geometries, solutions of Einstein's equations". The entangling task T_E (Eq. (9)) is split by
locality into T1 on QA ⊕ M and T2 on M ⊕ QB (Eqs. (10), (11)); the two mediator states m^{+0}, m^{−0} left after T1
are shown to be distinct, not distinguishable from t0 or t1, and readable only through complementary observables on
QA ⊕ QB.

**What the theorem rules out, and does not (Sec. 4, Discussion).** Mixtures are out: "By Bell's theorem, m^{α+} cannot
be a statistical mixture of t0 and t1, because, if it were, it would provide a local hidden variable model for quantum
entangled states of QA ⊕ QB. This argument, therefore, shows that collapse models, which would predict M to be in a
statistical mixture of the observable T, are incompatible with observing entanglement." What is not required: "M,
although capable of working as a faithful channel for creating entanglement between the two qubits, may not have the
full repertoire of operations such as preparation and measurement as a superinformation medium, let alone as a
qubit." And the generality claim: "It ensures that if entanglement is observed, then all classical models for gravity,
obeying our general principles, are ruled out." The invitation that section C below takes up: "it would be interesting
to understand what the mediator and its non-classical variable V are in each of the quantum gravity models that have
been proposed, particularly non-perturbative ones."

## 5. Marletto, "Constructor theory of thermodynamics" (arXiv:1608.02625v5). Read in part: Secs. 1, 1.1 and 2 (the constructor and the cycle), Sec. 7 (Kelvin's statement), from the PDF. And Marletto, Vedral, Knoll et al., "Emergence of constructor-based irreversibility in quantum systems: theory and experiment" (arXiv:2009.14649v2; PRL 128, 080401 (2022)). Read in part: the introduction and the definition of a constructor as a limit of machines, from the PDF.

**The cycle (thermodynamics paper, Sec. 1.1).** "A constructor (section 2) is an object that, if presented with one
of the task's designated inputs, produces (one of) the corresponding outputs, and retains the ability to do this
again. Thus it must operate 'in a cycle'. ... In reality no perfect constructor ever occurs, because of errors and
deterioration; but whenever a task is possible a constructor for that task can be approximated to arbitrarily high
accuracy." Sec. 2: "In traditional thermodynamics the system can be acted upon by a thermodynamic cycle – a sequence of
changes in the surroundings that start and end in the same thermodynamic state. ... A constructor is in turn a
substrate that undergoes no net change in its ability to do this – generalising a thermodynamic cycle." Adiabatic
accessibility (Sec. 1): "the physical transformation {x → y} can be brought about by a device capable of operating in a
cycle [a constructor], with the sole side-effect (on the surroundings) being the displacement of a weight in a
gravitational field."

**"Same state" is not required; "same set of states" is (irreversibility paper, after its Eq. (7)).** "The limiting
point of the sequence of machines {E[T]} is a constructor for the task T (please note that a constructor generalises
the notion of catalyst in resource theory [17], relaxing the requirement to stay in exactly the same state by saying
that it has to stay within the same set of states)." The machine is scored by a "relative deterioration" over n uses
at accuracy ε, with the order of limits "for a fixed accuracy ε, we let the number of usages go to infinity" (their
Eq. (7)). The 2026 review (Sec. 1.4) says the same: "catalysts must remain in the same state, as opposed to the same
attribute". This is the exact form of the cycle question in section A.

**Waste.** The word does not appear in the thermodynamics paper's text as extracted; the waste clause is Deutsch 2012,
Sec. 1.1 (quoted in section 1 above). The "arrow of time" paper named in the brief is, as far as the search went, the
irreversibility paper above (a task possible, its transpose not) and "Constructor theory of time" (arXiv:2505.08692,
abstract only); neither defines a cycle beyond the constructor definition.

## 6. "Tests of constructor theory" (Marletto, Deutsch, Vedral, arXiv:2606.07352v1, 5 June 2026). Read in part: abstract, Secs. 1 to 1.4, 2 to 2.4, 3.2, 5, from the arXiv HTML.

**Found.** arXiv search on 2026-11-02 for the exact title returned arXiv:2606.07352, posted 5 June 2026, authors
Marletto, Deutsch, Vedral, 736 lines of text. The text as read does not contain the strings "FQxI" or "Foundational
Review"; its acknowledgments name the Moore Foundation, the Eutopia Foundation, B. Vass and the Conjecture Institute.
So the FQxI series attribution rests on the owner's pasted article, not on the arXiv text; to verify against the
journal version when it appears.

**Its list of tests, as the paper gives it.** (i) The entanglement-based witness of non-classicality (Sec. 2.3), with
the BMV experiment as its gravity application (Sec. 2.3.1); (ii) the temporal witness, one probe plus a conservation
law (Sec. 2.4), with a biological molecule as a candidate mediator; (iii) constructor-based irreversibility, tested with
photonic qubits on the quantum homogeniser (Sec. 3.2); (iv) speculative: the Born rule from constructor-theoretic
axioms (4.1), the constructor theory of life (4.2), the universal constructor (4.3); and the closing list (Sec. 5):
post-quantum information, quantum biology, thermodynamics, and "Cosmology and quantum gravity: ... These constraints
can act as selectors of the initial conditions."

**Its statement of "classical" (Secs. 2.2, 2.3).** "The key assumption is that (M) possesses only a single observable
whose sharp states are all mutually distinguishable. ... The important point is that 'classical' here does not mean 'any
system described by classical Hamiltonian mechanics.' Ordinary classical systems can certainly have many observables,
such as position, momentum, energy, angular momentum, etc. However, all of those observables are jointly sharp and
mutually commuting". And Sec. 2.3: "a classical system is one whose observables are all jointly sharp, meaning that all
accessible properties can be reduced to a single commuting informational variable. Equivalently, (M) has distinguishable
states and probabilistic mixtures over them, but no incompatible observables analogous to non-commuting quantum
operators."

**What a BMV result would and would not do (Sec. 2.3.1).** "If GIE were successfully detected, it would provide the
first experimental contradiction of Einstein's general relativity as a purely classical theory of gravity". "GIE cannot
be used to falsify specific dynamical theories of quantum gravity. In the quasi-Newtonian regime where GIE emerges,
existing non-perturbative frameworks such as string theory and loop quantum gravity concur with the predictions of
linearised quantum gravity." And a null: "the absence of GIE in a carefully prepared experiment would raise several
equally interesting possibilities. It could indicate that gravity is fundamentally classical ... Alternatively, gravity
may indeed be quantum, but our current theoretical frameworks might be insufficient ... Another possibility is that the
principles of the constructor theory underlying the non-classicality witness are incorrect: this could refute either
locality or the interoperability of information."

**How principles are tested (Sec. 1.1).** "One must test them not by direct falsification of their predictions, but by
testing the subsidiary theories that comply with them, or by showing that given tasks that are ruled out by them are,
in fact, possible".

**Jones's NMR work.** Two papers, both Oxford. (a) Bhole, Jones, Marletto, Vedral, "Witnesses of non-classicality for
simulated hybrid quantum systems", J. Phys. Commun. 4, 025013 (2020): abstract through the IOP page, plus its experimental section as summarized by the fetch tool, not read verbatim. A four-qubit
NMR simulation (four ¹³C nuclei in labeled crotonic acid): the two outer qubits are the probes, the two middle ones the
mediator; entanglement passes along the chain only while the mediator stays quantum, and dephasing one mediator qubit
stops it. The 2026 review calls this "a quantitative model of the transition from a full non-classical behaviour (a
qubit) to a fully classical system (bit)" (Sec. 2.3.1). (b) Di Pietra, Bhole, Eaton, Baldwin, Jones, Vedral, Marletto,
"Temporal entanglement and witnesses of non-classicality", arXiv:2506.15474 (18 June 2025): abstract only. The temporal
witness, one qubit probe, "assuming a general conservation law, violating temporal Bell inequalities on the qubit
probe implies the non-classicality of the system", with "proof-of-principle experimental emulations ... using a three
qubit Nuclear Magnetic Resonance quantum computer." Neither is an experiment on gravity; both are simulations of the
witness logic on spins.

---

## A. The cycle question (ours, unverified)

**The hypothesis's turn.** Spacetime is one turn of a loop: a black hole's interior re-curls into the next X and
burps again (VISION Update 42: "it would not need more matter and energy from the hole for each burp; it could burp at
once"; Update 149: the rod, the pole, "they keep opening as each new two-dimensional space encloses a zero-dimensional
singularity to open a new spacetime into"). In Deutsch's words the turn is a candidate constructor: the thing that
performs the task (fuel in, a spacetime out) and "retains the ability to do this again" (Marletto 2016, Sec. 1.1). Its
substrates would be the energy it takes in and the spacetime it puts out; its allowed waste, under Deutsch Sec. 1.1, is
whatever the task's specification lists as "unavoidable outputs". The knots of paper 2 are exactly such an output: a
sprinkle of stuck arrangements of fixed energy whose number is set at the opening, not by the cooling (O104, O107:
every one of the 652 pieces of two and 103 of eight at L = 256 is a dip; the column 14 units, the knot of two kinds 20
to 30, the double column 8). Written as Deutsch's Eq. (6): fuel + curled X → spacetime + knots, with the loop as the
constructor. That is allowed. What is not allowed is for the constructor itself to run down (the battery, Sec. 1.1) or
to pile up what it takes in (the black hole of Sec. 2.2, "its size and gravitational effects would increase whenever
it was used"). So the question constructor theory puts to the loop is not whether it leaves knots but whether the
curled thing that burps comes back within the same set of states each turn, with the knots in the product and not in
the constructor.

**What the toy has already measured.** The fed slab under the layer form (T71; O144, O160) is the toy's one cycle.
In 17 of 18 cells (λ = 1.10, 1.25, 1.40; r = 1/64 and 1/16; L = 8, 12 and the held-out 16) every slab's worth fed
becomes one daughter carrying exactly a N_slab (to 1e-9), the slab reforms, and it does so 40 to 340 times a replica
with a period of 13 to 101 sweeps and no clean-switch move ever fired: the parent returns to the same arrangement each
time, as far as the energy ledger can tell. In the one cell where the feed outruns the chain (λ = 1.10, r = 1/16) the
stores pile up "to 25,000 to 95,000 at L = 12, about 30 to 110 per point", a clean two-switch move fires after the
first burp, the daughters carry 0.89 to 0.99 of a N_slab, and the end states carry "rewired patches (end energy above
flat 128 to 528 at L = 12, with 24 to 84 points off the ladder in 11 replicas)". Read in Deutsch's terms: at 17 settings
the slab is a constructor for "feed → daughter" to the accuracy measured; at one it is Sec. 2.2's sequestering black
hole, piling up what it takes in and deteriorating. The record's own rule-11 answer (O144 (2), (3)) says this is a
clock choice of the protocol, not a property of the slab, and names the cheaper test: more layer proposals a sweep, or
a slower feed. That test is also the constructor test.

**What the toy has not measured.** The daughter in T71 is a ledger, an energy account, not a wiring; nothing in T71
opens a space or leaves a knot, because layer moves are coordinated and leave no seams (O107's "no seam forms"). The
knots come from a different protocol: a tube opening from several seeds in a bath on the fair clock (T51, T55). And
under the switch model no fold test re-curled anything (T34, T57 and their relatives; Update 149 (v)), so the toy has
no measured cycle in which a product with wiring is made and the parent re-curls by its own dynamics. So "does the turn
return to the same state, knot count included" cannot be read from any existing run; it needs the two protocols
joined, and the honest statement is that the join is a construction of ours.

**Proposed registration (a draft for the owner; not written into PREREGISTRATION.md by this note).**

- *Question.* Over K repeated cycles of the fed slab under the layer form, does the parent return to the same
  arrangement after every daughter, and does each daughter, delivered as a spark to a cold tube, leave the same
  number of knots?
- *Protocol.* Stage A (the parent): T71's model arm and layer arm, same λ and r grid, with the number of layer
  proposals a sweep raised so that the chain keeps pace at r = 1/16 (O144 (3)), run to K = 200 daughters; and the
  original one-proposal setting kept as a control at the two cells where the clean move fired. Stage B (the product):
  each daughter's energy delivered as a local spark to a cold curled tube of the matching length under T51's protocol
  on the fair clock, cooled over T51's slowest schedule, and read by T55's reader. The two stages are joined by the
  ledger only; the toy has no move that turns a ledger into a wiring, and that is said in the registration.
- *Observables, named.* Stage A: (i) the parent's energy above the slab's own rung after each refold (exact zero is
  the same state; T71 reads F from the rows); (ii) points off the ladder after each refold (`local_dimension_d`
  census, 0 is the same state); (iii) the stores held by the parent after each refold (the sequestering test; a
  bounded, non-growing value is Deutsch's "no net change", a growing one is his Sec. 2.2 black hole); (iv) energy per
  daughter against cycle index. Stage B: (v) knots per daughter by kind (column, knot of two kinds, double column)
  against cycle index. Verdict words: SAME STATE (i to iv constant to the tolerance over K at a setting), DETERIORATES
  (ii or iii grows monotonically with K), and for stage B FIXED WASTE (v has no trend with cycle index) or DRIFTS.
- *Her prediction.* Owed before any run.
- *Ours.* SAME STATE at every setting where the chain keeps pace, DETERIORATES in the one-proposal control cells
  (the record's clean-move cell already shows the first steps of it); FIXED WASTE, with the mean knots per daughter set
  by the nucleation rate per length on the fair clock (T37; paper 2) and not by the cycle index, because each spark
  meets a fresh cold tube. If DETERIORATES appears at a setting where the chain keeps pace, the slab's turn is not a
  constructor in this family and the word is dropped from the pages.
- *Held-out size (rule 14).* Fit on L = 8 and 12; hold out L = 16. Disclosure: T71's L = 16 rows exist (O160) and
  were read for T71's observables; observables (ii), (iii) per cycle and (v) have not been read from them, and the
  prediction for L = 16 is written from L = 8 and 12 before any L = 16 row is opened for them. If the owner prefers a
  size no run has touched, L = 20 (6,400 points) is the alternative and its cost is to be priced first.

**One more thing the reading says about claim 6.** The hypothesis's conserved energy-like quantity across the
transition (claim 6; sealed runs hold it to the last unit) is what Deutsch's "stronger conservation law" asks of a
constructor's substrates (Sec. 2.2). The toy's ledger identity, held to 1e-9 (Q24, O158 addendum), is an accounting
identity and not physical conservation; the record already says so, and it should keep saying so if Deutsch is cited.

## B. The entanglement fork (ours, unverified)

**What the toy's carriers are, in the theorem's terms.** Every carrier in `docs/design/gravity_carriers_2026-11-01.md`
is a classical variable: A, a real number per point; B, a real length per link (`graphity.edge_wave`); C, a number
per point setting a local pace; E and G, links or phases kept by rule; F, walkers. Each is sampled or evolved by a
Monte Carlo chain, so its state at any time is one sharp configuration and its statistics are a probabilistic mixture
over sharp configurations. That is "classical" in exactly the sense the General Witness Theorem uses: "all accessible
properties can be reduced to a single commuting informational variable. Equivalently, (M) has distinguishable states
and probabilistic mixtures over them, but no incompatible observables" (review, Sec. 2.3), and the Discussion of
Marletto and Vedral 2020 closes the mixture loophole by Bell's theorem. Candidate D (interchangeable points) is not a
field at all, "a weight on whole arrangements, not a field; it carries nothing between two places" (carriers note),
so it is not a mediator in the theorem's sense and the question does not arise for it. The counting leg of the quantum
sentence is in the same position for a different reason: O29 shows a renaming of a fixed arrangement is "a complete
instruction set", a local hidden variable, and the 2020 Discussion says a mediator whose states are such mixtures
"cannot" entangle the probes.

**Which of the theorem's assumptions the toy meets.** Locality, Principle 1: the toy's energy is a sum of per-link
terms (O22), a switch changes two links, the sealed and bath protocols act on a point or a patch, and the state of two
far-apart regions is the pair of their wirings; a task on one region does not change the other's wiring. So the toy's
dynamics meet the ordered-pair locality as far as a classical model can (the exception is D, whose weight is a function
of the whole arrangement; it is set aside above). A mediator with attributes: a carrier field has attributes (its
configurations) and they are copiable and permutable by the chain, so it is an information medium with one maximal
observable T; that is the theorem's classical case. What the toy lacks entirely is the other side of the theorem: the
probes. There are no qubits in the toy, no superinformation medium, nothing with two observables whose union is not an
information variable (Update 20, 21: the counting gives only signs and no amplitude rule has been adopted). So the
theorem does not run inside the toy; it runs on reality, with the toy's carrier as the hypothesis's claim about what
gravity is.

**The prediction, in the papers' own terms.** If the hypothesis's carrier of gravity is any item on the toy's menu,
then by Theorem 1 of Marletto and Vedral 2020 it cannot entangle two masses by local interaction, so the hypothesis
predicts for the Bose-Marletto-Vedral experiment: the two masses stay separable; in Bose et al.'s witness, W ≤ 1
(their W ∼ 1.16 is what linearized quantum gravity gives at m ∼ 10⁻¹⁴ kg, d ∼ 450 μm, τ ∼ 2.5 s); in Marletto and
Vedral 2017's Eq. (2), the ordinary single-mass interference pattern with no loss of visibility from the other mass.
This is the branch "gravity is fundamentally classical" of the review's Sec. 2.3.1, and it is the same prediction as
general relativity's and as semiclassical gravity's (2017 supplement: "semi-classical versions of quantum gravity ...
would not lead to any spatial entanglement"). The fork: an observed W > 1, mediated by gravity alone, rules out every
carrier on the toy's menu as the carrier in reality, provided locality and interoperability hold; the hypothesis would
then need a non-classical carrier. A null result is consistent with the menu but, in the authors' own words, "would not
imply that gravity is not quantum", and under rule 13 it is not evidence for the hypothesis.

**What would change with a quantum carrier.** The theorem needs only two incompatible variables in the mediator, not
the full quantum formalism; in the 2017 supplement the two are the complementary observables (a − a†)/2i and a†a (their text
before Eq. (3)), and in the 2020 paper the variable V, "the descriptors of the quantum Heisenberg picture". In the toy
the nearest object is carrier B, the link-length field, which already has a wave equation (gapless, speed one link per
sweep) and, with decision (3) of the waves brief, two polarizations; quantizing its modes would give exactly the
amplitude and phase pair the supplement uses, and the entanglement between field and masses would be of order
(m/mP)², small, while the masses could still become maximally entangled. Adopting that is the amplitude rule the owner
held on 23 September (Update 21: "quantum mechanics put in, not derived"; Hardy's fifth axiom), now applied to the
carrier rather than to a loop of four. It is a knob under S1 and her decision. Its consequence for the fork is plain:
with a quantum carrier the hypothesis predicts W > 1 as linearized quantum gravity does, and the review's Sec. 2.3.1
says the experiment "does not distinguish one quantum gravity theory from another" in that regime, so a positive BMV
result would not be evidence for the hypothesis either (rule 13); and the toy's Monte Carlo could not compute the
entanglement, so the prediction would be made by the published linearized calculation, not by any run here.

**What is exact and cheap, needing no decision.** The classification above of each carrier as classical in the
theorem's sense is a statement about the code and can be written into the carriers note's table as a column ("meets
the theorem's 'classical'": yes for A, B, C, E, F, G; not a mediator for D). That is the one line this reading adds to
the record without a run.

## C. Rule 13, and what a letter could ask (ours, unverified)

**Rule 13 first.** Constructor theory and the witness theorem are targets. Deutsch's principles are, by his own
word, conjectures (Sec. 4), and they are tested through the subsidiary theories that obey them (review, Sec. 1.1). The
hypothesis gains nothing from resembling them: that the loop's turn can be phrased as a constructor, that the exact
results are statements of impossible tasks, and that claim 6 reads like Deutsch's stronger conservation law are
restatements, not results. What the reading supplies is two things the hypothesis must now carry: the cycle
requirement of section A (the constructor must come back within the same set of states, with the knots in the product),
and the fork of section B (a classical carrier predicts no gravity-induced entanglement, and that prediction is shared
with general relativity, so it cannot single the hypothesis out).

**The narrow question for Chiara Marletto.** Her papers answer, for quantum theory and for general relativity, that
both satisfy the locality principle in its ordered-pair form (2020, Sec. 4: "satisfied by both quantum
theory and general relativity"), and they ask, of other quantum-gravity models, "what the mediator and its
non-classical variable V are" (2020, Sec. 4). They do not say what the theorem makes of a mediator whose states are
discrete arrangements weighted by a global symmetry count. In the owner's model the points of the network can be
interchangeable, and then an arrangement's weight is divided by the number of its renamings (Update 12; Q15; O55), a
number that depends on the whole arrangement and not on any ordered pair of parts. Phrased for her letter, in plain
words:

> "In your witness theorem the mediator has to obey a locality principle: the state of two parts together is the
> pair of their separate states, and acting on one part leaves the other's state alone. In the toy model I work with,
> gravity's carrier would be a discrete network, and when its points are treated as interchangeable (as identical
> particles are) the weight of an arrangement depends on a symmetry count of the whole network, not on its parts. Does
> a mediator of that kind satisfy your locality principle at all, and if it does, is it classical in your sense, so
> that your theorem predicts it cannot entangle the two masses in the Bose-Marletto-Vedral experiment?"

Why it is inside her work and not already answered: the locality principle is hers (2020, Principle 1; Deutsch 2012,
Sec. 3.10), the classical-mediator definition is hers (2020, Sec. 2, "Non-classicality"), and the 2020 Discussion
explicitly leaves open how the theorem reads on non-perturbative and discrete models of gravity. It is one question, it
needs no knowledge of the hypothesis beyond the sentence given, and either answer is useful: "it violates locality"
means the interchangeable-points knob is outside the theorem's reach and the fork of section B applies only to the
named-points carriers; "it is classical" means the fork applies to the whole menu, D included. Under the owner's
outreach preferences the letter discloses the AI drafting and checks her most recent papers first; the 2025 Rev. Mod.
Phys. review ("Rev. Mod. Phys. 97, 015006 (2025)", cited as [28] in the 2026 paper) has not been read and should be
before the letter goes, since it may already answer the question.

---

## Read-status table

| Key (proposed) | Paper | arXiv | Read status | Route |
|---|---|---|---|---|
| [Deu13] | Deutsch, "Constructor theory", Synthese 190, 4331 (2013) | 1210.7439v2 | Read in full (40 pages) | PDF, PyMuPDF text; ar5iv page was a stub (4.7 kB) |
| [DM15] | Deutsch, Marletto, "Constructor theory of information", Proc. R. Soc. A 471, 20140540 (2015) | 1405.5563v2 | Read in part: Secs. 3 to 7, 8.1 to 8.4, 8.9 | PDF, PyMuPDF text (set notation partly mangled: ⊥ and its negation print alike; quotations here avoid those symbols); ar5iv stub |
| [MV17] | Marletto, Vedral, PRL 119, 240402 (2017) | 1707.06036v2 | Read in full, supplement included | arXiv HTML, converted to text by this agent |
| [BMV17] | Bose et al., PRL 119, 240401 (2017) | 1707.06050v1 | Read in part: abstract, entanglement section, Stern-Gerlach scheme, explicit scheme, decoherence; not the Casimir-Polder appendix or the later "Overcoming challenges" in full | arXiv HTML, converted |
| [MV20] | Marletto, Vedral, "Witnessing nonclassicality beyond quantum theory", Phys. Rev. D 102, 086012 (2020) | 2003.07974v3 | Read in full | arXiv HTML, converted |
| [Mar16] | Marletto, "Constructor theory of thermodynamics" | 1608.02625v5 | Read in part: Secs. 1, 1.1, 2, 7 | PDF, PyMuPDF text; ar5iv stub |
| [MVK22] | Marletto, Vedral, Knoll, Piacentini, Bernardi, Rebufello, Avella, Gramegna, Degiovanni, Genovese, "Emergence of constructor-based irreversibility in quantum systems: theory and experiment", PRL 128, 080401 (2022) | 2009.14649v2 | Read in part: introduction and the constructor-as-limit definition through Eq. (7) | PDF, PyMuPDF text |
| [MDV26] | Marletto, Deutsch, Vedral, "Tests of constructor theory" | 2606.07352v1 (5 June 2026) | Read in part: abstract, Secs. 1 to 1.4, 2 to 2.4, 3.2, 5, acknowledgments, reference list; not 3.1, 4.1 to 4.3 or the appendix | arXiv HTML, converted |
| [BJMV20] | Bhole, Jones, Marletto, Vedral, "Witnesses of non-classicality for simulated hybrid quantum systems", J. Phys. Commun. 4, 025013 (2020) | 1812.09483 (found by the second agent through the arXiv API) | Abstract, plus the experimental section as summarized by the fetch tool, not read verbatim (IOP page, by fetch-tool summary) | web |
| [DPJ25] | Di Pietra, Bhole, Eaton, Baldwin, Jones, Vedral, Marletto, "Temporal entanglement and witnesses of non-classicality" | 2506.15474 | Abstract only | arXiv abstract page |
| [DM25] | Deutsch, Marletto, "Constructor theory of time" | 2505.08692v3 | Abstract only | arXiv abstract page |
| (none) | Marletto, Vedral, Rev. Mod. Phys. 97, 015006 (2025), the BMV review cited as [28] in [MDV26] | not searched | Not read | |

All arXiv HTML renders carry a generation date of "August 24, 2026" in their header; the version numbers above are
the arXiv versions the renders are of. Searches: arXiv and web, 2026-11-02, "Tests of Constructor Theory" Marletto
Deutsch Vedral (found 2606.07352); "Jonathan Jones NMR entanglement witness Marletto" and "Jones Marletto Vedral NMR
witness non-classicality 2025 2026" (found [BJMV20] and [DPJ25]; no 2026 NMR paper found); "Marletto arrow of time
constructor theory irreversibility cycle" (found [MVK22] and [DM25]).

## What is owed

1. `REFERENCES.bib` entries for the eleven rows above, with the read status in each `note` field as the table gives
   it, before any of them is cited on a page. The keys are proposals; none exists in the bib on this date (checked:
   no Deutsch, Marletto or Vedral entry; the one "Bose" is a different author).
2. The owner's prediction for the cycle registration of section A, and her decision whether it is written into
   PREREGISTRATION.md at all; the registration is a draft here and nowhere else.
3. A column in `docs/design/gravity_carriers_2026-11-01.md` recording each carrier's status under the theorem's
   "classical" (section B, last paragraph), if she wants it.
4. The 2025 Rev. Mod. Phys. review read before any letter is sent (section C).
5. Verification of this note's quotations against the PDFs by a second agent, as was done for the 1 November notes;
   the HTML-converted ones ([MV17], [BMV17], [MV20], [MDV26]) first.
6. The FQxI attribution of [MDV26] to verify against the journal version; the arXiv text does not carry it.

Verified against the sources by a second agent on 2026-11-02 (ninety-odd quotation strings matched); its eight corrections applied the same day.

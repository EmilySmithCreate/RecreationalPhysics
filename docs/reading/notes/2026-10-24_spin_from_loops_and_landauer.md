# Reading: spin one half from loops in configuration space (Finkelstein and Rubinstein), and Landauer's bound

Reading task 3 and 4 of `docs/design/particle_handoff_brief_2026-10-24.md` (the table of readings: "Spin from
configuration-space loops", "Landauer's bound"). It checks two statements the record already makes in
`sandbox/out/particle_handoff_looks_2026-10-24.txt` (part 4, the 2π gate; part 6, her entropy idea), in the brief's
items 4 and 7, and in ASSUMPTIONS O154 (5). **No tracked file other than this note is changed.**

Kinds of statement (rule 10): **published** (with how much was read), **exact** (arithmetic or a standard theorem
quoted from a source read here), **ours** (interpretation, unverified), **hers** (the owner's). "General knowledge, to
verify" marks a physics or mathematics statement from memory, not checked at a source in this session.

**Date:** 2026-10-24. **Who read:** an assistant agent (Claude), working from the worktree; the owner has read none of
the sources below. PDFs were downloaded to the session's scratchpad and read as text (PyMuPDF) or, for the scanned
Landauer reprint, as page images.

## 1. Sources and read status

| Key | Source | Read status |
|---|---|---|
| [FR68] | D. Finkelstein and J. Rubinstein, "Connection between spin, statistics, and kinks", J. Math. Phys. 9, 1762–1779 (1968), doi:10.1063/1.1664510 | **Not read.** No open copy found (one web search, 24 October). Everything said about it below comes from the three papers that describe it, and is marked so. |
| [Kru03] | S. Krusch, "Homotopy of rational maps and the quantization of Skyrmions", Ann. Phys. 304, 103–127 (2003), doi:10.1016/S0003-4916(03)00014-9, arXiv:hep-th/0210310 | Sec. 2.1 ("Finkelstein-Rubinstein Constraints"), Eqs. (2)–(8), read in full; rest not read. |
| [KS06] | S. Krusch and J. M. Speight, "Fermionic quantization of Hopf solitons", Commun. Math. Phys. 264, 391–410 (2006), doi:10.1007/s00220-005-1469-4, arXiv:hep-th/0503067 | Introduction and Sec. 4 ("Finkelstein-Rubinstein constraints"), Eqs. (4.1)–(4.4), read in full; rest not read. |
| [AKS06] | D. Auckly, L. Kapitanski and J. M. Speight, "Geometry and analysis in non-linear sigma models", St. Petersburg Math. J. 18, 1–31 (2006), arXiv:hep-th/0411101 | Sec. 2.2 ("The fundamental group of configuration space"), around Theorem 3, read; rest not read. |
| [Hat02] | A. Hatcher, *Algebraic Topology*, Cambridge University Press (2002), free edition at pi.math.cornell.edu/~hatcher/AT/AT.pdf | Example 1.43 (π₁ of real projective space) and the opening of Sec. 3.D (SO(3) ≈ RP³; the double cover S³ → SO(3)), read. The citable text for π₁(SO(3)) = Z₂. |
| [Lan61] | R. Landauer, "Irreversibility and heat generation in the computing process", IBM J. Res. Dev. 5, 183–191 (1961), doi:10.1147/rd.53.0183 | Read from the IBM reprint (IBM J. Res. Dev. 44, 261–269, 2000; hosted on J. Norton's Pitt lecture pages), pages 261–266 (abstract, Secs. 1–4 and the start of Sec. 5) read in full as page images; Sec. 5's kinetics (pp. 267–269) not read. |
| [Ben03] | C. H. Bennett, "Notes on Landauer's principle, reversible computation, and Maxwell's demon", Stud. Hist. Phil. Mod. Phys. 34, 501–510 (2003), arXiv:physics/0210005 | Read in full to the start of its last section ("Landauer's principle in the context of other ideas ..."), i.e. pp. 1–5 of the arXiv version; the last section's remainder not read. |
| [LW03] | M. Levin and X.-G. Wen, "Fermions, strings, and gauge fields in lattice spin models", Phys. Rev. B 67, 245316 (2003), arXiv:cond-mat/0302460 | Abstract only (arXiv page, through a summarising fetch). |
| [LW06] | M. Levin and X.-G. Wen, "Quantum ether: photons and electrons from a rotor model", Phys. Rev. B 73, 035122 (2006), arXiv:hep-th/0507118 | Abstract only (arXiv page, through a summarising fetch); already in `REFERENCES.bib` from O154. |

`REFERENCES.bib` already holds [FR68] and [Lan61] as "Not read". This note does not edit the bibliography. Owed when
it is next edited: [Lan61] becomes "pp. 261–266 of the 2000 reprint read (Secs. 1–4)"; [FR68] stays "Not read,
described via [Kru03] Sec. 2.1 and [KS06] Sec. 4"; [Kru03], [KS06], [Hat02], [Ben03] are added with the statuses above.

## 2. Terms, in plain words

- **Configuration space.** The set of every arrangement the system can be in, treated as a space: two arrangements are
  "near" if one can be changed into the other a little. For a field, a point of it is a whole field; for the toy, a
  point would be one wiring with all its labels.
- **A loop in it.** A continuous sequence of arrangements that ends where it started (for example: take an object
  and rotate it slowly through a full turn).
- **Contractible / non-contractible loop.** A loop is contractible if it can be shrunk, through a continuous family
  of loops, to "do nothing". A non-contractible loop cannot: it goes round a hole in the space.
- **π₁ (the fundamental group).** The loops at a point, with two loops counted as the same if one can be deformed into
  the other; going round one loop and then another is the group's product. π₁ = 0 means every loop shrinks. π₁ = Z₂
  means there is one loop that cannot be shrunk, and going round it twice can.
- **π₁(SO(3)) = Z₂ and the belt trick.** SO(3) is the space of all rotations of 3D space. A full 2π turn, as a loop
  in SO(3), cannot be shrunk; a 4π turn (twice round) can. [Hat02] Example 1.43 proves π₁(RPⁿ) ≅ Z₂ for n ≥ 2, and
  Sec. 3.D proves SO(3) is homeomorphic to RP³ (quoted below). The belt trick (also "Dirac's string trick", "plate
  trick") is the hands-on demonstration: an object tied by a belt or strings to a fixed wall, turned once (2π),
  leaves the belt twisted in a way no motion of the belt alone can undo; turned twice (4π), the belt can be untangled
  without turning the object back. *The attribution to Dirac and the demonstration itself: general knowledge, to
  verify; no source for it was read.*
- **Double cover.** A space that sits two-to-one over another, like the sphere S³ over SO(3): each rotation has two
  points above it, and a 2π loop in SO(3) lifts to a path from one of the two to the other. [Hat02] Sec. 3.D: the map
  S³ → SO(3) is "the universal cover", and SO(3) is the quotient of S³ by {±1}.
- **Spinor.** A quantity that changes sign under a 2π rotation and returns only after 4π: something that lives on the
  double cover. Spin one half is the spinor case (general knowledge, to verify).
- **Finkelstein–Rubinstein constraint.** If a field theory's configuration space has a non-contractible loop, its wave
  function may be defined on the covering space and required to change sign round that loop. If a 2π rotation of an
  object is such a loop, the object then has half-integer spin, with nothing spinorial put into the field itself.
  The constraint is the rule that fixes the sign for each symmetric configuration (equations quoted below).
- **Landauer's bound.** Merging several distinguishable states of a memory into one (erasing it) lowers the memory's
  entropy; the second law then requires at least that much entropy to appear elsewhere. With the surroundings a heat
  bath at temperature T, that means at least kT ln 2 of heat per bit erased, kT ln W for W equally likely states.
- **Logical irreversibility** (Landauer's term): an operation whose output does not determine its input (two or more
  inputs, one output). **Thermodynamic irreversibility**: a process that increases the total entropy of the world.
  [Ben03]'s point is that the first does not always imply the second (quoted below).

## 3. What the sources say, with quotations

### 3.1 Finkelstein and Rubinstein, as described by [Kru03], [KS06], [AKS06]

- **The idea** ([Kru03] Sec. 2.1, p. 4): "Finkelstein and Rubinstein argued that if the configuration space Q* is not
  simply connected, then the wave functions have to be defined not on configuration space Q*, but on the covering
  space of configuration space CQ*."
- **Why Z₂ for the Skyrme model** ([Kru03] Eq. (2)): π₁(Q*_B) ≅ π₄(S³) ≅ Z₂, from Finkelstein's earlier paper
  ("Kinks", J. Math. Phys. 7, 1218 (1966), not read) and a theorem of Whitehead.
- **The sign is a choice** ([Kru03] Eqs. (6)–(7), p. 5): the deck move L_a satisfies L_a ψ = e^{iφ} ψ, and π₁ = Z₂
  forces e^{2iφ} = 1. "If the phase is trivial then we can define the function on Q*_B. In physicists' language, this
  corresponds to a theory which only contains bosons. Therefore, we impose a nontrivial phase L_a ψ = −ψ." [KS06]
  Sec. 4, p. 8, says the same: "In order to allow for fermionic solitons, we must consistently choose the latter
  possibility: our wavefunctions must always be odd under Π."
- **The constraint** ([Kru03] Eq. (8); [KS06] Eq. (4.4)): for a configuration invariant under a rotation by α combined
  with an isorotation by β, e^{−iα n·J} e^{−iβ N·I} ψ = +ψ if the induced loop is contractible, −ψ otherwise.
- **Spin one half from it** ([Kru03] p. 5): "When a 2π rotation gives rise to a nontrivial loop then this
  corresponds to half integer spin." [KS06] p. 8: "every allowable state in this sector aquires a minus sign under
  spatial rotation by 2π, the hallmark of spinoriality."
- **The spin–statistics theorem of [FR68]** ([Kru03] p. 5): "Q*_B admits half integer spin if and only if it admits
  odd exchange statistics." ([KS06] p. 8: the equivalence "was proved by Finkelstein and Rubinstein".)
- **The precondition, stated by [KS06]** (Introduction, p. 2): solitons "can consistently be quantized as fermions
  provided the fundamental group of configuration space has a Z₂ subgroup generated by a loop in which two identical
  solitons are exchanged."
- **Odd and even composites** ([AKS06] Sec. 2.2, p. 9): "The loop in configuration space represented by a compound
  particle making a full rotation is trivial in the fundamental group if the compound particle consists of an even
  number of basic particles, and is non-trivial if the compound particle consists of an odd number of basic
  particles. This observation is the basic motivation behind Finkelstein and Rubinstein's method".

### 3.2 π₁(SO(3)) = Z₂ ([Hat02])

- Example 1.43 (Sec. 1.3): from the covering Sⁿ → RPⁿ, "we deduce that π₁(RPⁿ) ≈ Z₂ for n ≥ 2."
- Sec. 3.D ("The Cohomology of SO(n)", pp. 293–294 of the printed book): "SO(3) is homeomorphic to RP³", by sending a
  vector x in the ball D³ to the rotation through |x|π about x, with antipodal boundary points (rotations by π about
  opposite directions) identified. And: restricting a quaternion map to the diagonal "gives the universal cover
  S³ → SO(3), so SO(3) is isomorphic to the quotient group of S³ by the normal subgroup {±1}."
- Same book, Sec. 1.3 (in the discussion of finite groups acting on S³): the rotation groups of the regular solids
  lift two-to-one to the "binary" groups in S³, among them O*₄₈ over the 24 rotations of the cube. *Ours, from this
  passage:* the cubic lattice's rotation group has a double cover of order 48, and a spin-one-half lattice object
  would transform under it.

### 3.3 Landauer [Lan61]

- **Abstract:** logical irreversibility "is associated with physical irreversibility and requires a minimal heat
  generation, per machine cycle, typically of the order of kT for each irreversible function."
- **The definition** (Sec. 3): "We shall call a device logically irreversible if the output of a device does not
  uniquely define the inputs."
- **The bound** (Sec. 4, p. 265 of the reprint): resetting a thermal ensemble of bits to ONE, "the number of states
  covered in the ensemble has been cut in half. The entropy therefore has been reduced by k logₑ 2 = 0.6931 k per bit.
  The entropy of a closed system, e.g., a computer with its own batteries, cannot decrease; hence this entropy must
  appear elsewhere as a heating effect, supplying 0.6931 kT per restored bit to the surroundings. This is, of course,
  a minimum heating effect, and our method of reasoning gives no guarantee that this minimum is in fact achievable."
- **Beyond one bit** (Sec. 4, p. 266): a three-bit machine mapping eight equally likely states onto four with
  probabilities 1/8, 1/8, 3/8, 3/8: "The difference S_i − S_f is 1.18 k. The minimum dissipation, if the initial state
  has no useful information, is therefore 1.18 kT." So the bound is k T times the drop in the Shannon–Gibbs entropy
  −k Σ p ln p, not only k T ln 2 per bit.
- **Known inputs cost nothing** (Sec. 4, p. 265): "if the initial states are all ZERO they also carry no information,
  and no entropy change is involved in resetting them all to ONE", and (p. 266) the cost "can be reduced, but only by
  taking advantage of our knowledge about the inputs".
- **A condition set aside** (Sec. 4, p. 265): "We shall ignore in this Section ... the case in which the ONE and ZERO
  are represented by states with different entropy."

### 3.4 Bennett [Ben03]

- **The principle** (p. 1): "any logically irreversible manipulation of information, such as the erasure of a bit or
  the merging of two computation paths, must be accompanied by a corresponding entropy increase in non-information-
  bearing degrees of freedom of the information processing apparatus or its environment."
- **Where the entropy goes** (p. 1): "Typically the entropy increase takes the form of energy imported into the
  computer, converted to heat, and dissipated into the environment, but it need not, since entropy can be exported in
  other ways, for example by randomizing configurational degrees of freedom in the environment."
- **Logical against thermodynamic irreversibility** (p. 1 and p. 4): erasing random data is thermodynamically
  reversible, "a reversible transfer of entropy from the data to the environment, rather like ... when a gas is
  compressed isothermally"; erasing known data is thermodynamically irreversible.
- **Its status** (p. 5, after Earman and Norton): if the demon "is a thermodynamic system already governed by the
  Second Law, no further supposition about information and entropy is needed to save the Second Law". So the bound is
  the second law applied to the merging, not an extra law.

## 4. Check (a): the Finkelstein–Rubinstein route to spin one half

**The record's statement** (handoff looks, part 4; brief item 4): a full turn of the cubic lattice returns every link
label, so any state built on link labels comes back with +1; spin one half needs spinor variables put in, or a loop in
configuration space that cannot be shrunk with a sign chosen round it (Finkelstein–Rubinstein).

**Verdict: correct, and it can be stated more sharply.**

1. **The first half is the bosonic case of [Kru03] Eq. (7), exactly.** A wave function that is a function of the
   configuration alone ("defined on Q*_B") is the case [Kru03] calls "a theory which only contains bosons". Labels
   permuted by the rotation and returned by four quarter turns are this case. *Ours, exact (group theory, general
   knowledge, to verify):* on any space of states spanned by label configurations, with a lattice rotation acting by
   permuting labels, the cube's 24 rotations act as an ordinary (linear) representation; spin one half needs a
   projective one, the binary group O*₄₈ of [Hat02] Sec. 1.3, in which the 2π element acts as −1. Permutations of
   labels never give that.
2. **What [FR68] needs, precisely (as [Kru03] and [KS06] state it).** (i) A configuration space with a continuous (or
   at least cell) structure, so that loops and their deformations mean something; (ii) a loop that cannot be shrunk,
   and for spin specifically, the loop "rotate the object by 2π" must be one of them; (iii) a **choice**: the wave
   function is required to be odd round that loop (Eq. (7)); the even choice is equally consistent and gives bosons.
   [KS06] states the Skyrme-model precondition as π₁ containing a Z₂ generated by an exchange loop. *Ours, unverified:*
   "π₁ contains Z₂" is the form the Skyrme and Hopf cases take; what spin needs is only that the 2π rotation loop is
   non-contractible. If that loop had infinite order, the sign −1 could still be chosen, but so could any phase, which
   in 2D is the anyon case (general knowledge, to verify).
3. **The toy's configuration space, as it stands, has no loops.** *Ours, exact as stated:* the set of the toy's states
   (a wiring plus integer twist labels: signed thirds on body diagonals, signed halves on face diagonals, Update 97) is
   a finite set; as a space it is discrete, and π₁ of a discrete space is trivial. A rotation of the lattice is not a
   path through states either: there is no state "rotated by 10°", only the quarter turn, which jumps. So condition
   (i) fails before (ii) can be asked. The U(1) link phases of `graphity.u1` do form a continuous space, but for a
   fixed wiring it is a torus of angles, whose π₁ is a free abelian group Zⁿ with no element of order two (general
   knowledge, to verify); and the lattice rotation still acts on it by permuting links, so the 2π rotation is not a
   loop in it at all.
4. **Could a framed ribbon or twisted strand on a lattice supply it?** *Ours, unverified,* three routes, from nearest
   to the toy outward:
   - **Build the loop space from the moves.** Take the toy's states as points, its moves as edges between them, and
     declare some cycles of moves to be fillable (2-cells). π₁ of the result is fixed by which cycles are declared
     fillable; a graph alone has a free π₁, never one with Z₂ in it, so a Z₂ appears only through that declaration.
     The declaration is then the physics, put in by hand, and it would have to be justified (for example, by asking
     that the move-complex of a tethered ribbon on the lattice reproduce the belt trick: a sequence of moves turning
     the ribbon's end by a full turn that cannot be filled, and its double that can).
   - **The belt trick as the tether.** A closed band rotated rigidly is unchanged; the 2π loop is non-contractible
     only for an object **tied to the rest** (the belt to the wall, or [AKS06]'s particle to its surrounding field).
     So her electron as a closed 360° band (Update 97) would not be spinorial by itself; a spinor would need its
     attachment to the surrounding graph to be part of the configuration. In the belt trick a full turn of the end
     adds one full twist to the belt, and two full twists can be undone by moving the belt round the end: so only the
     **twist mod 2** survives once the end may turn. The toy's twist count is an integer kept exactly by every move
     that does not cut a strand (Update 97), which is a finer, different invariant; if it is never changed, the
     move-complex does not contain the move that undoes two full twists, and the belt trick's Z₂ is not there.
   - **Emergent fermions as string ends** ([LW03], [LW06], abstracts only). Bosonic lattice models (spins or rotors
     on a cubic lattice) can have fermionic excitations at the ends of strings, with [LW06] reporting "massless Dirac
     fermions" alongside a photon. This is the nearest published route on a lattice; it works through the algebra of
     the string operators, not through a continuous loop in configuration space. Whether those fermions carry spin
     one half under the lattice's rotations is not stated in the abstracts (to verify by reading).
5. **Can the toy's twist labels ever meet the condition?** *Ours, unverified:* not as labels alone. Signed thirds and
   halves are integers on a finite set; four quarter turns return them; and the record's own reading (part 4) stands.
   They could enter a Finkelstein–Rubinstein construction only as the data of a tethered framed strand inside a
   move-complex built as above, with a rule for which move cycles are fillable and a chosen sign round the 2π one.
   That is a new ingredient under S1, and the sign would still be chosen, not derived: [Kru03] Eq. (7) and [KS06]
   both say "impose" and "choose".

## 5. Check (b): Landauer's bound and her entropy idea

**The record's statements** (handoff looks, part 6; brief item 7; O154 (5)): three twists collapsing three
placements into one gives up ln 3 of entropy; at temperature T at least kT ln 3 must be carried away, which one photon
can carry; the bound is a minimum, not a value; it cannot select one photon.

**Verdict: correct; the sources make the last point stronger.**

1. **The precise statement.** [Lan61] Sec. 4: entropy reduced by k ln 2 per bit, "0.6931 kT per restored bit to the
   surroundings", "a minimum heating effect", with no guarantee it is achievable. Generalised by its own example (p.
   266): the minimum is T times the drop in −k Σ p ln p. For three equally likely placements merged into one, k ln 3,
   so at least kT ln 3 ≈ 1.10 kT of heat. *Exact arithmetic.* If the three placements are not equally likely, the drop
   is smaller than k ln 3.
2. **Its conditions.** (i) The merging is logically irreversible (three inputs, one output); (ii) the inputs are not
   already known: [Lan61] p. 265, known inputs cost nothing, and [Ben03] p. 1, the cost on random data is a reversible
   transfer; (iii) the entropy has somewhere to go, and it becomes heat kT ln W only if the place is a heat bath at
   temperature T; (iv) [Lan61] sets aside states "with different entropy": the bound counts the information-bearing
   states only. *Ours:* in the toy each placement is itself many microscopic wirings and labellings, so the three
   placements and the one may carry different internal entropies, and the count of placements alone is not the whole
   entropy change; (v) the dynamics conserves fine-grained entropy, Hamiltonian or unitary ([Ben03] p. 1). The toy's
   Monte Carlo is not Hamiltonian; *ours:* its counterpart is the free energy F = E − g S at coupling g, by which the
   all-alike triple is disfavoured by g ln 3 unless its energy is lower by at least that. That is the same bound in
   the toy's language, and like the bound it says "at least", not "how much".
3. **Can it say anything about the number of photons?** **No.** [Lan61] speaks of a "heating effect" and nothing of
   its carrier. [Ben03] p. 1 goes further: the entropy "need not" leave as energy at all; it "can be exported in other
   ways, for example by randomizing configurational degrees of freedom in the environment". So the bound allows one
   photon of energy at least kT ln 3, several smaller ones, heat into the graph's own wiring, or (in principle) no
   energy at all if the entropy goes into the arrangement of something else. One photon is her idea, not a consequence
   of the bound (as O154 (5) already says). *Ours, unverified:* what could select one photon is a conservation rule or a
   coupling (for example, a rule that the merging move emits exactly one quantum of the `graphity.u1` field), which
   would be a new ingredient, not thermodynamics.
4. **A bath is needed for "kT".** *Ours:* the bound's temperature is the temperature of whatever receives the entropy.
   Where the merging is meant to happen (inside X, before the burp, which has "order but not time", Update 41) the
   record has not said what that receiver is or what its temperature would be. In the toy's sealed runs the
   temperature is read off the bath of stores (ASSUMPTIONS Q12), so a sealed run could say how much the bath warms
   when triples merge, which is the bound measured, not the number of photons.

## 6. What it supplies to her theory

Her rule (memory, "existing math is good news"): a published mathematics that covers her idea is the result wanted.

- **Spin from topology is published and is a mainstream route.** That a particle made of a bosonic field can be a
  spin-one-half fermion because of the shape of the space of arrangements, with no spinor put into the field, is
  [FR68]'s result, used for the Skyrme model's nucleons ([Kru03]) and for Hopf solitons ([KS06]). Her picture, a
  particle as a twisted strand or band with no spin put in, is of this kind, and the work it needs has a name.
- **Odd against even, for free.** [AKS06]: a composite of an odd number of basic objects is spinorial, an even number
  is not. *Ours, unverified:* if her thirds were the basic objects, a triple (her electron; three-quark baryons) would
  be a fermion and a pair (her pairs, Update 97; mesons) a boson, which is the observed pattern (general knowledge, to
  verify). The rule counts strands, not net twist, so her neutron (three strands, twists cancelling) would still spin,
  which matches her current answer that it spins with no twist (Update 101). This is the count, not a derivation: the
  thirds' being spinorial is still put in.
- **The belt trick connects to her "full twist".** *Ours, unverified:* in the belt trick a full turn of a tethered
  object is exactly one full twist of the band; her electron is three thirds closing into one full twist (Update 97).
  So her "whole number of twists" and the 2π rotation are the same object in the published picture, provided the band
  is tied to something.
- **Her entropy idea has an exact published floor.** Three placements to one costs at least kT ln 3 = 1.10 kT,
  [Lan61]'s own method. That is a usable number for any sealed toy run that merges triples.

## 7. Where it differs

- **The toy has no continuous configuration space and no tether.** [FR68] needs loops that cannot be shrunk; the toy's
  states are a finite set and its rotations jump (section 4, items 3 and 5). The route needs a new structure
  (a move-complex with declared 2-cells, a tethered framed strand), under S1, before it can be asked.
- **The sign is chosen in every source.** [Kru03] Eq. (7) and [KS06] Sec. 4 impose the odd sign because the even one
  gives only bosons. So even a configuration space with the right loop would explain why spin one half is *possible*,
  not why it is *chosen*. Her picture would face the same question.
- **Integer twist against twist mod 2.** The published Z₂ is twist parity; the toy keeps an integer (thirds, halves).
  These are different invariants; a theory using both would have to say how they relate.
- **Landauer fixes a floor, not a carrier or an amount.** "Three becoming one is one photon" is hers; the bound allows
  any carrier, including none that carries energy ([Ben03]), and only says "at least kT ln 3" when the receiver is a
  bath at T.
- **Her placements need named strands.** With interchangeable strands every set has one placement and the entropy
  change is zero (handoff looks, part 6); the idea needs ordered strands (the interchangeable-points rule), which the
  braid model also assumes ([BT05] Sec. II, cited in the record).

## 8. What this note does not do

It does not read [FR68] itself; it does not read [LW03] or [LW06] beyond their abstracts; it does not verify the belt
trick at a source; it changes no code, no record file and no bibliography entry. Anything in sections 4 to 7 marked
"ours" is unreviewed, and the group-theoretic and topological facts marked "general knowledge, to verify" were not
checked at a source in this session except where [Hat02] is cited.

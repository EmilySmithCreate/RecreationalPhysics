# Reading note: Levin and Wen, "Quantum ether" (2006), against the particle sector (2026-10-24)

**Why this was read.** The Codex audit of 24 October (ASSUMPTIONS O154; VISION Update 103) named this paper as a
missing published work: a model built only from variables on the links of a cubic lattice whose low-energy particles
behave like photons and like electrons. That is the aim of the owner's particle handoff
(`docs/geometric_particle_model_handoff_2026-10-24.md`, section 0), and it bears directly on the toy's obstruction
recorded in VISION Update 96: "Any state built on link labels comes back with sign +1 after a full turn, so spin one
half cannot come out of the toy as it stands".

## Bibliographic data

- **[LW06]** M. Levin and X.-G. Wen, "Quantum ether: Photons and electrons from a rotor model", *Physical Review B*
  **73**, 035122 (2006), doi:10.1103/PhysRevB.73.035122, arXiv:hep-th/0507118 (v2, 13 February 2007; the text is
  dated May 2005). 10 pages. Key `LW06` in `REFERENCES.bib`.
- **[LW05]** M. A. Levin and X.-G. Wen, "String-net condensation: A physical mechanism for topological phases",
  *Physical Review B* **71**, 045110 (2005), arXiv:cond-mat/0404617 (v2, 27 April 2004). 21 pages. This is the
  paper's reference [5], the general theory.

## Read status

- **[LW06]: read in full** on 2026-10-24 by an assistant agent, from the arXiv PDF (v2). The text was extracted
  with PyMuPDF and every section was read: abstract, I, II.A to II.E (Eqs. 1 to 5), III.A to III.E (Eqs. 6 to 12),
  IV.A to IV.D (Eqs. 13 to 26), V, and the reference list. The figures were read only through their captions, since
  the extraction keeps no images. The owner has not read the paper. No physicist has reviewed this note.
- **[LW05]: read in parts**: the abstract; Sec. III's closing paragraph; Sec. IV.B, the passage defining the twists
  θ_α and their link to spin (around Eq. 28); and Sec. V, on (3+1) dimensions (Figs. 10 and 11 by caption, and
  Eq. 33 with the paragraphs around it). The tensor-category machinery of Secs. IV.A and IV.B and the appendices was
  not read.
- The references that [LW06] relies on were **not read**: Wen's book (ref. [7]), Wen PRB 68, 115413 (2003)
  (ref. [8], the earlier rotor photon), Levin and Wen PRB 67, 245316 (2003) (ref. [11], the "statistical hopping
  algebra" behind every statistics claim below), Wen PRD 68, 065003 (2003) (ref. [13], massive electrons from
  non-Abelian models), and Motrunich and Senthil (ref. [15]). Anything said here about their content comes from how
  [LW06] cites them.
- **Earlier partial reading in this repository.** `docs/reading/notes/loop_exchange_rules_2026-09-25.md` (entry
  [LW05b]) read Secs. II.A to II.C and III.A to III.C on 25 September. That entry writes the fine-structure constant
  as "of order J/g". The paper says √(J/g) (Sec. II.C), so the entry needs correcting. The `REFERENCES.bib` note for
  `LW06` still says "Not read by us" and should become "read in full 2026-10-24 (assistant agent)". This note does
  not edit either file.

**Labels.** Text in quotation marks is verbatim from the named source, with its section or equation. Unmarked prose
under "What the paper does" paraphrases the source. *Ours, unverified* marks this note's own inferences, which are in
no source. *General knowledge, to verify* marks physics not read at source for this note.

## What the paper does, in plain English

### Terms

- **Rotor**: a quantum particle on a circle. It has an angle θ and an angular momentum L^z, and L^z comes only in
  whole numbers (…, −1, 0, 1, 2, …). L⁺ = e^{iθ} raises L^z by one; L⁻ lowers it by one. In this paper there is one
  rotor on every **link** (edge) of the cubic lattice. Nothing lives on the points.
- **Bosonic model**: every variable is an ordinary commuting quantity. No variable is put in with the minus sign that
  fermions carry when two of them are swapped.
- **Plaquette**: one square face of the cubic lattice, bounded by four links.
- **Gauss's law, charge**: the charge at a point is a signed sum of L^z over the six links meeting there. Where it is
  zero, every line of L^z that enters a point also leaves it.
- **Fermion**: a particle whose quantum state changes sign when two identical ones are swapped. The Pauli exclusion
  principle follows from that sign. In three dimensions, the spin-statistics connection ties the swap sign to the
  sign a single particle picks up under a full 360° turn, which is spin one half (general knowledge, to verify).
- **String-net**: a network of lines drawn on the links. In this model a "string" is a path along which L^z
  alternates +1, −1, +1, … ([LW06] Fig. 3). A closed string carries no charge. An open string has a charge at each
  end.

### The model and how photons appear (Sec. II)

The Hamiltonian has three terms (Eq. 1):

    H_rotor = V Σ_I Q_I² + J Σ_i (L^z_i)² − g Σ_p (B_p + h.c.),
    B_p = L⁺₁ L⁻₂ L⁺₃ L⁻₄,   Q_I = (−1)^I Σ_(legs of I) L^z_i,   (−1)^I = (−1)^(Ix+Iy+Iz).

- **V** charges a price for any nonzero charge, so at low energy every point is neutral.
- **J** charges a price for every unit of L^z, so long strings cost energy. This is a **string tension**.
- **g** rotates the four rotors around a square together. It creates a small closed string or moves an existing
  one: the strings' **kinetic energy**.

With V ≫ g ≫ J > 0 (Sec. II.B), the low-energy states are superpositions of many large closed strings, a
"string-net condensate". Its gentle collective motions are gapless waves, and the paper shows that they are photons.
The demonstration is an exact rewriting (Sec. II.C, Eqs. 2 to 4). Set e_IJ = (−1)^I L^z_i and n_I = Q_I. The rotor
model then *is* compact U(1) lattice gauge theory in its Hamiltonian form, with L^z as the integer electric field and
θ as the vector potential, coupled to a charge field. The charge field cannot move until a hopping term is added
(Sec. II.D: H_hop = −2t Σ_i cos θ_i). The ends of open strings are the charges. They are gapped, with energy of order
V. Computed with the "statistical hopping algebra" of ref. [11], they come out **bosons** (Sec. II.E, Eq. 5).

The scales: α ~ √(J/g) and c ~ √(gJ)·a (Sec. II.C; a is the lattice spacing). If J ≫ g, the strings are too costly
to fluctuate. That phase confines and has no photons. The change between the two phases "is the usual
confinement-deconfinement transition from gauge theory" (Sec. II.C).

### How fermions appear: the "twist" (Sec. III)

The one change is a sign attached to the plaquette term. A string operator W(C) = L⁺ L⁻ L⁺ … along a curve C (Eq. 6)
is replaced by a **twisted string operator** (Eq. 8):

    W̃(C) = (L⁺_i1 L⁻_i2 …) · (−1)^(Σ_(legs of C) n^c_i L^z_i),

where n^c_i counts how many times link i crosses a **framing** curve C′ drawn just beside C. The framing turns the
string into a thin ribbon, and the extra sign reads the parity of the L^z on the links the ribbon's edge crosses.
Defining "beside" requires choosing a projection of the 3D lattice onto a 2D plane (Fig. 4a). The twisted plaquette
term B̃_p = W̃(∂p) acts on the square's four rotors and on eight neighbouring "leg" rotors (Eq. 9, Fig. 5).

Two results follow.
1. **Without charge motion, nothing changes.** For t = 0 the twisted and untwisted models "are completely equivalent
   and can be mapped onto one another" (Sec. III.C): the same photons and the same static charges.
2. **With charge motion, the charges become fermions.** With a matching twisted hopping term (Eqs. 10, 11), the
   hopping algebra picks up a minus sign (Eq. 12):
   L̃⁺_i L̃⁻_j L̃⁺_k = (−1)·L̃⁺_k L̃⁻_j L̃⁺_i. "This sign makes all the difference" (Sec. III.E). The string ends are
   now fermions, and no mapping to an ordinary lattice gauge theory survives.

### Electrons proper: Dirac fermions (Sec. IV)

In Sec. III the fermions misbehave at lattice scale: any number of them can sit on one point, and they interact even
when J = 0. Sec. IV repairs this. Charges are allowed only at "eee" points (all three coordinates even), where they
are +1, and at "ooo" points (all odd), where they are −1. They hop by two steps along an axis (Eqs. 13, 14). The
low-energy theory is then exactly the standard tight-binding model of fermions in a dynamical compact U(1) field
(Eq. 22). Which particles appear is set by the chemical potential µ:
- µ < −6t: an insulator, with gapped fermions of charges ±1 and gap Δ = −6t − µ (Sec. IV.C).
- µ > −6t: two Fermi liquids (Sec. IV.C).
- µ = 0, with a pattern of hopping signs χ (Eqs. 24, 25) that puts a flux of π through each doubled 2 × 2 plaquette:
  nodal points with linear dispersion (Eq. 26). "Together, the two nodes give rise to one four-component Dirac
  fermion in the continuum limit". Counting the band degeneracy and the two sublattices gives "a total of 4 massless
  four component Dirac fermions" (Sec. IV.D), that is, QED with four species.

The paper also states its limits. The photon speed c ~ √(gJ)·a and the fermion speed c_e ~ t·a are different, so
Lorentz invariance holds only if t is tuned to make them equal. The electrons are massless. A naturally small mass
needs non-Abelian gauge fields (ref. [13]). Neutrinos and SU(2) bosons are out of reach because of "the famous
chiral-fermion problem" (Sec. V).

### What the string-net paper adds ([LW05], parts read)

- In (3+1) dimensions, string-net condensates correspond to "symmetric tensor categories", and their low-energy
  theories "are gauge theories coupled to bosonic or fermionic charges" (Sec. V).
- Fermions come from "twisting the usual gauge theory solution by ω̃ = ω·(−1)^(P(j)P(k))" (Eq. 33), where P assigns
  an even or odd parity to each string type. "In twisted gauge theories, all the quasiparticles corresponding to
  'odd' representations i are fermionic" (Sec. V).
- "Unlike in two dimensions, higher dimensional quasiparticles necessarily have trivial mutual statistics, and must
  be either bosonic or fermionic" (Sec. V).
- The twists θ_α are "statistical angles", and "by the spin-statistics theorem they are closely connected to the
  quasiparticle spins s_α: e^{iθ_α} = e^{2πi s_α}" (Sec. IV.B, before Eq. 24). So a twist of π is a spin of one half.
- A 3D lattice's plaquette boundaries "will always make both left and right turns" under any projection (Sec. V,
  Fig. 11). This is the reason the 3D construction needs the general twisted string operators, which is what [LW06]
  then uses.

## Key quotations

- Abstract ([LW06]): "We give an example of a purely bosonic model – a rotor model on the 3D cubic lattice – whose
  low energy excitations behave like massless U(1) gauge bosons and massless Dirac fermions."
- Sec. I: "The gauge bosons correspond to fluctuations in the strings - the collective motions of the strings that
  fill the space. ... The fermions correspond to endpoints of the strings - that is, defects in the string liquid
  where a string ends in empty space."
- Sec. I: "the mapping between the rotor model and QED is essentially exact, and does not require a large N limit or
  similar approximation."
- Sec. II.B (on Eq. 1): "the J-term penalizes strings for being long. It therefore corresponds to a string tension.
  ... Thus the g-term generates string 'hopping' or string fluctuations."
- Sec. II.B: "nonzero charge configurations are made up of open string-nets - with the charge located at the
  endpoints of the open strings."
- Sec. II.C: "the 'fine structure constant' α of the gauge theory is of order √(J/g). The 'speed of light' c is of
  order √(gJa²)".
- Sec. II.C: "The physics of the rotor model (1) is therefore completely equivalent to a U(1) gauge field coupled to
  bosonic charges."
- Sec. III.B: "The only difference is that here the amplitude for this process is not always 1. The amplitude is ±1,
  depending on the rotors on the legs of the plaquette boundary."
- Sec. III.C: "the twisted and untwisted rotor Hamiltonians (9), (1) are completely equivalent and can be mapped onto
  one another."
- Sec. III.D: "The two models are only equivalent in the special case where t = 0 and the charges have infinite
  mass. As soon as the charges can hop, the mapping between the two models breaks down".
- Sec. III.E (Eq. 12): "This sign makes all the difference. ... We conclude that in the twisted rotor model the
  charged particles are fermions."
- Sec. III.E: "the hopping term H_hop allows positive and negatively charged fermions to annihilate each other if
  they occupy neighboring sites."
- Sec. IV.D: "the low energy physics of the rotor model H_t.b with µ = 0, V → ∞, g ≫ J, t, and t given by the above
  formula, is equivalent to QED with four species of massless Dirac fermions."
- Sec. IV.D: "the speed of light c ∼ √(gJ) a and the speed of the massless Dirac fermion c_e ∼ ta are not the same in
  our rotor model. However, we can tune the value of t to make c = c_e."
- Sec. V: "Surprisingly, this 'twist' was enough to turn the Higgs boson into a fermion."
- Sec. V: "we can produce photons, gluons, leptons and quarks, but we do not know how to produce neutrinos or SU(2)
  gauge bosons."

Two details of the text are worth noting. Sec. IV.B says "U → ∞" where V → ∞ is meant. And at lattice scale the paper
calls its fermions "spinless" (Sec. III.E, contrasting with "a standard tight binding model of spinless fermions").
**The paper never discusses rotations or spin.** It derives exchange statistics, plus a four-component Dirac structure
in the continuum limit.

## What it supplies to her theory

The owner's rule: existing mathematics that covers one of her ideas is the result we want. Item by item, with the
handoff's numbering (section 1) and the VISION updates:

1. **Idea 1, "a flat path/link exists without a photon; a photon is an excitation traveling along a pre-existing
   path"**: covered exactly, and in a stronger form than `graphity.u1`. In [LW06] the links carry rotors whether or not
   any photon is present, and the photon is the collective motion of closed strings of L^z over them (Sec. II.B,
   II.C). The toy's u1 field is the same compact U(1) theory (Wilson's), written classically and in Euclidean form.
   [LW06] Eq. 2 is its Hamiltonian, quantum form. *Ours, unverified:* the toy orients each link from its kind-0 point
   to its kind-1 point, and that is the same bookkeeping as [LW06]'s alternating sign (−1)^I in Q_I and in
   e_IJ = (−1)^I L^z (Eq. 4). Both rest on the lattice being bipartite.
2. **Strands, open strands confined (VISION Update 97 (6): "a lone third is confined")**: the mechanism exists, as the
   string tension J. An open string costs J per unit length, and in the J ≫ g phase "there are no gauge bosons at low
   energies" and charges are confined (Sec. II.C). In the condensed phase the string's cost disappears into the
   condensate, and the ends become free particles. *Ours, unverified:* this is the published form of "strands with
   ends", but in [LW06] the strand is a line of electric flux and the particle sits at its end. In her picture the
   strand is the particle.
3. **Twisted strands, and the obstruction to spin one half (VISION Update 96)**: this is the main thing the paper
   supplies. The equation is Eq. 8 with Eq. 12. Putting a sign (−1)^(Σ n^c L^z) into the string and plaquette
   operators, a sign read from a framing ribbon beside the string, turns the string ends into fermions. No new
   variable is added. The Hilbert space is still integers on links.
   - *Ours, unverified.* This refines the obstruction rather than refuting it. A *closed* bosonic system as a whole
     still returns to itself under a full turn. Charges are created in ± pairs (Sec. III.E: the hopping term "either
     creates two charges at neighboring sites, or ... makes a charge hop"), and on a closed lattice they add to zero.
     What becomes possible is a **single string end** behaving as a fermion: a sign appears when two ends are swapped
     (Eq. 12), and by [LW05]'s e^{iθ} = e^{2πis}, a sign when one end is turned through 360° relative to its ribbon.
     The −1 lives in the dynamics (the plaquette term's sign) and in loops through configuration space, not in any
     single configuration. That is the route Update 96 named ("come from a loop in the space of configurations";
     Finkelstein and Rubinstein, general knowledge, to verify). [LW06] is a working lattice example of it. It is not a
     reading that "spin one half is in the link labels".
   - *Ours, unverified.* The twist that does this is a **sign**, a half turn (θ = π). In 3D no other choice exists:
     "higher dimensional quasiparticles ... must be either bosonic or fermionic" ([LW05] Sec. V). Her ribbon picture
     (a strand as a band; one-sided after an odd number of half turns, VISION Update 101 (2)) has a published
     relative here. A framed string is a ribbon, and the fermionic one carries the π sign. But in her assignment
     **halves belong to dark strands and thirds to matter strands**. If the published mechanism applies, the half twist
     is what makes a strand's end a fermion, and a third of a turn cannot be an exchange phase of a point particle in
     3D at all. A third could be a charge (a label mod 3, like quark triality) but not a statistics. This is a real
     tension for her to see. It does not settle her rule.
4. **Charge, how it is defined and conserved (VISION Update 101: charge = −(net signed thirds)/3)**: in [LW06],
   charge is the Gauss-law operator Q_I = (−1)^I Σ_legs L^z (Eq. 1). It commutes with every term of the Hamiltonian,
   including the hopping terms, which only move charges or create them in ± pairs. Total charge on a closed lattice is
   zero, as `graphity.u1` already tests. **Charges are whole numbers**, and in Sec. IV only ±1. Nothing like thirds
   appears. *Ours, unverified:* conservation here is exact because charge is the end of a flux line and flux lines
   cannot stop. Her thirds would need a different conserved count, a Z₃ or SU(3) string-net, which the general
   construction allows (Sec. V: "one should be able to construct a model that gives rise to SU(3) gauge bosons and
   massless Dirac fermions - that is, QCD") but which this paper does not build.
5. **Idea 5, opposite twists combine and cancel, and annihilation releases waves**: present in kind. Positive and
   negative fermions "annihilate each other if they occupy neighboring sites" (Sec. III.E). *Ours, unverified:* in the
   gauge theory the energy released goes into the field, which is photons. The paper does not compute this.
6. **Antiparticles (VISION Update 100: the mirror image of its strand)**: in [LW06] Sec. IV the antiparticle is the
   opposite charge, kept on the other sublattice (+1 on eee points, −1 on ooo points). That echoes her 24 October
   answer that "the kinds separate regular and anti" (Update 97). But in [LW06] the separation is imposed by the
   V-term of Eq. 14. It is not a mirror image, and it is not a consequence of the lattice.
7. **Idea 7, gluons**: only at the level of a claim. "We can produce photons, gluons, leptons and quarks" (Sec. V),
   through the general construction of [LW05]. Not built here.
8. **Idea 9, mass as stored curl**: not supported here. The fermion gap is Δ = −6t − µ, set by the hopping and the
   chemical potential (Sec. IV.C), and the Dirac fermions are massless. A naturally small mass needs non-Abelian
   fields (ref. [13], not read). Nothing in [LW06] ties mass to curl or to the field's energy.

**What it predicts, the constants it exposes, and the test it names.**
- The constants are V (the charge gap), J (string tension), g (string hopping), t (charge hopping) and µ. Physical
  quantities follow from them: α ~ √(J/g), c ~ √(gJ)a, c_e ~ ta, and Δ = −6t − µ. *Ours, unverified, order of
  magnitude only:* α ≈ 1/137 would need J/g of about 5 × 10⁻⁵, so g ≫ J by a wide margin, which is the condensed
  regime the paper assumes.
- Its predictions are structural: photons appear only in the condensed phase g ≫ J; the string ends are bosons
  without the twist and fermions with it; four species of Dirac fermion appear at µ = 0 with π flux (fermion
  doubling); and Lorentz invariance does not come for free.
- The test it names is algebraic and exact. Compute the hopping operators' exchange relation, Eq. 5 against Eq. 12,
  on the lattice. A + sign means bosons and a − sign means fermions. The same test is how the toy would check any
  claim that a strand's end is a fermion.

## Where it differs from her theory and from the toy

- **Quantum against classical.** [LW06] is a quantum Hamiltonian model, and its fermions are a statement about
  operator algebra. The toy samples a classical Euclidean weight (`graphity.u1`: Metropolis on exp(β Σ cos φ)).
  Exchange signs have no meaning in a classical sample. *Ours, unverified:* the twisted plaquette term has amplitudes
  ±1 that depend on the state, so a path-integral Monte Carlo of the twisted model is expected to suffer a sign
  problem (general knowledge, to verify).
- **A fixed, embedded cubic lattice.** The framing needs a projection of the 3D lattice onto a 2D plane (Sec. III.A,
  Fig. 4a), and the legs of B̃_p are specific neighbouring links (Fig. 5). The toy's flat six-link torus is a cubic
  lattice, so the construction transfers there. The toy's other graphs do not supply this: the curled tori, where the
  ring round a side of 4 also counts as a square and has no framing convention, and above all the rewiring graph,
  which has no embedding at all.
- **Three dimensions only.** The four-link (2D) toy is a different case. In two dimensions exchange phases need not
  be ±1 (anyons; [LW05] Sec. V), so neither the argument nor the restriction carries over.
- **Charges are whole numbers at string ends. Her matter is signed thirds on strands.** Body diagonals and face
  diagonals play no role in [LW06]. The fermions hop two steps along axes (Eq. 13), and the only special point classes
  are eee, ooo and mixed.
- **Fermions are spinless at lattice scale.** The four-component Dirac structure appears only in the continuum limit,
  from the band structure of π flux, and with fermion doubling. Spin one half under the lattice's own rotations is
  not shown in the paper.
- **No mass mechanism, no chirality, no neutrinos** (Sec. IV.D, V).
- **Nothing curls.** The lattice is fixed. The paper has no counterpart of the toy's curling cost, its λ, or its
  rewiring moves.

## What it would take to apply it to the toy

*All ours, unverified; each is a proposal, not a decision. A new ingredient needs her dated decision under S1.*

1. **The cheapest exact look (no decision needed; a sandbox look).** On the toy's own six-link flat torus
   (`graphity.cqg_d.torus`, every side at least 6), build L^±, L^z and (−1)^(L^z) as operators on rotors truncated to
   L^z ∈ {−1, 0, 1} on a handful of links. Then check Eq. 5 for the untwisted hopping operators and Eq. 12 for the
   twisted ones of Eq. 11. This reproduces the paper's central algebra on the toy's lattice and is the gate any further
   use would need (rule 2, reproduce before extending).
2. **Quantum time evolution**, at least for small systems by exact diagonalization, since the fermionic sign is a
   quantum statement. The classical sampler in `graphity.u1` cannot see it.
3. **A framing rule on the toy's graphs.** For the curled tori, a convention for the ring round the curl. For the
   rewiring graph, a framing defined from the wiring alone, with no embedding. That is open research. *Ours,
   unverified:* [LW05] Sec. V's remark that 3D plaquette boundaries make both left and right turns under any
   projection suggests the convention is not free.
4. **Her thirds** would need a Z₃ or SU(3) string-net, from the general construction of [LW05] (not read in those
   parts). That construction gives charges mod 3 or color. In 3D it still gives exchange statistics of ±1 only.
5. **Gate questions for her** before anything is built: whether matter's fermion sign may come from a half twist
   when she has assigned halves to dark strands; and whether "strand" means the flux line (as in [LW06]) or the
   particle itself.

## Summary of the bearing

The paper is the nearest published model to the particle handoff's aim, and it is exact rather than approximate.
Photons come from closed strings of whole-number flux on the links of a cubic lattice. Fermions come from the ends of
open strings once a ribbon sign, the "twist", is put into the plaquette and hopping terms. Charge is the Gauss-law
count at string ends, whole numbers, conserved exactly. For the toy it changes the obstruction of Update 96 from "spin
one half must be put in" to "the fermion sign can be put into the dynamics, as a ribbon sign on string operators, with
no new variables". The price is a quantum treatment and a framing that needs an embedded 3D lattice. And in 3D the
only twist that does this is a half turn, never a third.

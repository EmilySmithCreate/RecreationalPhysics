# Reading note: how others make sense of "everything fits in two dimensions" (2026-10-24)

**The owner's question.** "How else do people make sense of this stuff, knowing it has to all simplify to information
that can be held in 2 degrees of freedom?" The assistant first answered from memory, naming holography and the area law
('t Hooft; Susskind; Maldacena; Bekenstein and Hawking), dimensional reduction to two at short distances ([Carlip17]),
string worldsheets, and tensor networks (Swingle). This note checks that answer against the primary sources.

**What was read, and how.** Read on 2026-10-24 by an assistant agent. Abstracts were taken word for word from the arXiv
export interface (`export.arxiv.org/api/query`), which also gave the journal references and DOIs listed below. Three
papers were downloaded from arXiv and their text extracted with PyMuPDF: 't Hooft (gr-qc/9310026v2, 13 pages, read in
full), Susskind (hep-th/9409089v2, 34 pages, introduction read and the rest searched), and Swingle (0905.1317v1, 15
pages, searched for its main passages). Bekenstein (1973), Hawking (1975) and Polyakov (1981) are not on arXiv. Their
bibliographic data were checked against the Crossref catalogue, but the papers themselves were not reachable: the APS
page returned 403 and Springer asked for a login. **They are not read.** What this note says about them comes from the
read papers that cite them, or is marked "general knowledge, to verify". The owner has not read any of these sources,
and no physicist has reviewed this note.

**Labels.** Text in quotation marks is verbatim from the named source. Unmarked prose under a source is a paraphrase of
that source. *Ours, unverified* marks this note's own readings, which are not in any source.

## First, a correction to the question's wording

*Ours, unverified, but checked against the sources below.* None of these sources says that everything fits in **two
degrees of freedom**. What they say is that it fits in **a two-dimensional surface's worth** of degrees of freedom:
about one bit for each Planck-sized patch of a surface ('t Hooft's Eq. (3): n = A / (4 ln 2) Boolean variables for a
horizon of area A in Planck units; Susskind: "one discrete degree of freedom per Planck area"; Bousso: "10^(69) bits per
square meter"). A surface the size of a room holds about 10^70 of them. So the count is enormous. What is limited is how
the count grows. It grows with the **area** of the boundary and not with the **volume** inside, as if the world were a
two-dimensional sheet of bits. The rest of this note reads "two" as "two-dimensional" in that sense.

[Carlip17] uses "two" in a third sense: the **effective dimension** that some measurements of spacetime give at very
short distances. That is neither a count of degrees of freedom nor a statement about boundaries (see the
[Carlip17] note).

## Terms, defined once

- **Planck length**: the length, about 1.6 × 10⁻³⁵ m, built from the gravitational constant, the speed of light and
  Planck's constant. A **Planck area** is its square. (General knowledge, to verify.)
- **Entropy** (here): the logarithm of the number of distinct states a system can be in. 't Hooft's Eq. (2) puts it as
  "e^S = N = 2^n" for n two-valued variables, "Hence the entropy directly counts the number of Boolean degrees of
  freedom."
- **Area law**: a black hole's entropy is proportional to the area of its horizon and not to its volume.
- **Holography / holographic principle**: everything that happens inside a region can be described by degrees of
  freedom on its boundary, at no more than about one bit per Planck area.
- **Bulk and boundary**: in the dualities below, the "bulk" is the higher-dimensional space with gravity and the
  "boundary" is the lower-dimensional theory without gravity that describes it completely.
- **Anti-de Sitter space (AdS)**: a spacetime with constant negative curvature. It has a boundary at infinity on which
  the dual theory lives. Our universe, with its accelerating expansion, is closer to de Sitter space, which has positive
  curvature. (General knowledge, to verify.)
- **Tensor network**: a way of writing a quantum state of many parts as a network of small linked pieces. Its wiring
  records which parts are entangled with which.

## The sources

### 1. 't Hooft, "Dimensional Reduction in Quantum Gravity" (1993)

**Data.** G. 't Hooft, arXiv:gr-qc/9310026 (v1 19 October 1993; v2 20 March 2009, read), Utrecht preprint THU-93/26,
essay dedicated to Abdus Salam. The arXiv record lists no journal reference. **Read in full.**

**What it says.** The abstract: reconciling gravitational collapse with quantum mechanics "implies that at a Planckian
scale our world is not 3+1 dimensional. Rather, the observable degrees of freedom can best be described as if they were
Boolean variables defined on a two-dimensional lattice, evolving with time." The argument is a count. Fill a closed
surface of area A with as much as it can hold. A hot gas gives entropy that grows only as A^(3/4) (Eq. (8)). The most
you can put inside is a single black hole that just fits, with entropy "S_max = 1/4 A" (Eq. (11)). So the number of
possible states grows with the area and not with the volume: "given any closed surface, we can represent all that
happens inside it by degrees of freedom on this surface itself ... One Boolean variable per Planckian surface element
should suffice." He calls this "a somewhat extreme point of view" and compares it to a hologram, which stores a
three-dimensional image on a two-dimensional film. He concludes that the degrees of freedom of three-dimensional space
"are not independent but, if considered at Planckian scale, they must be infinitely correlated."

The second half of the essay tries to build such a world, and it is closer to this project's toy than anything else
read here. He takes a cubic lattice of discrete variables and imposes "on every plaquette of the lattice a relation
among the data", meaning on every square face of each unit cube (Eqs. (12a) to (12f)), so that the data on a line fix
the data everywhere. The six face relations of a cube must agree on its last corner (Eq. (16)). The only solutions his
computer search found were linear ones, which he calls "too trivial to be of much physical interest" because they
describe only "non-interacting" particles. To get from three dimensions down to the problem he can study, he writes:
"By choosing the initial data to be periodic in that one extra dimension the problem reduces to the three dimensional
one." His closing summary: "The picture we sketched of the 2+1 (or perhaps it is better to say 2+2) dimensional nature
of our micro-universe seems to follow from quite general arguments," while "it is extremely difficult to reproduce
anything resembling Lorentz invariance" with discrete degrees of freedom.

**How it bears on her picture.** *Ours, unverified.* 't Hooft's two-dimensional description is a **bound on how much
information there is**. It is not a phase in which the third direction is closed: in his picture the three-dimensional
world is fully present, and the surface is a second, equivalent way to write it down. Her picture is a phase whose
third dimension opens and closes over a cycle, so it would need more than his bound. It would need the bound to be
reached physically in some state. His essay does point at one such state: the bound is saturated by "one black hole
[that] has the largest possible size that still fits", and that agrees with her reading of black holes as places where
space re-curls. Two details are close to the toy, and they are noted here as resemblances, not results. His building
block is a constraint on each square face of a cube, as the toy's energy counts squares. And he cuts one dimension away
by making the data periodic in it, which is what a curled direction is. He also names the obstacle every discrete model
faces, Lorentz invariance, which is on this project's "out of reach" list (VISION, "The target").

### 2. Susskind, "The World as a Hologram" (1995)

**Data.** L. Susskind, arXiv:hep-th/9409089 (v2 28 September 1994), J. Math. Phys. 36 (1995) 6377 to 6396,
DOI 10.1063/1.531249. **Abstract read. Introduction (Sec. 1) read; the rest searched.**

**What it says.** The abstract: "According to 't Hooft the combination of quantum mechanics and gravity requires the
three dimensional world to be an image of data that can be stored on a two dimensional projection much like a
holographic image. The two dimensional description only requires one discrete degree of freedom per Planck area and yet
it is rich enough to describe all three dimensional phenomena." In Sec. 1 he pictures the boundary as a distant
"screen" made of "pixels", where "A pixel can only store one bit of information and is therefore either lit or dark."
He reaches the same conclusion from string theory: "string theory in the light front gauge has the form of a two plus
one dimensional theory with no explicit mention of a longitudinal direction." He states the principle like this: "the
theory can be formulated with no direct reference to the longitudinal direction x− and the transverse space may be
taken to be a discrete lattice ... the net result should be one bit per Planck cell." He then asks "how we code the
longitudinal location of a parton" (a parton is a point-like constituent), and his answer leads to a prediction:
"particles must grow in size as their momenta are increased far above the Planck scale." The match between string
theory and this picture "requires unproven but plausible assumptions about the nonperturbative behavior of string
theory."

**How it bears on her picture.** *Ours, unverified.* This is the first worked attempt to say how the missing third
direction is stored in the two. It is stored in how the bits on the screen are arranged, and it shows up as particles
that spread out at high momentum. If her two-degree-of-freedom phase is a real phase, she will face the same question
he asks: where is the third direction kept while it is closed? Two answers are already on the table. In Susskind's,
the information about the hidden direction is spread over the bits of the screen. In the toy, a curled direction
survives as a short loop (length 4), so the closed direction is still present as wiring. The two answers do not have
to agree.

### 3. Maldacena (1997); Gubser, Klebanov and Polyakov (1998); Witten (1998): the AdS/CFT correspondence

**Data.**
- J. M. Maldacena, "The Large N Limit of Superconformal Field Theories and Supergravity", arXiv:hep-th/9711200 (v3 22
  January 1998), Adv. Theor. Math. Phys. 2 (1998) 231 to 252, DOI 10.1023/A:1026654312961. **Abstract only.**
- S. S. Gubser, I. R. Klebanov, A. M. Polyakov, "Gauge Theory Correlators from Non-Critical String Theory",
  arXiv:hep-th/9802109, Phys. Lett. B 428 (1998) 105 to 114, DOI 10.1016/S0370-2693(98)00377-3. **Abstract only.**
- E. Witten, "Anti De Sitter Space And Holography", arXiv:hep-th/9802150, Adv. Theor. Math. Phys. 2 (1998) 253 to 291
  (the arXiv record gives no DOI). **Abstract only.**
- O. Aharony, S. S. Gubser, J. Maldacena, H. Ooguri, Y. Oz, "Large N Field Theories, String Theory and Gravity",
  arXiv:hep-th/9905111, Phys. Rept. 323 (2000) 183 to 386, DOI 10.1016/S0370-1573(99)00083-6 (the standard review).
  **Abstract only.**

**What they say.** Maldacena: "the large N limit of certain conformal field theories in various dimensions include in
their Hilbert space a sector describing supergravity on the product of Anti-deSitter spacetimes, spheres and other
compact manifolds", and "We conjecture that compactifications of M/string theory on various Anti-deSitter spacetimes are
dual to various conformal field theories." In plain words, a theory without gravity in d dimensions is claimed to be
exactly the same as a theory with gravity in d + 1 dimensions. Witten gives the dictionary: "correlation functions in
conformal field theory are given by the dependence of the supergravity action on the asymptotic behavior at infinity",
and "dimensions of operators in conformal field theory are given by masses of particles in supergravity." He also notes
that the boundary theory "has a large N phase transition related to the thermodynamics of AdS black holes." Gubser,
Klebanov and Polyakov place a boundary of AdS "analogous to a cut-off on the Liouville coordinate of the
two-dimensional string theory". So the extra direction of the bulk is tied to the extra field that a two-dimensional
string surface carries (see source 7).

**How it bears on her picture.** *Ours, unverified.* This is the most precise "fewer dimensions describe more"
statement in physics, and it is still a conjecture, not a theorem (general knowledge, to verify; the word "conjecture"
is Maldacena's own). Three limits matter for her picture. (a) It is a **duality**: the two descriptions hold at the same
time, so it gives no phase in which the extra direction is absent. (b) It holds in anti-de Sitter space, and our
universe is not anti-de Sitter (general knowledge, to verify). Trugenberger's programme, as recorded in VISION, uses a
negatively curved two-dimensional surface as a holographic screen ([T23], [T24]), which is the same ingredient. (c) The
nearest thing in it to her opening and closing is Witten's phase transition tied to AdS black holes. In that transition
the bulk changes from a geometry with no black hole to one with a black hole as the temperature changes (general
knowledge for the description, to verify). It is a change of geometry with a sharp step, which is the kind of thing
claim 4 is about. It has not been read past the abstract.

### 4. Bekenstein (1973) and Hawking (1975): the area law

**Data.** J. D. Bekenstein, "Black Holes and Entropy", Phys. Rev. D 7 (1973) 2333 to 2346, DOI
10.1103/PhysRevD.7.2333. S. W. Hawking, "Particle creation by black holes", Commun. Math. Phys. 43 (1975) 199 to 220,
DOI 10.1007/BF02345020 (with an erratum, Commun. Math. Phys. 46 (1976) 206, DOI 10.1007/BF01608497). Data checked in
Crossref. **Neither read**: both publisher pages refused access.

**What they say, from sources that cite them.** Susskind (Sec. 1, read) gives Bekenstein's argument that the maximum
entropy of a region is set by its boundary area, because otherwise collapsing it into a black hole would lower the
entropy and "the second law would be violated." 't Hooft (read) uses the result as S = 4πM² + C (his Eq. (1), natural
units), which equals one quarter of the horizon area (his Eq. (3)). Bousso's review (abstract read) calls the area bound
"a universal relation between geometry and information ... It has yet to be explained." From general knowledge, to
verify: Hawking showed that a black hole radiates at a temperature inversely proportional to its mass, which fixed the
constant in Bekenstein's proportionality at one quarter of the area in Planck units.

**How it bears on her picture.** *Ours, unverified.* This is the observational anchor for every "two-dimensional"
claim above, as far as anything about quantum gravity is anchored. It is a calculation that combines established
theories; no black hole's entropy has been measured. It supports her picture only indirectly: it is the reason anyone
thinks gravity's degrees of freedom live on surfaces. If her black holes are places where macro space re-curls, the
area law is a number her picture would have to reproduce: a re-curled region's count of states should grow with its
boundary area. That could be checked in the toy as a count, in the same way the hidden count of O87 was taken. It is
not designed.

### 5. Bousso, "The holographic principle" (2002), the review

**Data.** R. Bousso, arXiv:hep-th/0203101 (v2 29 June 2002), Rev. Mod. Phys. 74 (2002) 825 to 874, DOI
10.1103/RevModPhys.74.825. **Abstract only.**

**What it says.** "There is strong evidence that the area of any surface limits the information content of adjacent
spacetime regions, at 10^(69) bits per square meter." The review explains which region belongs to which surface (the
"light-sheets") and tests the bound "in a wide range of examples." It says the holographic principle "asserts that its
origin must lie in the number of fundamental degrees of freedom involved in a unified description of spacetime and
matter. It must be manifest in an underlying quantum theory of gravity."

**How it bears on her picture.** It is the place to start for "what does the area law actually claim, and where does it
fail." Its last sentence is a bar her picture would face. An underlying theory, the toy included, should show the bound
in its own counting and not have it added by hand.

### 6. Ryu and Takayanagi (2006); Van Raamsdonk (2010): entanglement builds space

**Data.** S. Ryu, T. Takayanagi, "Holographic Derivation of Entanglement Entropy from AdS/CFT", arXiv:hep-th/0603001,
Phys. Rev. Lett. 96 (2006) 181602, DOI 10.1103/PhysRevLett.96.181602. **Abstract only.** M. Van Raamsdonk, "Building
up spacetime with quantum entanglement", arXiv:1005.3035, Gen. Rel. Grav. 42 (2010) 2323 to 2329 and Int. J. Mod. Phys.
D 19 (2010) 2429 to 2435, DOI 10.1007/s10714-010-1034-0. **Abstract only.**

**What they say.** Ryu and Takayanagi: the entanglement entropy of a region of the boundary theory "can be obtained
from the area of d dimensional minimal surfaces in AdS_{d+2}, analogous to the Bekenstein-Hawking formula for black hole
entropy." In words: how entangled a patch of the boundary is equals the area of the smallest surface in the bulk that
hangs down from it. Van Raamsdonk: "the emergence of classically connected spacetimes is intimately related to the
quantum entanglement of degrees of freedom," and "Disentangling the degrees of freedom associated with two regions of
spacetime results in these regions pulling apart and pinching off from each other."

**How it bears on her picture.** *Ours, unverified.* This is the strand closest to the project's starting point: space
is a pattern of relations, and connectedness follows the relations. Van Raamsdonk's "pinching off" is a published way
for a region of space to separate, and VISION already cites a bud pinching off ([BGG87]). The difference is that his
relations are quantum entanglement, while the toy's relations are links. The toy has no entanglement, since its
simulations are classical (VISION, "The target").

### 7. String worldsheets: Polyakov (1981)

**Data.** A. M. Polyakov, "Quantum geometry of bosonic strings", Phys. Lett. B 103 (1981) 207 to 210, DOI
10.1016/0370-2693(81)90743-7. Data checked in Crossref. **Not read.**

**What it says, from sources that cite it.** [Carlip17] Sec. 6 (read) says the "dream" of a fundamentally
two-dimensional theory "is oddly reminiscent of the Polyakov approach to string theory [210]." Gubser, Klebanov and
Polyakov (abstract read, source 3) speak of "the Liouville coordinate of the two-dimensional string theory" and tie it
to the extra direction of anti-de Sitter space. From general knowledge, to verify: in string theory the fundamental
object sweeps out a two-dimensional surface, its worldsheet. The theory is written on that surface, and the directions
of spacetime appear as fields living on it. In Polyakov's treatment an extra field on the worldsheet, the Liouville
mode, can act as one more spacetime direction.

**How it bears on her picture.** *Ours, unverified.* This is a third and different sense of "two": the theory is
two-dimensional, and spacetime's directions, including ones that are curled or emerge, are things the two-dimensional
theory produces. It is the closest of the sources to "a two-dimensional substrate whose output includes a third
direction." The papers that would show how a direction appears from the Liouville field have not been read.

### 8. Tensor networks: Vidal (2007); Swingle (2009, 2012); Pastawski, Yoshida, Harlow and Preskill (2015)

**Data.**
- G. Vidal, "Entanglement renormalization", arXiv:cond-mat/0512165, Phys. Rev. Lett. 99 (2007) 220405, DOI
  10.1103/PhysRevLett.99.220405. **Abstract only.**
- B. Swingle, "Entanglement Renormalization and Holography", arXiv:0905.1317 (v1 8 May 2009), Phys. Rev. D 86 (2012)
  065007, DOI 10.1103/PhysRevD.86.065007. **Abstract read; text searched and its main passages read.**
- B. Swingle, "Constructing holographic spacetimes using entanglement renormalization", arXiv:1209.3304 (2012; the
  arXiv record gives no journal reference). **Abstract only.**
- F. Pastawski, B. Yoshida, D. Harlow, J. Preskill, "Holographic quantum error-correcting codes: Toy models for the
  bulk/boundary correspondence", arXiv:1503.06237, JHEP 06 (2015) 149, DOI 10.1007/JHEP06(2015)149. **Abstract only.**

**What they say.** Vidal builds a network for the ground state of a chain of quantum spins, layer by layer, each layer
coarser than the last, and finds that "ground state entanglement in extended quantum systems is organized in layers
corresponding to different length scales." Swingle reads that stack of layers as geometry. In his abstract the network
organizes "information in a quantum state in terms of scale and defin[es] a higher dimensional geometry from this
structure. While states with a finite correlation length typically give simple geometries, the state at a quantum
critical point gives a discrete version of anti de Sitter space. Some finite temperature quantum states include black
hole-like objects." In the text, the state "is effectively extended into an emergent dimension representing scale," and
the cells of the network are "units filling out a higher dimensional 'bulk'." The depth of that new dimension depends on
the state. A state with only short-range entanglement runs out of entanglement after a few layers, at what he calls the
"factorization" scale. A critical state does not run out, and gives the full anti-de Sitter geometry. Pastawski and
coauthors build exactly solvable networks in which "the Ryu-Takayanagi formula and the negativity of tripartite
information are obeyed exactly in many cases."

**How it bears on her picture.** *Ours, unverified.* Of everything read, this is the closest to "a lower-dimensional
system whose extra dimension opens and closes." In Swingle's picture the extra direction is not fixed. It is deep when
the state is critical, shallow when the state has a finite correlation length, and it can contain black-hole-like
objects when the state is warm. A change of state lengthens or shortens a direction. Three cautions. His base system is
one-dimensional and the emergent bulk is two-dimensional, so the counting would have to be redone for her two-to-three.
The emergent direction is **scale** (how coarse the view is), not a direction that matter can move along in the
ordinary sense; whether it acts like one is the question his 2012 paper takes up and this note has not read. And the
toy is classical while tensor networks describe quantum states. Still, it offers her picture a concrete published
pattern: the extent of a direction is set by how far correlations reach in the lower-dimensional state.

### 9. Dimensional reduction at short distances: [Carlip17], and the fundamental-2D proposal it cites

**Data.** [Carlip17], S. Carlip, "Dimension and dimensional reduction in quantum gravity", arXiv:1705.05417, DOI
10.1088/1361-6382/aa8535. **Read in full, 2026-10-23**: `docs/reading/notes/2026-10-23_carlip_dimensional_reduction.md`.
G. Amelino-Camelia, M. Arzano, G. Gubitosi, J. Magueijo, "Gravity as the breakdown of conformal invariance",
arXiv:1505.04649, DOI 10.1142/S0218271815430026 (Carlip's [155]). **Abstract only.**

**What they say.** Carlip reviews many approaches to quantum gravity in which some measure of dimension falls to about 2
at very short distances. He says the measures "need not always agree", that "none of these hints is terribly convincing"
alone, and that the pattern is "much less firmly established" than black hole thermodynamics. **His review contains no
holographic argument**; the earlier note checked that "holography", "area law" and "Bekenstein" do not appear in it.
The only proposal it mentions in which the fundamental theory is two-dimensional is [155], and he calls it "so far only
a dream". The abstract of [155] proposes that "at the beginning of the universe gravity existed in a limbo," that the
proposal "finds support in recent results in quantum gravity suggesting that spacetime becomes two-dimensional at
super-Planckian energies," and that "gravity and the Big Bang Universe are relics from the mechanism responsible for
breaking the fundamental conformal invariance." The proposal predicts "departures from scale-invariance in the
primordial power spectrum and the level of gravity waves generated."

**How it bears on her picture.** *Ours, unverified.* [155] is the published idea nearest to her birth story: a
two-dimensional early phase, with gravity and the expanding universe as what is left after a symmetry breaks. It also
names what would test it, the primordial spectrum and gravitational waves. Carlip's own short-distance "2" is a
different claim. It is a measured effective dimension, and in at least one of his two explanations the spacetime stays
four-dimensional throughout (the earlier note, part (3)).

### 10. Also relevant, found while searching: Jacobson (1995)

**Data.** T. Jacobson, "Thermodynamics of Spacetime: The Einstein Equation of State", arXiv:gr-qc/9504004, Phys. Rev.
Lett. 75 (1995) 1260 to 1263, DOI 10.1103/PhysRevLett.75.1260. **Abstract only.**

**What it says.** "The Einstein equation is derived from the proportionality of entropy and horizon area together with
the fundamental relation δQ = TdS connecting heat, entropy, and temperature." He concludes: "Viewed in this way, the
Einstein equation is an equation of state."

**How it bears on her picture.** *Ours, unverified.* If the area law is assumed, gravity itself follows as
thermodynamics. That is the published root of the entropic route to gravity that the project already tests (Update 40,
O87), and it links source 4's area law to her "curve-first" gravity. The project's existing gravity notes
(`gravity_mechanisms_2026-09-25.md`, `2026-10-05_dark_energy_and_entropic_gravity.md`) are where it belongs. It is
recorded here only because it is the step from "information lives on surfaces" to "gravity".

## What this adds up to, for her question

*Ours, unverified.* People make sense of "it all fits in two dimensions" in four distinct ways, and the sources keep
them apart:

1. **A bound on information** ('t Hooft, Susskind, Bekenstein, Hawking, Bousso). A region holds at most about one bit
   per Planck area of its boundary. The three-dimensional world is still there, but it carries no more information
   than a sheet does. This is the strongest-supported of the four. It is a theoretical result, not a measured one.
2. **An exact equivalence** (Maldacena, Witten; Ryu and Takayanagi). A theory in one fewer dimension describes the bulk
   exactly. It is a conjecture, it holds in anti-de Sitter space, and the two descriptions hold at once, so neither is
   a phase.
3. **A built extra dimension** (Swingle; Pastawski and coauthors; Van Raamsdonk). The extra direction is made from how
   the lower-dimensional system is entangled, and its extent depends on the state. This is the nearest of the four to a
   direction that opens and closes.
4. **A measured short-distance dimension** (Carlip; [155] as the speculative fundamental version). Some measures of
   dimension fall to 2 at tiny scales. This is separate from holography, and Carlip keeps it separate.

Her picture, a phase with two dimensions' worth of degrees of freedom whose third dimension opens and closes over a
cycle, is not the same as any of these. Its closest relatives are (3), where a direction's depth follows the state, and
[155], where a two-dimensional early phase breaks into gravity and an expanding universe. Each of the others gives a
target, in the sense of rule 13 (something her picture would have to reproduce, not evidence for it). The area law (1)
is a count a re-curled region would have to match. Witten's black-hole phase transition (2) is a published sharp change
of geometry. [155]'s predicted departures from scale invariance are something it would have to match or explain.

## Read status, at a glance

| Source | Identifier seen | Status |
|---|---|---|
| 't Hooft 1993 | arXiv:gr-qc/9310026v2 | read in full |
| Susskind 1995 | arXiv:hep-th/9409089v2; DOI 10.1063/1.531249 | abstract; Sec. 1 read; rest searched |
| Maldacena 1998 | arXiv:hep-th/9711200; DOI 10.1023/A:1026654312961 | abstract only |
| Gubser, Klebanov, Polyakov 1998 | arXiv:hep-th/9802109; DOI 10.1016/S0370-2693(98)00377-3 | abstract only |
| Witten 1998 | arXiv:hep-th/9802150 | abstract only |
| Aharony et al. 2000 | arXiv:hep-th/9905111; DOI 10.1016/S0370-1573(99)00083-6 | abstract only |
| Bekenstein 1973 | DOI 10.1103/PhysRevD.7.2333 (Crossref) | not read (access refused) |
| Hawking 1975 | DOI 10.1007/BF02345020 (Crossref) | not read (access refused) |
| Bousso 2002 | arXiv:hep-th/0203101; DOI 10.1103/RevModPhys.74.825 | abstract only |
| Ryu, Takayanagi 2006 | arXiv:hep-th/0603001; DOI 10.1103/PhysRevLett.96.181602 | abstract only |
| Van Raamsdonk 2010 | arXiv:1005.3035; DOI 10.1007/s10714-010-1034-0 | abstract only |
| Polyakov 1981 | DOI 10.1016/0370-2693(81)90743-7 (Crossref) | not read |
| Vidal 2007 | arXiv:cond-mat/0512165; DOI 10.1103/PhysRevLett.99.220405 | abstract only |
| Swingle 2009/2012 | arXiv:0905.1317; DOI 10.1103/PhysRevD.86.065007 | abstract; text searched, main passages read |
| Swingle 2012 | arXiv:1209.3304 | abstract only |
| Pastawski et al. 2015 | arXiv:1503.06237; DOI 10.1007/JHEP06(2015)149 | abstract only |
| [Carlip17] | arXiv:1705.05417; DOI 10.1088/1361-6382/aa8535 | read in full (2026-10-23 note) |
| Amelino-Camelia et al. 2015 | arXiv:1505.04649; DOI 10.1142/S0218271815430026 | abstract only |
| Jacobson 1995 | arXiv:gr-qc/9504004; DOI 10.1103/PhysRevLett.75.1260 | abstract only |

None of these is in `REFERENCES.bib` yet except [Carlip17] (and [tHooft14], a different 't Hooft work). Adding any of
them, with these read statuses, is left to whoever cites them first (rule 1).

## Worth reading next, if the owner wants to go further

- Swingle, arXiv:1209.3304, for whether the emergent "scale" direction behaves like an ordinary direction of space.
  This bears most directly on a direction that opens and closes.
- Witten, arXiv:hep-th/9802150, the section on the large-N phase transition and AdS black holes: a published sharp
  change of bulk geometry.
- Bousso, arXiv:hep-th/0203101, Secs. on the covariant bound, for exactly what the area law claims and where it fails.
- 't Hooft's essay is short and its cube-face constraint construction is close enough to the toy that the owner may
  enjoy reading it directly (13 pages, no heavy mathematics past its Eq. (19)).

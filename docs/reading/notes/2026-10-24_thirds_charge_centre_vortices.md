# Reading note: thirds of charge, the Z6 quotient, and centre vortices (2026-10-24)

**Why this was read.** VISION Updates 96 to 103 give the owner's rules for matter strands: each body diagonal carries
a signed whole number of thirds; charge = −(net signed thirds) ÷ 3 (Update 101, sign as corrected by Update 102); anything
free carries a whole number of twists; a lone third is confined. Her handoff idea 3 said the opposite of the charge rule
("A one-third twist is not an electric charge of ±1/3"), and the reversal is put back to her
(`docs/design/owner_questions_2026-10-24.md`, items 0a to 0d). The table in
`sandbox/out/particle_handoff_looks_2026-10-24.txt`, part 5, shows that every observed particle satisfies
3Q + t = 0 mod 3, with t the count of quark thirds mod 3, and points to Tong (2017), then read at abstract only. This note
reads Tong in full, the centre-vortex sections of Greensite's review, 't Hooft (1978) at the level reachable, and the
relevant section of Baez and Huerta, to say what published mathematics already covers her rule and where it differs.
Her standing rule applies: existing mathematics that covers her idea is the good result.

**What was read, and how.** Read on 2026-10-24 by an assistant agent (Claude). PDFs were downloaded from arXiv and their
text extracted with PyMuPDF; journal references and DOIs were taken from the arXiv export interface and, for 't Hooft,
from Crossref and INSPIRE. The owner has not read any of these sources, and no physicist has reviewed this note.

**Labels.** Text in quotation marks is verbatim from the named source (extraction can drop sub- and superscripts; the
reconstruction is given in brackets where needed). Unmarked prose under a source is a paraphrase of that source.
*Ours, unverified* marks this note's own readings. *General knowledge, to verify* marks physics not read at source here.

---

## Sources

**[Tong17]** D. Tong, "Line operators in the Standard Model", JHEP 07 (2017) 104, doi:10.1007/JHEP07(2017)104,
arXiv:1705.01853 (v2, 12 June 2017). **Read in full** (18 pages; figures seen only as extracted labels). Already in
`REFERENCES.bib` as `Tong17`, whose note still says "Abstract read ... Full text not read"; that note is now out of date
(this file does not edit the bibliography; the change is owed).

**[Gre03]** J. Greensite, "The confinement problem in lattice gauge theory", Prog. Part. Nucl. Phys. 51 (2003) 1,
doi:10.1016/S0146-6410(03)90012-3, arXiv:hep-lat/0301023 (v2, 5 March 2003). **Read in part:** Sec. 1 (introduction),
Sec. 2 (what is confinement, including Sec. 2.2 "A first encounter with the center"), Sec. 3.1 (the Wilson loop),
Sec. 3.3 (the 't Hooft operator), Sec. 3.4 (the vortex free energy), Sec. 5 opening (the centre vortex confinement
mechanism, Eqs. (89) to (96)), Sec. 6.1 and 6.2 (centre dominance; vortex-limited Wilson loops), Sec. 6.6 (Casimir
scaling and centre vortices) and Sec. 6.7 (critique). Not read: Secs. 4, 5.1 onward in detail, 6.3 to 6.5, 7 onward
(monopoles, Coulomb gauge, large N). Not in `REFERENCES.bib`.

**[tH78]** G. 't Hooft, "On the phase transition towards permanent quark confinement", Nucl. Phys. B 138 (1978) 1-25,
doi:10.1016/0550-3213(78)90153-0. **Abstract only** (from INSPIRE, record 122455; the paper is behind the publisher's
paywall and not on arXiv). What the body says is taken only from [Gre03]'s account of it (Sec. 3.3, Eq. (43) and the
paragraph after), and is marked so. Cited by [Tong17] as its ref. [7] for 't Hooft lines. Not in `REFERENCES.bib`.

**[BH10]** J. C. Baez and J. Huerta, "The algebra of grand unified theories", Bull. Amer. Math. Soc. 47 (2010) 483-552,
arXiv:0904.1556. **Read in part:** the list of theorems (Sec. 1), the hypercharge representations (Sec. 2.3), and the
SU(5) section where the Z6 kernel is found (the passage from "give an isomorphism between GSM and S(U(2) × U(3))"
through "Table 3: Hypercharge relations" and the paragraph after it). The rest searched, not read. Not in
`REFERENCES.bib`.

---

## Terms, defined once

- **Gauge group.** The group of symmetry transformations that the forces of the Standard Model are built on: SU(3) for
  the strong force (colour), SU(2) for the weak force, U(1) for hypercharge. Electromagnetism's U(1) is a combination
  of the SU(2) and hypercharge parts left after the Higgs field condenses.
- **Centre of a group.** The elements that commute with every element. For SU(3) the centre is three matrices,
  1, ω·1 and ω²·1 with ω = exp(2πi/3) ([Gre03] Eq. (12) for SU(N)): turning every colour by the same third of a full
  phase turn. The centre of SU(3) is called **Z3**, of SU(2) **Z2** (the matrices ±1).
- **Triality (N-ality for SU(3)).** How a particle responds to the centre: a quark is multiplied by ω (triality 1), an
  antiquark by ω² (triality 2), a gluon or any colourless bound state by 1 (triality 0). [Gre03] Sec. 2.2: it is "the
  number of boxes in the corresponding Young tableau, mod N"; in plain terms, the number of quarks minus the number of
  antiquarks, mod 3. *Ours:* this is exactly the `t` of the sandbox table, part 5.
- **Z6 quotient.** Six combined transformations, each a hypercharge phase together with a centre element of SU(2) and of
  SU(3), act as the identity on every known particle ([Tong17] Sec. 3; [BH10] SU(5) section). "Dividing the gauge group
  by Γ" means declaring those transformations to be no transformation at all. Γ can be all six (Z6), the three that
  involve only colour and hypercharge (Z3), the two that involve only weak isospin and hypercharge (Z2), or none.
- **Wilson loop / Wilson line.** Carry a test charge round a closed path and record the phase (for colour, the
  rotation in colour space) it comes back with. A **Wilson line** in [Tong17] is the world line of an infinitely heavy
  electric test charge in a chosen representation.
- **'t Hooft line.** The same for an infinitely heavy *magnetic* test charge: a defect round which the gauge field is
  twisted ([Tong17] Sec. 2).
- **Line operator.** Either of these, or a combination (a dyonic line). Which line operators are allowed depends on Γ,
  even though no local experiment can tell the choices of Γ apart ([Tong17] Sec. 1).
- **Centre vortex.** A tube (in three space dimensions; a sheet in four-dimensional spacetime) of colour-magnetic flux
  in the gluon field, such that a Wilson loop in the quark representation that links it once picks up a centre element:
  for SU(3), a factor exp(±2πi/3) ([Gre03] Sec. 3.3, Eqs. (39) to (42)). It is a configuration of the gauge field, not
  a particle.
- **Area law.** A Wilson loop whose average falls off as exp(−σ × area) instead of exp(−constant × perimeter). An area
  law means the energy of a separated quark and antiquark grows in proportion to their distance (a string of tension σ):
  confinement ([Gre03] Sec. 3.1, Eq. (19)).

---

## [Tong17]: what it says

**The claim.** Abstract: "There is an ambiguity in the gauge group of the Standard Model. The group is G = SU(3) ×
SU(2) × U(1)/Γ, where Γ is a subgroup of Z6 which cannot be determined by current experiments." Sec. 1: "At present, we
can only say that the gauge group involves a quotient by Γ, which is a subgroup of Z6, i.e. Γ = Z6, Z3, Z2 or 1. Each of
these possibilities defines a different theory and, ultimately, gives rise to different physics."

**Why no current experiment decides.** Sec. 1: "Correlation functions of local operators in R^{1,3} depend only on the
Lie algebra of the gauge group and are unaffected by global issues such as the choice of Γ. This means that no current
experiment can distinguish between the four possibilities." Footnote 1: unification prefers Z6, "since only then is G
a subgroup of SU(5) or Spin(10). It may well be true that this is the way Nature works. However, the philosophy of this
paper is to admit our ignorance of the ultra-violet".

**The generator.** Sec. 3: Z6 "is generated by ξ = e^{2πiq/6} ⊗ η ⊗ ω where η ∈ Z(SU(2)) obeys η² = 1 and
ω ∈ Z(SU(3)) obeys ω³ = 1 and q is the U(1)_Ỹ charge. The quotient Γ = Z3 is generated by ξ² and the quotient Γ = Z2 is
generated by ξ³." Tong's hypercharge is normalised to integers, Ỹ = 6Y (footnote 2).

**The charge pattern, as a statement about which lines exist.** Sec. 3, for Γ = Z3: "Wilson lines must now be invariant
under ξ². This mean that electric lines must have q = z₃ᵉ mod 3." For Γ = Z6: "the Abelian charge is q = 3z₂ᵉ − 2z₃ᵉ
mod 6. It is noticeable that all fundamental fermions in the Standard Model obey this relationship between the
charges." He lists them: left-handed lepton (2,1)₋₃, right-handed electron (1,1)₋₆, left-handed quark (2,3)₊₁,
right-handed up (1,3)₊₄, right-handed down (1,3)₋₂, and the Higgs (2,1)₃; "The fact that all Standard Model fields
satisfy q = 3z₂ᵉ − 2z₃ᵉ mod 6 is, of course, equivalent to the statement made in the introduction that the Standard Model
gauge group is consistent with U(1) × SU(2) × SU(3)/Z6." Footnote 3 adds that Wilson lines are heavy test charges, not
the chiral fermions themselves, "Nonetheless, both sit in representations of the gauge group with Γ = Z6."

**The Dirac condition between electric and magnetic lines** (Eq. (3.1)): (−1)^{z₂ᵉz₂ᵐ} (e^{2πi/3})^{z₃ᵉz₃ᵐ} e^{−2πiqg} = 1,
equivalently 3z₂ᵉz₂ᵐ + 2z₃ᵉz₃ᵐ − 6qg ∈ 6Z. For Γ = Z3 it "now allows lines with SU(3) magnetic charge z₃ᵐ = 0, 1, 2, as
long as they are accompanied by Abelian magnetic charge g = z₃ᵐ/3." For Γ = Z6 "a basis of magnetic operators is
(z₂ᵐ, z₃ᵐ)_g = (1, 0)_{1/2} and (0, 1)_{1/3}."

**After the Higgs condenses** (Sec. 3.2): Q = q/6 + λ₂ᵉ/2, normalised so that the electron has Q = −1. Minimum electric
charge of a line operator: Γ = 1, Q = 1/6; Γ = Z2, 1/3; Γ = Z3, 1/6; Γ = Z6, 1/3; minimum magnetic charge G = 6, 3, 2, 1
respectively. For Z3 and Z6 the naive Dirac condition QG ∈ Z fails; "the magnetic monopole must also carry colour
magnetic charge" (Corrigan and Olive, his ref. [10], not read by us).

**What would decide it** (Sec. 4): "Obviously, if a neutral quark is discovered, transforming in the (1, 3)₀
representation of G, then we must take Γ = Z2 or 1. In contrast, as we saw above, the discovery of a magnetic monopole,
consistent with the minimum Dirac quantisation with respect to the electron, but not with respect to the quark, would
mean that Γ = Z6. Of course, these predictions are rather toothless: the particles have a mass which is constrained only
by the Planck scale". He also notes the conjecture that in a theory with gravity every charge carried by a line operator
is carried by some dynamical object (his refs. [18], [19], not read by us).

**The hypercharge theta angle.** Sec. 3.1: the quotient Γ = Z_p extends the range of the hypercharge theta angle to
[0, 2πp²) while θ₂ and θ₃ keep period 2π (Eq. (3.2)). Not needed for her questions.

## [BH10]: the same fact, in plain algebra

The map from U(1) × SU(2) × SU(3) onto the block matrices S(U(2) × U(3)) inside SU(5) "has a kernel, Z6. The kernel
is the set of all elements of the form (α, α⁻³, α²) ∈ U(1) × SU(2) × SU(3) and this is Z6, because scalar matrices α⁻³
and α² live in SU(2) and SU(3), respectively, if and only if α is a sixth root of unity." Then: "the SU(5) GUT is doomed
unless Z6 acts trivially on every fermion." Checking each case turns into four rules (their hypercharge convention is
Q = I₃ + Y/2, so Y is twice Tong's Y): left-handed quark "Y = even integer + 1/3", left-handed lepton "Y = odd integer",
right-handed quark "Y = odd integer + 1/3", right-handed lepton "Y = even integer" (their Table 3). "SU(5) passes the
test, not despite the bizarre pattern followed by hypercharges, but because of it!" And: "Z6 is the entire kernel.
Because of this, we could say that GSM/Z6 is the 'true' gauge group of the Standard Model."

*Ours, unverified:* [BH10] and [Tong17] agree on the arithmetic and differ only in emphasis. [BH10] says Z6 is the
kernel of the representation on the known fermions, which is a fact about the particles found so far. [Tong17] says
whether the gauge group itself is divided by Z6 (or Z3, Z2, nothing) is a separate question, not yet settled by
experiment, because it is a statement about particles and line operators that might exist and have not been seen.

## [Gre03]: centre vortices and confinement

**State of the field (as of 2003).** Sec. 1: "Despite efforts stretching over thirty years, there exists no derivation
of quark confinement starting from first principles, nor is there a totally convincing explanation of the effect. It is
fair to say that no theory of quark confinement is generally accepted, and every proposal remains controversial." The
centre-vortex picture is one of two proposals the review treats at length (the other, abelian monopoles).

**Absence of fractional charge is not the definition of confinement.** Sec. 2: free-quark searches look for "free
(hadronic) particles with electric charge ±1/3 e and ±2/3 e. But this experimental fact, from a modern perspective, is
not so very fundamental. It may not even be true. Suppose that Nature had supplied, in addition to the usual quarks, a
massive scalar field in the 3 representation of color SU(3), having otherwise the quantum numbers of the vacuum. In that
case there would exist bound states of a quark and a massive scalar, which together would have the flavor quantum
numbers of the quark alone. ... If so, particles with fractional electric charge await discovery at some future
detector." *Ours:* this hypothetical scalar is Tong's "neutral quark" (1,3)₀, whose discovery would exclude Γ = Z3 and Z6.

**Triality decides what can screen a quark.** Sec. 2.2: "a quark of non-zero N-ality can never form a color singlet by
binding to one or more particles of zero N-ality." Sec. 3.1: "gluons themselves are zero N-ality particles", so gluons
can break the string only between sources of zero N-ality; "Only the string tension σ_r of non-zero N-ality sources can
serve as an order parameter for the confined phase" (Eq. (20)).

**How a centre vortex is made** (Sec. 3.3). In electromagnetism the field outside a thin solenoid is zero, yet an
electron carried round it picks up the phase e^{iΦ_B} (Aharonov–Bohm, Eqs. (32) to (35)). For SU(N), a singular gauge
transformation with a jump g(x(1)) = z g(x(0)), z ∈ Z_N, on every loop linking a closed surface S gives
"U(C) → z* U(C)" (Eqs. (39), (40)), and "the singular transformation creates a surface of infinite field strength along
S in the continuum gauge theory, which is known as a thin center vortex. For an SU(N) gauge group there are N − 1
possible vortices, corresponding to the number of elements in Z_N different from the identity. ... it is possible to ...
smear out the thin vortex into a surface-like region of finite thickness, and finite field strength. This is a 'thick'
center vortex." On the lattice: multiply one column of links by z (Eq. (41)); "All x−y plaquettes on the surface S ...
are transformed by a center element U(P) → zU(P)" (Eq. (42)). Linking: "a closed loop can be topologically linked to a
hypersurface of co-dimension 2", a loop to a loop in three dimensions, a loop to a surface in four.

**'t Hooft's algebra** (Sec. 3.3, as [Gre03] reports [tH78]; the 1978 paper itself not read). An operator B(C) creates
a thin centre vortex on a curve C, and U(C′)B(C) = zB(C)U(C′) for a Wilson loop C′ linking it once (Eq. (43)). "Using
only this commutation relation, 't Hooft argued ... that only area-law or perimeter-law falloff for the U(C), B(C)
expectation values is possible, and that in the absence of massless excitations, the simultaneous behavior [both
perimeter law] is ruled out". So a perimeter law for the vortex operator implies confinement (area law for Wilson
loops). The [tH78] abstract says the same in its own terms: in 3+1 dimensions "the topological operators and the gauge
field operators form a closed algebra from which it is deduced that this system can be in one of the four different
phases: (i) spontaneous breakdown via an explicit or composite Higgs field, (ii) no Higgs field but permanent
confinement of gauge quantum numbers, (iii) Higgs effect and still confinement, presumably only if there is an unbroken
subgroup, and (iv) an intermediate phase (critical point?) with massless particles."

**The mechanism** (Sec. 5). Motivation: "the asymptotic string tension σ_r, extracted from Wilson loops in the r
representation of color SU(N), depends only on the N-ality k_r of the representation; i.e. σ_r = σ(k_r)" (Eq. (89)); "In
particular, σ_r = 0 if k_r = 0." If vortices pierce a large planar loop at random, with short-range correlations
(Eq. (94)), each piercing contributes a factor Z^{k_r}, and ⟨χ_r[U(C)]⟩ ≈ d_r exp[−σ(k_r)Σ] (Eq. (95)), an area law
whose tension depends only on triality: "conﬁnement is simply a matter of short range correlations in the center flux on
minimal surfaces".

**Numerical evidence and its limits** (Sec. 6; almost all for SU(2), whose vortex phase is −1). Centre projection keeps
the string tension to "about 10%" ("center dominance", Sec. 6.1); removing the vortices removes confinement (Fig. 18);
a Wilson loop pierced by n vortices tends to (−1)^n times the unpierced one (Eq. (156), Fig. 19). Vortices are "comparatively
thick objects, with a surface thickness on the order of one fermi" (Sec. 6.6). Critique (Sec. 6.7): the agreement
"varies widely among different adjoint gauges, and among Gribov copies"; "the real argument that center projection
locates vortex configurations is at present empirical"; Casimir scaling is compatible with vortices but not predicted
to the accuracy seen; the Lüscher term has not been seen in centre-projected data.

---

## What it supplies to her theory

### (a) "Anything free carries a whole number of twists" against the observed charge pattern

**The published statement.** Every observed particle obeys a lock between the fractional part of its electric charge
and its triality. In [Tong17]'s notation the Z3 condition is q ≡ z₃ᵉ (mod 3) with Q = q/6 + λ₂ᵉ/2; since
3λ₂ᵉ ≡ 0 (mod 3), 2(3Q) = q + 3λ₂ᵉ ≡ z₃ᵉ (mod 3), so **3Q + t ≡ 0 (mod 3)**, with t = z₃ᵉ the triality (*ours:
two lines of arithmetic on Tong's Sec. 3 and 3.2, checked against every row of the sandbox table, part 5*). In words:
an object with no net quark thirds has a whole-number charge; one net quark third forces a charge of −1/3 plus a
whole number; two force +1/3 (equivalently −2/3) plus a whole number. This is the Z3 part of the Z6 relation. The Z2
part ties weak isospin to hypercharge and has no counterpart in her rule yet.

**Status, exactly.**
- *Measured:* every particle found so far satisfies it ([Tong17] Sec. 3, "all fundamental fermions in the Standard
  Model obey this relationship"; the Higgs too). Free-quark searches have found no colour-neutral object with
  fractional charge ([Gre03] Sec. 2 refers to them; the searches themselves are not read here: general knowledge, to
  verify).
- *Not known:* whether the lock is a law, that is whether the gauge group is divided by Z3 (Γ = Z3 or Z6) so that no
  particle could ever break it, or only a fact about the particles we have found (Γ = Z2 or 1). [Tong17]: "Γ is a
  subgroup of Z6 which cannot be determined by current experiments". A discovered neutral colour triplet would give
  Γ = Z2 or 1; a monopole of minimum Dirac charge relative to the electron but not the quark would give Z6 (Sec. 4).
  Unification prefers Z6 (footnote 1), which is theory, not data.

**How her rule maps onto it** (*ours, unverified*). Her rule, charge = −(net signed thirds) ÷ 3, with "free means a whole
number of twists" (net thirds a multiple of 3), gives exactly 3Q + t ≡ 0 (mod 3) with t = net thirds mod 3, and makes it
a law. So in the published language **her rule chooses Γ ⊇ Z3**: it predicts that no colour-neutral fractionally
charged particle exists at any mass, and no neutral quark-like triplet. That is a real prediction: it is the side Tong
says a "neutral quark" discovery would refute. It is not one that current experiment can confirm, since experiment does
not yet decide between Γ choices; it is consistent with every particle observed.

Her rule says more than the published lock in one respect. The published relation holds only mod 1: an up quark
(t = 1) has Q = +2/3 and a down quark (t = 1) has Q = −1/3; the whole-number part comes from weak isospin and
hypercharge, not from colour. Her rule fixes the whole charge from the thirds, so the up quark needs net thirds −2 (and
−2 ≡ 1 mod 3, the correct triality) and the down quark +1 (*ours, arithmetic*). That is an allowed lift of the mod-3
relation, but it makes the strand count carry what the Standard Model splits between colour and hypercharge. Whether her
strands can also carry the weak (Z2) half is open.

Her rule also covers only matter strands; free dark strands of ½ and 1.5 (Update 101, audit item 6) are outside it, and
nothing in these papers bears on them.

### (b) Is a centre vortex a published "neutral one-third twist"?

**Yes, in a precise sense.** A centre vortex of SU(3) is a tube of the gluon field round which a quark (triality 1)
Wilson loop picks up exp(±2πi/3), one third of a full phase turn, while a gluon or any colourless object picks up
nothing ([Gre03] Sec. 3.3, Eqs. (39) to (42); Sec. 5, Eq. (89) and "σ_r = 0 if k_r = 0"). It carries no electric charge
and is not a particle; it is a twist in the field. *Ours, unverified:* that matches her handoff idea 3 ("a one-third twist
is not an electric charge of ±1/3") closely as a statement about an object: there is a published one-third twist that
is neutral.

**Where it differs from idea 3.** In idea 3 the neutral third is a building block of matter. A centre vortex is not: it
is a configuration of the vacuum's gluon field, proposed as what makes quarks confined, and it lives in pure gauge theory
with quarks taken infinitely heavy ([Gre03] Sec. 3.1, "conﬁnement is a property of the gauge theory vacuum in the
absence of matter ﬁelds"). It changes the phase of a quark that goes round it; it is not something a quark is made of.
And the mechanism is a proposal, not settled physics ([Gre03] Secs. 1 and 6.7).

**Her gluon question.** She predicts gluons carry no half-curl. The published counterpart (*ours, unverified, as a
reading*) is that gluons have triality zero: centre elements act on them as the identity ([Gre03] Sec. 2.2), they cannot
screen a quark's triality, and Wilson loops in the gluon (adjoint) representation have zero asymptotic string tension
(Eq. (89)). So "gluons carry none of the thirds and do not see the one-third twist" is published. Her word was "half-curl",
not "third"; in her picture the half is the photon's bound twist and the dark strands' unit, and these papers say nothing
about that.

*A coincidence, recorded under rule 13 and given no weight:* for SU(2) the centre is Z2 and the vortex phase is −1, a
half turn ([Gre03] Sec. 3.4, Eq. (45); Sec. 6.2). Her dark strands carry halves (Update 97). Nothing connects the two.

**The tie between the colour third and the charge third** (*ours, unverified; arithmetic on [Tong17] Eq. (3.1)*). For
Γ ⊇ Z3, a purely colour-magnetic third (z₃ᵐ = 1) is not allowed on its own; it must come with a hypercharge-magnetic
third, g = 1/3. Combined, the colour phase and the hypercharge phase cancel on every Standard Model particle: a quark
with z₃ᵉ = 1, q ≡ 1 (mod 3) gets e^{2πi/3} e^{−2πi/3} = 1, an electron gets 1. So in a world with the Z3 quotient, "a
third of colour twist" and "a third of charge twist" are one twist seen two ways, which is the published shape of her
rule that the thirds are the charge. Whether this is a fair reading of her strands, which are electric rather than
magnetic, is for a physicist.

### (c) Her questions 0a, 0b and confinement

**0a (keep "charge = thirds ÷ 3", or keep idea 3?)** (*ours, unverified*). The published lock says a third that carries
triality also carries a fractional charge (mod 1); no known particle has triality 1 and a whole-number charge. So for
the thirds that make quarks, the charge rule agrees with observation and idea 3 would not, unless an integer offset
cancels it. Both can stand if they are about different objects: the charge rule for matter strands' thirds (as now), and
idea 3 for a neutral one-third twist of the field that is not matter, which is what a centre vortex is. The choice is
hers; these sources only say that the second object has a published form.

**0b (an electron against three down quarks)** (*ours, unverified*). In the Standard Model the electron and a three-down
baryon (the Δ⁻, ddd: general knowledge, to verify) both have triality 0 and charge −1. They are told apart by colour
content and by baryon and lepton number, not by charge. So the published answer to "what separates them" is: another
count. Under her rule the electron's three thirds would carry baryon-like content unless the electron's thirds are
bound differently from quarks'. The nearest published model already makes this distinction: in Bilson-Thompson's braids
the electron is one braid of three ribbons all twisted the same way, each twist "an electric charge of ±e/3", and a
colour is the position of the odd ribbon out, so an all-alike triple has no colour; a down quark is one braid with a
single twisted ribbon ([BT05] Sec. II; `docs/reading/notes/2026-10-21_matter_as_loops.md`, section 3). The difference
between an electron and three downs there is three thirds on one braid against one third on each of three braids.

**Confinement.** Her "a lone third is confined" is the published confinement criterion stated for triality: sources of
non-zero triality have an area law; triality-zero sources are screened ([Gre03] Sec. 3.1, Eq. (20); Sec. 5, Eq. (89)).
Her "anything free carries a whole number of twists" is a stronger statement: it adds that no heavy colour-triplet,
colour-neutral field exists that could bind to a quark and make a free fractional charge, which [Gre03] (Sec. 2) says is
"conceivable (albeit unlikely)". In Tong's terms that addition is Γ ⊇ Z3 (*ours, unverified*).

---

## Where it differs

- **Strands against fields.** These papers are about representations of a gauge group and configurations of a gauge
  field. Her thirds are integers carried by body diagonals of a graph. The mapping above (her net thirds mod 3 = triality)
  is ours and unverified; nothing in the sources says that triality is a twist of a strand.
- **Exact against mod 3.** The published lock fixes charge only mod 1; her rule fixes the whole charge. The Standard
  Model needs weak isospin and hypercharge for the whole-number part.
- **Law against fact.** Whether the lock is a law (Γ ⊇ Z3) is open in the literature; her rule takes it as a law. That
  is a prediction, not a derivation.
- **A centre vortex is not a building block.** The neutral one-third twist that exists in print is a vacuum field
  configuration that confines quarks (a proposal, debated), not a constituent of particles.
- **The Z2 half has no counterpart yet.** The Z6 relation ties weak isospin to hypercharge as well (the left-handed
  doublets); her rule says nothing about the weak force.
- **Nothing on dark strands.** None of the sources bears on half-twist dark strands or one-sided closure.

## Reading owed

- [tH78] in full (paywalled; the account here is [Gre03]'s).
- Aharony, Seiberg and Tachikawa (2013), arXiv:1305.0318, Tong's ref. [1], the general theory of which line operators
  a gauge group allows. Not read.
- Corrigan and Olive (1976), Tong's ref. [10], on monopoles needing colour-magnetic charge. Not read.
- [Gre03] Secs. 5.1 to 6.5 and 7 in full; SU(3)-specific centre-vortex studies (his refs. [77], [82]). Not read.
- `REFERENCES.bib`: update `Tong17`'s note to "Read in full (2026-10-24)"; add [Gre03], [tH78] (abstract only) and [BH10]
  (read in part). Not done in this note (the task allowed one new file).

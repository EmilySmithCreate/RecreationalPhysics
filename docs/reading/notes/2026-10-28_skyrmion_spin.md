# Reading: the proton as a twist of a field with spin one half (Skyrme; Finkelstein and Rubinstein; Witten)

A reading note, not a prior-work search: it records what the published line says, with how much of each source was
read, so that the owner's question (how can a whole-number twist carry spin one half?) can be set against it. It
follows the shape of `prior_work_template.md` where that fits (sources, what was read, what came closest, what would
change the reading). It complements `2026-10-24_spin_from_loops_and_landauer.md`, which covered the
Finkelstein-Rubinstein constraint through [Kru03] and found that a finite set of graph labellings has no loop in it to
carry the sign; nothing here contradicts that note. **No tracked file other than this note is changed.**

Kinds of statement (rule 10): **published** (with how much was read); **exact** (arithmetic on a published formula);
**ours, unverified** (interpretation). "General knowledge, to verify" marks a statement from memory, not checked at a
source in this session.

**Date:** 2026-10-28 by the clock of the task (`date` on the laptop read Tue 27 Oct 22:12 EDT when the work was done;
the filename follows the task's date). **Who read:** an assistant agent (Claude), from the worktree
`particle-sector`; the owner has read none of the sources. PDFs were downloaded from arXiv to the session's scratchpad
and read as text (`pdftotext`, plain and UTF-8 modes; Greek letters were lost in the plain mode, so every equation
below was checked in the UTF-8 extract or is marked).

## 1. Sources and read status

**The three originals were not read.** None has an open copy that this session could reach: ScienceDirect returned
403 for Witten's papers, and two web searches found no free PDF of [FR68], [Wit83a] or [Wit83b]; Skyrme's papers were
not searched beyond their records. What is said about them comes from their abstracts (INSPIRE, the publisher's
abstract as stored there) and from the reviews named against each claim.

| Key | Source | Read status |
|---|---|---|
| [Sky61] | T. H. R. Skyrme, "A non-linear field theory", Proc. R. Soc. Lond. A 260 (1300), 127–138 (1961), doi:10.1098/rspa.1961.0018 (checked at Crossref) | **Not read.** Described through [Ait20], pp. 9–10 (the paragraph on "the remarkable third paper in the series"), which quotes its winding-number formula. |
| [Sky62] | T. H. R. Skyrme, "A unified field theory of mesons and baryons", Nucl. Phys. 31, 556–569 (1962), doi:10.1016/0029-5582(62)90775-7 (INSPIRE) | **Abstract only** (INSPIRE, Elsevier abstract), plus [Ait20] p. 11. |
| [FR68] | D. Finkelstein and J. Rubinstein, "Connection between spin, statistics, and kinks", J. Math. Phys. 9 (11), 1762–1779 (1968), doi:10.1063/1.1664510 (checked at Crossref) | **Abstract only** (INSPIRE, AIP abstract, read in full), plus [Kru03] Sec. 2.1 and [Giu93] abstract and introduction. Already in `REFERENCES.bib` as "Not read". |
| [Wit83a] | E. Witten, "Global aspects of current algebra", Nucl. Phys. B 223, 422–432 (1983), doi:10.1016/0550-3213(83)90063-9 (INSPIRE) | **Abstract only** (INSPIRE, Elsevier abstract). Its Wess-Zumino term and quantization law are described through [SW99] Sec. 3.1, Eq. (3.12) and footnotes 3–5. |
| [Wit83b] | E. Witten, "Current algebra, baryons, and quark confinement", Nucl. Phys. B 223, 433–444 (1983), doi:10.1016/0550-3213(83)90064-0 (INSPIRE) | **Abstract only** (INSPIRE, Elsevier abstract). The N_c-odd result is described through [SW99] Sec. 4.1 (Eqs. 4.7–4.11 and the paragraph after), [Cat03] p. 2, [JM04] (Eqs. 6, 7 and the paragraph after), [Kru03] Sec. 1. |
| [SW99] | J. Schechter and H. Weigel, "The Skyrme model for baryons", arXiv:hep-ph/9907554 (1999); pp. 337–369 of a volume recorded by INSPIRE as record 542037 (title of the volume to verify) | **Read in part:** Sec. 2 opening (Eqs. 2.1–2.5), Sec. 3.1 (Eq. 3.12, the quantization of its coefficient, footnotes 3–5, consequences (i), (ii)), Sec. 4 opening and Sec. 4.1 (Eqs. 4.7–4.11 and the paragraph after), the start of Sec. 4.2 (Eq. 4.14 and footnote on allowed representations). |
| [Ait20] | I. J. R. Aitchison, "Tony Skyrme and the origins of Skyrmions", arXiv:2001.09944 (2020); journal publication to verify | **Read in part:** abstract, introduction, the section on Skyrme's motives, and the pages on the sine-Gordon kink, the third paper and the sixth paper (pp. 1–11 of the arXiv PDF). |
| [Kru03] | S. Krusch, "Homotopy of rational maps and the quantization of Skyrmions", Ann. Phys. 304, 103–127 (2003), arXiv:hep-th/0210310 | **Read in part:** Sec. 1 (paragraphs 2–3), Sec. 2.1 (Eqs. 2–8), and the passage around Eqs. (74)–(75). Already in `REFERENCES.bib`. |
| [Giu93] | D. Giulini, "On the possibility of spinorial quantization in the Skyrme model", Mod. Phys. Lett. A 8, 1917–1924 (1993), doi:10.1142/S0217732393001641, arXiv:hep-th/9301101 | **Read in part:** abstract, introduction, opening of Sec. 1. |
| [Cat03] | S. Catto, "Effective hadronic Lagrangians based on QCD: potential models and Skyrmions", arXiv:hep-th/0302101 (2003); journal publication to verify | **Read in part:** p. 2 only (the paragraph summarizing Witten's 2π rotation). |
| [JM04] | E. Jenkins and A. V. Manohar, "The chiral soliton model for arbitrary colors and flavors", Phys. Rev. D 70, 034023 (2004), doi:10.1103/PhysRevD.70.034023, arXiv:hep-ph/0402150 | **Read in part:** the hypercharge constraint, Eqs. (4)–(7), the counting of boxes, and the two "modulo two" sentences. |
| [Pra92] | M. Praszalowicz, "Strangeness in Skyrme and in Nambu-Jona-Lasinio models", Siegen Baryons Workshop 1992, pp. 43–56, arXiv:hep-ph/9211278 | **Read in part:** Sec. 3, Eqs. (24)–(26). |
| [War95] | R. S. Ward, "Stable topological Skyrmions on the 2D lattice", Lett. Math. Phys. 35, 385–393 (1995), doi:10.1007/BF00750845, arXiv:hep-th/9502048 | **Read in part:** abstract, Sec. 1, Sec. 2 to just after Eq. (5). |
| [CIK15] | E. G. Charalampidis, T. A. Ioannidou and P. G. Kevrekidis, "Lattice three-dimensional skyrmions revisited", Phys. Scripta 90, 025202 (2015), doi:10.1088/0031-8949/90/2/025202, arXiv:1411.1313 | **Abstract and the opening of Sec. 1 only**; searched for "spin", "fermion", "statistic", "quantiz": no hits. |

## 2. Terms, in plain words

- **Field with values in a sphere.** At each point of space the field is a point on a 3-sphere (four numbers with
  σ² + π₁² + π₂² + π₃² fixed), or, equivalently, a 2×2 unitary matrix U of determinant 1 (the group SU(2)).
- **Winding number (baryon number B).** If the field takes the same value at every far-away point, space is in effect
  closed up into a 3-sphere, and the field is a map from one 3-sphere onto another. B counts how many times the field
  covers its target sphere, with sign. It is a whole number and cannot change under any continuous change of the
  field.
- **Configuration space.** The set of all fields of finite energy, one point per whole field. It splits into pieces,
  one per value of B.
- **Collective coordinates.** The handful of numbers that say how a fixed soliton is rotated (in space or in the
  internal "isospin" or "flavor" directions); the quantum soliton is a wavefunction of these.
- **Wess-Zumino (WZ) term.** An extra term in the action that cannot be written as an integral over ordinary spacetime
  of a local expression; it is written as an integral over a five-dimensional region whose boundary is spacetime. It
  exists only when the field has three or more flavors.

## 3. What each source says

### 3.1 Skyrme (1961, 1962): the winding number is the baryon number (via [Ait20])

- [Ait20] p. 9, on [Sky61]: "Here for the first time in particle physics, the concept of a winding number is
  introduced, which is a conserved quantity measuring (in this case) the number of times three-dimensional space is
  mapped by the fields onto the elementary volume of angular field space."
- [Ait20] p. 10 gives Skyrme's definition, for four fields φ = (π₁, π₂, π₃, σ) on a sphere of radius f (the
  normalization of φ relative to f as printed in [Ait20]; to verify against [Sky61]):

      N = −(1/2π²) ∫ det(φ, ∂ₓφ, ∂ᵧφ, ∂_zφ) d³x                        ([Ait20] p. 10, quoting [Sky61])

  and Skyrme "showed that such a configuration carried the value N=1" for the hedgehog
  πᵢ = f (rᵢ/r) sin ϑ(r), σ = f cos ϑ(r), with ϑ(0) = π and ϑ(∞) = 0. (2π² is the volume of the unit 3-sphere.)
- The same quantity in matrix form, [SW99] Eq. (2.2): the topological current

      B^μ = (1/24π²) ε^{μνρσ} tr[(U†∂_νU)(U†∂_ρU)(U†∂_σU)],   B = ∫ d³x B⁰

  ("This number counts the coverings of the target space and is the charge ∫d³x B⁰ associated with the topological
  current", [SW99] Sec. 2; the overall sign and the order of factors in the extract were partly lost, to verify
  against the PDF page). [SW99] Sec. 3.1 (ii): with three flavors and the gauged WZ term, "this current is identical
  to the topological current B^μ in eq (2.2)", which is why B is the baryon number.
- On spin, [Ait20] p. 11: Skyrme "ended this classic paper by giving arguments to suggest that, as in the S-G case, the
  idealized point-like soliton would obey a 4-dimensional Dirac equation"; and of the 1962 paper, "Tony was unable to
  construct operators which created or destroyed the sources represented by the solitons in the point-like limit ...
  That remains an unsolved problem." So Skyrme conjectured the fermion; he did not prove it. [Sky62]'s abstract
  (INSPIRE) says only that the theory "may contain its own sources" and that "the structure of the particle source in
  the classical theory is calculated".
- [Ait20] abstract: Skyrme's program was "making fermionic nucleons out of bosonic pion fields"; p. 3: "you can easily
  add half-integers to make whole integers, but how do you make half-integers out of whole ones?" (his framing of the
  owner's question, in 1958–62).

### 3.2 Finkelstein and Rubinstein (1968): half-odd spin is *allowed*, from the topology of configuration space

- [FR68] abstract (INSPIRE, verbatim excerpts): kinks are modes "whose number is strictly conserved in virtue of
  boundary conditions and continuity"; "with canonical commutation (not anticommutation) relations ... even if the
  intrinsic angular momentum is an integer, a rotating kink can have half-odd angular momentum, if double-valued state
  functionals are admitted"; "for fields with integer-valued intrinsic angular momentum, the observed relation between
  spin and (exchange) statistics follows from continuity alone, parastatistics being excluded"; "while the rotational
  spectrum of a kink will in general possess both integer and half-odd spin states ... only one of these two
  possibilities will ever be observed for each kind of kink".
- **The loop is not π₁(SO(3)) by itself.** [Kru03] Sec. 2.1, Eq. (2): the configuration space Q_B of the SU(2) model
  in each sector has

      π₁(Q_B) = π₄(S³) = Z₂                                                   ([Kru03] Eq. 2)

  (the step π₁(Q₀) ≅ π₄(S³) is credited there to Finkelstein, "Kinks", J. Math. Phys. 7, 1218 (1966); not read). A
  wavefunction on the double cover may change sign round the nontrivial loop, [Kru03] Eq. (7). A 2π rotation of
  space is a loop in SO(3) that is not contractible there (π₁(SO(3)) = Z₂); it gives half-integer spin only if its
  image in Q_B is the nontrivial loop: "When a 2π rotation gives rise to a nontrivial loop then this corresponds to
  half integer spin" ([Kru03] after Eq. 8). Whether it is depends on B:
- [Giu93] abstract: "loops generated by 2π-rotations are contractible in the even-, and non-contractible in the
  odd-winding-number sectors". [Kru03] Eqs. (74)–(75) recover this: a 2π rotation gives N = B² in π₁ = Z_{2B} of the
  rational-map space, contractible for B even, non-contractible for B odd.
- **Allowed, not forced.** [Kru03] Sec. 1: "For the SU(2) Skyrme model there is a choice whether to quantize a
  Skyrmion as a boson or a fermion when B is odd. Yet, it has to be quantized as a boson if B is even". And, from
  [FR68] as reported by [Kru03] after Eq. (8): "Q_B admits half integer spin if and only if it admits odd exchange
  statistics."

### 3.3 Witten (1983): with three flavors the choice is fixed, and it is fixed by N_c

- [Wit83a] abstract (INSPIRE): "A new mathematical framework for the Wess-Zumino chiral effective action is described.
  It is shown that this action obeys an a priori quantization law, analogous to Dirac's quantization of magnetic
  change [sic, "charge"]. It incorporates in current algebra both perturbative and non-perturbative anomalies."
- [Wit83b] abstract (INSPIRE): "It is shown that ordinary baryons can be understood as solitons in current algebra
  effective lagrangians. The formation of color flux tubes can also be seen in current algebra, under certain
  conditions." **Neither abstract states the N_c-odd result; it is taken from the reviews below.**
- **The WZ term and its quantization**, [SW99] Sec. 3.1, Eq. (3.12):

      Γ = λ ∫_{M₅} tr ε^{μνρστ} α_μ α_ν α_ρ α_σ α_τ,     λ = −i n / (240 π²),  n ∈ Z

  with α_μ = U†∂_μU (the definition of α_μ is in a part of [SW99] not read; to verify), and M₅ a five-dimensional
  region with ∂M₅ = spacetime. "The choice of M5 is not unique because its complement has the same boundary. In order
  to nevertheless have a unique action the constant λ ... must be quantized", footnote 3: "the analogy to Dirac's
  quantization of the magnetic monopole". Footnote 4: "the term (3.12) vanishes in the case of two flavors". Sec. 3.1
  (i): matching π⁰ → γγ "requires setting n = N_C, i.e. the Wess-Zumino term is proportional to the number of
  colors."
- **The collective Lagrangian**, [SW99] Eq. (4.7): rotating the hedgehog by an SU(3) matrix A(t), the WZ term
  contributes a term linear in the eighth angular velocity, proportional to N_C B Ω₈/(2√3) (Eq. 4.8 gives the
  separation used). By Eq. (4.10) this fixes the "right generator" R₈ = −N_C B/(2√3), i.e. the right hypercharge
  Y_R = 2R₈/√3 has magnitude N_C B/3 ("Y_R = 2R₈/√3 = 1 for B = 1 and N_C = 3"; the sign conventions in the extract
  are partly lost, to verify). [Pra92] Sec. 3: "The constraint Y_R = N_c/3 selects the representations of triality
  zero: 8, 10, 10̄, 27, 35, 35̄, 64, ... for N_c = 3" (his Eq. 25).
- **The spin argument**, [SW99] Sec. 4.1, after Eq. (4.11), verbatim: "In analogy to the Gell-Mann Nishijima relation
  a right charge Q_R = −J₃ + Y_R/2 may be defined. Completing the analogy we note that the eigenvalues of Q_R are 0,
  ±1/3, ±2/3, ±1, .... Hence for Y_R = 1 the relation (4.11) can only be fulfilled when the eigenvalue of J₃ is
  half-integer. This yields the important conclusion that the SU(3) model describes fermions. A priori this is not
  expected since the starting point has been an effective model of bosons. This discussion can be generalized to
  arbitrary N_C showing that the Skyrmion describes fermions when N_C is odd and bosons when N_C is even [30]."
  ([30] is [Wit83a].)
- **The 2π rotation**, [Cat03] p. 2, verbatim: Witten "rotated a skyrmion adiabatically through 2π-radians and found
  that the skyrmion had picked up a phase of N_cπ. Hence a skyrmion is a fermion if N_c is odd." (A one-sentence
  summary; the derivation was not read.)
- **For any number of flavors F**, [JM04]: "The hypercharge constraint says that there must be a state with Y = N_c in
  R" (their normalization of Y); allowed tableaux "have N_c + rF boxes"; and "Taking the last relation in Eq. (6)
  modulo two shows that the soliton is a fermion or boson depending on whether N_c is odd or even. The cases F = 4, 3,
  2 are all special and must be considered individually"; for F = 3, "Using the above equations modulo two shows that
  the soliton is a fermion or boson depending on whether N_c is odd or even."
- [Kru03] Sec. 1, summarizing both: "Witten showed in Refs. [6, 7] that in the SU(3) model the B = 1 Skyrmion has to be
  quantized as fermion if the number of colours is odd, yet no such restriction applies to the SU(2) Skyrme model."

### 3.4 On a lattice

- [War95] Sec. 1: "In the usual lattice version of the O(3) sigma model, namely the Heisenberg model, the topological
  properties are essentially lost (which is what one would expect, since topology has to do with continuity)." Sec. 2:
  removing "exceptional" configurations by hand leaves sectors "labelled by an integer N", but minimizing energy in a
  sector drives the field to an exceptional configuration and it unwinds; "if we could ensure that the angle between
  neighbouring spins was always acute, then unwinding could not occur, and topology would be restored", which he does
  with a bond energy f(θ) = −log(cos θ) (his Eq. 5, symbols restored from the extract; to verify) that becomes
  infinite at θ = π/2. This is in two space dimensions and is classical.
- [CIK15] constructs lattice analogues of the three-dimensional skyrmion for topological stability; its abstract and
  the searched text say nothing about spin, statistics or quantization.
- No source read here discusses the Finkelstein-Rubinstein sign or Witten's N_c phase on a lattice or a graph. Every
  derivation above (π₁(Q_B) = π₄(S³), the WZ term over M₅, its quantization) is stated for continuous fields on
  continuous space. The lattice route to fermions from bosons that the record has already read is a different one:
  string ends in Levin and Wen's rotor model ([LW06]; `2026-10-24_levin_wen_quantum_ether.md`).

## 4. Answers to the four questions, as the sources state them

(a) **What integer, and how defined.** The degree of the map from space (closed up into S³) to the target S³ ≅ SU(2):
B = (1/24π²) ∫ d³x ε^{ijk} tr(U†∂ᵢU U†∂ⱼU U†∂ₖU) ([SW99] Eq. 2.2), equivalently Skyrme's
N = −(1/2π²) ∫ det(φ, ∂ₓφ, ∂ᵧφ, ∂_zφ) d³x ([Ait20], quoting [Sky61]). It is identified with baryon number through the
gauged WZ term ([SW99] Sec. 3.1 (ii)).

(b) **When the spin is half-integer.** Two steps. (i) Topology *permits* it: π₁ of each sector is Z₂, and a 2π rotation
is the nontrivial loop exactly when B is odd ([Giu93]; [Kru03] Eqs. 2, 74–75); in the two-flavor model the sign is a
free choice for odd B ([Kru03] Sec. 1). (ii) The WZ term, whose coefficient must be a whole number n and equals N_c,
*fixes* the choice in the three-flavor model: a 2π rotation gives the phase e^{iπ N_c} for B = 1 ([Cat03]), so the
skyrmion is a fermion exactly when N_c is odd ([SW99] Sec. 4.1; [JM04]). The same constraint makes Y_R = N_c B/3.

(c) **Lattice or graph.** Not in the sources read. The results are continuum results; on a plain lattice the
topological integer itself is "essentially lost" and survives only if neighbouring field values are kept close
([War95]). No statement was found about the spin sign or the WZ phase on a lattice (searched only in [War95] and
[CIK15], so this is not a prior-work verdict).

(d) **Z₃ / triality.** Yes, in the three-flavor quantization: Y_R = N_c/3 "selects the representations of triality
zero" for N_c = 3 ([Pra92] Eq. 25); in [JM04] the allowed flavor tableaux have N_c + 3r boxes for F = 3, so (exact,
counting boxes mod 3) their triality is N_c mod 3. And the spin argument of [SW99] Sec. 4.1 runs through thirds:
Q_R takes values in steps of 1/3, Y_R/2 = 1/2 for N_c = 3, so J₃ must be half-integer.

## 5. What bears on the owner's rules

**What the sources say** (published, with the read status above):

1. The winding number itself is an ordinary whole number. The half comes from somewhere else: from the sign a
   wavefunction may pick up round a loop in the *space of all fields* (π₁(Q_B) = Z₂), not from the twist being a half.
2. In the plain two-flavor model that sign is optional for odd B and forbidden for even B. It becomes compulsory only
   with an extra ingredient, the WZ term, whose coefficient is quantized and equals the number of colors; the soliton
   is a fermion exactly when that number is odd.
3. The ingredient that forces the half is tied to a three-way structure: it exists only with three or more flavors,
   it sets a right hypercharge N_c B/3, and it selects flavor representations of triality N_c mod 3.
4. Everything is derived for continuous fields; on a lattice even the integer needs a special rule to survive.

**Ours, unverified** (interpretation for the owner; not checked by a physicist):

- The published answer to "how can a whole-number twist carry spin one half?" is: the twist does not carry it alone.
  The twist (B) decides whether a full turn is a nontrivial loop (B odd); a second, separately quantized number
  (N_c, through the WZ term) decides the sign that loop carries. A whole number times a whole number, read mod 2, gives
  the half. If the owner's rules want spin one half from a twist in steps of 1/3 (matter, triality) or 1/2 (dark), the
  nearest published analogue is that the phase of a full turn is e^{iπ·(twist count)·(a second integer)}, with the
  second integer playing the role of N_c. Whether her rules have such a second integer is hers to say.
- The thirds-and-halves bookkeeping of [SW99] Sec. 4.1 (a charge in steps of 1/3 plus Y_R/2 = 1/2 forcing J₃ to be a
  half) has the same shape as her "steps of 1/3 for matter, 1/2 for dark". That is a resemblance, not a derivation
  (rule 13): in [SW99] the 1/3 steps belong to flavor SU(3), not to a geometric twist on lattice diagonals.
- On her toy, which is a graph with labels, the 2026-10-24 note's finding stands: a finite set of labellings has no
  continuous loop, so neither the Finkelstein-Rubinstein sign nor the WZ phase can arise there by itself; each would
  have to be declared as a rule (a sign attached to a move sequence, as a framing sign is in [LW06]). The continuous
  "curl" (the U(1) link phases) is the one place a loop of fields could exist, and whether a full turn there is a
  nontrivial loop is an exact question that has not been asked.

## 6. What would change this reading

- Reading [Wit83a] Sec. on the SU(3) collective coordinates and [Wit83b] in full (library copy, or the reprints listed
  by INSPIRE: Shapere and Wilczek, *Geometric Phases in Physics*, pp. 369–379; Rebbi and Soliani, *Solitons and
  Particles*, pp. 617–628), to replace [Cat03]'s one-line summary of the e^{iπ N_c} phase with Witten's own derivation.
- Reading [FR68] itself, for its definition of exchange of kinks and whether it says anything about discrete systems.
- Reading [Sky61] for the exact normalization of N.
- A targeted search for fermionic quantization of solitons on a lattice or graph (none was done here beyond [War95]
  and [CIK15]); rule 15 applies before any sentence says it has not been done.

## 7. Proposed BibTeX entries (not added to `REFERENCES.bib`)

[FR68] and [Kru03] are already there. The others, as proposed; DOIs from INSPIRE or Crossref as marked in section 1.

```bibtex
@article{Sky61,
  author  = {Skyrme, T. H. R.},
  title   = {A non-linear field theory},
  journal = {Proceedings of the Royal Society of London. Series A},
  volume  = {260},
  number  = {1300},
  pages   = {127--138},
  year    = {1961},
  doi     = {10.1098/rspa.1961.0018},
  note    = {**Not read.** Its winding number N = -(1/2 pi^2) int det(phi, d_x phi, d_y phi, d_z phi) d^3x is quoted from [Ait20] p. 10: docs/reading/notes/2026-10-28_skyrmion_spin.md. Bibliographic data checked at Crossref 2026-10-27.}
}

@article{Sky62,
  author  = {Skyrme, T. H. R.},
  title   = {A unified field theory of mesons and baryons},
  journal = {Nuclear Physics},
  volume  = {31},
  pages   = {556--569},
  year    = {1962},
  doi     = {10.1016/0029-5582(62)90775-7},
  note    = {**Abstract only** (INSPIRE), plus [Ait20] p. 11: docs/reading/notes/2026-10-28_skyrmion_spin.md.}
}

@article{Wit83a,
  author  = {Witten, Edward},
  title   = {Global aspects of current algebra},
  journal = {Nuclear Physics B},
  volume  = {223},
  pages   = {422--432},
  year    = {1983},
  doi     = {10.1016/0550-3213(83)90063-9},
  note    = {**Abstract only** (INSPIRE). The Wess-Zumino term and the integer quantization of its coefficient (n = N_c) are described via [SW99] Sec. 3.1, Eq. 3.12: docs/reading/notes/2026-10-28_skyrmion_spin.md.}
}

@article{Wit83b,
  author  = {Witten, Edward},
  title   = {Current algebra, baryons, and quark confinement},
  journal = {Nuclear Physics B},
  volume  = {223},
  pages   = {433--444},
  year    = {1983},
  doi     = {10.1016/0550-3213(83)90064-0},
  note    = {**Abstract only** (INSPIRE). The skyrmion is a fermion exactly when N_c is odd, as stated by [SW99] Sec. 4.1, [Cat03] p. 2, [JM04], [Kru03] Sec. 1: docs/reading/notes/2026-10-28_skyrmion_spin.md.}
}

@incollection{SW99,
  author  = {Schechter, J. and Weigel, H.},
  title   = {The Skyrme model for baryons},
  pages   = {337--369},
  year    = {1999},
  eprint  = {hep-ph/9907554},
  note    = {Book title, editors and publisher to verify (INSPIRE parent record 542037). **Read in part by an assistant agent, 2026-10-27** (Secs. 2 opening, 3.1, 4.1; Eqs. 2.2, 3.12, 4.7-4.11): docs/reading/notes/2026-10-28_skyrmion_spin.md.}
}

@misc{Ait20,
  author  = {Aitchison, Ian J. R.},
  title   = {Tony Skyrme and the origins of Skyrmions},
  year    = {2020},
  eprint  = {2001.09944},
  note    = {Journal publication to verify. **Read in part by an assistant agent, 2026-10-27** (pp. 1-11): docs/reading/notes/2026-10-28_skyrmion_spin.md.}
}

@article{Giu93,
  author  = {Giulini, Domenico},
  title   = {On the possibility of spinorial quantization in the Skyrme model},
  journal = {Modern Physics Letters A},
  volume  = {8},
  pages   = {1917--1924},
  year    = {1993},
  doi     = {10.1142/S0217732393001641},
  eprint  = {hep-th/9301101},
  note    = {**Read in part by an assistant agent, 2026-10-27** (abstract, introduction): docs/reading/notes/2026-10-28_skyrmion_spin.md. 2 pi rotations are non-contractible loops exactly in the odd-winding-number sectors.}
}

@misc{Cat03,
  author  = {Catto, Sultan},
  title   = {Effective hadronic Lagrangians based on {QCD}: potential models and Skyrmions},
  year    = {2003},
  eprint  = {hep-th/0302101},
  note    = {Journal publication to verify. **Read in part by an assistant agent, 2026-10-27** (p. 2 only): docs/reading/notes/2026-10-28_skyrmion_spin.md.}
}

@article{JM04,
  author  = {Jenkins, Elizabeth and Manohar, Aneesh V.},
  title   = {The chiral soliton model for arbitrary colors and flavors},
  journal = {Physical Review D},
  volume  = {70},
  pages   = {034023},
  year    = {2004},
  doi     = {10.1103/PhysRevD.70.034023},
  eprint  = {hep-ph/0402150},
  note    = {**Read in part by an assistant agent, 2026-10-27** (hypercharge constraint, Eqs. 4-7): docs/reading/notes/2026-10-28_skyrmion_spin.md.}
}

@inproceedings{Pra92,
  author    = {Praszalowicz, M.},
  title     = {Strangeness in Skyrme and in Nambu-Jona-Lasinio models},
  booktitle = {Siegen Baryons Workshop 1992},
  pages     = {43--56},
  year      = {1992},
  eprint    = {hep-ph/9211278},
  note      = {**Read in part by an assistant agent, 2026-10-27** (Sec. 3, Eqs. 24-26): docs/reading/notes/2026-10-28_skyrmion_spin.md. Y_R = N_c/3 selects representations of triality zero.}
}

@article{War95,
  author  = {Ward, R. S.},
  title   = {Stable topological Skyrmions on the {2D} lattice},
  journal = {Letters in Mathematical Physics},
  volume  = {35},
  pages   = {385--393},
  year    = {1995},
  doi     = {10.1007/BF00750845},
  eprint  = {hep-th/9502048},
  note    = {**Read in part by an assistant agent, 2026-10-27** (abstract, Secs. 1-2 to Eq. 5): docs/reading/notes/2026-10-28_skyrmion_spin.md.}
}

@article{CIK15,
  author  = {Charalampidis, E. G. and Ioannidou, T. A. and Kevrekidis, P. G.},
  title   = {Lattice three-dimensional skyrmions revisited},
  journal = {Physica Scripta},
  volume  = {90},
  number  = {2},
  pages   = {025202},
  year    = {2015},
  doi     = {10.1088/0031-8949/90/2/025202},
  eprint  = {1411.1313},
  note    = {**Abstract and Sec. 1 opening only** (assistant agent, 2026-10-27): docs/reading/notes/2026-10-28_skyrmion_spin.md.}
}
```

When `REFERENCES.bib` is next edited, [FR68]'s note can add "abstract read (INSPIRE), 2026-10-27".

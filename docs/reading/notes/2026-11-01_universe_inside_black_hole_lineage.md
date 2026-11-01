# Reading: the "universe inside a black hole" lineage, as a benchmark for piece 11

*Date of the reading: 2026-11-01. Who read: an assistant agent (Claude Fable 5.1), on the instruction of TASKS.md ("The
reviews of 6 October", item 6: read Pathria, Poplawski and the lineage before any citation). The owner has not read these
passages. Everything below marked "published" is quoted or closely paraphrased from the papers' own text as fetched from
arXiv (abstract pages and the ar5iv HTML renderings; one PDF extracted with PyMuPDF); everything marked "ours" is the
agent's and is unverified. Rule 13 applies throughout: these papers are targets a black-hole-birth picture must reproduce
or answer, never evidence that the owner's picture does. Quotations from HTML-to-text conversions are to be checked against
the PDFs before any of them appears in a paper.*

## Read status, paper by paper

Verified against the sources by a second agent on 2026-11-01; its corrections applied the same day.

| Key (proposed for REFERENCES.bib) | Paper | How read |
|---|---|---|
| [Pathria72] | R. K. Pathria, "The Universe as a Black Hole", Nature 240, 298-299 (1972), DOI 10.1038/240298a0 | **Not read.** Nature's page and PDF redirect to a login (paywalled). Known here only through [Khakshournia14] (read in full, 5 pages) and Berman, arXiv:physics/0612007 (abstract and Sec. I only). Owed: the two-page original, from a library. |
| [Khakshournia14] | S. Khakshournia, "A note on Pathria's model of the universe as a black hole", arXiv:1412.0105 | Read in full from ar5iv. |
| [FMM89] | V. P. Frolov, M. A. Markov, V. F. Mukhanov, "Through a black hole into a new universe?", Phys. Lett. B 216, 272-276 (1989) | **Not read**; INSPIRE abstract summary only. |
| [FMM90] | V. P. Frolov, M. A. Markov, V. F. Mukhanov, "Black holes as possible sources of closed and semiclosed worlds", Phys. Rev. D 41, 383-394 (1990), DOI 10.1103/PhysRevD.41.383 | **Not read**; APS page returns 403; the INSPIRE record (267342, 345 citations; not re-verified by the second agent: INSPIRE was unreachable; stands as read by the first agent) gives the abstract, read sentence by sentence. The model's content is taken from [BF95], which generalizes it and restates it. **Note on the date:** VISION line 2870 cites them as 1989 without naming the journal; ASSUMPTIONS O159 already gives both years. The Phys. Rev. D paper is 1990 (volume 41, 383-394); the 1989 paper is the Physics Letters one. Both should be cited with their own year. |
| [BF95] | C. Barrabes and V. P. Frolov, "How many new worlds are inside a black hole?", arXiv:hep-th/9511136 (Phys. Rev. D 53, 3215 (1996), from the arXiv journal-ref field) | Read in full from the PDF (text extracted with PyMuPDF), Secs. 1, 2.1, 2.3, 5 closely; Secs. 3 and 4 (shell intersections) skimmed. |
| [Pop10a] | N. J. Poplawski, "Radial motion into an Einstein-Rosen bridge", Phys. Lett. B 687, 110-113 (2010), arXiv:0902.1994 | Read in full from ar5iv (Secs. I to IV, Eqs. 1 to 25). |
| [Pop10b] | N. J. Poplawski, "Cosmology with torsion: An alternative to cosmic inflation", Phys. Lett. B 694, 181-185 (2010); Erratum B 701, 672 (2011), arXiv:1007.0587 | Read in full from ar5iv (Secs. I to VII, Eqs. 1 to 29). |
| [Pop11] | N. J. Poplawski, "Matter-antimatter asymmetry and dark matter from torsion", Phys. Rev. D 83, 084033 (2011), arXiv:1101.4012 | Read in part from ar5iv: abstract, introduction, the mechanism (Eqs. 2, 13 to 15), the numbers (Eqs. 18, 19), discussion. |
| [Pop12] | N. Poplawski, "Nonsingular, big-bounce cosmology from spinor-torsion coupling", Phys. Rev. D 85, 107502 (2012), arXiv:1111.4595 | Read in full from ar5iv (unnumbered sections, Eqs. 1 to 32). |
| [Pop16] | N. Poplawski, "Universe in a black hole in Einstein-Cartan gravity", Astrophys. J. 832, 96 (2016), arXiv:1410.3881 | Read in part from ar5iv (v1 text): Secs. I, V, VI, VII, VIII closely; Secs. II to IV (field equations) skimmed. The arXiv abstract page now shows a v2 dated 26 May 2026 whose abstract is worded more cautiously than the v1 text ar5iv renders (see below). |
| [Pop21] | N. Poplawski, "Gravitational collapse of a fluid with torsion into a universe in a black hole", JETP 132, 374 (2021), arXiv:2008.02136 | Abstract only. |
| [Pop23] | N. Poplawski, "Gravitational collapse with torsion and universe in a black hole", in *Regular Black Holes*, C. Bambi (ed.), Springer 2023, p. 485, arXiv:2307.12190 (arXiv notes substantial overlap with 2008.02136) | Read in full from ar5iv (Secs. I to VIII). Used as his 2020-2026 review. |
| [Smolin06] | already in REFERENCES.bib, read 2026-09-23 | Not re-read; one paragraph below from the existing note. |

Searched for and not found (arXiv listing for author Poplawski, N., years 2020 to 2023, searched 2026-11-01): a 2021 or
2022 arXiv review by Poplawski of the whole picture (the 2021 JETP paper and
conference slides at MG16 2021 and HEPMAD 2024 exist; the slides were not read). Not read: Easson and Brandenberger
(2001), Stuckey (1994), Smoller and Temple (2003), Morgan (1991), Markov's original limiting-curvature papers, Knutsen's
critique of Pathria; all cited by the papers above and listed here only so that nobody cites them from this note.

## 1. Pathria (1972): a closed Friedmann universe as the inside of a Schwarzschild black hole

**Mechanism replacing the singularity: none.** Pathria's model is a matching of two classical solutions, not a bounce.
[Khakshournia14], paraphrasing him: "a pressureless closed Friedmann-Robertson-Walker (FRW) universe can lie
inside a Schwarzschild black hole" that exists "in a bigger universe" (Sec. 1); the event horizon of that black hole "is
identified with the radius of the universe at the point of its maximum expansion" (abstract), and Pathria took the identity R_max = R_s to be
"fundamental to the structure of the universe", "meaning that the universe is indeed inside a black hole". The matching
holds "for the certain values of the cosmological constant" (abstract). Berman (physics/0612007, Sec. I and conclusions)
confirms the two assumptions, p = 0 and a condition on Lambda, and adds nothing on the parent.

**Causal connection, matter, observables:** not discussed in anything we could read. *Ours, unverified:* a closed FRW
interior glued at its maximum radius to a Schwarzschild exterior has no bounce and no birth event; the daughter is simply
assumed to exist, and the parent's matter is the daughter's matter by construction (the FRW dust *is* the hole's mass).

**Its standing.** [Khakshournia14] shows the matching is not smooth: the horizon "is the history of a null shell admitting
a surface pressure" (abstract; the pressure p = rho a / 4 after its Eq. 17), and its "Note added in the published version" records Knutsen's
view that "Pathria's idea of the Universe as a black hole is untenable" with a timelike matching, reconciled by moving the
matching surface to the null horizon. So the lineage's first paper is a kinematic identity with a known defect, not a
mechanism. For piece 11 it fixes one benchmark number: a closed universe of mass M sitting inside a horizon has
R_max = 2GM/c^2.

## 2. Frolov, Markov and Mukhanov (1989, 1990): limiting curvature, a de Sitter core, a closed or semiclosed world

**Mechanism: a limiting curvature.** The INSPIRE abstract of [FMM90], sentence by sentence (paraphrase; short exact
phrases in quotes; not re-verified by the second agent: INSPIRE was unreachable; stands as read by the first agent): the interior of a black hole is studied assuming a "limiting curvature" exists; the Schwarzschild
interior can be joined to a de Sitter geometry across a "spacelike junction surface" acting as a thin transition layer;
Israel's thin-shell formalism gives the layer's properties; "instead of the singularity the closed world can be formed
inside the black hole"; this is expected to hold more generally if gravity is asymptotically free and a limiting curvature
exists; after a deflationary phase the closed world "may start to expand and become a new large-scale universe"; the
model is offered as a laboratory-style example of "creating a closed or semiclosed world"; the fate of an evaporating black
hole is briefly considered.

[BF95], Sec. 1, restates it: "inside a black hole there exists a closed Universe instead of a singularity. The metric is
obtained by gluing the Schwarzschild metric to the de Sitter metric through a surface r = r0 = const located inside the
black hole. The parameter r0 is chosen in such a way that the value of a curvature calculated at r0 coincides with a
limiting curvature, which is assumed to be of Planckian order ... the transition region required for change of the regimes
is approximated by a thin spacelike shell. In the FMM-model the spacetime passes through the deflation stage and instead
of the singularity a new inflating Universe is created." Sec. 2.1: r0 = (12)^(1/6) (r+/l_Pl)^(1/3) l_Pl, and "the change to
a new phase occurs everywhere simultaneously (at the spacelike surface r = r0 ~ (r+ l^2)^(1/3))". The limiting-curvature
principle itself is Markov's (BF95 refs. [1, 2]) and is a hypothesis about the unknown complete theory: "We cannot hope to
derive this result without knowledge of the theory, but we may at least discuss and classify possibilities. Such a
'zoological' approach is a natural first step" (Sec. 1).

**Causally disconnected?** The abstract's own word is "closed or semiclosed". *Ours, from general knowledge, to verify
against [FMM90] itself:* in Markov's usage a semiclosed world is a closed Friedmann world joined to the outer space through
a narrow throat, so "semiclosed" is the case where a thin connection to the parent survives; "closed" is the fully
disconnected case. [BF95] (Sec. 5) makes disconnection explicit for its own generalization: bubbles of the new phase
nucleating independently "might result in the formation of disconnected worlds", two bubbles separated by more than l_max
"remain completely disconnected" (Sec. 3.1), and the shells that were "initially attached through the timelike shell become
disconnected after the time interval T_sep". Neither paper says the daughter can signal the parent.

**The parent's matter.** Not discussed as inheritance. What the daughter is made of is the de Sitter phase (vacuum energy
at the limiting curvature), not the collapsed star. [BF95], Sec. 5, counts something else: as many as
N_max ~ (l_Pl/a)^2 (m/mu_Pl)^4 disconnected daughter worlds could form during the parent's evaporation (Eq. 34), a count
the paper says is much larger than the dimensionless Bekenstein-Hawking entropy S_BH of the black hole or the number of
emitted Hawking quanta N ~ (m/mu_Pl)^2, two quantities it describes as being of the same order of magnitude (paraphrase of
Sec. 5), and uses the count to argue (Eqs. 35, 36) that "the internal state of each newly
created universe is pure while the ensemble of universes is described by a density matrix", an application to the
information-loss puzzle.

**Observables claimed:** none for the parent's outside; the daughter is invisible by construction. The one testable-in-
principle statement is the count of worlds and its bearing on information loss, which is a consistency argument, not a
measurement.

## 3. Poplawski (2009-2023): torsion instead of a singularity, every black hole a daughter universe

### 3.1 The 2010 wormhole paper [Pop10a]

Classical general relativity only; no torsion yet. The abstract: an Einstein-Rosen bridge's interior "is regular and
physically equivalent to the asymptotically flat exterior of a white hole"; "Einstein-Rosen and Schwarzschild black holes
are different, physical realizations of general relativity. Yet for distant observers, both solutions are
indistinguishable"; so observed black holes may be Einstein-Rosen bridges, "each with a new universe inside that formed
simultaneously with the black hole. Accordingly, our own Universe may be the interior of a black hole existing inside
another universe." The argument for geodesic completeness is a discontinuity of the expansion scalar at the horizon
(Eq. 15) and Rindler's elliptic identification in the Kruskal diagram (Sec. III, text after Fig. 2). **One-way:** "The particle enters
region III (with no possibility of coming back to region I)" (Sec. III). **Observables:** none; the interior's nature
"cannot be satisfactorily determined, unless an observer enters or resides in the interior region" (Sec. IV). **Matter:**
the infalling particle continues into the interior with proper time extending to infinity; emerging matter is "an exploding
white hole" (Sec. IV).

### 3.2 The torsion bounce [Pop10b], [Pop12]

**Mechanism: torsion coupled to spin.** In Einstein-Cartan-Sciama-Kibble gravity the spin of fermions sources torsion,
and averaging the spin into a Weyssenhoff spin fluid gives an effective energy density eps - kappa s^2/4 ([Pop10b] Eqs. 8,
10) whose torsion part scales as a^(-6) (Eq. 15) against radiation's a^(-4) (Eq. 14 with w = 1/3; the total is Eq. 16), so it dominates at small a and is
repulsive: |H| = H0 (Omega_R a^-4 + Omega_S a^-6)^(1/2) (Eq. 21) with Omega_S = -8.6 x 10^-70 (Eq. 23), a minimum scale
factor a_m = (-Omega_S/Omega_R)^(1/2) = 3.1 x 10^-33 of today's, about 9 x 10^-6 m (Eq. 24): "the expansion of the Universe
started when H = 0". [Pop12] redoes it with Dirac spinors instead of a spin fluid: the minimal coupling gives a spin-spin
term that acts "like a perfect fluid with a negative energy density" (Eqs. 9, 10), and "such an interaction averts the
unphysical big-bang singularity, replacing it with a cusp-like bounce at a finite minimum scale factor, before which the
Universe was contracting" (abstract; Eqs. 16, 17; "The bouncing point, where the scale factor has its minimal value, is a
cusp").

**Observables claimed (these are the ones the lineage actually puts numbers on):**
- Flatness without inflation: Omega at sqrt 2 times the minimum scale factor is 1 + 8.9 × 10⁻⁶⁴ ([Pop10b] Eq. 26; Omega
  itself diverges at the bounce), and at the bounce 1 + 1.3 x 10^-70 ([Pop12] Eq. 31); "the apparent fine tuning of Omega in the very early Universe is naturally caused by the extremely small and
  negative torsion density parameter" ([Pop10b] Sec. V).
- Horizon problem without inflation: the antipodal velocity peaks at about 1.1 x 10^32 c ([Pop10b] Eq. 29), so one
  causally connected region becomes about 10^96 causally disconnected volumes (Sec. VI); [Pop12] likewise, N ~ v_ant^3.
  The total expansion attributed to the bounce is a factor of about sqrt 2, against 10^26 for standard inflation
  ([Pop10b] Sec. V), which is why he calls it an alternative and not a variant.
- A preferred direction: "A universe born from a rotating black hole should inherit its preferred direction, related to
  the axis of rotation", with "small corrections to the FLRW metric" ([Pop10b] Sec. VII). Not developed quantitatively.
- The arrow of time: "the time asymmetry of motion at the boundary of this black hole may cause the perceived arrow of
  cosmic time" ([Pop10b] Sec. VII); [Pop16] Sec. VI: "The motion of matter through the event horizon is unidirectional".
- Laboratory tests of torsion: whether torsion couples to spin "should be tested experimentally"; if it couples to orbital
  angular momentum it would affect "the precession of gyroscopes without spin polarization" (Gravity Probe B is cited);
  a Kerr-radius bound a = M/(mc) checked against GRS 1915+105 ([Pop10b] Sec. VII).
- Parity: not addressed in [Pop10b], [Pop12] or [Pop16]. The spin pseudovector appears in the equations and no parity
  conclusion is drawn. The owner's expectation that Poplawski claims parity is not borne out by these papers; what he
  claims is a charge-conjugation asymmetry (next item).

### 3.3 Matter against antimatter [Pop11]

The one paper of his that bears on the owner's twins. Mechanism: torsion adds the cubic Hehl-Datta term to the Dirac
equation (Eq. 2); under charge conjugation that term flips sign relative to the mass term (Eq. 13), so "A classical Dirac
spinor and its charge conjugate therefore satisfy different field equations", and "Fermions in the presence of torsion have
higher energy levels than antifermions, which leads to their decay asymmetry" (abstract; Eqs. 14, 15). Heavy
baryon-carrying fermions ("archaeons", mass 14.4 TeV (Eq. 19), which he quotes as about 10 TeV; freeze-out near 10^13 GeV, Eq. 18) decay mostly to
nucleons while their antiparticles decay mostly to a hidden antimatter: "Accordingly, dark matter is in fact hidden
antimatter" (introduction), and "The conserved total baryon number of the Universe remained zero" (abstract). The effect
matters only "at extremely high densities that existed in the very early Universe or exist inside black holes"
(introduction). [Pop16] Sec. VIII and [Pop23] Sec. VIII list the asymmetry as an open problem torsion "may also explain",
with no calculation.

### 3.4 The full picture [Pop16], [Pop23]

**Every black hole a universe.** [Pop16] v1 text (ar5iv), abstract: "every black hole in the presence of torsion forms a
nonsingular, closed, nearly flat" homogeneous and isotropic universe beyond its event horizon; Sec. I: "Every astrophysical
black hole may thus be an Einstein-Rosen bridge (wormhole) to a new universe"; "Accordingly, our Universe may be the
interior of a black hole existing in another universe and a part of a multiverse"; Sec. VIII: "Our Universe is a stable
part of the multiverse" that "may contain inflating regions of spacetime (new universes) only in black holes". **Caution
on versions:** the arXiv abstract page now shows a v2 (26 May 2026, "published version") whose abstract says only that a
collapsing black hole's matter "may be regarded as" a nonsingular closed universe, does not say "every", does not say
"nearly flat", and does not say our Universe originated inside a black hole. The strong sentences above are from the v1
rendering; a paper that quotes them must say which version, and the ApJ text is to be checked.

**Mechanism inside the hole.** [Pop23] (Tolman metric, collapsing homogeneous spin-fluid sphere, Secs. III to VI):
"gravitational repulsion of torsion prevents a singularity, replacing it with a nonsingular bounce" (abstract); "the spin
fluid on the other side of the event horizon must expand as a new, growing universe with a closed geometry" (Sec. VI).
[Pop16] Sec. I: "The universe in a black hole contracts until it reaches a minimum radius and maximum density", then
expands. Without particle production the daughter is "oscillatory with an infinite number of bounces and crunches"
([Pop16] Sec. VII; [Pop23] Sec. VI: "each cycle is alike"). With particle production in the bounce's extreme curvature
(Eqs. 40 to 50 of [Pop16]) each cycle is larger: "Particle production increases the maximum size of the scale factor that is
reached at a crunch" ([Pop23] Sec. VII); "After a finite series of cycles" it expands indefinitely ([Pop23] Sec. VIII), and
the last bounce is the big bang, in each source's own words: "The last bounce, referred to as the big bounce, is the big
bang" ([Pop23] Sec. VIII); after "several nonsingular bounces" the last one "can be regarded as the big bang" ([Pop16]
abstract, v2 wording), with a cosmological constant needed "for a closed universe to expand to infinity" ([Pop23]
Sec. VIII). Inflation is a special case (exponential expansion at nearly constant temperature, [Pop16] Sec. VII, Eqs. 52 to
56), so he claims inflation and reheating "without a scalar field" ([Pop16] abstract; Sec. VIII: "without requiring finely
tuned scalar fields").

**Causally disconnected?** The daughter "cannot be observed outside the black hole because of the infinite redshift at the
horizon" ([Pop23] Sec. I; [Pop16] Sec. I: "Such an expansion is not visible from the outside"); matter cannot return
"because of the unidirectionality of the motion of matter through a horizon" ([Pop23] Sec. VI); yet topologically "the
boundary of the black hole becomes an Einstein-Rosen bridge connecting this universe with the outer universe" ([Pop10b]
Sec. VII), and the daughter "is thus a separate spacetime branch with its own timeline" (same section). So: one-way,
connected by a bridge, unobservable from the parent. [Pop16] Sec. V notes the daughter's own interior "is causally
connected" (it is one Friedmann patch at the bounce), which is how the horizon problem is met.

**The parent's matter.** The daughter starts as the collapsed star's spin fluid, with mass M_BH = c^2 a_i/(2G) ([Pop16]
Eq. 17), but most of what it ends up holding is made, not inherited: "Extremely large tidal forces cause an intense pair
production which generates the observed amount of mass" ([Pop10b] Sec. VII); "an intense particle production which creates
an enormous amount of mass inside the black hole ... without changing the total energy (matter plus gravitational field) of
the new universe" ([Pop16] Sec. I); the growth factor from production exceeds 10^10 (Eq. 38). The daughter's total energy
is zero ([Pop23] Sec. I: "whose total energy is zero"). None of the papers says how much of the parent's specific particle
content survives the bounce or whether the daughter's matter-antimatter balance is the parent's.

**Numbers he states for the bounce** ([Pop16] Eq. 29 and nearby): T_max = 1.15 x 10^32 K, tau = 4.75 x 10^-45 s,
N_max ~ 10^52 (the quantity N_max there is his, not [BF95]'s count of worlds: in [Pop16] Sec. V it is the maximum number of
causally disconnected regions in the closed universe, about (a_i/l_P)^3).

**What he himself lists as missing** ([Pop16] Sec. VIII): "we need to derive primordial density fluctuations generated in
the early universe formed in a black hole"; the asymmetry "may be caused by the nonlinearity of the Dirac equation in the
presence of torsion"; and "The presented theory predicts phenomena that are similar to those in some other cosmological
scenarios", which is his own admission that the observables are not yet discriminating. [Pop23] Sec. VIII adds that the
picture "is consistent with the Planck observations" of the CMB and that torsion "could explain the cosmological constant".

## 4. Smolin: the selection-side relative (one paragraph, from [Smolin06] as already read on 2026-09-23)

Cosmological natural selection takes the bounce for granted (black-hole singularities bounce into new expanding universes)
and adds heredity with variation: each birth shifts the low-energy parameters by a small random step, so the fitness of a
parameter set is the number of black holes a universe with it makes, and the master prediction is that almost no small
change of our parameters increases that number; three published predictions follow (a neutron-star mass limit near 1.6
solar masses, single-parameter inflation, little early massive-star formation), the first of which 2-solar-mass neutron
stars count against (general knowledge, to verify). It is the only paper in this lineage with a falsifiable prediction
about *our* universe; the others predict things about the daughter. Its relation to the owner's picture is recorded in
`docs/parked/extension_2026-09-22.md` and VISION Updates 33 and 43: she selects for observers over a loop's turn, not for
black holes.

## 5. What the owner's picture shares and where it differs (ours, unverified)

Her picture, from VISION Updates 42 and 149: X inside a black hole is a curled slab, two directions curled and one open,
made of tightly stacked one-sided dark-matter loops of one handedness; surplus dark matter is crushed into a shell round a
zero-dimensional space at the slab's center, the rod; photons apply curl energy to the slab until a big bang fires at one
pole of the rod; matter breaches first and a new three-dimensional spacetime is born, then a twin from the surplus
antimatter; the surplus is returned to the hole for later burps.

**Shared with the lineage.**
- The black hole's interior is where the next universe is made, and the singularity is replaced by a specific state
  (theirs: a de Sitter core or a torsion bounce; hers: the curled slab, a stuck arrangement with a wall). Both are
  "limiting" states that stop the collapse short of a point; Markov's limiting curvature and her "no space, nothing can
  move" are the same move made with different machinery.
- The daughter is one-way from the parent and invisible from outside (Poplawski's infinite redshift; FMM's closed or
  semiclosed world). Her zero-dimensional space enclosed by the shell is of the same kind. The toy has no horizon and
  cannot test this; it is an assumption on both sides.
- The daughter's matter is mostly made at the birth, not carried in (Poplawski's pair production; FMM's de Sitter
  phase). Her burp is the same claim: the release at the pole, not the parent's star, is what the new space holds. The
  toy measures the release per point exactly (4(lambda - 1), or 3a under her tie) and that is the one number in this
  programme that could be set beside Poplawski's "enormous amount of mass ... without changing the total energy", if a
  conversion between the toy's units and energy existed (it does not; VISION "What no outcome can show").
- Repeated births from one hole: Poplawski's several bounces, each larger; her twins and the gap before the next set.
  Different in kind: his repeats are oscillations of one daughter; hers are separate daughters from one parent, which is
  closer to [BF95]'s many disconnected worlds per hole than to Poplawski.
- A matter-antimatter asymmetry made at the birth from the geometry's own handedness: Poplawski's charge-conjugation
  asymmetry from torsion ([Pop11]); her one-handed stack breaching matter first, then antimatter. Hers separates the two
  into twin universes (which escapes the gamma-ray bound on antimatter domains inside one universe, VISION 3745 ff.); his
  keeps them in one universe with the antimatter hidden as dark matter. Both keep total baryon number zero.

**Where hers differs.**
- One daughter against twins. Every paper read gives one daughter per bounce; [BF95] gives many but by independent
  nucleation, not by handedness. "Twins, matter then antimatter" is hers alone as far as we have read.
- A preferred point of birth. Poplawski's bounce is homogeneous (the whole Friedmann patch bounces); FMM's transition is
  "everywhere simultaneously"; [BF95]'s bubbles nucleate anywhere. Her big bang fires at one pole of a rod. T88 read this
  as a testable prediction in the toy (ONE FRONT at the fed end, Update 150), and it is the one place where the owner's
  picture makes a claim none of these papers makes.
- Dark matter as the building material of X. In Poplawski dark matter is a product (hidden antimatter); in hers it is the
  substrate the slab is stacked from. No paper read treats the collapsed state as made of dark matter.
- The surplus returned to the hole. In Poplawski the daughter keeps everything (zero total energy, nothing comes back);
  FMM say nothing. Her return of the surplus for later burps has no relative here.
- What stops the collapse. Theirs is a term in the gravitational field equations (torsion, limiting curvature); hers is
  the wall of a discrete arrangement, with no continuum field at all. Rule 13's demand is therefore sharper for her: the
  toy must show the stuck state, its wall and its release before anything is compared to a bounce.
- Observables. Poplawski's claimed consequences (flatness to 10^-64, 10^96 causally disconnected volumes, a preferred
  axis from the parent's spin, the arrow of time from the horizon, 10 TeV archaeons) are all statements about the
  daughter's interior as seen by its own inhabitants. Her picture would have to produce its own versions of these; the
  toy supplies none of them today.

## 6. Benchmarks, never evidence (rule 13)

What any black-hole-birth picture, hers included, must reproduce or answer, as these papers already state it:

1. **A state that replaces the singularity, with its scale fixed by something.** FMM: a Planckian limiting curvature,
   r0 ~ (r+ l_Pl^2)^(1/3). Poplawski: a minimum scale factor a_m = 3.1 x 10^-33 (about 9 x 10^-6 m) set by Omega_S. Hers:
   the curled slab's size, which the toy would have to fix from the wall and the tie, not assume.
2. **The horizon as a one-way door and the daughter's invisibility**, so that no observable from inside the parent can
   confirm the daughter. Every paper here says the daughter cannot be seen from the parent; a picture that claims
   otherwise has to say what gets out.
3. **Where the daughter's matter comes from and that the books balance.** Poplawski: zero total energy, pair production
   growing the contents by more than 10^10 without changing the total. Hers: the burp's release, the twins' split and the
   returned surplus must add up, with the conserved quantity of claim 6 named.
4. **Flatness, homogeneity and isotropy of the daughter without an inflaton**, or with one. Poplawski's numbers:
   Omega - 1 of order 10^-64 at sqrt 2 times the minimum scale factor ([Pop10b]) and 10^-70 at the bounce ([Pop12]); about 10^96 causally disconnected volumes from one connected patch.
   A birth that opens from one pole and spreads as a front (hers) has to say how the far side of the daughter comes to
   look like the near side.
5. **Repeated births**: how many per parent (one, several in sequence, or [BF95]'s N_max ~ (m/mu_Pl)^4), and what sets the
   gap between them. Hers: "a gap, then another set of twins when there are enough curls again" is a rate claim the toy
   could price (energy per burp against inflow).
6. **The matter-antimatter balance of the daughter**, with total baryon number zero across everything made ([Pop11]).
   Hers: twins must hold equal and opposite excesses, and the breach order (matter first) must come from the stack's
   handedness, not be chosen.
7. **An arrow of time and, for a spinning parent, a preferred axis** inherited by the daughter ([Pop10b] Sec. VII).
   Hers: the rod has an axis and a pole already; what the daughter inherits from them is a prediction she could state.
8. **The information question**: whether the parent's information goes into the daughter ([Pop23] Sec. VIII: "the
   information about the initial state of a collapsing matter is not lost"; [BF95] Eqs. 35, 36). Hers has not been asked.
9. **The classical check, as the 6 October review asked (O103 (j))**: any re-curled region the toy produces is to be set
   beside Schwarzschild or a closed-FLRW black-hole cosmology, with R_max = 2GM/c^2 (Pathria) as the plainest number.
10. **A mechanism in the gravitational theory or an admission that there is none yet.** FMM: "We cannot hope to derive
    this result without knowledge of the theory". Poplawski: torsion, with laboratory tests named. Hers: the toy's wall is
    a fact of the toy's energy, and the step from it to a statement about real black holes is not made anywhere in the
    record; the pages must keep saying so.

## 7. What this reading changes in the record (proposed, not enacted)

- REFERENCES.bib: add the keys in the table above with the read statuses given, with Frolov, Markov and Mukhanov as two
  entries, the 1989 Physics Letters B paper and the 1990 Physical Review D paper, each with its own year. VISION line 2870
  cites them as 1989 without naming the journal; ASSUMPTIONS O159 already gives both years.
- VISION line 3749 says Poplawski's asymmetry is "from torsion (2011)": confirmed, it is [Pop11], and the mechanism is a
  charge-conjugation asymmetry of the Hehl-Datta term, not parity.
- TASKS "The reviews of 6 October" item 6: Pathria and Poplawski read as far as reachable (Pathria's original still
  owed from a library); the Fife reference is still to be obtained from the owner.
- Nothing here is evidence for piece 11. Before any sentence in a paper compares her picture to these, the checks of
  rule 13 and the staged targets of piece 11 (a stable localized curled region inside open space; a reproducible
  threshold; growth with stored energy; trapping or an analogue; a sensible large-scale limit) come first.

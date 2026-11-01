# Reading note: units for the toy. Can a sweep be a second and a link a meter?

**Date:** 2026-11-01. **Who read:** an assistant agent (Claude Fable 5.1), from the arXiv texts (fetched and searched,
not summarized). **The owner has not read these passages.** Everything below is a quotation with its location, or is
marked ours. Quotations come from the arXiv HTML conversions, which flatten fractions and sometimes garble equation
numbers; check against the PDFs before quoting any of them further.

**The question it answers** (the owner, 2026-11-01): "can we write a translation between our sweep clock and the
meters per second or whatever is a good unit for spacetime?"

**The short answer** (ours, unverified; the long answer is sections 5 and 6): yes, a table can be written, and every
row with a physical unit in it is an *identification* chosen by us, not a derivation from the toy. Two of the
identifications (one link is one Planck length; the lattice step of light is one Planck time, so c = 1 link per step)
are the conventional ones in the neighboring programmes and are therefore a convention and not a fit. The published
model itself [T25] says the model has exactly two fundamental units, a link length and a rate of elementary moves, and
leaves both unfixed; its one bridge to a mass, Eq. (45), carries an unspecified factor n(g). Nothing in the toy's
measurements fixes either unit, and nothing the toy can measure changes if both are rescaled together.

## 1. Sources and how far each was read

| Key | Paper | arXiv | Read for this note |
|---|---|---|---|
| [T25] | Trugenberger, "Networks as the fundamental constituents of the universe" (titled "Combinatorial quantum gravity" in the task) | 2512.17676v2 | Sec. I, IV.1, V, V.1, VI.1 searched in the HTML; the last 20,000 characters (Sec. VI.3 to end) searched for units only. Read in full by the project on 2026-09-19 (REFERENCES.bib). |
| [KTB19] | Kelly, Trugenberger, Biancalana, "Self-assembly of geometric space from random graphs" | 1901.09870v2 | Sec. 1, 3.1.1, 3.1.2 searched in the HTML (first 100,000 of 167,606 characters); read in full by the project on 2026-09-19. |
| [T22] | Trugenberger, "Emergent time, cosmological constant and boundary dimension at infinity in combinatorial quantum gravity" | 2112.03778v2 | Abstract, Sec. I, III, IV, V, VII searched in the HTML; read in full by the project on 2026-09-19. |
| AGJL12 (added to REFERENCES.bib 2026-11-01) | Ambjorn, Goerlich, Jurkiewicz, Loll, "Nonperturbative quantum gravity" (Physics Reports review) | 1203.3591v1 | Sec. 1 to 2.8 and 4 to 7.2 searched in the HTML; Sec. 11, where the Planck-unit size is determined, is beyond the 100,000 characters fetched; **not read**. |
| AGJL08 (added to REFERENCES.bib 2026-11-01) | Ambjorn, Goerlich, Jurkiewicz, Loll, "The nonperturbative quantum de Sitter universe" | 0807.4481v2 | Sec. 3, 7 and 8 searched in the ar5iv HTML; this is where the lattice spacing in Planck lengths is actually computed. |
| [Loll19] | Loll, "Quantum gravity from causal dynamical triangulations: a review" | 1905.08669 | Sec. 2 to 5 searched in the HTML (first 100,000 of 190,287 characters); REFERENCES.bib marks it NOT READ before today. |
| Surya19 (added to REFERENCES.bib 2026-11-01) | Surya, "The causal set approach to quantum gravity", Living Reviews in Relativity | 1903.11544v2 | Sec. 2, 3, 4, 4.1, 4.2 searched in the ar5iv HTML (first 100,000 of 268,327 characters). |
| Sorkin03 (added to REFERENCES.bib 2026-11-01) | Sorkin, "Causal sets: discrete gravity (notes for the Valdivia Summer School)" | gr-qc/0309009v1 | Searched in the HTML for "number = volume", Planck units, sprinkling. The notes have unnumbered sections. |
| [KMS06] | Konopka, Markopoulou, Smolin, "Quantum graphity" | hep-th/0611197 | Searched in full in the HTML for speed, time step, lattice spacing, Planck. Read in full by the project earlier. |
| [KMSev08] | Konopka, Markopoulou, Severini, "Quantum graphity: a model of emergent locality" | 0801.0861v2 | Searched in full in the HTML for the same terms; REFERENCES.bib marks it unread. |
| HMPS09 (added to REFERENCES.bib 2026-11-01) | Hamma, Markopoulou, Premont-Schwarz, Severini, "Lieb-Robinson bounds and the speed of light from topological order" | 0808.2495v2 | Abstract and the two sections on the effective theory and the bound searched in the HTML. |

The five keys marked "added to REFERENCES.bib 2026-11-01" were entered the same day (first written as owed entries), with these read statuses, before any of them is cited in
a paper (rule 1). This note does not add them (it writes one file only).

Verified against the sources by a second agent on 2026-11-01; its corrections applied the same day.

## 2. The published model: what has units, and what fixes them

### 2.1 [T25]: two fundamental units, both left open

**Only a dimensionless coupling is fundamental; energy, length and speed are emergent.** Sec. I: "the intrinsic
fluctuations of binary degrees of freedom can only be governed by a dimensionless coupling." Of Planck's constant,
Sec. I: "its definition requires the concepts of energy, a length scale and a speed, which are emergent", and so
"Planck's constant cannot be a fundamental constant of nature". Time: it "becomes, thus an emergent geometric time".

**The link length is put in by hand and the Planck length is identified with the correlation length.** Sec. IV.1: "To
make contact with manifolds, we shall henceforth endow the links of the graph with a uniform length scale ℓ and identify
the correlation length with the Planck length, ξ(g)ℓ = ℓ_P(g). With this definition, the Planck length vanishes at g = 0
whereas at g = g_cr it equals the graph diameter." Here ξ(g) is the decay length of the square-square correlation in
graph steps ([T25] Eq. (23); see the note of 2026-10-22). Sec. I says the same in words: "a fundamental scale, the
Planck length, emerges naturally in the geometric phase. This scale, given by the correlation length, characterizes the
typical size of clusters". *Ours:* so in [T25] the Planck length is **not** one link. It is ξ(g) links, a number that
depends on the coupling, and ℓ itself is never given a value in meters.

**The two units, named.** Sec. V, on the motion of defects: "it is an open question, beyond the scope of this review,
how the collective translation can occur in terms of elementary edge moves. In any case the average velocity v of this
collective Brownian motion is limited by above by a velocity c determined by the length ℓ and the inverse number of
elementary moves per unit time, which are the two sole fundamental units in the model." *Ours:* this is the sentence the
owner's question needs. The published model's own author says the model has exactly two units to fix, a length per link
and a time per elementary move, and that a top speed c is their ratio. He does not fix either.

**Time.** Sec. V: "we need to introduce a universal Newtonian time t". Sec. V.1, after Eq. (31): "Asymptotically, the
manifold coordinate z is dynamically soldered to the absolute time"; "with positive curvature, the universal time t
becomes the coordinate time of a Lorentzian manifold." Eq. (31): "z_t = v t", "where v = J D/2 is the inertial
velocity of the defect and D is the diffusion coefficient, which depends on its size." Eq. (44) uses "the previously
introduced time t~ measured in seconds". The words "sweep", "Monte Carlo step", "unit of time" and "quantum of time" do
not occur in Sec. V; "Monte Carlo" occurs only in Sec. IV, for the sampler. *Ours:* the universal time of [T25] is a
diffusion time of defects, a continuous parameter in a hydrodynamic picture, and the paper never equates it to a count
of Monte Carlo sweeps. The sampler's clock and the model's universal time are different things in the published model
too.

**The bridge to mass, Eq. (45), Sec. VI.1** (verbatim as the HTML renders it; the full reading is in
`2026-10-22_eq45_free_energy_to_curvature.md`): "−(⟨K⟩ − 4Λ₂) ℓ² = (κ/ℓ) F, κ = n(g) 8πG_N / c⁴, in units where the free
energy F is measured in Joule with respect to the surrounding geometric matrix with curvature 4Λ₂. G_N is Newton's
gravitational constant and n(g) is a numerical factor depending on the original coupling g." Sec. VI.2: "We identify the
internal energy as the black hole mass (times velocity squared)." No formula for n(g) and no conversion from the graph's
energy count to a joule appears anywhere in the text (confirmed again today across the whole HTML, including the tail
from character 100,000 on, where the only unit-like phrase is Sec. VI.3's "an extremely high curvature 1/ℓ²").

### 2.2 [KTB19]: a dimensionless volume and a cosmological length, no Planck length

Sec. 1, Eq. (3): β = (ℏg)⁻¹ where "g is the gravitational coupling strength in units of the Newtonian gravitational
constant" (the paper's only mention of Newton's constant). Sec. 3.1.1: "the RHS diverges in the thermodynamic limit for
D > 2 unless we renormalise g"; "We thus identify β~ = (ℏg)|V(ω)|^(2/D − 1) and investigate the phase transition in terms
of β~." The lengths: "Treating |V(ω)| as a dimensionless universe volume", the paper writes ℓ = ℓ₀|V(ω)|^(−1/D), where
"ℓ₀ is a fixed length scale (a cosmological scale)"; and "Since |V(ω)| is the dimensionless volume of the universe, |S|
thus scales as an area". Sec. 3.1.2: "treat each edge intersecting with u as a basis vector of length ℓ in the tangent
plane of u." Sec. 1: "the discreteness scale ℓ is then sent to 0" (of dynamical triangulations), and ℓ is called "an
effective discreteness scale (cutoff)".

**Not found in [KTB19]:** the words "Planck length", "Planck scale" or "Planck" (searched; absent in the first 100,000
characters, which cover the sections that define the model). *Ours:* [KTB19] fixes the link length from the top down,
ℓ = ℓ₀ N^(−1/D) with ℓ₀ a cosmological scale, so that more points means shorter links at fixed total size. That is the
opposite direction from [T25]'s bottom-up identification and from the Planck-length-per-link convention below. At D = 2
the coupling rescaling is the identity, which the record already has (ASSUMPTIONS Q3 and Update 3).

### 2.3 [T22]: the edge length is a free scale, the Planck length runs with the coupling

Sec. III: "Let us endow the graph edges with a fixed length ℓ and let us investigate what are the manifolds"; the
coupling is written ℏg = N^(1 − 2/D) χ_cr f "with f = χ/χ_cr denoting the dimensionless gravitational coupling"; "We
shall identify the dynamical scale ξ(f) with the Planck length ℓ_P(f)"; "We then have ℓ_P(0) = ℓ and ℓ_P(1) = N^(1/D) ℓ".
Sec. I: "this is the Planck length and is directly related to the cosmological constant and the emergence of time."
No numerical value or unit for ℓ anywhere.

**Time in [T22].** Sec. I: "time as we know it is far from fundamental but most probably an emergent concept"; "there is
no a priori notion of either time or space"; "the concept of time as a coordinate of a space-time manifold is an
emergent asymptotic concept". Sec. IV, Eqs. (15) to (17): the spectral dimension is read from "the return probabilities
after t diffusion steps on the graph", and near Eq. (19): "a scale factor from the different definitions of the
diffusion time t can be absorbed in a redefinition of the curvature." Sec. V, Eq. (27): "the coordinate z can be
identified with the diffusion time" and "a dimensionful diffusion coefficient has been absorbed into t"; "it escapes to
infinity at unit speed and has an asymptotic direction"; Eq. (23): "where v is the velocity of propagation of the
ballistic particles." Sec. VII: "there is no more time coordinate as we know it, only diffusion time." Not found: any
absolute time tied to Monte Carlo steps, any speed of light in links per step, any Planck time. *Ours:* [T22]'s
time is the step count of a random walk on a fixed graph (the spectral-dimension probe), not the sampler's sweep; its
normalization is explicitly a convention absorbed elsewhere.

## 3. How the neighboring programmes fix units

### 3.1 Causal dynamical triangulations: the lattice spacing is a regulator, and its size in Planck lengths is measured

**The edge length is a physical cutoff, not a coordinate.** AGJL12 Sec. 1.4, after Eq. (2): "Note that the lattice
spacing a is a physical, and not a coordinate length." Sec. 2.1: all spatial squared link lengths are a², timelike
ones −αa², and "There is a preferred notion of a discrete 'time', namely, the parameter labeling successive spatial
slices"; "This 'proper time' is simply part of the invariant geometric data common to each of the Lorentzian
geometries." Sec. 1.5, Eq. (7): the spacing goes to zero at the critical point, a(g₀) ∝ |g₀ − g₀ᶜ|^ν, with the physical
mass held fixed. Sec. 1.10 promises that "Under a few assumptions we can determine the physical size of our quantum
universe in Planck units" (that section, 11, is beyond the 100,000 characters fetched; not read).

**The number itself, from AGJL08.** Sec. 7, Eq. (47): G = (a²/k₁) √C̃₄ s̃₀² / (3√6), the coefficient of the fitted
minisuperspace action read as Newton's constant; "from our measurements we have determined k₁ = 0.038"; "Taking
everything together according to (47), we obtain G ≈ 0.23a², or ℓ_Pl ≈ 0.48a, where ℓ_Pl = √G is the Planck length";
"the linear size πR of the quantum de Sitter universes studied here lies in the range of 12-21 Planck lengths"; "the
Planck length is roughly half a lattice spacing"; and the value runs with the bare coupling, "ℓ_Pl = √G increases from
approximately 0.48a to 0.83a when κ₀ changes from 2.2 to 3.6". Sec. 8 quotes "G ≈ 0.42a²" (the two sections do not
reconcile the two numbers in the text we read). The assumptions are stated: Sec. 7, "Assuming for the moment that the
semiclassical minisuperspace action is valid" and "under the assumption that the coupling constant G of formula (47) is
indeed a true measure of the gravitational coupling constant".

**Time in CDT.** [Loll19] Sec. 5: "One can attach a discrete proper time label t to these sandwiches"; "a renormalized
version of t assumes the role of global, cosmological proper time" in the de Sitter phase; and "Whether or not the label
t can be related to some physical notion of time in a suitable continuum limit cannot be determined a priori." Not found
in [Loll19]'s first 100,000 characters: any value of a in Planck units.

*Ours:* the lesson for the toy is the method, not the number. CDT does **not** declare a to be the Planck length. It
measures a dimensionless coefficient of an effective action, identifies it with 1/G, and reads the Planck length off in
lattice units as an output; a is a cutoff that is meant to go to zero. The toy has no effective action with a
gravitational coefficient to fit, so this route is closed to it today.

### 3.2 Causal sets: one element per fundamental volume, the volume "most obviously" Planckian and not required to be

Surya19 Sec. 3: "One therefore assumes a fundamental correspondence between the number of elements in a region" and its
volume ("Number ∼ Spacetime Volume" (Sec. 3, proposal 2(b); Eq. (5) is the slogan Order + Number ∼ Lorentzian
Geometry)); "A causal set is said to approximate a spacetime C ∼ (M, g) at density
ρ_c = V_c⁻¹" (unnumbered; the faithful embedding it defines is Eq. (7)); "every finite spacetime volume V is represented by a finite number of elements n ∼ ρ_c V";
⟨n⟩ = ρ_c v (Eq. (9)); "the causal set microstate depends on the discreteness scale V_c, which is a fundamental spacetime
volume cut-off." Footnote 7: "The most obvious choice for V_c is the Planck volume, but we will not require it at this
stage." Sec. 4.2 keeps it general, "as long as there is a sufficient separation between the discreteness scale
ℓ_c ≡ V_c^(1/d)" and the scales of interest. Sorkin03: "Only if we measure length in units such that v₀ ≡ 1 can we
express the hypothesis that number = volume in the form N = V"; "In order to realize the equality N = V, the selected
points must be distributed with unit density in M"; and the fundamental scale is estimated, not assumed: from black-hole
entropy, "about one bit of entropy belongs to each horizon 'plaquette' of size κℏ", so that l ≡ (v₀)^(1/4) "is around"
√(κℏ) ∼ 10⁻³² cm with κ = 8πG (the HTML's own figures; the sentence is longer than the quotation).

*Ours:* causal sets make the cleanest statement of the convention this note needs: the one free number is a volume per
element, the natural choice is the Planck volume, and the choice is declared, not derived. There is no time step in a
causal set (it is a partial order, not a dynamics), so nothing there corresponds to the sweep.

### 3.3 Quantum graphity: the lattice spacing is set to the Planck mass by assumption; the speed of light is a derived ratio

**[KMS06] does not say "one link per time step".** Searched in full: no sentence about a speed of light, a maximum
speed, a light cone, a time step, "one edge per unit time", the Planck length or the Planck time. What it has (Sec. IV,
after Eq. (30)): "The variables a and g denote the lattice spacing and the coupling constant, respectively", and before
Eq. (33): "if we set the inverse lattice spacing on the order of the Planck mass", a⁻¹ ∼ m_P, from which it estimates the
sizes of its couplings (Eq. (33)). Sec. I: "The excitations of the spin system are interpreted as photons coupled to
massive charged particles" propagating on the graph of "on" edges; Sec. II.1: "H_hop allows the M variables to propagate
from an on edge to other edges adjacent to the same vertex." It uses a Hamiltonian and a heat bath "kT = 1/β" and never
says whether its time is fundamental. **The task's attribution of "the speed of light as one link per time step" to
[KMS06] is therefore not supported by the text; we have not found it there.** [KMSev08], searched in full: no sentence on
speed, light cone, Lieb-Robinson, lattice spacing or Planck scale either (its one "time-step" is a greedy edge-deletion
process in Sec. V).

**Where the graphity programme does fix a speed of light: HMPS09.** Section "Topological order and artificial light",
after Eq. (1): the effective theory has "speed of light given by c = √(2gJ)" in natural units, with g and J the two
couplings of the spin model; the lattice is "a lattice with Planck-scale distance" (Introduction, an assumption).
Section "Lieb-Robinson bound for the emergent U(1) model", after Eq. (5): "The speed v is estimated numerically as
v ≈ √2 e √(2gJ) ≡ v_LR = √2 e × c"; "We consider this result a strong indication that the maximum speed of signals is
light." *Ours:* so in that programme c is a ratio of couplings with ℏ = 1, in units of one lattice spacing per unit of
1/J; the lattice spacing is *assumed* Planckian and the time unit follows from the energy scale J. Nothing is one link
per step by construction; the one-link-per-step picture is a property of a hopping model with a single coupling in
natural units, not a published definition.

## 4. The Planck units themselves (textbook; general knowledge, to verify against CODATA before use)

ℓ_P = √(ℏG/c³) ≈ 1.616 × 10⁻³⁵ m; t_P = ℓ_P/c ≈ 5.39 × 10⁻⁴⁴ s; E_P = √(ℏc⁵/G) ≈ 1.22 × 10¹⁹ GeV ≈ 1.96 × 10⁹ J. By
construction c = ℓ_P/t_P, so any scheme that sets one link = ℓ_P and one light step = t_P gets c = 1 link per step for
free; that is a tautology of the units, not a result.

## 5. What the toy can and cannot say (ours, unverified)

Facts from the record that the table rests on, each with its source:

- **The toy's light moves one link per sweep by construction.** `graphity.twist.Photon` (her first form, 30 to 31
  October): "carried one link per sweep by its spin"; "Nothing is derived; the values are the rules." The edge-wave field's
  long-wave speed is 2/√m links per sweep and her one c for light and gravity pins m = 4 (`graphity.edge_wave`, waves brief
  Sec. 2B and 3a; her decision (1) confirmed 2026-11-01, "time in sweeps, speeds in links per sweep, c = 1 link per sweep").
  So c = 1 link per sweep is a **decision**, and the one quantity it then fixes is m, not a unit.
- **The chain sweep is a sampler's clock, not a physical one.** O90: the chain picks two links at random from the whole
  graph, so a particular local pair is offered "about 2/N times a sweep", and a fair sweep is N/96 chain sweeps so that
  local events happen at a size-independent rate. The waves brief fixes which sweep the wave uses: the chain's sweep on a
  fixed lattice, the fair sweep where the wave runs beside the chain. Nothing physical selects the number 96; it is the
  size of T19 and T25, kept so their numbers stand.
- **Rates in the toy depend on the coupling g and on stored energy, and are not time dilation.** O93: the tube's front
  crosses a band in 0.80 and 0.71 of the control's time where 6 and 10 units per point are stored, and "Read as a clock, a front
  that runs faster where energy sits is the opposite of clocks running slower near mass". Front speed in columns per
  chain sweep also halves as the tube doubles (O90, T47), which is the sampler, not physics.
- **There is no temperature in kelvin.** g is a dimensionless coupling (TASKS notation: "g coupling (acts like
  temperature)"; [T25] Sec. I above). A Boltzmann factor exp(−ΔH/g) with ΔH a count of squares has no k_B in it; to
  write g in kelvin one would first have to assign a joule to one square, which is the n(g) and joule problem of Eq. (45).
- **The one published bridge to a mass carries two unknowns.** Eq. (45) needs ℓ in meters and n(g), neither given
  ([T25] Sec. VI.1; the note of 2026-10-22, Sec. 3 and 6). Ratios of free energies between two objects at the same g
  cancel both, so the toy can state mass *ratios* under Eq. (45)'s assumptions and never a mass in kilograms.

**The two things that cannot be derived, said once.** (i) A length per link. Every observable the toy measures is a count
(squares, surplus squares, links, points, columns) and is unchanged if every link is declared a meter or a Planck length.
(ii) A time per sweep. Every rate the toy measures is a count per sweep, and the sweep's own content changes with N (O90)
and with the sampler (Metropolis against Glauber, Q11 tempering), so the sweep is not even a fixed unit inside the toy
until a clock rule is chosen. The toy has no action whose coefficient is 1/G (the CDT route), no correlation length tied
to a physical scale (the [T25] route, which would also make ℓ_P run with g), and no energy scale J in joules (the
graphity route). What it has is the two-unit statement of [T25] Sec. V, and the owner's decision that c is one link per
sweep, which ties the two units together without fixing either.

**What is then free, and what is conventional.** With c fixed at one link per sweep, one choice remains: the length of a
link (equivalently the duration of a sweep). The convention in causal sets (one element per Planck volume, Surya19
footnote 7, Sorkin03) and in graphity (a⁻¹ ∼ m_P, [KMS06] Sec. IV; "a lattice with Planck-scale distance", HMPS09) is to
set the discreteness scale to the Planck scale. CDT does not assume it and finds a ≈ 2 ℓ_Pl at one bare coupling
(AGJL08). [T25] and [T22] set ℓ_P to ξ links, which is coupling-dependent and is **not** the one-link convention. So "one
link = ℓ_P" is the usual declaration in two of the four neighboring programmes and is contradicted in form by the
published model this toy is built on, where the Planck length is the correlation length. Either choice must be stated as
a choice.

## 6. The translation table

Status: **derived** means it follows from the toy's rules or measurements with no outside number; **chosen** means an
identification we would declare, with the field's convention noted; **not available** means nothing in the toy or in the
published model supplies it.

| Toy unit | What it would be identified with | Status | Source and remark |
|---|---|---|---|
| 1 link (one edge of the graph) | One length unit ℓ. **Convention:** ℓ = ℓ_P ≈ 1.6 × 10⁻³⁵ m (causal sets: Surya19 fn. 7, Sorkin03; graphity: [KMS06] Sec. IV, HMPS09). **Published model:** ℓ unfixed, and ℓ_P = ξ(g)ℓ, not ℓ ([T25] IV.1, [T22] III). **CDT:** a ≈ 2 ℓ_P measured, not assumed (AGJL08 Sec. 7). | chosen | Conventional in two programmes, contradicted in form by [T25]. The toy's counts do not change under any choice. |
| 1 light step (a photon's advance; one chain sweep on a fixed lattice) | One time unit τ = ℓ/c. With ℓ = ℓ_P, τ = t_P ≈ 5.4 × 10⁻⁴⁴ s. | chosen | Follows from the ℓ row once c = 1 link per sweep is taken. The toy fixes the ratio, not either unit. |
| c (speed of light) | 1 link per sweep; with the rows above, 299,792,458 m/s by construction. | derived in the toy as a **rule** (hers, 30 October to 1 November; `Photon`, `edge_wave` m = 4); the m/s value is a tautology of the two chosen rows | [T25] Sec. V has c as the ratio of the two units; HMPS09 has c = √(2gJ) in natural units. Neither is one link per step by derivation. |
| 1 chain sweep (2N proposals) | A sampler's unit: each local pair offered about 2/N times. Not a physical time. | not available as a physical time; derived as a sampler fact | O90. On a fixed lattice the waves brief uses it as the wave's clock by decision (1). |
| 1 fair sweep (N/96 chain sweeps) | The size-fair unit for local rates; equal to the light step where a wave runs beside the chain (decision (1)). | chosen (the 96 is T19's and T25's size, not physics) | O90. Nothing physical selects 96; it keeps earlier numbers unchanged. |
| 1 unit of H (one quarter of a lost square; H = 16(N − S) + 4λX) | An energy in joules. [T25] Eq. (45) needs this through F "measured in Joule" and n(g). | not available | [T25] VI.1; the note of 2026-10-22. Ratios of F between objects at the same g are independent of it. |
| g (the coupling) | A temperature in kelvin, k_B T, only after one unit of H is a joule. | not available | Dimensionless by the model's own statement ([T25] Sec. I). exp(−ΔH/g) carries no k_B. |
| A mass (a relic's F) | Through Eq. (45), (⟨K⟩ − 4Λ₂) and n(g) 8πG_N/c⁴; needs ℓ and n(g). | not available (ratios only) | [T25] VI.1, VI.2 ("internal energy as the black hole mass (times velocity squared)"). |
| The front's speed (columns per sweep) | A physical speed only through the ℓ and τ rows; its energy dependence (O93) is a sampler effect of stored energy, not a metric effect. | derived as a toy rate; not a clock rate | O90, O93, T47. On the chain sweep it halves as N doubles; on the fair sweep it is constant. |
| N (points) | A volume or area in ℓ^D. [KTB19] instead sets ℓ = ℓ₀ N^(−1/D) with ℓ₀ cosmological, making the whole graph a fixed size. | chosen (two published conventions pull opposite ways) | Causal sets: N = V in units of V_c. [KTB19] 3.1.1: N is "a dimensionless universe volume". |

**Said plainly for the owner.** The toy can honestly say: "if one link is one Planck length and light moves one link per
step, then one step is one Planck time, and every speed we report in links per sweep is that fraction of c." Those two
"ifs" are declarations. They are the same declarations causal sets and quantum graphity make, so making them is
conventional, not a fit to anything, and no verdict in the record depends on them. The toy cannot say what a square's
worth of energy is in joules, what g is in kelvin, or what a relic weighs in kilograms; the published model cannot either
(its Eq. (45) leaves ℓ and n(g) open, and its own Planck length is ξ(g) links, not one). And the sweep remains a sampler's
clock: its physical content was decided (c = 1 link per sweep), not measured, and the fair sweep's 96 is a bookkeeping
choice.

## 7. What this does not settle, and what is owed

- Whether the toy should adopt "one link = ℓ_P" (the causal-set and graphity convention) or "ℓ_P = ξ(g) links" (the
  published model's), or neither. This is a dated decision of the owner's under S1 if any page is to carry a meter or a
  second; until then the pages say "links" and "sweeps".
- The CDT review's Section 11 (AGJL12) is beyond the 100,000 characters fetched and was not read; the Planck-unit number is taken from AGJL08 Sec. 7 instead, and its
  own Sec. 7 and Sec. 8 give two values of G in a² (0.23 and 0.42) that the text we read does not reconcile.
- Bibliography entries for AGJL12, AGJL08, Surya19, Sorkin03 and HMPS09, with the read statuses of Sec. 1, before any is
  cited; [Loll19]'s and [KMSev08]'s notes to be updated from "not read" to "searched in part, 2026-11-01"; and check
  the [T25] title field in REFERENCES.bib against arXiv 2512.17676v2 ("Networks as the fundamental constituents of the
  universe").
- The attribution of "c = one link per time step" to [KMS06] in the task is **not found** in that text; if a page has
  said so, it should cite HMPS09's c = √(2gJ) instead, or the toy's own rule.
- Nothing here is about the real universe. A unit attached to a count makes the count easier to picture; it does not make
  the toy a measurement of anything.

# Independent audit by Codex, 25 October 2026

*Pasted into the session by the owner on 25 October 2026. The reviewer was Codex (a different model), working from the
brief `docs/reviews/2026-10-25_codex_audit_brief.md`, pinned to commit 247da44e and blind to the same-day audit O155.
The text below is the report as received; only the citation chips of the reviewer's interface ("GitHub", "arXiv +1",
"Phys. Rev. D" and the like, standing alone on a line) have been removed. What it found and what it got wrong, checked
against the record, is ASSUMPTIONS O156; the corrections are VISION Update 117.*

---

Independent audit: 25 October 2026
Repository: RecreationalPhysics
Branch: claude/particle-sector-2026-10-24
Target commit: 247da44eb33b163c8bb84f7998f10c982dcfc157
Scope: The 25 October record, especially VISION.md Updates 104–111, the owner's notebook entries, the questions file,
four sandbox investigations, and the cited reading notes.

## 1. Summary

1. The square-count arithmetic is correct, but the claimed Gauss–Bonnet equivalence is not established. The toy graph is
   not automatically a two-dimensional surface.
2. The proposed growth move is impossible as stated. A four-regular bipartite graph cannot gain exactly one vertex while
   preserving its defining properties.
3. The N = 18 connectivity result checks out, but only for the investigated move set and graph family. It does not
   establish that the proposed model works at larger sizes.
4. The cube and continuum wave calculations reproduce, but both are interpreted too broadly. The light mode is
   particularly problematic: the earlier record identifies it as a scalar, not a photon.
5. The existing curvature-sign experiment does not test the new rule. It uses saved states from the old dynamics.
6. Several published-physics comparisons are inaccurate or too strong, particularly Birkhoff's theorem, the Higgs/charge
   claim, bubble-wall physics, and baryogenesis.
7. The record generally preserves the owner's words, but some assistant conclusions have become recorded answers or
   decisions.
8. The main correction is evidentiary: keep arithmetic identities, finite checks, proposed mechanisms, published
   results, and owner decisions separate.

Overall assessment: The record contains useful calculations and potentially productive analogies. It does not yet
provide a consistent mathematical realization of the proposed cosmology, and several statements labeled exact or
published should be downgraded.

## 2. Findings

### 1. The zero-total rule

**1. The central counting identity is correct. — High confidence**

Where: VISION.md, Update 105.

Let \(N\) be the number of vertices, \(S\) the number of four-cycles, and \(S_e\) the number of four-cycles containing
edge \(e\). In a four-regular graph there are \(2N\) edges. Each square contains four edges. Therefore,
\[ \sum_e(S_e-2)=4S-2(2N)=4(S-N). \]
Thus the proposed rule of zero total curl-minus-uncurl is exactly \(S=N\), under the record's definitions.

For a six-regular graph there are \(3N\) edges and the chosen flat baseline is four squares per edge, giving
\[ \sum_e(S_e-4)=4S-12N=4(S-3N). \]
So \(S=3N\) is also correct. These are combinatorial identities, not numerical approximations.

**2. The Hamiltonian simplification is correct, but its consequences are understated. — High confidence**

Where: Updates 105 and 108; the published CQG Hamiltonian.

The quoted Hamiltonian is \(H=16(N-S)+4\lambda X\). Under \(S=N\), its square-count term is zero, not merely an
unspecified constant, and \(H=4\lambda X\).

There is an important qualification: the proposed zero-total restriction is not part of the published CQG model. It
defines a new model.

There is also a distinction between the graph families used in the record. In the version with a maximum of two squares
per edge, \(S=N\) forces every edge to have exactly two squares, so \(X=0\). Then \(H=0\) for every permitted state. To
retain balanced curled and uncurled edges, the model needs a graph family allowing more than two squares per edge.

Thus the restriction can eliminate the energy distinction that was supposed to drive the dynamics. This deserves an
explicit warning next to the proposed rule.

**3. The N = 18 connectivity calculation is sound within its stated search. — High confidence**

Where: sandbox/zero_total_rule_reach_n18.py; Update 108.

I independently reconstructed the four-regular bipartite graph search and the allowed edge-switch transitions rather
than treating the recorded output as proof.

The calculation reproduced:
- 26 graph-isomorphism classes at \(N=18\);
- nine classes satisfying \(S=18\);
- three of those nine with \(X=0\);
- six with balanced curl and uncurl;
- one connected component among all nine allowed classes when moves must preserve \(S=18\).

The nine classes have \(X\)-values \(0,\ 0,\ 0,\ 2,\ 4,\ 4,\ 6,\ 8,\ 9\).

Using classes rather than individually labeled graphs is legitimate here because the legal moves are invariant under
relabeling, and the isomorphisms preserve the bipartite structure. Connectedness of the quotient is sufficient for the
corresponding labeled configurations, up to the specified side-preserving relabelings.

Limit: This proves a finite result for the selected degree, size, constraints, and moves. It does not show
connectedness for arbitrary \(N\), nor that curled configurations survive the stricter two-square-per-edge family. The
record should not use it as evidence of general ergodicity.

**4. Zero total does not imply zero energy cost for changing the system's size. — High confidence**

Where: Updates 105–106.

An \(H=0\) configuration at one fixed \(N\) and another \(H=0\) configuration at another \(N\) do not establish a
zero-cost growth process.

A variable-size model needs its own definition of the allowed moves and statistical weights. Even if an energy
difference is zero, the number of accessible arrangements changes with \(N\), and so can the free energy and
probability of growth.

The record notes that a growth rate is needed, but it first treats costless growth as an established consequence of the
existing fixed-\(N\) Hamiltonian. That step is unjustified.

### 2. Combinatorial Gauss–Bonnet

**5. The Gauss–Bonnet proof requires a surface that the toy has not supplied. — High confidence**

Where: Update 104 and the owner's clarification in Update 107.

For a genuine quadrangulation of a closed surface, a familiar combinatorial curvature at vertex \(v\) is
\[ K(v)=1-\frac{d(v)}2+\sum_{f\ni v}\frac1{|f|}, \]
with the sum counting face corners.

For a four-regular quadrangulation, each vertex has four corners belonging to four-sided faces, so
\(K(v)=1-2+4/4=0\).

More generally, with degree four and all incident faces having at least four sides, \(K(v)\leq0\). On a torus, the total
curvature is zero by Euler's formula, forcing every vertex to be flat. That is valid mathematics for the stated kind of
cellular embedding.

But CQG supplies an abstract graph. Its four-cycles are not automatically faces of a cellular embedding, and a generic
graph need not be a toroidal quadrangulation at all. Counting every four-cycle as a face can count overlapping or
geometrically incompatible cycles.

The owner's further clarification makes this more important: the proposed surface is not a spatial surface but two
underlying degrees of freedom, twist and curl. Having two degrees of freedom does not itself define a two-dimensional
manifold, a metric, faces, or Euler characteristic.

The Gauss–Bonnet analogy is worth keeping, but the alleged theorem about this toy is unproved.

**6. The comparison with two-dimensional Einstein gravity is too loose. — High confidence**

Where: Update 105.

For a fixed-topology closed two-dimensional manifold, the integral of scalar curvature is a topological quantity, so the
pure Einstein–Hilbert term gives no local bulk gravitational dynamics.

The proposed graph rule instead fixes a number of four-cycles. These are different constructions. The 2D result does not
establish that the toy's curl is geometric curvature, that its square count has the required continuum limit, or that no
dynamics remain.

The precise statement should be: The proposed conservation rule resembles a topological constraint in one respect, but
no equivalence to two-dimensional gravity has been demonstrated.

### 3. The cube investigations

**7. The finite cube calculations are correct. — High confidence**

Where: sandbox/cube_sixty_degree_look.py; Update 107.

I reproduced the script's geometry:

| Operation about a cube body diagonal | Symmetry? | Effect on vertex colors |
|---|---|---|
| 60° rotation alone | No | Not applicable |
| 120° rotation alone | Yes | Preserves |
| 180° rotation alone | No | Not applicable |
| 60° rotation plus perpendicular mirror, \(S_6\) | Yes | Swaps, for this cube-centered setup |
| \(S_6^2\) | Yes | Preserves |
| \(S_6^3\) | Yes; central inversion | Swaps, for this cube-centered setup |

There are also 12 right-angle pairs among the six links meeting at a cubic-lattice point and three straight pairs.

**8. The color-swap claim depends on the center, and inversion is not spin one-half. — High confidence**

Where: Updates 107–109.

The script applies transformations about the cube's center. With that choice, the \(S_6\) operation swaps the cube's
bipartite vertex colors.

Apply the same linear signed-permutation matrix about an integer lattice point, however, and it preserves the parity
coloring of the infinite cubic lattice. I checked both conventions. Consequently, swapping black and white is not an
intrinsic property of the rotation-plus-mirror matrix independent of origin.

Also, three \(S_6\) operations yield inversion through the cube's center, not an ordinary 180° rotation. Physical spin
one-half refers to how quantum states transform under rotations: a full 360° rotation changes a spinor's sign, while
720° returns it. A parity operation does not prove this structure.

Update 109 usefully separates the proposed internal strand twist from a turn of the grid. That correction should be
retained; the earlier cube analogy should not be promoted into a derivation of electron spin.

### 4. Push on the opening front

**9. The continuum reflection calculation and momentum sign reproduce. — High confidence**

Where: sandbox/front_push_step.py; Update 110.

For a wave of frequency \(\omega\) crossing from a region with dispersion \(k_{\rm curled}=\sqrt{\omega^2-m^2}\) to one
with \(k_{\rm open}=\omega\), the selected stand-in gives
\[ R=\left(\frac{k_{\rm open}-k_{\rm curled}}{k_{\rm open}+k_{\rm curled}}\right)^2, \qquad T=1-R. \]
Writing \(a=k_{\rm curled}/k_{\rm open}\), its calculated momentum transfer per incident quantum is
\[ \frac{\Delta p}{k_{\rm open}} = a(1+R)-T =-\frac{2a(1-a)}{1+a}. \]
For \(0<a<1\), the result is negative.

I reproduced the recorded values, including \(-0.3431\) at \(\omega=2.20\) and \(-0.3000\) at \(\omega=2.50\). There is
no arithmetic error in this specific continuum exercise.

**10. The exercise does not determine the force on the actual lattice front. — High confidence**

Where: Updates 110–111.

The model uses a stationary, one-dimensional continuum mass step, not the proposed moving, charged, dynamically rewiring
lattice boundary.

It does not include the momentum carried by the boundary's own changing fields, radiation incident from both sides, the
field's graph-specific dispersion, shell charge, or backreaction. Therefore the statement that reflected light helps the
cosmological front open is, at most, a possible interpretation of this chosen stand-in.

The negative sign in one coordinate convention is not itself a general prediction about a moving front.

**11. More seriously, the backed-up mode is not identified as a photon in the earlier model record. — High confidence**

Where: Update 109 versus sandbox/LOG.md, 24 October correction.

The 24 October log explicitly corrects an earlier characterization: the mode along the curled direction is a
Wilson-line scalar, not light; the propagating light mode retains the flat speed.

Update 109 then states that one polarization of light backs up at the curled boundary and labels that conclusion exact
in the toy. This contradicts the earlier correction.

A reflected scalar mode may be interesting, but it cannot be used as a demonstrated photon pressure mechanism without
first resolving which field degree of freedom is being scattered.

### 5. The curvature-sign investigation

**12. The recorded counts are internally consistent, but they do not test the new zero-total model. — High confidence**

Where: sandbox/opened_space_curvature_sign.py; Update 108.

The log reports 600 saved outcomes:

| Sign of measured curl-minus-uncurl | Count |
|---|---|
| Positive | 519 |
| Zero | 80 |
| Negative | 1 |

The reported mean is approximately \(+9.2\).

I inspected the calculation and its source data requirements, but could not rerun the original script because the
saved T51 adjacency archives were not locally available. The numerical counts are therefore not independently verified.

The more consequential issue is interpretive. These are saved outcomes of the earlier, unconstrained fixed-\(N\)
dynamics, not runs under the newly proposed hard \(S=N\) rule. The result can challenge an earlier intuition about that
old model. It cannot establish what the new model predicts.

**13. Cooling-rate dependence is not a system-size effect. — High confidence**

Where: The curvature-sign log and discussion.

The decline in residual curl with slower cooling reflects a change in annealing protocol and relaxation time. It is not
evidence that the signed residue approaches zero with increasing graph size. That would require comparisons across
sizes with properly matched cooling schedules and observables.

Finally, signed excesses in graph squares are not, without further construction, measurements of positive or negative
cosmological spatial curvature. The sign labels should stay attached to their combinatorial definition.

### 6. Physics recalled from memory

**14. Birkhoff's theorem and LIGO are overextended. — High confidence**

Where: Update 104; later references to a hidden parental surplus.

Birkhoff's theorem concerns spherically symmetric vacuum regions. A rotating, nonspherical black-hole merger is not
covered by that hypothesis.

An event strictly inside an event horizon cannot send an outgoing signal to infinity, but that fact comes from causal
structure, not the proposed use of Birkhoff's theorem. Changes affecting the observable exterior would need to satisfy
the measured merger waveform and energy accounting.

LIGO does not interpret its signals as sudden mass-loss "burps." Its inspiral–merger–ringdown consistency tests compare
the remnant's inferred mass and spin across signal phases. Results agree with general relativity within uncertainties,
and searches have not established post-merger echoes. Echoes are often discussed as signatures of exotic reflective
near-horizon structure, not proof of an event inside a conventional horizon.

The record is right to treat the burp as a hypothesis. It is wrong to imply that standard black-hole theorems make it
observationally unconstrained.

**15. Matter–antimatter mirroring does not reverse gravitational curvature. — High confidence**

Where: Update 104.

The record correctly warns that a mirror image does not reverse ordinary scalar curvature. ALPHA-g's 2023 antihydrogen
experiment also found antihydrogen falling downward, consistent with ordinary gravitational attraction at its measured
precision.

However, this is not merely a problem awaiting a "handed sorter." Electromagnetically separating opposite electric
charges is not the same as separating baryon matter from antibaryon antimatter. Electrons and positrons, protons and
antiprotons, and neutral composite particles make the distinction unavoidable.

The proposed separation mechanism needs a clearly defined conserved quantity and particle-species accounting.

**16. Wald, Blandford–Znajek, Vilenkin, and leptogenesis are related but distinct results. — High confidence**

Where: Update 104's proposed black-hole sorter.

- Wald (1974): A rotating black hole placed in an external magnetic field develops an electromagnetic field and
  selectively accretes electric charge. This does not demonstrate bulk matter–antimatter sorting.
- Blandford and Znajek (1977): Their mechanism extracts rotational energy electromagnetically from a spinning black hole.
  It does not produce a net baryon asymmetry by itself.
- Vilenkin: The cited directional neutrino effect is real: a rotating emitter can favor neutrinos in one direction and
  antineutrinos in the other because weak interactions violate parity. Crucially, the first Parity Nonconservation and
  Rotating Black Holes article was published 27 November 1978, not first in 1979; it has a 1979 erratum and a related
  1979 follow-up.
- Leptogenesis: A directional flux is not automatically the creation of net lepton number, nor does it show how the
  proposed black-hole event generates the observed baryon excess.

These can motivate questions about spin, weak handedness, and charge flow. They are not a published version of the
proposed two-universe sorting mechanism.

**17. Weak handedness is described too broadly. — High confidence**

Where: Update 104.

The useful Standard Model fact is that left-chiral fundamental fermions form weak \(SU(2)_L\) doublets, whereas their
right-chiral partners are singlets. The charged-current weak interaction selects the appropriate chiral components.

But the neutral weak interaction also couples to right-chiral charged fermions. Chirality should not be conflated with
helicity, and parity violation alone does not give a reliable cosmic matter–antimatter sorter or the CP violation
required by ordinary baryogenesis.

**18. Several elementary particle checks are right; the Higgs interpretation is not. — High confidence**

Where: Updates 104–106.

Correct points include:
- A photon can produce an electron–positron pair near a nucleus or another recoiling system, given sufficient energy. A
  single photon cannot spontaneously produce the pair in empty vacuum while conserving four-momentum.
- Electron–positron annihilation at rest ordinarily yields two or more photons, not a single photon.
- A \(\Delta^-\) baryon has quarks \(ddd\), charge \(-1\), and spin \(3/2\).
- Muons and tau leptons have the electron's electric charge despite much greater masses.
- The 21-cm hydrogen line involves a change in the electron–proton hyperfine spin configuration.

But the statement that electric charge and particle masses both first appear when the Higgs field settles is
misleading. The electromagnetic charge generator \(Q=T_3+Y\) is already part of the electroweak theory; electroweak
symmetry breaking selects the unbroken electromagnetic gauge symmetry and gives masses to particular particles. Charge
is not caused simply by possessing mass.

Also, the example \(\Delta\to p+\gamma\) needs a charge label: \(\Delta^+\to p+\gamma\) is allowed, while
\(\Delta^-\to p+\gamma\) is forbidden by charge conservation. Radiative \(\Delta(1232)\) decay is rare, about
0.55–0.65%; approximately 99.4% of decays are to a nucleon and pion.

**19. The Hubble arithmetic checks, but it does not derive coasting cosmology. — High confidence**

Where: Update 106.

I independently checked the scale conversions. With \(H_0=67.4\) km/s/Mpc and an age of 13.79 billion years,
\(H_0t_P\approx1.18\times10^{-61}\), \(H_0t_{\rm age}\approx0.951\). With \(H_0=73\) km/s/Mpc, these become
approximately \(1.28\times10^{-61}\) and \(1.030\). These agree with the recorded arithmetic.

However, the numerical proximity of \(H_0t_{\rm age}\) to one does not establish a linearly expanding universe. Nor does
an opening front speed of \(c\) imply a universal scale factor \(a(t)\propto t\): the front's geometry, number, and
nucleation history matter.

The numerical analogy between inverse Planck/Hubble scales and the \(10^{122}\) cosmological-constant problem is
likewise not a derivation.

**20. Timescape is a useful comparison, not a match. — High confidence on the distinction; medium on the paper-specific
numbers**

Where: Updates 106–107; dated timescape reading notes.

The notes reasonably identify a resemblance: different regions expand differently, and large voids increasingly
dominate volume.

But Wiltshire's timescape cosmology describes spatially negatively curved voids expanding faster than comparatively
spatially flat walls. Its observed acceleration is an apparent, observer-dependent effect; the volume-average expansion
decelerates. It does not add graph vertices or prescribe fronts traveling at \(c\).

The owner's definition "flat means empty" can resolve a vocabulary mismatch, but it cannot make spatial flatness and
spatial negative curvature mathematically identical.

The record's quoted void fractions and acceleration-onset estimates are consistent with its reading notes; I have not
independently verified those numbers from the original papers. Label them from secondary reading, to verify rather than
fully checked.

**21. Bubble-wall physics is not the proposed charged-shell mechanism in published form. — High confidence**

Where: Updates 109–111.

Bödeker and Moore's 2009 paper supplies criteria under which an electroweak bubble wall can accelerate to extremely
relativistic speeds—run away—rather than always reach a speed limit. Their 2017 paper adds transition-radiation friction
that can limit wall Lorentz factors under specified conditions. It is inaccurate to say both simply establish a
universal push-back that grows with speed.

Cohen, Kaplan, and Nelson's electroweak baryogenesis involves CP-violating particle transport near a phase-transition
wall and conversion of asymmetries by baryon-number-violating processes. It does not supply a published model of
oppositely charged shells attracting across causally disconnected universes.

The record states that nothing passes between the universes, while using electromagnetic attraction across their
boundary to hold the front back. A coupling capable of transmitting that force has not been defined.

**22. The remaining published analogies need narrower descriptions. — Medium to high confidence**

Where: Updates 104, 106, and 111.

Boyle, Finn, and Turok's CPT-symmetric cosmology joins time-reflected cosmological branches around the Big Bang; it is
not a merger-generated mother–daughter black-hole universe.

Cohen, De Rújula, and Glashow's matter–antimatter-domain constraints are relevant to neighboring domains in the
observable universe. Separate causally inaccessible universes are not directly subject to the same annihilation-boundary
argument.

The causal entropic principle concerns entropy production within a specified causal region, not a proof that an
observer must appear when two cosmological expansion eras "cancel." The record's "why now" statement is therefore a
proposed interpretation, not a result of that principle.

Hofstadter did discuss video feedback as a strange-loop illustration; the analogy is apt as an image. The Mandelbrot
recurrence is \(z_{n+1}=z_n^2+c\), however, and a visual similarity between recursive patterns and physical networks
establishes no dynamics, critical point, or prediction.

### 7. Light at leading order under the hard rule

**23. The leading square-count cancellation is right, within a limited expansion. — High confidence**

Where: Update 108.

At small field stiffness \(\beta\), the leading independent-plaquette contribution to the integrated field weight has
the same factor for each square, commonly expressed using \(I_0(\beta)^S\). Under the hard rule \(S=N\) at fixed \(N\),
that contribution is identical for all allowed graphs.

So the assistant was right that this leading contribution does not distinguish arrangements with different amounts of
local curl.

But "leading order" refers to a small-\(\beta\) or strong-coupling expansion, not all \(\beta\). The result does not
establish the full field's effect on curling at physically relevant stiffness.

**24. One normalization difference cancels exactly, while higher-order geometry effects do not. — High confidence**

Where: The field zero-energy fork discussed in Updates 105 and 108.

Two common plaquette weights, \(e^{\beta\cos\phi}\) and \(e^{-\beta(1-\cos\phi)}\), differ by \(e^{-\beta}\) per square.
If \(S=N\) is fixed, their total ratio is \(e^{-\beta S}\), a graph-independent factor for every \(\beta\). Thus that
particular choice of energy zero cannot change relative graph probabilities in the hard-rule, fixed-size ensemble—not
merely at leading order.

Other field effects can depend on the arrangement of squares through closed surfaces, shared boundaries, and
higher-order terms. Those are not canceled by holding \(S\) constant.

At \(\beta=0\), the field decouples. Beyond that, the sign of its full correction is uncomputed here. The record should
distinguish this exact normalization cancellation from the unresolved physical effect of the field.

### 8. Her words against the assistant's readings

**25. The notebook preserves the owner's original words, but some later answers are not hers. — High confidence**

Where: sandbox/NOTEBOOK.md, 25 October; docs/design/owner_questions_2026-10-24.md, "Answered on 25 October, first
pass."

The notebook accurately retains the owner's question about whether LIGO might be seeing burps. The rewritten questions
file lists "LIGO's signals are not burps" among the day's answers.

That is the assistant's assessment, not an answer supplied by the owner. It should be moved out of the owner-answer list
and labeled as an assistant interpretation or external constraint.

**26. The curvature-sign decision needs a direct read-back. — High confidence**

Where: Notebook's initial 25 October entry; Update 108; questions file H5.

The original proposal says the black hole around us has slight negative curvature, and matter universes like ours also
have slight negative curvature, while the pair is net flat.

The later record says ours negative, parent positive, and attributes agreement to the owner.

A later question about the sign receives a request for more information and general assent to proceeding with a sandbox
check, but I did not find a comparably clear owner statement explicitly reversing the original parent sign.

The best classification is unresolved or internally contradictory, not a settled confirmed sign assignment.

There is a further mismatch: the owner's "net flat" was explained in terms of the loop and stacked amplitude versions,
not necessarily one parent-plus-daughter spatial surface. The later account treats those as equivalent without
constructing the proposed averaging.

**27. Broad permission to proceed is repeatedly converted into detailed acceptance. — Medium to high confidence**

Where: Update 106's "Proceed, as you suggest"; Updates 109–111.

"Proceed, as you suggest" reasonably authorizes investigating the assistant's proposed direction. It does not, on its
own, demonstrate independent endorsement of every asserted component: the exact cosmological expansion history, a
timescape-like mechanism, or entropy-based observational prediction.

Similarly, the owner's "Adopt at l3" supports the chosen L3 answer about shell charge. It does not establish the
correctness of the assistant's continuum pressure calculation or the existence of the proposed force.

The clean distinction is:
- Owner's words: preserved in the notebook.
- Owner's decision: only what she explicitly accepted.
- Assistant's reconstruction or predicted implication: labeled as such until read back.
- Physical validation: still separate from either person's acceptance.

### 9. Kinds of statement and evidence labels

**28. "Exact" is sometimes used for an identity and sometimes for a physical interpretation. — High confidence**

Where: Updates 105–110.

Correct examples of exact include square-incidence counting, a cube's finite symmetries about the chosen center, and the
specified continuum scattering algebra.

Incorrect expansions of that label include:
- A Gauss–Bonnet property of an abstract graph with no supplied cellular embedding.
- A physical photon backed up by a curl mode that the earlier log identifies as a scalar.
- The assertion that global curl–uncurl balance requires a shell around the front, rather than compensating defects
  located somewhere in the graph.
- A one-vertex growth process that has no legal graph operation behind it.

These should be marked hypothesis, interpretation, or unverified construction.

**29. Exploratory sandbox calculations are doing work reserved for promoted tests. — High confidence**

Where: Updates 107–110; CLAUDE.md rule 16.

The record's own method says a sandbox look may rule out an idea or help design a test, but cannot by itself support a
promoted claim.

The cube calculation establishes cube geometry; it does not establish particle spin. The curvature-sign look evaluates
earlier runs; it does not validate cosmology. The continuum wave step establishes a boundary calculation; it does not
demonstrate a force on the intended graph model.

These results are valuable precisely when their limits remain visible. Their current use as evidence for physical
mechanisms is too strong.

**30. Several "published form" and "general knowledge" labels need correction. — High confidence**

Where: Updates 104–111.

The phrase published form is especially misleading for the claim that Bödeker–Moore plus Cohen–Kaplan–Nelson supply the
charged front mechanism. They establish particular phase-transition and baryogenesis results, not the described
mother–daughter cosmology.

Some physics is flagged "general knowledge, to verify," as required. Other sentences are presented with comparable
confidence despite not being checked at their primary sources—especially the Higgs/charge sentence, the strong
timescape mapping, and the stated Birkhoff consequence.

A reference's presence in REFERENCES.bib is not evidence that its claimed implication was verified. The claim and the
paper's actual result need to match.

### 10. Internal consistency

**31. The proposed "one point and one square" growth step violates four-regular bipartite graph arithmetic. — High
confidence; major finding**

Where: Updates 106 and 107.

For a four-regular bipartite graph with black vertex set \(B\) and white vertex set \(W\), count the edges from each
side: \(4|B|=E=4|W|\). Therefore \(|B|=|W|\), and \(N=|B|+|W|=2|B|\) must be even.

Adding exactly one point cannot preserve the defining four-regular bipartite structure, regardless of whether a square
is added. A vertex also requires four incident edges, degree-preserving rewiring, and all other validity constraints.

The identity \(\Delta S=\Delta N\) is necessary to preserve \(S=N\), but not sufficient to define a valid graph
operation.

This is the clearest concrete mathematical error in the proposed expansion mechanism. The record needs to withdraw the
claim that adding one flat cell is already permitted by the toy.

**32. The global hard rule does not require a local uncurl shell. — High confidence**

Where: Updates 105 and 109.

The global equation \(\sum_e(S_e-2)=0\) requires equal total positive and negative contributions. It says nothing about
their distance apart or whether uncurl has to surround each curled object.

A shell around the front is an additional spatial-locality condition. It requires a definition of locality and proof or
a new explicit rule. It cannot be described as an exact consequence of \(S=N\).

**33. The proposed charge sorter does not explain the observed matter excess or electrical neutrality. — High
confidence**

Where: Updates 104, 108, and 111.

The proposal variously invokes antimatter curls, positrons pulled away by a black hole, excess electrons, and a matter
surplus.

These are not interchangeable. A universe containing excess electrons but no matching positive electric charge would be
highly charged, whereas ordinary observed matter is electrically neutral to excellent approximation. Removing positrons
does not by itself create an excess of baryons over antibaryons.

The bookkeeping needs to keep at least electric charge, baryon number, lepton number, and the record's proposed strand
handedness distinct. At present the verbal mechanism switches between them.

**34. Several pairs of statements remain incompatible without additional definitions. — High confidence**

Where: Updates 104–111 and the questions file.

- Curvature: The parent's negative sign in the first owner proposal conflicts with the later recorded positive sign.
- Surface: A proposed nonspatial two-degree-of-freedom foundation is treated as though an ordinary toroidal surface
  theorem already applies.
- Flatness: "Flat" means empty in the owner's usage, but geometrically flat walls and negatively curved voids are
  distinct in the cited timescape model.
- Growth: Points and links are described as emergent rather than fundamental, yet the expansion proposal relies on
  directly inserting them into the model.
- Rotation: H3's grid-turn description is superseded by Update 109's internal strand-twist decision; the stale
  formulation should not remain a simultaneous active assumption.
- Causality: Nothing passes between the mother and daughter, yet an electromagnetic attraction across them is supposed
  to exert a holding force.
- Conservation: Net zero over "stacked amplitude versions" is treated like an arithmetic sum of classical geometric
  curvatures. Quantum amplitudes cannot simply be added as signed curvatures; a specified quantum state, observable, and
  probability measure would be needed.

These are not necessarily fatal to the owner's exploratory ideas. They are unresolved incompatibilities in the recorded
model and must not appear as already reconciled.

## 3. What I ran

Execution limitation: Direct cloning from GitHub was blocked by the environment's network configuration. I inspected
files at commit-specific GitHub URLs and reconstructed the runnable computations in an independent scratch directory. I
did not modify the repository or run anything writing to results/. The reproductions below are independent
implementations, not claims that I executed each original repository script verbatim.

| Requested script | What I ran or inspected | Result |
|---|---|---|
| cube_sixty_degree_look.py | Independent reproduction of integer-cube geometry and the stated transformations | Agrees with the recorded 12 squares, three straight pairs, and symmetry table. Found an omitted dependence on rotation center. |
| zero_total_rule_reach_n18.py | Independent enumeration of four-regular bipartite incidence matrices and class-level permitted switches | Agrees: 26 classes total; nine \(S=N\) classes; one connected restricted component. Does not generalize to all sizes or stricter square caps. |
| front_push_step.py | Independent continuum reflection and momentum calculation | Agrees numerically at every recorded frequency and with the closed form. Does not validate the interpretation as photon pressure on the lattice front. |
| opened_space_curvature_sign.py | Source and log inspected; original execution unavailable without the saved T51 graph archives | Not independently reproduced. Recorded counts are 519 positive, 80 zero, one negative, mean approximately \(+9.2\). Conclusions must be limited to the older saved-run ensemble. |

A representative extract of the independently reproduced wave-step values is:

| Frequency \(\omega\) | Reflected fraction | Transmitted fraction | Calculated push / open-side momentum |
|---|---|---|---|
| 2.05 | 0.4096 | 0.5904 | −0.2810 |
| 2.20 | 0.1696 | 0.8304 | −0.3431 |
| 2.50 | 0.0625 | 0.9375 | −0.3000 |
| 3.00 | 0.0213 | 0.9787 | −0.2175 |
| 4.00 | 0.0052 | 0.9948 | −0.1244 |
| 6.00 | 0.0009 | 0.9991 | −0.0555 |
| 10.00 | 0.0001 | 0.9999 | −0.0200 |

Disagreement with the record: The independent calculations find no material arithmetic disagreement in the three
reproduced investigations. The disagreements are in what those calculations are said to prove. The original
curvature-sign investigation remains a reproducibility gap in this environment.

The original repository sources examined include VISION.md, the notebook, the questions file, and the sandbox log.

## 4. Missing published work

I looked at the 25 October updates, their cited reading notes, and the relevant bibliography additions—not every
reference anywhere in the repository. The following are missing or underused in those explanations, not claims that the
works are absent from the entire project.

| Published work | Why it matters here | Verification status |
|---|---|---|
| Tullio Regge (1961), "General Relativity Without Coordinates" | A direct precedent for defining curvature on discrete geometric structures. It gives a much more appropriate benchmark for whether the toy's square-count defects approximate geometric curvature. | Publication and scope checked at publisher. |
| Thomas Banchoff (1967), "Critical Points and Curvature for Embedded Polyhedral Surfaces" | Relevant discrete Gauss–Bonnet mathematics, including the significance of an actual embedded polyhedral surface. The embedding assumptions are precisely what the current graph argument omits. | Bibliographic details and application to verify against full source. |
| Yann Ollivier (2009), coarse Ricci curvature for metric spaces; Robin Forman (2003), combinatorial Ricci curvature | Established ways to assign curvature-related quantities to discrete spaces without simply equating four-cycle count with classical curvature. They may expose which definition the hypothesis needs. | To verify for applicability to this graph family; neither automatically identifies the proposed curl with Ricci curvature. |
| Holger Nielsen and Masao Ninomiya (1981), lattice fermion no-go theorem | Essential when proposing that handed twists on a lattice produce chiral fermions. Under common assumptions, lattice constructions encounter unwanted left/right species doubling. A proposed electron mechanism needs to say which assumptions apply. | The theorem's scope checked against publication abstract. |
| Stephen Coleman (1977); Sidney Coleman and Frank De Luccia (1980), false-vacuum decay and gravitational bubble nucleation | Standard mathematical starting points for bubble formation and expansion. They provide an actual framework for defining a moving wall, rather than inferring its dynamics from \(R=ct\). | To verify from primary texts for this specific comparison. |
| Werner Israel (1966), junction conditions for thin shells in general relativity | Particularly relevant to the proposed charged shell and an interface between different spacetime regions. It forces the interface's stress-energy and geometric matching conditions to be stated. | To verify against the original work and its assumptions. |
| Alan Guth and Edward Farhi (1987); Farhi, Guth, and Guven (1990), child-universe formation | More directly relevant to black-hole-connected daughter universes than an analogy with a CPT-symmetric universe. Their assumptions and obstacles deserve comparison before calling the proposed split a novel mechanism. | To verify in primary papers. |
| Andrei Sakharov (1967), baryogenesis conditions; Masataka Fukugita and Tsutomu Yanagida (1986), leptogenesis | The record already recognizes Sakharov's conditions, but needs a sharper distinction between creating a matter excess and separating two initially balancing populations. These references clarify what must be conserved and what symmetry violation is required. | Sakharov framework cross-checked with published reviews; detailed application to verify. |
| A. Vilenkin (1978), "Parity Nonconservation and Rotating Black Holes" | Particularly close to the owner's intuition about rotation, handedness, and directional neutrino/antineutrino emission. The 1978 original should be cited distinctly from its 1979 erratum and follow-up. | Verified at the publisher. |
| Bödeker and Moore (2009, 2017), read as a pair | The contrast between possible runaway walls in 2009 and transition-radiation speed limits in 2017 is the relevant published lesson. The record presently merges them into a stronger, partly opposite claim. | Both abstracts checked. |

The most constructive mathematical comparisons are Regge's discrete geometry, genuine combinatorial Gauss–Bonnet with
explicit embeddings, and established lattice-fermion constraints. For the cosmological front, junction conditions and
bubble-wall dynamics are more directly applicable than the current loosely combined analogies.

Final judgment: Keep the zero-total square-count rule as an explicitly new, testable restriction; keep the correctly
reproduced finite calculations; and preserve the owner's language as hypotheses. Withdraw the one-vertex growth claim,
the asserted Gauss–Bonnet equivalence, and the claim of an exact photon-pressure result until the underlying
mathematical objects and field modes have been defined consistently. Those corrections would make the research record
substantially more reliable without requiring any change to the owner's exploratory ideas.

# Codex report on the record of 28 October 2026 (saved verbatim from the owner's paste, 28 October, 15:48 UTC; recorded as ASSUMPTIONS O166)

# Independent physics audit — 28 October 2026

Repository: RecreationalPhysics\
Commit: `4c1e01419f95d63af5f9d8150c5ec876f90c06a0`\
Reference: [Codex audit brief](https://github.com/EmilySmithCreate/RecreationalPhysics/blob/4c1e0141/docs/reviews/2026-10-28_codex_audit_brief.md)

Scope: Read-only, skeptical review of the particle rules, link-length gravity, T83, and the associated claims. Findings below distinguish mathematical checks from physical interpretations. Independent analysis in this report is Ours, unverified, pending further review.

## Findings, ranked by significance

### 1. Critical — The link-length gravity energy has an uncontrolled scale mode

Files: `docs/design/gravity_link_brief.md:37–49`; `src/graphity/lengths.py:2–15`

The proposed energy includes Ollivier curvature evaluated using variable link lengths, together with a source term proportional to the local absolute curl.

There is an exact obstruction to unconstrained relaxation.

If every link length is multiplied by the same positive factor s, all shortest-path distances and optimal transport costs are multiplied by s. Consequently,

κ_e(sℓ) = 1 − sW_e/(sd_e) = κ_e(ℓ).

The curvature energy is therefore unchanged by uniform rescaling.

But the source term is not. Starting from reference lengths, uniform scaling gives

ΔH_source = α(s − 1) Σ_e |c_e|.

For any nonzero curl:

- If α < 0, the energy decreases without bound as s → ∞.
- If α > 0, the energy decreases as s → 0⁺, approaching the boundary of positive link lengths.
- Neither case has an unconstrained, finite stationary point along this direction.

Verdict: The proposed full energy does not yet define the finite relaxed geometry claimed in `lengths.py`. Removing the zero mode with a pseudoinverse produces a mathematically defined constrained solution, but the constraint has not been derived from the proposed physical dynamics.

The quadratic Green-function calculation remains useful as a conditional mathematical model. Its identification as emergent gravity does not follow without fixing this problem.

### 2. Critical — The particle spin rule contradicts observed charge and spin assignments

File: `docs/design/twist_curl_rules_2026-10-27.md:30–46`, with the 28 October spin interpretation at lines 146–149.

The stated rules identify net loop twist with integer electric charge and spin angle with half the net twist angle. Taken literally, they make spin depend on the same net winding that determines charge.

That immediately gives conflicts:

| Particle     | Electric charge | Observed spin | Problem with the rule                              |
| ------------ | --------------- | ------------- | -------------------------------------------------- |
| Neutron      | 0               | ½             | Zero net twist cannot supply its half-integer spin |
| Charged pion | ±1              | 0             | Unit net twist gives a half-integer, not zero      |
| Photon       | 0               | 1             | Zero net twist does not supply spin one            |

This is not a numerical uncertainty or an issue of lattice resolution. It follows from combining the two proposed definitions.

Verdict: The spin rule cannot describe the observed particle spectrum as written. Spin needs a degree of freedom or construction not rigidly identified with net electric charge. A topology-based spin mechanism would also need to distinguish spatial rotations from internal winding.

### 3. High — T83 scores LONG, but does not establish long-range transmission of curl

Files: `PREREGISTRATION.md:7830–7859`; `results/t83_curl_corr_stage1.csv`; `src/graphity/correlation.py:1–19`

The preregistered criteria are clear: a surviving, fluctuating sheet with C(3) > 0.05 by more than twice its reported standard error qualifies as LONG.

One qualifying result is: T83 stage 1, λ = 1.02, 32 × 32, g = 3, replica 1: C(3) = 0.07754, reported error 0.00255, minimum flat share 0.99219.

The cell passes both scoring gates. Its C(3) exceeds the threshold by approximately 10.8 reported standard errors. Therefore the registered stage-1 verdict is LONG, not SHORT.

But the interpretation is a separate issue.

`correlation.py` correlates fluctuations in local square counts at graph distance r. A localized defect changes the square counts in a neighborhood of several vertices. Correlations between those vertices can remain positive at distance three without anything physically propagating through the surrounding flat sheet.

Independent numerical check: I constructed a separate 32 × 32 periodic square lattice, performed one degree-preserving switch between widely separated links, recomputed the square counts, and evaluated the same normalized correlation definition using all vertex pairs at graph distance three.

Results: flat-edge share approximately 0.99316; C(3) approximately 0.13799; no thermal chain or long-range field was involved.

This independently demonstrates that a single isolated switching event can produce a value larger than the registered LONG threshold.

Verdict: T83's LONG result is correctly scored but cannot, by itself, distinguish a defect's geometrical footprint from a transmitted gravitational influence. The wording of the preregistration makes that distinction essential.

A better test would fix or condition on the source defect, measure the connected response outside its footprint, and compare with a null model containing noninteracting localized defects.

### 4. High — The quadratic stiffness is reproducible, but its physical interpretation is conditional

Files: `sandbox/regge_step1_stiffness.py:3–17, 51–67`; `src/graphity/lengths.py:2–15`

I checked the definition against Trugenberger, Networks as the fundamental constituents of the universe. Section II.2 defines the curvature using uniform neighbor measures, optimal transport, and the ratio of Wasserstein distance to graph distance. The script implements that definition for weighted graph distances. The variable-length extension, however, is not an independently validated Regge action.

I then independently reconstructed the six-neighbor torus calculation using shortest-path distances and a minimum-cost matching of the neighbor sets, without using the repository's linear-programming routine.

For one perturbed link of length 1 + δ, the local result is ΔH = 12δ²/(1 + δ). For two adjacent, parallel links both changed by δ, the mixed energy is ΔH_mixed = −4δ²/(1 + δ). These give the advertised local Hessian coefficients K_ee = 24, K_ef = −4 for a neighboring parallel link. My independent numerical checks agreed for positive and negative perturbations from 0.01 to 0.2.

That supports the local stiffness calculation. It does not settle three issues:

1. The finite-difference Hessian describes a particular neighborhood of the flat geometry. Changes in shortest paths and optimal transport plans can create different branches elsewhere.
2. The curvature functional is dimensionless and scale invariant. Unlike a conventional Regge action, it does not include the appropriate hinge-volume weighting. Adding such weights changes the variation and may change the inferred stiffness.
3. A zero eigenvalue of a local stiffness matrix does not automatically establish a stable, propagating gravitational field. The global scale instability in Finding 1 still applies.

Verdict: The local numerical result is credible. The claim that it independently establishes physical gravity is not.

### 5. High — The claimed attraction is not universal, even within the implemented model

Files: `src/graphity/lengths.py:3–24, 53–76`; `sandbox/relaxed_lengths_pull.py`; `docs/design/gravity_link_brief.md`

The repository's quadratic model uses three independent lattice Laplacians, one for each direction of link. Its pseudoinverse gives a Green function G. For two positive sources in the same link family, the interaction term is E_int(r) = −α² q₁q₂ G(r).

I independently evaluated the exact finite-torus Fourier sum on a 16 × 16 × 16 lattice, using the stated stiffness K = 4(6I − A). [A chart of G along one axis, r = 1 to 8, was included: positive near the source, changing sign at separations seven and eight.]

The positive near-source interaction does have the attractive sign expected in the quadratic model. But at separations seven and eight, the mean-zero Green function changes sign. Also, two sources assigned to different link families have zero cross interaction, because the stiffness has no coupling between families.

A periodic, mean-zero Green function need not reproduce infinite-space attraction at every separation; the sign reversal is not itself proof that the short-distance calculation is wrong. It does disprove an unqualified claim of universal attractive interaction in the finite model.

The published comparison with a point-source Newtonian shape is also not an independent physical prediction. Both curves use the same prescribed lattice Green-function structure. No two-relic trajectory, dynamical force measurement, or gravitational equivalence-principle test has been established.

Verdict: Short-distance, same-family attraction is a valid feature of the constrained quadratic model. Universal gravitational attraction is not established.

### 6. High — The isotropy comparison tests assumed distance formulas, not the derived gravity field

Files: `sandbox/gravity_carrier_isotropy.py:0–38`; `docs/design/twist_curl_rules_2026-10-27.md:138–140`

The three comparison arms are different mathematical constructions:

| Arm          | Assumed potential                 | What it actually tests                                       |
| ------------ | --------------------------------- | ------------------------------------------------------------ |
| Point scalar | Discrete Laplacian Green function | Long-wavelength response of a local Laplacian                |
| Link count   | 1/d_Manhattan                     | Direction dependence imposed by link-count distance          |
| Link lengths | 1/d_weighted                      | Direction dependence imposed by a fixed shortest-path metric |

The link-count arm necessarily yields a face-diagonal-to-axis ratio 1/√2 and a body-diagonal ratio 1/√3. This follows directly from the chosen definition of distance; it is not a newly derived gravitational prediction.

More importantly, the actual link-length stiffness in `lengths.py` is itself a discrete Laplacian on link positions. Each family therefore has a long-wavelength, approximately rotationally symmetric Green function. A field living on links need not obey the 1/d_Manhattan potential used for the link-count comparison.

Verdict: The calculation is useful as a diagnostic of two distance conventions. It cannot establish that link-carried gravity has a permanent directional discrepancy, or that only a point-carried field can become isotropic.

Physical constraints also need to match the observable being tested. An experimental limit on the directional dependence of the speed of light is not, without additional theory, the same as a limit on the directional dependence of gravity.

### 7. High — The gravity code omits the diagonal geometry central to the proposal

Files: `docs/design/gravity_link_brief.md:9–19, 35–60`; `src/graphity/lengths.py:20–24, 33–50`; `sandbox/relaxed_lengths_pull.py:97–110`

The proposed geometry includes face, body, and box diagonals with lengths √2, √3, √6. The owner specifically connects these to rigidity, particle twist, and the paths followed by light.

The implemented calculation instead uses a six-neighbor cubic graph. It has three axis-link length fields. Rewired edges are assigned to whichever axis family is closest by a bookkeeping rule. The `light_path` routine explicitly searches axis links only.

Consequently, it does not vary actual face or body diagonal lengths, impose geometric consistency between diagonals and sides, or test the owner's proposed diagonal light paths.

Verdict: The calculation does test a simpler link-field model. It does not yet test the full geometry described in the brief. Adding true diagonal degrees of freedom could change both the Hessian and its spectrum; the present positive result should not be assumed to survive that extension.

### 8. High — The polygon calculations reveal a particle-construction obstruction

Files: `sandbox/proton_loop_fold.py:0–15, 22–25, 77–93`; `sandbox/LOG.md:650–652`

A box-diagonal step is a permutation of (±1, ±1, ±2). Every such step changes x + y + z by an even integer. Therefore the checkerboard parity of its endpoints is always equal.

It follows without a numerical simulation that every connected loop formed solely by these diagonals remains on one checkerboard colour.

If a proton's three strands are meant to be a single end-to-end box-diagonal loop containing two strands of one colour and one of the other, that construction is impossible under the stated geometry. An assembly around a common square can contain both colours, but that is a different connectivity rule and requires its own specification.

The writhe routine uses the Gauss integral on nonadjacent straight segments. That is a legitimate way of calculating a polygon's geometric writhe. But writhe is generally a real-valued geometric quantity, not a quantized particle mass or spin by itself. The classical ribbon relation Lk = Tw + Wr requires a ribbon framing to determine twist and linking; a midline polygon alone does not supply those quantities.

A Möbius-band relation with twice the writhe can be meaningful under specialized conventions, but the cited formula needs the exact definition and normalization of its quantities. The 2023 Möbius-band treatment I checked is formulated with explicit geometric hypotheses; it is not a universal license to identify loop writhe with particle mass.

Verdict: The one-colour obstruction is exact. The recorded enumeration is plausible but I did not independently reproduce every loop count or the full numerical writhe distribution. Neither those counts nor the Gauss integral establishes proton mass, spin, or confinement.

### 9. Medium — The held-out L = 10 check is weaker than its label suggests

Files: `docs/design/gravity_link_brief.md:70–76`; `VISION.md:1850–1851`; `CLAUDE.md:36–37`

The repository reports a successful prediction at L = 10: the isolated-link and nearest-parallel-link energy coefficients match L = 6 and L = 8.

That agreement is real but relatively weak evidence. The interactions had already been found to have range one on L = 6. Once the local transport configuration is identical and the system is larger than that neighborhood, the same coefficients are expected.

Moreover, the predicted L⁻² spectral gap follows algebraically after assuming the exact lattice-Laplacian form. It is a prediction of the fitted stiffness matrix, not an independent demonstration that the nonlinear length-relaxation theory has a stable continuum limit.

Rule 14 verdict: L = 10 supplies a useful implementation cross-check. It is not a strong held-out test of the physically important size claim.

The more discriminating prediction would concern an independently computed finite-size response, nonlinearity, or force observable not fixed solely by the already-known nearest-neighbor coefficients.

## Audit of the record and research rules

### 10. High — Rule 10 is not consistently respected in the interpretation of the gravity result

Files: `VISION.md:1850–1855`; `docs/design/gravity_link_brief.md:72–90`; `CLAUDE.md:27–29, 40–41`

The central physical conclusions need separate classifications.

| Statement in the 28 October record                           | Audit classification                                                                                                          |
| ------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------- |
| Single-link curvature energy is 12δ²/(1 + δ)                 | Exact, for the specified graph and variation                                                                                  |
| The local stiffness is 4(6I − A) per link family             | Exact local calculation, subject to the transport branch and model definition                                                 |
| Flat geometry is a minimum                                   | Conditional; there are zero modes, and adding a source destabilizes uniform scale                                             |
| The source creates a 1/r-like response                       | Conditional mathematical inference from the constrained quadratic model                                                       |
| Reach emerges without anything put in                        | Interpretation, Ours, unverified; a source coupling, mean constraint, and instantaneous relaxation are additional assumptions |
| Two relics experience Newton-shaped gravitational attraction | Interpretation, Ours, unverified, and not established universally by the finite-torus model                                   |
| Light experiences Shapiro delay                              | Not demonstrated; a path-length increase is not yet a relativistic clock or light-propagation calculation                     |

Rule 10 explicitly distinguishes arithmetic from interpretation. A dated entry is present, but the wording exact in Update 136 extends beyond the parts that have actually been proved.

Rule 16 also prohibits using a sandbox look to crown a positive physical claim. The gravity result is correctly described as exploratory in the sandbox record, but its subsequent interpretation in `VISION.md` is stronger than that status permits. The failed initial prediction and the uncoupled link families are, to the record's credit, disclosed rather than concealed.

Verdict: Retain the exact local calculation. Reclassify the physical gravity and light claims as conditional interpretations, pending fresh registered tests.

### 11. Medium — Rule 11 and the T83 failure are partly handled well, but the scientific question remains open

Files: `ASSUMPTIONS.md:4769–4777`; `PREREGISTRATION.md:7860–7861`; `CLAUDE.md:30–31`

The record correctly preserves the failed prediction and reports LONG. It also identifies the defect-footprint problem rather than silently changing the outcome. That is good practice.

There are two qualifications.

First, the phrase Rule 11's four answers refers to the older version of the rule. The operative rule was shortened on 11 October to require the cheapest discriminating calculation before a replacement enters the strict lane. The four written answers are useful, but no longer the rule's formal requirement.

Second, the proposed replacement gate—stationary cells with at least 20 defects and a footprint-subtracted correlation—is data-informed. It must be treated as a new analysis and tested on fresh data, not used to rewrite T83's original result.

There is a deeper possibility: the accessible regime may not contain a stationary, warm, flat sheet with sufficiently many defects. The current results show cells that barely move and cells that begin to melt. Calling the scoring gate an assistant error does not resolve whether the intended equilibrium state exists.

Verdict: T83 remains LONG under its original rules, and inconclusive as evidence for transmitted curl. The first new test should establish the existence and stationarity of the proposed sheet regime before attempting another correlation verdict.

### 12. Medium — The owner's decisions are mostly traceable, but the revised T84 mechanics are over-attributed

Files: `sandbox/NOTEBOOK.md:2761–2764, 2869–2875`; `PREREGISTRATION.md:7883–7888`

I compared the recorded verbatim messages with the assistant's subsequent descriptions.

- Sign by colour: Faithful. The owner explicitly approved taking the twist's sign from the diagonal's colour. That does not establish that the sign rule describes real particle charges.
- Step 2 with uncoupled link families: Faithful. The owner explicitly said it could run that way first, with coupling considered later.
- Adjust my prediction: The owner authorized an adjustment for consistency but did not specify the complete replacement mechanics. The choice α < 0, replacement of the shorter-path response by a total-energy Metropolis rule, and the combined CLOSES/DELAYED prediction were formulated by the assistant.

That third item matters because changing the acceptance energy changes the model, not merely the predicted outcome. The adjustment may be reasonable as an assistant proposal, but the exact choices should not be represented as independently specified or separately confirmed by the owner.

Verdict: Mark T84 Amendment 1 as assistant-formulated at the owner's request, awaiting confirmation of its specific mechanics. Preserve the original owner prediction and the original response rule in the historical record.

## Additional independent numerical check: polygon writhe

To check the polygon method without running the repository script, I constructed the following nonplanar five-edge loop of allowed box diagonals: (0,0,0) → (−2,−1,−1) → (−4,−2,−2) → (−3,−3,0) → (−2,−1,1) → (0,0,0).

I integrated the five nonadjacent segment pairs using an independent adaptive two-dimensional quadrature, rather than the repository's subdivided Gauss–Legendre implementation. The result was Wr = 0.123375857214425. A separate fixed-order quadrature calculation agreed to approximately 14 decimal places. This confirms that the Gauss-integral construction yields a nonzero, non-quarter-integer geometric writhe for an allowed lattice loop. It reinforces Finding 8: the writhe calculation can be mathematically valid without making fold a quantized physical charge, mass, or spin.

## Comparison with the project's own conclusions

After examining the downstream record, my assessment is:

- Agreement: The local link stiffness is reproducible, the three link families are uncoupled in the computed model, T83 formally scores LONG, and one isolated defect can explain its positive distance-three correlation.
- Disagreement: An unconstrained finite relaxed length field has not been obtained; the finite-torus interaction is not attractive at every separation; the isotropy comparison does not establish a general limitation of link-carried fields; and the particle spin formula has immediate conflicts with observed particles.
- Qualifications: The project's own record acknowledges several problems, including the T83 footprint and lack of demonstrated relic motion. Those disclosures are important, but the stronger positive claims still need to be narrowed.

## What I could not verify

The strict Part A blind-reading protocol was not fully preserved. Some prefatory text and search results exposed downstream conclusions before I had completed every independent calculation. The numerical checks above were independently implemented, but this should not be represented as a completely blinded audit.

I inspected the pinned repository files online, but could not establish a working local clone. Therefore I did not run `pytest`, the full `regge_step1_stiffness.py` program, or the repository's complete polygon enumeration. I also did not independently verify every T83 trajectory, the exact Denne–Larsen attribution, the full Möbius formula in the intended convention, or the unrun T84 outcome.

For external comparison, the relevant reference standards include the 2026 Particle Data Group Review, the published network curvature model (arXiv:2512.17676) and the Călugăreanu ribbon theorem. A complete confrontation with gravitational Lorentz-symmetry experiments remains outstanding; electromagnetic limits cannot simply be substituted.

## Cheapest decisive next step

The uniform-rescaling calculation in Finding 1 is already the cheapest falsification check, and it exposes a structural problem before any long simulation is needed.

Before promoting another gravity claim, the proposed energy should be made well posed: specify a physical treatment of its scale mode, preserve positive lengths, and check whether a finite nonlinear minimum exists for a nonzero curl source. Then repeat the two-source calculation, including maximum torus separation, cross-family sources, and genuine diagonal geometry. Only after those conditions hold would a registered T84 trajectory test provide meaningful evidence for attraction.

## Overall verdict

The 28 October record contains a credible and interesting local mathematical result, but not a demonstrated theory of gravity or particles. The weighted Ollivier-curvature calculation does produce the reported lattice-Laplacian stiffness near the flat graph, and T83's negative interpretation is supported independently. The decisive limitation is that the proposed source-coupled energy has an uncontrolled scale mode; its advertised gravitational attraction comes from a constrained quadratic pseudoinverse, not a proven finite physical relaxation. The particle rules also fail elementary charge–spin comparisons, while the diagonal geometry central to the proposal is missing from the implemented gravity model. The best scientific outcome is to preserve the reproducible calculations, explicitly downgrade the physical interpretations, and resolve these mathematical obstructions before additional simulation or claims of agreement with reality. Ours, unverified.

# Independent audit of the 24 October 2026 particle-sector record

**Scope:** `EmilySmithCreate/RecreationalPhysics`, **commit `394666205c7ee46e68a609dce3aae1c98db77eb9` only**. Read-only review, 24 October 2026. No repository files, commits, results, or branches were changed. This is an independent review of the requested frozen snapshot, **not a claim that the Codex application was launched**.

**Execution limitation:** I could retrieve the frozen GitHub files through the connected GitHub account and inspect their prior commit history, but the scratch computer could not clone GitHub (`Could not resolve host`). Consequently, I **did not run** `pytest tests/test_u1.py` or the repository's own sandbox scripts. I did run a separate Python reconstruction of the graph and field matrices, exact Bessel-function sums, winding tests, and arithmetic. Findings distinguish what was checked independently from what was only inspected in source or saved results. The report is therefore **substantial but not a complete execution audit**.

## 1. Summary

1. **Keep the U(1) code, but correct a false winding-move guarantee:** its symmetric Metropolis proposal is sound; an attempted instanton addition does *not* always change topological winding by exactly one.
2. **The third reproduction gate met its precommitted numerical thresholds, but that does not erase two failures.** Eight of ten final estimates lie high; independent multi-seed validation remains warranted.
3. **The exact 2D torus formula and local field equations check out.** The side-four mass formula also survives an independent small-lattice spectral check.
4. **Do not say physical light has been shown to lower curling costs or refold space.** The result is a leading term in an equilibrium field partition function, not a photon-population or refolding calculation.
5. **Correct the O151 scope:** the massive mode is a scalar seen from the open directions, not light; no actual curled/flat boundary was simulated.
6. **Fix recordkeeping:** the current questions file still repeats the withdrawn bound-photon origin of electron charge, and an inferred boundary prediction was credited to the owner before confirmation.
7. **Add missing prior work:** a 1994 U(1)-plus-dynamical-gravity study and Levin–Wen's emergent-photon/fermion rotor model are especially relevant.
8. **Particle properties remain assigned rather than derived.** The present twist count does not derive spin-½, statistics, confinement, QCD color, mass or antimatter asymmetry.

## 2. Findings

### 1. The field's code

**F1.1 — The core fixed-graph equations are internally consistent. [High confidence]**

**Where:** [`src/graphity/u1.py`](https://github.com/EmilySmithCreate/RecreationalPhysics/blob/39466620/src/graphity/u1.py), `links`, `squares`, `Field.__init__`, `force`, `charge`, `delta_action`, `_metropolis`.

**Finding:** I found no incorrect edge sign or missing derivative in the fixed-graph code. Orienting every link from kind 0 to kind 1 is legitimate. For each recorded square the coefficients `[+1,−1,+1,−1]` produce an oriented loop; `B divᵀ = 0` expresses gauge invariance; the potential's force is `−κ Bᵀ sin(Bθ)`; and every internal link's contribution cancels in the sum of the Gauss-law charges. The local Metropolis action difference correctly uses only squares incident to the changed link.

**How checked:** Independently reconstructed periodic bipartite torus graphs and their link–vertex and square–link incidence matrices. On the 6×6, 10×10, 4×8 and 4×8×8 examples, `B divᵀ` was identically zero. The one-link proposal is uniform and symmetric, and the local accept/reject step follows the requested Boltzmann weight. The velocity-Verlet force matches the gradient of the stated potential by differentiation. **Qualification:** I did not execute the repository's Numba kernel. The field allows arbitrary real charge initial data; it does not derive quantized particle charges or implement dynamical charged matter.

**F1.2 — The `instanton` winding claim is false as a universal statement. [High confidence]**

**Where:** `Field.instanton` and `Field.metropolis` docstrings and `test_square_signs_and_winding`.

**What is wrong:** The file claims a global proposal `θ → θ ± instanton` *changes the winding by one*. It does so for the constructed instanton alone and for sufficiently smooth starting holonomies. For a generic field, plaquettes crossing the `±π` wrapping boundary can change the recorded integer by more, by less, or in the opposite direction. The existing unit test explicitly conditions its assertion on *no such crossings*, so it does not establish the unconditional claim.

**What is right:** The proposal remains **symmetric**, because `+instanton` and `−instanton` are equally likely inverses on the periodic link-phase space. Accept/reject using the full action therefore preserves detailed balance. It is better described as a **topology-changing proposal**, not an exact `Q → Q±1` operation for every state.

**How checked:** In 500 independently generated random phase fields on the 6×6 torus, adding the positive instanton changed winding by `+1` in 183 cases, `0` in 189, `−1` in 96, `−2` in 26 and `−3` in 6. On 10×10, the corresponding counts were `+1`:187, `0`:178, `−1`:86, `−2`:34, `−3`:13, `−4`:2. The integer was computed by wrapping square holonomies and applying the alternating orientation signs. These are **proposal-level** checks, not measurements of accepted moves at equilibrium.

**F1.3 — Some tests establish less than their names suggest. [High confidence]**

**Where:** [`tests/test_u1.py`](https://github.com/EmilySmithCreate/RecreationalPhysics/blob/39466620/tests/test_u1.py), especially `test_square_signs_and_winding`, `test_gate_u1_short`, `test_evolution_conserves_energy`.

**What is wrong/right:** A short Monte Carlo chain can pass an approximate 5-error test despite sector freezing or uncertainty misestimation; energy conservation over one initial condition does not prove all dynamical constraints; and the winding test only checks ±1 conditionally. A fixed-order sweep **preserves** the target distribution, but, unlike an individual symmetric proposal, a whole deterministic ordered sweep is not generally itself reversible. The module's description correctly says the sweep leaves the weight invariant; it should not silently promote that property to sweep-level detailed balance. Add explicit tests for a generic winding proposal, gauge-charge conservation under evolution, and global-move acceptance/mixing. This is a coverage gap, not evidence the accepted Metropolis move is biased.

### 2. The exact answer used as the gate

**F2.1 — The character-expansion answer is correct for the stated ordinary 2D tori. [High confidence]**

**Where:** `exact_mean_cos_2d`; `u1.py` module explanation; Gate U1.

**What is right:** For a two-dimensional periodic lattice whose faces are just its elementary plaquettes, there is one oriented relation among plaquette angles. The square orientation signs can be absorbed by `n → −n` because `I_{−n}(β)=I_n(β)`. With `P` faces,

`Z = Σ_n I_n(β)^P`, and `⟨cos φ⟩ = [Σ_n I_n(β)^(P−1) (I_(n−1)(β)+I_(n+1)(β))/2] / Z`.

I independently evaluated the formula at β=8: **0.9366115384048215** for `P=36`; **0.9352577250493289** for `P=100`, matching the saved gate targets. These are not the infinite-volume values.

**Caution:** The default fixed truncation `n_max=60` should be bounded or made adaptive if used at couplings much larger than the tested range. The simple single-constraint formula must **not** be reused unchanged for the 4×L curled tube, where the program counts additional 4-cycle faces and the left null space of `B` is larger.

### 3. The gate sequence

**F3.1 — The acceptance thresholds really were committed before each run. [High confidence]**

**Where:** [`TASKS.md`, 24 October section](https://github.com/EmilySmithCreate/RecreationalPhysics/blob/39466620/TASKS.md); gate CSV files in [`results/`](https://github.com/EmilySmithCreate/RecreationalPhysics/tree/39466620/results); pre-target GitHub commit history.

**Evidence:** `059b9741` registered U1 before its results were added by `6c74e4ff`. `2903791c` registered U1′ before `831ed6d0` stored its results. `04e6f845` registered U1″ before `9c47395d` added its results. The criterion stayed **all ten points within 3.5 estimated block errors**, with the finite-torus and local-acceptance checks. That is a genuine safeguard; this was not a post-hoc relaxation of a threshold.

**F3.2 — The successful third gate is conditional evidence, not a clean three-attempt reproduction. [High confidence on history; medium on statistical interpretation]**

**Where:** Same files. The original U1 missed on 6×6, β=8 by **3.94 errors**, and 10×10, β=8 by **11.50**; its local sampler was observed to freeze in the initial winding sector. U1′ used the global move and missed one point, 10×10, β=8, by **3.648 errors** against the 3.5 cutoff. U1″ used new seeds and four times the measurement sweeps; its largest deviation was **2.476**, so it *passed its precommitted gate*. All failures were preserved.

**What to fix in the reading:** Report the gate as *“passed on the third, longer test with the topology-changing sampler; independent reliability remains to be assessed.”* Do not imply that U1″ retrospectively makes U1 and U1′ passes, or proves absence of small bias. It is fair that a code change and a diagnosis justified retesting after U1. For U1′, a lone marginal miss among ten points can be a chance event, but a sequence stopped after the first pass is still vulnerable to selection.

**F3.3 — The eight-high pattern deserves explicit follow-up. [Medium confidence]**

Eight of ten U1″ estimates lie above the exact answers. Taking the saved signed standard-error scores at face value, their sum divided by `√10` is **+2.643**, a nominal two-sided normal-tail probability near **0.008**, assuming independent calibrated errors. This calculation is **exploratory**, and the ten block-error estimates are not an independently validated covariance matrix. The separate sign count alone is weaker: eight or more positive signs occur **5.47%** of the time under independent fair signs. Neither establishes bias, but the directional agreement should not be brushed away as merely a pleasant pass. Perform a predeclared, new-seed comparison of average signed residual and repeated-chain coverage before using this sampler for precision claims.

### 4. O151 and its correction: light in a curled direction

**F4.1 — The mass formula checks out as a property of *this* lattice action. [High confidence]**

**Where:** [`ASSUMPTIONS.md`, O151](https://github.com/EmilySmithCreate/RecreationalPhysics/blob/39466620/ASSUMPTIONS.md), `test_bloch_formula_with_side_four_rings_gives_the_whole_spectrum`, `sandbox/u1_curl_mass_general.py`.

On a side-four direction, the path around the full circumference is itself one of the program's four-link squares. Its extra energy term creates a frequency gap for the *link component along the curl*. For a wave traveling along an uncurled direction, the mode has `ω²=4+4sin²(k/2)` while a transverse mode wholly in the open directions has `ω²=4sin²(k/2)`, given unit inertia and κ=1. The general momentum-space matrix displayed in the source has the expected form, with an added `+4` on a curled component only for momentum zero around that component. On an independently constructed **4×8** graph, its full eigenvalue spectrum matched direct diagonalization to **5.33×10⁻¹⁵**. I did not run the source's six-case pytest or ten-case sandbox sweep.

**F4.2 — The corrected particle label is right, but two descriptions are too strong. [High confidence]**

Seen from the open directions, the curl-directed zero mode behaves as a **Wilson-line scalar**, not a second polarization of the ordinary photon. The correction in O151 is important and right. But (a) O151 says the **6×8×8 and 8×8×8 lattices have “the same spectrum.”** They have different numbers of vertices, links and allowed momenta and cannot have identical full spectra; they share the **same flat-lattice dispersion relation** for comparable momenta. (b) No actual interface between a flat and curled region was built. Reflection, passage unchanged, and any interaction of light with charged matter are **not** established by the homogeneous torus spectral calculation. The short-wavelength lattice photon still has direction-dependent dispersion even where the long-wave speed agrees.

### 5. The exact looks

**F5.1 — The main bookkeeping facts checked independently are sound, within their stated geometry. [High confidence]**

**Where:** `sandbox/particle_handoff_looks.py`, `sandbox/strand_answers_look.py`, `sandbox/diagonal_112_look.py`, `sandbox/strip_corner_and_ring_energy.py`, `sandbox/u1_graph_free_energy.py`, and `sandbox/LOG.md` for 24 October.

The independent reconstruction gives **36 faces on a 6×6 flat torus**, **100 on a 10×10**, **40 on a 4×8** (eight extra circumference rings), and **832 on a 4×8×8** (768 regular plaquettes plus 64 circumference rings). The 4×8 graph has **eight** square-surface null modes, while the flat 6×6 and 10×10 each have **one**. In a **2×2×2** cube block there are **48** unoriented (1,1,2)-type diagonals; in **2×2×3** there are **80**; all join vertices of the same parity. The Euclidean lengths `√2`, `√6` and `√18=3√2` and the parity claims agree. The quoted circular bending energies from the *assumed formula* `2π²B/L` are **13.9577B** at `√2`, **8.8276B** at `√5`, and **8.0585B** at `√6`. Standard cubic-lattice rotational axes have orders four along an edge, two along a face diagonal, and three along a body diagonal. The modulo-three table `3Q+t ≡ 0 mod 3` holds for its chosen observed charges.

**F5.2 — The charge census is not a confinement or particle result. [High confidence]**

**Where:** `particle_handoff_looks.py`, charge section; first brief, exact looks.

The script's 531,441 configurations enumerate labels on a **2×3 periodic grid**, which is not one of the toy's ordinary admissible bipartite even-sided tori (and its two-site periodic direction needs special handling if treated as a simple graph). The reported **243 possible source patterns** are plausible and follow more generally from the rank of an incidence matrix over `Z3` on a connected graph. That is a useful **neutrality counting identity**, not a demonstration that thirds are confined, that they form only physical mesons and baryons, or that `Z3` is the Standard Model's `SU(3)` color interaction. A far-separated plus/minus pair is allowed by the same count; no separation energy was computed.

**F5.3 — Geometric illustrations are sometimes described as physical consequences. [High confidence]**

The continuum-elastica bending constant **B**, twist constant **C**, and even the physical ribbon framing are not present in the rigid graph Hamiltonian. The script's comparison of strips is therefore a **conditional illustrative calculation**, not a measured energy difference between particles. Likewise, three unoriented planes 60° apart through a cube body diagonal do not, by themselves, specify how a framed ribbon twists along a *closed curve* or make it Möbius. The later statement “an explicitly closed strip with an odd number of half-turns is one-sided” is correct, but the strip and its full twist must actually be defined. The first pulse simulations supply observations for **chosen launches**, not proof that every possible “half-curl” is immobile. The 2π rotation check shows classical link labels return to themselves; it does not settle what a future quantum state could do.

**Execution status:** These assessments combine independent matrix and arithmetic checks with reading the source and saved log. I could **not** rerun the full individual source scripts. Claims about their exact runtime output, such as the 531,441-state enumeration and all long cycle lists, remain **source-inspected, not independently executed**.

### 6. The claim that light lowers curling cost

**F6.1 — The leading partition-function algebra is correct; its physical name is misleading. [High confidence]**

**Where:** [`docs/design/u1_rewiring_graph_brief_2026-10-24.md`](https://github.com/EmilySmithCreate/RecreationalPhysics/blob/39466620/docs/design/u1_rewiring_graph_brief_2026-10-24.md), `sandbox/u1_graph_free_energy.py`, VISION Updates 100–101.

With normalized integration over phases at each fixed graph, the exact character expansion is `Z_U1(G)=Σ_{n:Bᵀn=0} Π_p I_{n_p}(β)`. The zero-flux contribution is `I₀(β)^P`. A 4×L tube has **N/4 more squares** than a flat N-point sheet, and the quoted bare energy disadvantage is `4(λ−1)N`. Accordingly, the **leading-order** effective-cost translation is

`λ_eff−1 = (λ−1) − (g/16) ln I₀(β)`.

The coefficient `1/16`, the quarter-square count and the factor of `g` are consistent with the conventions written in the brief. Its formal zero for `λ=1.25`, `g=1.5` occurs at **β≈4.2783**. This is independently calculated, **not a measured transition**.

**What is not right:** This integrates over an *equilibrium statistical ensemble of gauge phases*. It does **not** add a specified number of photons or a radiation energy density, propagate light into the network, or demonstrate a time-dependent refolding. Calling it “light lowers the curling cost” presents a field-entropy weight as though it were a photon–geometry interaction already demonstrated. Better: **“Integrating out the compact U(1) field favors graphs with more counted squares at leading order.”** Whether the full coupled model favors the tube requires the still-unperformed exact partition-function comparison and its own dynamics.

**F6.2 — Positive individual expansion terms do not fix the sign of the *relative* correction. [High confidence]**

The ratios `I_n(β)/I₀(β)` are nonnegative for β≥0. Thus omitted terms increase **each graph's** partition function above its own `I₀^P` contribution. But the tube-to-sheet **log-weight difference** receives `log C_tube − log C_sheet`, where both correction factors exceed one; positivity alone does **not** establish that their difference is positive. The tube has many extra closed-square surfaces (16 rather than one at N=64, per source), so its corrections are likely important. The claim that *every correction therefore makes the curling reward stronger* needs a separate inequality or exact comparison and should not be presented as proved.

### 7. Her words against the assistant's readings

**F7.1 — The “kept current” owner-questions summary contradicts the later recorded decision. [High confidence]**

**Where:** [`docs/design/owner_questions_2026-10-24.md`](https://github.com/EmilySmithCreate/RecreationalPhysics/blob/39466620/docs/design/owner_questions_2026-10-24.md), final “Answered on 24 October” paragraph versus its item 1 and VISION Update 101.

The last summary still says **“charge from a bound half-curl for the electron”** as if it remains accepted. The same file's item 1 and VISION Update 101 say that source of electron charge was **withdrawn**, replaced by net signed thirds divided by three. Preserve the historical answer in the dated account, but correct the **current-state recap**. This is a concrete example of rule 17/20 drift, not just a theoretical disagreement.

**F7.2 — The boundary claim has been promoted beyond the owner's quoted words. [High confidence]**

**Where:** VISION Update 100; `owner_questions.md`, item 4; O151.

The owner's recorded words were **“boundary is there is no charge. Maybe it moves on a different plane.”** Update 100 restates that as her prediction that **“light crosses the boundary with no charge to stop it”**. That is a possible interpretation, not a confirmed quotation or unambiguous prediction. The questions file correctly asks her to confirm it, but the VISION reading already attributes it as hers. Change that attribution to **“assistant interpretation — to confirm,”** and do not score it as a passed interface prediction.

**F7.3 — One tentative idea is written more firmly in the decision ledger. [Medium confidence]**

**Where:** VISION Update 101, neutron section. The owner is quoted **“spin with no twist can be mildly magnetic but no charge.”** The ledger renders this as **“the neutron spins with no twist”** and treats it as a settled neutron definition. The shift from “can be” to a concrete neutron mechanism should be returned for confirmation. In any case the graph code has no neutron or spin-½ state.

**What I could not verify:** The brief's preserved owner comments, VISION, notebook and log show substantial effort to retain her ideas. Without all original chat turns visible at this snapshot, I cannot certify that **every idea from the entire day** made it into one of those files, or that every quote was transcribed perfectly. The three specific issues above are supported by the written record; I am not claiming other messages were silently omitted.

### 8. Kinds of statement and research process

**F8.1 — A first sandbox look was promoted into a strong explanatory statement without the required independent confirmation. [High confidence]**

**Where:** `sandbox/u1_graph_free_energy.py`; `sandbox/LOG.md`; VISION Updates 100–101; rewiring-graph brief.

Rule 16 permits quick sandbox checks to **reject or narrow** a claim but does not let a first look **support** a claim. The report of the leading square-weight term passed directly from a sandbox look into an owner-facing VISION reading of what light does. The **analytic identity** is independently checkable and can legitimately become an exact statement—but that needs to be clearly presented as a separate proved derivation, not as an observed behavior, and the physical refolding effect remains untested. Mark the proposed physical interpretation **ours, unverified** until a predeclared coupled-graph test is run.

**F8.2 — Some “general knowledge” caveats are correctly marked, but the record still uses results stronger than their source. [High confidence]**

The files often correctly mark Landauer, Finkelstein–Rubinstein and related ideas “general knowledge, to verify.” The specific claim that an entropy change of `k ln 3` *means one photon leaves* is not established by Landauer's bound: a bound on work/heat in a specified thermal setting cannot select a photon number or a formation mechanism. Similarly, a classical link-rotation argument is a constraint on the existing state space, not proof that **no** quantum spin-½ mechanism could ever be built. The recorded corrections to O151 and the preserved failure gates are good process examples; they should not be undone.

### 9. The prior-work note

**F9.1 — “PARTLY FOUND” is defensible, but the comparison set is incomplete. [High confidence for identified papers; medium for novelty]**

**Where:** [`docs/reading/notes/2026-10-24_prior_work_u1_curl_mass.md`](https://github.com/EmilySmithCreate/RecreationalPhysics/blob/39466620/docs/reading/notes/2026-10-24_prior_work_u1_curl_mass.md).

The note correctly recognizes that the ingredients are established: gauge fields on graphs (Filk, 2000), potential terms on loops in theory space (Gregoire and Wacker, 2002), compact-direction scalar modes, and gauge fields coupled to dynamical triangulations (Candido and colleagues, 2020/2021). I found its principal preprint identifiers for those works resolve to appropriately related titles and abstracts. This is **not a claim to have checked every equation in every cited paper**.

Two major omissions change the framing:

- **Renken, Catterall and Kogut (1994), “U(1) lattice gauge theory coupled to quantum gravity.”** It explicitly couples U(1) gauge variables to **dynamical triangulations** in three dimensions. It is a direct precedent for a field on fluctuating geometry, preceding the cited 2020 work by decades. DOI [10.1016/0920-5632(94)90496-0](https://doi.org/10.1016/0920-5632(94)90496-0). I checked bibliographic records and the abstract, **not the full article**.
- **Levin and Wen (2006), “Quantum ether: Photons and electrons from a rotor model.”** A bosonic model on a cubic lattice develops **massless U(1) gauge modes and Dirac fermions** in its low-energy limit. It does not supply the present hypothesis, but is much closer to the particle handoff's goal of emerging photons *and* fermions than most papers in the note. [Phys. Rev. B 73, 035122](https://doi.org/10.1103/PhysRevB.73.035122); [arXiv:hep-th/0507118](https://arxiv.org/abs/hep-th/0507118). Abstract verified; complete mathematical comparison still owed.

Additional bibliographic corrections: **A. Romeo is indeed a listed third author** of Ferrer and de la Incera's [hep-ph/0107229](https://arxiv.org/abs/hep-ph/0107229), marked unverified in the note. The compact-dimension lattice study [arXiv:1003.4643](https://arxiv.org/abs/1003.4643) also lists **Marco Panero**, omitted in the note's short attribution. Do not claim the side-four construction is unprecedented based on the search recorded; say only that **the search did not locate that exact combination**, with its date and coverage.

### 10. Particle definitions now standing (Updates 97–101)

**F10.1 — The bookkeeping agrees with itself only under added choices; several observed properties remain unexplained. [High confidence]**

**Where:** VISION Updates 97–101; handoff's benchmark table; `strand_answers_look.py`; owner-questions file.

- **Thirds and halves:** On an ideal cubic lattice, a body diagonal has a threefold rotational symmetry and a face diagonal a twofold one. Choosing signed thirds for matter and signed halves for dark strands is a coherent convention, but the symmetries **do not supply a conserved electric charge, quantum state, mass, or interaction law**. On the rewiring graph there is no permanent cubic embedding specifying those diagonal axes.
- **Closure:** Each body-diagonal step changes bipartite vertex kind, so three body diagonals cannot form a closed ring. A “three-thirds electron” must therefore use a braid, a single longer strand or some other separately defined closure; it cannot be a three-edge ring on the stipulated lattice.
- **Charge:** Choosing `Q = (net signed thirds)/3` and assigning the observed quark counts makes electron/proton charges numerically consistent **by definition**. It does not explain why charge is conserved when strands change, why electron and proton charges are quantized, or how ordinary U(1) Gauss charge is connected to these strand labels. The earlier statement that a *full twist was neutral* was withdrawn in Update 101; any current recap retaining it is inconsistent.
- **Spin and statistics:** The neutron claim (“spin with no twist”) is unimplemented, and so are the electron's and quarks' spin-½ rotation and fermionic exchange statistics. The fixed classical link variables cannot supply the required minus sign under a 2π spinor rotation.
- **Antiparticles:** Calling an antiparticle the *mirror image* of a strand is a model choice; it does not establish the full charge-conjugation operation. Ordinary mirror reflection (parity, P) and changing particle to antiparticle (C) are different physical symmetries. In particular, the present mirror rule alone cannot explain the observed matter surplus.
- **Confinement and persistence:** Net-zero charge on a closed graph does not produce a potential growing with separation. The required `SU(3)` dynamics, two- and three-quark channels, gluons, stable/unstable lifetimes, and electron/proton/neutron mass differences are not derived.

**What is right:** The model is recorded as exploratory, earlier choices are visibly withdrawn instead of erased, and the handoff lists genuinely falsifying tests. The appropriate conclusion is that the particle definitions are **candidate labels and constraints**, not a demonstrated model of observed particles. This does not require inventing a replacement mechanism.

## 3. What I ran, and what I did not run

**Ran independently:** `python /mnt/data/u1_independent_checks.py`, a scratch-only reconstruction of periodic bipartite lattice links, four-cycle incidence, gauge constraints, exact U(1) character sums, side-four Bloch spectrum and the instanton winding diagnostic. Repeated it to verify the results. I also independently counted 1×1×2 diagonals inside two cube blocks and calculated the strip-bending values. Notably:

| Check | Independent result | Compared with record |
|---|---:|---|
| 6×6 flat torus: sites, links, faces, rank(B) | 36, 72, 36, 35 | Agrees |
| 10×10 flat torus: sites, links, faces, rank(B) | 100, 200, 100, 99 | Agrees |
| 4×8 curled torus: sites, links, faces, left-nullity | 32, 64, 40, 8 | Agrees |
| 4×8×8 curled torus: sites, links, faces, left-nullity | 256, 768, 832, 321 | Supports the four-cycle rule |
| Gauge-check `max |B divᵀ|` on all four | 0 | Agrees |
| 4×8 direct spectrum vs side-four Bloch formula | maximum absolute gap 5.33×10⁻¹⁵ | Agrees |
| Exact β=8: 36 / 100 faces | 0.9366115384 / 0.9352577250 | Agrees |
| Positive instanton winding change, 6×6, 500 random states | only 183 cases changed by +1 | **Contradicts unconditional docstring** |
| Positive instanton winding change, 10×10, 500 random states | only 187 cases changed by +1 | **Contradicts unconditional docstring** |
| 1×1×2 diagonals in 2×2×2 / 2×2×3 blocks | 48 / 80 | Agrees |
| Circular bending energies at lengths √2 / √5 / √6 | 13.9577B / 8.8276B / 8.0585B | Agrees *conditional on assumed energy law* |
| Leading-cost formal zero, λ=1.25, g=1.5 | β≈4.2783 | Agrees; **not a transition test** |
| U1″ signed residuals | 8 positive; combined nominal +2.643 errors | Same saved data, additional exploratory statistic |

**Inspected saved results, did not rerun:** `results/gate_u1_2d.csv`, `results/gate_u1b_2d_winding.csv`, `results/gate_u1c_2d_winding_long.csv`; their configs, runner and registration history. The failure/pass values above are **reported archived values**.

**Could not run from the repository:** `pytest tests/test_u1.py`; `scripts/run_u1_gate.py`; `sandbox/particle_handoff_looks.py`, `sandbox/u1_gate_topology.py`, `sandbox/u1_gate_autocorr.py`, `sandbox/strand_answers_look.py`, `sandbox/diagonal_112_look.py`, `sandbox/strip_corner_and_ring_energy.py`, `sandbox/light_in_curled_space.py`, `sandbox/u1_curl_mass_general.py`, and `sandbox/u1_graph_free_energy.py`. Their source and 24 October logs were inspected; no claim is made that their source output was freshly reproduced. The scratch verification wrote **nothing to `results/` or the repository**.

## 4. Missing published work and priority reading

These are the most relevant missing or underemphasized works I found. **Abstracts and bibliographic entries were checked unless a different status is stated; full-paper physics comparisons remain to be done.**

1. **R. L. Renken, S. M. Catterall and J. B. Kogut (1994), “U(1) lattice gauge theory coupled to quantum gravity.”** [DOI](https://doi.org/10.1016/0920-5632(94)90496-0). Direct precedent for a U(1) field on changing triangulated geometry, especially relevant to the next graph-rewiring stage. *Abstract checked; complete text not read.*
2. **Michael Levin and Xiao-Gang Wen (2006), “Quantum ether: Photons and electrons from a rotor model.”** [arXiv:hep-th/0507118](https://arxiv.org/abs/hep-th/0507118), [journal](https://doi.org/10.1103/PhysRevB.73.035122). Published example of both emergent U(1) photons and Dirac fermions; a particularly helpful benchmark for the particle ambitions. *Abstract checked; derivation to read.*
3. **Thomas Gregoire and Jay G. Wacker (2002), “Mooses, Topology and Higgs.”** [arXiv:hep-ph/0206023](https://arxiv.org/abs/hep-ph/0206023). Already in the note and very close on the topological effect of loop terms; compare its exact assumptions rather than presenting an unqualified equivalence to the present U(1) ring. *Abstract checked; the note says portions were read.*
4. **Alessandro Candido and collaborators (2020/2021), U(1)/SU(2) gauge theories coupled to two-dimensional causal dynamical triangulations.** [arXiv:2010.15714](https://arxiv.org/abs/2010.15714). Already listed but deserves prominence as a source for algorithms and detailed-balance issues when **both gauge variables and geometry move**. *Abstract-level verification; algorithm details to read.*
5. **T. Filk (2000), graph gauge action as a sum of closed walks.** [arXiv:hep-th/0010126](https://arxiv.org/abs/hep-th/0010126). In the note and directly relevant to the nonstandard choice of treating *every* four-cycle as a face. Compare closed **walks** versus simple four-cycles and ensure coefficient/multiplicity conventions agree. *The record says full paper checked; I confirmed bibliographic identification, not the complete derivation.*
6. **E. J. Ferrer, V. de la Incera and A. Romeo (2001), “Photon Propagation in Space-Time with a Compactified Spatial Dimension.”** [arXiv:hep-ph/0107229](https://arxiv.org/abs/hep-ph/0107229). A useful example of compact-dimension effects in a **different, one-loop physical setting**. Its results must not be mistaken for the present tree-level Wilson-line scalar. *Author list and abstract verified.*

**Literature verdict:** **PARTLY FOUND** remains the fair label. Published work covers the field mathematics, compact-loop potentials, changing-geometry gauge theories, and even models with emergent photons and fermions. I did **not find the exact side-four/all-four-cycles construction in the materials checked here**, but I have not performed an exhaustive full-text novelty search. Nothing about the current evidence justifies a claim of priority or a new observed particle mechanism.

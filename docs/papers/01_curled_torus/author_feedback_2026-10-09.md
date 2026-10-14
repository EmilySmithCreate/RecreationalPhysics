# Author feedback on *The curled torus burps*

**Reviewed:** 9 October 2026. **Source:** `paper.tex`, 477 lines, SHA-256 `cd5753c6acf2a6f621998243d3aae8da733f6474b9a8d1d3795ef7576a2af127`.

This is an AI-generated scientific review, not an endorsement by a human physicist. New derivations and computational observations below are **Ours, unverified**, in the repository's terminology. “Verified” below means checked in this review against algebra, source text, code, or existing data; it does not mean independently peer reviewed. Line references are to the source above.

## Recommendation and scope

**Revise substantially before submitting this version.** The central energy arithmetic and the counted low-cost exit moves hold up. The paper can make a useful, bounded claim about activated escape and conversion in a specified graph Markov chain. Its weakest points are the interpretation of a counting observable as geometric order, the distinction between first exit and detected decay, and the thermodynamic interpretation of its finite demon bath. There is also a definite mathematical error in the symmetry discussion: a factor of order N in a rate corresponds to a barrier shift proportional to log N, not N.

I read the full TeX source; examined the relevant simulation, classification, and statistical analysis code; reproduced the existing statistical analysis; enumerated exit moves at N = 64, 96, and 192; solved the small-graph metastability inequalities; and independently reconstructed the square complexes of all 120 saved T8 endpoints at lambda = 1.05. I checked relevant primary literature online and the local Kelly thesis. I did not rerun the production simulations, audit every historical preregistration against its Git timestamp, prove ergodicity at large N, or perform a new exhaustive literature search.

The accompanying [reviewer checks](reviewer_checks_2026-10-09.py) are read-only and reproduce the new numerical checks. The independent geometry reader was also checked against a known 6 × 6 flat torus, a 4 × 16 curled torus, and a disconnected union of two flat tori; all returned the expected square counts and topology diagnostics. Existing results and the manuscript were not edited. The review uses the local working copy, whose HEAD was `35e2efc9ad3d4e532d5ad1e75de56827983e0864`; refreshing remote references was unavailable because `.git/FETCH_HEAD` was not writable.

## Priority list

| Priority | Issue | Required correction |
|---|---|---|
| High | Mean demon energy is identified with temperature | Derive or calibrate the thermometer and revise the reservoir estimate |
| High | d = 1 or 2 is treated as certification of an ordered geometry | Use stronger neighborhood checks or call these counting signatures |
| High | Largest connected converted component is promoted to a single front | Narrow the claim or measure interfaces and the history of nucleation |
| High | First-exit theory and detected-decay statistics are interchanged | Define separate stopping times and compare like observables |
| High | Very long decay waits are softened by pooled exponential tests | Treat them as evidence requiring a separate mechanism/detector audit |
| High | Symmetry weighting is described with an incorrect acceptance prescription and barrier scaling | Write the full Metropolis–Hastings rule; replace N by log N for the barrier shift |
| Medium | A 200-sweep criterion is presented as a metastability endpoint | Call it an operational persistence boundary |
| Medium | Exact energy difference is presented as exact release in every decay | Condition on the endpoint and distinguish energy from free energy |
| Medium | The “exact” escape argument relies partly on a finite neutral walk | Prove or certify closure of the neutral basin |
| Medium | Post-data amendments are called preregistered verdicts | Separate original tests, amended analyses, and fresh confirmations |
| Medium | Microcanonical equilibration and absence of coexistence are overstated | State the extended ensemble and the finite-time evidence |
| Low | Missing definitions, domain restrictions, and reproducibility details | Add a compact model/protocol table and freeze a release |

## 1. Correct the demon thermometer and the reservoir argument

**Location:** lines 242–246 and 259–265. **Status:** a concrete mismatch between the thermodynamic interpretation and the implementation.

The paper says the stores' mean reads the temperature. `scripts/run_sealed_tube.py` records `bath_T = mean[k]`, and `scripts/analyse_t9.py` compares it directly with the canonical coupling 3.5. But graph energy changes at lambda = 1.25 are integers:

\[
\Delta H=-16\Delta S+5\Delta X.
\]

Starting from stores containing 0 and 12, each store remains on an integer energy lattice. Floating-point storage does not make its reachable energies continuous. The exit census includes moves costing 12 and 25, so a common lattice spacing of one unit is relevant; determine the actual accessible spectrum rather than assuming it.

For an equilibrated demon with levels 0, delta, 2 delta, ... and an approximately canonical distribution,

\[
P(k\delta)=(1-e^{-\delta/g})e^{-k\delta/g},\qquad
u_D(g)=\langle E_D\rangle=\frac{\delta}{e^{\delta/g}-1},\qquad
g=\frac{\delta}{\ln(1+\delta/\langle E_D\rangle)}.
\]

Thus the mean equals g only in the continuous-level limit or approximately when delta/g is small. With delta = 1, g = 3.5 corresponds to mean demon energy **3.024**, not 3.5. Conversely, mean energy 0.5 corresponds to g = **0.910**, not 0.5. This matters particularly for claims that the cold bath lies below a specified healing or melting coupling.

The repository already has this inversion in `graphity.sealed.demon_temperature`, but the sealed-torus runner does not use it. That function's comment also incorrectly says quarter-integer lambda makes all changes multiples of four: at lambda = 1.25 the coefficient 4 lambda is five, and the census contains a 25-unit move. Correct the comment separately if that function is used.

There is a second approximation in C* approximately N/3.5. Conservation gives

\[
E_{\rm tot}=\varepsilon N+s=H_{\rm graph}+E_{\rm bath}.
\]

If equilibrium at a crossover coupling g_m is established, a more defensible estimate is

\[
C^*\simeq\frac{\varepsilon N+s-U_{\rm graph}(g_m)}{u_D(g_m)}.
\]

The current estimate drops the seed, residual defects, the graph's thermal energy, and the discrete thermometer correction. Even retaining only the last correction changes the large-N estimate from N/3.5 to N/3.024, about 16%. That is not necessarily enough to change the coarse observed crossover, but it prevents calling its quantitative prediction exact.

**Action:** retain the raw `bath_T` data unchanged, label it mean store energy, determine the level spacing and equilibration regime, and add a corrected analysis. Report the reservoir crossover as measured and its energy-balance estimate as approximate. A small reservoir has unbounded energy storage in this implementation; it fails to preserve an ordered product because it heats too much, not because it reaches a maximum storage capacity. For context, [Creutz's original paper](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.50.1411) defines the constant-total-energy approach; the discrete thermometer equation above follows directly from summing a geometric distribution.

## 2. The order parameter does not certify either ordered geometry

**Location:** lines 101–108, 168–174, 288–289, and the abstract. **Status:** verified counterexample to the inference, not a demonstrated failure of the reported histogram.

The disclaimer that d(v) is not a Hausdorff or spectral dimension is correct. However, the text subsequently identifies every vertex at d = 1 or 2 as belonging to the curled or flat ordered state. That implication is stronger than the definition supports.

I enumerated valid single switches from a perfect N = 64 curled torus and found d = 2 vertices whose incident edge square counts are **[1, 2, 2, 3]**, rather than [2, 2, 2, 2]. They close four squares at the vertex, as a flat vertex does, but have a different local arrangement. One such graph has 52 vertices at d = 1, eight at d = 2, and four at d = 3. The companion script reproduces this witness. Therefore “98.8–99.8% of vertices belong to one ordered state or the other” is not established just by the measured d histogram.

There is a useful exact identity here. Under the hard-core rule, an edge pair at a vertex closes at most one square. If q_v is the number of squares through v,

\[
d(v)=6-q_v,\qquad \sum_v d(v)=6N-4S.
\]

The runner's conversion coordinate is therefore

\[
f=\frac{5N/4-S}{N/4}=5-\frac{4S}{N}=\overline d-1.
\]

It equals the fraction of flat vertices only when the vertices actually consist of the two ideal signatures d = 1 and d = 2. Melting can increase f as well. The dimension histogram is a useful distributional refinement of the square count, but its mean is not an independent geometric observable.

**Action:** call the reported percentages “vertices with curled-like or flat-like square-count signatures.” If claiming ordered neighborhoods, compare the square-incidence link or a rooted neighborhood with the ideal states. A flat square-complex vertex should have a four-cycle as its link, not merely four incident squares. Record both the existing preregistered statistic and this stronger diagnostic; do not silently change the original test.

## 3. Establish what “decompactification” and “flat torus” mean

**Location:** title; lines 60–65, 97–108, 112–115, 221–225, and 387–390. **Status:** incomplete geometric evidence in the manuscript; some independent endpoint checks succeeded.

Removing the extra four-cycles and reaching H = 0 does not by itself show that the short direction has opened to a macroscopic size. For example, a **6 × L** square torus has the same d = 2 signature and zero energy as a more isotropic torus, while retaining a direction of fixed circumference as L grows. Also, the Hamiltonian allows disconnected graphs: a disjoint union of zero-energy tori is another zero-energy state. Connectedness is not enforced by the kernel.

Here is evidence in the paper's favor: I independently filled every square in all 120 saved T8 endpoints at lambda = 1.05. At every size, all 30 endpoints were connected, each edge belonged to two squares, every vertex link was cyclic, the surface was orientable, and Euler characteristic was zero. These checks establish **torus topology for that set of endpoints**, rather than relying on energy alone. They do not establish an isotropic aspect ratio or a macroscopic increase of both independent periods, and they do not cover every other dataset.

**Action:** distinguish three questions: local square order, torus topology, and opening of an independent geometric period. If retaining “opens to full size,” reconstruct periods/holonomy or measure noncontractible cycle lengths and their dependence on N. If this is beyond the present paper, explicitly define “decompactification” as removal of the four-cycle compactification signature. Describe ground states by the proved condition S_e = 2, and classify topology separately. The “every space ... is a torus” figure joke should not function as an unstated restriction on the graph ensemble.

## 4. A dominant connected component is weaker than a single front

**Location:** lines 30–31, 168–180, 288–289, 332–339, and 387–390. **Status:** overstatement of what the stated measurements establish.

The test requires at least 70% of d = 2 vertices to lie in the largest induced connected component, averaged over decays. That can be satisfied by several nuclei that have merged, or by an irregular connected region with multiple boundaries. It does not count moving interfaces or prove that the change began at exactly one place. On a periodic tube, a growing connected interval would ordinarily have two boundaries; “one front” needs a stated geometric meaning.

The paper itself reports a failed coarse-front test: 21 of 59 nucleating T12 decays converted in several patches. It also reports that the share with several converted pieces at quarter conversion is about 0.43–0.44 at lambda = 1.30 in the repeats, even though the abstract says the single-front character persists there. These statements can coexist only if “single front” means the loose, later-time dominance statistic, not unique nucleation or one propagating boundary.

**Action:** use “conversion is dominated by one connected flat-like region at half conversion.” State that multiple early patches occur. To make a stronger front claim, show actual snapshots and time series of interface size, number of connected regions, and first appearance of separate nuclei. Specify whether geometry is read in the evolving graph or the original torus coordinates. The schematic is correctly labeled, but it is not evidence of a front. Report the distribution across replicas, not only the average largest-piece fraction.

## 5. Keep first exit, successful nucleation, and detected decay separate

**Location:** lines 26–30, 136–146, 154–166, 183–189, 290–306, and 433–452. **Status:** the first-exit calculation is supported; its transfer to other waits is not established.

At least four stopping times appear in this work:

1. First accepted move out of the perfect/neutral curled basin, counted attempt by attempt in T22.
2. First excursion that grows rather than returning to that basin.
3. The T7/T8 detector crossing after its 200-sweep resting window.
4. A specified conversion fraction or final settling criterion.

Eq. (2) predicts the first of these. `run_tube_decay.py` measures the third using a threshold estimated from the same trajectory's first 200 sweeps. The discussion acknowledges recrossings, but the abstract and exponential claims still run these observables together.

I reproduced `scripts/analyse_paper_stats.py`: the 432 first exits give D = 0.035 and bootstrap p = 0.53; T22's 240 attempt-counted first exits tested against Eq. (2)'s predicted means give D = 0.039 and p = 0.85. Those are reassuring checks of the first-exit theory. They do not show that subsequent growth or the decay detector has the same law.

If excursions were independent renewal attempts with success probability kappa, the successful departure rate could approximately be kappa times the exit rate, with additional time spent on failed excursions and growth. That requires assumptions; it cannot simply be substituted for the first-exit calculation. Likewise, exits/fallbacks counted until 25% conversion yield a useful empirical success fraction, but do not automatically establish a transition-state-theory transmission coefficient. Define the basins, commitment event, estimator, and uncertainty before adopting that terminology.

**Action:** add a table naming each stopping time, how it is observed, and which prediction applies. Make the first-exit agreement the quantitative kinetic result. Describe detected-decay agreement as a separate empirical comparison with detector and recrossing limitations.

## 6. The long waits need a decisive audit; pooled KS agreement does not resolve them

**Location:** lines 183–189, 303–306, 333–341, and 449–452. **Status:** reproduced observations with an unresolved interpretation.

The text now discloses the later outliers, which is necessary. But calling the whole distribution exponential and describing the failures mainly as a too-tight band remains too reassuring.

For N = 64, I read these maxima directly from the T24 CSV files:

| lambda | Maximum detected wait | Eq. (2) first-exit mean | Ratio |
|---|---:|---:|---:|
| 1.25 | 20,270 sweeps | 845.14 | 23.98 |
| 1.30 | 32,155 sweeps | 419.04 | 76.74 |

For 120 independent exponential waits with that mean, the probability of at least one wait above r times the mean is at most 120 exp(-r): about **4.6 × 10^-9** and **5.7 × 10^-32**, respectively. These are **illustrative null probabilities, not valid final p-values for these decay data**: Eq. (2) predicts another stopping time, and the examples were examined after the data. Their significance is that these observations cannot responsibly be dismissed as ordinary scatter around that particular exponential model. The 200-sweep recording floor is far too small to explain their magnitude on its own.

Pooling cells after dividing by their own measured means can obscure rate heterogeneity; outliers also inflate the means used for normalization. KS is most sensitive to the bulk of a distribution, and a large p-value is not evidence that every cell or its far tail is exponential. The reproduced analysis rejects the unfiltered T7/T8 residual sample at p = 0.03 and T7 alone much more strongly; the clean T8 subset gives p = 0.55. These are different datasets and hypotheses, not a universal memorylessness result.

**Action:** state “first-exit data are consistent with the exponential prediction; detected-decay waits show unresolved long tails.” Audit the saved waiting graphs for entry into another basin, repeated failed growth, and delayed threshold crossing. Use a prespecified tail or hazard test in a fresh run, with the relevant stopping time counted directly. Preserve every old verdict. Starting the clock later until a test passes is useful exploratory diagnosis, not confirmatory validation.

## 7. The detection correction is an idealized observation model

**Location:** lines 292–295, 367–370, and 441–448. **Status:** the formula's arithmetic is correct; its applicability needs qualification.

If T is exponential and the observed wait is W = max(T,a), then

\[
\mathbb E[W]=a+\tau e^{-a/\tau}.
\]

Thus the quoted formula is correct for a recording floor. If instead one keeps only runs that truly survived until a, memorylessness gives **E[T | T > a] = a + tau**, a different expression. At lambda = 1.30 these predictions are about 462 and 624 sweeps; at 1.35 they are about 265 and 388 sweeps.

The actual code does more than impose a floor: changes during the initial window affect the estimated resting variance and hence the detector threshold. It samples S only at five-sweep intervals and an excursion can heal between checks. “Not yet changing at sweep 200,” operationally f_200 = 0, is also not equivalent to “has never exited before sweep 200.” It may include a torus that exited and returned.

**Action:** identify which sample each curve describes and call the dashed line a recording-floor approximation. A calibrated null analysis should reproduce the full detector, selection rule, and censoring, or use direct first-exit measurements. The bootstrap appropriately re-estimates fitted means, but its exponential draws and rounding do not reproduce the trajectory-dependent threshold.

## 8. Separate energetic trapping from operational persistence

**Location:** lines 119–122, 176–177, 281–287, and the abstract. **Status:** a terminology problem; the small-N arithmetic can be strengthened.

The paper uses “metastable” for both an above-ground local minimum and a condition where most trajectories remain at least 75% torus after 200 sweeps. The second depends on g, the clock convention, and the arbitrary watch duration. The perfect torus's B-move cost stays positive until lambda = 1.6; disappearance of 200-sweep persistence around 1.35–1.40 is not an energetic spinodal.

Also, tau = 200 is a mean-wait condition, not a 50% survival condition. For pure exponential first exits, median survival at 200 would correspond to tau = 200/ln 2, approximately 288.5. The actual “75% torus” condition includes growth, so neither relation derives its boundary exactly.

I independently explored the 26 N = 18 classes and solved the affine single-move inequalities on lambda >= 1. The strict above-ground minima have (S,X) = **(21,12)** on 1 < lambda < 1.6 and **(22,16)** on 1 < lambda < 4/3. This supports the stated small-N interval without relying on a finite grid. It does not establish a global large-N metastability window.

**Action:** call the map's edge an “operational persistence boundary under the 200-sweep criterion.” Present the N = 18 inequality certificate as the exact small-system result. Do not extrapolate its class structure to the production sizes.

## 9. Repair the symmetry acceptance rule and effective-barrier scaling

**Location:** lines 394–406. **Status:** definite mathematical correction plus an underdetermined kinetic extrapolation.

For a fixed bipartition with n vertices per side, a graph class has (n!)^2/A(G) distinct labelings, where A is its side-preserving automorphism count. Giving each unlabelled class one Boltzmann weight can therefore be implemented on labelled graphs with target weight proportional to A(G) exp[-H(G)/g]. That part of the argument is correct.

For the stated symmetric proposal, the corresponding acceptance rule is

\[
a(G\to G')=\min\left[1,\frac{A(G')}{A(G)}e^{-\Delta H/g}\right].
\]

“Multiplying each acceptance by the ratio” is not a correct general prescription if “acceptance” already means min(1, exp[-Delta H/g]). Multiplication and clipping must be applied in the order above. A downhill move with a sufficiently small symmetry ratio is an immediate counterexample to the naive rule.

If an exit rate is suppressed by a factor cN, then

\[
\Delta F_{\rm sym}=g\ln(cN),
\]

not a barrier change of order N. Correct line 406, which explicitly misidentifies the rate factor as the effective barrier. The A-move symmetry ratios provide an instantaneous suppression estimate; the total lifetime also depends on neutral-state occupancy, B moves, other exits, and the chosen proposal on the quotient. No decay simulation or complete effective-rate calculation is supplied for this alternative ensemble.

Uniform weights over unlabelled classes are a legitimate **alternative measure**. They are not uniquely required by calling vertices interchangeable or invoking identical particles. State the measure as a modeling choice; quantum indistinguishability alone does not derive this classical graph weighting. [Betre and Lewis](https://arxiv.org/html/2509.08296v1) study a quantum multigraph construction, so identify the precise result being cited rather than treating that paper as automatic justification for uniform classical class weights.

## 10. Preserve the exact energetics but condition every release claim

**Location:** lines 24–39, 68–75, 91–108, 221–225, and 378–381. **Status:** sound formulas with overly broad prose.

The identity

\[
H=4\sum_e\left[(2-S_e)_++(\lambda-1)(S_e-2)_+\right]
\]

makes the ground-state statement transparent. For lambda > 1, H = 0 iff every edge has two squares. At lambda = 1, zero energy instead requires every edge to have **at least** two squares, so the degeneracy is much wider.

The ideal curled-to-zero-energy difference is exactly epsilon N. For a decay ending with residual graph energy H_f, however,

\[
Q=H_i-H_f=\varepsilon N-H_f.
\]

The 14-unit relic at lambda = 1.25 leaves a deficit 14/N per vertex. A thermal measuring window may differ again from the energy of its final saved graph. The later T24 classification defines “FLAT” by H = 0 alone; its name should not silently certify topology.

**Action:** write “the ideal-state energy difference is epsilon per vertex; that full decrease is realized when a zero-energy endpoint is reached.” State how measured bath heat, graph-energy decrease, and thermal averages are defined. There is no demonstrated latent heat here, and the paper correctly disclaims a thermodynamic first-order transition. Retain that disclaimer.

At lambda = 1 the three named ideal arrangements are degenerate, but “no ordered arrangement can turn into another with any release” is too broad: it does not cover every possible ordered curved/defected arrangement. Restrict it to these states. Equal energies also do not imply equal free energies or no dynamical conversion, because entropy can differ.

## 11. Make the exactness and domain of the exit argument explicit

**Location:** lines 101–108 and 124–150. **Status:** checked move counts; missing general closure argument.

The census reproduces 3N distinct A moves, 2N B moves, and N/2 neutral moves at N = 64, 96, and 192. The costs 32 - 16 lambda and 64 - 40 lambda, their crossing at 4/3, and the 12-unit A cost at 1.25 are correct. At N = 192, lambda = 1.25, g = 1.5, all omitted moves add about **0.885%** to the A+B rate, consistent with the stated small correction. This is evidence supporting the paper, not a defect.

However, a 60-step walk through neutral moves is not an exhaustive proof that every reachable neutral arrangement has the same hazards or no cheaper exit. The script enumerates moves exactly at each visited state; the sequence of visited states is sampled. Distinguish these two kinds of exactness. The claim that every smaller seed is impossible throughout the neutral basin needs a bound on the entire accessible basin, not just the visited configurations.

**Action:** give a constructive characterization of all neutral twists and show their local move census is invariant, or exhaustively enumerate the neutral classes for each stated size and certify closure. Until then, qualify the neutral-basin extension as checked on the walk. Eq. (2) is an A+B approximation, not an exact total rate: include the omitted-move correction in comparisons where it is resolvable.

With a constant per-attempt exit probability p, the exact waiting law in attempts is geometric. Its mean in sweeps is exactly 1/(2Np); the continuous exponential law is the small-p approximation. This distinction is small here, but simple to state.

Finally, specify the torus domain: the bipartite periodic construction requires even periods; the one-curled formula assumes the other period exceeds four. **4 × 4 is the 4-cube**, with S = 3N/2 and X = 2N, not the one-curled counts 5N/4 and N. State the sizes for which the exit formulas are proved or enumerated rather than leaving L unrestricted.

## 12. A fixed seed is an energetic requirement, not automatically a spatially local trigger

**Location:** lines 33–35, 249–257, and 387–391. **Status:** lower-bound logic is sound conditional on basin closure; scope of the trigger is overstated.

With a perfect initial torus, nonnegative stores, and no exit cheaper than 12, a total seed below 12 cannot pay for an exit. That is a strong necessary-energy statement. Eight successes out of eight at each tested seed above threshold are observations of sufficiency for this protocol and duration; they are not a proof that every such trajectory eventually converts. For perspective, eight successes give a two-sided 95% binomial lower bound on success probability of approximately 0.63.

The seed in this experiment is in a globally selected store, and the two edges of each switch are drawn from the whole graph. It is not initially attached to a spatial location. The cheapest escape edits a bounded neighborhood, but the energy-delivery protocol is globally mixed.

**Action:** use “a size-independent total activation budget” and “a bounded-size escape move.” Reserve “local spark” for a protocol that actually fixes where energy is deposited. Keep the barrier to first exit distinct from the minimum maximum energy along a complete path to the final state. State the seed scan grid, conversion criterion, and run duration alongside the 8/8 result.

## 13. Energy conservation does not establish equilibration or rule out coexistence

**Location:** lines 242–247 and 259–265. **Status:** conservation is well checked; ensemble and inference need qualification.

The conserved quantity is the energy of **graph plus stores**. The graph's own energy changes. If an integer bath of C stores is equilibrated, the graph marginal is weighted by the number of bath allocations, approximately

\[
\Omega_C(M)=\binom{M+C-1}{C-1},\qquad M=E_{\rm tot}-H(G),
\]

for nonnegative integer M within the reachable sector. Thus C changes the bath entropy as well as its thermal response. A symmetric accepted move has a symmetric reverse on the extended state space, supporting a microcanonical invariant measure there; equilibration within that space still requires accessibility and mixing evidence. This matters when the phenomenon itself is prolonged trapping.

No stalled run under the chosen duration and coarse C grid is evidence about that protocol. It cannot exclude a coexistence temperature, especially when the reported thermometer and equilibrium status have not been calibrated. Canonical equilibrium coexistence would be a statement about free energies, not simply whether a finite seeded run stops with both signatures present.

**Action:** say “energy-conserving dynamics on the graph-plus-reservoir system” and “no sustained two-order stall was observed in the tested runs.” Show stationarity/equilibration diagnostics if reporting a thermodynamic temperature or equilibrium conclusion. Quote conservation to the measured numerical tolerance; “to the last unit” should not imply bitwise exact arithmetic at noninteger lambda.

## 14. Clarify preregistration and strengthen statistical reporting

**Location:** lines 40–42, 168–189, 226–232, 313–341, and 429–431. **Status:** transparent disclosures are present, but their headline description still overstates confirmation.

The paper commendably states that three energy-gate amendments were made after the rerun they judged and that all three maps were inconclusive. Nevertheless, a verdict computed using those amendments is not wholly preregistered. The original unchanged predictions may be preregistered; the amended retrospective energy analysis is another category. The Methods claim that analysis rules behind every verdict were committed before the runs conflicts with the disclosed timing of those amendments.

Similarly, T24's replacement gate verifies existence and validity of saved graphs. It is a useful data-integrity check, but it no longer tests the earlier energy-release hypothesis. State that the claim tested by the gate changed; validity is not confirmation of complete release.

**Action:** provide a short table of original predictions and verdicts, dated amendments applied to already-observed data, and fresh runs scored under previously fixed revised rules. Use “preregistered component tests” and “retrospectively amended energy analysis” where appropriate. Do not rename or erase failures.

Other statistical changes that would help a referee:

- Report uncertainty for flat-endpoint fractions, success fractions, kappa, and front statistics. Treat replicas as the independent units; vertices within one graph are correlated.
- A CV near one is not sufficient for memorylessness. Preserve it as the original test, not the definition of an exponential law.
- Correctly emphasize that a failure to reject a slope or positional null is not evidence of exact size or positional independence. “No detectable growth over N = 64–288” and “no association detected by the specified distance statistic” are supported descriptions. A mean-distance randomization test can miss other positional structure.
- The quoted inverse-variance weighted waiting-time ratios use uncertainties estimated from the waits themselves. With 16 replicas and skewed waits, shorter sample means can receive larger weights. Use the exponential/geometric likelihood or report exact intervals for its mean rather than letting the weighted average carry the main agreement claim.
- The fitted N = 64 slope 14.4 ± 1.0 differs from the A cost 12 by about 2.4 quoted standard errors. A+B channels and omitted exits cause curvature in log tau versus 1/g; an effective fitted slope is not automatically a collective barrier. Compare to the full predicted curve before interpreting that fit.
- State counts of runs reaching each stopping event, censored runs, and exclusions. Some analyzers restrict summaries to trajectories reaching 75% conversion, which can select faster or more successful decays.
- The claim of an upper bound on latent heat from a single-peaked finite-size histogram needs its estimator, confidence/coverage, equilibration checks, and scope. At minimum call it the analysis's finite-size resolution bound, not a general bound on a thermodynamic transition.

## Smaller corrections and presentation improvements

1. **Define g at first use.** Write the target probability proportional to exp(-H/g), the Metropolis rule, H units, and that g is a dimensionless coupling serving as temperature for this sampler. The source normalization is H = -4 sum_v sum_{w~v} kappa(v,w), not literally an unsigned sum of curvature. The minus sign and normalization should accompany “total curvature.” [Trugenberger's Eq. (21)](https://arxiv.org/html/2512.17676v2#S4.E21) gives that convention; deriving your bipartite energy directly from the edge curvature is safer than relying solely on the displayed split in Eq. (22).

2. **State the ensemble.** Simple undirected graphs? Fixed labelled bipartition of N/2 vertices per side? Connectedness unrestricted? These choices matter for ground states, symmetry factors, and the word “torus.” Symmetric proposals give detailed balance, but ergodicity at N <= 18 does not prove global equilibration at production sizes. Replace unconditional “samples the equilibrium distribution” with the precise stationary-measure statement and the known ergodicity limits.

3. **Make the protocol self-contained.** Define f, the 200-sweep threshold, five-sweep sampling, settling rule and cap, and snapshot selection in Methods. Give the sealed run duration (T10 uses 30,000 sweeps), the definition of a counted relic, and what the table ranges average over. These are central observables, not incidental code details.

4. **Clarify the chronology in line 230.** The “three predictions” include morphology at half conversion and are not all predictions about the first switch. Replace that description with their actual scope.

5. **Restrict physical terminology.** The existing disclaimers about physical time and thermodynamic first order are appropriate. Also avoid saying the release happens “all at once” without comparing waiting and conversion durations. Describe the false-vacuum connection as motivation for classical activated decay; no tunneling or Lorentzian spacetime dynamics has been computed.

6. **The N = 18 result deserves a small table.** The intervals checked in this review would replace a vague scan statement with a short verifiable certificate. “Three exact consequences follow” currently introduces four italicized items.

7. **Freeze reproducibility.** Cite a commit/tag or archival release, not only a moving repository URL. Add a claim-to-script/config/data table. Existing `.meta.json` files recording versions and seeds are useful, but without the code revision they do not fully identify the computation.

8. **Support the novelty sentence precisely.** `REFERENCES.bib` contains a dated 23 September search log addressing both deformation and ordered conversion. So it would be wrong to say no search record exists. Move/link that record into the required dedicated prior-work note, and distinguish a search for lambda deformations from a search for ordered-to-ordered kinetics. The broader decompactification note addresses related theories rather than establishing novelty in this exact model.

9. **Literature comparisons need qualifiers.** [Kelly–Trugenberger–Biancalana](https://arxiv.org/html/1901.09870v2) discuss the capped bipartite simulation as well as the uncapped action; distinguish those cases when comparing equilibrium curves. [Gorsky–Valba](https://arxiv.org/html/2101.04072v1) do not impose precisely the same bipartite ensemble, so agreement on first-order behavior in the global-only model is context, not identical-model validation. The local Kelly thesis passage does report small higher-degree hysteresis and reluctance to infer definitive first-order behavior; your cautious account of that disagreement should remain. Cite the discussion on printed p. 219 (PDF page 226) and Fig. 4.58 on printed pp. 224–226 (PDF pages 231–233), which covers N = 50–500. The thesis's [repository record](https://www.ros.hw.ac.uk/items/24919179-d6d0-4d34-afe8-a035e9368960) verifies its bibliographic identity.

10. **Verify release artifacts.** The source is newer than the compiled `paper.pdf`, and `arxiv_abstract.txt` has wording different from the current abstract. Regenerate the PDF and synchronize the separate abstract only after deciding the revisions. A static source check found no undefined citation keys; a LaTeX compilation was not performed in this review.

## A defensible central claim

This is suggested wording, not an edited abstract:

> In a lambda-deformed graph energy adjacent to combinatorial quantum gravity, an ideal one-curled torus lies an exactly known energy above zero-energy square-lattice states. For the specified Metropolis edge-switch chain, enumerated low-cost moves predict the mean time to first exit without fitted parameters, and the directly counted first-exit data are consistent with that prediction. During conversion, most vertices retain one of two local square-count signatures, and one connected converted region usually dominates at half conversion. Energy-conserving graph-plus-reservoir dynamics show a size-independent activation budget over the tested sizes and a product that depends on the reservoir's thermal response. Detected-decay waits contain unresolved long tails, and several preregistered global verdicts remain inconclusive.

This leaves room for the result that is actually supported while separating the geometric, thermodynamic, and statistical questions still open.

## Minimum work before submission

1. Correct the thermometer, symmetry acceptance formula, log-N barrier statement, and preregistration wording.
2. Distinguish all stopping times and qualify the detected-decay tails and operational metastability edge.
3. Narrow “ordered states,” “single front,” and “decompactification,” or supply the stronger geometric measurements they require.
4. Certify the neutral-basin argument if retaining universal seed/barrier language.
5. Add uncertainties and a frozen reproducibility map, then regenerate the PDF and abstract.

The present arithmetic does not need to be discarded. The revision should make each conclusion follow from the particular calculation or observation that supports it.

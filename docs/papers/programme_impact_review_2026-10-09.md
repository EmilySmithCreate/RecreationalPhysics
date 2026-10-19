# How the curled-torus review affects the wider physics programme

**Date:** 9 October 2026. **Status:** AI-generated dependency audit; new scientific interpretations and reviewer calculations are **Ours, unverified**. This supplements [the paper review](curled_torus/author_feedback_2026-10-09.md). It is not a replacement for the programme's dated experiment record.

## Main assessment

The errors do **not** invalidate the whole repository. They affect different layers:

- The graph-energy arithmetic, conservation bookkeeping, and several exact enumerations survive.
- Some measured outcomes remain valid for their recorded algorithms, but their physical names or explanations are too strong.
- Some downstream numerical interpretations need reanalysis, particularly bath temperature and defect support.
- Several programme-wide claims are demonstrably broader than the evidence: a square-count signature does not certify flat space; fully curled graphs need not be hypercubes; and cube components can join by allowed moves.

The largest consequence is to the inference **“these vertices have the right count, therefore space has opened, therefore this is a physical front with a fixed activation.”** That inference is reused in later classifiers and, more seriously, in the interpretation of the direction-tie Hamiltonian. The temperature issue is more contained, but it affects the comparison between sealed relic survival and canonical annealing.

One important clarification of the previous review: **the implemented symmetry samplers already use the correct acceptance rule.** The paper's ambiguous prescription and incorrect effective-barrier scaling do not demonstrate an implementation error in those chains. Likewise, the earlier 120-endpoint topology check supported the torus identification at lambda = 1.05; that evidence should not be discarded because the counting diagnostic is insufficient in general.

I inspected the core kernels, relevant runners and analyzers, all later paper sources by targeted searches, the current programme draft, series plan, and relevant experiment records. I reproduced T38's existing analysis, mapped a nominal discrete thermometer onto the T10 final readings, and constructed exact graph counterexamples. I also read one saved cold T37 endpoint to check where its energy sits. I did not rerun production experiments, change preregistered scores, or audit every saved state. Only this report and its [read-only check script](programme_impact_checks_2026-10-09.py) were added for this task; programme files and result data were not changed.

## Dependency map

| Earlier issue | Downstream use | What is affected | What survives |
|---|---|---|---|
| Mean store energy treated as g | T9/T10/T11/T18; sealed higher-degree runners; relic and fertile-window papers | Temperature estimates, comparison with canonical melting/healing, bath-capacity explanation | Recorded energy, conservation, counts, and observed outcomes under the actual bath |
| d used as geometric certification | T30/T37/T44–T49/T51/T53/T55/T56; later paper claims | FLAT/OPENS/ONE SPACE labels, defect boundaries, decompactification interpretation | The measured d histograms, graph connectivity, and exact H values |
| Connected patch called a unique front | T17/T37 seed-to-relic argument; T47/T50 time/propagation track | Unique nucleation, interface speed, and physical-clock interpretation | Counted patches and conversion-coordinate trajectories |
| First exit equated with detected decay | T38, T37 nucleation-rate estimate, metastability maps | Memorylessness, physical “two populations,” predicted number of seeds | Direct T22 first-exit test and T38's score under its recorded rules |
| One-move barrier equated with full conversion barrier | Higher-degree cascade and critical-patch work; T54 | Extrapolation of a fixed total opening cost | Exact costs of the stated single moves; measured outcomes with the supplied seeds |
| Symmetry formula/barrier wording | T21/T42/T49; gravity and quantum discussions | Explanation of entropy and rate scaling | Correctly implemented symmetry-weighted chains and finite graph counts |
| Exact gap equated with heat fully released | Relic fractions, “fertility,” fitted release ledgers | Interpretation of residual energy and proposed cosmological abundances | Ideal-state gaps and the actual final graph energy |
| Post-data changes described as preregistration | Series plan, README, programme summaries | Strength of confirmation and which hypothesis was tested | Original scores, fresh fixed-rule runs, and disclosed exploratory analyses |

## 1. Bath temperatures: the cold relic comparison changes substantially

**Relevant code:** `src/graphity/sealed.py:136–155, 237–254`; `src/graphity/sealed_d.py`; `scripts/run_sealed_tube.py:59`; `scripts/analyse_t9.py:24, 59–79`; `scripts/analyse_t10.py:80–111`; `scripts/run_sealed_sheet_budget.py:64`.

**Relevant claims:** `docs/papers/relic/paper.tex:79–85, 203–209`; `docs/papers/curled_torus/paper.tex:242–265`; series paper 3's reservoir/fertility interpretation.

The shared-bath runners record average demon energy as `bath_T`. For the zero-offset, one-unit discrete spectrum relevant as a candidate at lambda = 1.25, the equilibrium canonical approximation gives

\[
g=\frac{1}{\ln(1+1/\mu)},\qquad \mu=\langle E_D\rangle.
\]

I applied that mapping to the existing final T10 readings:

| N | Mean recorded store energy | Mean mapped g | Replicas satisfying recorded energy < 1 | Replicas satisfying mapped g < 1 |
|---:|---:|---:|---:|---:|
| 64 | 0.4875 | 0.8963 | 20/20 | 19/20 |
| 96 | 0.4922 | 0.9015 | 20/20 | 20/20 |
| 192 | 0.4922 | 0.9016 | 20/20 | 20/20 |
| 288 | 0.4939 | 0.9035 | 20/20 | 20/20 |

These are **nominal recalibrations, not certified thermodynamic temperatures**: they assume the accessible lattice, an approximately exponential demon marginal, and equilibration. Those conditions must still be checked. The average of mapped final readings is also not a replacement for a time-averaged thermometer.

Nevertheless, the correction is large enough to matter. Paper 2 contrasts survival for 30,000 sweeps in a sealed bath near g = 0.5 with annealing at canonical g = 1.0. The relevant bath may instead be near **0.9**, much closer to that canonical point. The actual observation of survival remains true; the assertion that it survived at about half that temperature does not follow from the recorded mean.

There is also a direct gate consequence: T10 criterion (c) requires the bath to end below g = 1. At N = 64, one final mean is 0.59375. The nominal discrete map puts it slightly above one. If that map were validated and the physical temperature criterion applied literally, the all-replicas temperature condition would fail. Do **not** overwrite the historical verdict: distinguish its implemented reading from a physically calibrated reanalysis.

For T9, replacing g_m = 3.5 by its candidate mean demon energy 3.024 changes the simplified estimate C* = N/3.5 to N/3.024. It also needs the graph's thermal energy and the seed in the energy balance. However, T9's main `BONFIRE WITH A THRESHOLD` score is based on endpoint classes and the C grid, not on whether that numerical estimate is exact. A thermometer correction alone does not erase the empirical transition from disordered to mostly flat-like products as C increases.

Similarly, T18's `PROPORTIONAL` verdict is based on the smallest C with a majority of sheet-classified endpoints. Its numerical C values are not changed by relabeling the temperature axis. Its explanation as a precise heat-capacity law is weakened, and its geometric endpoint classification needs a separate audit.

An additional implementation detail is worth correcting in future analysis: `run_sealed_sheet_budget.py` calls the otherwise appropriate inversion function with spacing `4*lambda`. At lambda = 1.25 this is five, although valid energy changes need not be multiples of five. The argument passed to a thermometer must represent the reachable spectrum, including any offset or disconnected sector; the surplus coefficient alone does not establish that spectrum.

**Programme action:** recalibrate the bath diagnostics from stored time series or new explicitly diagnostic runs; correct the temperature comparison in paper 2; and retain the measured conservation and endpoint data. Canonical runs with an externally supplied g, including T19/T25/T37/T51/T53/T56, do not inherit this thermometer error.

## 2. The counting diagnostic propagates into geometry, defect selection, and the energy rule

**Relevant code:** `src/graphity/dimension.py`; `scripts/run_sealed_curled_d.py:52–80`; `scripts/analyse_t30.py`; `scripts/analyse_t37.py:end_state, leftovers`; `scripts/analyse_t48.py:38–58`; `scripts/analyse_t53.py:class_of`; `scripts/analyse_t55.py:50–70, 101–122`; `scripts/analyse_t56.py:one_space`; `src/graphity/sealed_tie_d.py:follow, table_total`.

### The issue also occurs at six links

The previous paper review found a four-link d = 2 vertex that was locally different from the flat lattice. I checked the six-link case directly. A valid switch on the 4 × 6 × 6 torus produces d = 3 vertices with incident square counts

\[
[3,4,4,4,4,5],
\]

rather than the flat lattice's [4,4,4,4,4,4]. The witness switch is `(0,36),(2,38) -> (0,38),(2,36)`, with Delta S = -8, Delta X = -14 and Delta H = 58 at lambda = 1.25. The script constructs it and checks it with the kernel.

This matters for T48 and its descendants. Their `OPENS` classifier uses the fraction at d = D and the largest connected component at d = D. T56's `ONE SPACE` condition adds whole-graph connectedness and a 90% largest d = 3 region. Those are stronger than a histogram alone, but they still do not prove flat local order, torus topology, absence of shortcuts, or opening of an independent geometric period.

These scores remain well-defined measurements. The correction is to the interpretation: **“a connected region dominated by the designated square-count signature”** is supported; **“one flat three-dimensional space”** needs more diagnostics. Nor does this counterexample show that any specific reported OPENS majority would change under a stronger diagnostic. That requires checking the saved graphs.

### Flat-labeled vertices can carry defect energy

This is not just a hypothetical classifier issue. I read `results/t37_lam125_g125_L1024_a_adj/N4096_rep0.npz`, one cold endpoint used by the relic/hidden-count track. Using the programme's own per-vertex energy convention,

\[
e(v)=16-2\sum_{e\ni v}S_e+2\lambda\sum_{e\ni v}(S_e-2)_+,
\]

I obtained:

| Support | Energy |
|---|---:|
| Vertices with d = 1 | 96 |
| Vertices with d = 2 | 110 |
| Other d values | 0 |
| Whole graph | 206 |

There are **44 d = 2 vertices with positive energy**. Thus identifying the complete defect support with `d != 2` omits over half this graph's residual energy under that energy allocation. This is not a conservation failure; summing all vertices gives H exactly.

T37/T51's full H remains correct. But their “columns” are cores selected by a count, not automatically complete isolated energetic objects. T55's energy summed over the selected piece should be called **energy assigned to the selected core**, not the total energy of the defect including its neighborhood. The arbitrary choice of how to allocate an edge term between endpoints is another reason to define object energy through a full graph comparison.

T52 counts graph-distance windows around selected cores and therefore can include their neighbors. Its enumerator need not be wrong. What needs review is whether the selected core/window and the corresponding flat control define the physical object and boundary intended by the hidden-entropy claim. Do not alter a running count merely to obtain a desired result.

### The direction tie uses d in the Hamiltonian

The follow tie and table tie are exact functions of d. Their implementation may be entirely correct as count-dependent energies. But d is not a general count of physical axes that are open or curled in an arbitrary damaged graph. Consequently, the claim that this term implements “the three directions tied together” is a physical interpretation beyond the verified rule.

For example, a nonflat vertex with d = D receives the same tie price as an ideal flat vertex. The table also assigns zero extra tie price to d > D. That provides routes through damaged/count-degenerate states which cannot be understood just by pricing the ideal Cartesian-product ladder. Exact wall calculations still price the chosen Hamiltonian; they do not prove that its low-cost routes represent a geometric opening.

**Programme action:** before interpreting T56 or using it to choose the next physical mechanism, add reported diagnostics for edge square-count distributions, square-incidence links, whole-graph connectivity, and geometric periods/shortcuts. Keep the registered count-based scores beside the stronger diagnostics. Treat a changed geometric definition as a new analysis or new hypothesis, not a retroactive replacement gate.

## 3. The “fully curled gas of cubes that never join” conclusion is too strong

**Affected record:** `ASSUMPTIONS.md:O85`; `REFERENCES.bib:Mul79`; `docs/papers/programme_draft.md:30, 165`; the choice to replace a fully curled precursor by the connected rod/slab in VISION Updates 42–47.

The cited result says a connected (0,2)-graph of degree k has at most 2^k vertices, with equality only for the k-cube. The repository's own reference note states the upper-bound/equality distinction. It does **not** say every such graph is a cube. O85 itself mentions the four-link 14-vertex exception, but later argues that a gas of cubes is the only fully curled arrangement at the larger sizes. That last step does not follow.

I constructed the **folded 6-cube**, Q6 with antipodal vertices identified. It has:

- 32 vertices, six links at each vertex, and one connected component;
- a bipartition, with all distinct pairs sharing zero or two neighbors;
- d = 0 at every vertex;
- S = 120, X = 96, and H/N = 12(lambda - 1), the same ideal fully saturated energy density as Q6.

Four copies give a valid 128-vertex fully curled graph with four 32-vertex components and no 64-vertex Q6 component. The construction and graph properties agree with [Brouwer's mathematical description](https://aeb.win.tue.nl/drg/graphs/Folded-6-cube.html); the check script independently verifies the common-neighbor counts. This is an exact counterexample to “the only fully curled arrangement there is at those sizes is a gas of cubes.”

There is a second, separate correction. Starting with **two ordinary Q6 cubes**, an allowed cross-component switch joins them into one connected 128-vertex graph. It has Delta S = -10 and Delta X = -32, hence

\[
\Delta H=160-128\lambda.
\]

The cost is 19.2 at lambda = 1.10 and **zero at lambda = 1.25** in the untied model. The joined graph includes vertices with damaged/count-changing neighborhoods; it is not a fully saturated connected graph, so it does not violate the component-size theorem. It shows that the transition dynamics do not structurally forbid components from joining. A tie can add a further cost; this example does not claim zero-cost joining for every tied model.

**What survives:** a fully saturated connected component cannot exceed the stated finite size bound, assuming the cited theorem is applied with its actual hypotheses. A large graph which is fully saturated everywhere must have several components. The simulations' failure to make one large flat-like region under their tested conditions remains a measured result.

**What changes:** cube gases are one family of starts, not the entire admissible fully curled family; “never join” is not a universal restriction of the move set; and the assertion that an initially partly open rod/slab is the only possible route to a connected product is not established. The decision to study rod/slab starts can remain a useful experimental choice, but its structural justification needs correction. This does not rescue the failed all-directions-opening prediction: it identifies a false elimination of alternatives.

## 4. T38 already qualifies the memoryless story, but does not identify two physical populations

**Relevant record:** `PREREGISTRATION.md:T38`; `ASSUMPTIONS.md:O84`; `scripts/analyse_t38.py`; programme piece 2; the older series-plan summary that attributes failures only to a tight CV band.

I reproduced the local T38 analysis:

| lambda | N | Recorded waits used | Blank waits omitted | Tail count beyond 10 robust scales | Recorded at sweep 205 | Registered cell reading |
|---:|---:|---:|---:|---:|---:|---|
| 1.25 | 64 | 3,942 of 4,000 | 58 | 2 | 342 | UNCLEAR |
| 1.25 | 192 | 1,000 of 1,000 | 0 | 1 | 87 | NO TAIL |
| 1.30 | 64 | 3,868 of 4,000 | 132 | 14 | 609 | TAIL |
| 1.30 | 192 | 1,000 of 1,000 | 0 | 5 | 174 | TAIL |

The combined registered verdict is **TWO POPULATIONS**, as O84 records. The raw conclusion is that the **detected waits** deviate from a single-exponential description under this score. The paper's directly counted first-exit result can still be correct; these are different stopping times.

The mixture fit also produces a short component with a time scale of roughly 10–14 sweeps, representing about 12–22% of used waits. This is a fit to `waiting - 200`. Many observations are fixed at the first allowed detector value, 205. Consequently, that short component has an immediate observational alternative: the recording floor and threshold behavior, rather than a distinct physical population that opens in ten sweeps. The true departure may have occurred much earlier in the initial watch.

The tail threshold uses a scale estimated from the same data. The fit uses continuous exponential components despite discrete observations and an atom at the recording floor. The analyzer also omits blank waits. A physical two-population inference needs an observation-aware null, explicit handling of those blanks, and classification of waiting graphs. This does not justify erasing the registered TWO POPULATIONS score; it limits what its name establishes.

**Downstream effect:** T37 estimates a nucleation rate from the time of its first counted patch and plugs it into a one-dimensional nucleation-and-growth calculation. If the initial waits, patch detector, or successful excursions have multiple time scales, a single rate cannot be carried over without checking the event definition. T37's warm seed-count prediction already fails and its melting correction is recorded. Those are real constraints, not failures to be explained away by the original first-exit law.

**Programme action:** reconcile first-exit, successful-departure, detector, and first-counted-patch clocks before claiming a universal nucleation rate. Read the saved waiting graphs before another expensive waiting-time experiment. Bring the series plan/README summaries into agreement with O84 and the distinction between original and amended scores.

## 5. Front speed, local heat, and the physical-time track need stricter boundaries

**Relevant code:** `scripts/run_front_speed.py:1–17, 59–64`; `scripts/analyse_t47.py:read_front`; `scripts/run_front_matter.py:opened_columns, sides`; `src/graphity/sealed.py:145–150, 210–227`; `src/graphity/sealed_d.py:28–31, 53–57, 90–96`; `src/graphity/spark.py:local_stores`.

T47 infers per-front displacement from fL/2. This assumes one seed, two contiguous spreading boundaries, fixed circumference, and square loss attributable to that conversion. The earlier review showed why a connected patch or square count alone does not establish those assumptions. A nearly linear f(t) is a measured conversion rate; it is not automatically a measured geometric interface velocity.

T50 improves the spatial bookkeeping by recording columns on the two sides of the original seed. But a column is called open if three of its four vertices have d = 2, and progress is a count of such columns, not the location of a contiguous boundary. Scattered openings and changes in wiring can produce the same count. Its paired result, that the count advances faster in the energized treatment, is not therefore proof that matter alters a physical clock or that a maximum propagation speed exists.

There are two further concrete limits of the “local” bath:

1. A move pays from u1's store, but **u2 is drawn from the entire side of the graph**. Energy is anchored to one vertex label; the move itself is not constrained to a bounded spatial region. Accepted switches can create long links. A size normalization of the Monte Carlo clock does not impose a physical light cone.
2. Only side-0 stores can pay or receive energy. The mean returned by the kernels divides the total by all N stores, including N/2 inert side-1 stores. If those inert stores start empty, the active-store mean is twice the returned mean. It would still need the discrete-spectrum and equilibration corrections, and local stores need not share one common temperature.

T50 initializes the band energy in **every vertex's store**, including side 1. Half of that initial budget cannot participate in the switch dynamics. Its recorded total energy includes this inert contribution correctly, so conservation is not broken. But its energy-per-point axis and the comparison between band energy remaining and energy that can accelerate conversion need to identify the accessible half.

**What survives:** the recorded progression of f and the chosen column signature, the paired treatment difference, and the fair-clock algebra for proposal frequency. T51's use of the fair clock is also explicit and testable; it does not by itself derive physical time or guarantee that one time rescaling collapses all kinetics. Its P1 failure is already on the record.

**Programme action:** add direct boundary histories, connectedness checks, and a census of long links; label local energy as vertex-anchored rather than spatially local dynamics; separate active/inert bath energy; and keep “time” or relativity as an untested physical interpretation. These diagnostics can first use existing saved data where available.

## 6. The exact barrier calculations do not supply a complete higher-dimensional opening mechanism

**Relevant work:** T30/T32/T33/T39–T46/T48/T49, the ideal tied-energy ladders, O103(b), and the proposed T54 critical-patch test.

A smallest positive single-move cost is an exact property of a starting graph and move set. A minimum activation budget for a **successful full conversion** concerns paths with several moves, energy redistribution, possible healing, and intermediate maxima. Neither the exact ideal-state energy ladder nor a first-exit barrier determines that path barrier.

The programme has partly recognized this: O103 explicitly limits the fixed-push result to a tube with fixed transverse extent, and T54 is intended to price a growing patch. That correction should be kept. However, assertions that the tube has no critical nucleus, or that a slab barrier must diverge as lambda approaches one, are still theoretical interpretations requiring a derivation for this graph move set. They do not follow solely from the counted first move or continuum nucleation intuition.

The latest T56 test can be valuable for the chosen count-dependent Hamiltonian. Its canonical g is externally specified, so it is not affected by the demon thermometer. Its single-move wall table remains arithmetic. But an OPENS/ONE SPACE verdict needs the geometric qualification in section 2, and a failure cannot cleanly distinguish a geometric mechanism from a count-based tie until those diagnostics exist.

**Programme action:** prioritize the actual path/commitment calculation and validated geometry over another fit of ideal-state release shares. Preserve the existing failed predictions and tested starts; do not declare a new tie physically successful merely because its count-based acceptance and score are internally consistent.

## 7. Gravity, quantum counting, and cosmological interpretation: what is actually exposed

### Symmetry sampling and quantum counting

`src/graphity/interchangeable.py:71` implements

\[
\min\{1,e^{-\Delta H/g}A(G')/A(G)\},
\]

and `interchangeable_d.py:116–117` forms the same product before clipping. Their sealed versions use the symmetry ratio on the extended energy shell. Thus the acceptance-order warning in the first review is a **paper explanation issue**, not a demonstrated bug in T21/T42/T49. No blanket rerun is warranted on that basis.

Exact automorphism and hidden-wiring counts also survive as counts for the declared state space. Uniform unlabelled-class weighting is a choice of measure; it is not forced by quantum indistinguishability. Correct the N-versus-log-N effective-barrier discussion, but do not discard correctly computed weights.

The claim that classical counting supplies interference, phases, the Born rule, or Bell correlations was already an uncompleted branch. These paper errors do not supply the missing quantum dynamics, and they do not newly falsify all mathematical work on counts. The relevant question remains what physical meaning, if any, the declared count and boundary have.

### Gravity

The exact additivity of the stated local energy for suitably separated fixed defects does not depend on the first-exit waiting law or demon thermometer. Neither do fixed-wiring Laplacian/Green-function computations. Those calculations remain applicable to the graphs and source choices actually used.

However, the identified source region and its inferred “mass” need the support check in section 2. Also, the assertion that a cheapest graph switch of cost 32/64/128 establishes a spectral or correlation gap is not a theorem. The gravity paper explicitly acknowledges that its analogy with a quantum lattice gap is unproved; compressed programme summaries should not promote it into a reason to close every entropic-force route before measuring the actual correlation length.

Static pair-energy additivity limits the proposed bare-energy force. It does not establish the absence of entropic interactions when the surroundings fluctuate. Conversely, an exact hidden count is not a demonstrated long-range force. The planned warm-background correlation measurement remains the correct intermediate question, with geometric and equilibration checks.

### Dark matter, dark energy, and fertility

Ideal release arithmetic is not changed by these corrections. Residual H and bath energy still balance. But converting a selected relic count into a physical abundance requires the complete object/background definition, its survival probability, size scaling, and a physical cooling/expansion history. “One relic per seed” was already rejected as a literal rule, and the newer T51 cooling result makes a fixed universal surviving share still less defensible.

A window in the algorithm where a precursor persists and a product stays mostly flat-like is not a measured fertility function or a universe-production rate. Its persistence edge changes with the clock and observation horizon; its product criterion uses the geometry proxy. That limits extrapolation from lambda maps to an optimal cosmic coefficient.

These issues constrain evidence for the hypothesis. They do not, by themselves, decide the hypothesis about reality. The toy still has no calibrated cosmological time, expansion, black-hole mechanism, or conversion from its dimensionless energy to observed particle/dark-sector quantities.

## 8. Papers and records needing attention

| File or track | Specific revision/reanalysis |
|---|---|
| `curled_torus/paper.tex` | Apply the first review's distinctions; include T38 as later detected-decay evidence if updating the paper |
| `relic/paper.tex` | Correct “bath near g = 0.5”; separate core count, object energy and geometric identification; retain existing annealing observations |
| `fertile_window/paper.tex` | Distinguish operational persistence, ideal energy ladder and full conversion; qualify fronts and temperature/capacity interpretations |
| `six_links/paper.tex` | Audit d = 3/4 geometry labels, cascade path claims and selected starting-family scope |
| `black_hole/paper.tex` | Retain correctly implemented weighted runs; qualify fold/melt classifiers, temperature axes and extrapolation beyond tested setups |
| `gravity/paper.tex` | Preserve exact fixed-wiring results; do not equate switch barriers with a proven correlation gap; identify complete defect/source support |
| `programme_draft.md` | Replace the universal “gas of cubes/never join” claims; distinguish geometric order from counts; qualify time/seed/release interpretations |
| `series_plan.md`, README, VISION summaries | Reconcile older “memoryless/one front/established” summaries with T38, amended energy gates, and later failed tests |
| T51/T55/T52 | Report stronger local-order/support diagnostics without changing historical scores or the running enumerator's definition |
| T53/T56 | Keep the canonical runs as planned; score their fixed rules, then add geometry diagnostics before calling an endpoint one flat space |

## Practical next steps, in order

1. **Correct claims already contradicted by exact examples.** A saturated graph need not be a cube; joining is an allowed transition; d = D need not be flat local order. Record the distinction between theorem, measured negative result, and interpretation.
2. **Calibrate the demon bath.** Reconstruct accessible spectra, distinguish active/inert stores, assess stationarity, and reanalyze temperature-based statements. Retain original data and historical verdicts.
3. **Audit saved geometry before spending on more mechanisms.** Begin with the graphs underlying clean/OPENS/ONE SPACE labels and the relic cores. Edge square counts and rooted square-incidence links are cheap; periods, topology and shortcuts address stronger claims.
4. **Audit the detector and waiting graphs.** Preserve T38's registered score, but distinguish its observed mixture from physical populations and the direct first-exit law.
5. **Reassess the front/time track.** Count actual connected boundaries and histories, and state the global proposal rule. Correct the accessible-energy accounting in T50's interpretation.
6. **Update shared summaries together.** Avoid leaving stronger “established” claims in the programme/series plan after narrowing the papers. Preserve the dated old statements and explain replacements rather than silently rewriting history.

The defensible programme remains a set of exact graph-energy calculations and finite, declared stochastic experiments. The work most exposed by this audit is the promotion of those measurements into geometry, temperature, physical time, and unique precursor structure. Most of the immediate repair can start with existing data and cheaper diagnostics, without discarding or rerunning the entire programme.

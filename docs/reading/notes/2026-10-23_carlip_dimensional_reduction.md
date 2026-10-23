# Reading note: Carlip, "Dimension and dimensional reduction in quantum gravity" (2026-10-23)

**What was read, and how.** arXiv:1705.05417 **v2** (dated 29 May 2017 on the arXiv stamp; the abstract page lists v1 of
15 May 2017 and v2 of 29 May 2017 as the current version, with the comment that v2 "added many references and made minor
clean-up"). Read in full by an assistant agent on 2026-10-23 from the arXiv PDF (34 pages, all loaded; text extracted with
pypdf). The abstract page was fetched for the version history; it gives the DOI 10.1088/1361-6382/aa8535 but no journal
line, so the journal reference "Classical and Quantum Gravity 34 (2017) 193001" in this note's title is the task brief's,
checked only against that DOI's journal prefix (1361-6382 is Classical and Quantum Gravity). No HTML rendering was
fetched; none was needed. Nothing failed to load. The extraction inserts stray spaces inside words and splits ligatures;
quotations below have had only those repaired, and were checked by eye against the page. The author's em-dashes inside
quotations are shown as " -- " so that this note contains none of its own; nothing else in a quotation is altered.

**Who has read it.** The assistant agent. The owner has not. Nothing here has been reviewed by a physicist.

**Labels.** Text in quotation marks with a section number is verbatim from the paper. Unmarked prose under a heading is
paraphrase of the section named. Anything labeled *Ours, unverified* is this note's own reading, made here, and is not
in the paper.

## Terms, defined once

- **Dimensional estimator**: Carlip's word for any measurable quantity that depends on dimension in a simple way, used
  to assign a dimension where the usual meaning is unclear (Sec. 2).
- **Hausdorff dimension** (also called fractal dimension): a dimension read from how volume or covering count grows
  with size. If a ball of radius r has volume growing like r^n, n is the dimension at that scale (Sec. 2.1, "Scaling").
  On a graph this is volume growth: how many points lie within k steps of a point.
- **Spectral dimension**: a dimension read from a random walk. Start a walker at a point and ask how likely it is to be
  back at its start after a time s; on an ordinary d-dimensional space that probability falls like s^(-d/2), so the
  rate of fall gives d. Carlip's Eq. (2.7) defines it as a function of the walk time s, so it can differ from one scale
  to another.
- **Walk dimension**: a dimension read from how fast a random walker's distance from its start grows with time
  (Eq. (2.8)). Not independent: "it can be shown [34, 36] that dW = 2dH/dS, where dH is the Hausdorff dimension"
  (Sec. 2.1).
- **Holography** (not Carlip's term; defined here because the owner's question of 23 October uses it): the idea, from
  black hole thermodynamics, that the information in a region of space is bounded by the area of its boundary rather than
  its volume, so that a theory in d dimensions can be described by one in d minus 1. **The words "holography",
  "holographic", "area law", "entanglement" and "Bekenstein" do not occur anywhere in this paper** (searched in the
  extracted text).
- **Asymptotic silence**: Carlip's second candidate "common thread": a limit in which "light cones collapse to lines, and
  nearby points become causally disconnected" (Sec. 4.2).
- **Kasner space**: an exact but anisotropic solution of Einstein's equations in which different directions stretch and
  shrink at different rates; used in Secs. 2.1, 3.6 and 4.2.

## (1) What "dimensional reduction" claims exactly

**The claim is about effective dimension measured by estimators, flowing with scale. It is not a claim that the
fundamental degrees of freedom are two-dimensional.**

Abstract (verbatim): "A number of very different approaches to quantum gravity contain a common thread, a hint that
spacetime at very short distances becomes effectively two dimensional. I review this evidence, starting with a discussion
of the physical meaning of 'dimension' and concluding with some speculative ideas of what dimensional reduction might
mean for physics."

Sec. 1: "hints have emerged from quantum gravity suggesting that the dimension of spacetime is dynamical and
scale-dependent, and shrinks to d ∼ 2 at very small distances or high energies."

Sec. 1.1 puts its strength beside the one commonality he does trust: "Dimensional reduction of spacetime near the Planck
scale is a candidate for second such commonality, albeit one that is much less firmly established." (The first is black
hole thermodynamics.)

Sec. 2 says the word itself is not single-valued: "A number of rather different possibilities exist, and different
choices need not always agree. Dimension may depend on exactly what physical question we are asking." And: "if our smooth
spacetime is somehow emergent at large distances, as many approaches to quantum gravity suggest, then its dimension, too,
should be emergent."

Sec. 2 lists the estimators in two families. Mathematical: topological (inductive, covering: integers, "too primitive and
too far removed from observation"), scaling (box-counting, Hausdorff, and for graphs Requardt's "internal scaling
dimensions" [27]), random-walk (spectral and walk), Lorentzian (causal spectral dimension, Myrheim-Meyer, midpoint
scaling), and geodesic ("a random geodesic will 'see' fewer than the full d − 1 dimensions"). Physical: thermodynamic
(four of them, from free energy, energy density, equation of state and equipartition), Green's function, Unruh detector
response, and the anomalous scaling dimension of quantum field theory. Sec. 2.2.1 notes that the thermodynamic estimators
agree in flat space but "there are known examples in which they different [sic] from each other [48, 49]."

Sec. 3.9 is the clearest statement that the measured "2" need not be a change in what spacetime is made of: "The models
I have described are defined on ordinary four-dimensional manifolds, and while the reduction of spectral dimension takes
place at high energies, it is essentially classical. ... The moral, perhaps, is once again that one must be very careful
about exactly what one means by 'dimension' -- different choices of how to measure dimension can give different results,
which may not always reflect our intuition of what the dimension 'really' is."

The only place a *fundamentally* two-dimensional theory is proposed is the last paragraph of Sec. 6, and it is marked as
a dream: "Or perhaps we should be more radical. In [155] it is proposed that we should start with a fundamental
conformally invariant two-dimensional theory, from which the added dimensions of spacetime emerge after conformal
symmetry-breaking. This is so far only a dream (though it is oddly reminiscent of the Polyakov approach to string
theory [210]), but it could be a dream worth pursuing."

*Ours, unverified:* the statement the model's author made to the owner on 23 October (that nearly all models of quantum
gravity agree gravity's fundamental degrees of freedom are two-dimensional and the third dimension is emergent) is
stronger than anything this review asserts. Carlip's claim is that many approaches give an *effective* dimension near 2
at short distances by *some* estimator, that the estimators disagree, and that the evidence is "much less firmly
established" than black hole thermodynamics. He does not say the degrees of freedom are two-dimensional, and the one
proposal that they are is labeled a dream. Whether the author's statement rests on other literature (holography, which
this paper does not discuss) is not something this note can judge.

## (2) Which approaches show it, on what evidence, with Carlip's caveats

Paraphrase of Sec. 3, one row per subsection, with his caveat in his words where he gives one.

| Sec. | Approach | What is reported | Estimator | Carlip's caveat (verbatim where quoted) |
|---|---|---|---|---|
| 3.1 | High-temperature string theory (Atick and Witten 1988 [18]) | Above the Hagedorn temperature the free energy goes as T², so the thermodynamic dimension falls to 2; Atick and Witten said the system behaves "as if this system were a (1+1)-dimensional field theory" | d_th1, and he checks d_th2, d_th3 | "This dimensional reduction occurs for strings in a flat background. It may differ in other settings"; exponential fall of fixed-angle scattering is "only hints of interesting behavior" |
| 3.2 | Causal dynamical triangulations [19] | Spectral dimension 4 at large scales, "drops to dS ≈ 2 at small scales"; a 3D version drops from 3 to about 2 [69]; checked independently [70, 71], verified analytically in a toy model [72] | spectral | "Because of numerical uncertainty, the lower limit is not known exactly, and may be consistent with dS = 1.5 [71], but the occurrence of short distance dimensional reduction in this approach is unambiguous." Euclidean DT with a tuned measure [73]: falls to about 1.5, "the simulations so far are quite coarse" |
| 3.3 | Asymptotic safety | At a non-Gaussian fixed point "operators at the fixed point will necessarily acquire precisely the anomalous dimensions necessary to make the theory appear two-dimensional [78–80]"; the spectral dimension shows "three scaling regimes": classical 4, quantum 2, and an intermediate regime "that depends on the truncation and the renormalization group trajectory" | anomalous (quantum Green's function) dimension; spectral | "Whether general relativity is asymptotically safe is a deep question, and we are far from a definitive answer." The argument: "the Einstein-Hilbert action is scale invariant only in two dimensions" |
| 3.4 | Causal set theory | Myrheim-Meyer dimension about 2 for sets of four to six elements [50]; generic (Kleitman-Rothschild) orders 2.38; sprinklings into Minkowski space fall to about 2 for small subspaces [39] | Myrheim-Meyer; causal spectral; Green's function | The causal spectral dimension of Eichhorn and Mizera [38] "increases at short distances", but their d'Alembertian "fails to reproduce the standard flat spacetime d'Alembertian"; with the "right" one it falls to 2 [51]; Green's function dimension falls to 2 "although there are some ambiguities in a choice of regularization" |
| 3.5 | Loop quantum gravity | Modesto's area scaling (3.2) translated into an effective metric gives a flow from 4 to 2; the same in spin foams [89] | spectral via effective metric; Hausdorff and spectral on spin networks | "the evidence is mixed"; "pure spin network states do not exhibit dimensional flow [91]"; superpositions can, but "the short-distance dimension depends on details of the superposition [92]"; loop quantum cosmology gives 2.5 [93] or 1 [94] depending on "model-dependent choices" |
| 3.6 | Short-distance Wheeler-DeWitt equation | The strong-coupling limit is ultralocal; solutions are locally Kasner with BKL bounces; the geodesic dimension "shrinks to dgeod = 2"; spectral dimension plausibly the same (Eq. (3.4)) | geodesic; spectral | "Now, Kasner space is certainly four-dimensional." The reduction is a resolution effect: at fixed return time s there is always an early enough time at which the second term of (3.4) dominates. The Wheeler-DeWitt equation itself "is almost certainly not quite the right way to quantize gravity" |
| 3.7 | Modified dispersion relations; noncommutative geometry | Polymer quantization gives 2.5 [49]; Snyder space gives 2 by three thermodynamic estimators [46]; doubly special relativity gives 2 "but the result depends on a free parameter [112]"; κ-Minkowski gives a reduction whose "limiting value again depends on a nonunique choice"; the Connes spectral action gives 0 [118, 119], a variant gives 2 [120] | thermodynamic; spectral; Green's function | "This gives us an uncomfortable amount of freedom -- we can choose any scale dependence of dimension we like, and build by hand a suitable dispersion relation" |
| 3.8 | Minimum length | A smeared starting point for diffusion gives d/2 at the minimum length [123]; a "quantum metric" gives box-counting dimension 2 [124]; generalized uncertainty principles give it through modified dispersion | spectral; box-counting | None stated beyond "a minimum length is not a universal feature of quantum gravity, but it is a common one" |
| 3.9 | Modified gravity (Horava-Lifshitz, curvature-squared, nonlocal) | Spectral and thermodynamic dimensions fall to 2 | spectral; thermodynamic; Green's function | "they may also serve as cautionary notes": these are on "ordinary four-dimensional manifolds" and the reduction "is essentially classical" |
| 3.10 | Spacetime foam (Crane and Smolin; Haba; Carlip et al.) | Virtual black holes or stochastic metrics reduce the Hausdorff and Green's function dimension by an amount "that depends on the details of the distribution"; vacuum fluctuations collapse light cones in two spacetime dimensions [140] | Hausdorff; Green's function | The two-dimensional light-cone result: "It seems likely that this result can be extended to higher dimensions; see [143] for a first step" |
| 3.11 | Multifractional geometry (Calcagni) | A framework, "not so much a model of quantum gravity that predicts dimensional reduction"; it supplies the strongest observational constraints (Sec. 5) | any | By construction it incorporates scale-dependent dimension rather than deriving it |

His overall weighing, Sec. 4 (verbatim): "Taken individually, none of these hints is terribly convincing. Perhaps the
best evidence comes from asymptotic safety, in which the argument for two-dimensional behavior at the ultraviolet fixed
point is compelling, and causal dynamical triangulations, in which the evidence for flow of the spectral dimension is
extremely strong. But for this evidence to be truly persuasive, we would have to actually know that quantum gravity has
an interacting ultraviolet fixed point, as required by asymptotic safety, or that causal dynamical triangulations has the
right continuum limit; that is, we would have to know how to quantize gravity." And: "Taken as a body, though, these
hints become quite a bit more compelling. It seems rather unlikely that so many different approaches to quantum gravity
would converge on the same result merely by accident."

Sec. 5 on tests: "we do not yet have observational evidence". The CMB spectrum limits departure from 4 at the surface of
last scattering to "at most a part in 10^-5 [47]"; the electron's magnetic moment and the Lamb shift bound the Hausdorff
dimension at ordinary scales to within 5 × 10^-7 and 3.6 × 10^-11 of 4; multifractional models are constrained to a
reduction scale below 10^-17 m (or 10^-27 m for a particular choice). "It is not yet known, however, whether there are
features that would uniquely distinguish models with dimensional reduction from more conventional cosmologies."

## (3) Fundamental or artifact; and the holographic argument

**On fundamental versus artifact.** Carlip does not decide it, and he offers two candidate reasons for the pattern
(Sec. 4), each of which places the "2" somewhere different:

- *Scale invariance* (Sec. 4.1): at a fixed point "the theory becomes scale invariant. This, in turn, implies dimensional
  reduction, essentially because it is only in two dimensions that Newton's constant is dimensionless." Here the 2 is a
  property of the theory's behavior at short distances, read through anomalous dimensions, not a count of directions.
- *Asymptotic silence* (Sec. 4.2): "In this limit, light cones collapse to lines, and nearby points become causally
  disconnected. ... In a sense, this is a reduction to one dimension, but the process goes by way of two dimensions,
  since, as described in section 3.6, the decoupling of neighboring points leads to BKL behavior with dgeod ∼ 2." Here the
  manifold stays four-dimensional ("Kasner space is certainly four-dimensional", Sec. 3.6) and the 2 is what a geodesic
  or a diffusion at fixed resolution can see. Sec. 5 adds that in this picture "the preferred Kasner axis that picks out
  the local two-dimensional spacetime at any given point varies chaotically [166, 167]", so the reduction is
  "nonsystematic", with no single global choice of which two directions survive.

He also flags that reduction could signal a problem rather than a feature (Sec. 2.2.2): in theories with something like
a Källén-Lehmann representation "one must worry that dimensional reduction could indicate the appearance of negative-norm
states or a breakdown in quantum field theory [51, 53]", and "any theory of quantum gravity that predicts dimensional
reduction will eventually have to address this issue."

On Sec. 3.9's models, where the reduction is on a fixed four-dimensional manifold, his word is that it "is essentially
classical" and the results "may also serve as cautionary notes".

**On holography.** The paper contains no holographic argument. The word does not appear, nor do area laws, entanglement
or Bekenstein. The nearest things in the text are: (a) Sec. 6's "2+2" splitting of the metric, Eqs. (6.1) and (6.2), in
which the Einstein-Hilbert action "looks very much like a two-dimensional action for the transverse metric", with an
effective two-dimensional Liouville field "with a central charge c ∼ A⊥/ℓp²" (a central charge proportional to a
transverse area in Planck units), which he calls "still far from the whole story" because the metric (6.1) "exhibits a
'systematic' breaking of Lorentz invariance, with a global choice of longitudinal and transverse directions"; and (b)
Sec. 1.1's remark that black hole thermodynamics is the one established commonality among approaches. Neither is
presented as a holographic argument for two-dimensional degrees of freedom.

*Ours, unverified:* the REFERENCES.bib note written before this reading guessed, from general knowledge, that the
motivation for caring about d = 2 is that Newton's constant is dimensionless there. That guess is confirmed by Secs. 3.3
and 4.1 in almost those words.

## (4) How 3+1, motion, matter or gauge fields re-emerge at large scales

The paper says very little about this, and nothing about electromagnetism, gauge fields, or motion. What it does say:

- The one direction it treats at length is the *other* one. Sec. 1.2: in Kaluza-Klein theory "At larger scales, though,
  the compact dimensions can no longer be resolved, and the spacetime becomes effectively four-dimensional, with
  excitations in the compact directions appearing as towers of massive four-dimensional modes. The converse process of
  dimensional deconstruction [12], in which appropriate four-dimensional modes effectively 'create' extra dimensions at
  large distances, has more recently become popular in high energy theory. Here we are interested in the opposite
  phenomenon".
- In causal dynamical triangulations the large-scale 4 is *measured*, not assumed (Sec. 3.2, quoted under (5) below),
  and the program produces "a de Sitter ground state with the correct volume profile" and "the expected spectrum of
  quantum volume fluctuations [67]". That is the only place where a four-dimensional large-scale spacetime is reported to
  come out of a model that is two-dimensional at short distances, and it comes out because the model is built from
  four-dimensional simplices with a time direction, not from two-dimensional pieces.
- Matter: Sec. 3.3, "A variation of this argument shows that matter fields interacting with gravity at a non-Gaussian
  fixed point exhibit two-dimensional behavior as well [76]." Sec. 6: in the early universe reduction "would be reflected
  not only in the geometry, but in the structure of the quantum vacuum, the equations of state for matter, and
  thermodynamic relations." Nothing on how matter's three-dimensional behavior is recovered.
- Sec. 6 on what a theory would look like: "At the very least, it would suggest new formulations in which our four (or
  more) macroscopic dimensions are split into two sectors with different characteristic length scales." The 2+2
  splitting of Eqs. (6.1), (6.2) is offered as "an interesting place to start", with the eikonal scattering literature
  [205–207] as its source, and "A more general '2+2' splitting can be found in [209]".
- The "fundamental two-dimensional theory" of [155] is a dream (Sec. 6, quoted above); the paper gives no mechanism for
  how its extra dimensions, or anything in them, would emerge beyond the phrase "after conformal symmetry-breaking".

*Ours, unverified:* for the owner's question of 23 October (how a theory with two-dimensional fundamental degrees of
freedom recovers electromagnetism and motion in three dimensions) this review is not the place to look. It is a review of
how dimension is measured and of hints that the measured value falls, not of how a low-dimensional theory rebuilds the
large-scale world.

## (5) What bears on choosing a 4-regular over a 6-regular graph

The paper never discusses the degree (number of links per point) of a graph, nor any graph model of gravity other than
through Requardt's internal scaling dimensions on graphs [27] (one sentence in Sec. 2.1) and the simplicial complexes of
dynamical triangulations. What it says that bears on the question:

- **Dimension, in every estimator he uses, is read from random walks, volume growth, scattering or thermodynamics, not
  from the local connectivity of the building block.** Sec. 2.1: "In any space on which a random walk can be defined, the
  resulting diffusion process gradually explores larger and larger regions. More dimensions mean both slower diffusion --
  there are more 'nearby' points -- and a slower return to the starting point." Sec. 3.2: "It is easy to define a random
  walk on a simplicial complex, so a natural choice for a dimensional estimator is the spectral dimension dS of section
  2.1."
- **The dimension of the building block does not fix the dimension measured**, in his own words (Sec. 3.2): "The
  construction of a four-dimensional spacetime in causal dynamical triangulations starts with four-dimensional simplices.
  But this does not necessarily determine the large scale spacetime dimension; the path integral may be dominated by
  configurations that are not manifold-like or that have very different macroscopic appearances, and ultimately the
  dimension has to be measured." And on the older Euclidean triangulations: "the simulations typically yielded a
  'crumpled' phase with very high Hausdorff dimension and a two-dimensional 'branched polymer' phase [65]."
- **Reduction to 2 is reported from a three-dimensional starting point as well as a four-dimensional one.** Sec. 3.2:
  "if one starts with a three-dimensional model the spectral dimension drops from dS = 3 at large scales to dS ≈ 2 at
  small scales [69]." Sec. 5: "the hints of dimensional reduction in section 3 are largely independent of the number of
  starting dimensions, so we can begin with more than four dimensions and still ask about dimensional reduction to
  d = 2."
- The one place he touches the "count of perpendicular lines" notion of dimension (Galileo's, Sec. 2) is to say it is a
  starting intuition that mathematics and quantum mechanics showed "is not enough" (Sec. 2), and the thermodynamic
  equipartition estimator d_th4 is "the thermal analogy of Galileo's counting of perpendicular lines from a point"
  (Sec. 2.2.1).

*Ours, unverified:* three consequences for the toy, stated as readings and not as results. (a) The toy's own
dimension (the number of link pairs at a point that close no square: sheet 2, tube 1, 4-cube 0; `graphity.dimension`) is
a local combinatorial count. In Carlip's taxonomy it is closest to Galileo's count, which he treats as an intuition and
not an estimator; none of his estimators is a property of a point's degree. (b) Nothing in this paper argues against
building a model whose large-scale dimension is 3; the published three-dimensional triangulation model [69] is such a
model, and its reported short-distance value is about 2 by the spectral estimator. What the review would lead one to
expect of *any* quantum-gravity model, built from four links or six, is that its short-distance spectral dimension might
come out near 2, and that the number to compare is the measured spectral or volume-growth dimension at each scale, not
the degree. (c) The project's record already has the published model's own version of this: [T25] reports the random
phase with infinite Hausdorff dimension and the geometric phase with dimension close to 2 (VISION, "What X is", last
bullet), and TASKS T13 rung 1 plans to measure spectral and volume-growth dimension with our tools. Neither has been run
in the six-link model. If the six-link decision turns on dimension, that measurement is the one this paper's method
would ask for, and it is cheap.

## (6) References Carlip leans on most

From his reference list, with his arXiv numbers as printed. "Most" is read from how often and how centrally each is cited
in Secs. 3 and 4; the count is ours.

| Ref. | Who | What it is used for | arXiv |
|---|---|---|---|
| [19] | Ambjørn, Jurkiewicz, Loll, PRL 95 (2005) 171301 | the CDT spectral dimension flow 4 → 2, "the idea really took hold" (Sec. 1.2) | hep-th/0505113 |
| [69] | Benedetti and Hanson, PRD 80 (2009) 124036 | 3D CDT: 3 → 2 | 0911.0401 |
| [70], [71] | Kommu (2012); Coumbe and Jurkiewicz (2015) | independent checks; the lower limit possibly 1.5 | 1110.6875; 1411.7712 |
| [72] | Giasemidis, Wheater, Zohren (2012) | analytic verification in a toy model | 1202.2710 |
| [73] | Laiho, Bassler, Coumbe, Du, Neelakanta | Euclidean DT with tuned measure, about 1.5 | 1604.02745 |
| [76] | Niedermaier, CQG 24 (2007) R171 | asymptotic safety; matter fields two-dimensional at the fixed point | gr-qc/0610018 |
| [78], [79], [80] | Lauscher and Reuter (2002); Percacci and Perini (2004); Litim (2006) | anomalous dimensions at the fixed point make the theory look two-dimensional | hep-th/0108040; hep-th/0401071; hep-th/0606044 |
| [81], [82] | Reuter and Saueressig (2011); Rechenberger and Saueressig (2012) | spectral dimension under the renormalization group: three regimes | 1110.5224; 1206.0657 |
| [34] | Dunne, J. Phys. A 45 (2012) 374016 | heat kernels on fractals; dW = 2dH/dS | 1205.2723 |
| [36] | Calcagni, JHEP 1703 (2017) 138 | multifractional review; momentum-space Hausdorff dimension; constraints | 1612.05632 |
| [38] | Eichhorn and Mizera, CQG 31 (2014) 125007 | causal spectral dimension increases at short distances | 1311.2530 |
| [50] | Carlip, CQG 32 (2015) 232001 | Myrheim-Meyer dimension about 2 for tiny causal sets | 1506.08775 |
| [51] | Belenchia, Benincasa, Marciano, Modesto (2016) | the "right" d'Alembertian on causal sets gives 2; unitarity worry | 1507.00330 |
| [44], [45] | Carlip (2009, 2012) | the Kasner/BKL geodesic argument, dgeod → 2 | 1009.1136 (both as printed) |
| [140] | Carlip, Mosna, Pitelli, PRL 107 (2011) 021303 | vacuum fluctuations collapse light cones in 2D | 1103.5993 |
| [159] | Eichhorn, Mizera, Surya | causal sets break into disconnected "islands" at short distances | 1703.08454 |
| [88] | Modesto, CQG 26 (2009) 242002 | loop quantum gravity area scaling, Eq. (3.2) | 0812.2214 |
| [91], [92] | Calcagni, Oriti, Thürigen (2014, 2015) | spin networks: no flow for pure states; superpositions depend on details | 1311.3340; 1412.8390 |
| [48], [49] | Amelino-Camelia, Brighenti, Gubitosi, Santos (2017); Husain, Seahra, Webster (2013) | thermodynamic estimators differ; polymer quantization gives 2.5 | 1602.08020; 1305.2814 |
| [110] | Sotiriou, Visser, Weinfurtner, PRD 84 (2011) 104018 | any spectral-dimension flow can be rebuilt as a dispersion relation | 1105.6098 |
| [155] | Amelino-Camelia, Arzano, Gubitosi, Magueijo, IJMPD 24 (2015) 1543002 | scale invariance as fundamental; the "dream" of a 2D starting theory | 1505.04649 |
| [168] | the same four, PRD 87 (2013) 123532 | dS = 2 gives a scale-invariant CMB spectrum without inflation | 1305.3153 |
| [18] | Atick and Witten, Nucl. Phys. B 310 (1988) 291 | the first hint, high-temperature strings | none printed |
| [27] | Requardt, IJGMMP 3 (2006) 285 | scaling dimensions on graphs | math-ph/0507017 |
| [204] | Carlip, AIP Conf. Proc. 1483 (2012) 63 | the 2+2 splitting of Sec. 6 | 1207.4503 |

None of these has been read for this project. Of them, [19] is already in REFERENCES.bib as [AJL05] (unread).

## What it bears on for the six-link decision

The paper's position, stated without a recommendation: dimensional reduction is "a hint that spacetime at very short
distances becomes effectively two dimensional" (abstract), by estimators that are read from random walks, volume growth,
thermodynamics and scattering rather than from the local structure of any building block; the hint is "much less firmly
established" than black hole thermodynamics (Sec. 1.1), "none of these hints is terribly convincing" alone (Sec. 4),
and the estimators "need not always agree" (Sec. 2). The two candidate explanations he gives, scale invariance at a
fixed point and asymptotic silence, both leave the question of whether the short-distance 2 is fundamental open: the
first makes it a property of the theory's couplings, the second makes it a resolution effect on a manifold that stays
four-dimensional. The one proposal of a fundamentally two-dimensional theory is called "only a dream" (Sec. 6). The
paper contains no holographic argument and no discussion of the degree of a graph; it does say that the dimension of a
model's building block "does not necessarily determine the large scale spacetime dimension" and that "ultimately the
dimension has to be measured" (Sec. 3.2), and it reports the same reduction from a three-dimensional starting model as
from a four-dimensional one. What the paper supplies for the decision, then, is a vocabulary and a method: say which
estimator is meant, measure it on the model at each scale, and expect the short-distance value to be a measurement, not a
consequence of the number of links.

## Questions the paper does not answer

- **The owner's question of 23 October: how approaches with two-dimensional fundamental degrees of freedom aim to recover
  electromagnetism and motion in three dimensions.** Not addressed. The paper does not discuss gauge fields or
  electromagnetism at all (neither word appears), does not discuss motion, and treats the recovery of large-scale
  dimensions only in reverse (Kaluza-Klein, Sec. 1.2), in the measured CDT result (Sec. 3.2, where the large-scale 4
  comes from four-dimensional simplices), and in two sketches in Sec. 6 (the 2+2 splitting, and the [155] "dream" with
  "conformal symmetry-breaking" as its only stated mechanism). Where to look instead, from the paper's own references
  and not read by us: [155] (Amelino-Camelia, Arzano, Gubitosi, Magueijo, arXiv:1505.04649) for the fundamental-2D
  proposal; [204] (Carlip, arXiv:1207.4503) and [209] (Yoon, gr-qc/0003059) for the 2+2 splittings. The holographic
  route the model's author may have had in mind is not in this paper, and a separate reading would be needed for it.
- Whether the fundamental degrees of freedom are two-dimensional: left open, as above.
- Whether any of the estimators agree with each other away from flat space: he says they can differ (Secs. 2.2.1, 3.4,
  3.7) and does not resolve it.
- Whether the toy's "dimension" (pairs of links at a point closing no square) corresponds to any estimator here: not a
  question the paper could address; *ours* that it is closest to Galileo's count and is none of his estimators.
- Which graph degree a discrete model should use: not discussed.

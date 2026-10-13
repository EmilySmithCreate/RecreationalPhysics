# Observer-relative histories: records, observers, and what the toy models show

**Plain-language research draft**

**Status:** explanatory account of an exploratory research program. The calculations below are exact within their stated toy models; they are not physical experiments or evidence for a new theory.

## Where this belongs

This work is connected to **programme pieces 13 and 14**, not Paper 1.

- **Piece 13, “Interference and records: the rule the versions were missing,”** asks how ordinary quantum amplitudes and physical records relate to the project's earlier “versions” idea. Its key result is that the standard amplitude-and-record framework supplies interference and cancellation as an input; the graph model has not derived that rule.
- **Piece 14, “Observers inside the loop: who counts, and when we are,”** asks how observers with shared records should be treated and how any claim about when observers are typical depends on a declared sampling rule.

Together these pieces are the quantum-foundations part of the larger programme. They are distinct from the numbered graph-energy papers and their curled-torus simulations. Paper 1's results do not test these quantum claims.

## The question, in ordinary language

When a quantum system leaves a distinguishable mark in its surroundings, interference between the alternatives becomes harder to see in the system alone. If that mark is copied into several places, multiple observers can read it. If the mark is erased by reversing the interaction, interference can return in a small model.

The project asks what an observer-relative description adds: given the records an observer has retained, which histories in a chosen family are compatible with those records, and what probability measure do those histories carry? As records accumulate, the compatible set can shrink. That is ordinary conditioning expressed in the language of histories; it does not mean other branches are destroyed. The total measure of an exhaustive family remains normalized, but that fact alone is not evidence of decoherence—the sum rules for the histories are the relevant check.

The second question concerns observers and cosmic time. People who read the same physical record are correlated, so their reports cannot automatically be treated as independent. And “How typical is an observer at the present cosmic time?” has no single answer until the reference class and sampling rule are specified.

## What the project has done

The work is recorded in the [findings report](../../theory/orh_findings.md), with code under `src/orh/`, run scripts under `scripts/`, data under `results/orh_*`, figures under `docs/figures/orh_*`, and a literature map under `docs/theory/orh_stage_a_literature_map.md`.

### Literature review

The project mapped the relevant claims against fourteen papers on Everettian quantum mechanics, decoherent histories, physical records, quantum Darwinism, self-location, typicality, and cosmic-time observer measures. The existing project notes summarize these sources and flag assumptions or claims that still need expert review. The review found that the main candidate claims—nested record-compatible histories, shared observer records, and cosmic-time observer fractions—have close prior-work counterparts. The draft therefore presents this as an application and clarification of existing mathematics, not a discovery of new physics.

### Exact quantum toy calculations (Stages B–D)

These are small, deterministic state-vector calculations, checked against closed-form results in the code. They are **computational demonstrations**, not laboratory experiments.

- **Interference and environmental records:** in the two-path qubit model, visibility follows the overlap of the environment states. A perfect record removes the interference fringes in the system; undoing the record restores them in the toy. A conjugate-basis readout separates subensembles with restored visibility, while their aggregate visibility remains zero.
- **History probabilities:** a two-slit history family without a record has nonzero interference terms and fails the probability sum rule for the coarse-grained output. With a sufficiently distinguishing record, interference terms vanish and the sum rule holds. The example shows why “the total weights sum to one” is not, by itself, a decoherence test.
- **Accumulating records:** in a four-record example, the measure of the histories compatible with a particular sequence falls from 0.3 to 0.108 as records are added, while the family remains decoherent. This is the product rule for conditional probabilities, already present in the established framework—not a newly derived probability law. Erasing a record removes the corresponding historical decoherence in the toy.
- **Two observers:** when both read the same perfect record, their reports agree exactly. Multiplying their separate probabilities would incorrectly assign weight to disagreements. With imperfect records, the toy produces disagreements at the rates set by its chosen couplings.

The code and tests establish that the implementations reproduce these examples. They do not establish that the project's graph “versions” are Everettian branches, that its model derives the amplitude rule, or that a qubit register is a conscious observer.

### Cosmic-time population model (Stage E)

A separate deterministic calculation applies published stellar and habitability equations on a fixed cosmological background, with the project's explicitly chosen observer-window and reference-class assumptions. It reproduces the cited baseline result in kind, then shows how strongly the answer depends on those choices. In the red-dwarf-friendly scenario with a 4.5-billion-year delay and observers weighted by observer-moments, the calculated fraction of weight at or before 13.8 billion years is about **0.00085**; counting each inhabited planet once at its origin gives **0.81** for the same broad scenario. The latter is a different sampling rule, not a competing measurement of the same quantity.

The model's outputs are exact arithmetic on declared inputs, but the inputs are exploratory assumptions, not measured rates of life or observers. Several declared scenarios did not run exactly as originally planned; the findings report records that mismatch. With arbitrarily late exotic observers, the integral does not converge and the proposed late-time percentile is undefined. These results show sensitivity to assumptions; they do not predict when real observers should exist.

## What has not been done

No physical experiment has been conducted for this work. The exact quantum toy models and cosmic-time calculations have been run, and the source and tests are in the repository. No result shows that observer-relative histories add a new law, derive the Born rule, explain the felt passage of time, establish a preferred cosmic present, or yield a new falsifiable prediction. The two-turn test of record erasure at the proposed loop boundary remains proposed, not run.

## What to ask a UVA researcher over coffee

> “Pieces 13 and 14 apply established decoherence, record, and observer-sampling mathematics to my model. The qubit toy reproduces the standard amplitude-and-record rule, but the graph model has not derived it. What would be a useful next calculation or experiment to test whether the model contributes anything beyond that application?”

This is a foundations question with an adjacent experimental angle: a quantum-optics or quantum-information researcher may help identify a concrete record-writing/erasure setup or sharpen what the toy should compare. That does not imply the researcher works directly on this interpretation.

## Suggested reading for that conversation

Read the primary sources alongside the project’s notes; the notes are research aids, not substitutes for expert review.

1. **Hartle, “Arrows of Time and Initial and Final Conditions in the Quantum Mechanics of Closed Systems Like the Universe”** ([arXiv:2002.07093](https://arxiv.org/abs/2002.07093)): boundary conditions and time arrows. Project note: [arrows of time](../../reading/notes/2026-10-12_orh_copenhagen_and_arrows_of_time.md).
2. **Gell-Mann and Hartle, “Quantum Mechanics in the Light of Quantum Cosmology”** ([arXiv:1803.04605](https://arxiv.org/abs/1803.04605)): decoherent histories, records, and quasiclassical domains. Project note: [decoherent histories](../../reading/notes/2026-10-12_orh_decoherent_histories_gmh.md).
3. **Gell-Mann and Hartle, “Strong Decoherence”** ([arXiv:gr-qc/9509054](https://arxiv.org/abs/gr-qc/9509054)): strong decoherence and records.
4. **Zurek, “Quantum Darwinism”** ([DOI: 10.1038/nphys1202](https://doi.org/10.1038/nphys1202)): redundant environmental records. Project note: [quantum Darwinism](../../reading/notes/2026-10-12_orh_quantum_darwinism_records.md).
5. **Sebens and Carroll, “Self-Locating Uncertainty and the Origin of Probability in Everettian Quantum Mechanics”** ([arXiv:1405.7577](https://arxiv.org/abs/1405.7577)): self-location and probability. Project note: [Everett and typicality](../../reading/notes/2026-10-12_orh_everett_selflocation_typicality.md).
6. **Project results:** [ORH findings](../../theory/orh_findings.md) and [programme pieces 13–14](../programme_draft.md).

## One achievable next goal

Before coffee, read Hartle's 2020 paper with the findings report open. Make a one-page note separating (1) what the toy calculations verify, (2) what they merely reproduce from standard theory, and (3) what experiment or calculation could test the model's unresolved connection to amplitudes and records. Bring the question above and ask the researcher to critique that proposed next step.

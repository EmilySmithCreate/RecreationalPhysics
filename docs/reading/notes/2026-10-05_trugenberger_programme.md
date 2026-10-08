# The model author's programme, from his papers: reading notes (5 October 2026)

The owner asked what the model's author is currently working on, as his papers state it, to judge where her work
overlaps his. **Read by an assistant agent on 5 October 2026 from the arXiv HTML full texts, searching the text for
specific terms; the owner has not read these passages.** Figure images could not be displayed, so axis labels are
unverified. Keys refer to `REFERENCES.bib`. Nothing here comes from private correspondence.

## What exists

No paper on combinatorial quantum gravity newer than the review [T25] was found on arXiv or INSPIRE (v2 of the review,
29 April 2026, corrects two black-hole formulas and nothing else). Read in full: [T25] v2; [T24]; [T23]; the 2023 JHEP
paper on effective de Sitter space; [T22]. Read in part: [KTB19] (parts of the introduction, Secs. 3.3.2, 4, 5).

## The order of the transition, in print

- Continuous throughout. [T25], Introduction: "The transition from random to geometric phase is continuous and
  driven by the condensation of short cycles". Its Fig. 3 (N = 160): "Note the absence of hysteresis, as expected for
  a continuous phase transition."
- The words "hybrid", "mixed", "nucleation", "latent heat" and "compactif-" occur in none of the texts searched.
- With the global term only: "a first-order phase transition in which the graph decomposes into isolated, weakly
  interacting hypercubic complexes" ([T25] IV.1).
- For D = 3 nothing is said about the order of the transition or about hysteresis. [T22] calls the D = 3 transition
  "clearly identified"; a 2023 footnote says "computational limitations have permitted numerical studies only in 2D."

## What he says is missing

- [T22]: "assuming that its nature can be further cemented by large-scale numerical simulations presently out of reach
  of the available computational resources"; "We expect that resources at high-performance computing centres may be
  sufficient to address at least the 3D case."
- [KTB19]: finite-size scaling is "precluded"; "we are some way off the asymptotic regime".
- 2023: "the treatment of D>2 manifolds is beyond the scope of presently available numerical power".
- [T25], Fig. 6: "simulations at each value of N require months of CPU time".

## The D = 3 figure of [T22], literally (this bears on Gate C)

- Its Eq. (1) is a sum over vertices and, for each, over its neighbours: **each edge is counted twice.** Our six-link
  energy counts each edge once, and Gate C′ found that our curve matches the ordered side of the published one when our
  coupling is halved (O53). That factor of two is in the published equation.
- Its Eq. (3) writes the weight as exp(−S/(għ)) with S already carrying 1/g; read literally the coupling enters twice.
  The paper does not comment. (Gate C′ tested and rejected the 1/g² reading, O53.)
- The configuration space is "2D-regular graphs with independent short cycles". **The word "bipartite" does not
  appear**, and the text speaks of "possible residual triangle and pentagon defects". [T25], by contrast, says "one can
  use bipartite graphs" to make simulations cheaper.
- Fig. 3's caption in full: "Average number of squares per vertex as a function of the coupling constant għ for D=3.
  The maximum value for a cubic lattice is 12." **N is not in the caption**; N = 500 is stated only for another figure.
- Not stated anywhere: the algorithm, the number of sweeps, the starting state, the direction of the scan. "Monte
  Carlo", "Metropolis", "anneal", "sweep" and "hysteresis" do not occur.

## Allotropes, in his words

- [T24]: "Such domains, characterized by 0<s_i<s̄ are neither baryonic matter nor space but, rather, represent natural
  candidates for dark matter." Their lifetime is conditional: "depending on their free energy difference to the
  minimum and the barrier in between, may be extremely long-lived" ([T25]).
- No simulation of them in any paper. ([T24]: "no datasets were generated or analyzed".)
- The review's text says such domains have more squares than their surroundings; its Fig. 9 and [T24] show fewer.

## Other statements used elsewhere in this project

- Black holes: merged bubbles of the random phase; "Bubbles of random phase much larger than the Planck length are not
  stable" ([T25]).
- Time: a universal clock; "it is possible to identify 1/g itself with universal time" ([T24]).
- [KTB19] Sec. 3.3.2: the flat and the over-full ground states are separated by something "akin to the existence of an
  infinite energy barrier" as N grows.
- Open, in his words: network fluctuations ("an open and challenging problem"); how a cluster moves by elementary
  moves ("an open question"); cosmology ("still at a qualitative level").

## Where this project overlaps it (*ours*)

1. **The order of the transition in D = 2 by finite-size scaling**, at his exact rule: the test his papers call out of
   reach. This project has run it to 676 points (T6, T13, T16); the larger sizes did not equilibrate.
2. **Anything in D = 3.** His papers have one figure. This project's six-link runs at 500 points show cooling and
   heating disagreeing near g = 4 (our units), which his papers do not discuss; but the six-link code has not
   reproduced his figure, and three things the paper does not state stand in the way: the size, whether the graphs
   were restricted to two-sided ones, and the protocol.
3. **Allotropes.** His dark-matter proposal has no data. This project has the first we know of: they are transient in
   an equilibrated graph (T36) and a planted one dissolves at every coupling (T43).

A first-order result would cut against his programme, whose continuum limit needs a correlation length that diverges.

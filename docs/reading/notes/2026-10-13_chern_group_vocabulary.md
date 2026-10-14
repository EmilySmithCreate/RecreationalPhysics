# The Chern group's vocabulary beside ours, and where its work bears on the series (13 October 2026)

**Status.** Written by an assistant (Claude) on 13 October 2026 at the owner's request: she is considering
G.-W. Chern's condensed-matter theory group at the University of Virginia as readers of papers 1 and 2, and asked
for our wording to be matched to theirs where the same concept is meant. Quotations are exact, taken from the
arXiv HTML of each paper converted to text and searched; section numbers are the papers' own. Everything marked
*ours* is an AI's reading, unverified; no physicist has reviewed any of it. Keys refer to `REFERENCES.bib`.
Nothing here has been sent to anyone, and nothing here is evidence for the hypothesis (rule 13): a published
vocabulary that fits is a way to be understood and checked, not a confirmation.

## 1. What was read, and how

| Key | arXiv | What was read |
|---|---|---|
| [JC26] Jang, Chern | 2602.05815 | The whole text |
| [JYC25] Jang, Yang, Chern | 2512.07744 | Abstract, Sec. V; searched for its dynamics |
| [BBJC26] Bora, Bakshi, Jang, Chern | 2609.28436 | Abstract; searched for "apparent exponent" |
| [LLC26a] Le, Lee, Chern | 2604.18902 | Abstract; searched for its definitions |
| [LLC26b] Le, Lee, Chern | 2601.05933 | Abstract; searched |
| [BaC26] Bakshi, Chern | 2609.12661 | Abstract only |
| [BBM26] Bose, Bakshi, Majumdar | 2606.24800 | Abstract, Introduction, Secs. IV and V |
| [BFC26] Bakshi, Fan, Chern | 2602.03761 | Abstract only |
| [YC24] Yang, Chern | 2406.11755 | Abstract only |
| [FZC26] Fan, Zhang, Chern | 2601.07583 | Searched for nucleation and interface |
| [dCZ14] del Campo, Zurek | 1310.1600 | Searched for "freeze-out" (not the group's; for one clash of terms) |

The group's forty most recent arXiv papers (the arXiv API listing of 13 October 2026) were scanned by title.
The largest groups among them: defects, quenches and melting in electron-lattice models; machine-learned force
fields for making such simulations large; frustrated magnets and their energy landscapes. Chern has a recent
paper with M. Vucelja (2609.30025), who is named in the series plan for paper 1.

## 2. The same concept in two vocabularies

"Used" says where the term was added on 13 October: P1 is `docs/papers/01_curled_torus/paper.tex`, P2 is
`docs/papers/02_relic/paper.tex`.

| Ours | Theirs | Where they say it | Used |
|---|---|---|---|
| sealed (run, box, system) | an isolated system "with strictly conserved total energy"; "Hamiltonian or microcanonical" dynamics | [JC26] abstract, Sec. II | P1, P2 |
| the stores, in a sealed run | an "internal bath" or internal reservoir: degrees of freedom inside the isolated system that exchange energy with the ordering ones "without energy dissipation" | [JC26] abstract, Sec. IV | P2 |
| a bath at fixed coupling g | coupling to an external thermal bath or "thermal reservoir"; dissipative dynamics | [JC26] Sec. I; [JYC25] Sec. II | P2 |
| a seed (of the new arrangement) | a nucleus; nucleation | [JC26] Sec. III: "a nucleation-and-growth process in which locally ordered regions emerge at random spatial locations and subsequently expand and coalesce into extended domains" | P2 |
| a front | the propagating wall or interface between the two phases | [FZC26] Introduction: a transition "initiated via the nucleation of" domains, "followed by the propagation of" the walls between the phases | P2 |
| a patch (flat patch, converted region) | a domain | [JC26] Sec. III | P2 |
| where fronts meet | where domains coalesce or merge | [JC26] Sec. III | P2 |
| relic, leftover, scrap, flaw | a defect | throughout | P2 |
| heals, anneals | annihilation, for their defects, which vanish in pairs; "anneals" is kept for ours | [JC26] Sec. IV | P2 |
| freezes in; "nothing moves" | arrested; frozen; "immobile" defects; "dynamically arrested" | [JC26] abstract, Sec. III.2 | P2 |
| the relic moves, or does not | defect mobility | [JC26] Sec. III.3 | P2 |
| a patchwork (T61) | a state of several domains separated by defects | [JC26] Sec. III.2: "fragments into multiple CDW domains separated by kinks or domain walls" | P1 |
| stuck; stable for now | metastable; "trapped near one of the metastable minima" | [JC26] Sec. III.2 | P2 |
| the wall; the cheapest move out | a barrier; this one is a first-exit cost | [LLC26a] | (already "barrier") |
| the true barrier: the least possible highest point on any route | the minimax barrier, "the largest barrier that must be crossed along the lowest-barrier path connecting two" states | [LLC26a] Fig. 2 caption | P1 |
| listing every state and every move (the dip census; Q9) | exact enumeration of the energy landscape; a disconnectivity graph, which shows "how configurations cluster into basins and what barriers must be crossed to move between them" | [LLC26a] Introduction, Sec. II | note only |
| classes the switch does or does not join | components of the phase-space network; "trapping sectors"; "effective ergodicity breaking" | [LLC26b] Sec. II | note only |
| an exponent fitted over the range that was run | an "apparent" exponent, "extracted over a restricted time interval, rather than identified a priori with the asymptotic exponent" | [BBJC26] Sec. III | note only |
| the outcomes against room and curling cost (T9, T61) | a dynamical phase diagram of post-quench regimes | [JC26] Sec. III, Fig. 1 | note only |
| the energy left | the excess energy | [JC26] Sec. III.2 | P2 |
| the square-count signature d(v) | a local order parameter | [JC26] Eq. (9) | (P1 already says so) |
| melted (the random phase) | melting of the order; two kinds, see section 5 | [BBM26]; [YC24] | note only |

## 3. Words that look the same and are not

- **λ.** Ours is the coefficient of the local term. Theirs is the strength of the electron-lattice coupling
  ([JC26] Sec. II). Unrelated.
- **g, "the coupling".** Ours, as in CQG, enters the weight as exp(−H/g) and plays the role of a temperature.
  Theirs is a coupling constant, and their temperature is T. A reader from their field will read "fixed coupling"
  as "fixed interaction strength" unless told. Paper 2 now defines g where it first appears.
- **Seed.** Theirs are "symmetry-breaking seeds", tiny perturbations put in at the start ([JC26] Sec. III). Ours
  is a nucleus of the new arrangement, and in paper 1's sealed runs a seed is a total activation budget.
- **Kink, domain wall, topological defect.** Theirs separate two symmetry-related versions of one order and
  disappear only in pairs. A relic is a small piece of the old arrangement left in place, and a single one
  anneals alone (T19): do not call it a kink. But the product is not unique. About half of the 2,014 flawed
  end states of the four λ maps hold a stretch wider than six around, and in the 440 where both widths are
  present they never meet directly: a flaw always lies between (O116, addendum of 12 October; exploratory,
  exact per graph). A leftover of that kind is the joint
  between two regions of the product: the nearer relative of their domain wall, between two different members of
  a degenerate family instead of two mirror images. Which of the knots of O107 are joints has not been read.
  The nearest thing here to their two mirror images is the notebook's open question of 11 October: the tube's
  seam can shift either way, and nobody has asked what forms where the two shifts meet.
- **Coarsening.** The growth of domains as defects meet and cancel. The tube's change is the decay of a
  metastable ordered state, followed by the annealing of isolated defects. "Coarsening" could apply to a
  patchwork, where flaws were seen to wander and cancel in sandbox looks only (`sandbox/LOG.md`, 11 and 12
  October), which support no claim.
- **Freeze-out time.** In the Kibble–Zurek literature it is the instant at which the system can no longer
  "keep up with the change imposed from the outside" ([dCZ14]). T25's registered "freeze-out time" is a
  threshold cooling duration. Paper 2 keeps the registered label and now says it is a different quantity.
- **Quench.** Theirs is a sudden change of a parameter from a state with no order. Our runs start from a
  prepared ordered state. The nearer phrase is "decay of a metastable state".
- **Melted.** In sealed runs it is a registered label for damage, not the random phase (O123).

## 4. Differences that limit the borrowing (*ours*)

1. Their dynamics is the physics: equations of motion with a clock. Ours is a Markov chain chosen to sample,
   and both papers say that its rates are properties of that chain.
2. Their order grows out of a symmetric state and has two equivalent versions. Ours starts ordered. The states
   it can end in at zero energy are a family, every arrangement with two squares on every link, which fixes
   neither connectedness nor topology: tori six around or wider, separate pieces, one-sided ones (paper 1,
   Introduction; O116). Regions of differing short period meet at defects in T61's endpoints (O121).
3. What constrains their defects is conservation of electron number ([JYC25]). What constrains ours is the
   degree, the two sides, the hard-core rule and, sealed, the energy.
4. Their isolated system is deterministic. Ours is stochastic (Creutz stores), with the reservoir's size a
   declared knob.

## 5. Their work beside Trugenberger's (*ours*)

| | Trugenberger ([T22] to [T25], [KTB19]) | Chern's group |
|---|---|---|
| What the system is | A network whose ordered phase is geometry | Electrons and a lattice, or spins, in materials |
| The question | Equilibrium: which phase, and the order of the transition, which his continuum limit needs to be continuous | Kinetics: how a system gets from one state to another in time, and where it gets stuck |
| The role of the dynamics | A sampler; the protocol is mostly unstated ([T22] names no algorithm, sweep count or scan direction) | The object of study; isolated against bath-coupled is a central distinction |
| Defects | Allotropes, "long-lived metastable domains", proposed and not simulated ([T24]: "no datasets were generated or analyzed") | Kinks and domain walls, counted, tracked and given effective kinetic models |
| Words absent | "nucleation" and "latent heat", in every text searched for the note of 5 October | Geometry and gravity are not their subject |
| Sizes | Up to 2,000 points in two dimensions, 500 in three; "months of CPU time" | Lattices of 200 × 200 ([BBJC26]), with learned force fields to go larger |
| What each could check in this project | Whether the model is his, and the reading as geometry | Whether the statistical mechanics and the kinetics are done correctly |

In one sentence: the model is Trugenberger's, deformed; the questions asked of it (how one ordered state turns
into another, sealed or in a bath, and what is left) are of the kind Chern's group asks of its own models; the
motivation is the owner's. Two of Trugenberger's open items read as kinetics problems in the group's language:
how long an allotrope lasts ("depending on their free energy difference to the minimum and the barrier in
between", [T25]) is the lifetime of a metastable domain, and "how a cluster moves by elementary moves" is
defect mobility.

## 6. Where each result bears on the series

Numbers are the short papers of `docs/papers/series_plan.md` (5 October list).

- **Paper 1 (the curled torus).** "Isolated" and "microcanonical" for sealed; "minimax barrier" as the published
  name for what the paper says the 12-unit cost is not; T61's endpoints as domains joined at defects. Added to
  the manuscript on 13 October with [JC26] and [LLC26a].
- **Paper 2 (what the burp leaves behind).** The defect vocabulary of section 2. Three things for the rewrite
  that will add T51 and T55: (a) [BBJC26]'s caution on apparent exponents applies to T51's fits over 1.5
  decades of cooling time; a sandbox look on 13 October (`sandbox/LOG.md`) found the recorded frozen share
  equally well described by a constant floor plus one exponential, which narrows the power-law reading and
  supports nothing until registered; (b) [JC26]'s effective model has a fitted probability that an encounter
  removes defects, and names deriving it from the microscopic rules as open; the relic count per seed (T17) is
  our nearest quantity; (c) the knots of T55 sit behind nearly the same first-exit cost as the column and do
  not anneal, which is a question about minimax barriers, not first exits.
- **Paper 3 (links that reach far).** Their domain walls form where independently nucleated domains meet
  ([JC26] Sec. III). T55 found no far link in T51's pieces.
- **Paper 5 (how curled directions open; T54).** O118's correction says T54's numbers are completed-patch
  energies, not barriers. The quantity wanted is a minimax barrier, and [LLC26a] computes one exactly on small
  systems and statistically on large ones.
- **Paper 6 (the rule, the room).** [JC26]'s dynamical phase diagram is the published form of "which outcome
  for which room and curling cost". [BaC26] (abstract only) recasts "where an isolated system settles" as
  entropy maximized under what the dynamics retains, a possible formal home for the energy-budget estimate C*.
- **Paper 12 (concentrated energy does not fold space).** [BBM26], [BFC26], [YC24]: order melted by injected
  energy, and its recovery. [BBM26] separates melting that loses agreement between regions while local order
  survives from melting that destroys the local order. Our local counts could tell which kind each of our
  "melts" is; that reading has not been made.
- **Paper 14 (a front's pace).** [FZC26] for a propagating interface between two phases; [BBJC26] for a growth
  law written as a crossover.
- **Paper 15 (allotropes dissolve).** [JC26] Sec. III.2 gives a criterion for arrest: the energy available is
  below the local barrier. T43's planted allotrope dissolved at every coupling.
- **The ergodicity checks (Q9) and paper 1's neutral-class enumeration.** [LLC26b]'s phase-space networks.

## 7. Questions that could be put, one at a time (nothing is drafted or sent)

1. For paper 2: two defects with nearly the same first-exit cost, one of which anneals and one of which does
   not. Is a minimax barrier, computed as in [LLC26a], the right thing to calculate, and how is it done beyond
   small sizes?
2. For paper 2: how would they tell a floor plus one exponential from a slow power law over 1.5 decades?
3. For paper 1, later: whether a member of the group would read the statistical-mechanics half.

## 8. M. Vucelja, the reader for the measurement side (added later on 13 October, at the owner's question)

The owner asked whether the paper Vucelja and Chern wrote together should be read and the connection fleshed out.
It was read, and so was the list of her papers (the arXiv API listing of 13 October 2026).

- **The joint paper [FPVC26] is not the connection.** It is an equilibrium Monte Carlo study of how two-faced
  particles line up (abstract; text searched for its methods). It shows that the two work together and little
  else for us. One sentence of it is worth keeping, because this project has made the mistake it warns of: a
  snapshot "taken during relaxation rather than from the equilibrated ensemble" illustrates the defects a model
  supports and does not measure their statistics (Sec. III).
- **Her own line of work is.** Her recent papers are about how fast a system relaxes after a change of
  temperature, in Markov chains and under Metropolis dynamics: the Mpemba effect, in which a system started
  hotter reaches the bath's temperature sooner than one started warm, expressed through mean first passage times
  ([WV22], abstract); a 2025 review of such effects ([TBLRV25], abstract); a 2018 exact solution of Metropolis
  dynamics on a complete graph (title only, arXiv:1812.11962, with I. Klich); and in August 2026 "thermalization
  packets", auxiliary systems prepared in advance and coupled to a target to speed its relaxation,
  "characterized not only by their temperature or heat capacity, but also by their microscopic preparation"
  ([KV26], abstract). Earlier: non-reversible Monte Carlo sampling (titles only).
- **Where that meets this project (*ours*).** Three places. (a) Paper 1's first exit is a mean first passage
  time under Metropolis dynamics, with its channels counted exactly and about a third of exits falling back
  (T22): her subject, and the question already written for her in the series plan. (b) Paper 1's reservoir of
  stores is a finite bath whose number and starting contents are declared parameters, and the paper already
  says that changing the number of stores "changes the entropy as well as the thermal response": [KV26] is
  about exactly such a prepared auxiliary system. (c) Paper 2's cooling results (T25, T51) are relaxation
  against a cooling protocol. A test in her terms that the toy can run: do products started from a warmer bath
  lose their curled columns sooner on the way to the same cold bath than products started from a cooler one?
  That is a Mpemba-style question, it has a yes or no answer, and it is in the sandbox notebook.
- **So the measurement side has two natural readers, who publish together:** Vucelja for the kinetics of the
  chain (first exits, relaxation, what a finite prepared bath does) and Chern for defects and energy
  landscapes. J. Bechhoefer, a co-author of her review, is also an author of the one-dimensional
  nucleation-and-growth paper T37 was scored against.
- **Before anything is put to her:** read [TBLRV25] and [WV22] in full; neither has been.

## 9. Not established

- That any member of the group has seen this project. None has.
- Any quotation's context beyond the passages searched; eight of the eleven papers were not read in full.
- The journal references, and the positions of the group's members.
- Whether a given relic is an isolated defect or a joint between two widths. T19 shows one annealing alone, and
  T55 found no far links; O116's addendum finds joints in 440 of 2,014 flawed end states. Whether a joint
  can be removed without its two stretches first becoming one width has not been asked, and it is the question
  that decides how much of the group's pair-annihilation kinetics carries over.

# Design brief: connecting quantum behaviour to the loop, by counting

Written 2026-09-22 at the author's request, after VISION Update 17 recorded her hypothesis. This is
a brief, not a pre-registration: every computation below gets its own section in `PREREGISTRATION.md`
before it runs (rule 4). Nothing here adds a knob to the energy; the one knob it uses, interchangeable
points, was decided in VISION Update 12. Physics reasoning is *ours, unverified* unless a source is
named, and the published relatives at the end are from general knowledge, none read by us, all to
verify before any of this is claimed as new.

"Experimentally" here means what it has meant throughout this project: exact counting on small
networks where every arrangement can be listed, then long runs of the model at sizes where it cannot,
checked against the exact answers first. There is no laboratory in this brief.

## 1. What is being connected

**The hypothesis** (VISION Update 17, the author's). Points whose swap changes no relationship are one
point with two names. A version of the world that differs only by such a renaming is the same world,
and inside a loop with no start, no end and no outside there is no vantage point from which versions
could be told apart, so all of them hold at once. That is superposition. A measurement is a new
relationship that a swap would not preserve; the versions then differ, and the world is in one of them.
A particle is an allowed vibration of a small closed loop of the substrate. Because the loop of reality
is endless, every version that can arise does arise, and interaction is what separates them.

**What has to be true for the connection to be more than a picture.** Quantum mechanics is not a mood;
it is three numerical facts that any account must reproduce:

1. **Probabilities add, are swap-invariant, and follow the Born rule** (the square of an amplitude).
2. **Interference**: alternatives that cannot be told apart do not add as probabilities but as
   amplitudes, so they can cancel.
3. **Bell correlations**: two separated measurements on one prepared pair can be correlated more
   strongly than any assignment of pre-existing local facts allows (CHSH above 2) and never more
   strongly than 2√2.

The third is the bar that matters, because it is the one a counting picture is most likely to fail,
and the one that would mean most if it passed. The design below is a ladder up to it.

## 2. The one piece of mathematics that ties a loop to a probability

**Established.** A system with finitely many states, run by a fixed rule, must revisit a state and
from then on cycle (the pigeonhole principle; Poincaré's recurrence theorem is the physical form, 1890).
If the rule has chance in it, as the model's reshuffling does, and every state can reach every other,
then every state is revisited endlessly, and **the fraction of all time the system spends in a state
settles to a definite number, the same from every starting point** (the ergodic theorem for finite
Markov chains). For the model's dynamics at coupling g that number is proportional to exp(−H/g) per
labelled arrangement; at fixed total energy it is the same for every arrangement of that energy.

**What this buys the hypothesis** (*ours*). "The probability of finding the world in arrangement C,
given an endless loop that behaves as ours does" is not a metaphor and needs no outside observer: it
is the long-run fraction of the loop's time spent in C, and that fraction is a **count**. Probability
in this picture is the arithmetic of how many arrangements there are, weighted by energy. This is the
sentence that lets everything below be computed rather than argued.

**Two counts, and they are different things.** The project already has both, and the hypothesis needs
them kept apart:

| Count | What it counts | Large for | Small for | Where measured |
|---|---|---|---|---|
| **Multiplicity** | how many *distinct* arrangements share a coarse description (entropy) | the melted phase; a black hole | a perfect sheet | T9 end states; O20; the exact ensembles at N = 16, 18 |
| **Symmetry** | how many *renamings* of one arrangement change no relationship (the versions) | a perfect sheet (320 at N = 160); a pile of knots (10^29.4) | a melted graph (exactly 1) | Q15, `scripts/measure_symmetry_cost.py` |

Multiplicity is what decides **which** coarse state the loop spends its time in: that is Part IV of the
public account and needs no quantum mechanics. Symmetry is what the hypothesis calls the versions: the
superposition **within** one arrangement. They pull opposite ways: the state with the most ways to be
(the melt, the black hole interior) has the fewest versions, and the states with the most versions are
the ordered, symmetric ones. Under the hypothesis that is the right way round for a world that looks
classical at large scale, since anything wired into everything has one version. It also fixes what a
measurement is, formally: **a measurement is an event after which one class of namings has become
several classes**, and the probabilities of the pieces are their multiplicities. That sentence is
computable, and it is the core of every rung below.

**The ceiling on degrees of freedom.** In a scenario of N points, the largest number of versions any
valid arrangement can have is a definite number. For the shattered state of k identical knots it is
192^k · k! by Q15's convention (192 renamings per knot, k! for swapping whole knots), which is 10^29.4
at N = 160. A perfect sheet has 2N. A melted graph has 1. The physical cousin of "the most degrees of
freedom a region can hold" is the Bekenstein–Hawking bound, set by the area of the region's boundary
(*general knowledge, to verify*), and it is a multiplicity, not a symmetry; the two ceilings are
therefore not the same object, and the brief does not pretend they are.

## 3. The ladder

Each rung names a scenario, what is computed, the prediction to be written down before the
computation, and what failure looks like. Cost is given as exact (enumeration or arithmetic, minutes),
run (Monte Carlo at sizes where enumeration is impossible), or design (needs a construction that may
not exist).

### Rung 0. Do the versions exist where the hypothesis says? (exact; TASKS T13 rung 4)

- **Scenario.** The saved end states of T10 (the four-point remnant, O16; the 20-unit twist, O15), a
  perfect torus, a tube, and a melted graph, at N = 64 to 288.
- **Compute.** The renaming count of each whole arrangement (sheet included) by the method of Q15; the
  count of the isolated leftover; and the Laplacian spectrum of the leftover's own loop.
- **Predict, before computing** (*ours*). A perfect torus: 2N. A torus with one remnant: the
  renamings that fix the remnant's position and shape, expected 2 or 4, not 1. A melted graph: 1. An
  ordered region joined by one link to a melted one: 1. The remnant and the twist have distinct spectra.
- **Failure.** A remnant in a sheet with exactly one renaming. Then a particle in space has no
  versions, the hypothesis has no superposition to speak of, and the ladder stops here.

### Rung 1. Do the loop's time-fractions equal the counts? (exact, then run)

- **Scenario.** N = 16 and 18, where every arrangement is listed (Q9), with points treated as
  interchangeable (the unlabelled ensemble of TASKS T10, weight 1 per class), and a scenario at N = 64
  with two leftovers of known shape.
- **Compute.** The exact probability of each class from the count, and the long-run fraction of time
  a chain spends in each class, run with the renaming correction applied per measured configuration
  (the affordable approximation named in T10).
- **Predict.** They agree to within sampling error, as the labelled chain already agrees with the
  labelled exact averages (T4).
- **Failure.** They do not, in which case the approximation is wrong and no probability above this
  rung can be trusted. This rung is validation, not physics, and it is why nothing above it runs first.

### Rung 2. Are the probabilities quantum in form? Swap-invariance and additivity (exact)

- **Scenario.** A system, one small closed loop with m points, joined by one link to an environment,
  a region of the sheet with its own renamings. The detector is a defect placed in the sheet next to the
  loop; the setting is which of the loop's points it links to; the outcome is which class of namings the
  world is left in.
- **Compute.** Before attachment, one class. After, the classes it splits into and their
  multiplicities. The probability of an outcome is its multiplicity over the total.
- **Predict** (*ours*). Outcomes related by a swap of the system that can be undone by a swap in the
  environment are equally probable. This is the structure Zurek's envariance argument uses to derive
  the Born rule (*to verify; not read*), and it is the author's mechanism said in a physicist's words.
  Probabilities of disjoint outcomes add.
- **What this rung cannot do.** It cannot show the square law. The Born rule's square comes from the
  fine-graining step of Zurek's argument, which needs amplitudes to fine-grain; a counting picture has
  multiplicities to fine-grain instead, and whether the two agree is the open question this rung sets
  up and does not answer.

### Rung 3. Bell: does a shared relationship beat the classical bound? (design, then exact)

This is the bar.

- **Scenario.** A flat sheet containing two particles, A and B, each a small closed loop of the
  substrate, placed far apart in the sheet but sharing one relationship that the sheet's geometry does
  not respect: a direct link between a point of A and a point of B, made when they were made. That is
  the model's entangled pair: two things that are one thing because a relationship predates the space
  between them.
- **Settings.** Which point of A the detector at A links to, and which point of B the detector at B
  links to. A loop of m points offers m settings spaced 360°/m apart. **A four-point loop cannot
  violate the bound even in quantum mechanics** (spin measured at 90° separations gives CHSH ≤ 2), so
  the particles must be loops of at least eight points, which the model allows (a curl of eight is a
  valid torus side). This is itself a small prediction of the picture: a four-state particle is
  classical.
- **Outcomes.** Binary at each detector: which of the two classes the world is left in, read from the
  namings that survive the attachment (for a loop, the two ways round).
- **Compute.** For each pair of settings (a, b), the classes the joint arrangement splits into and
  their multiplicities; from them p(same), p(different), E(a, b) = p(same) − p(different); then the
  CHSH combination S over the four setting pairs that maximise it.
- **Predict, written before the computation, with the fork stated** (*ours*).
  - If the set of namings is fixed before the measurements and each outcome is a function of the
    naming and its own detector's setting, this is a local hidden-variable model with the naming as the
    hidden variable, and **S ≤ 2 by Bell's theorem**, whatever the shared link does. The hypothesis
    then reproduces classical correlations only and fails the bar.
  - The hypothesis can beat 2 only if the two attachments **jointly** decide which classes exist, so
    that the classes for (a, b) are not the product of the classes for a and for b. That is the
    author's "a distinction comes into existence" said precisely, and the counting decides whether it
    happens.
  - Above 2√2 is a failure the other way: it would let one detector's setting change the other's
    outcome distribution, which nothing in the model or in nature does.
- **Failure.** S ≤ 2 for every construction tried. That is reported as loudly as a pass, and it would
  say the hypothesis is a way of speaking about identical particles and not an account of quantum
  correlation.
- **Design task first.** Whether a valid arrangement of this shape exists at all: four links per point,
  two sides, the hard-core rule, two eight-loops, one shared link, at a size that can be enumerated or
  at least sampled. `torus`, `is_valid` and the switch move are the tools; if no valid construction
  exists the brief says so and stops.

### Rung 4. Interference (not designed)

Interference needs amplitudes that add and cancel, and the model has no wave dynamics: it reshuffles
wirings, it does not propagate anything. The vibration spectrum of a loop (the modes of Part V) is
static arithmetic on the loop, not a dynamics of the model. A rung here would need a dynamical rule for
how a naming propagates along the sheet, which would be a new ingredient and under S1 needs a dated
VISION decision before any run. It is named so that nobody mistakes rungs 0 to 3 for having covered it.

## 4. What would falsify the line as a whole

- Rung 0: a particle in space has one version.
- Rung 1: the loop's time-fractions do not match the counts, so probability is not counting here.
- Rung 3: S ≤ 2 for every construction, or S > 2√2 for any.

Any of these ends the quantum leg of the hypothesis as stated, and the public document's Part V would
then be a description of identical-particle symmetry and no more.

## 5. Published relatives, to read before any of this is called new

All from general knowledge, none read by us, details to verify.

- Zurek, envariance and the Born rule (2003, 2005): probabilities from swap symmetry between a system
  and its environment. The closest published form of the author's mechanism.
- Rovelli, relational quantum mechanics (1996): a state is defined only relative to what it has
  interacted with. The author's "measurement is a relationship".
- Bell (1964); Clauser, Horne, Shimony and Holt (1969); Tsirelson (1980): the bound, the test, and the
  ceiling used in rung 3.
- 't Hooft, the cellular automaton interpretation (2016): a deterministic finite substrate beneath
  quantum mechanics, and how it meets Bell.
- Wolfram's physics project (2020): hypergraph rewriting with a "branchial" space of all rewritings
  held at once, which is the author's "every version" in another vocabulary.
- Konopka, Markopoulou and Smolin, quantum graphity [KMS06]: the graph itself as a quantum system,
  already in `REFERENCES.bib`.

## 6. Order of work

1. Rung 0, exact, on files that exist. One afternoon; pre-register the predictions in section 3 first.
2. Rung 1, exact then run, because nothing above it is trustworthy without it.
3. The rung 3 design task (does the arrangement exist), before rung 2, because if it does not exist
   the ladder's top is gone and rung 2 changes priority.
4. Rung 2 and rung 3 proper.
5. Reading, section 5, before any write-up.

The author decides whether to start; this brief adds nothing to the scorecard and asserts no result.

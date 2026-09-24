# Design brief: connecting quantum behaviour to the loop, by counting

Written 2026-09-22 at the author's request, after VISION Update 17 recorded her hypothesis; revised the
same day after the published relatives were read (section 7). This is a brief, not a pre-registration:
every computation below gets its own section in `PREREGISTRATION.md` before it runs (rule 4). Nothing
here adds a knob to the energy; the one knob it uses, interchangeable points, was decided in VISION
Update 12. Physics reasoning is *ours, unverified* unless a source is named. Sources are keyed to
`REFERENCES.bib`, whose `note` fields say how much of each was read.

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

**What has to be true for the connection to be more than a picture.** Quantum mechanics is three
numerical facts that any account must reproduce:

1. **Probabilities add, are swap-invariant, and follow the Born rule** (the square of an amplitude).
2. **Interference**: alternatives that cannot be told apart add as amplitudes, so they can cancel.
3. **Non-classical correlation**: two or three separated measurements on one prepared set can be
   correlated in ways no assignment of pre-existing local facts allows (Bell; GHZ), and never so strongly
   that one side's setting shows up in the other side's statistics (no-signalling).

**What the reading settled (section 7), in one paragraph.** Fact 1 is not the discriminating test.
In a counting picture the probability of an outcome is by construction the fraction of equal-weight
versions that carry it, p = m/M, and that is exactly the form Zurek's derivation of the Born rule
arrives at once the environment is fine-grained into equal-amplitude pieces [Zurek05]; the square law
then says only that the amplitude is defined as the square root of a count. The content of quantum
mechanics lies in facts 2 and 3, and fact 2 needs a dynamics the model does not have (section 3, rung
4). So **the bar is fact 3**, and the reading supplied the exact form of the test: an *empirical model*
built from counts, checked for a *global section* [AB11], with the GHZ version as a yes/no test that
needs no statistics [Mermin90] and the CHSH version scored against three published graph numbers
[CSW14].

## 2. The one piece of mathematics that ties a loop to a probability

**Established.** A system with finitely many states, run by a fixed rule, must revisit a state and
from then on cycle (the pigeonhole principle; Poincaré's recurrence theorem is the physical form).
If the rule has chance in it, as the model's reshuffling does, and every state can reach every other,
then every state is revisited endlessly and **the fraction of all time the system spends in a state
settles to a definite number, the same from every starting point** (the ergodic theorem for finite
Markov chains). For the model's dynamics at coupling g that number is proportional to exp(−H/g) per
labelled arrangement; at fixed total energy it is the same for every arrangement of that energy.

**What this buys the hypothesis** (*ours*). "The probability of finding the world in arrangement C,
given an endless loop that behaves as ours does" is not a metaphor and needs no outside observer: it
is the long-run fraction of the loop's time spent in C, and that fraction is a **count**. Probability
in this picture is the arithmetic of how many arrangements there are, weighted by energy. This is the
sentence that lets everything below be computed rather than argued.

**Two counts, and they are different things.**

| Count | What it counts | Large for | Small for | Where measured |
|---|---|---|---|---|
| **Multiplicity** | how many *distinct* arrangements share a coarse description (entropy) | the melted phase; a black hole | a perfect sheet | T9 end states; O20; exact ensembles at N = 16, 18 |
| **Symmetry** | how many *renamings* of one arrangement change no relationship (the versions) | a perfect sheet (320 at N = 160); a pile of knots (10^29.4) | a melted graph (exactly 1) | Q15, `scripts/measure_symmetry_cost.py` |

Multiplicity decides **which** coarse state the loop spends its time in (Part IV of the public account;
no quantum mechanics needed). Symmetry is what the hypothesis calls the versions: the superposition
**within** one arrangement. They pull opposite ways: the state with the most ways to be has the fewest
versions. Under the hypothesis that is the right way round for a world that looks classical at large
scale. It also fixes what a measurement is, formally: **a measurement is an event after which one class
of namings has become several classes**, and the probabilities of the pieces are their multiplicities.
That sentence is computable, and it is the core of every rung below.

**Two consequences of "probability is a count", both exact** (*ours*).

- Every probability the model predicts is a **rational number**. The quantum values at the settings a
  Bell test needs are not: the singlet gives p(same) = sin²(22.5°) = (2 − √2)/4 at 45°. So **no finite
  scenario can reproduce the quantum probabilities exactly**; what it can do is beat the classical bound,
  which needs only S > 2 and admits rational values (the no-signalling maximum S = 4 is reached by a
  rational table). The Tsirelson ceiling 2√2 can be approached, never hit.
- The **ceiling on versions** in a scenario of N points is a definite number: for the shattered state of
  k identical knots it is 192^k · k! by Q15's convention (10^29.4 at N = 160); a perfect sheet has 2N; a
  melt has 1. The physical "most degrees of freedom a region can hold" is the Bekenstein–Hawking bound,
  a multiplicity set by boundary area (*general knowledge, to verify*); the two ceilings are different
  objects and the brief does not pretend otherwise.

## 3. The ladder

Each rung names a scenario, what is computed, the prediction to be written down before the
computation, and what failure looks like. Cost: exact (enumeration or arithmetic, minutes), run (Monte
Carlo where enumeration is impossible), or design (needs a construction that may not exist).

### Rung 0. Do the versions exist where the hypothesis says? (exact; TASKS T13 rung 4)

- **Scenario.** The saved end states of T10 (the four-point remnant, O16; the 20-unit twist, O15), a
  perfect torus, a tube, and a melted graph, at N = 64 to 288.
- **Compute.** The renaming count of each whole arrangement, sheet included, by the method of Q15; the
  count of the isolated leftover; the Laplacian spectrum of the leftover's own loop.
- **Predict, before computing** (*ours*). A perfect torus: 2N. A torus with one remnant: the renamings
  that fix the remnant's position and shape, expected 2 or 4, not 1. A melted graph: 1. An ordered
  region joined by one link to a melted one: 1. The remnant and the twist have distinct spectra.
- **Failure.** A remnant in a sheet with exactly one renaming. Then a particle in space has no versions
  and the ladder stops here.

### Rung 1. Do the loop's time-fractions equal the counts? (exact, then run)

- **Scenario.** N = 16 and 18, every arrangement listed (Q9), points interchangeable (the unlabelled
  ensemble of TASKS T10, weight 1 per class); then a scenario at N = 64 with two leftovers of known shape.
- **Compute.** The exact probability of each class from the count, and the long-run fraction of time a
  chain spends in each class with the renaming correction applied per measured configuration.
- **Predict.** Agreement within sampling error, as the labelled chain already agrees with the labelled
  exact averages (T4).
- **Failure.** Disagreement, in which case no probability above this rung can be trusted. Validation,
  not physics, and the reason nothing above it runs first.

### Rung 2. Swap-invariance and additivity of outcome probabilities (exact)

- **Scenario.** A system, one small closed loop of m points, joined by one link to an environment, a
  region of sheet with its own renamings. The detector is a defect placed in the sheet beside the loop;
  the setting is which of the loop's points it links to; the outcome is which class the world is left in.
- **Compute.** Before attachment, one class. After, the classes it splits into and their multiplicities.
- **Predict** (*ours*). Outcomes related by a swap of the system that can be undone by a swap in the
  environment are equally probable; probabilities of disjoint outcomes add. Both are exactly the
  assumptions Zurek's fine-graining makes and then counts with [Zurek05]. Passing this rung says the
  counting is the right kind of counting; it does not say the probabilities are quantum.

### Rung 3a. GHZ: a yes/no test with four-point loops (design, then exact)

> **Settled by argument, 2026-09-23, before any construction** (PREREGISTRATION T15 rung 3a, its reading;
> ASSUMPTIONS O29). A renaming of a fixed arrangement fixes or swaps each loop's two pairs of points at
> once, so it is a complete instruction set; attaching detectors changes which renamings survive, not the
> colours they give. CLASSICAL for every arrangement, and S ≤ 2 for rung 3b by the same argument. The fork
> below was wrong as written: "which namings survive" changes the classes, never the supports. Section 5's
> consequence applies. Kept as written so that the mistake can be read.

The reading moved this above CHSH: it needs only **two settings per particle**, which a four-point
loop supplies (attachment points 90° apart), so it can be run on objects the model already makes, and
its verdict is a logical contradiction rather than a statistic [Mermin90].

- **Scenario.** Three small closed loops A, B, C made in one event and pairwise related by links the
  sheet does not respect. Each has two settings, 1 and 2 (two attachment points at right angles), and a
  binary outcome (red or green, in Mermin's telling: the two classes).
- **The published rules** [Mermin90, read]. In runs with settings 122, 212 or 221, an odd number of
  red lights always flashes (RRR, RGG, GRG or GGR). In runs with settings 111, an odd number of red is
  never observed. No set of pre-carried instructions can do both: the eight instruction sets that satisfy
  the first rule all give an odd number of red in 111. Quantum mechanics does both.
- **Compute.** For each of the four contexts, the classes the joint arrangement splits into and their
  multiplicities. Read off the support: which colour triples occur at all.
- **Predict, the fork** (*ours*). If the namings are fixed before the attachments, each naming *is* an
  instruction set, so the supports admit a global assignment and the 111 context shows an odd number of
  red in some runs: classical, and the rung fails. If the joint attachments decide which namings survive
  in a way that depends on all three settings at once, the supports can be the quantum ones, which in
  [AB11]'s terms is **strong contextuality**: no assignment respects all four supports. That is the
  strongest form of non-classicality there is, and it is a finite check with no error bars.
- **The one concrete mechanism that could produce it** (*ours*). The hard-core rule forbids two points
  sharing more than two neighbours. When detectors attach at all three loops, some combined namings can
  become invalid *only jointly*, so that the set of surviving namings for context 122 is not the product
  of per-loop sets. Whether it does is what the computation finds out; it is the whole of the "magic",
  and it is either there in the rules or it is not.

### Rung 3b. CHSH: the statistics, with eight-point loops (design, then exact)

- **Scenario.** Two loops A and B far apart in a sheet, sharing one link made when they were made. A loop
  of m points offers m settings 360°/m apart; the standard test needs 45° steps, so **m = 8** (a curl
  of eight is a valid torus side). A four-point loop cannot violate the bound even in quantum mechanics.
- **Compute.** For each pair of settings, the classes and multiplicities; from them p(same),
  p(different), E(a,b) = p(same) − p(different); the CHSH combination S over the best four pairs; and,
  in the event form of [CSW14], the sum of the eight event probabilities.
- **Diagnostics, in this order** [AB11, read]. (i) **Compatibility**: A's outcome distribution must be
  the same to the last count whatever B's setting is. If it is not, the construction signals and is
  disqualified, since nothing in nature does. (ii) **Global section**: does a single non-negative
  distribution over all four measurements marginalise to every context's table? A linear programme
  answers it. If yes, the model is classical and S ≤ 2 follows without computing S. (iii) Only then S.
- **Predict, the fork** (*ours*). Fixed namings: a global section exists (each naming is one) and
  S ≤ 2. Joint splitting that fails (ii): S can exceed 2. Above 2√2, or any failure of (i), is a failure
  the other way.

### Rung 4. Interference (not designed)

Interference needs amplitudes that add and cancel, and the model has no wave dynamics: it reshuffles
wirings, it does not propagate anything. The loop spectrum of Part V is static arithmetic. A rung here
would need a dynamical rule for how a naming propagates, a new ingredient that under S1 needs a dated
VISION decision. Named so that nobody mistakes rungs 0 to 3 for having covered it.

## 4. The probabilities we are predicting

Written here so that the numbers are on record before any construction exists. "Quantum" is the
spin-½ singlet correlation E = −cos Δ, the standard benchmark; "hidden angle" is Bell's own example of a
local model with a shared hidden direction, E = −1 + 2Δ/π; "rigid link" is a shared relationship that
fixes the relative naming outright, so every E is ±1.

**Table 1. Two eight-point loops: p(same outcome) against the angle Δ between the settings.**

| Δ | 0° | 45° | 90° | 135° | 180° |
|---|---|---|---|---|---|
| Quantum (singlet) | 0 | 0.146 | 0.500 | 0.854 | 1 |
| Hidden angle (local) | 0 | 0.250 | 0.500 | 0.750 | 1 |
| Rigid link (deterministic) | 0 or 1 at each Δ, a step function | | | | |
| **This model** | to be computed; rational; the fork of rung 3b decides which row it resembles | | | | |

The discriminating settings are 45° and 135°: local models give 0.25 and 0.75 there, quantum gives
0.146 and 0.854, and the model's count cannot give 0.146 exactly but can fall below 0.25.

**Table 2. The CHSH score, two forms.**

| Bound | Correlator form S | Event-sum form [CSW14] |
|---|---|---|
| Classical (local) | 2 | 3 (independence number of Ci₈(1,4)) |
| Quantum (Tsirelson) | 2√2 ≈ 2.828 | 2 + √2 ≈ 3.414 (Lovász number) |
| No-signalling | 4 | 4 (fractional packing number) |
| **This model** | to be computed; ≤ 2 if a global section exists | |

**Table 3. GHZ with three four-point loops: what the supports must be.**

| Context | Quantum support | Any instruction set | This model |
|---|---|---|---|
| 122, 212, 221 | odd number of red only | can match | to be computed |
| 111 | never an odd number of red | odd red forced by the rule above | to be computed |

One line, stated before any run: **our honest expectation is the classical row in every table**, because
the count of namings of a static arrangement is a classical probability space with the naming as the
hidden variable, and Bell's theorem then applies. The hypothesis earns the quantum row only through the
mechanism of rung 3a, joint invalidity under the hard-core rule, and the computation is what decides.

## 5. What would falsify the line as a whole

- Rung 0: a particle in space has one version.
- Rung 1: the loop's time-fractions do not match the counts.
- Rung 3a: the 111 context shows an odd number of red, for every construction tried.
- Rung 3b: a global section exists for every construction, or compatibility fails for any.

Any of these ends the quantum leg of the hypothesis as stated, and the public document's Part V would
then be a description of identical-particle symmetry and no more.

## 6. Order of work

1. Rung 0, exact, on files that exist; pre-register section 3's predictions first.
2. Rung 1, because nothing above it is trustworthy without it.
3. The construction task for rung 3a: three four-point loops pairwise linked inside a valid sheet
   (`torus`, `is_valid`, the switch move). If no valid arrangement exists, say so and stop.
4. Rung 3a, then rung 2, then the eight-loop construction and rung 3b.
5. The unread items of section 7 before any write-up.

## 7. What the published work fixes (read 2026-09-22; status per item in `REFERENCES.bib`)

- **[Zurek05], envariance and the Born rule** (the envariance and fine-graining sections read, arXiv
  text). Equal Schmidt coefficients: a swap on the system can be undone on the environment, so the
  outcomes must be equiprobable. Unequal coefficients: a counter system fine-grains each outcome into
  m_k orthonormal equal-amplitude pieces, and counting them gives p_k = m_k/M = |a_k|². The counting
  assumes mutually exclusive outcomes, equal amplitudes, and that probabilities of exclusive events add.
  **For us:** the hypothesis counts equal-weight namings, which is the right kind of counting; the Born
  rule is then form, not test.
- **Branch counting in many-worlds** ([Saunders21] abstract; Wallace's objection from secondary
  sources). Naive counting of branches does not give the Born rule; counting done on a fine-grained,
  equal-weight branch structure does, and Saunders ties it to Boltzmann's and Planck's combinatorics.
  **For us:** the same lesson as Zurek's, from the other side, and a warning that "count the versions"
  must mean the fine-grained equal-weight ones, which the namings are.
- **[CSW14], the graph-theoretic bounds** (the CHSH section read, arXiv text). Any Bell or
  non-contextuality correlation is a positive sum of event probabilities; exclusive events are adjacent
  vertices of a graph; the classical, quantum and no-disturbance maxima are the independence number, the
  Lovász number and the fractional packing number. For CHSH the graph is Ci₈(1,4) and the numbers are
  3, 2 + √2 and 4. **For us:** the scoring of rung 3b, and a curious fact for the author, that the
  quantum bound is a property of a graph.
- **[AB11], contextuality as the absence of a global section** (definitions read, arXiv text). An
  empirical model is a table of outcome distributions, one per jointly measurable context; compatibility
  of overlapping contexts is no-signalling; a global section is one distribution over all measurements
  that marginalises to every table; its absence is contextuality, with three strict levels: probabilistic
  (Bell), possibilistic (Hardy), strong (GHZ, where no assignment respects all supports). **For us:**
  the diagnostics of rung 3b and the meaning of rung 3a, and the exact sense in which "fixed namings" is
  classical: each naming is a global assignment.
- **[Mermin90], the GHZ gadget** (read, saved PDF). Three detectors, two settings each, red or green;
  the rules and the eight legal instruction sets are as stated in rung 3a. **For us:** the cheapest
  sharp test, and it fits the four-point objects the model already makes.
- **['tHooft14], the cellular-automaton interpretation** (abstract). A classical substrate beneath
  quantum mechanics, meeting Bell by superdeterminism: the choice of setting is not independent of the
  system. **For us:** a boundary. Our fork is not superdeterminism; the settings are free and the
  namings are *made* by the measurement. That is contextuality, and it is the honest name for it.
- **[Rovelli96], relational quantum mechanics** (abstract). States are relative to what a system has
  interacted with; no observer-independent state. **For us:** vocabulary for "measurement is a
  relationship"; no computation follows from it.
- **[Gorard20], quantum properties of the Wolfram model** (search summary only; not read). Multiway
  systems hold every rewriting at once, with a branchial space in which the Born rule is read from path
  weights and interference from cancelling weights. **For us:** the closest computational cousin of
  "every version at once", and the one to read before rung 4 is ever designed.
- **Bell (1964), Clauser–Horne–Shimony–Holt (1969), Tsirelson (1980), Popescu–Rohrlich (1994)**: the
  bound, the test, the quantum ceiling, the no-signalling ceiling. General knowledge, not read, numbers
  as in Table 2.

The author decides whether to start; this brief adds nothing to the scorecard and asserts no result.

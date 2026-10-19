# Paper 1, explained: seven ideas you need to be able to say back

Written for Emily, as a study aid, 2026-10-12. It covers `docs/papers/curled_torus/paper.tex` (the curled torus
"burp"). It is not part of the scientific record and is not a paper.

**How to use it.** Read one idea, close the file, say it out loud in your own words, then open the next. When
all seven are done, take the quiz (`paper1_quiz.md`) and have it graded before you open the answer key.

**What kind of statements are here** (rule 10). Statements about what the paper measured or computed are
the paper's own and are cited by section. The *standard physics names* for each idea (Arrhenius law,
metastable state, nucleation, microcanonical ensemble and so on) are general knowledge that I have not looked up for
this file. Treat them as **ours, unverified**: check each against a textbook or a physicist before you say
it to one. Where the toy differs from the textbook idea, I say so, because that is where the questions will come.

---

## 0. What the toy is

A **graph** is points joined by links. Here every point has exactly four links. A **square** is four points
joined in a loop. The toy gives every graph an **energy**, H, built from counting squares (paper, Eq. 1):

- Squares lower the energy (each point wants to be in squares).
- But a *third* square on one link is penalized, by a dial called **λ** (lambda).

The flat grid (a **torus**, a grid whose edges wrap around like the screen in an old arcade game) has exactly two
squares on every link and energy zero. When λ > 1 nothing has lower energy, so it is the **ground state**.

The **curled torus** is the same grid but one direction is only four points around: a tube. Each link
round the tube carries three squares, so it pays the penalty. Exact result (Eq. 2 area): it sits
**4(λ − 1) per point above** the flat grid. Call that ε. At λ = 1.25, ε = 1.

**Say it back:** what is a torus, what does λ do, and why is the tube higher than the flat grid?

**Why λ = 1 matters.** At λ = 1 this is the published model (Trugenberger's CQG), and ε = 0: flat, tube
and the 4-cube all tie. Everything in the paper is at λ > 1, so it is *next to* his model, never in it.

---

## 1. Stable, and stable for now

A ball in a dip is stable. A ball in a *shallow* dip beside a deeper one is stable **for now**: any small
nudge rolls back, but a big enough one tips it over. Physicists call the shallow dip a **metastable state**
(a local minimum of energy). The deeper one is the true ground state.

The tube is the shallow dip, the flat grid the deep one. "Dip" here is exact and checkable: from the tube, **every
single move the dynamics can make costs energy** (paper, "Metastability window"). Enumerating all valid graphs at 18 points,
such states exist only for 1 < λ < 1.6.

**Where it differs from the textbook picture.** A ball has one position. This toy has a huge number of
possible graphs, so "the dip" is one arrangement among astronomically many that the dynamics wanders between.

**Say it back:** what makes a state metastable, and how do we know the tube is, with certainty, not just by watching?

---

## 2. The barrier, and why waiting time follows a law (Arrhenius)

To leave the shallow dip you need one specific move. The cheapest costs **12 energy units at λ = 1.25** ("move A": 32 − 16λ).
That is the **barrier**, ΔE‡.

The dial **g** is the toy's temperature (how willing the dynamics is to take an uphill move). The chance a
move that costs ΔE is accepted is about e^(−ΔE/g). Standard name for this: an **Arrhenius law** (the rate of a
reaction rises exponentially with temperature). So:

> wait ≈ 1 / (how often the move is offered × e^(−ΔE/g))

The paper's point: "how often offered" is **counted exactly** (move A: 3 times per sweep, move B: 2 times),
not fitted to the data. So Eq. (3) has nothing adjustable, and the measured waits matched it over a ninety-fold range.

**Where it differs / the trap.** The wait does **not** shrink in a bigger system. You might expect it to
(more places to start). But this chain draws its two edges from the *whole* graph, so any one region is offered
a way out about 1/N as often, which cancels the N regions. The paper says plainly this is a property of
**this chain's proposal, not of the barrier** (Sec. II, last paragraph; Discussion).

**Say it back:** what is a barrier, what does g do, and why is the wait the same at 64 points and 192?

---

## 3. A memoryless wait

If the exit is one rare event with a fixed chance each sweep, then the wait has no memory: a tube that has waited
2,000 sweeps is no closer to leaving than a fresh one. The shape of such waiting times is the **exponential
distribution**, and its tell-tale number is the **coefficient of variation** (CV, the spread divided by the
average), which equals 1. Standard name for the process: a **Poisson process**.

Why it makes physical sense here: nothing builds up in the tube. It does not "tire". Each sweep is a fresh lottery.

The paper pre-registered "CV between 0.7 and 1.3". With only thirty decays that band is too tight (two
standard errors wide), so it failed in several cells by chance, and the paper says so honestly. Afterwards it
tested the whole distribution (the **Kolmogorov-Smirnov** test, a measure of how far two distributions are apart) and the pooled waits were
exponential (p = 0.53). That second test was *not* pre-registered, and the paper labels it that way.

**Say it back:** what does "memoryless" mean for a tube that has already waited a long time, and why is the CV
band a weak test?

---

## 4. A seed, then a front (and what "sharp" does and does not mean)

After the first exit, the opening **spreads from one place**, like fire along a fuse. The two arrangements, tube
and flat, sit either side of a **front**. At half conversion, 98.8 to 99.8% of points are one or the other, almost
nothing in between. And the energy released is exactly ε per point.

Standard name: **nucleation and growth**: a seed forms, then a boundary sweeps outward.

About a third of exits fall back into the tube without ever growing (the **transmission coefficient** κ of 0.56
to 0.68). So the barrier governs the *first exit*, and whether it grows is a separate step.

**The trap, which the paper itself marks as "not claimed".** This is **not a first-order phase transition** in the
thermodynamic sense. A first-order transition is about equilibrium, how a system behaves as you vary temperature,
with two coexisting phases and a latent heat. What is measured here is the **decay of a metastable state at a
fixed temperature**. "Sharp" is used in the paper's pre-registered sense (seed, front, two states, nothing between).
If a physicist hears "first order" they will think of the other thing.

**Say it back:** what is a front, what is κ, and why is "first-order transition" the wrong phrase for this result?

---

## 5. A sealed system (no heat bath)

Normally the toy sits in a **heat bath**: an unlimited supply and sink of energy that fixes the temperature.
The sealed version has **no outside**. Energy is split between the graph and a set of C small "stores"
(**Creutz demons**, Creutz 1983). Total energy is conserved to the last unit, checked in every run. The
temperature is not set; it is read off the stores' average. Standard name: the **microcanonical ensemble**
(an isolated system with fixed total energy).

Two results:
1. **A seed of 12 units starts the change at every size tested, and nothing smaller does.** 12 is exactly the
   barrier. The seed does not grow with the system, but the energy released (εN) does.
2. **The change completes only if the surroundings can absorb the release.** With too few stores
   (C ≤ N/16) the released energy heats the new flat region until it **melts into the random phase**. Stores at
   N/2 or more give a clean flat torus. The crossover scales with N because the release does.

**Where it differs.** The sealed dynamics is *one* energy-conserving version of the chain, not "the" dynamics of a
sealed universe (the paper says so).

**Say it back:** why does a bigger tube need a bigger reservoir, and what happens if it does not get one?

---

## 6. The relic, and the two-way reading of "about one"

After conversion there is usually a small defect left: about **one four-point loop (14 units) per tube, at every
size** from 64 to 288 points (0.90, 0.85, 1.05, 0.95). The fitted growth with size is zero to within its error.

What this does and does not show: it shows no growth *over the sizes reached*. Rule 14 asks for more than that for any
size claim: a number written down in advance for a size not yet run. The paper claims only "no measurable growth, across
the sizes we could reach" and does not claim why.

**Say it back:** what is the relic, and what would you need to do to turn "no growth so far" into a real size claim?

---

## 7. Labelled or interchangeable points

All runs treat points as individually named (point 17 is not point 41). A physicist might ask why, since identical
particles are interchangeable. The paper handles it as follows: counting interchangeable points
re-weights each arrangement by its number of symmetries. **That leaves every energy unchanged** (so ε, the
barrier and the 12-unit seed are the same). **It changes the rates.** The perfect tube has 2N symmetries, but the
arrangements one move away have 2, so each exit is accepted roughly N/2 to N times less often, and the wait would
**grow with N**. This is flagged as transition-state reasoning, not a derived clock, and **not run**.

**Say it back:** which results survive switching to interchangeable points, which do not, and which of the two is
untested?

---

## A map of the kinds of statement in the paper (rule 10)

| Kind | Examples from paper 1 |
|---|---|
| Exact (arithmetic or full enumeration) | ε = 4(λ − 1); moves A and B cost 32 − 16λ and 64 − 40λ and are offered 3 and 2 times a sweep; metastable window 1 < λ < 1.6 at 18 points |
| Measured, pre-registered | Two-state change, single front, at N = 64, 96, 192 (with the amendments listed) |
| Measured, exploratory | Arrhenius test over 12 conditions; the 12-unit seed threshold; exponential-distribution checks added after the runs |
| Interpretation (ours, unverified) | Reading κ as a transition-state transmission coefficient; reading the excess near λ = 1 as statistical |
| The hypothesis's claim about reality (hers) | The Outlook: space emerged from an ordered precursor by a change of this kind. The paper marks it "motivation, not a result" |

If you can sort any sentence of the paper into one of these rows, you are ready for most questions.

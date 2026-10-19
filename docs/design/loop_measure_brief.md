# The yield of a turn: piece 12's scoring function, written as terms (2026-10-18)

**Status: ours, a specification and not a computation.** Written 18 October 2026 on the owner's "proceed", from her terms
of the same afternoon (`sandbox/NOTEBOOK.md`, 18 October: the length of the era of starlight, the black holes formed and
when, the observation window) and her decisions on the measure (VISION Updates 23, 26, 43, 59). The standard numbers
are from search summaries and general knowledge, all to verify (`docs/reading/notes/2026-10-18_far_future_and_observation_window.md`).
Nothing here is a knob of the toy or a run. One choice is left to her (section 4), and without it no setting can be
scored.

## 1. What is scored, and what the reward is

A **setting** s of the loop: in the hypothesis, the constants of a universe (the curling cost λ, the number of directions
and their ties, and, in the sky, the strengths of gravity and the other forces). The owner holds that λ is the same in a
parent and its daughters (Update 23, extended in Update 59), so a setting is inherited down the tree and a tree is
scored as a whole.

The **reward** is observers who evolved (Update 43): not brains assembled by chance, which cannot evolve. Things that go
with observers evolving stand in for them where observers cannot be counted: a long cold period, stars with planets at the
right temperature, complex molecules. Her addition of 18 October: an observer that can learn the universe's history,
which needs the observation window of section 2 to be open.

The **unit** is per universe per generation (Update 59: each universe's turn ends when its last black hole has dissolved,
and every black hole births many daughters; the count is the branching one).

## 2. The terms

Each term with its definition, its value for our setting where one is published, and whether the toy has a counterpart.

| Term | Definition | Our setting (to verify) | In the toy |
|---|---|---|---|
| T_star | the length of the era of starlight: from the first stars to the last small red stars burning out | about 10^14 years; star formation itself is past its peak (about 10^10 years ago) and nearly over by about 10^11 | none |
| n_pl(t) | the rate at which habitable planet-lifetimes begin, per unit time, across the universe | unknown in absolute terms; it follows the star-formation history, peaking about 10^10 years ago | none |
| τ_hab | how long a planet stays habitable for complex life | Earth about 4.5 × 10^9 years so far with one to two billion left; planets round small red stars up to 10^12 or more | none |
| p_obs | the chance that one habitable planet-lifetime produces a society that asks about the universe | one data point (us), which cannot be read as a rate | none |
| T_obs | the observation window: the time in which an observer can still learn the universe's history (other galaxies visible, the background light detectable, the light elements' record clean) | of order 10^11 years (Krauss and Scherrer 2007: beyond it a future observer sees one island of stars and infers a static universe) | none |
| N_BH(t) | black holes formed by time t; N_BH its total | the total is set mostly in the first 10^10 to 10^11 years, since structure stops forming once dark energy dominates; of order 10^19 to 10^20 stellar black holes in the observable universe (general knowledge, to verify) | none directly: the fold is piece 11, where nothing has yet curled from energy alone |
| T_turn | the length of a universe's turn: until its last black hole has dissolved (Update 44, 59) | about 10^100 years | none |
| b | daughters per black hole | the owner's "trillions"; nothing measured | **exact under Update 66:** one daughter per a N_slab fed, so b = E_in / (a N_slab), the energy that falls in divided by one daughter's lump |
| B | daughters per universe, B = N_BH × b | | |
| t_cold | the owner's trade (Update 43): a universe that makes more black holes sooner has less time with stars and planets undisturbed | the function linking N_BH(t) to T_star and to n_pl(t) is not written anywhere and is the first thing a model would have to supply | none |

## 3. The function, in stages

**Stage 1, one universe.** Observers who evolved and could see:

    O(s) = ∫_0^{T_star(s)} n_pl(t; s) · p_obs(s) · W(t; s) dt

with W(t; s) = 1 while t < T_obs(s) and smaller after (the owner's requirement that an observer can still learn the
universe's history; a weight rather than a cut-off if she prefers). Every term depends on the setting through physics no
model here can compute; for our setting the integrand is concentrated in the first 10^11 years of a 10^14-year era, so
most of the era of starlight yields observers who cannot see the beginning.

**Stage 2, the tree.** A universe of setting s births B(s) = N_BH(s) · b(s) daughters of the same setting. After k
generations the tree holds B^k universes and, with every term equal across a setting's universes, yields

    Y_k(s) = O(s) · B(s)^k.

**Stage 3, the trade.** The owner's constraint that keeps the branching from running away (Update 43): making black holes
sooner shortens the cold time, so N_BH(s) and O(s) pull against each other. Written as a dependence, O(s) falls as the
black-hole formation rate rises; the shape of that fall is the unknown function of section 2's last row.

## 4. How the generations are combined: decided by the owner, 18 October (VISION Updates 67 and 68)

Y_k grows without bound in k for any setting with B > 1, so settings cannot be compared by their total yield (O101: a
turn's count has to be finite, and a branching process is dominated by its rate of multiplying). Three rules were put to
the owner, each ranking settings differently: (1) per universe, score O(s), the branching ignored; (2) the growth rate,
score ln B(s) with O(s) > 0 as a filter (Smolin's selection for the most black holes, [Smolin06], not read, with her
observer requirement as the gate); (3) a fixed depth or a discount, O(s) · B(s)^K or Σ_k O(s) B(s)^k β^k, which imports a
number nothing fixes ([Bostrom11], [Askell18], read in part, O101).

**Her decision, two rules for two questions.** Her words: "Per universe only ignoring the branching when we are thinking
about identicle universes that can only be differentiated by a particle or quantum measurement that makes something
different at the macro scale. 2 for predictions of when an observer is most likely to occur in time where t=0 and the end
of life supporting stars."

- **Rule (i), per universe, within a setting.** Universes of one setting that differ only by a quantum outcome with a
  macroscopic consequence (versions; Update 17, piece 14) are each counted whole. *Ours:* this is the rule that avoids
  O101's trap. Within a setting every universe has the same O(s), so the branching adds nothing but copies, and no
  exponential weight falls on the deepest generations. The Born-weight caution of piece 14 applies to the copies: if versions are Everett's
  branches, each copy carries a weight. **Her position, the same evening:** "I believe they are as needed for amplitudes
  and interference to work correctly." So the copies carry Born weights on her word; whether the toy's versions are such
  branches is still untested (O125, piece 13).
- **Rule (ii), the growth rate, for when an observer exists.** The question: between a universe's birth (t = 0) and the
  end of its life-supporting stars, when is an observer most likely? *Ours, unverified; the mathematics is textbook
  demography and the cosmological form is published ([Freivogel11], read in part; [BFY08], read in full by an assistant
  agent, Eqs. 35 to 40).* Two readings of "most likely", and they disagree:
  - **Counted per universe** (rule (i) applied to the clock): the distribution over t is Stage 1's integrand,
    n_pl(t) · p_obs · W(t), the same in every universe of the setting. For our setting it peaks where habitable planets
    form and have had time to evolve observers, inside the observation window: from a few billion years after the start
    to a few tens of billions (piece 14's population model puts the share of observer-moments already past by today
    anywhere from under a millionth to 0.9 depending on who counts; `docs/theory/orh_findings.md`, O125). Our 1.4 × 10^10
    years sits inside that range and is not a surprise under this reading.
  - **Counted across the tree at one moment** (the growth rate at work): if each universe births daughters at a rate
    β(τ) per unit of its own age τ, the tree grows as e^(γT) in a common time T with γ fixed by 1 = ∫ β(τ) e^(−γτ) dτ,
    and the universes alive at any one moment have ages distributed as e^(−γτ) (the stable age distribution). Observers
    are then found at age τ in proportion to n_pl(τ) p_obs W(τ) e^(−γτ): the branching pulls the prediction toward the
    earliest age at which observers can exist. This is the youngness pressure of eternal inflation. **How strong, for her
    numbers:** "trillions" of daughters per universe, born as its black holes form within about 10^10 years, gives
    γ ≈ ln(10^12) / 10^10 years ≈ 3 × 10^−9 per year, so between the first possible observers (about 10^9 years) and us
    (1.4 × 10^10) the weight falls by e^(−γ × 1.3 × 10^10) ≈ e^(−36). Under this reading an observer at our age is
    predicted essentially never; an observer should find itself within the first billion years of its universe.
  - **What follows.** Her rule (ii) makes a prediction that can fail, which is what the measure needed. Under the
    across-the-tree reading it fails already, by our own age, unless the daughters per universe are far fewer than
    trillions (γ × 10^10 years of order one needs b N_BH of order e, that is a few daughters per universe, not 10^12) or
    the daughters are born late in the parent's life (β concentrated at ages past ours, which the black hole era allows:
    the mass that falls in over 10^100 years, not the formation of the holes, would set the births). Under the per-universe
    reading nothing fails. Which reading her rule (ii) means was the one question this decision left; **she settled it
    the same evening (VISION Update 68): per universe, by each universe's own age.** Her words: "daughter's clock is not
    her parent's - it's an exact copy though, starts at big bang runs though heat death, every time so yes The
    across-the-tree count needs a common clock running across universes, we don't have one clocks are only within a
    universe." So the across-the-tree reading below is not her rule; it is kept as the record of why it was asked. Rule 13
    applies to the youngness argument either way: it was made for eternal inflation and is carried here as a target.
  - **Her question, the same evening: can the forward weight be balanced by late observers (the last at 10^100 years;
    red dwarfs stable far longer than stars like ours)?** Her first instinct: do not count across the tree, line every
    universe up at its own birth and look from outside time. *Ours, arithmetic.* **Late observers cannot balance the
    weight; late births can.** The weight e^(−γτ) is fixed by when daughters are born, not by when observers live. With
    γ = 2.8 × 10^−9 per year (10^12 daughters within 10^10 years) an observer at 3 × 10^10 years needs 10^19 times the
    observers of now to pull even, one at 10^12 years (the red dwarfs' era) 10^1180 times, one at 10^100 years
    10^(10^91); no finite universe holds them. What lowers γ is the birth time: the same 10^12 daughters born at 10^12
    years give γ = 2.8 × 10^−11 and a weight of e^(−0.4) at our age, nothing. And early births set a floor whatever comes
    later, since 1 = Σ B_i e^(−γτ_i) ≥ B_early e^(−γτ_early): more than about three daughters per universe within the
    first 10^10 years already costs e^(−1.4) at our age, ten cost e^(−3), a million e^(−18). So the across-the-tree
    reading survives only if the black holes formed early birth almost nothing and the daughters come from what falls in
    over the long black hole era; under Update 66 (b proportional to the energy fed) that is not what the toy says.
    *On "from outside time":* lining every universe up at its birth is the per-universe count by age, and it is what an
    outside view gives: the whole tree counted per universe has every universe with the same distribution over its own
    age, so the branching adds copies and no weight. The across-the-tree count needs a common clock across universes,
    which the hypothesis itself denies (time emerges inside each open space, Update 65; a daughter's clock is not its
    parent's). Her instinct is the reading consistent with her own picture; eternal inflation's youngness paradox is the
    published argument against the other ([Freivogel11]: a regulator by a global time). *Her red-dwarf point does bite,
    in the per-universe reading, the other way:* with habitable planets round 0.1 solar-mass stars, the chance of an
    observer as early as now is at most about 0.1 % ([LBS16], read in full 12 October; `src/orh/cosmic.py`), so a
    per-universe count predicts an observer at about 10^13 years unless red dwarfs are poor hosts or late observers are
    weighted down. Her own term W(t) does the second: observers who cannot learn their universe's history (beyond about
    10^11 years, Krauss and Scherrer, not read) count less, so the peak moves inside 10^11 years and our age is
    unremarkable. The window is therefore a load-bearing term of her function, not a flourish: without it the
    per-universe count predicts the red-dwarf era. A "balance" in the across-the-tree reading (the youngness pull
    against the red dwarfs' numbers) would need γ of a few × 10^−11 per year, two numbers set to land on our age, which
    rule 13 forbids counting as anything.
  - **Her lean, later the same evening ("yes this makes sense"): the births set by the mass that falls in over the long
    black hole era, holes birthing now still running at 10^50 years.** Recorded as a lean, not as her word on the reading.
    *Ours, to verify against the sources:* under the converter (Update 66) a hole births only while fed, and the published
    far future has the feed front-loaded: nearly all infall in the first 10^10 to 10^11 years; a late minority tranche at
    about 10^20 years when galaxies relax (most remnants ejected, a minority swallowed); after that nothing to fall in, and
    Hawking loss outrunning gain, the stellar holes gone by about 10^67 years and the largest by 10^100 (Adams and Laughlin
    1997, search summaries only). At 10^50 years the holes exist and birth nothing. And the early floor is set per
    universe over all its holes together: 10^20 holes birthing one daughter each in the first 10^10 years gives e^(−60) at
    our age, 10^10 daughters e^(−30), a thousand e^(−9). So the across-the-tree reading needs the whole universe to birth
    at most a handful of daughters in its first 10^10 years, which is not "trillions" and, with the lump per daughter
    proportional to the energy fed, would make the late total small as well. The three together (across the tree,
    trillions, the converter) do not fit our age under the published infall history; the per-universe reading needs none
    of this.

## 5. What the toy supplies now, and what it never will

Exact today: b, under Update 66's rule, as the energy fed divided by one daughter's lump; the lump per daughter, a N_slab
(the gross equals the net under the layer form, Update 65); how long X sits between fold and burp (the gate); the room a
burp needs where it is sealed (T9, T18, two directions). Not supplied, and not reachable in this family: every
astrophysical term of section 2. The toy's one contribution to the score is therefore the factor b and its dependence on
λ (the lump per daughter grows with λ, so b falls as 1/(λ − 1) at fixed energy fed), which is the direction series paper
3 (the fertile window) already names: a larger curling cost gives a bigger lump and fewer daughters.

## 6. Our setting as one row, for the record (to verify)

T_star about 10^14 years; T_obs about 10^11; N_BH of order 10^20, formed mostly within the first 10^11 years; T_turn
about 10^100; b and p_obs unknown; today at 1.4 × 10^10 years, early in the era of starlight and inside the observation
window. The dark energy measured now (a constant, or weakening, at one to two sigma; DESI 2025 to 2026) gives the long
heat death and not the rip, which under her rule (ii) is the branch with the larger B, as the owner argued on 18
October. That is consistent with her measure; it is not evidence for it, since the rule was chosen with the outcome
known.

## 7. What would kill it

A setting with observers and a larger B than ours, found among the neighbours of our constants, would falsify her
rule (ii) as a selection principle; and under its across-the-tree reading our own age already does (section 4). No model here can score a neighbouring setting, so the function stands as a
specification until one can; what it fixes now is the list of terms a model would have to produce, and the one
reading of rule (ii), decided the same evening (Update 68): per universe, by each universe's own age, since clocks exist
only inside a universe. Under that reading the observation window W(t) is what keeps the per-universe count from predicting
the red-dwarf era ([LBS16]), so W(t) is the term a critic would attack first: what it must mean (an observer who can learn
its universe's history), and whether planets round the smallest stars host observers at all. The function was not scored on
our age, which was known when W(t) was chosen (rule 13). Other shorteners the owner named the same evening (a rip; dark
energy pulling galaxies apart; no interaction between planets) are in the notebook with what each does: a rip would bring
the peak forward but the data lean away from one and it cuts against her heat-death argument for many daughters; a
constant dark energy leaves bound structures bound and shortens only the window, which is W(t); and "no interaction"
moves nothing as a factor and a great deal as a rule for who counts (each civilization once), which is piece 14's
reference-class choice and is hers to make on its own grounds (sandbox look, LOG 18 October; a look, not evidence).

## 7a. The two definitions, decided (2026-10-19; VISION Update 71)

- **Counting unit: once per civilization.** The owner's choice ("let's go once per civilization"). In T72's terms the
  `fixed` and `hardsteps` kernels; the observer-moment and planet-years units are reported beside as variants, never
  scored. Her reason: a civilization's length of life depends on things the asking itself can affect (how long a
  being lasts, how it learns and passes information, its lifecycle, how destructive it is), so the measure does not
  weight by it.
- **Weight on ages: the causal diamond's comoving volume** ([BHKP07] Eqs. 18, 19; bottom tip at reheating; peaks at
  0.23 t_Λ, 4.05 Gyr for our constant; `Model.diamond_volume` in `scripts/observer_window.py`). Her reason: the strange
  loop and the version probabilities. It replaces the fixed comoving volume; the 100 Gyr cap stays as part of W(t).
- **An observer:** a civilization in which at least one intelligent being asks this particular question.
- **Measured consequences, known when chosen (O138, O139), and rule 13:** under these two choices class D (sun-like
  stars, hard steps) gives F = 0.53 and every other stellar class gives LATE. Our own age is therefore not scored under
  the measure from here; the measure's first test is a quantity it predicts that was not put in (candidates in Update
  71).

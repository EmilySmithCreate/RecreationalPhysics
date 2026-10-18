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

## 4. The one choice left to her: how the generations are combined

Y_k grows without bound in k for any setting with B > 1, so settings cannot be compared by their total yield (O101: a
turn's count has to be finite, and a branching process is dominated by its rate of multiplying). Three rules, each of
which ranks settings differently:

1. **Per universe:** score O(s). Ignores the branching; Update 59's "larger infinity" plays no part.
2. **Growth rate:** score ln B(s), with O(s) > 0 as a filter. This is Smolin's selection for the most black holes
   ([Smolin06], not read) with her observer requirement as the gate: a setting with no observers scores nothing, and
   among settings with observers the fastest-growing tree wins however few observers each universe holds.
3. **A fixed depth or a discount:** score O(s) · B(s)^K for a chosen K, or Σ_k O(s) B(s)^k β^k with β B(s) < 1. Both
   are well defined and both import a number (K or β) that nothing in the hypothesis fixes; the economics of infinite
   streams offers exactly these choices ([Bostrom11], [Askell18], read in part, O101).

Her words of 16 October lean to the second: "each universe producing a trillion more rather than just one more" is what
makes the arrangement more likely from the observer's perspective, with the cold time "just as long". Put as a rule: among
settings whose universes hold observers at all, the setting with the largest B wins; the cold time enters only as the
condition that O(s) stays above zero. That is the recommendation here, with one caution: under it, the measured universe
is predicted to sit near the maximum of B among settings that still allow observers, so the test of the measure is
whether neighbouring settings (a stronger gravity, say) make more black holes and no observers. Rule 13 applies to any
such comparison: a setting that lands near the maximum is not a result until its neighbours have been scored.

A second caution from piece 14 (`docs/theory/orh_findings.md`, section 10): if the loop's versions are Everett's branches,
the count over branches must be Born-weighted, so the plain count of universes in Stage 2 would need a weight per branch.
That is a different question from the combination rule and is not decided either.

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
heat death and not the rip, which under rule 2 of section 4 is the branch with the larger B, as the owner argued on 18
October. That is consistent with her measure; it is not evidence for it, since the rule was chosen with the outcome
known.

## 7. What would kill it

A setting with observers and a larger B than ours, found among the neighbours of our constants, would falsify the
recommended rule as a selection principle. No model here can score a neighbouring setting, so the function stands as a
specification until one can; what it fixes now is the list of terms a model would have to produce, and the single
choice (section 4) that is the owner's.

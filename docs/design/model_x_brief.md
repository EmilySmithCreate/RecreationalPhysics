# Design brief: a model of X turning into space

*Started 2026-09-20 at the author's request. A brief, not a model: nothing here has been built. It says what a design has to achieve, which factors decide how two phases relate, what the published model family already gives us, and which cheap experiments come first. Physics reasoning in it is ours and unreviewed unless a source is given.*

## The goal, in the author's words

Design one set of degrees of freedom in one phase that can transform into another set that is less symmetrical and looks like spacetime, and understand what is at play in the relationship between the two phases.

That is VISION claims 1 and 3 to 5 turned into a construction task. Everything in the project so far has tested pieces of it inside a published model, whose "before" is a random network (VISION Update 5). This brief is about the step after that.

## What "designing" means here

Four choices, and two arrangements they must produce.

| Choice | Meaning | In the published model |
|---|---|---|
| The pieces | what the degrees of freedom are | N vertices, 2N edges |
| The rules | what is forbidden outright | four edges per vertex, two sides, the hard-core rule |
| The energy F | which patterns are rewarded | squares rewarded; squares beyond two on an edge penalised, strength λ |
| The knob | what is turned to cause the change | the coupling g (temperature-like), and λ |

The two arrangements: **X**, specific and stable for now, and **S**, space-like, lower in F.

### The knob λ, in plain words

Think of the graph as a street map. A **square** is a city block: four streets closing a loop. The energy pays 16 for every block, so the network wants as many blocks as it can get. In a flat street grid every stretch of street has exactly two blocks beside it, one on each side. A third block on the same stretch of street cannot lie flat: the map has to fold over on itself there.

**λ is the fine for that folding.** Each block beyond two on a stretch of street is fined 4λ, and a block that overcrowds all four of its streets is fined 16λ in all, which is λ times what it earns.

| λ | What the fine does | What the cold network becomes |
|---|---|---|
| 0 | no fine | blocks are crammed in everywhere; the map folds into tight closed knots, the 4-cubes, and falls apart into pieces. Published: abrupt change, no space |
| between 0 and 1 | folding still pays, but less | cubes are still lowest; the flat sheet is a dip above them |
| 1 | the fine exactly cancels what an overcrowding block earns | cubes, tubes and the flat sheet all tie. This is the value at which the energy is the true curvature formula, the one tied to general relativity. Published: gradual change, a space forms |
| above 1 | folding loses | the flat sheet is lowest. Between 1 and 2, at N = 18, some folded arrangements are dips above it |
| very large | folding is forbidden outright | the "cap" of the 2019 paper |

Why it is the project's first knob: the two published results sit at its two ends (abrupt without a space at 0, gradual with a space at 1), and the hypothesis needs abrupt *with* a space. The question is whether any setting gives both.

## Requirements

| # | Requirement | From | How it would be checked |
|---|---|---|---|
| R1 | One F covers X, S and everything between | claim 3 | by construction |
| R2 | X is a **dip**: every single move out of it raises F. It is specific (one arrangement up to renaming), not a crowd of typical ones | claims 1, 4 | the dip check of `scripts/dip_census.py`; lifetime in a run |
| R3 | S is a dip too, lower than X, and passes "the spot": connected, a finite dimension, flat, local | claim 4, S4 | connectivity columns; dimension measures (not built yet) |
| R4 | The knob that triggers the change is named in advance. **Cooling is fine** (author, 2026-09-20, correcting the assistant, who had written that her picture called for some other trigger): what matters is that a threshold is reached which causes a rearrangement that releases energy and gives geometric spacetime. In physics terms that is supercooling: X is carried below the point where it stopped being the most stable arrangement, stays put because of its wall, and converts when the wall is finally crossed | claim 4 | by construction; then measured as the gap between where the two arrangements tie and where the change actually happens |
| R5 | The change is abrupt: two states coexist, and the energy released per converted vertex is measured | S2, S3 | histogram or entropy curve (T6); sealed runs |
| R6 | X is more symmetric than S, and S can sit inside X in three or more equivalent ways, which favours an abrupt change | claim 3; Landau theory, textbook, *ours in the application* | count the ways; then measure, because it is a tendency, not a guarantee |
| R7 | What is conserved across the change is stated; leftovers (X that did not convert, other arrangements) are allowed and counted | claims 5, 6 | bookkeeping columns |
| R8 | The family and its knobs are fixed before running, and the whole map is published | S1 | pre-registration |

## Factors at play between two phases

| Factor | Plain meaning | Where we have met it |
|---|---|---|
| Which is lower in F, and where they tie | which arrangement the rules prefer at each knob setting | 4-cubes and the flat sheet tie at exactly λ = 1 |
| How many ways each can be arranged | heat favours the one with more ways | the random phase wins at high g by numbers alone |
| The knob | what triggers the change | g in all published work; λ is the other knob we have |
| Dips and walls | "stable for now" means a dip with a wall round it; the wall's height sets how long it lasts. **The first move costs energy, the later ones give back more**: pay the wall, collect the wall plus the height of the dip above the ground. That is an activation energy, as in striking a match | the dip census below: at N = 18, λ = 1.25, pay 5 to get over the wall, and the way down to the flat ground state gives back 17 in all, a net release of 12 |
| What happens to the released energy | In a run at fixed temperature it is carried away and nothing more happens. In a sealed system it stays, and then two things compete: it can carry neighbouring regions over their walls (a chain reaction, an explosion), and it reheats what has not converted, which can stop the change part-way. Supercooled water does the second: tapped, only part of it freezes, and the slush ends up warmer than it started. That is claim 5, "what did not convert remained as hotter X" | not yet met: every run so far is at fixed temperature. It is what the sealed runs of VISION step 3 and S3 are for |
| The symmetry relation | two equivalent ways allow a gradual change; three or more usually make it abrupt | four equal dimensions with one singled out is four ways; four edges at a vertex pairing into two axes is three ways |
| The energy gap where they coexist | the latent heat, Δρ | about 13.6 per vertex at λ = 0 (exploratory) |
| What is conserved | the bookkeeping | same vertices and edges throughout; only the arrangement differs |
| Leftovers | unconverted regions, alternative arrangements | unfinished pieces; the 14-vertex biplane piece, which ties with the 4-cube (ASSUMPTIONS Q8) |
| Dimension of each phase | measured on the graph, not assumed | the ladder below |
| History | what you get depends on the route | hysteresis at λ = 0; quench against slow cooling |

## What the published family already contains (exact, tested)

**A ladder of dimensions.** A vertex has four edges, six pairs of edges. A pair that closes no square is a direction that stays large; curling a side of the torus to length 4 makes one more pair close a square (`test_sheet_tube_cube_ladder`).

| Arrangement | Squares per vertex | Large dimensions | Energy per vertex |
|---|---|---|---|
| flat sheet | 1.00 | 2 | 0 |
| tube, one side of length 4 | 1.25 | 1 | −4(1 − λ) |
| 4-cube, both sides of length 4 | 1.50 | 0 | −8(1 − λ) |

So "a dimension collapses and loops in", the author's illustration in VISION, already exists in this code as a curled side, and the square-count energy rewards it. With this energy the reward never stops: below λ = 1 everything curls (cubes, a shattered graph), above λ = 1 nothing does (the sheet). An arrangement with some dimensions large and one curled is never the lowest.

**Which arrangements are dips** (`test_which_arrangements_are_dips`). The flat sheet is a dip for every λ > 0; the cheapest way out costs 16λ. The 4-cube is a dip only for λ < 1; the cheapest way out costs 32(1 − λ). So for 0 < λ < 1 both are dips and the cubes are the lower one: the reaction-like change this family supports there runs from space to cubes, the opposite of the hypothesis. For λ > 1 the cube is no dip at all: one switch inside a cube already lowers the energy, so cubes cannot be the stable-for-now state above the sheet.

**Dips above the ground state, found by exhaustive search** (`results/dip_census_small.csv`, N = 14, 16, 18, nine values of λ). At N = 18 on the side where the flat graphs are lowest, there are specific, connected arrangements that are dips above them:

| λ | Squares | Height above the flat ground state | Cheapest way out |
|---|---|---|---|
| 1.25 | 21 | 12 | 5 |
| 1.25 | 22 | 16 | 1 |
| 1.5 | 21 | 24 | 2 |
| 2.0, 3.0 | none | | |

So the wiring the hypothesis needs (a specific arrangement, higher in F than the space-like one, with a wall round it) does occur in the published family, in miniature, for λ between 1 and 2. Eighteen vertices are not a space, the walls are low, and nothing is known about larger sizes. It tells us where on the knob to look, no more. [T24] describes the large-scale relative of this: long-lived "allotropes", regions stuck in another discrete arrangement. In his picture they are leftovers; in the author's, X is such an arrangement that once filled everything.

## Candidate directions (none chosen)

- **A. Stay inside the published model, 1 < λ < 2.** Look for dips above the flat ground state at sizes we can simulate: start a run in such an arrangement and measure how long it lasts and what it turns into. No new knob, so S1 is untouched. Needs a sampler that works at low g (T5).
- **B. A reward that stops.** Reward the first curled dimension and penalise the second, so that "some large, one curled" becomes the lowest dip: the author's illustration as a ground state. This is a new knob, so it needs a VISION decision and pre-registration before any run.
- **C. More dimensions.** The same ladder with six or eight edges per vertex has a rung "four large to three large and one curled". Far heavier to simulate; published numerical work exists only for the case we already run.
- **D. A changing membership.** The trigger is a vertex leaving or arriving, not a knob being turned. Needs an energy cost per vertex; parked in VISION.

## First experiments, cheapest first

1. **Done:** the dip census at N ≤ 18.
2. **Rehearse the measurement on the backwards reaction.** For 0 < λ < 1 start from the flat sheet and watch it fall into cubes. The energy released per converted vertex is known in advance, 8(1 − λ), so this tests our way of measuring S3 against an exact number before it is needed for real.
3. **Direction A at N = 64 to 160**, once T5 exists.

## What this brief is not

Not a claim that any of these directions works, not a model of the universe, and not a reason to skip the reproduction gates or the map of plan step 3. It is here so that the design question is written down with its requirements before anyone starts building towards an answer.

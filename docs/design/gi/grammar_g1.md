# The owner's grammar prior (G1), grounded in the record

Written 2026-10-30 (Fable). `PLAN_MATH_MODEL.md` turns the owner's preferences into a grammar: constants limited to
whole numbers, halves and thirds; a sign state s ∈ {−1, +1}; two degrees of freedom as the state; a lower cost for
these constants than for others. Below: where each preference actually occurs in this record, so that the prior is
a list of facts and not a taste; and one finding that the plan should know before G1 is built.

## Where each preference occurs

| Preference | Where it is exact or hers in the record | Kind |
|---|---|---|
| Whole numbers | the energy's coefficients 16 and 4; the walls 12, 16, 32, 36, 48, 64, 128; the spark threshold 12 (320 runs); the per-step walls of the four-direction ladder 20, 40, 80 (halving, exact only at λ = 5/4) | exact |
| Halves | spin one half from three 60° pieces (Update 107, 109); "each twin gets half the curl energy" (Update 122, open against Update 120); D(D − 1)/2 squares per point when flat (exact) | hers; exact |
| Thirds | charge as the net count of signed thirds (Updates 97, 101); three thirds to a strand; 120° = a third of a turn (a true symmetry of the cube, exact); the one-third against two-thirds budget split she noted (Update 30, set aside in Update 50) | hers; exact for the cube |
| Sign | handedness of the twins and of strands (Updates 100, 122); curvature sign, ours negative and the parent positive (H5); the twist label's sign (Update 97) | hers |
| Two degrees of freedom as the state | H1: curl and twist | hers |

## The finding: the record's own λ values fall outside G1

Every registered run uses a curling cost λ from {1.02, 1.10, 1.15, 1.20, 1.25, 1.30, 1.40, 1.50}. Of these only 1.5 is
a half; 1.25 is a quarter; the rest are tenths and twentieths. And the ladder's square count per point rises by
**a quarter** per curled direction (exact: S/N = D(D − 1)/2 + c/4). So a G1 restricted to whole numbers, halves and
thirds cannot write the toy's own rule in its own units. Three ways out, for the owner to choose (⚑):

1. **λ is an input, not a constant**: the grammar reads λ as a stated number, as the open world reads N and L, and
   the constants the model may write stay whole, half or third. Then the rule needs only 4 and 1/4.
2. **Admit quarters** (powers of two down to 1/4). Cheap, but then "halves and thirds" was not the preference; the
   preference was "small denominators", and that should be said.
3. **Rescale the units**: count squares per four points and energy per quarter-unit, so that every constant in the
   rule is a whole number. That is a choice of unit, which the plan's G0-against-G1 comparison must then declare.

A fourth possibility: the quarters are an artifact of the toy's curl length 4 (a direction curled to length 4 adds
one square per four points). In the base, where no length exists, the preference may hold. That is hers to say, and
it is why the G0-against-G1 test on worlds "not built to suit" G1 is the right test: if G1 wins there, the quarters
were the toy's.

## The simplicity measure

The plan asks for a written simplicity measure. The record has one already, implicit in every exact reading: the
number of distinct constants and the number of statements (the open world's limits are 12 numbers, 160 tokens,
depth 6). Proposed, not decided: cost = tokens + 4·(number of constants outside G1) under G1, tokens alone under G0.
The 4 is a knob and should be scanned, or the comparison is a fit.

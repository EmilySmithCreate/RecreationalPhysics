# The curl-store world family: two state variables, three readings (families D and N; math model curriculum step 3)

Written 2026-10-30 (Fable). Generator: `scripts/gi_world_family.py`; tests: `tests/test_gi_world_family.py`.
The world is built from exact facts of the record (the curling ladder and its walls) so that the hidden rule is
known to the last digit and the readings are the ones the toy's own runs report. It is a world family in the sense
of `PLAN_MATH_MODEL.md` ("state (u, v), three readings r1, r2, r3, each a hidden function of (u, v) and the step") and
of the eval's D family. It is **not** a world in (curl, twist): twist has no dynamical rule in the record yet.

## The state

- **u** = the number of directions still curled at the region, 0 ≤ u ≤ D.
- **v** = the energy in the store (the bath of Creutz-type stores of `sealed_d.py`, in the toy's units).

## The hidden parameters (never in a prompt)

D ∈ {2, 3, 4} directions; λ from a grid; N the number of points (shown as a stated number, as the open world shows N);
f the feed per step (whole number, 0 for a sealed spark); u0 the curled directions at the start; v0 the store at the
start; and the wall table w(D, u, λ), which is exact: the cheapest single-move kind of the rung, read from
`docs/figures/ladder_kinds.json` (ASSUMPTIONS O49, O50; `scripts/exact_ladder_d.py`).

## The rule (hidden; the generator's simulator is the verifier)

Each step:

    v = v + f
    if u > 0 and v >= w(D, u, lambda):
        u = u - 1
        v = v + a * N            # the release of one direction, a = 4 (lambda - 1) per point, paid into the store

Then the readings, each a function of u alone:

    r1 = a * u                   # energy per point (H / N) of the rung
    r2 = D (D - 1) / 2 + u / 4   # squares per point (S / N)
    r3 = D - u                   # local dimension d

So the second state variable, v, is visible **only through when the drops happen**. That is what makes the family
hard in the way the plan wants: the three readings over-determine u and say nothing about v except its timing.

What the rule encodes from the record (exact, with the registered results that measured the same thing):

- the wall does not grow with N and the release does (Update 9; the 320-run spark threshold);
- a sealed spark below the wall never opens anything (Update 9, "a tube with nothing to spare never converts");
- whether a release pays the next wall is the cascade question of piece 5 (T44 to T56): here it is arithmetic.
  At D = 3, λ = 5/4, N = 288, from u = 2 with a spark of exactly 16 (the rod's wall), the first opening pays 288 into
  the store, which exceeds the slab's wall of 36, so the second opens next step: a cascade. At N = 16 the store holds
  16 + 16 = 32 (a wall is a hill, not a toll: the spark is kept, O71), below 36: a stall. The toy's registered runs did **not** behave this simply (ADVANCES ONLY, O105; the slab
  breaks before it opens, O132), because the real barrier is not the single move (O118). The world family states the
  single-move rule as its law; the discrepancy is a C-family item (`conflict_items.md`, item 2), not a defect here.

## Kinds

| kind | f | what it tests | label |
|---|---|---|---|
| `fed` | > 0 | a steady feed: the drops come at the step when the store first reaches each wall | rule |
| `spark` | 0 | one spark v0 at the start: cascade, partial cascade or stall, decided by v0, the walls and aN | rule |
| `twisted` | > 0 | **foil: needs three state variables.** A hidden twist store y fills by 1 a step; an opening needs y ≥ κ as well as v ≥ wall, and y resets to 0 at each opening. Since y counts the steps since the last opening, it is not a function of (u, v): two worlds at the same (u, v) with different y have different futures. (A first design, a sign that flips at each opening, was found to be a function of u and was dropped.) The draw is kept only if y actually delays a drop | `not reducible to two` |
| `noisy` | > 0 | **foil: no rule within the budget.** The drop steps are drawn at random (seeded) with no wall | `no rule found` |

Every batch holds matched foils (the sister repository's rule 5). The right output on a foil is its label, decided
from residuals under a fixed budget; the generator writes the label under `hidden`.

## The task and the scoring

A case shows the readings for steps 0..T (the window) and the stated numbers N and D is readable from r2 and r3 at
step 0. The task is to recover the state rule and the reading map well enough to predict the three readings at the
probe steps T + 1, 3, 5, 10, 15 on **fresh parameters** (three fresh (f, v0, N) draws with the same D and λ), as the
open world scores (probe accuracy, tolerance 0.01). The window is chosen so that at least one drop falls inside it
and at least one falls after it; a model that only extrapolates the last plateau fails the later probes.

## The rule in the extended model language

The open world's language has the writable names `x, step, m1, m2, y, ystep`. The extension the plan asks for
(state `u, v`, readings `r1, r2, r3`) is written here as it would read; the one thing the grammar lacks is a table
lookup for w(D, u, λ). Two ways round it, for the sister repository to choose: pass the rung walls as stated
numbers `w1, w2, w3, w4` (then the rule is expressible today), or admit a `wall(u)` call. With the first:

    v = v + f
    if u > 0 and u == 1 and v >= w1 { u = 0; v = v + a * N }
    if u > 1 and u == 2 and v >= w2 { u = 1; v = v + a * N }
    if u > 2 and u == 3 and v >= w3 { u = 2; v = v + a * N }
    r1 = a * u; r2 = D * (D - 1) / 2 + u / 4; r3 = D - u

(The `u > k and u == k+1` guards keep one opening per step, as the simulator does.)

## Grammar prior check (G0 against G1)

The rule's constants are 4 (whole), 1/4 (a quarter), and λ − 1 (a quarter, a tenth, two fifths at the record's
settings). Under G1 as written in the plan (whole numbers, halves, thirds, sign) the reading map r2 is **not
expressible** unless quarters are admitted or λ and the per-direction square count are inputs. `grammar_g1.md`
records this and asks the owner.

## Usage

    PYTHONPATH="src;scripts" python scripts/gi_world_family.py --seed 1234 --per-kind 6 --out out/gi_world
    PYTHONPATH="src;scripts" python scripts/gi_world_family.py --seed 1234 --per-kind 6 --out out/gi_world --private

`--private` writes the hidden halves to a separate file so that the public half can be shared and the hidden half
kept out of git; the plan's privacy condition for the owner's framework. The output is deterministic in the seed.

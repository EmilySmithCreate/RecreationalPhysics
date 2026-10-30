# Resources for the three GeneralizedIntelligence plans, built from this record

Written 2026-10-30 by Claude Fable 5.1 (Fable) at the owner's request: "based on your interpretation of the 3 step
generalized intelligence plan, can you create some resources?" The three plans are in the sister repository
(`EmilySmithCreate/GeneralizedIntelligence`, PR #28, merged): `docs/PLAN_FRAMEWORK_EVAL.md`, `docs/PLAN_FINETUNE.md`,
`docs/PLAN_MATH_MODEL.md`. Nothing here is decided, registered or run as a test of the hypothesis; every statement is
labelled as rule 10 asks (**exact**, **measured**, **hers**, **published** with read status, **ours** unverified).

## 1. How I read the three plans against her story

The owner's one-paragraph statement of 30 October, in her words: spacetime is one version in a large infinite loop;
the pattern is simulated by an underlying two-degree-of-freedom state ("2d": not a plane, not time); the set of
inequities is self-referential, forming looping patterns like a video of a screen showing the video; observers can
evolve within the 3D spacetime simulated by the 2D state. *(I read "inequities" as inequalities: the constraints the
base must satisfy, such as the zero-total rule and "store at least the wall". ⚑ To confirm.)*

Where each sentence already sits in the record:

| Her sentence | Where it is in the record | Kind |
|---|---|---|
| The base is two degrees of freedom, not a plane, not time | H1, confirmed 25 October: curl and twist; points and links describe the emergent space (`docs/design/owner_questions_2026-10-24.md`; VISION Updates 107, 108, 119) | hers |
| 3D spacetime is simulated by the 2D state | "the flat space seen from inside is the fractal of the two degrees of freedom" (Update 122); the toys are built from points and links for that reason | hers |
| One version in an infinite loop | the strange-loop measure (Updates 23, 26, 43); a turn ends when all matter is in black holes (Update 44, her conjecture); the fed slab cycles (T71, measured, O144, O160) | hers; measured only as the toy's cycle |
| Self-referential, video of a screen | no self-reference exists in any toy; the nearest things are the observer measure (the loop selects the loop that holds its observers) and the twin birth (a universe births universes) | hers; **not modeled** |
| Observers evolve inside | the measure (Update 43); no toy has observers | hers; **not modeled** |

The three plans, read against that:

1. **The framework eval** (first; the yardstick). Its four task families map onto her theory directly, and her
   framework is the plan's own "private final test". What it needs from this record: an **axiom system** in the F
   (fidelity) form with exact answers and textbook foils; a **two-state-variable world family** for the D (discovery)
   form, "observed in 3D, made from 2"; **conflict items** (C) where the record's own observations contradicted a
   prediction; and **foils** (N) that really need three variables or have no rule.
2. **The fine-tune.** It needs the **imports ledger** to be concrete: a word list of what pulls a model back to the
   textbook, and her vocabulary beside the toy's variables, so that a reversion can be counted.
3. **The math-only model.** It needs her preferences as a **grammar prior (G1)**: whole numbers, halves, thirds, sign;
   and a first **numbers-in table** whose hidden rule is known exactly, so that M0 (search) has something real to try
   before the private test.

## 2. The resources

| File | For which plan | What it is | Status |
|---|---|---|---|
| `framework_axioms.md` | eval, family F; fine-tune (reversion pairs) | Her framework as twelve axioms, each labelled; the four textbook habits the plan names, each instantiated; a question bank of twelve with exact answers and the textbook-habit answer that would count as a reversion | exact answers checked by arithmetic here; the physics is hers |
| `world_family_curl_store.md` + `scripts/gi_world_family.py` + `tests/test_gi_world_family.py` | eval, family D and N; math model, curriculum step 3 | A two-state world built from the exact ladder: state (curled directions, store energy), three readings (energy per point, squares per point, local dimension), a feed or a spark, a cascade or a stall; foils that need a third variable (twist) and foils with no rule | generator runs, deterministic, tested |
| `grammar_g1.md` | math model (G0 against G1) | Her grammar prior grounded in the record: where whole numbers, halves, thirds and signs actually occur; one finding (the record's own λ values are quarters and tenths, outside G1 as written) | ours, from the record |
| `imports_glossary.md` | eval (imports), fine-tune (ledger) | Her words, the toy's variables, the textbook words, in one table; the reversions this project has already committed and corrected | ours, from the record |
| `conflict_items.md` | eval, family C | Eight cases where a pre-registered prediction of hers or ours failed in the toy, written as framework + contradicting observation + the faithful response | measured, from the record |

## 3. Three cautions

- **Privacy of the final test.** The plan keeps her framework "outside the repository, never in any training set, run
  once". This repository is public. The axiom and question files here are therefore a *draft* of that test, not the
  test: if she wants the guarantee, the question bank's numbers are regenerated locally with a fresh seed (the
  generator takes one) and the regenerated file stays out of git. The axioms themselves are already public in VISION.
- **The toys are not the base.** Every exact number below is a fact about points and links at two, three or four
  directions, which she calls a description of the emergent space, not the two degrees of freedom themselves. A
  world family in (curl, twist) proper cannot be written until twist has a dynamical rule (Update 97 declares a
  label, no rule). The world family here uses (curled directions, store), which is what has been measured.
- **Nothing here tests the loop.** The self-referential loop, the video of a screen, and observers are not in any
  toy. The resources make her framework *checkable for fidelity* (does a model stay inside it?) and *discoverable*
  (can a model recover its rules from numbers?). They do not make it true.

## 4. What is asked of the owner (one line each)

1. ⚑ "Inequities" read as inequalities (constraints): right, or did you mean something else?
2. ⚑ In the G1 grammar, are quarters allowed (the toy's λ = 5/4 and its c/4 squares per point need them), or is λ an
   input number rather than a grammar constant?
3. ⚑ Should the question bank be regenerated with a private seed and kept out of git, as the plan's privacy asks?

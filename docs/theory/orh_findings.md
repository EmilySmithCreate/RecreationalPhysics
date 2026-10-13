# Observer-relative histories: findings of 12 October 2026

The one home for the results of the program in `observer_relative_histories_research_handoff.md` (the owner's
handoff of the same day), worked through its Stages A to F. The plan is `orh_implementation_plan.md`, the
literature map `orh_stage_a_literature_map.md`, the assumption register `orh_assumptions.md`. Code: `src/orh/`;
exact tests: `tests/test_orh_*.py` (49 tests); results: `results/orh_stage_bcd.csv`, `results/orh_stage_e_summary.csv`,
`results/orh_stage_e_curves.csv`, each with a `.meta.json` carrying the config and the commit; figures:
`docs/figures/orh_*.png`.

**Kinds of statement (CLAUDE.md rule 10).** *Exact*: closed forms and exact state-vector computations, each
checked by a test; the Stage E population model's arithmetic on its declared inputs is exact in this sense too
(given those inputs; its config is labeled exploratory and no claim is made that any of its knobs is right).
*Ours, unverified*: every reading below, including every reading of a Stage E number. *The owner's*: the handoff
and its commitments. Nothing here is measured in rule 10's sense: no pre-registered run of the project's toy was
made. No physicist has read any of this. *(Reworded 2026-10-12, later the same day: an earlier version of this
paragraph and of the section 6 heading used a fifth kind, "model output", which rule 10 does not have.)*

**Provenance note (2026-10-12).** The three files `results/orh_stage_bcd.meta.json`,
`results/orh_stage_e_curves.meta.json` and `results/orh_stage_e_summary.meta.json` name commit `e59d87ba` with
`git_dirty: true`. That commit contains nothing under `src/orh/` (`git ls-tree -r --name-only e59d87ba -- src/orh`
is empty): the code that produced the results was untracked when they ran and was first committed, together with
the results, as `c23803cf`. The cause is that `graphity.results.provenance` looked only at tracked files, so
untracked code never counted as a departure from the named commit; it was found by a reviewer on 12 October and
the helper now counts untracked files as dirty and lists them (`git_untracked_count`, `git_untracked`; a test
exercises it in a temporary repository). The three `.meta.json` files are left as written (rule 5). The check in
their place: the results are deterministic computations with no random number, so a re-run under the committed
code is the test. Done on 12 October in the worktree at the merge of `c23803cf`'s branch with `main`, with the
scripts and `src/orh/` byte-identical to `c23803cf`, writing to a scratch directory outside `results/`: all three
CSVs (`orh_stage_bcd.csv`, 157 lines; `orh_stage_e_summary.csv`, 200; `orh_stage_e_curves.csv`, 9,901) came out
identical to the stored ones line for line, differing only in the line ending (the re-run on Windows wrote CRLF).
The figures redrawn by that re-run were byte-identical to the stored ones as well. (Later the same day the figure code in `scripts/orh_stage_e.py` was changed for figure 6, so that script is no longer byte-identical to `c23803cf`; the computation it runs is unchanged, and the `--figures-only` path writes nothing under `results/`.)

## 1. The answer to the first question: what is established, assumed, new

From Stage A (the map has the paper, section and equation for every row):

- **Established physics, restated.** Unitary evolution with records written by entangling interactions; class
  operators, the decoherence functional, probabilities for a decoherent family and their sum rules; records as
  orthogonal environment states, with interference visibility equal to their overlap; redundant records read by
  many observers; the conditional probability of the past given present records, and the nesting of records
  (Everett 1957 Sec. 5; Gell-Mann and Hartle 1993, 1995, 2018; Zurek 2003, 2009; Zwolak and Zurek 2017).
- **Interpretive assumptions, declared by the handoff or found on reading.** Everett's reading of the formalism
  (two of the handoff's own sources would not sign it as worded); a branch-independent family of histories; a
  final condition of indifference, which a one-boundary decoherence functional silently assumes (Hartle 2020);
  perfect records; "negligible off-diagonal terms" meaning medium rather than weak decoherence; a uniform
  self-location rule over observer-moments, and its pooled normalization across histories, which is Sebens and
  Carroll's form and not Srednicki and Hartle's.
- **Propositions that needed checking, and what the check found.** (i) The nested compatible set with
  nonincreasing measure: a restatement of Everett 1957 Eqs. 26, 33, 34 and of Gell-Mann and Hartle 2018 Eq. 20;
  true in the toy whenever the family is decoherent, false when a record is erased. (ii) The record surprisal:
  a definition (Shannon self-information) already made on nested record algebras by Martellini 2026, to be read in
  full before it is cited. (iii) Joint record distributions of interacting observers: Everett 1957 Sec. 5's own
  calculation; exact in the toy. (iv) The cosmic-time fraction F(13.8 Gyr): Loeb, Batista and Sloan 2016's
  calculation with other weights, already published four times under four rules with answers from 0.1 % to 68 %.
  **The prior-work search returned FOUND on all three of the handoff's candidate-novel claims; no sentence of the
  form "we have not found" may be written about any of them.**

## 2. Stage B: the exact small Hilbert-space model (exact)

The model: a system qubit, up to twenty environment qubits written by controlled tilts of angle theta (pi/2 is a
perfect copy), observer registers that copy fragments. Everything below matches its closed form to machine precision
(`tests/test_orh_darwinism.py`).

- **Visibility against environment overlap (Stage F item 1).** V = 2 sqrt(p(1 - p)) prod cos theta_i; for p = 1/2 it
  is the overlap |<E_B|E_A>| exactly, a straight line through the origin (`orh_stage_b_visibility.png`).
- **Partial information.** With perfect records I(S:F) sits at the classical plateau h(p) for every fragment short
  of the whole environment and rises to 2h(p) at the end; with weaker records the plateau is approached more slowly
  (`orh_stage_b_partial_information.png`). The von Neumann mutual information is used; the Holevo quantity, which has
  no final rise, was not computed (assumption P4).
- **Redundancy** R_delta = N / m_delta with delta = 0.1 and N = 20: 20 at 90 and 75 degrees, 10 at 60, 6.7 at 45,
  2.9 at 30, 1.7 at 15. A weak record is not redundant.
- **Eraser and recombination.** A perfect record kills the fringes (V = 0); reading the record in the conjugate basis
  and sorting restores V = 1 in each subensemble and 0 overall; the inverse interaction restores V = 1 exactly. In a
  two-qubit toy recoherence is easy; the papers stress that at scale it is not, and the toy's ease is a size artifact,
  not physics (Stage A, section 3).

## 3. Stage C: the history-measure model (exact)

- **The two-slit family interferes and still has total weight one.** With no record, the decoherence functional
  of (path, output) has every diagonal entry 1/4, off-diagonal entries of 1/4, and a diagonal that sums to 1 because
  the off-diagonal entries cancel in pairs. The sum rule for "output 0" fails: the fine-grained sum is 1/2 where the
  coarse-grained probability is 1. With a record of angle theta the off-diagonal entries are cos(theta)/4; at 90
  degrees the family is exactly decoherent and every sum rule holds (`orh_stage_c_decoherence_functional.png`).
  **So the handoff's Stage C demonstration, "the sum of exhaustive history weights stays one even as one record's
  compatible set shrinks", holds for every family, interfering or not, and tests nothing.** The sum rules, one per
  coarse graining, are the test.
- **Nested records (Stage F item 3).** Four systems with Born weights 0.3, 0.8, 0.5, 0.9, each recorded by its own
  register. The compatible set of the record "1, 1, 1, 1" shrinks from 8 histories to 1; its measure falls 0.3,
  0.24, 0.12, 0.108, exactly the running products; the surprisal rises 1.74, 2.06, 3.06, 3.21 bits; the family is
  exactly decoherent at every step (`orh_stage_c_nested_measure.png`). This is Everett's product measure, as the
  map says. *Checks of the code, not findings (exact, by construction; relabeled 2026-10-12):* the compatible
  sets nest, which holds for any record that extends the one before, since the set is an intersection; the
  conditional measure inside each set sums to one, which is how it is normalized; and the total weight stays one,
  which section 7 item 1 says holds for interfering families too. The script computes all three and the tests
  assert them, so that a bug would show; none of them says anything about decoherence or about records.
- **Two observers of one record.** mu(A = 0 and B = 0) = mu(A = 0) = 0.7, not 0.49; mu(A = 0 and B = 1) = 0.
- **An erased record is not a permanent fact.** With the record undone before the second time, the family that
  includes the earlier record value has off-diagonal D = 1/4 again and is not decoherent; with the record kept it
  is. Gell-Mann and Hartle's caveat about the permanence of the past, in two qubits.
- **Born weights are not branch counts.** Two histories carry 0.1 and 0.9; copying the record into a second
  register changes no weight and adds no history with weight.

## 4. Stage D: interacting observers (exact)

(`tests/test_orh_observers.py`; `orh_stage_d_joint_records.png`, Stage F item 4.)

- Two observers reading one error-free record never disagree: the joint distribution has only (0, 0) and (1, 1),
  at 0.7 and 0.3; the product of their marginals would put 0.21 on each disagreeing pair. Their records share
  h(0.3) = 0.88 bits of mutual information.
- With imperfect fragments (60 and 60 degrees) they disagree 11.25 % of the time, the closed form; at 90 and 60
  degrees 7.5 %.
- Telling: an observer with no record (0 bits with the other's) is perfectly correlated after being told.
- Forgetting: the swap takes the observer's mutual information with the system to zero and gives it to the sink;
  the branch weights (0.7, 0.3) are untouched; the observer's later register says 0 in every history, so its
  compatible set is everything again.
- Duplication changes the number of observers holding the record and not the Born weights.
- A register that is maximally mixed cannot hold a record: its state is the same whichever value the system has,
  and a second observer who reads it agrees with the system only half the time. A blank register copies exactly.
- The forward circuit run backwards unwrites every record; the count of registers correlated with the system grows
  0, 1, 2, 3, 4 along the forward circuit from the blank start.

## 5. The third question: records and the direction of experienced time

What the toy shows is narrow and standard: records accumulate in one direction along a unitary circuit because the
registers start blank, and the same circuit reversed unwrites them; a register that is not in a low-entropy state
holds no record. That is the thermodynamic arrow feeding the arrow of records, with no collapse anywhere. It does not
show that records *explain* the direction: in Hartle 2020 the explanatory order is the reverse (the asymmetry between
the initial and final conditions is why records can exist, and a one-boundary formalism assumes a final condition of
indifference), and none of the fourteen papers says anything about *experienced* time or its continuity. **Verdict on
the question as worded: partly standard (no collapse is needed; records are physical correlations that nest along a
branch) and an overreach in "explain" and "experienced".** What the toy adds to the standard account is nothing.

## 6. Stage E: the cosmological population model (exact arithmetic on declared inputs; every reading ours, unverified)

One fixed Planck-2018 background; Loeb et al. 2016's equations for star formation, the mass function, lifetimes and
the habitability window; our declared knobs (delay, observer window, lower stellar mass, reference class, interaction
factor, exotic late observers; register P11 to P24). The numbers are exact given those inputs (a deterministic
integral on a fixed grid; the grid is in the config); nothing about the inputs is measured, and the config
`configs/orh_stage_e.json` is labeled exploratory. The scenario grid was written before the script ran. Figures:
`orh_stage_e_w_of_t.png` (Stage F item 5) and `orh_stage_e_f_today.png` (item 6). *Two notes of 2026-10-12, later
the same day:* (a) the three reference classes that ran are not the three the plan declared. The classes that ran
were recorded at the time in register entry P20 (commit c23803cf, with the results); what was never written, until
a reviewer found the mismatch on 12 October, was that the plan's declared "uniform over observers" had been replaced
by `late`. The plan carries the dated entry (Stage E, "What ran, against what was declared"); "late-weighted
moments" in the table below is the class `late` of `src/orh/cosmic.py`, observer-moments weighted by the age of the
planet's observer era, and "uniform over origins" is `origins`, each inhabited planet counted once at its origin.
(b) Figure 6 was redrawn from the stored summary CSV: its first version clamped values at 10^-6 on an axis starting
at 10^-5, so the four late-weighted values below 10^-5 fell off the axis, and it labeled the `late` class "uniform
over late". They now sit on the axis floor as open markers with their own legend entry, which points to
`results/orh_stage_e_summary.csv` for the values. Three of the four are in the table below (7 x 10^-7, 2 x 10^-6,
1 x 10^-7); the fourth is Loeb et al.'s own setting (`loeb_baseline`) under the late-weighted class, 2.5 x 10^-6,
which has no row in the table.

**The published core is reproduced in kind.** Loeb et al.'s own setting (stars from 0.08 to 3 solar masses, no delay,
observers for the star's life, the 50 Gyr cutoff) gives F(13.8 Gyr) = 0.0017 against their "0.1 % at most", with
the peak of dP/d ln t at 4.4 x 10^12 yr against their "around 10^13 yr"; Sun-like stars only put the peak at 12.6 Gyr,
their "the current time indeed represents the peak". The test that pins this was written before the run.

**F(13.8 Gyr) under the main scenarios and the three reference classes** (interaction off, no exotic observers):

| Scenario (lower mass; delay; observer window) | Uniform over observer-moments | Uniform over origins | Late-weighted moments |
|---|---|---|---|
| Red-dwarf-friendly (0.08; 4.5 Gyr; the star's life) | 0.00085 | 0.81 | 7 x 10^-7 |
| Friendly, observers for 1 Gyr per planet | 0.79 | 0.81 | 0.78 |
| Red-dwarf-suppressed (0.5; 4.5 Gyr; the star's life) | 0.085 | 0.81 | 0.0084 |
| Sun-like only (0.9; 4.5 Gyr; the star's life) | 0.60 | 0.81 | 0.46 |
| Friendly, delay 1 Gyr | 0.0015 | 0.91 | 2 x 10^-6 |
| Friendly, delay 8 Gyr | 0.00029 | 0.59 | 1 x 10^-7 |

Other rows (the 20 Gyr cutoff, no cutoff) move the suppressed case by less than 0.01. The interaction factor at
gamma = +0.5 or -0.5 moves F by at most a third (Sun-like: 0.60 to 0.69 or 0.43). The last supporting time is
1.07 x 10^13 yr in every friendly scenario with observers for the star's life (the lifetime of a 0.08 solar-mass star),
about 120 Gyr in the suppressed ones and about 60 Gyr Sun-like; t_99.99 sits just inside it. With exotic late
observers at any rate per physical volume the integral does not converge and F and t_99.99 are undefined, as Bousso,
Freivogel and Yang 2008 Sec. V.E says.

**What moves F most, in order:** the reference class (at the same physics, 0.0009 against 0.81 against 7 x 10^-7);
the observer window (a 1 Gyr window at the same physics: 0.0009 to 0.79); the lower stellar mass (0.0009, 0.085,
0.60); then the delay, the cutoff and the interaction factor, each by less than a factor of five. **The two
normalizations of F across histories differ by a factor of fifty in a two-history demonstration** (friendly and
suppressed at equal Born weight: pooled 0.00086, averaged 0.043), so the handoff's F(t_0) and Srednicki and Hartle's
xerographic recipe are different quantities, and which is right is not decided by anything here.

**Against the expectations written before the run** (`orh_implementation_plan.md`, Stage E): the friendly case under
observer-moments at a few per cent at most, held (0.09 %); the suppressed case between 0.2 and 0.6, **missed** (0.085);
no scenario making today the median unless the cutoff rises to near a solar mass, held in that clause (Sun-like: the
median is 12.7 Gyr) but **missed** in not anticipating that a short observer window does the same at any stellar
cutoff (median 10 Gyr); t_99.99 undefined only with endless support and otherwise set by the longest stellar
lifetime, held; the reference class moving F more than the stellar inputs, held.

**Against the published numbers:** the toy's span, from under a millionth to 0.92 depending on the rule, contains
Loeb et al.'s 0.1 %, Lineweaver and Egan's 68 % (origins-like, no lifetime weighting), Hanson et al.'s below 1 %
(long planet lifetimes) and Behroozi and Peeples' order 7 %. The published spread is the reference-class spread.

## 7. Null results and contradictions, stated plainly

1. The handoff's Stage C demonstration ("total weight stays one") is true of interfering families too; it is not a
   check of decoherence. Replaced by the sum rules.
2. The nested-measure statement holds only while the family stays decoherent; an erased record breaks it exactly.
3. "Records explain the direction of experienced time" reverses the explanatory order of the handoff's own source
   (Hartle 2020) and adds "experienced", which no source addresses.
4. F(13.8 Gyr) is not a test of anything: it varies by six orders of magnitude across declared rules, and using
   it as evidence for a rule is the selection fallacy of Hartle and Srednicki 2007 Eq. 4.2.
5. The handoff's F(t_0) is not Srednicki and Hartle's xerographic distribution; the two differ by a factor of fifty
   in a two-history example.
6. With any exotic late observers the end criterion t_99.99 does not exist.
7. Two of our own pre-registered expectations for Stage E missed (section 6).
8. The quantum toy's ease of recoherence is a size artifact; the von Neumann against Holevo choice for I(S:F) is
   ours; the branch-independent family and the indifferent final condition are assumptions, not results.
9. Two of the handoff's seven priority sources are not Everettian and would not sign commitment 2 as worded.

## 8. Is anything here a new, falsifiable consequence?

**No.** Stages B to D are consistent restatements of Everett and decoherent histories, each now exact in a toy; the
one named quantity not in the fourteen papers is a definition already published elsewhere. Stage E is a population
model whose output is absorbed by its declared knobs: the reference class and the observer window move F(13.8 Gyr)
across six orders of magnitude, so no observation of "how early we are" can test the quantum part, and the
cosmological part reproduces the published spread rather than narrowing it. The handoff's success criteria 1 to 4 are
met in the narrow technical sense it asks for (interference suppression and shared records; rising surprisal along a
record sequence, where the nesting and the conserved norm beside it are checks of the code and not findings, section
3; joint histories for interacting observers; a declared weighting giving a distribution with its sensitivity), and
criterion 5 is answered: nothing here is a new prediction. A falsifiable
consequence would need an observable the knobs do not absorb; none was found.

## 9. What is asked of the owner

1. Whether this line becomes a piece of the programme page (a draft card is on the page, marked ours), or stays a
   note in the theory folder.
2. Whether Martellini 2026 (arXiv:2607.25307) is to be read in full; until it is, the record surprisal is not cited
   as ours anywhere.
3. Whether to keep the handoff's pooled F(t_0) or Srednicki and Hartle's averaged form as the declared rule, if
   Stage E is ever quoted.
4. Whether piece 9 adopts the published rule as the hypothesis's own (the amplitude rule proposed on 23 September
   and held since), with the toy of section 2 as the benchmark it must pass before Bell.
5. Whether the two-turn test of section 10, item 5, is registered.
6. Whether the claim's last sentence, revised on 12 October from this page (programme draft and page), is hers.

## 10. What the published mathematics gives the hypothesis (ours, unverified; added later on 12 October)

The owner's framing of the same day, on the prior-work result that every candidate-novel claim was already
published: "I don't need this to be new, much better if I can apply existing math and physics to my theory and use
it to predict and identify testable hypotheses and understand the key variables and constants." Sections 1 to 8
answer the handoff's question (what is established, what is new). This section answers hers, and her question of
the same evening: is there a narrative or mathematical connection between the amplitude-and-record rule and the
strange loop? Every item is ours and unverified. Published relatives are named where we know them; "general
knowledge" means not read by us, to verify before it is cited.

1. **Piece 9's missing rule is identified, and it is the standard one.** Her versions, standing at once until an
   interaction tells them apart, are Everett's branches. The interaction that tells them apart is one that writes a
   record somewhere in the surroundings, and two versions interfere exactly as much as their records overlap
   (section 2: V equals the overlap; section 3: a kept record makes the family decoherent, an undone one brings the
   interference back). The cancelling that counting could not do (T15 rung 3a: positive weights only add) is done
   by amplitudes. What this changes for piece 9: the search is no longer for a cancelling rule but for where the
   loop puts the amplitudes. The rule proposed on 23 September (`docs/design/amplitude_rule_brief.md`: amplitudes
   on a loop's points, evolving by the loop's Laplacian; quantum mechanics put in, not derived) is that rule in the
   toy's terms, and she held it. The benchmark any version must pass before Bell is this toy: visibility equal to
   record overlap, interference restored when a record is undone.
2. **Her strange-loop measure must be Born-weighted, by Everett's own derivation.** Everett 1957 Sec. 5 (Eqs. 26,
   33, 34, read in the Stage A note) asks for a measure on the branches of a superposition that is additive (the
   measure of a branch equals the sum of the measures of its sub-branches) and depends only on the amplitudes, and
   finds that the squared amplitude is the only such measure. Her count per turn (VISION Updates 23, 26, 43; O101)
   needs exactly that additivity across the branches of a turn. So, if her versions are Everett's branches (item
   1), a turn's yield is the Born-weighted sum over its branches of the observers each holds, in the declared unit:
   an expected yield, not a count of versions. A plain count is additive but ignores the amplitudes, which is rung
   3a's failure in another form; in the toy, duplicating an observer changed the count and no weight (section 4).
   What is left to choose is the unit (observer-moments, observers, civilizations per turn), which is the
   reference-class choice of Stage E in other words, and the combination rule across histories (pooled, Sebens and
   Carroll's form, or averaged, Srednicki and Hartle's; a factor of fifty apart in the two-history example of
   section 6). Both are hers.
3. **The view from outside the loop is a computed object.** In decoherent histories the probabilities of whole
   coarse-grained histories of a closed system, p(alpha) = D(alpha, alpha), are defined with no observer outside
   (Gell-Mann and Hartle 1993, 2018; Hartle 2020). The observer with one more dimension who sees every turn and
   every branch at once, each with its weight, is in the mathematics the decoherence functional of the universal
   state. Everett's relative state was built for exactly the loop's condition, no vantage point outside: each
   observer's state is relative to what it has interacted with. That is the mathematics of the sentence Update 20
   left "untouched as philosophy and unused as physics". Her words of 11 October (`sandbox/NOTEBOOK.md`: a view
   from the fourth dimension in which "there is no meaningful difference between the particles until a measurement
   pulls the particle into 3d") are this picture, with the measurement as a record written in the surroundings.
   Relatives of a timeless whole with time read from correlations inside it: Page and Wootters 1983 and the
   "problem of time" of canonical quantum gravity (general knowledge).
4. **A loop that turns for ever needs a stage that erases records, and the toy says what erasure does.** Within a
   turn, records accumulate one way only because the registers start blank (section 5; Hartle 2020 puts the
   direction in the asymmetry between the two ends of a history). In a loop the end of one turn is the start of the
   next, so for every turn to carry the arrow, the turn's end must return the registers to blank: the turn boundary,
   in her picture black holes gathering everything and burping, must erase records. Exact in the toy: an erased
   record restores interference between the histories that differed in it (section 3), and forgetting leaves the
   branch weights untouched (section 4). So, ours and unverified: to the extent the boundary erases, the branches of
   one turn re-merge there and the next turn's branching starts fresh, which is what her "turns need not differ;
   all equally real" requires; to the extent it preserves, branches never re-merge, the compatible set shrinks turn
   after turn without reset, and each turn inherits the last turn's arrow instead of renewing it. Which it is, is the
   black-hole information question in her terms (general knowledge: whether black holes destroy information is
   open; Penrose's conformal cyclic cosmology needs information loss at the end of each aeon to reset the entropy;
   Gell-Mann and Hartle's time-neutral formulation, with both an initial and a final condition, is the published
   place where a history with both ends fixed is written down, and a loop would set the two ends equal). We have not
   searched for that calculation, so no "we have not found" sentence is written about it (rule 15).
5. **A test the toy can run, not run.** Two turns of the circuit of section 4 in one run, with the records erased
   at the boundary (the swap to a sink, or the inverse interaction) against two turns with the records kept: whether
   the second turn's branch weights, sum rules and compatible sets are those of a fresh start or are conditioned on
   the first turn's records. Exact and cheap, and the only place the toy touches the loop. Not registered; the
   owner decides whether it is.
6. **What is not here.** No calculation of a cyclic universe in the decoherent-histories formalism; Stage E's
   cosmology is one expanding universe, not a cycle; nothing on gravity, the burp or which settings give observers.
   The toy has no loop, no black hole and no turn boundary; item 5 would give it a boundary by hand.

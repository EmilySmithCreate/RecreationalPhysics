# Handoff, 19 October 2026: how the process and the toy could improve from here

**Status: ours, for the owner.** Written at the end of 18 to 19 October (VISION Updates 62 to 69; T71 launched), as a
list of changes worth considering tomorrow. Nothing here is decided; each item says what it would cost and what it would
buy, and which ones need her word (a rule change or a new knob needs her dated decision, CLAUDE.md rule 9 and VISION S1).
The state of the work is `docs/HANDOFF.md`; this page is only about how to work better.

## 1. Process

### 1.1 The test suite before every commit

**What happens now.** Rule 6 says the suite passes before every commit, and today that was 1,131 tests in 7 to 10
minutes, run eight times for commits of which six changed only text (the notebook, the brief, VISION, the handoff). The
suite also runs on every push in CI (`.github/workflows/tests.yml`), so the local run before a text-only commit is a
second copy of a check that will happen anyway. Cost today: about an hour of wall time, during which nothing else was
done. The slowest tests are listed in section 1.1a below.

**Proposal (a rule change, hers).** Keep "the suite passes before every commit" for commits that touch `src/`, `scripts/`,
`tests/`, `configs/` or `results/`. For commits that touch only `.md`, `.html`, `.bib`, `.txt` and `.json` under `docs/`,
`sandbox/` and `cloud/`, run no tests locally and let CI run them on the push; if CI fails, the next commit fixes it. A
one-line check (`git diff --cached --name-only | grep -qvE '\.(md|html|bib|txt)$|^(docs|sandbox|cloud)/'`) decides which
lane a commit is in. What it costs: a text-only commit that breaks a test (a renamed file a test reads, say) is caught by
CI minutes later instead of before the commit; in this repository that has happened zero times that the record shows.
What it buys: most of an hour a day.

**A second, smaller change (ours to do, no rule change).** Mark the handful of slow tests (`@pytest.mark.slow`) and give the
quick lane `-m "not slow"`, so a code commit can run the fast nine tenths in about a minute and the slow ones in CI. The
slow tests are the kernels' long chains and the exact listings; they are the rule-6 checks and must keep running, but
not on every commit of a docstring.

### 1.1a The slowest tests, measured 19 October

Whole suite: 1,131 tests, 613 s run one after another on this container (the suite is not parallelised; the container
reports its core count in the hand-over line of today). The 25 slowest take about 365 s, three fifths of the time; the
other 1,106 take about 250 s. The ten slowest:

| Test | Seconds | What it checks |
|---|---|---|
| `test_first_exit_clocks::test_the_clocks_are_consistent` | 56 | three readers of the first exit agree (paper 1's clock) |
| `test_contraction::test_the_thermal_chain_over_widths_matches_the_exact_distribution` | 30 | the layer chain's Boltzmann weights (rule 6, the new kernel) |
| `test_first_exit_clocks::test_the_mean_first_exit_is_the_exact_count_where_waits_are_short` | 26 | the first exit against the exact count |
| `test_t61::test_the_runner_writes_the_same_file_twice_saves_graphs_and_refuses_to_overwrite` | 23 | same seed, saved graphs, no overwrite (rule 5) |
| `test_first_exit_clocks::test_the_saved_first_exits_of_t22_come_back_exactly` | 22 | a registered result reproduced |
| `test_general_chain::test_a_sheet_that_wraps_in_an_odd_number_of_steps_carries_free_pentagons` | 18 | the general kernel |
| `test_spark::test_hot_patch_is_reproducible_from_its_seed` | 18 | same seed (rule 6) |
| `test_first_exit_clocks::test_the_first_exit_is_the_same_attempt_in_all_three_readers` | 17 | the clock readers |
| `test_clean_move::test_clean_moves_out_of_the_slab_are_exact_and_leave_no_point_broken` | 17 | the clean two-switch move (rule 6) |
| `test_full_curvature::test_flat_sheet_stays_a_dip_when_braces_are_allowed` | 13 | the parked braces model |

Every one of them is a rule-6 check or a reproduction of a registered result, so none should be deleted. Two cheap
changes: mark these 25 `slow` and run them in CI and before code commits only; and run the suite in parallel
(`pytest-xdist`, `-n auto`), which on a four-core machine would cut the whole suite to about three minutes with no test
changed. Both are ours to do and change no rule; the two-lane rule above is hers.

### 1.2 One fact in one home, enforced

Rule 17 says a result is written once in full and linked elsewhere. Today each decision was written in five places (VISION,
the brief, the notebook, `docs/HANDOFF.md`, `TASKS.md`), and the programme page and its mirror had drifted apart for two
weeks: the artifact carried the state of 15 October, `docs/public/programme.html` the state of 5 October, and
`docs/papers/programme_draft.md` the state of 17 October. Re-synced today (artifact Version 92 is now built from the file in
the repository). Proposal: the artifact is only ever published from `docs/public/programme.html`, and `TASKS.md` stops
carrying per-hour lines (its 18 October item is a page long); the hand-over keeps the hourly record, the tracker keeps
the next action per item.

### 1.3 Predictions in a fixed form

Her T71 prediction used arm letters the reverse of the registration's, and was scored by the move sets she described.
Cheap fix: every registration that asks for her prediction ends with a short form to fill in, one line per arm or cell,
naming the thing (not a letter) and the words allowed. The "What the owner is asked" block written into T71 today is the
shape of it.

### 1.4 Sandbox looks earned their place

Three looks today changed what was asked next without a registered run: the knots' positions (the scraps' own layout is
not the seed spectrum), the shorteners of "when we are" (who counts is the lever, not interaction), and the kernel's own
check at L = 6 and 8 (which moved her T71 prediction before launch). Keep the habit: a look first, one line in the LOG,
a registered test only where a claim would rest on it.

### 1.5 Reading that is still owed before anything is cited

Adams and Laughlin 1997 (the infall history behind the daughters' birth times), Krauss and Scherrer 2007 (the observation
window, now a load-bearing term), [Freivogel11] in full (the youngness pressure), Loll's review (dynamical
triangulations, whose fixed-count practice was adopted). All are search summaries today. The proxy refuses arXiv; the PDFs
would have to come from her.

### 1.6 Compaction

This session's context was compacted once; the summary carried the decisions but not the exact wording of her messages, and
the notebook had to be the memory. That worked because the notebook is written as she speaks. Keep writing her words in
first, before anything of ours.

## 2. The toy

### 2.1 What T71 can and cannot decide

Both layer arms are close to arithmetic (the kernel's check already shows CYCLES with exactly a N_slab per daughter), so
the run's real content is: whether the clean switch move ever fires in the model arm; the period and the slab share under
her gate; and the size claim at L = 16. If all three come out as written, the layer form is a converter and nothing more,
and the next question is not another feed run.

### 2.2 The gate stands in for a wall; a wall would be better

Under the layer form the slab is not a dip: its split is downhill, and the gate is a rule that holds it shut. X "stable
for now" is then put in, not found. Two things could make it found. (a) A cost per point μ_N read off the fluctuations of
a free flat torus (E5 in the contraction brief, not done): if the toy's own statistics prefer a width, the slab may sit in a
dip without a gate. (b) An energy term under which width 4 is a local minimum against width 6, which is a new knob (S1)
and would need her decision; the price on loops of six (Update 56) runs the other way and is not it. The exact reach check
(E4, whether the layer moves plus the clean switch reach every state they should at the smallest sizes) is also not done
and is a rule-6 item for the layer form.

### 2.3 The daughter is a ledger, not a geometry

Under Update 66 the daughter is a number: energy that left. Her picture has the daughter as a space with its own scrap and
its own relic for the next turn (piece 12, "another is set at the end like our 14 pointer"). If a test ever needs the
daughter's own knots or its own width, the daughter has to be a second torus built from the release, which is a second
lattice in the runner and a decision about its size (points are not fundamental, she said, so the daughter need not be
smaller). Not needed for T71; needed before piece 7's "relic to relic" can be run.

### 2.4 What the toy supplies to the measure, and what it never will

Piece 12's function takes one term from the toy, b = (energy fed) / (a N_slab), and everything else from published
cosmology. Two cheap exact facts to add before paper 16 quotes b: how b depends on λ at fixed energy fed (it falls as
1/(λ − 1)), and that the lump per daughter scales with the slab's area, so a larger parent slab makes fewer, larger
daughters for the same feed. Both are arithmetic from Update 66 and need no run.

### 2.5 The curling-energy brief still waits on one answer

What carries curling energy (each relic, stores at the relic, or both). Until she answers, nothing registered runs with
it, and piece 11 has no registered test. The sandbox looks of 14 and 15 October are the only evidence either way.

### 2.6 Two-direction cycle as the cheap place to look

Her fold picture (a relic seeds a tube that a later activation opens again) closes in two directions, where paper 1's
machinery, the knots and the curl-only feed all exist. If the three-direction layer form keeps reading as pure arithmetic,
the two-direction cycle with a planted relic is the cheapest place to look for anything that is not already known.

### 2.7 Paper 1

Two sentences she proposed are drafted in `docs/papers/curled_torus/v2_changes.md` (the fixed count as the published
model's setting; breaking allowed and, under the published move, required). The paper is hers and held; the red-team pass
(rule 12) and the reader request wait on her.

## 3. Owed by her, as of this writing

Her word for T71's held-out size L = 16 after L = 8 and 12 are read; whether her T71 arm letters were meant as described;
what carries curling energy; T66's repair choice and her word for N = 1000; whether to adopt the test lane of 1.1 (a rule
change); the paper 1 sentences, to edit or adopt; who counts in piece 14, chosen on its own grounds.

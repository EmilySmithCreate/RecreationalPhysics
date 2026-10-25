# Brief for a fresh reader: the later record of 25 October 2026 (the twin daughters, the twin gate T82, growth, fronts)

*Written 25 October 2026 for a reviewer who starts with no history of this work (CLAUDE.md rules 12 and 22). The owner,
Emily Smith, will start the session and pass this page to you. You are meant to be a different model from the one that
wrote the record (Claude); Codex is the intended reader. This is the day's second brief; the first covered Updates 104
to 111 and its report is in the repository, but you are not to read it or anything from later commits.*

## Who you are and what you may do

You are a fresh, skeptical reader of a hobbyist physics research programme. You have not seen the conversations that
produced its record. **Work read-only:** do not edit, commit or push anything in the repository. You may run the
repository's scripts and tests (they write only to `sandbox/out/`, which is not tracked, or to your own scratch folder);
do not run anything that writes to `results/` (the T82 runner writes there: run it only with a scratch output folder,
`python scripts/run_layer_feed.py <config> <scratch dir>`, and only on a small copy of a config). Return your report as
your final message, in Markdown; the owner will save it as `docs/reviews/2026-10-25b_codex_report.md`, and the next
working session will record it as an ASSUMPTIONS entry (rule 12).

**Repository:** `https://github.com/EmilySmithCreate/RecreationalPhysics`, branch `claude/particle-sector-2026-10-24`,
**at commit `f0802dfa`** (full `f0802dfafd02394ce24680ab4541a6493d636dae`). Check out that commit and read nothing from later commits. An in-session audit of the same material (ASSUMPTIONS
O157, VISION Update 121) is already in that commit, with its corrections marked "O157" in place: do not read O157 or
Update 121 before your own findings are written, so that your read is independent. The corrected text is the state
to judge.

**Setup:** Python 3.10+, `pip install -e ".[dev]"`. `pytest tests/test_layer_feed.py` takes under a minute; the full suite
takes about half an hour and you do not need it. The T82 stage-1 results may not exist at that commit; you are judging the
design, the code and the predictions, not results.

**Read first:** `CLAUDE.md` (the rules; especially 1, 4 to 7, 10 to 16 and 19 to 22) and the top of `VISION.md` (the
hypothesis, claims 1 to 6, and the bar).

## The question

Later on 25 October the owner answered read-back questions and added ideas: the sign that alternates between generations
is matter against antimatter, set by the black hole's spin; "net flat" is a total over one joined surface; space grows by
whole rows, chosen as a one-way clock; each Big Bang makes two daughters, one with the matter surplus and one with the
antimatter surplus, each carrying the full curling cost, released together once the parent's stores hold twice that
cost ("one gate, double the bill"). The assistant recorded these (VISION Updates 113 to 120 and Update 117's in-place
corrections), ran three sandbox looks, built the twin gate into the toy's code, and registered a test of it (T82) with
the owner's predictions.

**Your job: find what is wrong.** Assume there are errors in the code, the physics, the arithmetic, the attribution of
ideas, the labelling of statements, the registration and the process, and look for them. A clean bill is a possible
answer, but it should be earned.

## What to read

1. `VISION.md`, **Updates 113 to 120** (Update 121 after them is the in-session audit's list; skip it), and the
   in-place corrections marked
   "Codex audit, O156".
2. `sandbox/NOTEBOOK.md`, entries dated 2026-10-25 from "Does handed behave like electric" on: her words, verbatim.
3. `docs/design/owner_questions_2026-10-24.md`, the sections at its end (read-backs RB1 to RB5, their answers, G1).
4. `docs/design/predictions_sheet_2026-10-25.md`, section 7; `PREREGISTRATION.md`, section **T82**; the configs
   `configs/t82_*.json` and `cloud/queue/2026-10-25_t82_stage1.txt`; `scripts/analyse_t82.py`.
5. The code: `src/graphity/layer_feed.py` (release_to "twins"), `scripts/run_layer_feed.py`, the last two tests in
   `tests/test_layer_feed.py`; for comparison, T71 (`PREREGISTRATION.md` section T71, `scripts/analyse_t71.py`, ASSUMPTIONS
   O144).
6. The sandbox looks and their lines in `sandbox/LOG.md`: `sandbox/local_pair_insertion_look.py`,
   `sandbox/soft_front_look.py` (run with `PYTHONPATH=src`), `sandbox/switch_influence_cone.py` (about an hour; inspect it
   and run a shortened copy if you like).

## What to check

Write each finding with where it is, what is wrong, what is right, how you know (a computation you ran, a source, an
argument), and how sure you are. Cover at least:

1. **The twin-gate code.** Is energy conserved exactly with both twins counted? Is the second twin paid from the right
   pool, and can the pool go negative or be double-counted? Does the gate behave as the registration says (a downhill
   move fires only when the pool holds 2 a N_slab)? What happens to a downhill contraction, and in the arm with the clean
   two-switch move? Do the new tests test what they claim, and what do they miss?
2. **T82 as a pre-registration.** Are the words and the predictions P1 to P5 well posed and scorable as written? Does
   `analyse_t82.py` implement them, including the births count, the period, the comparison with T71, and the clean-move
   count? Was anything chosen after a peek (a two-replica scratch check is disclosed; is the disclosure enough)? Is a held-out
   size handled as rule 14 requires? Is anything true by construction presented as a test?
3. **Her words against our readings.** Any reading of the assistant's presented as her decision, any decision recorded
   that she did not make, any of her words misquoted or dropped, any assistant conclusion listed among her answers.
4. **The sandbox looks.** Is the local pair insertion enumeration complete for what it claims ("every one-pair insertion
   with minimal rewiring" near one point)? Are the soft-front numbers and their reading right (no sharp front from the
   built field; a wall of fixed width and tension with a double well)? Does the switch-influence reading (JUMPS) follow?
5. **Physics from memory.** CP against CPT and what an anti-universe obeying our laws would need; Boyle, Finn and Turok's
   universe and anti-universe pair; the weak force's range; the phi^4 kink's width and tension; double layers and
   Coleman's thin-wall barrier; Lieb–Robinson bounds, causal sets and Wolfram's causal graphs; timescape's walls and voids.
   Is each stated correctly and marked "general knowledge, to verify" where it was not read?
6. **Internal consistency.** Contradictions between Updates 113 to 120, the questions file and the notebook, and with
   earlier corrections still standing (for example: the backed-up "light" is the Wilson-line scalar; points come in
   pairs; the hard zero-total rule fixes the total, not where the uncurl sits). Is the energy book of the twin birth
   (two curling costs per Big Bang) consistent with claim 6 and with how the toy pays it?

## What to return

A single Markdown report, in plain American English (the owner is a software engineer, not a physicist; define terms):

1. **Summary** (ten lines at most): the most important things to fix, in order.
2. **Findings**, numbered, under the six headings above, each with where, what, what is right, how you know, and how sure
   you are.
3. **What you ran:** each script or test, with its output where it disagrees with the record.
4. **Missing published work:** the published models, theorems or measurements most relevant to the day's ideas (twin or
   paired universes, universe and anti-universe pairs, growth of space by insertion, domain walls) that the record does
   not cite, with authors and years, "to verify" where unsure. Her stated aim is to apply existing mathematics to her
   ideas, so a good match is welcome news.

Do not write "nobody has done X"; write "I did not find X" and say where you looked. Mark anything you did not check at
its source as such.

## What not to do

Do not propose new mechanisms for her hypothesis and do not rewrite her ideas; judge what was recorded, computed,
coded, registered and answered. Do not read commits after the one named above. Do not change any file.

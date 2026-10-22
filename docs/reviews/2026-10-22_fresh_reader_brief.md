# Brief for a fresh reader: the record of 21 October 2026, and the audit of it

*Written 22 October 2026 for a reviewer who starts with no history of this work (CLAUDE.md rules 12 and 22). The owner,
Emily Smith, will start the session and pass this page to you. If you are a different model from the one that wrote the
record (Claude), so much the better.*

## Who you are and what you may do

You are a fresh, skeptical reader of a hobbyist physics research programme. You have not seen the conversations that
produced its record. **Work read-only:** do not edit, commit or push anything in the repository. Return your report as
your final message, in Markdown; the owner will save it as `docs/reviews/2026-10-22_fresh_reader_report.md` and the
next working session will record it as an ASSUMPTIONS entry (rule 12).

**Repository:** `https://github.com/EmilySmithCreate/RecreationalPhysics`, branch `claude/consistency-fixes-2026-10-19`,
at or after commit `a7d835ac`.

**Read first:** `CLAUDE.md` (the rules; especially 1, 7, 10, 12, 13, 15 and 19 to 22) and the top of `VISION.md` (the
hypothesis, claims 1 to 6, and the bar). You do not need the rest of the history.

## The question

On 21 October 2026 the owner streamed many new ideas (a particle as a twisted ring of diagonal links, matter and
antimatter, dark matter as loops on a cube's faces, a speed limit, dark energy settling to a constant, a daughter
universe bigger than its black hole). The assistant recorded each, answered from memory with "what it must face", ran
three small exact checks, and built a first piece of code. On 22 October an automated audit of that day was run, but its
adversarial checking step did not complete, so its conclusions are the assistant's own judging, unchecked.

**Your job is to check both, in this order, so that the audit's conclusions do not shape your first reading.**

### Part 1: read the day yourself, before the audit

Read, and only these, first:

- `VISION.md`, **Updates 78 to 91 only** (stop before Update 92).
- `sandbox/NOTEBOOK.md`, the entries dated 2026-10-21 and the first entry dated 2026-10-22 (the owner's words verbatim,
  with the assistant's notes marked "Ours").
- `sandbox/LOG.md`, the entries dated 2026-10-21, and the two scripts they cite (`sandbox/curl_uncurl_mirror.py`,
  `sandbox/diagonal_rings.py`; each runs in seconds and you may run them).
- `src/graphity/regge.py` and `tests/test_regge.py`.
- `docs/reading/notes/2026-10-21_matter_as_loops.md`.

Then write down, before reading anything else:

1. **Physics errors.** Every statement marked "ours" (especially "general knowledge, to verify") that is wrong, overstated,
   or misattributed, with what is right and the source that would settle it.
2. **Promotions.** Any statement given a stronger kind than it has earned (rule 10: exact, measured, interpretation, the
   owner's claim), or a first look described as a finding (rule 7).
3. **Her ideas mishandled.** Any idea of hers that was misread, dropped between the notebook and VISION, answered from
   memory where a reading or an exact check was due, or treated as a claim rather than a hypothesis to test.
4. **Missing published work.** The published models, theorems or measurements most relevant to her ideas that the record
   does not cite. Name authors and years; say "to verify" where you are unsure. Her stated aim is to find existing
   mathematics that describes her concept in whole or in part, so a good match is welcome news, not a criticism.
5. **The code.** Whether `regge.py` and its tests do what they claim, and whether any test cannot fail.

### Part 2: then read the audit, and check it

Now read:

- `VISION.md` **Update 92** (the corrections), and Update 93 (new rules).
- `docs/HANDOFF_2026-10-22.md`, **section 2** (what was missed; twenty research tasks; debts of attribution; her dropped
  ideas; answers to her four questions) and **section 3** (next steps).
- `docs/design/regge_stage_b_brief.md`, the "current definitions" box and the corrected exact item 2.

For each correction in Update 92 and each of the twenty research tasks, say: **right, wrong, or overstated**, and why, in
one or two sentences. Pay most attention to these, which carry the most weight if wrong:

- that the toy's "curl" (a link on a third square) is not curvature, so curls and uncurls need not balance;
- that a three-direction lattice with an energy charging only for curving (Regge calculus) has no gravitational waves
  and no pull, as in three-dimensional gravity;
- that one diagonal per square, chosen by the kind of point, cuts each cube into five tetrahedra with six lengths per
  point and no body diagonal;
- that the twist of a framed ring is not conserved and the linking number is (Lk = Tw + Wr);
- that the "one kind's diagonals are matter's" rule cannot carry a matter excess;
- that "negative curvature" was wrongly used as a synonym for dark energy;
- the answer given to her question on converting a black hole's feeding rate into the toy's sweeps (section 2.5, item 2).

Then say what Parts 1 and 2 disagree on: what you found that the audit missed, and what the audit found that you think is
wrong.

## What to return

A single Markdown report, in plain American English (the owner is a software engineer, not a physicist; define terms),
with these sections:

1. **Summary** (ten lines at most): the most important things to fix, in order.
2. **Part 1 findings**, numbered, each with: where (update number or file and line), what is wrong, what is right, the
   source, and how sure you are.
3. **Part 2 verdicts** on each Update 92 correction and each research task: right, wrong or overstated, with the reason.
4. **What the audit missed** and **what the audit got wrong**.
5. **The three published models** you think matter most for her concept right now, with why.

Do not write "nobody has done X"; write "I did not find X", and say where you looked (rule 15). Mark anything you did not
check at its source as such.

## What not to do

Do not propose new mechanisms of your own for her hypothesis, and do not rewrite her ideas; judge what was recorded and
what was answered. Do not change any file.

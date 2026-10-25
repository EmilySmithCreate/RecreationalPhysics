# Brief for a fresh reader: the record of 25 October 2026 (cosmology from the merger split to the fractal loop)

*Written 25 October 2026 for a reviewer who starts with no history of this work (CLAUDE.md rules 12 and 22). The owner,
Emily Smith, will start the session and pass this page to you. You are meant to be a different model from the one that
wrote the record (Claude); Codex is the intended reader.*

## Who you are and what you may do

You are a fresh, skeptical reader of a hobbyist physics research programme. You have not seen the conversations that
produced its record. **Work read-only:** do not edit, commit or push anything in the repository. You may run the
repository's scripts and tests (they write only to `sandbox/out/`, which is not tracked, or to your own scratch folder);
do not run anything that writes to `results/`. Return your report as your final message, in Markdown; the owner will
save it as `docs/reviews/2026-10-25_codex_report.md`, and the next working session will record it as an ASSUMPTIONS
entry (rule 12).

**Repository:** `https://github.com/EmilySmithCreate/RecreationalPhysics`, branch `claude/particle-sector-2026-10-24`,
**at commit `247da44e`**. Check out that commit and read nothing from later commits: a separate in-session audit of the
same day landed after it, and you are meant to be blind to it.

**Setup:** Python 3.10+, `pip install -e ".[dev]"`. The four sandbox scripts below run in seconds to a few minutes; the
full test suite takes about half an hour and you do not need it. Two of the scripts read saved graphs under `results/`
(read-only): `results/t51_*_adj/*.npz` and the small-graph enumeration, which the script recomputes.

**Read first:** `CLAUDE.md` (the rules; especially 1, 7, 10, 12 to 16 and 19 to 22) and the top of `VISION.md` (the
hypothesis, claims 1 to 6, and the bar). You do not need the rest of the history.

## The question

On 25 October 2026 the owner streamed a run of ideas: that a black-hole merger's "burp" splits matter from antimatter
between a parent and a daughter universe, net zero over the pair; that the two universes' curvatures balance because a
total must stay zero; a rule for the toy that keeps curl minus uncurl at zero; that empty space grows at no cost at a
front moving at light's speed; a picture of charge, spin and handedness from twists of 120° and 60°; light backed up in
a charged shell at the opening front; and the strange loop as a fractal. The assistant checked each against known
physics and the toy, ran four exact or sandbox "looks", had a reading done on timescape cosmology, and recorded eight
VISION updates (104 to 111) and a rewritten questions file with two rounds of her `#` comments.

**Your job: find what is wrong.** Assume there are errors in the physics, the arithmetic, the attribution of ideas, the
labelling of statements, and the process, and look for them. A clean bill is a possible answer, but it should be earned.

## What to read

In this order:

1. `VISION.md`, **Updates 104 to 111** (at the end of the file, as of commit `247da44e`).
2. `sandbox/NOTEBOOK.md`, entries dated 2026-10-25: the owner's words, which should be verbatim.
3. `docs/design/owner_questions_2026-10-24.md` (rewritten that day around her answers).
4. The sandbox scripts and their log lines in `sandbox/LOG.md`: `sandbox/cube_sixty_degree_look.py`,
   `sandbox/opened_space_curvature_sign.py`, `sandbox/zero_total_rule_reach_n18.py`, `sandbox/front_push_step.py`. Run
   each.
5. `docs/reading/notes/2026-10-25_timescape_reading.md`, the earlier `docs/reading/notes/2026-10-20_backreaction_timescape.md`,
   `docs/reading/notes/2026-10-19_causal_entropic_principle.md` (cited for "why now"), and the `REFERENCES.bib` entries
   added that day.

## What to check

Write each finding with where it is, what is wrong, what is right, how you know (a computation you ran, a source, an
argument), and how sure you are. Cover at least:

1. **The zero-total rule.** Is "curl minus uncurl summed over links = 4(S − N)" right for the four-link toy (and S = 3N
   for six links)? Is the claim that under the rule the published model's square term becomes a constant right, and is
   the comparison with Gauss–Bonnet (two-dimensional gravity has no dynamics) fair? Is the N = 18 reachability check
   (`zero_total_rule_reach_n18.py`) sound, including whether class-level connectivity is enough?
2. **The combinatorial Gauss–Bonnet argument** (Update 104): that a bipartite four-link graph drawn on a surface has no
   positively curved point, so on a torus every point is flat. Are its assumptions stated?
3. **The cube looks** (`cube_sixty_degree_look.py`): the 12 squares at a point, and the claims about 60°, 120° and 180°
   turns about a body diagonal, with and without a mirror, and which keep or swap the two kinds of point. Do the claims
   depend on the centre of the turn, and does the record match the owner's picture?
4. **The push on the front** (`front_push_step.py`): the reflection and transmission fractions, the momentum bookkeeping,
   the closed form, the sign, and whether the conclusion drawn in Updates 110 and 111 follows from a continuum stand-in.
5. **The curvature-sign look** (`opened_space_curvature_sign.py`): do its numbers hold, and what does the record say it
   shows? Is anything stated about cooling rates that is really a size effect?
6. **Physics from memory.** Check, at least: Birkhoff's theorem and what LIGO can see of a burp inside a horizon; the
   inspiral–merger–ringdown consistency test and echo searches; ALPHA-g; Wald and Blandford–Znajek; Vilenkin's neutrino
   asymmetry from rotating holes and leptogenesis; Boyle–Finn–Turok; Cohen–De Rújula–Glashow; pair creation and
   two-photon annihilation; the Δ⁻ (three down quarks); the Delta-to-proton-plus-photon decay and the 21 cm line; muon and
   tau charges; the Hubble arithmetic (H0 times Planck's time; H0 times the age) and the coasting (R = ct) cosmology;
   Bödeker and Moore (2009, 2017); Cohen, Kaplan and Nelson; Hofstadter's video-feedback image. Is each stated
   correctly, and marked "general knowledge, to verify" where it was not read?
7. **Light under the hard rule** (Update 108): that at leading order light neither lowers nor raises the curling cost
   because every allowed arrangement has the same number of squares. Is that right, and over what range of the field's
   stiffness β?
8. **Her words against our readings.** Using the notebook and the questions file, find any place where a reading of the
   assistant's is presented as her decision, a decision is recorded that she did not make, her words are misquoted or
   dropped, a question of hers is recorded as a prediction, or an assistant conclusion is listed among her answers (rules
   10, 20, 21).
9. **Kinds of statement.** Any interpretation labelled exact; any sandbox look used to support a claim (rule 16); any
   "published form" claimed for her idea where the published work does something different; any general-knowledge
   statement unmarked (rule 19).
10. **Internal consistency.** Contradictions between Updates 104 to 111, the questions file (its H-lines and answered
    lists) and the notebook; and whether her ideas of the day are consistent with each other (for example, sorting by
    electric charge against the observed neutrality of our universe; "net flat" against the signs she gave).

## What to return

A single Markdown report, in plain American English (the owner is a software engineer, not a physicist; define terms),
with these sections:

1. **Summary** (ten lines at most): the most important things to fix, in order.
2. **Findings**, numbered, under the ten headings above, each with where, what, what is right, how you know, and how
   sure you are.
3. **What you ran:** each script, with its output where it disagrees with the record.
4. **Missing published work:** the published models, theorems or measurements most relevant to the day's ideas that the
   record does not cite, with authors and years, "to verify" where unsure. Her stated aim is to apply existing
   mathematics to her ideas, so a good match is welcome news.

Do not write "nobody has done X"; write "I did not find X" and say where you looked. Mark anything you did not check at
its source as such.

## What not to do

Do not propose new mechanisms for her hypothesis and do not rewrite her ideas; judge what was recorded, computed and
answered. Do not read commits after `247da44e`. Do not change any file.

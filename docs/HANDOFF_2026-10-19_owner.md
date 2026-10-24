# Hand-over for Emily: what happened on 19 October, what it means, what is yours to do

Written for you at the end of 19 October 2026. Plain language; every term defined where it first appears; each item
says which kind of statement it is (exact, measured, ours, yours). The record's own homes are linked; this page says
nothing that is not there.

*Corrected 19 October evening after a consistency audit (docs/reviews/consistency_audit_2026-10-19.md).*

## 1. The day in one paragraph

You spoke with Carlo Trugenberger by video. What was said on the call is private correspondence: it is in the
outreach folder (`docs/outreach/`, gitignored, so it lives only on your laptop and never in the repository), and this
page does not repeat it. After the call you worked out, in conversation, three positions that are now decisions in the
record: the loop's coupling is fixed by the loop's total energy once every daughter's energy has come home at the end
of a turn (Update 70; no value of it has been computed); dark energy is the network's own thermal defect density at
that coupling, a hypothesis to test (the thermal defect density is how many defects, departures from a perfect
lattice, any network carries per unit of volume at a coupling above zero, because defected arrangements vastly
outnumber the one perfect one); and the measure that says where an observer should expect to find itself counts once per civilization,
weights the ages by the causal diamond, and defines an observer as, in your words, "a civilization where at least one
intelligent being asks this particular question". Two calculations in standard cosmology then ran under rules written
first. Their result, in one sentence: the way you count observers decides the answer more than the stars do, and under
your measure the one class that keeps our age typical at every input is the one built around our own case,
which by the project's rules is an assumption holding together and not a finding.

## 2. Where everything is

| What | Where | Kind |
|---|---|---|
| The call's notes; the follow-up email draft; the meeting plan; the slide briefing | `docs/outreach/` (gitignored: on your laptop only, never committed, absent from every branch and worktree) | private; ours |
| The deck prepared for the call | https://claude.ai/artifact/YC5suhVcYUKiFp4DVs3eye (private) | ours |
| Your decisions | `VISION.md` Updates 70 and 71 | yours |
| Your words of the day | `sandbox/NOTEBOOK.md`, 19 October | yours |
| The glossary's levels and six new terms | `docs/papers/glossary.md` | ours, at your request |
| The two calculations, their rules and readings | `PREREGISTRATION.md` T72, T73; `ASSUMPTIONS.md` O138, O139 | measured (computed); one exact statement |
| The code and its tests | `scripts/observer_window.py`, `scripts/read_t72.py`, `tests/test_observer_window.py`, `configs/t72_*.json`, `configs/t73_diamond.json`, `results/t72_*.csv`, `results/t73_diamond.csv` | |
| The reading behind it | `docs/reading/notes/2026-10-19_causal_entropic_principle.md`, `2026-10-19_observer_window_endpoints.md`, `2026-10-19_t72_inputs.md` | published, read by a fresh agent, quotations to check against PDFs |
| Paper 16, drafted | `docs/papers/loop_measure/paper.tex` (no PDF: no LaTeX on this machine) | ours, for your read |
| Paper 12, one paragraph added | `docs/papers/black_hole/paper.tex`, end of the 16 October section | ours |
| The programme page | https://claude.ai/artifact/JLtR2aqHmL2FghWmNZU8xW, published from `docs/public/programme.html`; the text source `docs/papers/programme_draft.md`, whose claim text was brought into line with the page's on 19 October evening | ours, your claim at the top |
| The branch | `claude/carlo-call-2026-10-19`, off `main`; merged into `main` as pull requests #58 and #59 on 19 October | |

## 3. What the two calculations say, in plain words

**The question.** By a universe's own age, counting from its birth, when is an observer like us most likely to exist?
Our age is 13.8 billion years. The answer is given as the share of such observers who come before our age: near a half
means typical; under five per cent means we are early; over ninety-five means we are late.

**What goes in.** How many stars form at each age (a published curve, peaking 3.5 billion years in); how many of them
have planets like ours (cancels out within a class); how long each star lives (10 billion years for one like the sun,
10 trillion for the smallest red stars); how long a planet needs before a civilization appears (4.5 billion years on
Earth, or Carter's "hard steps" version, in which a mind appears late in its planet's life because the steps are each
unlikely); which stars count (your class: sun-like, because sight needs a sun-like star); and the weight on ages.

**The first calculation (T72).** First, how it came to be read: its registered reproduction check passed on the share
(0.17 per cent of observers before now, inside the registered factor of two of the 2016 paper's 0.1 per cent) and
failed by the letter on the peak (4.4 trillion years, just below the registered window of 5 to 20 trillion). The
registration said the classes are not read on a failed check; you took it as passed on the share and the paper's loose
wording, and the classes were read on that decision (PREREGISTRATION T72; O138). Under your rule, each civilization
counted once at its birth, every class of stars came out typical: 81 to 86 per cent of observers before us in classes
A, B and C (sun-like; K and G stars; all stars), and 24 per cent in your class D. The exact reason: counting once at a
fixed delay makes the answer the star-formation curve shifted by the delay, whatever the stars, so sun-like stars and
all stars give the same curve to the last digit. The published "we are early by a thousandfold" (Loeb and others, 2016)
comes from weighting each planet by how long it lives: counting planet-years, which gives a planet round a red dwarf a
thousand times the weight of one round the sun because it lives a thousand times longer. The observer-moment variant,
which counts each civilization at every age while its planet's window is open, brings the same "early" back for all
stars (0.09 per cent before us; reported, not scored). The one input that changed the peak was Carter's hard steps:
under it a typical observer is at 17 billion years, with a quarter before us. Your prediction was "agree" with ours,
so it is scored with ours: class A typical held (its share came out higher than we said); class B typical held, but
its peak came out earlier than A's, not later, and its share too high; class C early failed; class D held in every
part.

**The second calculation (T73).** The causal diamond is the region an observer at a given age can be causally tied
to: bounded by the light cone of the beginning and the light cone of the end, it grows from nothing, peaks at 4
billion years, and is already half its peak at our age. Under the diamond weight, class B goes late (98 per cent of
observers before us), classes A and C go late or typical depending on the inputs (96 per cent at the registered
inputs; inconclusive by the registered rule for spread across inputs), the planet-years check class goes from early to
typical (80 per cent), and only your composite class D, sun-like stars with hard steps, stays typical, with our age
near its median (53 per cent before us). The comparison verdict is MOVES (O139). Your prediction that the diamond would
move the peaks held, and so did your prediction that the shares before now would rise; your prediction that no verdict
would change failed, and so did ours that A, B and C would stay typical. Also measured: the diamond is not the same
as the hundred-billion-year observation cap, which changed nothing in your class D because it bites where D's planets
are already gone (on the planet-years check alone the cap does move the share, from 0.17 to 8 per cent).

**Why this is not "closer than the real scientists".** Your class was built from our case: we orbit a sun-like star
and the hard-steps delay is calibrated on Earth. Thirteen combinations of class and counting rule were computed (the
four classes and the planet-years check, each with and without the diamond weight, and three classes under the
observer-moment variant), and one of thirteen landing near the median is about what chance gives (ours). And the
measure's last two definitions were chosen by you after the numbers were known, for reasons of principle that are
recorded as such. Rule 13 therefore says: our own age is not scored under the
measure from here. Loeb's own paper already finds sun-like stars put the peak at the present, so your class agrees with
the published work rather than beating it. What is new is structural: the counting unit decides more than the stars,
and we can now say exactly how.

## 4. Your decisions today, as recorded

- **Update 70.** At the end of a turn every daughter's energy has returned to the network, and the network's
  temperature is fixed by the loop's total energy alone ("YES"). Dark energy as the network's thermal defect density at
  that coupling, adopted as a hypothesis to test ("yes proceed"). Your "selected fast case" agreement recorded. The
  divergence with the published model on the Big Bang in your words.
- **Update 71.** Once per civilization; the causal diamond as the weight; an observer is "a civilization where at
  least one intelligent being asks this particular question". Disclosed: the numbers were known when you chose.
- **Smaller:** the T72 gate taken as passed on the share and the paper's wording; T73 drafted on your "yes draft it";
  paper 1 waits (no corrected copy to Carlo until it carries the six-around result); the glossary gains the levels of
  description and six terms (the network, a daughter, a black hole in the picture, a storage pool, a turn, the
  observer window).

## 5. What is yours to do next, in order

1. **Done: the pull requests for `claude/carlo-call-2026-10-19` are merged** (#58, #59). That merge is your
   acceptance of Updates 70 and 71 as worded. Glance at the Actions tab: the suite passed locally (1,141 tests collected; 1,140 pass and one
   is an expected failure). That one, in `tests/test_observer_window.py`, asserts that T72's check peak lies inside
   the registered window of 5 to 20 trillion years; it does not (4.4 trillion), so the test is marked to fail, and
   it stays as the visible record of the check's miss by the letter even though you took the check as passed.
2. **Send Carlo the follow-up email** (`docs/outreach/followup_draft_2026-10-19_carlo.md`, in the gitignored outreach
   folder on your laptop only): the prior-work question, the three D = 3 facts, the Bell request, and the draft's
   acknowledgment sentence.
3. **Name the measure's first real test:** a quantity it predicts that was not put in. Candidates in Update 71: the
   share of observers who find dark energy already dominant in their universe; the distribution of a universe's age
   over its dark-energy timescale among observers; the daughters born per unit of energy fed (the toy's one term).
4. **The two-system kernel.** A design brief (`docs/design/two_system_brief.md`, not written) for a network at a fixed
   cold coupling with a daughter at its own temperature, with the exact statement of what the network's thermal defect
   density is at a coupling g in the toy, read from the equilibrium curves already measured. Nothing runs with it
   before your answers to the brief's questions.
5. **Read paper 16's draft** and say whether its caveat section says what you want said.
6. **Owed from before today (the main items; the full list is in `TASKS.md`):** T66's repair choice and its N = 1000
   prediction; the curling-energy brief's one remaining question (what carries curling energy); confirmation of the
   programme page's claim wording of 17 and 19 October; your word for T71's held-out size once its two smaller sizes
   are read; and the open items of VISION Update 44 that `TASKS.md` still lists: whether piece 10 stays attached to the
   toy, dark energy as a release or as energy kept (Update 70's candidate source bears on it), when paper 1 is
   revised, and the reference for the Fife paper.

## 6. Corrections made today that you should know

The session that prepared the call worked from a copy of the repository ten days behind the record, and several things
it told you in the morning were superseded on `main`: the tube opens into a tube six around, not a sheet (O116); T54's
numbers are completed-patch energies, not barriers (O118); the direction tie was withdrawn on 16 October (Update 58);
"five fold tests" is seven registered tests (T21, T26, T27, T34, T42, T47 part B, T57; paper 12's table). The deck and the slide briefing were corrected the same evening; nothing wrong reached the
record.

## 7. Running, and what arrives on its own

T71 (the slab under the layer form, twelve cloud jobs) is still running on your gate and prediction. When it lands:
fetch, accept, commit unread, read with its analyzer, then the held-out size with your word first.

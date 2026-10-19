# Hand-over for Emily: what happened on 19 October, what it means, what is yours to do

Written for you at the end of 19 October 2026. Plain language; every term defined where it first appears; each item
says which kind of statement it is (exact, measured, ours, yours). The record's own homes are linked; this page says
nothing that is not there.

## 1. The day in one paragraph

You spoke with Carlo Trugenberger by video. He did not read the paper and will not; he asked for an acknowledgment "for
discussions"; he could not picture the curled torus because, in his words, a closed torus is not a thing (he is right:
every lattice torus is closed, and the object is the 4 × L lattice torus, a torus whose short period is four). After the
call you worked out, in conversation, three positions that are now decisions in the record: the loop's coupling is set
by the loop's total energy once every daughter's energy has come home at the end of a turn; dark energy is the
network's own thermal roughness at that coupling, a hypothesis to test; and the measure that says where an observer
should expect to find itself counts once per civilization, weights the ages by the causal diamond, and defines an
observer as a civilization in which at least one being asks this question. Two calculations in standard cosmology then
ran under rules written first. Their result, in one sentence: the way you count observers decides the answer more than
the stars do, and under your measure the one class that keeps our age typical is the one built around our own case,
which by the project's rules is an assumption holding together and not a finding.

## 2. Where everything is

| What | Where | Kind |
|---|---|---|
| The call, paraphrased; the follow-up email draft; the meeting plan; the slide briefing | `docs/outreach/` (private, never committed) | his words paraphrased; ours |
| The deck he saw the start of | https://claude.ai/artifact/YC5suhVcYUKiFp4DVs3eye (private) | ours |
| Your decisions | `VISION.md` Updates 70 and 71 | yours |
| Your words of the day | `sandbox/NOTEBOOK.md`, 19 October | yours |
| The glossary's levels and six new terms | `docs/papers/glossary.md` | ours, at your request |
| The two calculations, their rules and readings | `PREREGISTRATION.md` T72, T73; `ASSUMPTIONS.md` O138, O139 | measured (computed); one exact statement |
| The code and its tests | `scripts/observer_window.py`, `scripts/read_t72.py`, `tests/test_observer_window.py`, `configs/t72_*.json`, `configs/t73_diamond.json`, `results/t72_*.csv`, `results/t73_diamond.csv` | |
| The reading behind it | `docs/reading/notes/2026-10-19_causal_entropic_principle.md`, `2026-10-19_observer_window_endpoints.md`, `2026-10-19_t72_inputs.md` | published, read by a fresh agent, quotations to check against PDFs |
| Paper 16, drafted | `docs/papers/loop_measure/paper.tex` (no PDF: no LaTeX on this machine) | ours, for your read |
| Paper 12, one paragraph added | `docs/papers/black_hole/paper.tex`, end of the 16 October section | ours |
| The programme page | https://claude.ai/artifact/JLtR2aqHmL2FghWmNZU8xW, published from `docs/public/programme.html`; the text source `docs/papers/programme_draft.md` | ours, your claim at the top |
| The branch | `claude/carlo-call-2026-10-19`, off `main`; the pull request is yours to open and merge | |

## 3. What the two calculations say, in plain words

**The question.** By a universe's own age, counting from its birth, when is an observer like us most likely to exist?
Our age is 13.8 billion years. The answer is given as the share of such observers who come before our age: near a half
means typical; under five per cent means we are early; over ninety-five means we are late.

**What goes in.** How many stars form at each age (a published curve, peaking 3.5 billion years in); how many of them
have planets like ours (cancels out within a class); how long each star lives (10 billion years for one like the sun,
10 trillion for the smallest red stars); how long a planet needs before a civilization appears (4.5 billion years on
Earth, or Carter's "hard steps" version, in which a mind appears late in its planet's life because the steps are each
unlikely); which stars count (your class: sun-like, because sight needs a sun-like star); and the weight on ages.

**The first calculation (T72).** Under your rule, each civilization counted once at its birth, every class of stars
came out typical, with 81 to 86 per cent of observers before us. The exact reason: counting once at a fixed delay makes
the answer the star-formation curve shifted by the delay, whatever the stars, so sun-like stars and all stars give the
same curve to the last digit. The published "we are early by a thousandfold" (Loeb and others, 2016) comes entirely from
counting planet-years, which gives a planet round a red dwarf a thousand times the weight of one round the sun because
it lives a thousand times longer. The one input that changed the peak was Carter's hard steps: under it a typical
observer is at 17 billion years, with a quarter before us. Your prediction, "agree" with ours, held on three classes and
failed on the all-stars class, which we had both expected to read early.

**The second calculation (T73).** The causal diamond is the region an observer at a given age can be causally tied
to: bounded by the light cone of the beginning and the light cone of the end, it grows from nothing, peaks at 4
billion years, and is already half its peak at our age. Weighting by it, most observers in every class come before us,
except in your class, sun-like stars with hard steps, which lands with us at its median (0.53). Your prediction that
the diamond would move the peaks held; your prediction that no verdict would change failed, and so did ours. Also
measured: the diamond is not the same as the hundred-billion-year observation cap, which changed nothing because it
bites where nothing lives.

**Why this is not "closer than the real scientists".** Your class was built from our case: we orbit a sun-like star
and the hard-steps delay is calibrated on Earth. Twelve combinations of class and weight were looked at, and one landing
near the median is what chance gives. And the measure's last two definitions were chosen by you after the numbers were
known, for reasons of principle that are recorded as such. Rule 13 therefore says: our own age is not scored under the
measure from here. Loeb's own paper already finds sun-like stars put the peak at the present, so your class agrees with
the published work rather than beating it. What is new is structural: the counting unit decides more than the stars,
and we can now say exactly how.

## 4. Your decisions today, as recorded

- **Update 70.** At the end of a turn every daughter's energy has returned to the network, and the network's
  temperature is fixed by the loop's total energy alone ("YES"). Dark energy as the network's thermal defect density at
  that coupling, adopted as a hypothesis to test ("yes proceed"). Your "selected fast case" agreement recorded. The
  divergence with the published model on the Big Bang in your words.
- **Update 71.** Once per civilization; the causal diamond as the weight; an observer is a civilization in which at
  least one being asks this question. Disclosed: the numbers were known when you chose.
- **Smaller:** the T72 gate taken as passed on the share and the paper's wording; T73 drafted on your "yes draft it";
  paper 1 waits (no corrected copy to Carlo until it carries the six-around result); the glossary gains the levels.

## 5. What is yours to do next, in order

1. **Open and merge the pull request** for `claude/carlo-call-2026-10-19`. Merging is your acceptance of Updates 70
   and 71 as worded. Glance at the Actions tab: the suite passed locally (1,140 tests, one expected failure that
   records T72's gate miss on the peak).
2. **Send Carlo the follow-up email** (`docs/outreach/followup_draft_2026-10-19_carlo.md`): the prior-work question,
   the three D = 3 facts, the Bell request, the acknowledgment sentence "We thank Carlo Trugenberger for discussions".
3. **Name the measure's first real test:** a quantity it predicts that was not put in. Candidates in Update 71: the
   share of observers who find dark energy already dominant in their universe; the distribution of a universe's age
   over its dark-energy timescale among observers; the daughters born per unit of energy fed (the toy's one term).
4. **The two-system kernel.** A design brief (`docs/design/two_system_brief.md`, not written) for a network at a fixed
   cold coupling with a daughter at its own temperature, with the exact statement of what the network's roughness is at a
   coupling g in the toy, read from the equilibrium curves already measured. Nothing runs with it before your answers
   to the brief's questions.
5. **Read paper 16's draft** and say whether its caveat section says what you want said.
6. **Owed from before today:** T66's repair choice and its N = 1000 prediction; the curling-energy brief's first
   question (what carries curling energy); confirmation of the programme page's claim wording of 17 and 19 October;
   your word for T71's held-out size once its two smaller sizes are read.

## 6. Corrections made today that you should know

The session that prepared the call worked from a copy of the repository ten days behind the record, and several things
it told you in the morning were superseded on `main`: the tube opens into a tube six around, not a sheet (O116); T54's
numbers are completed-patch energies, not barriers (O118); the direction tie was withdrawn on 17 October (Update 58);
"five fold tests" is eight. The deck and the slide briefing were corrected the same evening; nothing wrong reached the
record.

## 7. Running, and what arrives on its own

T71 (the slab under the layer form, twelve cloud jobs) is still running on your gate and prediction. When it lands:
fetch, accept, commit unread, read with its analyzer, then the held-out size with your word first.

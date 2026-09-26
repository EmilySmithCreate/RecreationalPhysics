# Design brief: the next model, with loop and exchange rules

Written 2026-09-25, afternoon, at the author's decision (VISION Update 28): "We cannot just keep using Trugenberger's
models. We need to start using other models, get more deeply into loop and exchange rules." And her framing of what
came before: the four-, six- and eight-link runs at various λ are groundwork on the mechanics of folding and unfolding,
so that the new model is built in a way likely to succeed. This page says what the new model has to keep, what it has
to add, and offers candidate rules for her to choose among. Under S1 nothing is built until she chooses, and the
choice is dated on the VISION page. Physics here is *ours, unverified*; her positions are marked as hers.

## 1. What the groundwork fixed, and the new model must keep or beat

From the (D, λ) map (`docs/papers/series_plan.md`) and the verdicts on record:

- **A ladder of curled directions, additive, with an exact release per rung** (papers 1 and 3). The burp: one seed, one
  front, a fixed activation, an exact release. This is the part of the picture that worked at every size and every λ
  tried, and any new model must reproduce it or explain why it should not.
- **Walls that rise from rung to rung** (doubling exactly only with eight links at λ = 1.25), in four, six and eight links, so that nothing in this energy ties the
  directions together; they open one at a time (T30). The author's rule that the directions curl and open together is
  therefore an ingredient the new model must *add*: a term or a rule that couples the directions.
- **The counting drive appears only at full curling** (O55). If gravity is to come from counting (her curve-first
  gravity), the new model needs the counting weight to rise gradually with curling, not only at the end; or the drive
  must come from somewhere else.
- **The melt.** Energy given to flat space melts it in every protocol tried (paper 4). A model in which concentrated
  energy folds needs the fold to be the cheaper dynamical route, not only the cheaper energetic one.
- **Counting alone cannot beat Bell** (O29): versions of one fixed arrangement with positive weights are a hidden
  variable. Any quantum leg needs amplitudes that can cancel: a phase (rung 4 of T15; `amplitude_rule_brief.md`).
- **The closed loop of four is not a resonator inside the sheet** (O30); where anything resonates it is the curled
  column with its collar.

## 2. The author's words to build from

- Closed loops are where phases come from; a particle is an allowed vibration of a small closed loop (Update 17).
- Versions do not affect one another; they are not different in the first place (24 September). Counting was a probe.
- The three (or four) directions are intertwined and curl together (Updates 22, 25); time may be a singleton or tied.
- The strange loop: every burp the same; the rules constant from parent to child; the measure per turn (Updates 23, 26).
- Gravity is a mathematical result of interchangeable degrees of freedom unobserved from the large scale; cost and count
  are the two halves of one free energy (24 September).

## 3. Candidate rules, for her choice

Each is one ingredient added to the family we have, so that the groundwork carries over and the first exact tests are
cheap. Each has a first test that could kill it.

**A. An exchange phase on loops (the fermionic or anyonic sign).** Keep the graph energy; replace the counting weight of
an arrangement by a sum over its versions with a sign or phase attached to each renaming: +1 for even renamings, −1 for
odd (a fermionic rule), or a phase e^{iθ} per elementary swap around a loop (anyonic in two dimensions). Then versions
can cancel, which is the one thing counting lacked. *First test, exact:* on the saved leftovers (T10, T15 rung 0),
compute the signed sum over the automorphism group; for a symmetric arrangement it can vanish, which is a selection
rule (some arrangements are forbidden by exchange, as two fermions cannot share a state). *What would kill it:* nothing
vanishes anywhere, or the signed weight breaks positivity in a way that makes no probability. *Relatives (not read):*
the Pauli principle from antisymmetry; anyons in two dimensions.

**B. A coupling between directions (the intertwining).** Keep the ladder; add a term that makes the second fold cheaper
once the first has happened, beyond the lowering the walls already give: for example, a reward for a point whose open
directions are all open or all curled, penalizing the partial state 4 × 4 × L that the author's rule forbids. *First
test, exact:* the walls and windows recomputed with the term; the coupled model should turn T30's NEVER OPENS (for the tori; O64) into a
cascade at some λ. *What would kill it:* no coefficient gives a cascade without also melting flat space (its wall must
stay above the rungs').

**C. Loop amplitudes evolving by the loop's Laplacian (the wave rule of `amplitude_rule_brief.md`).** Hardy's fifth
axiom put in by hand: a continuous reversible transformation between the versions. *First test:* the interference
prediction drafted there (sin⁴ t across the loop of four against (1 − e^{−2t})²/4 under counting). Already proposed;
the author held it until rung 0b was answered, and rung 0b said the loop is not a resonator in the sheet, so the
object would have to be the cap (loop plus collar). *What would kill it:* no localized mode on the cap either.

**D. A different substrate: loops as the degrees of freedom.** Instead of points and links, take closed loops as the
elements (a loop gas), with an energy on how loops link and touch; curling and opening become the joining and splitting
of loops; the strange loop becomes literal. *First test, exact:* whether a loop gas has a flat phase at all (a state
that looks like space by the spot's criteria). This is the largest departure and the least constrained by the
groundwork; it is listed because it is closest to her words, and marked as the one we know least about.

## 4. What we recommend, and why it is her call

A is the cheapest and speaks to the two open legs at once (the quantum leg's need for cancellation, and the selection
of arrangements); its first test runs on files already saved. B speaks directly to piece 11 and can be pre-registered
against T30's verdict. C is already on the table and waiting. D is a new project. Under S1 the choice is hers; once she
chooses, the first exact test is a day's work and needs no compute.

## 5. What the reading of 25 September changes (ASSUMPTIONS O60 (b))

- **The "anyonic form" of rule A does not exist as stated.** Renamings form the symmetric group, whose only
  one-dimensional representations are the trivial one and the sign; any phase summed over one arrangement's renamings
  gives either the count or zero. Anyons need paths of exchanges (braids), a rule over histories (VISION Update 20), and
  our graphs are not planar, where the published classification allows only bosons and fermions on their well-connected
  parts.
- **What rule A forbids depends on a convention**: with the sign on points (O57) a few per cent of damaged sheets are
  forbidden; with the sign on pairs (Betre and Lewis) nothing is. The choice is the owner's under S1.
- **No exchange sign carries a force** (a flat connection); so rule A cannot help the gravity leg. The loop rules that
  give modes with no gap, which the gravity leg needs, are continuous fields: a phase on each square (option B of
  `gravity_brief.md` section 6, vector-like, so like relics repel) or a field on the points (option A there, scalar, so
  like relics attract). A field on the points is the recommended first rule for gravity; phases on squares stay the
  candidate for light and for the quantum leg.

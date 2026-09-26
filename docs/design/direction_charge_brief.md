# A charge per opening direction: design brief

Written 2026-09-26, 05:10 ET, after the owner's decision (VISION Update 34). Nothing here is built or run. Under S1 the
form below has to be chosen by the owner and dated in VISION before any code; every setting run is then published, and
the model with it is our family around combinatorial quantum gravity, never CQG itself.

## The owner's idea, in her words put in order

Each kind of matter and energy carries its own kind of charge, and a charge acts only on its own kind. Red (the first
direction to open; ordinary matter and energy) has ordinary electric charge. Blue (the second; dark matter) has a
blue charge that red cannot feel. Green (the third; dark energy) likewise. All three feel gravity, because all three came
from opened directions and the drive to curve is in all of them. This is why dark matter looks uncharged to us.

## What the model has today, and what it lacks

- **Kinds.** The model can already say which opening a point belongs to: the census of open directions per point
  (`graphity.dimension.local_dimension_d`) records when each point went from d to d + 1. A point's kind could be the
  rung at which its last direction opened, or the rung at which the region around it first opened. Neither label exists
  in code yet, and which one matches "red, blue, green" is a choice (below).
- **Charge and force.** The model has no charge and no force at a distance: flat space here has an energy gap, so
  nothing in the energy pulls two objects together from afar (ASSUMPTIONS O60, O61). Any charge has to come with a field
  that carries it.

## Three forms, for the owner to choose among

1. **A field per kind (recommended).** One field on the points for each kind, sourced only by points of that kind, plus
   the gravity field of `docs/design/gravity_brief.md` (option A), sourced by every kind. It is the most literal form of
   her picture: like kinds interact through their own field, unlike kinds only through gravity. It reuses the gravity
   rule, which is still waiting on her decision, so the two decisions go together.
2. **A label with a contact term.** A constant that lowers or raises the energy when two neighboring points share a kind.
   Cheap to build, testable at once, but it acts only at contact, like the tie, and gives no charge at a distance.
3. **Kaluza–Klein charge.** In the published idea, motion round a curled direction looks like electric charge in the
   large ones. It ties charge to a direction, as she wants, but the charge exists only while that direction is still
   curled; once all three are open there is nothing left to wind round. It fits a state with a curled remainder, which
   hers does not have after the burp. Recorded because it is the nearest published relative, not recommended.

## What would count as a test

- **By construction, not a result:** with form 1, unlike kinds exert no force except through gravity. That is put in.
- **Results the model could return:** (a) the shares of the three kinds after a burp, read from the labels, set beside
  the owner's ledger (piece 6 of the regrouped programme); (b) whether a cloud of one kind can shed energy and clump:
  a kind that can radiate through its own field can cool into disks, which observations limit for dark matter; (c)
  whether the kinds stay separate or mix as the space settles.
- **What would count against her picture:** labels that are not stable (points changing kind as the space settles);
  or a dark kind that cools and clumps as readily as ordinary matter, which observed halos rule out.

## What observations already say (general knowledge and search summaries, not read: this session's network blocked arXiv; see `docs/reading/notes/2026-09-26_dark_charge.md`)

Dark photons (a hidden charge with its own light) and mirror matter (a full hidden copy of our forces) are published
ideas. Both are limited: a strong dark charge with its own light would let dark matter radiate, cool and form disks, and
the shapes of halos and of colliding clusters bound how strongly dark matter can push on itself.

## Decisions waiting on the owner

1. Which form (1, 2 or 3).
2. How a point's kind is defined (the rung at which its last direction opened, or at which its region first opened).
3. Whether to decide the gravity field (gravity brief, option A) at the same time, since form 1 needs it.

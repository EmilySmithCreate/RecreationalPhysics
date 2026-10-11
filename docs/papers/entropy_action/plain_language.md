# Two score sheets for the same networks

**Series paper 10, plain-language draft, 10 October 2026.** The technical version is `paper.tex` in this folder.
No physicist has reviewed either. Labels in capitals say what kind of statement follows: PUBLISHED (someone
else's printed work), EXACT (arithmetic anyone can rerun), OURS (our reading, unchecked), THE AUTHOR'S (Emily
Smith's hypothesis).

## The question in one paragraph

A physicist, Ginestra Bianconi, has written down a rule that gives a network a single number, called an action.
In her work the network's wiring stays put, and she names what happens when the wiring changes as an open
question. Our networks do change their wiring. So we handed our networks to her rule, exactly as she wrote it, and
asked what number each one gets.

## What you need first

**A network.** Dots joined by links. In ours every dot has exactly four links.

**A square.** Four dots joined in a ring by four links. Squares are what our networks count.

**Three arrangements of the same dots.** They come from the first paper in this series.

- The **flat sheet**: a grid that wraps around both ways. Every link belongs to two squares.
- The **tube**: the same grid with one way around only four steps long. The short rings are squares too, so the
  links around each ring belong to three.
- The **knot**: sixteen dots curled both ways. Every link belongs to three squares.

A link that belongs to a third square is carrying one **surplus square**. The flat sheet has none.

**A score sheet.** A rule that looks at an arrangement and returns one number. Think of two judges at a diving
meet with different score sheets. They watch the same dives. What matters is whether they rank them in the same
order.

## The two score sheets

**Ours.** PUBLISHED, with one change of ours. The energy of the first paper gives points for every square and takes
points away for every surplus square. One knob, called lambda, sets how much a surplus square costs. At lambda = 1
this is a published model of emergent space (combinatorial quantum gravity). At that setting the three arrangements
tie. Below 1, curling up wins: knots beat the tube, and the tube beats the flat sheet. Above 1, the flat sheet wins.
The whole series works above 1, where flat space is the floor.

**Hers.** PUBLISHED. Her action compares two descriptions of the same network. One is a "metric": a number on every
dot, link and square that says how much it weighs. The other is the metric that matter would give those same cells.
The action measures how far apart the two descriptions are. With no matter present there are two cases:

- her **vacuum**, where the second description is as plain as it can be;
- a fuller case with one dial, called c0, that lets the network's own wiring shape the second description.

## What we did

1. **Checked that we built her machinery correctly.** EXACT. Her paper states several facts her operators must obey.
   Ours obey them on every network we tried. One of those facts counts holes: a flat sheet that wraps both ways has
   one piece, two independent loops and one enclosed space, and that is what came out.
2. **Scored the three arrangements**, each made of the same 64 dots.
3. **Scored 445 more networks**: end states saved by the simulations of the first paper, sheets with and without
   small leftovers and damage.

## What we found

**1. In her vacuum, her score sheet only counts.** EXACT. Every dot, link and square gets the same weight, so the
action is one fixed number for each of them, added up. Two networks with the same dots can then differ only in how
many squares they have. More squares, a more negative score: flat sheet -257, tube -273, knots -290. That is the
same ranking our score sheet gives when its surplus cost is switched off entirely.

**2. With her dial turned on, the ranking of the three stays the same.** EXACT. We tried the dial from a hundredth
to a thousand. Knots always scored below the tube, and the tube below the flat sheet.

**3. Across hundreds of networks, her score sheet behaves like ours with the knob below 1.** EXACT for each
network; the summary is OURS. Her action goes down with every square and up with every surplus square, which is
just what ours does. The surprise is that nobody put a surplus cost into her rule. It appears by itself, because
her rule notices when two squares share a link. But it is weak. Translated into our knob it comes out between
nearly zero and about one half, depending on her dial. Our knob has to pass 1 before flat space becomes the floor.

**4. A twisted twin scores the same.** EXACT. Cut the tube, turn one end, and glue it back. The result is a
different network, and her machinery can tell: the two have different fingerprints. Yet the action gives them the
same score to nine figures. At this size it responds to what the network looks like nearby and not to how it is
glued together far away.

## What this means, and what it does not

OURS. Read in the most direct way, her rule sits on the side where curling up pays. It has the right ingredient to
stop that, a cost for crowded links, in too small a dose.

That sentence has a large "if" in it. We scored every network with the same plain weights on all its cells. Her
theory says the weights should be worked out separately for each network, from an equation we have not solved. The
answer could change when they are. We also do not know whether comparing scores between different wirings is what
she has in mind at all.

So this is not a result about gravity, and it does not test her theory. It is the first step of a comparison, and
one question for her: is this the comparison you mean, and if so, what should be solved first?

## Where it sits in the larger picture

THE AUTHOR'S. In Emily Smith's hypothesis space is one settled arrangement of something deeper, and gravity belongs
to space: space has its own drive to curve. Her toy has no pull in it yet (the next paper in this group says why).
A published rule that links entropy to gravity is a natural place to look for the missing piece, and this paper
asks what that rule does on her networks before anything is borrowed from it.

## What comes next

- Her answer, if she gives one.
- The weights solved properly on the three arrangements, where symmetry keeps the work small.
- The same comparison on a flat sheet holding one of the small leftovers the first two papers describe.

## Words used here

| Word | Meaning |
|---|---|
| Action | A single number a rule assigns to an arrangement. |
| Cell | A dot, a link or a square. |
| Metric | A weight on every cell. |
| Surplus square | A third square on one link. |
| Lambda | Our knob: the cost of a surplus square. At 1 the model is the published one. |
| c0 | Her dial: how strongly the wiring shapes the second description. |
| Vacuum | Her case with no matter and the dial at zero. |

The numbers, the script that makes them and its tests are in the public repository (ASSUMPTIONS O111;
`scripts/exact_entropy_action.py`). Code and text were drafted with Claude (Anthropic) and directed and checked by
the author.

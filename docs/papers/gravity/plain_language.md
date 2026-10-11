# Why the leftovers do not pull on each other, and what a pull would need

**Series paper 11, plain-language draft, 10 October 2026.** The technical version is `paper.tex` in this folder
(first written 25 September, revised today). No physicist has reviewed either. Labels in capitals say what kind of
statement follows: PUBLISHED (someone else's printed work), EXACT (arithmetic anyone can rerun), MEASURED (a
simulation whose rules were written first), OURS (our reading, unchecked), THE AUTHOR'S (Emily Smith's hypothesis).

## The question in one paragraph

In this series a curled-up arrangement opens into flat space and leaves a few small knots behind. THE AUTHOR'S
hypothesis says gravity belongs to space: space has its own drive to curve, and things in it are drawn together
through the space between them. So here is a plain test for the toy model. Put two leftover knots into flat space,
some distance apart. Do they pull on each other?

The answer in the toy, as it stands, is no. This paper says why, and what would have to be added before the answer
could be yes.

## What you need first

**The toy.** A network of dots and links. Every dot has four links. The energy of an arrangement is worked out
link by link: each link looks at the squares it belongs to and reports a cost.

**Flat space.** A grid that wraps around both ways. In the toy it is the floor: nothing has lower energy.

**A leftover.** A small knot of dots still wired the old, curled way, sitting in otherwise flat space. The second
paper in this series found three kinds. Each is stuck: every single change you could make to it costs energy.

**A pull.** Two things pull on each other if the total cost of having both is lower when they are close than when
they are far apart. Then, given any jostling at all, they drift together.

## Three reasons there is no pull

**1. The bill is itemized.** EXACT. The energy is a sum of costs reported by single links, and a link only looks at
its own squares. Two knots that share no square get two separate bills, and the total is the same at every
distance. It is like two cars parked in the same lot: the fee for both is twice the fee for one, wherever they
park. The only discount comes when they touch.

**2. Counting look-alikes does not help.** EXACT, in the cases worked out. If dots are treated as interchangeable,
arrangements with more symmetry weigh more. That favors tidy placements, such as two knots exactly opposite each
other. It does not favor near over far, so it is not a pull.

**3. Flat space is stiff.** EXACT for the cost, OURS for what follows from it. Every single change to flat space
costs a fixed amount, the same however large the space is. A stiff medium passes a disturbance along only a few
steps before it dies out. Think of pushing on a brick wall: the push is felt where you push, not across the
building. PUBLISHED work on stiff media says the same: a force carried by a medium reaches only as far as the
medium's own ripples do.

These are really one fact. A pull between two things has to be carried by whatever lies between them. Here what
lies between them is flat space, and flat space in this toy carries nothing.

## What a pull would need

PUBLISHED work on forces that arise inside a medium names three ingredients, all needed at once.

- **Something that ripples freely.** A part of the medium that can change by any small amount at almost no cost, so
  that a disturbance spreads far. A pond has this. A brick wall does not.
- **Each object a source for it, in proportion to its energy.** Without that, a rippling medium gives only a faint,
  short-lived attraction.
- **The right kind of ripple.** Some kinds make like objects repel, as electric charges do. Gravity needs a kind
  that makes like attract.

## The simplest thing that would do it

EXACT. A network already carries one freely rippling thing if you allow it: a number on every dot, with a small
cost whenever neighboring dots disagree. We worked out exactly what this would add.

- By itself it gives a faint attraction that dies off very fast with distance. Right direction, wrong shape.
- If each leftover is a source for it, the result has the shape of Newton's gravity in three directions: it falls
  off as one over the distance.
- It barely changes which arrangements the toy prefers, so nothing in the first papers would move.

OURS. This would be putting gravity in, not finding it. What would be new is that the number lives on a network
that rearranges itself, so the thing carrying the pull travels through a space that the same rules built.

## Where things stand now

**Two routes.** THE AUTHOR'S decision and OURS for the cautions.

*A pull from counting, with nothing added.* Some published accounts get gravity from counting what a boundary
hides. For that to work here, the hidden count around a leftover has to grow with the boundary's size, and warm
flat space has to feel two leftovers at once. The count has been computed and is waiting to be read by the rules
written for it. How far warm space feels a disturbance is measured next. If that reach is short, this route is
closed.

*A number on every dot.* The author has decided to add one, on a condition: it must match her account of gravity
and give Einstein's numbers wherever those have been measured. Here is the catch. One number per dot is a theory
physicists tried a century ago. It gets falling apples right and starlight wrong: it does not bend light, and light
is seen to bend. So the condition needs more than one number per dot.

**The nearest published relative.** PUBLISHED. Ginestra Bianconi's "gravity from entropy" has a field of this kind
at every point of space, with equations for it. OURS: we tried the network version of her rule on our own
arrangements (the paper before this one). Used in the most direct way, it behaves like our rule with the knob set
where curling up wins, so it could not simply be borrowed. It is something to compare against, not evidence.

## What this paper does not show

It does not show that the author's account of gravity is wrong. It shows that this toy's energy, by itself, has
nothing in it that could carry a pull across a distance, and it names what would. A pull that comes from the
network rearranging itself in warm surroundings has not been measured.

## What comes next

- The reading of the hidden count.
- How far a disturbance is felt in warm flat space.
- A design for the quantity on the dots that says, before anything is run, what it must represent and what it must
  bend.

## Words used here

| Word | Meaning |
|---|---|
| Leftover, knot | A few dots still wired the curled way after space has opened. |
| Pull | A lower total cost when two things are near than when they are far. |
| Stiff | Every change costs at least a fixed amount. |
| Source | Something a field responds to, the way water responds to a dropped stone. |
| One over the distance | Twice as far, half as strong: the shape of Newton's gravitational potential. |

The exact results, scripts and tests are in the public repository (ASSUMPTIONS O22, O56, O60, O61, O103, O111).
Code and text were drafted with Claude (Anthropic) and directed and checked by the author.

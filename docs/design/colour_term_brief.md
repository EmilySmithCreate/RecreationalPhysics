# A term that tells the two colours apart: the brief (1 November 2026)

*Written at the author's request ("a term that tells the colours apart: we have this in concept, how can we solidify it
and add it to the toy?"). Ours, unverified, for her decisions under S1. Nothing here is built. The model with any of
these is our family around the published model, never combinatorial quantum gravity.*

## 1. What "colour" is in the toy, exactly

- Every point is on one of two sides (the bipartition), and every link joins the two sides. On the particle sheet the
  sides are the black and white points (`twist_curl_rules_current.md`, section 1): a box diagonal runs black to black or
  white to white, and the sign of a twist is its colour.
- A curled loop of four alternates sides, so it has two ways round, and **the two ways round differ only in which kind
  of point sits where** (T87, O170, exact on 2,048-point sheets: a side-preserving reversal of the loop extends to a
  renaming of its surroundings in only 4 to 8 % of columns; every signed column has a reversal that swaps the sides).
  That is the toy's colour sign of a curl: the loop's orientation relative to the two kinds of point.
- Her statement of 30 October: this is related to twist but not the same thing. The record keeps "colour sign" for it.

## 2. Why nothing in the toy can prefer a colour today (exact)

The energy is computed from the wiring alone: `total_squares(adj)` and `surplus(adj)` take the adjacency and never the
side array, and H = 16(N − S) + 4λX. Swap the names of the two sides everywhere and H is unchanged. The move set is the
same for both sides (a switch picks two links and exchanges their ends; the side array only says which end is which).
So the swap of the two sides is a symmetry of the energy, of the proposals and of every built torus, and any ensemble
or run that starts from a side-symmetric state stays side-symmetric on average. T88's one exception is the protocol
itself: its stores sat on the side-0 points of the fed layer, which is a one-sided boundary condition put in by hand.
Rule 11 applied to "the matter handedness breaches first at the pole" (Update 149): in this family that cannot happen by
the energy; it needs a term, a boundary, or a starting state that is itself one-handed.

## 3. Four ways to put it in, cheapest first

| | What is added | Where it lives | Exact first check | What it costs, said in advance |
|---|---|---|---|---|
| **D. A chiral X** (recommended first) | nothing in H; a built starting state with no side-preserving mirror. Candidates the record already has: a rod or slab whose curled direction closes with a shift along an open direction (a screw seam; O116's "shifted by two" and the half-turn closures of the 23 October twist check), or a seam that reverses orientation | the initial state | build it; check with networkx that no automorphism preserving sides maps it to its mirror (the T87 test on the whole state); then the T88 protocol on it with the fed stores split evenly between the sides, and the colour census by end | no knob at all, so S1 is untouched; the question becomes "does a one-handed X open one-handedly", which is her claim in its purest toy form. If the census shows no skew, D is dead and the claim needs B or A |
| **B. A one-sided push** (closest to her mechanism) | a rule of the sealed protocol, not of H: the stores at the pole pay only for moves that create curl of one colour sign (the feed is typed by colour) | the sampler's acceptance in sealed runs | the sign of a proposed move's new loops must be readable from the wiring before and after (needs the sign value of section 4, not only SIGNED/MIRROR); then T88 with the typed feed against the untyped one | a non-equilibrium rule: detailed balance is not claimed for sealed runs anyway, but the rule must be written down as a dynamics, with the sign convention fixed first; Update 31's typed stores (by direction) were withdrawn, and this is typing by colour, a different thing, so it needs its own dated decision |
| **A. A chiral energy term** | H_c = ε Σ over curled loops of the loop's sign value, ε a constant | the energy | the ladder with the term: a slab of one handedness and its mirror differ by 2ε per loop; every rung's wall shifts by a known amount; the term must vanish on flat space (it does, no curled loops) | it is C violation put in by hand, with a constant to scan and never tune; the published model's authors would call it a new model. Rule 13: a fit of ε to any observed asymmetry counts for nothing |
| **C. Interchangeable points** (already decided, Update 12) | nothing; the weight of an arrangement is divided by its renamings | the ensemble | none needed: the side swap is a symmetry of the counting as well, so the two colours weigh the same on average (exact argument) | it cannot do this job; listed so it is not proposed again |

## 4. The one thing every option needs: a sign *value*, not only SIGNED or MIRROR

T87 answers "does this loop have a sign at radius r" (yes in 92 to 96 % of columns) and not "which sign". A value needs
a frame. Two candidates, hers to choose:

- **The lattice frame.** On a built torus every point carries its original coordinates, the curled direction is an axis,
  and a loop a, b, c, d (a and c on side 0) is right- or left-handed by the sign of (b − a) × (d − a) · (the curled
  axis). Exact and cheap on the built state and on anything that keeps its labels; meaningless where the rewiring has
  scrambled the labels (a melted patch), which the census must say.
- **The two kinds of point as the frame.** The orientation that runs from a side-0 point to its side-1 neighbour along
  the loop in the direction in which the surroundings are not mirror-symmetric (T87's reversal). This is intrinsic and
  needs no coordinates, but it is defined only for SIGNED loops and only relative to the surroundings, so two loops'
  signs can be compared only when their surroundings can be matched. Harder; honest.

The T88 colour census now running in the sandbox uses the cheapest reading, the side census of the opened points and of
the five-square links by end, which needs no sign value; it says whether the fed end's opening favoured one kind of
point beyond what the one-sided feed put in. Its word is a look, not a verdict.

## 5. What is decided already, and what is asked

Decided (Update 149, confirmed): the slab is a stack of one-sided loops of one handedness, and the two twins carry the
two handednesses. Asked of her: (1) D first, or straight to B? (2) Which sign convention of section 4? (3) For D, which
built chiral X (the screw seam is the one the record can build today)? (4) The held-out size and her prediction, before
any run (rule 14). Nothing runs before her answer.

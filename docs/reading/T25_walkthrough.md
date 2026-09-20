# Trugenberger 2025, section by section, in plain English

*A walkthrough of [T25], "Networks as the fundamental constituents of the universe" (J. Phys. Complex. **6**, 042001; arXiv:2512.17676), for a reader following this project and not trained in physics. For each section: what the paper says, then how our approach compares. Written 2026-09-20. The paper was read in full; quotations are from the arXiv HTML version dated 2026-04-29.*

*Starts at section IV.1, as asked. Sections I to III define the curvature of a network and prove it converges to the curvature of general relativity. That is the machinery, and it bears on none of the six claims in `VISION.md` directly, so it is skipped here. Two things from it are worth carrying: the energy we implement is its equation (8), and the reason this curvature is worth using at all is section III, which is why our project uses this model and not Konopka's.*

*Section VI.2, on black holes and Hawking radiation, is also skipped: `VISION.md` parks black holes.*

---

## 4.1 Cycle condensation

**What it says.** The network is rewarded for containing short loops. Triangles pay best, then squares, then pentagons (9/8 : 1 : 5/8). But the no-sharing rule means a triangle can only sit next to a pentagon, and a triangle-plus-pentagon earns 9/8 + 5/8, which is less than the 2 you get from two squares. So squares win, and triangles and pentagons survive only as scattered defects.

Squares then pile onto a single street until it carries two, one on each side. Past that the local term takes back exactly what a further square earns, so the network starts filling up a different street instead. Keep going and every street ends up with two squares. In two dimensions that is a flat torus.

The paper then states the result our whole project turns on:

> "If only the global term is retained, the model undergoes a first-order phase transition in which the graph decomposes into isolated, weakly interacting hypercubic complexes. If the full Hamiltonian is used, instead the model undergoes a continuous phase transition from a random graph phase to a geometric phase."

Figure 3 is its evidence: squares per point against the coupling, cooling and heating, from 0.126 in the random phase up to 1 for a torus. Its caption argues the transition is continuous because the two directions show no hysteresis.

**How we compare.** This is the section we have spent the project reproducing.

- **The knob λ has three published points on it, and the line between them is ours.** λ = 0 is "global term only"; λ = 1 is the full energy of this paper; λ → ∞ is the hard cap, which is what Kelly et al. 2019 Sec. 4 actually simulated, since an infinite penalty is a prohibition. Each paper treats its own point as a separate model. We ran λ = 0 and λ = 1 to reproduce them. **The design work of this project sits between λ = 1 and about 1.6** — that is, between the full curvature and the cap, not between the first two — because that is where a flat sheet is the lowest state and other specific arrangements still sit in dips above it.
- At λ = 0 our runs reproduce what it claims: a jump, a wide gap between cooling and heating, and a cold phase shattered into small closed pieces. That is Gate A, which you passed.
- At λ = 1 we reproduce the *other* published figure, Kelly et al. 2019 Figure 8a, to half a per cent. We do not reproduce Figure 3 here. We agree with it at both ends and differ only between g = 2 and g = 6.3, where its points drop almost vertically and ours rise smoothly. That is unexplained and is the question for the authors.
- **The reasoning about triangles and pentagons is a ground-state argument.** The paper drops them because they "are excluded for an homogenous ground state". Figure 3 is not about the ground state but about the transition, where its own words leave them alive as defects. You raised this; we tested it, and the hot end of Figure 3 sits where a triangle-free run sits, so the hypothesis does not hold (`ASSUMPTIONS.md`, axis section).
- **The claim that it is continuous rests on no hysteresis at 160 points.** Our runs show no hysteresis either. But a weak first-order transition looks exactly the same at that size, because the barrier between the two states grows with size and a small system hops across it freely. Telling them apart needs the entropy curve, which is task T6.

**Bears on:** claim 1 (spacetime as a phase), claim 3 (one energy over both phases), and above all **claim 4**, since the order of this transition is the point on which your hypothesis and his make opposite predictions.

---

## 4.2 Geometry from combinatorics

**What it says.** This is where a network stops being a diagram and becomes a surface. Give every street the same length. Every loop then becomes a polygon, and the network becomes a tiling.

At each crossing four polygons meet. Call the number of sides of those four polygons k₁ to k₄. The sum

> α = Σ (kᵢ − 2) / kᵢ

decides the shape of the surface: below 2 it curves like a ball, exactly 2 is flat, above 2 it curves like a saddle.

In the geometric phase every crossing has at least one square, the rest being hexagons or larger. The further you cool, the more squares per crossing, and the flatter the surface, until four squares at every crossing makes it exactly flat. So the number of squares around a crossing is a **quantised curvature**: it can only be 1, 2, 3 or 4, and each value gives a different fixed curvature.

**How we compare.**

- Our order parameter and their curvature are the same quantity seen from two ends. Squares per crossing is four times our φ, so φ = 1 is four squares and flat, φ = 0.75 is three squares and saddle-shaped.
- **Our ladder of dimensions is a different cut through the same structure.** We count pairs of streets at a crossing that close no square: two such pairs means two large directions (a sheet), one means one (a tube), none means a closed knot. They count how many squares surround a crossing. Both are ways of reading geometry off the counting, and neither is in the other paper.
- Nothing in our project measures curvature yet. The "spot" in `VISION.md` asks for it, and this section is the recipe for doing it.

**Bears on:** claim 1 (what the space-like phase actually is) and claim 2 (the bridge towards general relativity).

---

## 5 Dynamics

**What it says.** Everything so far was about which arrangements are favoured. To watch a network change, the paper introduces a universal time and a rule for accepting a change:

> p = 1 / (1 + exp(ΔH/g))

It gives one elementary move, the "neighbourhood swap" of its Figure 8, which on a square lattice replaces three squares with two pentagons.

It then makes an observation that matters for your picture: a bubble of random phase can be *moved* somewhere else at no energy cost at all, because its energy depends only on how many points are inside it and on its boundary. Free motion at no cost means such bubbles drift about, and there is a maximum speed set by the street length and the number of moves per unit time. A speed limit falls out of the model rather than being put in.

**How we compare.**

- **We implement exactly this acceptance rule.** It is the "Glauber" option in our code, and our tests check it gives the same answers as the more usual Metropolis rule.
- **We do not implement their move.** We use a different one, the bipartite edge switch. Task T4 listed every arrangement up to 18 points and proved our move can reach all of them, which is more than the papers establish for theirs. At the sizes we actually simulate, neither is proved.
- Their time is counted in Monte Carlo steps, and so is ours. Your claim 6 says X has its own ordering and that our time is emergent. That is the same choice he makes.

**Bears on:** claim 6 (an ordering that is not our time), and the speed limit is a first step towards claim 2.

---

## 5.1 Hyperbolic holography

**What it says.** This is the most speculative part of the paper and the part that tries to deliver claim 2.

On a saddle-shaped surface, a random walk does not wander the way it does on a flat one. The space opens out so fast that a walker is carried away in what amounts to a straight line. The paper works through this and arrives at a striking claim: a random process on a two-dimensional saddle-shaped surface, seen by an observer carried along with the flow, looks exactly like **quantum mechanics in three-dimensional space**.

So the two-dimensional network is a "holographic screen", and the three large dimensions we live in, together with quantum behaviour and the arrow of time, are what that screen looks like from inside.

**How we compare.**

- We have nothing here, and we say so. Our model has no time and no quantum behaviour, and `VISION.md` lists both as out of reach.
- This is his answer to the hardest of your six claims, number 2. It is also where his programme is least tested: the paper states elsewhere that general relativity has not yet been derived in the large-scale regime.
- **It is worth comparing with your own picture of dimensions.** Yours has a fourth large dimension curling up, leaving three. His has three large dimensions appearing as the view from a two-dimensional surface. Both change the number of large dimensions; they do it in opposite directions. Neither is tested.

**Bears on:** claim 2, and it is the rival account of where three dimensions come from.

---

## 6.1 Matter, the Einstein equations and the cosmological constant

**What it says.** This is the section that competes with your claim 4 most directly.

Take a bubble of random phase sitting inside the geometric phase. Its points carry almost no squares, and its boundary points carry fewer squares and longer loops than the space around them. Two things follow together: the bubble has higher free energy than its surroundings, and it is more sharply curved.

Because those two rise together, you can write one as proportional to the other. Demand that this relation be expressed as a proper tensor equation that conserves what it should, and there is exactly one possibility: Einstein's equations with a cosmological constant.

The conclusion is stated flatly:

> "Matter, in this model is simply the random phase of the microscopic network."

and

> "at large scales, it is 'geometry that defines matter', not the other way around."

**How we compare.** This is the rival to your claim 4, and the difference is worth stating precisely because it is the crux of the whole project.

| | His account | Your claim 4 |
|---|---|---|
| What matter is | leftover bubbles of the random phase that never converted | what the energy released by the change turned into |
| Where its energy comes from | excess curvature of those bubbles | the latent heat of a first-order change |
| What the transition has to be | continuous is fine | must be first order, or there is no latent heat |

You both make matter out of the same stuff as space, which is your claim 3, and you agree it is not a separate ingredient. The disagreement is about the route. **His account needs no latent heat at all**, which is exactly why he can be comfortable with a continuous transition and you cannot.

One thing worth noticing: his bubbles are the *unconverted remainder*. That is your claim 5, the part that did not convert, doing the work your claim 4 assigns to the released energy.

**Bears on:** claim 4 (as its rival), claim 3, claim 2.

---

## 6.3 Dark matter

**What it says.** As the coupling falls, not everything reaches the best arrangement. Domains get stuck with a different number of squares per crossing than their surroundings: higher energy, more sharply curved, long-lived because there is a barrier around them.

He calls these **allotropes**, after the word for the same substance in two crystal forms. Carbon is the example: graphite is the settled form, diamond the higher-energy one that survives anyway. Such a domain is neither empty space nor ordinary matter, but it does gravitate, which makes it a candidate for dark matter.

**How we compare.** This is the closest thing in the published literature to your **X2**, and the resemblance is close enough to be worth taking seriously.

- **The difference, which `VISION.md` already records:** his allotropes are *less* stable than the space around them and are left behind by the change. Your X2 was proposed as *more* stable than X, and as a product of the change.
- **A note of ours, unverified.** His picture has the favoured arrangement stepping between discrete levels as the coupling falls: four squares per crossing, then three, then two. A system that switches between discrete levels, with long-lived stuck domains and a barrier in between, is the usual description of *first-order* behaviour, and he attributes it to a continuous transition. If those switches are real, each would be a small first-order step with its own latent heat, which would give your Δρ a home even if the first transition is continuous. That is on the list for step 3 of the plan and has not been tested.
- **What we have seen ourselves.** At λ = 0 our runs shatter into small closed pieces, and one of them is a 14-point piece nobody has described, which ties exactly with the 4-cube in energy. So alternative arrangements at equal or near-equal energy do turn up by themselves in this model family, which is the ingredient X2 needs.

**Bears on:** claim 5 (X2), and claim 4 through the allotrope ladder.

---

## What the paper never addresses

Worth naming, because these are where your hypothesis is on its own:

- **A sealed system.** Every calculation in the paper is at a fixed coupling, which means an unlimited bath. Your claims 5 and 6 are about what happens when the released energy has nowhere to go. We built that ourselves (`src/graphity/sealed.py`) and it is not in the paper.
- **A specific starting arrangement.** His "before" is the random phase throughout. Your X is specific and stable for now. The paper has no counterpart.
- **Energy conservation across the change.** Not discussed, because with a fixed coupling it never arises.

---

*Sources: the paper as cited above, read in full. Our own results, with their caveats, are in `ASSUMPTIONS.md` section D; the six claims are in `VISION.md`; how they differ from his programme is tabulated there under "How this differs from Trugenberger's combinatorial quantum gravity". Anything in this walkthrough labelled as ours is unreviewed by a physicist.*

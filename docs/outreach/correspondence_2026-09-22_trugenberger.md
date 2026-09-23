# Correspondence with the model's author: first reply, 2026-09-22

**Status.** A private email from Carlo Trugenberger to Emily, received 2026-09-22, in answer to
`note_to_model_authors.md`. It is **paraphrased** here, not quoted, and must not be quoted on any public
page or post without his permission. It is recorded because several of its points bear on the project's
own record (`ASSUMPTIONS.md` Q3 and O26, `VISION.md` Update 18, Gate B, T6).

## What he said, in order (paraphrase)

1. He does not use GitHub and so saw no plots or drawings; he asked us to bear with him.
2. **On the order of the transition (our question 1).** Fig. 8a of the 2019 paper points to a very smooth
   second-order transition. But both his own code, used for the 2025 review, and a very recent code
   written with Claude produce something that looks like a **hybrid transition**, which he says is typical
   of network models: **two continuous branches with a jump in the middle.**
3. He does not know what we mean by "hard cap" and "soft penalty" and has **no such thing in his code**.
   The **hard-core restriction is always imposed**; without it the networks crumple at low coupling.
4. **His current protocol** (the recent code): 1024 nodes; 10,000 sweeps and about 10^7 attempted moves
   per coupling; 40 couplings; **cold ascent**, each coupling starting from the final state of the
   previous, smaller one; a warm-up of 240 sweeps per coupling.
5. Our question 2 confused him: every graph studied is finite, and no theoretical finite-size scaling has
   been derived for this transition.
6. **On the 14-vertex graph.** The 4-cube is the torus lattice ground state with 16 vertices, so he does
   not see why its energy is compared with a 14-vertex graph; and the 4-cube analogy holds only at 16
   vertices, not for large graphs.
7. He could not picture "flat sheet" (he asks whether we mean a lattice torus) or "a torus with one side
   curled to length 4".
8. Free-energy minima can depend a great deal on N; for some N the ground state is highly degenerate. The
   real physics should be studied at **N = 4p² with p prime, where the ground state is unique**, and at
   very large p. The transition is rich and interesting and he is available to discuss further once he
   understands what we mean.

## What it changes (*ours*)

- **The "cap" is no longer a published case.** Our reading of [KTB19] Sec. 4, that its simulations ran on
  the space with no edge above d − 2 squares (ASSUMPTIONS Q3; VISION Update 3, "three published points"),
  is disputed by the author: no such restriction in his code, only the hard-core rule (Q2). The capped
  kernel stays what it always was in the code, the λ → ∞ end of the knob, but it is now labelled *our
  reading of Sec. 4, disputed by the author*, not a reproduction target. The kernel that is his model is
  the full Hamiltonian at λ = 1 with the hard-core rule, which matches Fig. 8a to rms 0.005 and Fig. 3 at
  both ends. Gate B's disagreement narrows to the middle stretch of g, and to protocol and size.
- **The author's current position on the order is "hybrid", not "continuous".** Two continuous branches
  with a jump between them, seen in his own runs at N = 1024. A jump is a discontinuity in the order
  parameter, which is the thing S2 looks for; a hybrid transition is not the plain first-order picture
  either. Two readings, and runs decide between them: **(a)** a genuine large-N effect that our
  equilibrium runs at N ≤ 160 are too small to show, which is exactly what T6's unreached sizes were for;
  **(b)** an artefact of cold ascent with a 240-sweep warm-up, in which the lattice branch survives past the
  transition and then collapses, which is metastability and would not appear at the same g on cold
  descent. **Discriminator:** both directions at N = 4p² (484 with p = 11, 676 with p = 13), parallel
  tempering, comparing the position of any jump on ascent and descent. This is now the top of the
  disorder → order track and is pre-registered before it runs.
- **Sizes.** Adopt N = 4p², p prime, for every disorder → order run: 36 and 100 (already run in T6), then
  196, 484, 676, 1156. The tube, a 4 × L torus, needs L even and L = p² is odd for odd p, so the tube runs
  cannot use these sizes. That is not a conflict: the tube is a chosen metastable arrangement, not the
  ground state, and its sizes were fixed by its own pre-registration. Say so wherever the two tracks are
  set side by side.
- **Vocabulary, for every future note.** Flat sheet = the lattice torus. Tube = the 4 × L lattice torus,
  whose wrap-around 4-cycles are themselves squares, so the edges along the short direction carry three.
  Knot = the 4-cube = the 4 × 4 lattice torus. Cap = "no edge with more than two squares". Soft penalty =
  the local term of Eq. (22) of the review, with its coefficient made a knob λ. Picture:
  `docs/figures/for_authors_torus_vs_tube.png`.
- **The 14-vertex point was misread**, and the fault is the note's: it is a statement about the
  global-term-only regime (λ = 0, [GV21]), where the network shatters into pieces with three squares on
  every edge, and the comparison is per vertex. Nothing to do with the lattice ground state at λ = 1. In
  the reply it is explained in one paragraph and then dropped.
- **S5 is not met.** He has read the note, not the plots or the code, and he replied with questions. The
  door is open; that is all that can be claimed, and the public pages must not say more.

## Actions

1. Reply (draft: `reply_draft_2026-09-22.md`), with pictures attached as files, not links.
2. Pre-register and run T6 at N = 196, 484 and 676, both directions, with tempering, when the laptop is
   free. Our prediction, written here first: on cold descent at equilibrium, no jump at N = 196 (our
   N = 160 runs are smooth in both directions); at 484 and 676 we do not know, and that is the point. If a
   jump appears at the same g in both directions, it is a discontinuity and T6's λ = 1 verdict is revisited
   at the new sizes. If it appears on ascent only, it is metastability of the lattice branch.
3. Ask him for the "hybrid transition" reference for network models, and read it.

---

## Second note from him, received 2026-09-23 (paraphrase; his words are private)

He added a postscript of his own accord, after the exchange above. Paraphrased:

- In his last codes he used **the final graph at one coupling as the starting point for the next**.
- That procedure **may have accentuated the apparent jump** in the middle of the transition.
- It **tends to accentuate trapped configurations in the wrong phase**, though it is faster and is
  what allows the larger networks.
- The real behaviour around the transition is **difficult to obtain for large graphs**.
- A diverging correlation length and susceptibility, finite-size, indicate the transition is
  **either continuous or mixed**, and the two are hard to disentangle.

### What it bears on

**1. He has named reading (b) of T13 himself.** T13 was written on 22 September to separate two
readings of his jump: (a) an equilibrium discontinuity above our sizes, or (b) the lattice branch
surviving past the transition on a protocol that carries state from one coupling to the next. His
postscript describes (b), as a caution about his own method, without having seen our runs.

**2. Our N = 196 data already shows the shape of (b), and it was read before this note arrived.**
Protocol P, a faithful copy of his method, gives hysteresis of 0.159 and an ascent jump in three of
four replicas. Protocol E at the same size, parallel tempering from a melt, passes its round-trip
gate and is smooth with no jump anywhere. Two protocols, one size, one kernel, opposite answers —
which is the disentangling he says is hard, done at a size where it is affordable.

**3. His own diagnostic points continuous.** A diverging correlation length is the signature of a
*continuous* transition; at a first-order transition it stays finite while the autocorrelation time
diverges ([RdF15], recorded in `TASKS.md` T6). So the evidence he cites for "continuous or mixed"
is evidence against first order, and he says so himself.

**4. It is a candidate explanation for Gate B** (*ours, unverified, and it should be checked before
it is believed*). Gate B has never passed because [T25] Fig. 3 and [KTB19] Fig. 8a disagree with
each other at the same N = 160 — 0.99 against 0.62 at g = 5 — and our equilibrium runs match Fig. 8a
to rms 0.005 while differing from Fig. 3 by up to 0.41, only in the middle of the transition. If
Fig. 3 was produced by the continuation procedure he has just described, then its high middle is
trapped configurations, which is the same shape and the same region as the gap between our own P
and E at N = 196. **The check is cheap and we have all four curves:** compare the P-minus-E gap at
N = 196 with the Fig.3-minus-Fig.8a gap at N = 160, in position and in size. If they match, the
two-year-old disagreement between his own figures has an explanation, and it is his.

**Checked the same day, and it does not fit** (`scripts/compare_gate_b_gap.py`; ASSUMPTIONS O27).
Three mismatches. *Direction:* Fig. 3 is above Fig. 8a on the *cooling* leg too (by 0.38), where
trapping would hold the random phase and put the curve *below*; our own descent under his protocol
sits on equilibrium to 0.004. *Extent:* our ascent under his protocol departs from equilibrium only
below g ≈ 3.5 and by 0.16 at most; Fig. 3 is above Fig. 8a from g ≈ 2 to 6.2 (heating) and 7.6
(cooling). *Position:* Fig. 3 crosses φ = 0.6 at g ≈ 6.2 to 7.0; Fig. 8a and our N = 160 runs at
5.2; all our N = 196 curves at 4.8. Fig. 3's transition is somewhere else in both directions, not a
trapped copy of Fig. 8a's. What *is* confirmed is the postscript itself: his continuation gives an
ascent-only tail at N = 196, exactly as he says. The question for him narrows to Fig. 3's coupling
axis or size.

### What it does not change

No definition, gate, prediction or verdict in T13. The amendments of 23 September were decided by
Emily earlier the same day, **before this note was pasted into the session**, and the reading of
N = 196 under the original wording is on the record above them. Nothing here is a reason to relax
a gate: T13 still needs two or more sizes, and protocol E at N = 484 has so far returned 0 round
trips on its first replica, which is the measurement his note makes most valuable and the one our
sampler is currently least able to deliver.

### Actions

1. ~~Run the Gate B check in point 4.~~ Done 2026-09-23; it does not fit (above, and ASSUMPTIONS O27).
2. Tell him what the two protocols gave at N = 196, since it speaks directly to his postscript, and
   ask the narrowed Gate B question (coupling axis or size of Fig. 3). Both are now in
   `reply_draft_2026-09-22.md`, in the paragraph added 2026-09-23.
3. The sampling problem at 484 and 676 is now the bottleneck on the question he cares about.

---

## Third note from him, received 2026-09-23, in answer to our letter of the same day (paraphrase; private)

- Warm thanks; he sees our skills as complementary and calls himself a poor programmer.
- **The coefficient of the local term must be exactly 1.** Only then is the Hamiltonian the total
  combinatorial curvature of the graph, and so the Einstein-Hilbert action on graphs. He knows the
  degeneracy at 1; the 2019 paper argues it does not matter on cooling, because squares form up to two
  per edge and then it pays to form squares elsewhere rather than add a third. What we called the cap
  helps reach the torus and speeds simulations.
- That argument assumes one torus ground state. At N other than 4p², p prime, several tori exist (the
  4 × L torus, whose handles are single 4-cycles, is his example), which is extra degeneracy even when a
  torus is reached; a finite-size effect absent at infinite N; hence N = 4p².
- **Our curled column is not an allotrope.** His example of one: a hyperbolic tessellation with three
  squares at each vertex, with an embedded region where some vertices have two; higher energy than the
  background, not matter, a different "space crystal", like graphite and diamond.
- **For physics a smooth plot is much better than the jump.** Starting each coupling from the previous
  one's final state makes long metastable trapping likely. He asks whether replica exchange can prove
  there is no hysteresis, i.e. that cooling and heating give the same curve.
- **He asks for the correlation-length plot of [KTB19] Fig. 9a**, for a talk at an important conference
  on 5 October, where he would present our plots with full credit for the numerical work.
- He raises a possible joint technical paper on these questions.

### What it bears on (ours)

- **The coefficient.** With λ = 1 fixed by him, the tube → sheet change of T7, T9, T10 (λ = 1.25) is not
  in his model: at λ = 1 the tube and the sheet have the same energy and nothing is released, and the
  exhaustive census at N = 18 finds no stuck state above the flat torus at exactly λ = 1
  (`results/dip_census_fine.csv`; the dips' height above the flat torus falls to zero as λ → 1). This does
  not change any result; it changes what they can be said to be about: a neighbour of his model.
- **His allotropes are order → order objects at λ = 1.** A stuck region of one ordered arrangement inside
  another is the shape of VISION claim 4 (Update 13), inside his model and his programme (dark matter as
  allotropes, [T24]). Whether any such patch is stuck at all in the 4-regular case, and how it gives way,
  has not been looked at by us; it needs a construction from him.
- **Hysteresis.** T13 at three sizes (PREREGISTRATION T13, reading of 23 September evening): no hysteresis
  above g ≈ 3.2; below it, no sampler used here reaches equilibrium at 484 or 676, and at 196 the
  lattice-started replica exchange never unlocked. **Our letter of 23 September overstated this** when it
  said the N = 196 jump "is the metastable lattice branch": which branch is the equilibrium below g ≈ 3.2
  is not known. The reply corrects it.
- **The correlation length** is pre-registered as T16 and running.

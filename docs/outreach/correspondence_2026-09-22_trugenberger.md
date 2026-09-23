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

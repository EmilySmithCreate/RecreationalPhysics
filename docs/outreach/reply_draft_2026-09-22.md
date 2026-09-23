# Draft reply to Carlo Trugenberger (not sent)

Drafted 2026-09-22 for Emily to send if she chooses. Attach the pictures as files: he does not use
GitHub. Suggested attachments: `docs/figures/for_authors_torus_vs_tube.png` (picture 1) and
`docs/figures/equilibrium_curves.png` (picture 2). Check each number against `ASSUMPTIONS.md` before
sending.

---

**Subject:** Re: Reproducing your combinatorial quantum gravity model: pictures attached, and your advice on N taken

Dear Carlo,

Thank you for such a quick and generous reply. You are right that I should have sent pictures rather
than a link. Two are attached, and I have translated my home-made words into yours below.

**What I meant.**

- "Flat sheet" is the lattice torus.
- "A torus with one side curled to length 4" is the 4 × L lattice torus (picture 1). Its short
  direction is a 4-cycle, so every wrap-around loop of length 4 is itself a square, and the edges along
  that direction lie in three squares instead of two. That is the only difference from the lattice torus.
  With the local term of Eq. (22) of your review multiplied by a coefficient λ, this torus has energy
  4(λ − 1) per vertex relative to the lattice torus: above it for λ > 1, tied at λ = 1, below it for λ < 1.
- "Soft penalty" is that local term of Eq. (22), with its coefficient used as a knob λ. "Hard cap" was my
  reading of Sec. 4 of the 2019 paper, where I understood the simulations to run on the space with
  P_ω = ∅, that is, with no edge carrying more than d − 2 squares. If that restriction was never in the
  code, I misread the sentence, and I am glad to know it. Everything I compare with your figures uses the
  full Hamiltonian at λ = 1, with the hard-core restriction always imposed, as in yours.
- The 14-vertex graph: I compared energies per vertex, and only in the global-term-only case (Eq. (22)
  without the local term), where the network breaks into pieces with three squares on every edge, as in
  Gorsky and Valba's simulations. The 4-cube is one such piece, and the 14-vertex incidence graph of the
  7-point biplane is another with the same energy per vertex. It is a curiosity about that limit and says
  nothing about the lattice ground state at λ = 1. I should have said so.

**On the transition.** This is the most useful thing you told me. Two continuous branches with a jump
between them is exactly what my runs do not show at N = 160: with the full Hamiltonian, heating from the
lattice torus and cooling from a random graph agree to 0.003 and give one smooth curve, which passes
through the points of Fig. 8a of the 2019 paper to an rms of 0.005 (picture 2). So either the jump needs
sizes well above 160, or it depends on the protocol. May I ask two things about the 1024-node runs?

1. Does cold descent (cooling from a random graph) show the jump at the same g as cold ascent? If the
   ascent branch were the lattice surviving past the transition as a metastable state, the two
   directions would differ, and that is what I would want to rule out first.
2. Roughly how large is the jump in S/N at N = 1024, and at what g does it occur?

I will take your advice on sizes and run N = 4p² with p prime, at 196, 484 and 676, in both directions,
using replica exchange so that the cold side equilibrates, and I will send you the curves as pictures.
If the jump appears at the same g in both directions at those sizes, I will have reproduced it and will
be glad to say so. If you could point me to a reference for the hybrid transitions you have in mind in
network models, I would read it first.

On my second question, sorry for the confusion. I was asking whether anyone had measured how the
transition moves with N, since the curves in Fig. 8a for N = 100 to 200 do not lie on top of one
another. Your answer, that no finite-size scaling has been derived, answers it.

With thanks, and with real appreciation for your time,

Emily Smith

---

*Not in the letter, for Emily:* nothing about the hypothesis, the loop, or the public pages goes to him
until the reproduction conversation has run its course; that was the plan in VISION "Before anything is
shown to anyone", and his reply shows why (he could not picture the tube from words alone). His email is
private and is paraphrased in `correspondence_2026-09-22_trugenberger.md`; do not quote it publicly
without asking him.

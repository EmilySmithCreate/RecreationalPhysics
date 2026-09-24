# Draft reply to Carlo Trugenberger (not sent)

Drafted 2026-09-22 for Emily to send if she chooses; revised the same night after she asked that it be
short, in his words, and useful to him. Everything to attach is copied into `docs/outreach/for_carlo_2026-09-22/` with the names the letter uses (picture 1, picture 2, the table), plus the letter as plain text. The repository is public, so the zip link works.

---

**Subject:** Re: Reproducing your model: pictures attached, my words translated into yours, and something that may be useful

Dear Carlo,

Thank you for such a quick and generous reply. You are right that I should have sent pictures rather
than a link. Two are attached, and I have translated my home-made words into yours below. I should also
say plainly what I am: a software engineer doing this as a hobby, mainly interested in a larger idea of
my own. I will keep our correspondence to the reproduction of your model, where I can be useful to you.

**What I meant.**

- "Flat sheet" is the lattice torus.
- "A torus with one side curled to length 4" is the 4 × L lattice torus (picture 1). Its short direction
  is a 4-cycle, so every wrap-around loop of length 4 is itself a square, and the edges along that
  direction lie in three squares instead of two. That is the only difference from the lattice torus.
- "Hard cap" was my reading of Sec. 4 of the 2019 paper, where I understood the simulations to run on the
  space with P_ω = ∅, that is, with no edge carrying more than d − 2 squares. If that restriction was never
  in the code, I misread the sentence, and I am glad to know it. Everything I compare with your figures
  uses the full Hamiltonian with the hard-core restriction always imposed, as in yours. "Soft penalty" was
  my name for the local term of your Eq. (22).
- The 14-vertex graph: I compared energies per vertex, and only in the global-term-only case (Eq. (22)
  without the local term), where the network breaks into pieces with three squares on every edge, as in
  Gorsky and Valba's simulations. The 4-cube is one such piece, and the 14-vertex incidence graph of the
  7-point biplane is another with the same energy per vertex. It says nothing about the lattice ground
  state, and I should have said so.

**On the transition.** This is the most useful thing you told me. Two continuous branches with a jump
between them is exactly what my runs do not show at N = 160: heating from the lattice torus and cooling
from a random graph agree to 0.003 and give one smooth curve, which passes through the points of Fig. 8a
of the 2019 paper to an rms of 0.005 (picture 2). So either the jump needs sizes well above 160, or it
depends on the protocol. May I ask two things about the 1024-node runs?

1. Does cold descent (cooling from a random graph) show the jump at the same g as cold ascent? If the
   ascent branch were the lattice surviving past the transition as a metastable state, the two directions
   would differ, and that is what I would want to rule out first.
2. Roughly how large is the jump in S/N at N = 1024, and at what g?

I have taken your advice on sizes. Runs at N = 4p² with p = 7, 11 and 13 are in progress, in both
directions, using replica exchange so that the cold side equilibrates, and a copy of your protocol as
you described it (cold ascent from the lattice, 240 sweeps of warm-up, 10,000 sweeps per coupling) at
the same sizes. I will send you the curves as pictures when they finish. If your jump appears at the same
g in both directions, I will have reproduced it and will be glad to say so.

*(Paragraph added 2026-09-23, after his postscript and after N = 196 finished; the two above stand for
484 and 676, which are still running.)*

**At N = 196 both have now finished, and your postscript is what we see** (picture 4). Your protocol, each coupling
starting from the previous coupling's final graph, gives on ascent a lattice that survives past the
transition and collapses between g ≈ 3.5 and 2.7, in three of four independent chains, with the ascent
curve up to 0.16 above the descent curve there; the descent curve itself agrees with replica exchange
to 0.004 at every coupling. Replica exchange from a random start, with 5 to 15 round trips between
g = 9 and 2.2 in every replica, gives one smooth curve and no jump anywhere. So at this size the jump
is the metastable lattice branch, exactly as you suggest, and it appears in a faithful copy of your
procedure. Whether the same holds at 484 and 676 I will know within days.

One thing the postscript does not seem to explain, which I mention only in case it is useful to you.
Fig. 3 of the review sits above Fig. 8a of the 2019 paper in *both* directions, cooling from random as
well as heating from the lattice, by up to 0.4 across the whole transition, and its rise is at g ≈ 6
where Fig. 8a's is at g ≈ 5. Trapping on descent would keep the random phase and put the cooling curve
*below* equilibrium, and our copy of your protocol shows no departure on descent at all. Could Fig. 3
have been made at a different size, or with the coupling normalised differently? Our runs match Fig. 8a
to 0.005 and Fig. 3 at both ends, so the difference is confined to that middle stretch.

**Something that may be useful to you**, since you mentioned a new code. At N = 18 we listed every valid
graph exhaustively (about 1.8 × 10¹² labelled graphs in 26 classes), so the averages there are exact
sums, not simulations. The table attached gives ⟨S⟩/N at seven couplings for the full Hamiltonian, with
the assumptions stated. Any code that samples the same ensemble should land on those numbers, and ours
does to 0.03 %; it is how we checked our sampler before trusting it at larger sizes. If it helps, the whole
code and every result file can be downloaded as a single zip without a GitHub account:
https://github.com/EmilySmithCreate/RecreationalPhysics/archive/refs/heads/main.zip

On my second question, sorry for the confusion. I was asking whether anyone had measured how the
transition moves with N, since the curves in Fig. 8a for N = 100 to 200 do not lie on top of one
another. Your answer, that no finite-size scaling has been derived, answers it.

With thanks, and with real appreciation for your time,

Emily Smith

---

## For Emily: what each paragraph says, and why it is there

Read this before sending. If any line here is not something you would say yourself, cut it from the
letter; nothing below is needed for the letter to work.

- **Opening.** Thanks; admits the link was the wrong medium; says what you are (a hobbyist with a larger
  idea, keeping to the reproduction). This is the sentence you asked for. It sets the terms honestly and
  means you never have to defend the hypothesis to him.
- **"Flat sheet is the lattice torus."** His name for our sheet. A torus is a grid whose edges wrap round,
  so it has no boundary.
- **"The 4 × L lattice torus."** Our tube is the same grid with one side only four steps long. Walk four
  steps that way and you are back where you started; that four-step loop is a square, which is why the
  edges along it sit in three squares instead of two. Picture 1 shows it. That extra square per edge is
  the whole of what "curled" means in the model.
- **"Hard cap."** We had read one sentence of his 2019 paper as saying his simulations forbade any edge
  from having more than two squares. He says no such rule is in his code. This paragraph says: then we
  misread you, and everything we compare with your figures uses your model. True: the curve in picture 2
  is the uncapped one.
- **"Soft penalty."** Just our name for the local term of his Eq. (22), the part of his energy that
  charges for a third square on an edge. Named so he can map it.
- **The 14-vertex graph.** In our note we mentioned a 14-vertex piece that ties with the 4-cube. He read
  that as a claim about his ground state. It was about the other case (local term switched off), where
  the network breaks into pieces. This paragraph says so and moves on. The fact itself is ours, checked by
  computer: every edge of that 14-vertex graph carries three squares, exactly like the 4-cube.
- **On the transition.** His jump is the one thing in his reply that could change our results. Our runs
  at 160 points show no jump whether we heat or cool. So either his jump needs bigger networks, or it
  comes from his procedure. Question 1 asks the discriminating thing: does cooling show the jump at the
  same place as heating? If not, the heated lattice was just hanging on past the transition, like
  supercooled water. Question 2 asks for the size and position of his jump so we can compare.
- **Sizes.** He said use N = 4p² with p prime. We are: 196, 484, 676. "Replica exchange" is parallel
  tempering, our tool for getting the cold side to equilibrate. "A copy of your protocol" is exactly
  what he described. Both are running now (T13). The promise to send pictures is one you can keep.
- **The N = 196 paragraph** (added 2026-09-23). His postscript said his own procedure might exaggerate the
  jump by trapping the lattice. Our copy of his procedure at 196 points shows exactly that: heating from
  the lattice, the lattice hangs on past the transition and then collapses, in three chains of four;
  cooling, and replica exchange, show no jump. Telling him this is the most useful thing we have, and it
  is his own suggestion confirmed. "Round trips" are graphs that travelled from the hottest coupling to
  the coldest and back, the check that replica exchange actually mixed.
- **The Fig. 3 paragraph** (added 2026-09-23). We checked whether his postscript explains why his two
  published curves at 160 points disagree with each other (ASSUMPTIONS O27). It does not: Fig. 3 is high
  on the cooling side too, where trapping would make it low, and its whole rise sits at a larger coupling.
  The paragraph asks the one question that remains, size or coupling, and says where we agree with him
  (Fig. 8a to 0.005, Fig. 3 at both ends) so that it reads as help rather than complaint. Cut it if it
  feels like too much for one letter; it can wait for his answer to the first questions.
- **The benchmark table.** At 18 points we listed every possible arrangement, so the averages are exact
  arithmetic, not simulation. A code that samples the same thing must land on those numbers. He said he
  has a new code written with Claude; this is a way to test it that costs him nothing. The assumptions
  are stated in the table so that a mismatch is informative rather than confusing.
- **The zip link.** GitHub can hand out the whole repository as one zip file to anyone, no account
  needed. Check the repository is public first, or the link will not work for him.
- **Second question.** We had asked whether anyone had measured how the transition moves with size. He
  found the question confusing. This paragraph restates it in one sentence and accepts his answer.

*Not in the letter, and why:* nothing about the hypothesis, the loop, or the public pages. He did not ask,
it is not his field, and his reply showed that even the tube needed a picture. His email is private and
is paraphrased in `correspondence_2026-09-22_trugenberger.md`; do not quote it publicly without asking him.

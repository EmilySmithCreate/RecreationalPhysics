# Second reply to Carlo Trugenberger (draft, not sent)

**For Emily, not for the letter.** *24 September: rebuilt from the version you pasted, with the ask now about
the paper: read it and, if it fits gr-qc, endorse it (an endorsement confirms the paper is on topic for the
category; it is not a review). Three changes to your version besides that:*
- *A stale figure is removed. "Within 0.3 % on average over ten conditions" is the number caught and corrected
  on 23 September. The record is a plain mean of 0.98 over twelve conditions (weighted 0.88 ± 0.06).*
- *The paper's terms are used (activation energy, relic defect, 4(λ − 1)).*
- *The torus statistics moved from the allotropes point into the new paper point, so they appear once.*

*Attach the paper (`docs/papers/curled_torus/paper.pdf`), picture 5
(`for_carlo_2026-09-22/picture5_N196_484_676_his_protocol_vs_replica_exchange.png`) and picture 6
(`for_carlo_2026-09-22/picture6_correlation_length_and_susceptibility.png`).*

---

Dear Carlo,

Thank you. Your reply was generous, and I agree that our skills are complementary: you know what the
model means, and I can build the tests. One thing you should know: I write the code and the analysis with
Claude (Anthropic's AI), which I direct and check; every new piece of code is tested against an independent
calculation before any result from it is trusted. You mentioned your newest code was written with Claude too.

**1. The correlation length, for your talk.** I ran it, defined exactly as in Sec. 4 of the 2019 paper:
the field on a vertex is the average of (squares on the edge)/2 over its four edges; C(r) is the
correlation of its fluctuations at graph distance r, divided by the variance of the edge field;
ξ = −⟨r / log C(r)⟩, divided by the diameter. The paper leaves three details open, and I fixed them before
any run: the average is over the distances where 0 < C(r) < 1; a perfect lattice, which has no
fluctuations, is skipped and counted; pairs in different pieces are ignored. I also recorded the
susceptibility N·var(S/N). Two protocols: your procedure, cooling and heating, at N = 196, 484 and 676,
read only at couplings where cooling and heating agree; and replica exchange at N = 196. (It ran at 36 and
100 too, but a check I set in advance on how often the copies swap turned out too strict for the smaller
sizes, so I leave those out.)

What came out is in picture 6, and it does not show what Fig. 9a shows.

- **The correlation reaches one or two steps, at every coupling and every size.** C(1) is 0.1 to 0.2, C(2)
  is 0.01 to 0.04, and beyond that C(r) is zero to within about 0.01, from g = 12 down to 1.5 and from
  N = 196 to 676. It does not reach further near the transition.
- **The susceptibility peaks at about 0.18 at every size**: 0.183 at N = 196, 0.181 at 484, 0.180 at 676.
  Its peak moves to lower g as N grows, as the curve does, but it does not get higher.
- **ξ / diameter, computed by the formula, shows spikes at single couplings and no trend with N.** Its
  largest values come from distances near the diameter, where there are few pairs and C(r) is noisy, and
  from snapshots in which C(r) at some distance is just below 1, where −r / log C runs away. That seems to
  be the difficulty Christy Kelly's thesis warns about.

So with the definition as I read it, and at these sizes, I cannot reproduce a divergent tendency. What I
see looks like a smooth crossover in which nothing grows with N, which is neither the signature of a
continuous transition nor that of a first-order one, and larger N could change that. If your code
computed ξ differently (a fit of C(r) to exp(−r/ξ), only small distances, a different normalisation, or
an average at fixed pairs of vertices over the run), that difference may be the whole story, and I
would like to know it. You are welcome to show any of these plots, with the sizes and protocols stated.

**2. Can replica exchange prove there is no hysteresis?** Partly, and I have to correct something I told
you. Picture 5 shows all three sizes, now with replica exchange started both from random graphs and from
the lattice torus. **Above g ≈ 3.2, yes:** at N = 196, 484 and 676, four independent ways of producing the
curve (your procedure cooling, your procedure heating, and replica exchange from either start) agree to
about 0.002 in S/N. There is no hysteresis there. **Below g ≈ 3.2, not yet.** At 484 and 676 replica
exchange does not mix: no copy travels from the hot end to the cold end and back, and the lattice-started
copies stay at S/N ≈ 1 while the random-started ones rise smoothly to about 0.95; the two never meet. Even
at 196, where the random-started copies mix well, the lattice-started ones never left the lattice. So in my
last letter, when I said the jump at 196 "is the metastable lattice branch", I said more than the data
showed: which of the two branches is the equilibrium one below g ≈ 3.2 is not known. That is exactly your
question, and it is open.

What is clear under your procedure: on heating, the lattice gives way at g ≈ 3.3 to 3.5 at every size,
while the curve it falls onto moves to lower g as N grows (S/N = 0.5 at g ≈ 5.9, 4.3 and 3.9). So the jump
grows with N: 0.16, 0.29 and 0.34 at 196, 484 and 676. If that pattern continues it would be larger still
at 1024. To settle which branch is the equilibrium one, I know of two ways: a move that mixes better, such
as the neighbourhood swap of Fig. 8 of the review (have you used it, and did it help at low coupling?), or
computing the free energy of both branches and finding where they cross.

**3. The coefficient.** Thank you for the clear answer: it is 1, because only then is the Hamiltonian the
total curvature. I accept that for your programme, and it has a consequence I should state. At exactly 1
the 4 × L torus has the same energy as the flat torus, so its opening releases nothing; the change I
described needs the coefficient slightly above 1. At N = 18, where we listed every graph, nothing is stuck
above the flat torus at exactly 1; the stuck states appear only above it. So that object lives next to
your model, not in it, and I will not describe it as more than that.

**4. A short paper, and a request.** I have written up the 4 × L torus as a short paper, "The curled torus
burps: front-driven decompactification in combinatorial quantum gravity" (attached, five pages). With the
coefficient λ above 1, the curled torus opens into the flat torus by a single front, with the two orders side
by side and almost nothing between them. It releases exactly 4(λ − 1) per vertex. Its waiting time matches a
prediction with nothing fitted (measured over predicted averages 0.98 across twelve conditions). Its
activation energy is exactly 12 at every size from 48 to 192 vertices, and it leaves one relic defect however
large the torus. A final section maps it from λ = 1.05 to 1.45. Every verdict was pre-registered, and the
code and data are public.

It is my first arXiv submission, so arXiv asks for an endorsement from someone who already publishes in the
category, and gr-qc is yours. As I understand it, an endorsement is not a review of the results: it confirms
that the paper is on topic for the category. Would you look at it and, if you think it belongs in gr-qc,
endorse it? The link arXiv gave me is [endorsement link; in the sent email only, kept out of this public
repository]. If you see anything wrong, I would of course rather hear it before it is posted.

**5. Allotropes.** Thank you for the example. The question I am here for is this: can a specific ordered
arrangement, stable for a while, turn into the space around it sharply (starting at one spot, spreading as
a front, releasing a definite amount of energy), and what is left behind? Your allotropes are arrangements
of this kind, and they belong to your model at coefficient 1. The tools in the paper do this measurement:
they follow the front as it moves, keep the total energy exactly fixed so that what is released can be
counted, and find the smallest push that starts the change. What I lack is a concrete allotrope to plant in
a 4-regular graph. If you can describe one (what the region looks like and what it sits in), I can find out
whether it is stuck at all at coefficient 1 and, if it is, how it gives way.

**6. A joint paper.** Yes, I would like that, and I should be clear about one thing now rather than later.
My time for this is limited (I'm building an AI startup and have upcoming travel), and it goes to the
question in point 5. A paper that asks how allotropes (or any stuck ordered region) give way in your model,
with the transition studied in detail alongside, is one I would gladly work on with you. A paper on the
random-to-lattice transition alone is not something I can take on.

With thanks,

Emily

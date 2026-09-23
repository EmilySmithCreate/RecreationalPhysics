# Second reply to Carlo Trugenberger, 2026-09-23 (draft, not sent)

**For Emily, not for the letter.** Answers his third note (paraphrased in
`correspondence_2026-09-22_trugenberger.md`). Attach picture 5
(`for_carlo_2026-09-22/picture5_N196_484_676_his_protocol_vs_replica_exchange.png`). The paragraph marked
**[RESULTS]** is filled in when T16 finishes, with a picture 6; **do not send before then**, so the letter
promises nothing. Three things are your call: the collaboration paragraph (its condition is yours, and
the wording should be too), whether he may show the plots (he offered full credit), and whether the
correction in paragraph 2 stays as blunt as it is (I recommend it does).

---

Dear Carlo,

Thank you. Your reply was generous, and I agree that we complement each other: you know what the
model means, and I can make the computer do what you want. One thing you should know: I write the code
and the analysis with Claude (Anthropic's AI), which I direct and check; every new piece of code is tested against an
independent calculation before any result from it is trusted. You mentioned your newest code was
written with Claude too.

**1. The correlation length, for your talk.** Yes, gladly. It is running now, defined exactly as in Sec. 4
of the 2019 paper: the field on a vertex is the average of (squares on the edge)/2 over its four edges;
C(r) is the correlation of its fluctuations at graph distance r, divided by the variance of the edge
field; ξ = −⟨r / log C(r)⟩, divided by the diameter. The paper leaves three details open, and I fixed them
before any run: the average is over the distances where 0 < C(r) < 1; a perfect lattice, which has no
fluctuations, is skipped and counted; pairs in different pieces are ignored. I also record the
susceptibility N·var(S/N). Two protocols: replica exchange at N = 36, 100 and 196 (p = 3, 5, 7), where it
mixes, and your procedure, cooling and heating, at N = 196, 484 and 676. The 484 and 676 curves are read
only at couplings where cooling and heating agree, which is where both are at equilibrium.

**[RESULTS: filled in from T16 when it finishes; picture 6.]**

You are welcome to show these plots, with the sizes and protocols stated. One caution you will know
better than I do: Christy Kelly's thesis warns that correlation lengths may not be well defined in this
model, since the diameters are short; at our sizes ξ is read from only 5 to 26 distances.

**2. Can replica exchange prove there is no hysteresis?** Partly, and I have to correct something I told
you. Picture 5 shows all three sizes, now with replica exchange started both from random graphs and from
the lattice torus. **Above g ≈ 3.2, yes:** at N = 196, 484 and 676, four independent ways of producing the
curve (your procedure cooling, your procedure heating, and replica exchange from either start) agree to
about 0.002 in S/N. There is no hysteresis there. **Below g ≈ 3.2, not yet.** At 484 and 676 replica exchange does
not mix: no copy travels from the hot end to the cold end and back, and the lattice-started copies stay at
S/N ≈ 1 while the random-started ones rise smoothly to about 0.95; the two never meet. Even at 196, where
the random-started copies mix well, the lattice-started ones never left the lattice. So in my last letter,
when I said the jump at 196 "is the metastable lattice branch", I said more than the data showed: which of
the two branches is the equilibrium one below g ≈ 3.2 is not known. That is exactly your question, and it
is open.

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

**4. Allotropes.** Thank you for the example; it made the idea concrete. The question I am here for is
this: can a specific ordered arrangement, stable for a while, turn into the space around it sharply — starting at
one spot, spreading as a front, releasing a definite amount of energy — and what is left behind? Your
allotropes are arrangements of this kind, and they belong to your model at coefficient 1. The tools I built
for the 4 × L torus do this measurement: they follow the front as it moves, keep the total energy exactly
fixed so that what is released can be counted, and find the smallest push that starts the change. On the
4 × L torus they gave waiting times predicted from the height of a single move, with nothing fitted,
to within 0.3 % on average over ten conditions; a release of exactly 1 per vertex; a push threshold of exactly 12 at every size from 48 to
192 vertices; and one small leftover however large the torus. What I lack is a concrete allotrope to plant
in a 4-regular graph. If you can describe one — what the region looks like and what it sits in — I can
find out whether it is stuck at all at coefficient 1, and, if it is, how it gives way.

**5. A joint paper.** Yes, I would like that, and I should be plain about one thing now rather than later.
The time I can give this comes from the question in point 4. A paper that studies the transition in
detail and also asks how allotropes (or any stuck ordered region) give way in your model is one I would
gladly work on. A paper on the random-to-lattice transition alone is further from what I can give time
to, although I am happy to keep answering questions about it, as with the plots for your talk.

With thanks,

Emily

# Second reply to Carlo Trugenberger, 2026-09-23 (draft, not sent)

**For Emily, not for the letter.** *Rewritten tight on 23 September, late night, at your direction: the paper goes with it (`docs/papers/curled_torus/paper.pdf`) and the letter asks for endorsement in gr-qc, his primary arXiv category. The earlier claim that waiting times matched to 0.3 % over ten conditions came from a stale line in VISION and is corrected here to the detailed record (plain mean 0.98, weighted 0.88 ± 0.06, twelve conditions).* Answers his third note (paraphrased in
`correspondence_2026-09-22_trugenberger.md`). Attach picture 5
(`for_carlo_2026-09-22/picture5_N196_484_676_his_protocol_vs_replica_exchange.png`) and picture 6
(`for_carlo_2026-09-22/picture6_correlation_length_and_susceptibility.png`). **The results paragraph is now
filled in (T16, PREREGISTRATION reading of 23 September, night), and it is not the result he wanted for
his talk**: no divergent tendency, correlations one or two steps long at every coupling, a susceptibility
peak that does not grow with N. Rewritten the same night at your direction: no offers of further work; point 5 is tit for tat (the
plots were the favour; a joint paper must include point 4's question). Four things are your call: the
collaboration paragraph (its condition is yours, and the wording should be too), whether he may show the plots (he offered full credit; he may not
want to now), whether the correction in paragraph 2 stays as blunt as it is (I recommend it does), and
the proposed T16 amendment (the swap-rate ceiling), which changes no verdict and is not mentioned in the
letter beyond one clause.

---

Dear Carlo,

Thank you; your reply was generous. For transparency: I write the code and analysis with Claude
(Anthropic's AI), which I direct and check, and every piece of code is tested against an independent
calculation before its results are trusted.

**1. The correlation length (picture 6).** Computed exactly as in Sec. 4 of the 2019 paper, with the three
details it leaves open fixed before any run (the average over distances where 0 < C(r) < 1; a perfect
lattice skipped; pairs in different pieces ignored), plus the susceptibility N·var(S/N). Your procedure at
N = 196, 484, 676, read where cooling and heating agree, and replica exchange at 196. It does not show what
Fig. 9a shows. C(r) falls to about zero within two steps at every coupling and size; the susceptibility
peaks at 0.18 at every size, moving to lower g with N but not growing; ξ/diameter shows spikes at single
couplings and no trend, driven by distances near the diameter where few pairs exist. At these sizes it
looks like a smooth crossover in which nothing grows with N. If your code computed ξ differently, that may
be the whole story, and I would like to know it. You are welcome to show these plots, with sizes and
protocols stated.

**2. Hysteresis (picture 5).** Above g ≈ 3.2, at N = 196, 484 and 676, four independent routes (your
procedure cooling and heating, replica exchange from random and from lattice starts) agree to about 0.002
in S/N: no hysteresis there. Below g ≈ 3.2 I cannot yet say. Replica exchange does not mix at 484 and 676,
and even at 196 the lattice-started copies never left the lattice, so which branch is the equilibrium one
is open. I have to correct my last letter, which called the jump at 196 "the metastable lattice branch";
that was more than the data showed. Under your procedure the lattice gives way at g ≈ 3.3 to 3.5 at every
size while the curve moves down (S/N = 0.5 at g ≈ 5.9, 4.3, 3.9), so the jump grows: 0.16, 0.29, 0.34.
Have you used the neighbourhood swap of Fig. 8 of the review, and does it mix at low coupling?

**3. The coefficient.** Understood: it is 1, because only then is the Hamiltonian the total curvature. At
exactly 1 the 4 × L torus and the flat torus have the same energy, so nothing is released, and at N = 18,
where we listed every graph, nothing is stuck above the flat torus. The change I described lives next to
your model, not in it.

**4. A short paper, and a request.** I have written up that change as a short technical paper (draft
attached). For the coefficient above 1: the curled torus decays by one front with the two orders
coexisting, releases exactly 4(λ − 1) per vertex, is started by a local push of exactly 12 at every size,
and leaves one small defect however large the torus; a final section maps it down towards 1. I would be
grateful if you would read it and, if you think it appropriate, endorse my first submission to gr-qc,
which arXiv asks of new authors. Beyond that, your allotropes are where the same question lives at
coefficient 1, and a joint paper on how they give way is one I would gladly work on with you. My time is
limited, so I cannot take on the random-to-lattice problem on its own.

With thanks,

Emily

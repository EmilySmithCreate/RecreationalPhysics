# Answer key for the paper 1 quiz

Do not open until you have answered. Section references are to `docs/papers/curled_torus/paper.tex`.
Standard-physics names are general knowledge, not looked up (ours, unverified).

1. λ multiplies the penalty on a third square on a link (the "local term"). At λ = 1 the energy is Trugenberger's
   CQG curvature, and a link with three squares costs the same as one with two, so flat, tube and 4-cube tie and
   nothing releases energy. (Intro, Sec. II)
2. ε = 4(λ − 1) = 1 per point at λ = 1.25. It is counted exactly from Eq. (1), H = 16(N − S) + 4λX. The tube has S = 5N/4
   squares (more than the flat grid's N), which lowers H by 4 per point, and X = N surplus squares (every link round
   the tube carries a third square), which raises it by 4λ per point. Net: 4λ − 4 = 4(λ − 1). Exact. (Sec. II, Ladder)
3. 12. It is the cost of one specific edge switch (move A, 32 − 16λ), the cheapest single move that leaves the
   tube. (Sec. III)
4. Moving from g = 1.5 to 1.25 multiplies the wait by e^(12/1.25 − 12/1.5) = e^(9.6 − 8) = e^1.6 ≈ 5, so about
   4,000 to 5,000 sweeps. (Move B and the other small terms change it by a little; this is the order of magnitude.)
   Standard name: the Arrhenius law.
5. The wait does not fall with N. It is flat. The reason is a property of the chain: it draws its two edges from the
   whole graph, so any one region is offered a way out about 1/N as often, cancelling the N places to start. A
   dynamics that updated each region at its own fixed rate would give a wait falling as 1/N. Fact about the chain,
   not about nature. (Sec. II end, Sec. III, Discussion)
6. Below 4/3 move A is cheaper than move B; at 4/3 they cost the same (32 − 16λ = 64 − 40λ gives λ = 4/3, cost
   about 10.7); above it move B is cheaper. (Sec. II, Eq. 3 and Sec. IV)
7. The same as a fresh tube: no memory. Nothing builds up in the tube; each sweep is a fresh draw. That is what the
   exponential distribution means. (Sec. III)
8. With thirty decays the band 0.7 to 1.3 is about two standard errors wide, so a perfectly memoryless sample
   fails it fairly often by chance. The paper says this and tests the whole distribution afterward instead
   (Kolmogorov-Smirnov, p = 0.53 pooled; not pre-registered). (Sec. IV)
9. A front is the boundary between converted and not-yet-converted regions, which moves outward from the seed. The
   measured share of points that belong to one order or the other at half conversion: 98.8 to 99.8% at λ = 1.25.
   Standard name: nucleation and growth. (Sec. III)
10. The transmission coefficient κ (0.56 to 0.68). It says the barrier governs the first exit, but crossing it does
    not guarantee growth; about a third of exits fall back. Recrossings lengthen the time to convert, not the time to
    the first exit. (Sec. IV)
11. No. A first-order phase transition is an equilibrium statement (two coexisting phases, a latent heat, as
    temperature varies). This is the decay of a metastable state at a fixed temperature. "Sharp" means the
    pre-registered sense: seed, single front, two states, little between. The paper says so under "Not claimed".
    (Discussion; VISION Update 44, open item (a))
12. 12 is the cost of the cheapest single switch out of the tube. With energy conserved and the moves being single
    switches, nothing below 12 can pay for any move, so that bound holds for any energy-conserving dynamics made of
    these switches. That 12 always *sufficed* is a property of this particular dynamics. (Sec. V)
13. The released energy (εN) goes into too few stores, so it heats the converted region past the melting
    coupling (about 3.5) and it dissolves into the random phase. A big enough reservoir (C ≥ N/2) absorbs it. The
    crossover scales with N because the release does. (Sec. V)
14. A held-out size: fit on the smaller sizes only, write a number with a range for the largest size before it
    runs, and score the verdict at that size alone. The paper claims only "no measurable growth across the sizes we
    could reach." (CLAUDE.md rule 14)
15. ε, the barrier, the 12-unit seed are unchanged (energies do not depend on how points are counted). The waiting
    time changes: each exit would be accepted roughly N/2 to N times less often, so the wait would grow with the
    system. That is reasoning, not run. (Discussion, "Labelled or interchangeable vertices")
16. Exact.
17. Measured, exploratory (the prediction was written into the config but not pre-registered).
18. Interpretation (ours, unverified): the κ numbers are measured; calling it a transition-state transmission
    coefficient is the borrowed reading.
19. The hypothesis's claim about reality (hers). The paper puts it in the Outlook as "motivation, not a result."
20. No: the paper does not claim that. It is "one Markov chain used to sample the model", with Metropolis acceptance
    chosen by us. What survives for any dynamics made of these switches is the energetics: the gap ε, the cheapest
    single move (12), and so the least energy a sealed system needs. What does not survive is the rates: waiting
    times, their independence of N, and κ. (Intro, Discussion)

## How to read your result

- Questions 1 to 6, 12 and 13 are the core. If any is shaky, re-read that explainer before anything else.
- Questions 11 and 20 are the ones a physicist will most likely ask. If you can answer them without notes, you
  are close to ready for a conversation.
- Questions 14 and 15 are where the project's own rules show. They are good ones to be able to raise yourself.

# Exact averages at 18 vertices: a benchmark any code can be checked against

Prepared 2026-09-22 for the model's author, to attach to a reply. Source: `results/ergodicity_small.csv`
(every valid state at N = 18 listed exhaustively, task T4, ASSUMPTIONS Q9) and
`scripts/exact_small_averages.py`. No sampling: each number is a finite sum over all states.

**The model these numbers assume.** 4-regular bipartite graphs on N = 18 vertices, with the hard-core
restriction (no two vertices share more than two neighbours); energy H = 16 (N − S) + 4 Σ_e (S_e − 2)₊,
where S is the number of squares (4-cycles) and S_e the number of squares through edge e (this is the
full Hamiltonian, Eq. (22) of the 2025 review with the local term at its own coefficient, in our
normalisation where a square is worth 16); Boltzmann weight exp(−H/g) over labelled graphs. At N = 18
every valid graph is connected and there are 26 classes up to renaming vertices within a side,
1 785 021 235 200 labelled graphs in all.

| g | ⟨S⟩/N | ⟨Σ_e (S_e − 2)₊⟩/N | share of weight on graphs with an over-full edge |
|---|---|---|---|
| 1 | 1.1539 | 0.6164 | 83.3 % |
| 1.5 | 1.1537 | 0.6188 | 84.0 % |
| 2 | 1.1522 | 0.6202 | 85.3 % |
| 3 | 1.1456 | 0.6165 | 88.5 % |
| 5 | 1.1307 | 0.5986 | 93.1 % |
| 10 | 1.1117 | 0.5707 | 96.6 % |
| 30 | 1.0963 | 0.5480 | 98.3 % |

Two remarks. At N = 16 every valid class has the same energy at this coefficient (the degeneracy the
review states), so ⟨S⟩/N = 1.3000 at every g there and the check is weaker. At N = 18 the averages
move with g, and our Monte Carlo reproduces them to about 0.03 % (ASSUMPTIONS section D), which is how
we know the sampler is right before trusting it at larger sizes. If a code does not restrict to
bipartite graphs, or does not impose the hard-core restriction, these numbers will not match and should
not be expected to.

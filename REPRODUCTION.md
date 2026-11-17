# What was reproduced from the published work, and where the evidence is

One page, so that nobody has to search the repository. Every path is relative to the repository root.
"The published model" is combinatorial quantum gravity as simulated in the papers below; the code here is an
independent implementation, written with an AI assistant (see the README's disclosure).

A copy of this page as it stood on 17 November 2026 is deposited with the paper on Zenodo
(https://doi.org/10.5281/zenodo.24310341). This page is the current one.

Sources: [KTB19] Kelly, Trugenberger and Biancalana (2019); [T22] Trugenberger (2022); [T25] Trugenberger (2025).
Full references are in `REFERENCES.bib`.

## The short answer

| Published result | Status | Number |
|---|---|---|
| [KTB19] Fig. 8a, squares per vertex against coupling, N = 160 | **Matched** where our chain is in equilibrium (g ≥ 4.9) | rms difference 0.005, largest 0.009, over 14 published points |
| Published behavior with the global term only (λ = 0): a jump, hysteresis, and a cold phase that shatters into closed pieces | **Matched in kind** at N = 64, 96, 160 | jump 0.65 → 1.46 in squares per vertex; hysteresis of about 2 in g; 84 to 95 % of vertices in closed pieces |
| [T25] Fig. 3, N = 160 | **Not reproduced** | agreement at both ends; up to 0.41 apart between g ≈ 2 and 6.3 |
| [KTB19] Fig. 9a, the correlation length | **Not reproduced** | ASSUMPTIONS O31 |
| [T22] Fig. 3, the three-dimensional (six-link) curve, N = 500 | **Not reproduced** | ASSUMPTIONS O43, O53 |

The two published N = 160 figures also disagree with each other in the same window (0.62 against 0.99 at g = 5),
so the [T25] Fig. 3 difference is recorded as an open question about that figure, not as a match and not as a
resolved bug. One candidate cause was tested and ruled out: the model's author reports that the local term of the
Hamiltonian as printed in [KTB19] and [T25] is missing a factor of 2 (ASSUMPTIONS Q28), and running the printed
form does not reproduce [T25] Fig. 3 either (ASSUMPTIONS O149). Our kernel was derived from the curvature formula
and carries the corrected coefficient.

Every statement on this page is a measurement by us (the authors of this repository) unless it says otherwise. The
match is to one curve at one size, over the range where our sampler equilibrates. It is not a validation of the
whole equilibrium curve. The comparison runs are labeled exploratory in their configurations: they were checks of
the code, not pre-registered tests of a prediction.

## 1. The reproduction: code, configuration, output

| What | Where |
|---|---|
| The kernel (energy, moves, detailed-balance argument in the docstring) | `src/graphity/cqg.py` |
| Runner | `scripts/run_cqg_sweep.py` |
| Configuration for the N = 160 curve, with seeds | `configs/cqg_n160_lam1_nocap_vs_t25fig3.json` |
| Its output and run metadata | `results/cqg_n160_lam1_nocap_vs_t25fig3.csv`, `.meta.json` |
| The same curve by parallel tempering (a second method) | `results/cqg_n160_lam1_nocap_tempering.csv` |
| Configuration and output for λ = 0 | `configs/cqg_lam0_first_look.json`, `results/cqg_lam0_first_look.csv` |

Result files are never overwritten or edited by hand; each comes from a configuration through a script.

## 2. The validation: comparison with the published points

The published points were digitized by us from the figures:

| Figure | Digitized points | Digitizing script |
|---|---|---|
| [KTB19] Fig. 8a, N = 160 | `docs/published/KTB19_fig8a_N160_digitised.csv` | `scripts/digitise_ktb19_fig8a.py` |
| [T25] Fig. 3 | `docs/published/T25_fig3_digitised.csv` | `scripts/digitise_t25_fig3.py` |
| [T22] Fig. 3 | `docs/published/T22_fig3_digitised.csv` | `scripts/digitise_t22_fig3.py` |

The comparison needs no simulation. It reads two committed files and prints a point-by-point table:

```bash
pip install -e ".[dev]"
python scripts/compare_with_published.py results/cqg_n160_lam1_nocap_vs_t25fig3.csv docs/published/KTB19_fig8a_N160_digitised.csv interpolate 4.9
```

Last two lines of its output:

```text
largest |difference| = 0.009
rms difference = 0.005 over 14 points
```

The `4.9` drops published points at colder couplings, where our single chains are not in equilibrium (heating
and cooling legs stop agreeing). Replace the second file with `docs/published/T25_fig3_digitised.csv` to see the
figure that is not reproduced.

Plots:

- `docs/figures/equilibrium_curves.png`: our N = 160 curves with the digitized published points
  (made by `scripts/plot_equilibrium_curves.py`).
- `docs/figures/cool_heat_lam0_vs_lam1.png`: cooling against heating at λ = 0 and λ = 1
  (made by `scripts/plot_cool_heat.py`).

Checks that do not depend on any published figure:

- **Exact enumeration.** Every valid graph at N = 16 and 18 is listed (`src/graphity/small_graphs.py`), which gives
  exact averages; the sampler reproduces them (`tests/test_small_graphs.py`, `scripts/exact_small_averages.py`).
- **Energy and moves.** Brute-force checks against networkx, incremental energy against full recomputation,
  constraint preservation and same-seed reproducibility (`tests/test_cqg.py`). Run all tests with `pytest`.
- **Two machines.** Re-running `configs/cqg_first_look.json` on Windows and on Linux gave the same CSV byte for byte.

## 3. The documentation: what was done and what it means

| Document | What it holds |
|---|---|
| `README.md`, "What has been done and tested" | the verdict table, including the gates above |
| `ASSUMPTIONS.md`, section D | the written account of each comparison, with numbers, commands and caveats |
| `TASKS.md`, Gate A, Gate B and the six-link section | the acceptance criteria, written before the comparisons, and their outcomes |
| `docs/papers/curled_torus/paper.pdf`, Methods, "Sampler and validation" | what the paper claims about reproduction, in four sentences |
| `docs/papers/curled_torus/supplement.md` | the claim-to-evidence map for the paper's own results |

## What this does not show

- Agreement with one published curve at one size does not show that the published model's transition is of any
  particular order, and the paper does not claim it does.
- The paper's own results are at a setting (λ > 1) that is not the published model. They rest on the kernel checks
  above and on their own pre-registered tests, not on the reproduction.
- The digitizing was done by us, from figures, and carries its own error (the published dots scatter by about 0.02).
- Nothing here has been reviewed by a physicist.

If you run the command and get a different number, please open an issue.

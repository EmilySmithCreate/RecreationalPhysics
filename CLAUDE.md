# Project memory for Claude Code

Read this first. Then read @VISION.md (the fixed reference for what we are testing and why) and @TASKS.md (what to do next, in order). Read `ASSUMPTIONS.md` before touching any model code.

## What this project is

A hobbyist's hypothesis about emergent spacetime, tested honestly on toy models. The owner, Emily, is a software engineer, not a physicist. The work asks one question:

> In graph models where geometry forms from a random network, which ingredients of the energy function make the transition first order (latent heat) and which make it continuous?

Current test bed: Trugenberger's 2D combinatorial quantum gravity model (`src/graphity/cqg.py`). Earlier work on Konopka's graphity model and a "restricted menu" idea is parked but kept (`energy.py`, `mc.py`, `graphs.py`, `docs/parked/`).

## Non-negotiable rules

1. **Every assumption has a source or is marked "Ours".** Add it to `ASSUMPTIONS.md` with a status (Sourced / Calibrated / Ours / Unverified) in the same commit as the code that relies on it. Cite section or equation numbers. Never invent a citation; if unsure of a detail, write "to verify".
2. **Reproduce before extending.** A published number or curve must be matched before any new result built on that code is interpreted. The gates are in `TASKS.md`. Do not skip or weaken a gate; if one fails, stop and report.
3. **No cherry-picking (VISION S1).** Parameter families are explored only along knobs fixed in advance, and every setting that was run is kept and reported.
4. **Pre-register.** Predictions and analysis choices are committed to `PREREGISTRATION.md` before the runs that test them. Exploratory runs are labelled exploratory in their config `_purpose` field and in any write-up.
5. **Results are append-only.** Never overwrite or delete files in `results/`. Every result comes from a config in `configs/` via a script in `scripts/`, with seeds in the config and a `.meta.json` beside the CSV. No hand-edited data. The runners refuse to overwrite; a `*.partial` file is scratch left by a crashed run and is the only thing in `results/` that may be deleted.
6. **Tests must pass** (`pytest`) before every commit. New kernels need: an independent brute-force check (networkx), an exactness check of incremental updates against full recomputation, constraint-preservation checks, and a same-seed reproducibility check.
7. **Say what is not known.** Distinguish measured, published, and guessed. Physics reasoning produced by an AI (including you) is unreviewed: label it "Ours, unverified". Do not describe a first look as a finding. Report inconvenient results as prominently as convenient ones.
8. **Plain language for the owner.** Explain results without jargon, define terms, lead with the answer, and push back when something does not hold up. She wants to understand the work, not just receive it.
9. **Do not drift.** A new idea goes to the parked list in `VISION.md` unless it bears on the working question. Changes to `VISION.md` are deliberate commits that say why.

## Commands

```bash
pip install -e ".[dev]"
pytest                                                        # all tests
python scripts/run_cqg_sweep.py configs/cqg_first_look.json   # ~3 min
python scripts/run_sweep.py configs/smoke_test.json           # parked Konopka model
```

## Code conventions

- Python 3.10+, NumPy, Numba for inner loops (`@njit(cache=True)`), networkx only for setup and tests.
- Graph state: `(N, degree)` int64 neighbour array; `-1` marks a temporarily empty slot during a move.
- Monte Carlo moves must have a written detailed-balance argument in the module docstring.
- Source keys in comments (`[T25]`, `[KTB19]`, ...) match `REFERENCES.bib`, whose `note` fields record whether each paper was read in full, abstract only, or not at all.
- Keep modules small and readable; the owner must be able to follow every line.

## Known state (2026-09-19)

- `cqg.py` implements global term + a **hard cap** of two squares per edge. The published model uses a **soft local penalty** instead ([T25] Eq. 22). The first-look results therefore test neither published case. Fixing this is task T2.
- Hot-phase square density agrees with the published Poisson floor 20.25/N to a few per cent at four sizes. This is the only external check so far for `cqg.py`, and it is weaker than it first looked: at infinite temperature and N = 160 the code gives 0.120 against the published 0.126, because of the hard-core rule, not the cap (ASSUMPTIONS O5). Whether that is a discrepancy depends on how the published number was obtained; unresolved.
- An apparent drift of the crossover with ln N was seen in the capped variant. Unexplained; do not cite it as a result.
- Chains freeze at low coupling (acceptance < 1 %). Parallel tempering is task T5.
- Ergodicity of the move set inside the constrained space is unproven (task T4).

## Disclosure

All code and documents so far were drafted with Claude (Anthropic) in conversation with the owner. Keep the disclosure section of the README accurate.

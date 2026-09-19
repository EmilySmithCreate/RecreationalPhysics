# geometrogenesis

Monte Carlo experiments on graph models in which space forms from a random network, asking one question:

> Which ingredients of the energy function make the geometry-forming transition **first order** (two coexisting phases, a latent heat) and which make it **continuous**?

This is a hobby project by a software engineer, not a physicist. It exists to test, honestly and reproducibly, one link in a personal hypothesis about emergent spacetime. It makes no claim about the real universe.

| Read this | For |
|---|---|
| [`VISION.md`](VISION.md) | the hypothesis, the working question, how it differs from published work, success criteria, plan |
| [`paper/introduction_plain_language.md`](paper/introduction_plain_language.md) | a non-scientist's introduction to the idea |
| [`ASSUMPTIONS.md`](ASSUMPTIONS.md) | every assumption, its source, and how far it has been checked; first-look results with caveats |
| [`TASKS.md`](TASKS.md) | what happens next, with acceptance tests and two reproduction gates |
| [`REFERENCES.bib`](REFERENCES.bib) | sources, each marked read-in-full / abstract-only / unread |
| [`CLAUDE.md`](CLAUDE.md) | working rules for AI-assisted sessions |

## Status

- **Test bed:** the 2D combinatorial quantum gravity model of Trugenberger and collaborators (`src/graphity/cqg.py`). Kernel tested; one external check passed (random-phase square density matches the published value at four sizes).
- **Not yet done:** the published model's soft local term (the current code uses a hard cap instead), and both reproduction gates. Until the gates pass, nothing in `results/` should be read as a finding.
- **Parked:** an earlier study on Konopka's graphity model and a "restricted menu" idea (`energy.py`, `mc.py`, `graphs.py`, `docs/parked/`). Its ground-state energy (−12.207 per node) matches the published −12.2.

## Run it

```bash
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
pytest
python scripts/run_cqg_sweep.py configs/cqg_first_look.json   # about 3 minutes on a laptop
```

Outputs: `results/<name>.csv` and `results/<name>.meta.json` (config, seeds, package versions). A runner refuses to start if its output already exists; to run a config again, copy it under a new name. While a run is in progress its rows go to `<name>.csv.partial`, so a crash keeps what had finished.

Checked on 2026-09-19: re-running `configs/cqg_first_look.json` on a second machine (Windows, numpy 2.5.3, against the original Linux, numpy 2.4.4) reproduced `results/cqg_first_look.csv` byte for byte.

## Reproducibility rules

1. Every number comes from a config in `configs/` and a script in `scripts/`. No hand-edited data.
2. Seeds live in the config. Results are append-only, and the runners enforce it (`src/graphity/results.py`).
3. Predictions are committed (`PREREGISTRATION.md`) before the runs that test them.
4. Whole parameter maps are published, not selected members.
5. Pin the environment before production runs (`pip freeze > requirements.lock`) and archive tagged releases (e.g. Zenodo) for a DOI.

## Layout

```
src/graphity/cqg.py        2D combinatorial quantum gravity kernel (current focus)
src/graphity/analysis.py   fluctuation measures, block bootstrap, autocorrelation time
src/graphity/results.py    result writer that never overwrites
src/graphity/energy.py     parked: Konopka cycle energy
src/graphity/mc.py         parked: Konopka Monte Carlo
src/graphity/graphs.py     parked: start states and menus
scripts/                   config-driven runners
configs/                   experiment definitions
results/                   outputs (append-only)
tests/                     25 tests
paper/                     text
docs/parked/               pre-registration draft of the parked menu study
```

## Licence

Not chosen yet. Until a `LICENSE` file is added, others cannot legally reuse the code. MIT and BSD-3-Clause are the usual choices for research code.

## Disclosure

Code and documents were drafted with Claude (Anthropic) in conversation with the author. Physics arguments marked "Ours" in `ASSUMPTIONS.md` have not been reviewed by a physicist.

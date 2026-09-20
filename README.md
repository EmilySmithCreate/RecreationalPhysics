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

- **Test bed:** the 2D combinatorial quantum gravity model of Trugenberger and collaborators (`src/graphity/cqg.py`). Kernel tested. The energy, the hard-core rule and the conventions of the published figures have been checked against the text of the source papers. The code as it stands (a hard cap of two squares per edge) is the model simulated in Kelly, Trugenberger and Biancalana (2019), Sec. 4.
- **External checks so far, exploratory, at the published size N = 160:** the soft-penalty model reproduces the digitised curve of Kelly, Trugenberger and Biancalana (2019) Fig. 8a to an rms of 0.005 wherever our simulation reaches equilibrium. Neither variant reproduces the sharp jump in Trugenberger (2025) Fig. 3: both agree with it on the hot side and rise smoothly where it jumps, by up to 0.4. Since the two published figures also disagree with each other there, that is an open question for the authors. Neither variant shows any sign of a first-order transition at this size. Details in `ASSUMPTIONS.md`, section D. These are observations, not findings.
- **Built (task T2):** the soft-penalty variant and the λ knob between the published models; the cap is now an option. See `ASSUMPTIONS.md`, section D, for what the first exploratory run of it shows.
- **Connectivity (task T3) and a first look at λ = 0, exploratory:** with the global term alone our kernel shows what is published for it: a jump on cooling, a wide gap between cooling and heating at three sizes, and a cold phase shattered into small closed pieces ("baby universes"), mostly 4-cubes. It also turned up a 14-vertex piece that ties with the 4-cube in energy, appears by itself in runs, and is not mentioned in the papers. Details in `ASSUMPTIONS.md`, Q8 and section D.
- **Gate A passed (2026-09-20, owner's decision):** the published behaviour of the global term alone is reproduced. That is a check on our reading of the model and on the sampler, not a finding of our own.
- **Not yet done:** reproduction gate B (λ = 1), which cannot pass against Trugenberger (2025) Fig. 3 for the reason above; whether Kelly et al. (2019) Fig. 8a should be the gate instead is an open decision. Until it is settled, nothing in `results/` should be read as a finding.
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
src/graphity/connectivity.py  connected pieces, baby universes, 4-cubes (has the graph shattered?)
src/graphity/squares.py    the two smallest graph readers, shared by the two modules above
src/graphity/analysis.py   fluctuation measures, block bootstrap, autocorrelation time
src/graphity/results.py    result writer that never overwrites
src/graphity/energy.py     parked: Konopka cycle energy
src/graphity/mc.py         parked: Konopka Monte Carlo
src/graphity/graphs.py     parked: start states and menus
scripts/                   config-driven runners (sweep over couplings; quench at one); digitiser and comparison for published figures
configs/                   experiment definitions
results/                   outputs (append-only)
tests/                     59 tests
paper/                     text
docs/parked/               pre-registration draft of the parked menu study
docs/published/            data points read off published figures (the images themselves are not kept)
```

## Licence

MIT (see [`LICENSE`](LICENSE)). Anyone may use, copy, change and share the code and the documents, for any purpose, provided the copyright notice stays with them. There is no warranty.

## Contributing

Pull requests are welcome from anyone. Only the owner merges into `main`. A pull request needs to pass the tests (they run automatically on every pull request) and follow the working rules in [`CLAUDE.md`](CLAUDE.md): every assumption sourced or marked "Ours", nothing in `results/` overwritten, and nothing described as a finding before its gate has passed. Contributions are accepted under the same MIT licence.

## Disclosure

Code and documents were drafted with Claude (Anthropic) in conversation with the author. Physics arguments marked "Ours" in `ASSUMPTIONS.md` have not been reviewed by a physicist.

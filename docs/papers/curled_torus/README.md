# The curled torus burps

**Activated escape and conversion in a graph model of emergent geometry**

- [Read the paper](paper.pdf).
- [Read the plain-language edition](paper_plain_language.pdf) ([source](paper_plain_language.tex), [notes](plain_language_README.md)). Its chapters run in the same order as the paper's sections, and the paper cites them as "PL, Ch. n".
- [Turn the knobs](https://claude.ai/artifact/F4sBf955J5ZT7rCq8uebW8): the interactive companion ([source](../../public/curling_ladder_tube.html)).
- Both editions as cross-linked web pages for the Side Nerd Blog, built from these sources: [`docs/public/mainnerd/`](../../public/mainnerd/) ([porting notes](../../public/mainnerd_PORTING.md)).
- A source number means the same source in both editions: the plain edition's sources 1 to 8 are this paper's reference list.
- [Supplemental methods, numerical certificates and reproducibility](supplement.md).
- [LaTeX source](paper.tex) and [abstract](arxiv_abstract.txt).
- [Release content hashes](release_manifest.json).

The paper distinguishes exact finite-size calculations, measured kinetics and exploratory interpretations. Its strongest kinetic result is the directly counted first-exit comparison. Reservoir equilibration and geometric period growth remain open questions. The long detected-decay waits are read retrospectively as mostly the detector's 200-sweep resting window (revision of 10 October 2026). A registered replay of the one cell with three waits left over (T58) found one more detector case and two real waits with nothing hidden, and first exits that follow the count when timed without the detector.

Build from the repository root with the project's `dev` and `plots` dependencies and Tectonic:

```text
python scripts/build_curled_paper.py --tectonic /path/to/tectonic
```

The supplement maps claims to configurations, data and analysis commands. The build synchronizes the abstract from the manuscript and regenerates figures, PDF and hashes. Check outputs ending in `_2026-10-09.log` are supplied for reproducibility. Author-feedback and draft-history files in this directory are working records, not part of the reader's paper or supplemental methods.

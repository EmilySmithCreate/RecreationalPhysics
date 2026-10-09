# The curled torus burps

**Activated escape and conversion in a graph model of emergent geometry**

- [Read the paper](paper.pdf).
- [Supplemental methods, numerical certificates and reproducibility](supplement.md).
- [LaTeX source](paper.tex) and [abstract](arxiv_abstract.txt).
- [Release content hashes](release_manifest.json).

The paper distinguishes exact finite-size calculations, measured kinetics and exploratory interpretations. Its strongest kinetic result is the directly counted first-exit comparison. Detected conversion tails, reservoir equilibration and geometric period growth remain open questions.

Build from the repository root with the project's `dev` and `plots` dependencies and Tectonic:

```text
python scripts/build_curled_paper.py --tectonic /path/to/tectonic
```

The supplement maps claims to configurations, data and analysis commands. The build synchronizes the abstract from the manuscript and regenerates figures, PDF and hashes. Check outputs ending in `_2026-10-09.log` are supplied for reproducibility. Author-feedback and draft-history files in this directory are working records, not part of the reader's paper or supplemental methods.

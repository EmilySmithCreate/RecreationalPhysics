# Corrections for review, 11 October 2026

Base: `5382053a60c4137cd446f83355e2a12177bb94ea`.
Branch: `codex/paper1-review-corrections-2026-10-11`.
Prepared with OpenAI Codex. This is a computational and editorial AI review, not human peer review.
Physical interpretations remain **Ours, unverified**.
This branch revises the manuscript sources and PDFs. The generated Side Nerd site has not been
refreshed or published; the converter is checked against the revised sources.

## Read the plain-language changes first

1. [Plain-language source](paper_plain_language.tex) and [rebuilt PDF](paper_plain_language.pdf).
2. [Technical source](paper.tex) and [rebuilt PDF](paper.pdf).
3. [Methods supplement](supplement.md), especially the retrospective geometry addendum.

For separate diffs against the reviewed version:

```sh
git diff 5382053a -- docs/papers/curled_torus/paper_plain_language.tex
git diff 5382053a -- docs/papers/curled_torus/paper.tex
```

The plain-language revision explains the six-link loop with a seam diagram, distinguishes zero
energy from one torus, and includes the fourth map and held-out size. It removes unsupported
inferences about phase order, coexistence, waiting-time tails and the alternative unlabelled
ensemble. The technical revision aligns the abstract, geometry, map and discussion with those
claims. Earlier registered failures remain failures.

## What the endpoint audit resolves

The width reader alone cannot identify a surface. The new reader checks the actual saved wiring:
ensemble validity, two square faces per edge, a single cyclic vertex link, connectedness,
orientability and Euler characteristic. For connected tori it reconstructs a translation lattice
and verifies every adjacency before measuring noncontractible loop lengths.

The original 120 low-lambda endpoints are narrow tori: shortest loop six, shortest independent
loop N/4. Among the 3,521 reached, zero-energy T60 endpoints, 3,446 are narrow tori, 73 are
disconnected surfaces and two are Klein bottles. These are retrospective, finite-sample findings.
Two T60 rows outside the reached selection also settle to zero energy; they are explicitly excluded
from this geometry denominator. No simulation data or original registration was changed.

The later six-link experiments answer a separate question. The previously discussed roughly
65% figure pools 20 wider-shell outcomes among 31 runs classified OPENS in three different
exploratory settings (4/5, 7/9 and 9/17). It is conditional on OPENS, is not a success rate over
all attempts, and uses a shell-profile comparison rather than a full endpoint topology certificate.
It should not replace Paper 1's four-link geometry result or be presented as a universal probability.

## First-reader positioning

The independent scientific question is whether a specified ordered graph escapes and converts
under a controlled deformation of CQG, and which geometric properties the local energy fails to
ensure. The broader origin-of-space hypothesis motivates the question; these runs do not test
that hypothesis against cosmological or quantum observations.

A modest initial reading request can therefore focus on the model and endpoint sections:
is the deformation clearly distinguished from CQG, and does the geometry result make the
bounded kinetic question scientifically useful? Novelty and suitability for publication still
need a relevant physicist's judgment. No claim of an error-free or publication-ready manuscript
follows from these checks.

## Validation

- Full suite: **926 passed in 523.05 seconds**, recorded in `pytest_2026-10-11.log`.
- The initial run had 920 passes and six converter fixture errors from a new LaTeX subsection.
  The heading now uses the manuscript's supported style; the figure-count expectation includes
  the new diagram. All 22 converter tests passed before the clean full rerun.
- All 3,641 selected saved graphs were read again by the packaged geometry checker; counts match
  the independent audit. Nine known-surface, relabelling and invalid-input controls pass.
- Both PDFs rebuilt with Tectonic: 34 plain-language pages, 11 technical pages, no unresolved
  references or overfull boxes. The geometry and conclusion pages were visually inspected.
  Remaining TeX underfull-box warnings concern spacing.
- The release manifest records the revised source and artifact hashes. Raw results and
  historical registrations were not edited. No site was published and no correspondence sent.

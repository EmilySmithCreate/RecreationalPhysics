# A measured number the toy could predict: the brief (draft, 20 October 2026)

*Written on the author's request of 20 October: "try and get us somewhere close to measured number that can be predicted
and then calculated with our toy to see how good it is." Ours throughout, for her decision. Rule 13 governs every line: a
number that comes out close counts only after it has been derived independently, its input uncertainty carried through,
its inputs checked for containing the target, its neighbouring settings tested, and the number of other combinations that
would also have matched counted (`docs/design/reality_targets.md`, item 12). Measured values below are from general
knowledge and are to be checked at their sources before anything is compared with them.*

## What makes a candidate fair

The toy must compute the number from its own rules, on its own clock, with no constant set by the target. The number must
be dimensionless, so that no conversion from toy units to physical ones is needed. And the measured value must be known
to a few per cent or better, so that agreement or disagreement means something.

## The candidates

| Measured number | What the toy would compute | Fair? | Expectation (ours) |
|---|---|---|---|
| **w, dark energy's equation of state**: w = −1.03 ± 0.03 (Planck 2018 with supernovae and BAO), with recent DESI analyses preferring a w that changes with time (w₀ above −1) at about 3 to 4 standard deviations | Under her growth rule (Update 75) new rows arrive clean and the network's missing squares fill them in at its coupling. Two rates on the toy's one clock, rows added and missing squares appearing, set whether the density of missing squares per point stays constant as space grows. Constant means w = −1; a density that falls means w above −1, by an amount the two rates fix | **Yes**: both rates come from the toy's rules and fair clock, and nothing sets the density by hand | A steady state at constant density, so w = −1 once growth has settled, with a departure while it settles. Which side of −1 the departure lies on is a sign the data can check |
| **n_s, the tilt of the early universe's ripples**: 0.9649 ± 0.0042 (Planck 2018), nearly the same strength at every scale | The spread of flaws in a space grown by rows, measured scale by scale | Yes, but the dimension (the toy's sheet is two-dimensional) has to be handled with care | Flat noise, which is far from the measured tilt; the knots' own layout already showed this (the look of 18 October). Most likely a clean failure |
| **The ratio of dark to ordinary matter, 5.36** | Nothing fair: it compares two slivers, not two releases (O89), and fitting to it is ruled out | No | — |
| **Three large directions** | The toy has no rule that picks a number of directions | Not yet | — |

## Recommendation: w

It is the one candidate where the toy computes the number with no free conversion. Both rates live on the fair clock: a
row is offered once per fair sweep (Update 75) and a missing square appears at the rate the coupling sets. It also asks a
live question: whether dark energy is truly constant. Her picture gives a definite answer, a constant once growth settles,
which the data can test.

What it needs:
1. **The growth rule built** (Update 75, now fully specified): rows inserted into a flat sheet only where no link within
   three steps along the row is curled, each row offered once per fair sweep. Code and rule-6 tests first. A row is
   well defined only where the sheet is flat around it, which the clear-corridor rule already guarantees.
2. **The coupling.** Update 70 says the loop's coupling is fixed by its total energy, but no value is derived. So the
   test scans several couplings and asks whether the answer is the same at every one. If it is, the prediction does not
   depend on the unknown.
3. **The translation from a sheet to space**, stated before the run: the toy is two-dimensional, so a density per point
   falling as a power of the area maps to w through the area's growth, not the volume's. That changes a factor, not a
   sign, and is said in the registration.
4. **Her prediction**, then the registration with a held-out size (rule 14), then the run.

## Two consequences of the growth rule, found while writing this (ours, exact by construction)

1. **Rows come two at a time.** On the toy's torus the two kinds of point alternate around every loop, so a loop must
   keep an even length; adding one row would make it odd. Growth adds rows in pairs. (Her words of 20 October: "at least
   2 but maybe more rows growing".)
2. **A whole row is clear less and less often as space grows.** A row is added only if the corridor three steps wide on
   either side of it, along its whole length, holds no curled link. If curled links appear at random with some small
   share f of the points, the chance a row of W points is clear falls roughly as e^(−7fW). In the toy's sheets (W of a
   few tens) rows clear often; in a space of astronomical size a whole row would essentially never be clear unless f is
   astronomically small. So in her picture growth requires the network's flaws to be extremely rare, and the network's
   flaws are also her candidate for dark energy (Update 70), which is observed to be extremely small. The rule ties the
   two together: space can grow only because dark energy is tiny. Whether that is a feature or a problem is hers to
   judge; one alternative is a row that only has to be clear over a stretch of fixed length, which would bring back
   flaws at the stretch's ends (the pairs, set aside on 20 October).

## What would count

- **For her picture:** the density of missing squares per point settles to a constant under growth at every coupling
  scanned (w = −1), and the settling is slow enough to leave a measurable departure whose sign matches the data.
- **Against it:** the density keeps falling (a dark energy that fades away) or keeps rising, at every coupling; or the
  growth stalls before any steady state.
- **Neither:** the answer changes from one coupling to the next, so it depends on a number the picture has not fixed.

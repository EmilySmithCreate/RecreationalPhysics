# Plain-language edition

**Draft of 13 October 2026, from the author's notes on Chapters 1 to 3; she has not read it.** Her notes: the
edition is dense; Chapter 1 should be a third as long and run author, hypothesis, approach, outline, then what a
toy is and why this one; Chapter 2 about half as long, on reproducing the published model and the one thing our
toy changes; and "flat" in Chapter 3's words and drawings misleads, because the tube is a ring and the sheet is
a fatter doughnut.

- **Chapter 1** is one page (0.6 of a page of text; it was 1.9 pages), in her order. Its two sketches are gone:
  the hill returns with its numbers in Chapter 4, and the histogram sketch left with the word "hump".
- **Chapter 2** is two pages (it was three). The published model is one figure, a card with its rules, its
  price list and its one move, in place of three figures; the card shows the published prices (16 and 4), and
  the knob comes after the reproduction, as the one thing we change. Sharp against smooth is three sentences
  (water, a magnet, the two names); the test is described as a jump in energy, and the six numbers are a
  two-row table. The caveats on the published simulations and Kelly's thesis share one footnote.
- **Chapter 3** has a new section, "Ring and doughnut: flat is not the same as open" (about a page). Every
  arrangement in the toy closes on itself; flat is about each dot's surroundings and wide is about the whole
  shape; a count an inhabitant could make (dots within one, two, three steps of home) matches an endless
  grid's until half the way around, so a doughnut much wider than its inhabitants is open in every way they can
  check, and the tube falls short at two steps. One paragraph sets this beside real space, measured flat and
  not measured endless (source 15, read by abstract). A direction is no longer called "large" where the count
  $d$ is defined: the count says a direction is not closed up in one square, not how far around it is.
  Chapters 6 and 7 now point back to these two words and this count.
- **The table's numbers are new to this edition and exact**: counted with the record's own readers
  (`scripts/read_open_shells.py`, `scripts/read_endpoint_width.py`) and pinned in
  `tests/test_read_shapes.py::test_the_count_from_inside_falls_short_at_half_the_way_round`. The technical
  manuscript does not carry them; its `width` reading of the saved end states is the same count.
- The PDF has 36 pages and 30 figures (it had 36 and 33). **The blog pages are not rebuilt**: post 01 under
  `docs/public/mainnerd/` and its record of figure sizes still hold the 12 October text and its 33 figures.
  When they are rebuilt, the pinned `plain-fig-33.svg` in `tests/test_main_nerd_pages.py` becomes 30.
- Not done, hers to decide: renaming "the flat sheet" through Chapters 4 to 11 (it is defined honestly in
  Chapter 3 and keeps its name after that), and any shortening of Chapters 3 to 11.

**Revised 12 October 2026 from the author's notes on the 11 October revision.** Chapter 1 says why two humps
are not enough and that the author asks for a jump in energy, not for the words "first order". Chapter 3
states the curling cost as something she wants tested, with what is exact in the toy and what is missing.
Chapter 6 adds what would happen if the re-gluing kept happening and whether being flat makes a wide shape
likely. Chapter 7 corrects "melted" (a sealed tube cannot melt: O123) and reports the trapped-heat test
(T61). Chapter 12 names the next test, a price on loops of six, and reports nothing from it. Later the same day, from her read of it: the jump-in-energy point is said once (it had been said four times), and Chapter 6 gains a figure of the seam shifted by two, four and six places, with the older six-step sketch moved up to sit before it. Chapter 6 also says what "flat" means where it asks whether being flat makes a wide shape likely (flat at every dot, which a narrow tube also is). Chapter 12 says what happened in the test with a price on loops of six (T62 and T64, two sizes) and what follows from it for the scrap paper and the three-direction paper, at the owner's request. 36 pages.

**Current revision: 11 October 2026.** Review [the corrections](review_corrections_2026-10-11.md)
before the earlier drafting notes below. The PDF now has 34 pages and 32 figures, including a
new seam diagram. Chapter 6 reports reconstructed narrow endpoints and distinguishes tori,
disconnected surfaces and Klein bottles. Chapter 9 includes T60 and the held-out size.
The conclusion separates first escape, committed conversion and large-scale geometric opening.
Both editions and the supplement include these corrections; sources and PDFs are synchronized.

## Earlier drafting notes (historical)

Read [paper_plain_language.pdf](paper_plain_language.pdf). It is a standalone explanation of
paper 1 for readers without a physics background, rebuilt on 9 October 2026 around one
narrative: we live in flat space and cannot rerun its birth; a published model of space made
of links asks whether geometry condenses out of randomness at the curvature setting; the
author asks instead what a sharp change *from a specific curled arrangement* would look
like, and the model is deformed by one knob to hold such an arrangement. Each chapter then
asks one question of that arrangement (what it costs to start, how long it waits, what takes
shape, where the energy goes, what remains, how the knob changes it), with a "why we went
here" note and a "point to keep" box. Chapter 10 maps every knob the simulations turned,
why each stopped where it did, and what lies past each edge, with the kind of knowledge
marked. Chapter 11 keeps the unfinished part (the long waits, the detector, the three
inconclusive maps) inside the story.

**Revised 10 October 2026 from the author's notes.** The edition now introduces each idea
before it uses it and reveals results in reading order (the technical paper has the abstract).
Chapter 2 holds all of the published model's mechanics: dots and links, the price list, the
knob λ, the one move (the partner swap), the warmth g and the bath, then the field's question
and our reproduction of it. Chapter 3 defines a direction, the torus, curling (and why four
steps around is the tightest curl), the tube, the ladder and, only there, the burp. Chapter 4
introduces the sealed system with its store at the push test, and Chapter 7 builds on it.
The author's idea is stated once in Chapter 1, with a paragraph on why she pursues it, and
returns once in Chapter 12; the chapters between are about the change itself, and the
hypothesis's claim numbers are no longer used. Sources are numbered and listed at the end,
with the technical paper as the first. The direction figure gained six- and eight-link dots
as a pointer to the later paper on three and four directions. Chapter 2's sentence that no
published work was found with the surplus price above 1 rests on the written search in
`docs/reading/notes/2026-10-10_prior_work_lambda_above_one.md` (CLAUDE.md rule 15), which is
source [5] of the edition; that note has to be committed with the edition for the reference
to resolve.

Every number comes from the technical manuscript and supplement beside it (`paper.tex`,
`supplement.md`; revised 10 October 2026 on top of commit
`d0326dec3b988f6cd516a1f5c6f4663344750b33`, and reordered that day to run in the same order
as this edition's chapters) or from the project's record (ASSUMPTIONS, PREREGISTRATION). Statements are tagged by kind (exact, measured, measured-exploratory,
published, our reading, the author's claim) following CLAUDE.md rule 10.
Later experiments (what the scrap does afterwards, larger networks, more directions) are
teased and named as the subject of later papers, not reported. The release is called the
burp, the author's word, in place of "lump" (her decision of 9 October 2026), from the point
in Chapter 3 where it is defined; before that the text says "energy given off".

Wherever the text asked the reader to build a picture from sentences, the sentences now sit as
callouts on a diagram instead (the author's note of 10 October): the model's rules with what
each forbids, what a direction is, the wrapping grid, the tube, why four steps is the tightest
curl, the third square on a curled link, bath against sealed, and the four checks that
certify a torus. The arithmetic of the ladder and of the two exit routes is set out as bills
in small tables.

The 33-page edition has 31 figures: the three figures of the technical paper
(`fig_tori.pdf`, `fig1.pdf`, `fig_lambda.pdf`) and 28 drawn in TikZ/pgfplots inside the
source, including data charts built from the record (the seed-threshold staircase, the
twelve waiting-time conditions against the count, the reservoir outcomes, the relic count
against size) and sketches labeled as sketches.

**The long waits, 10 October.** The former chapter on the unexplained long waits is gone. What
replaced it is the short closing section of Chapter 9, "The long waits that were not waits",
built on a retrospective reading of the saved decay rows (ASSUMPTIONS O109;
`scripts/read_wait_detector.py`; exploratory, no new run): the missed detections, the two
extreme waits of the third map and the fast share are tubes that changed inside the detector's
200-sweep watch, and the tail test's yardstick was bent by them. T38's pre-registered verdict
stands as scored. The author's instruction: state it and move on. The technical manuscript
carries the same reading since its revision of 10 October (its Sec. VII and Methods; the
supplement's "Retrospective reading of the saved rows"). Three long waits at λ = 1.30, N = 64
were left open; the pre-registered replay of that group (T58, the same day; ASSUMPTIONS O110)
found one more detector case and two real waits with nothing hidden, and both editions say so
in a few sentences.

**The ending, 10 October.** The edition has eleven chapters. The last, "What we have learned,
and what comes next", closes on the two papers that follow, named by their working titles in
`docs/papers/series_plan.md` ("What the burp leaves behind"; "How curled directions open"),
each teased at a high level with one measured result and no numbers, and on one line: "A push
of twelve units opens a tube. What opens a space?"

Three sets of numbers in this edition were first read from the recorded result files for it;
the first two were added to the technical manuscript on 10 October (its Sec. V and Methods) and
the third is plotted in its Fig. 2(a): the share of dots reading as tube or sheet at a quarter and
at three-quarters of the change (`results/t7_lam125_n*.csv`, `results/t7b_lam125_n*.csv`;
recorded by the pre-registered run, scored only at the half mark); the first set's count of
runs below the 70-percent rule at the half mark (0, 2, 4, 9; the manuscript quotes the second
set's 0, 1, 3, 5); and the twelve ratios in the waiting-time chart, which are the table in
ASSUMPTIONS, "The wall measured against temperature".

**Interactive companion.** The Chapter 10 figure "The box, knob by knob" links to
"The Tube's Curling Ladder", https://claude.ai/artifact/F4sBf955J5ZT7rCq8uebW8 (a private
artifact until the author shares it; source `docs/public/curling_ladder_tube.html`). It is a
paper-1 edition of the curling ladder: sliders for λ, the warmth g, the size N, the store
budget and the number of stores, with the exact numbers at any setting and the measured
results only where this paper's simulations ran. Its data are the technical paper's map table
(T8 at g = 1.5), the warmth scan (`results/cqg_tube_arrhenius_lam125.csv`), the T7 table, and
the push, reservoir and scrap counts as charted in this edition. The wider page, "The Curling
Ladder" (`docs/public/curling_ladder.html`), covers two to five directions and the ties.

**Sources, 10 October.** A source number now means the same source in both editions: sources
1 to 8 are the technical paper's reference list in its order (three of them newly cited here:
the model's founding paper, the fixed-energy method, and the published proposal of stuck
patches at λ = 1), and 9 to 12 are this edition's own.

**Web pages, 10 October.** `scripts/build_main_nerd_pages.py` turns this edition and the
technical paper into two cross-linked static pages in `docs/public/mainnerd/`, for the
author to port to sidenerdapps.com/mainnerd/ ("the Side Nerd Blog"; notes in
`docs/public/mainnerd_PORTING.md`). The text and figures on the pages are generated from
these LaTeX sources; the frame around them adds a searched question at the head of each
chapter with an answer that claims no more than the chapter does.

The technical [paper.pdf](paper.pdf) is a separate document. This edition adds no
experiments or scientific claims.

Editable source: [paper_plain_language.tex](paper_plain_language.tex).
Build from this directory with the project's Tectonic:

```sh
../../../.tools/tectonic/tectonic.exe paper_plain_language.tex
```

Its numerical statements keep the technical paper's scope: first escape is distinct from
completed conversion; local square counts are signatures, not certified geometry; store
energies are not calibrated temperatures; the three conversion maps remain inconclusive by
the letter of their rules; nothing is claimed beyond the sizes run.

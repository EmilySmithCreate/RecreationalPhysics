# Do Nobel laureates whose work is loop-shaped credit myth more often? A pre-registration

Date: 2026-11-02. Written by an assistant agent (Claude Opus 5.5) from the owner's question and prediction, before
any laureate's biography was coded. Exploratory in the sense of rule 4: a history-of-science count for the essay
`strange_loops_and_myth_draft_2026-11-01.md`, not a test of the physics hypothesis. Everything here is a design;
nothing below is a result.

## The question

The essay asked whether a culture's myths prime people for loop-shaped ideas. A first look (the companion note
`docs/reading/notes/2026-11-01_self_reference_bibliometrics.md` and the conversation of 2 November) found three
famous physicists whose loop-shaped work sits beside an explicit tie to a myth: Bohr (the taijitu on his arms,
1947), Schrödinger (Vedanta), Yukawa (Zhuangzi). Those three were found by looking for them, so they are the
reason for the question and are not evidence for any answer. The question, made countable:

> Among Nobel laureates in physics and chemistry, do those whose prize work is loop-shaped credit a myth or a
> religion as a source of their thinking more often than those whose prize work is not? And do their key mentors?

## The owner's prediction (recorded 2026-11-02, before any coding)

In her words: "I think will be more than the scientists of other fields or for Nobel prizes unrelated to loops."

Read as: the share of laureates crediting a myth or religion at level 3 or above (below) is higher for laureates
whose prize work is loop-shaped than for laureates whose prize work is not.

Her prediction for the mentors (recorded 2026-11-02, before any coding), in her words: "Probably mentors more, as
they have already translated some idea from the myth into math so the mentee may not need as strong a connection to
a myth."

Read as: mentors credit a myth or religion at level 3 or above more often than their students do; and her reason
implies a second, checkable pattern, that a student whose mentor credits a myth more often credits mathematics or
the mentor (categories 4 and 6) than the myth itself. Scored as in Step 3 under "Mentors".

## Our prediction (ours, recorded at the same time)

A small difference or none. If loop-shaped laureates come out higher, we expect most of the gap to be
documentation: the founders of quantum mechanics wrote philosophical memoirs, and most laureates did not. The
analysis below includes a check for exactly this.

## Population

All Nobel laureates in physics (231) and chemistry (202) to 2026, from the Nobel Prize API:
`https://api.nobelprize.org/2.1/nobelPrizes?nobelPrizeCategory=phy` and `...=che` (limit 100, paged), read
2026-11-02, organizations excluded (none in these two fields), 433 laureates. A laureate who won twice counts once
per prize. Chemistry is the "other field": it has some loop-shaped prizes of its own (autocatalysis, for example),
which the classification below handles the same way as physics.

## Step 1. Which prize work is loop-shaped (classified blind)

**Definition (proposed by the assistant; the owner may edit it before the classification is final).** A prize is
loop-shaped if the work its citation names has as its central object one of:

- (a) the observer or the measurement as part of the quantum description, or the meaning of the quantum state
  (including tests of entanglement);
- (b) a system whose behavior is set by its own effect on itself: self-consistency, self-interaction, self-energy,
  renormalization, autocatalysis, self-organization, self-assembly, or feedback that is the substance of the
  result (not merely a device that happens to use feedback);
- (c) cycles or self-generation in cosmology or the origin of structure;
- (d) self-reference in logic or computation.

**Procedure.** Two independent classifiers (fresh assistant agents) each see only the citation text and the year,
with no names, and the definition above. Each marks every prize LOOP or NOT, with one line of reason. Where they
agree, that is the class. Where they disagree, the prize is reported in a third group, DISPUTED, and the main
comparison is run twice, with the disputed prizes counted as loop and as not. The classification is fixed before
any biography is coded and is not revised after.

## Step 2. What each laureate and mentor credits (coded blind to Step 1)

**Sources, in this order of reading:** the laureate's biographical or autobiographical page on nobelprize.org; their
Nobel lecture; a published autobiography or memoir if one exists. Each credit is quoted with its location. A
credit that only a later biographer asserts is coded separately as "attributed", not "credited".

**What is credited (categories fixed now; the pilot may split or merge them, never after the main run starts):**

1. Myth or religion, theistic (Christian, Jewish, Muslim, other).
2. Myth or religion, non-theistic (Taoist, Buddhist, Vedantic, Confucian, Greek myth or Platonic cosmology).
3. Philosophy (named philosophers or schools, not as religion).
4. Mathematics (a theorem, a book, the beauty of mathematics).
5. A person: parent or relative.
6. A person: teacher or mentor.
7. Books: popular science.
8. Books: fiction, poetry, other literature.
9. Music or visual art.
10. Hands-on making: tinkering, radio, chemistry sets, workshops.
11. War, industrial or practical work.
12. Nothing credited (the sources say nothing about where the ideas or the engagement came from).

**Level of credit, for each item:** 1 naming (the source supplies a label only); 2 recognized afterward (the shape
is noticed in the source after the work); 3 shaped the outlook; 4 credited as the source of the idea; 5 credited
for getting them into science. Unknown is coded as unknown, never as zero.

**Mentors.** For each laureate: (i) the formal doctoral advisor, from Wikidata property P184, checked against the
Mathematics Genealogy Project (172 of 231 physics laureates have one in Wikidata on 2026-11-02); (ii) up to two
mentors the laureate names as formative in the sources above. Each mentor is coded on the same scheme from their
own sources. A mentor who is also a laureate is coded once and reused.

**Blindness.** The coders are fresh agents told only to code sources of ideas and engagement. They are not told
the hypothesis, the loop classification, or which laureates are loop-shaped.

## Step 3. Scoring the owner's prediction

**Primary measure.** The share of laureates with at least one credit in category 1 or 2 at level 3 or above.

- **HOLDS** if the loop share exceeds the not-loop share and a one-sided Fisher exact test gives p < 0.05, under
  both treatments of the disputed prizes.
- **FAILS** if the loop share is equal to or below the not-loop share under both treatments.
- **INCONCLUSIVE** otherwise.

**Said in advance:** the loop group will be small (likely 20 to 40 prizes), so only a large difference can reach
p < 0.05. An INCONCLUSIVE with the loop share higher is a likely outcome and is to be reported as exactly that.

**Checks reported beside the verdict, not changing it.**

- **Documentation.** The same comparison restricted to laureates whose sources credit anything at all (not
  category 12). If the gap vanishes there, the difference is in who wrote about their sources, not in the sources.
- **Lineages.** Laureates trained by the same mentor are not independent. The comparison is repeated with each
  mentor's students collapsed into one unit.
- **By field.** Physics and chemistry reported separately.
- **Theistic against non-theistic.** Categories 1 and 2 reported separately, for the essay's question of which
  myths.
- **Era.** Before and after 1950.
- **Mentors.** The same comparison for mentors, and whether a student credits the same category as their mentor
  more often than chance.

**Scoring the owner's mentor prediction.** Over all laureate-mentor pairs where both are coded: HOLDS if the share of
mentors with a category 1 or 2 credit at level 3 or above exceeds the share of their students, with a one-sided
paired (McNemar) test giving p < 0.05; FAILS if the mentors' share is equal or lower; INCONCLUSIVE otherwise. Her
reason ("translated into math") is checked beside it: among students whose mentor credits a myth at level 3 or
above, the share who credit mathematics or the mentor (categories 4 or 6) against the share who credit the myth
itself. Reported, not scored.

## Pilot

Thirty laureates drawn at random (Python `random.Random(20261102).sample` over the 433 in API order, names
present): Stark, O. W. Richardson, Kusch, Basov, Schrieffer, Josephson, Rainwater, R. Davis Jr., Wineland, Ashkin,
Mourou, Queloz, Hinton (physics); Ostwald, I. Joliot-Curie, Staudinger, Hinshelwood, Semenov, Eigen, Onsager,
Wilkinson, H. C. Brown, R. Hoffmann, Hauptman, Kohn, A. Suzuki, Karplus, J. Frank, F. H. Arnold, R. Robson
(chemistry). The pilot uses nobelprize.org pages only, to test whether the categories and levels can be applied
consistently. Its codes are not used in the main run: the thirty are coded again from scratch with the final
scheme. Any change the pilot forces in the categories is written here as a dated amendment before the main run.

## Prior work to search before any claim of novelty (rule 15)

Holton, *Thematic Origins of Scientific Thought* (1973; "The Roots of Complementarity"); Capra, *The Tao of
Physics* (1975); Root-Bernstein and Root-Bernstein et al. on arts avocations of laureates (2008); Zuckerman,
*Scientific Elite* (1977) on laureate lineages; Shalev, *100 Years of Nobel Prizes* (religious affiliation of
laureates). The write-up does not say this has not been counted before until a search note exists.

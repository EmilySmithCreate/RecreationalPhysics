# Self-reference in the published record: a bounded look, not a study

Date: 2026-11-01. Written by an assistant agent (Claude Fable 5.1) at the owner's request, for the essay draft
`docs/papers/essays/strange_loops_and_myth_draft_2026-11-01.md`. Everything below is **ours, unverified**. It is a
look at one database on one afternoon, with the queries written down so that the numbers can be rerun, and it is
not a study of anything. The owner's three questions, in her words: "key self referential loops in religious
mythology and the physics they focus on. europe and china are less religious, do they produce fewer publications
related to loops? where were the most successful scientists that produce related to self referential loops raised
and located?" The first question is answered in the essay; this note is about the second and third.

## (a) Works mentioning self-reference, by author country

### What was counted

OpenAlex (https://openalex.org), queried on 2026-11-01 through its public API. The search filter
`title_and_abstract.search` matches the title or the abstract of a work; the phrase search with OR is OpenAlex's own
syntax (https://docs.openalex.org/how-to-use-the-api/get-lists-of-entities/search-entities). Grouping by
`authorships.countries` counts a work once for every country that appears among its authors' affiliations, so a
work with a US and a German author counts for both. The baseline is the same grouping with no search.

Queries, exactly as run (replace `%22` with a double quote and `%20` with a space to read them):

1. Search hits by country:
   `https://api.openalex.org/works?filter=title_and_abstract.search:%22self-reference%22%20OR%20%22self-referential%22%20OR%20%22strange%20loop%22&group_by=authorships.countries&per_page=50`
2. All works by country (the baseline):
   `https://api.openalex.org/works?group_by=authorships.countries&per_page=50`
3. Search hits, total: the filter of query 1 with `&per_page=1` (read `meta.count`).
4. Search hits by field: the filter of query 1 with `&group_by=primary_topic.field.id`.
5. Search hits by language: the filter of query 1 with `&group_by=language`.

Totals: **27,004** works match the search; OpenAlex holds **329,118,719** works in all. The normalized share is
hits per 100,000 of a country's works. The `group_by` call returns the top 50 countries only, so Serbia (30 hits)
and Macao (28 hits) have no baseline here and are left out of the normalized table.

### Top 15 by raw count

| Country | Hits | All works in OpenAlex | Hits per 100,000 works |
|---|---:|---:|---:|
| United States | 3,947 | 32,298,366 | 12.2 |
| China | 1,593 | 16,489,043 | 9.7 |
| United Kingdom | 1,386 | 8,532,945 | 16.2 |
| Germany | 1,070 | 7,246,427 | 14.8 |
| Canada | 640 | 4,156,564 | 15.4 |
| Italy | 562 | 3,970,617 | 14.2 |
| Japan | 534 | 22,642,321 | 2.4 |
| France | 519 | 6,320,765 | 8.2 |
| Australia | 458 | 3,220,792 | 14.2 |
| Spain | 426 | 3,271,706 | 13.0 |
| Netherlands | 331 | 2,170,034 | 15.3 |
| Switzerland | 317 | 1,819,289 | 17.4 |
| India | 297 | 5,178,029 | 5.7 |
| Brazil | 258 | 4,048,400 | 6.4 |
| South Korea | 228 | 2,311,619 | 9.9 |

### Top 15 by normalized share (countries with at least 100 hits)

| Country | Hits per 100,000 works | Hits | All works |
|---|---:|---:|---:|
| Austria | 18.6 | 173 | 930,360 |
| Portugal | 18.1 | 149 | 823,945 |
| Israel | 18.0 | 153 | 850,067 |
| Switzerland | 17.4 | 317 | 1,819,289 |
| Hong Kong | 16.6 | 120 | 724,737 |
| Singapore | 16.5 | 104 | 630,759 |
| United Kingdom | 16.2 | 1,386 | 8,532,945 |
| Canada | 15.4 | 640 | 4,156,564 |
| Netherlands | 15.3 | 331 | 2,170,034 |
| Belgium | 15.2 | 207 | 1,361,015 |
| Germany | 14.8 | 1,070 | 7,246,427 |
| Australia | 14.2 | 458 | 3,220,792 |
| Italy | 14.2 | 562 | 3,970,617 |
| Spain | 13.0 | 426 | 3,271,706 |
| Denmark | 12.3 | 136 | 1,103,865 |

The United States sits at 12.2 per 100,000, below all fifteen of these. China sits at 9.7, Japan at 2.4.

### What the hits are about (query 4)

Arts and Humanities 5,543; Psychology 4,481; Physics and Astronomy 3,534; Social Sciences 3,152; Computer Science
2,901; Neuroscience 2,010; Engineering 1,512; Medicine 959; Mathematics 602. So the brief's expectation that
mathematics and computer science dominate the term is **wrong for this search**: the humanities and psychology
lead, and much of the physics and engineering count is almost certainly "self-referential" in the instrumental
sense (self-referenced interferometry, self-referencing frequency combs, self-referential sensors), which has
nothing to do with loops of meaning. Nobody has read the hits; this is a guess from the field labels.

### Language (query 5)

English 25,181 of 27,004 (93 %). Spanish 322, German 292, Portuguese 215, French 194, Italian 133, Chinese 85,
Japanese 80. The search terms are English, so a Chinese paper about 自指 (self-reference) with no English abstract
is invisible to it.

### Confounds, plainly

1. **English-language bias.** The terms are English and 93 % of the hits are English. Countries that publish in
   English, or whose journals carry English abstracts, are over-counted; China and Japan are under-counted by an
   amount nobody here has measured. Japan's 2.4 per 100,000 is the clearest symptom.
2. **OpenAlex coverage.** OpenAlex indexes what it can find; its coverage of humanities monographs, Chinese-language
   journals and older work is uneven, and the baseline (all works) is affected differently from the search hits.
3. **Field mix.** A country whose output is mostly medicine and materials science will score low on any humanities
   term whatever its culture. Normalizing by all works does not fix this; normalizing by humanities output would be a
   start and was not done.
4. **The term is not the idea.** "Self-reference" in a title catches Gödel scholarship, narcissism scales in
   psychology, self-referential encoding in memory research, and laser metrology. It misses most work on strange
   loops in physics, which is written in the vocabulary of observers, measures and participatory universes.
5. **Multi-author counting.** Each work counts once per author country, so collaborative countries gain.
6. **Religiosity is not in the data.** Nothing in OpenAlex says anything about belief. If the share by country is
   set beside a religiosity measure, the only standard one used here is the Pew Research Center's 2018 comparison of
   religious commitment by country (share saying religion is very important, weekly attendance, daily prayer):
   https://www.pewresearch.org/religion/2018/06/13/how-religious-commitment-varies-by-country-among-people-of-all-ages/
   Its figures, as read on 2026-11-01: United States 53 % say religion is very important, 55 % pray daily; China 3 %
   and 1 %; across Europe the average country has 23 % saying religion is very important and fewer than one in four
   praying daily. Pew notes that attendance and prayer are poor measures for Buddhist, Hindu and East Asian
   traditions, which weakens any reading of China's number.

### What the two numbers say when set side by side, suggestive only

The owner's guess was that less religious places might publish less about loops. On this one measure the opposite
direction appears: the United States, the most religious of the large research countries on Pew's measures, has a
**lower** normalized share (12.2) than Austria, Switzerland, the United Kingdom, the Netherlands, Belgium, Germany or
Denmark, all of which Pew places well below it in religious commitment. China is low (9.7) but is also the country
most damaged by confound 1, and Israel is high (18.0) with a very different religious profile. Given confounds 1
to 4 this is **not evidence either way**. The honest sentence is: the look does not support the guess, and it is not
good enough to refute it.

## (b) Fifteen people associated with self-reference: where born, raised, worked; religious upbringing

**Criterion for the list.** The people a standard reference on self-reference names: the Stanford Encyclopedia of
Philosophy entry "Self-Reference" (https://plato.stanford.edu/entries/self-reference/) and Hofstadter's *Gödel,
Escher, Bach* (1979) and *I Am a Strange Loop* (2007) together cover Gödel, Turing, Tarski, Russell, Kleene,
Smullyan, Barwise and Etchemendy, Escher and Hofstadter himself; the systems and biology branch (Luhmann, Maturana
and Varela, Bateson, Spencer-Brown) is the standard lineage of "autopoiesis" and "second-order cybernetics";
Lawvere's fixed-point theorem is the category-theoretic form of the diagonal argument; Wheeler's "self-excited
circuit" is the physics entry. This is a reading list, not a ranking by citations, and "most successful" was not
measured; the owner's phrase is read as "most associated with the idea."

Every cell is from the English Wikipedia page named in the last column, read on 2026-11-01 by an assistant agent, or
is marked "not found" (meaning the page does not state it; a fuller biography may). "Raised" is the childhood home
where the page gives one.

| Person | Born | Raised | Worked (main places) | Religious upbringing, as the page states it | Source |
|---|---|---|---|---|---|
| Kurt Gödel (1906 to 1978) | Brünn, Austria-Hungary (now Brno) | Brünn; Lutheran elementary school there | Univ. of Vienna; Institute for Advanced Study, Princeton | Catholic father, Protestant mother, children raised Protestant; described himself as a "baptized Lutheran" belonging to no congregation; a theist "following Leibniz rather than Spinoza"; read the Bible on Sunday mornings | https://en.wikipedia.org/wiki/Kurt_G%C3%B6del |
| Alan Turing (1912 to 1954) | Maida Vale, London | Southern England (Hastings, St Leonards-on-Sea, with a retired Army couple while his parents were in India; Guildford from 1927) | King's College Cambridge; Bletchley Park; National Physical Laboratory; Univ. of Manchester | Not found (page does not state the household's religion); page notes speculation that Christopher Morcom's death led to his atheism, and early writings about a spirit surviving death | https://en.wikipedia.org/wiki/Alan_Turing |
| Alfred Tarski (1901 to 1983) | Warsaw | Not found (schooled in Warsaw) | Univ. of Warsaw; Harvard; City College NY; IAS; UC Berkeley | Born to Polish-Jewish parents; converted to Roman Catholicism in 1923 with his brother; an "avowed atheist" | https://en.wikipedia.org/wiki/Alfred_Tarski |
| Bertrand Russell (1872 to 1970) | Trellech, Monmouthshire, Wales | Pembroke Lodge, Richmond Park, London, by his grandparents | Trinity College Cambridge; LSE; Univ. of Chicago; UCLA; Beacon Hill School | Father a deist whose will asked that the children be raised agnostic; grandmother, of Scottish Presbyterian family, had the will set aside and raised him religiously conservative; he became an atheist at 18 | https://en.wikipedia.org/wiki/Bertrand_Russell |
| Stephen Kleene (1909 to 1994) | Hartford, Connecticut | Not found | Univ. of Wisconsin-Madison (nearly all his career); IAS; Amherst | Not found | https://en.wikipedia.org/wiki/Stephen_Cole_Kleene |
| Raymond Smullyan (1919 to 2017) | Far Rockaway, Queens, New York | Far Rockaway, then Manhattan (family moved in the Depression) | Dartmouth; Princeton; Yeshiva Univ.; Lehman College and CUNY Graduate Center; Indiana Univ. | Family described as Ashkenazi Jewish; upbringing not found; a Taoist who wrote several books on Taoist philosophy | https://en.wikipedia.org/wiki/Raymond_Smullyan |
| Douglas Hofstadter (born 1945) | New York City | Stanford University campus, California (father a physics professor); a year at the International School of Geneva | Indiana Univ. Bloomington (since 1977); Univ. of Michigan | Not found (page says nothing of the parents' religion or his) | https://en.wikipedia.org/wiki/Douglas_Hofstadter |
| M. C. Escher (1898 to 1972) | Leeuwarden, Netherlands | Arnhem (from 1903) | Rome (1923 to 1935); Switzerland; Brussels; Baarn, Netherlands (1941 to 1970) | Not found | https://en.wikipedia.org/wiki/M._C._Escher |
| F. William Lawvere (1937 to 2023) | Muncie, Indiana | A farm outside Mathews, Indiana | Reed College; ETH Zurich; Univ. of Chicago; Dalhousie; Univ. at Buffalo | Not found | https://en.wikipedia.org/wiki/William_Lawvere |
| G. Spencer-Brown (1923 to 2016) | Grimsby, Lincolnshire | Not found (Mill Hill School, London) | Christ Church Oxford; Univ. of London; Cambridge; visiting posts in Australia and the US | Not found | https://en.wikipedia.org/wiki/G._Spencer-Brown |
| Niklas Luhmann (1927 to 1998) | Lüneburg, Germany | Lüneburg (the family house and brewery) | Lüneburg administration; Speyer; Münster; Bielefeld Univ. (until 1993) | Not found | https://en.wikipedia.org/wiki/Niklas_Luhmann |
| Humberto Maturana (1928 to 2021) | Santiago, Chile | Not found (schooled in Santiago) | Univ. of Chile; Harvard; MIT; University College London | Not found | https://en.wikipedia.org/wiki/Humberto_Maturana |
| Francisco Varela (1946 to 2001) | Talcahuano, Chile | Not found (Liceo Alemán del Verbo Divino, Santiago, a Catholic school by its name; the page does not say more) | Univ. of Chile; École Polytechnique; Univ. of Paris; CNRS | Upbringing not found; practiced Tibetan Buddhism from the 1970s | https://en.wikipedia.org/wiki/Francisco_Varela |
| Gregory Bateson (1904 to 1980) | Grantchester, Cambridgeshire | Not found (Charterhouse School) | Cambridge; fieldwork in New Guinea and Bali; Palo Alto; UC Santa Cruz | Family atheist "for several generations"; a lifelong atheist | https://en.wikipedia.org/wiki/Gregory_Bateson |
| Jon Barwise (1942 to 2000) and John Etchemendy (born 1952) | Independence, Missouri; Reno, Nevada | Not found; not found | Stanford (CSLI) for both; Barwise also Yale, Wisconsin, Indiana; Etchemendy also Princeton | Not found; not found | https://en.wikipedia.org/wiki/Jon_Barwise and https://en.wikipedia.org/wiki/John_Etchemendy |
| John Archibald Wheeler (1911 to 2008) | Jacksonville, Florida | Youngstown, Ohio (a year on a farm in Benson, Vermont) | Princeton (1938 to 1976); Univ. of Texas at Austin; Manhattan Project sites | Upbringing not found; he and his wife were founding members of the Unitarian Church of Princeton | https://en.wikipedia.org/wiki/John_Archibald_Wheeler |

Read across the table: 7 born in the United States, 4 in Britain, 2 in Chile, 1 each in Austria-Hungary, Poland,
the Netherlands and Germany. Almost all worked for long stretches in the United States or Britain, which is where the
twentieth century's logic departments were, so the location column measures where the jobs were more than where the
ideas came from. Religious upbringing is stated for 5 of the 16 people, and those five run the whole range: a Lutheran
theist (Gödel), a Jewish family converting to Catholicism and an atheist son (Tarski), a Presbyterian grandmother
overriding an agnostic will (Russell), a family atheist for generations (Bateson), a Jewish family and a Taoist
(Smullyan). No pattern can be read from five, and a Wikipedia page's silence on religion is not evidence of a secular
home.

## (c) Verdict

**What the look supports.** That "self-reference" as a title word is spread across the research world roughly in
proportion to each country's output, with the small, English-publishing, high-output-per-head countries of northern
and central Europe, plus Israel, Hong Kong and Singapore, at the top of the normalized list, and the United States in
the middle. That the standard names in self-reference were born mostly in the United States and Britain and worked
almost entirely there, which is also where the field's departments were. That the religious homes of those people,
where known, were of every kind.

**What it does not support.** Any statement about religiosity and loops in either direction. The owner's guess (less
religious places, fewer loop papers) is not borne out by the normalized share, but the measure is too confounded to
refute it, and the people table is too small and too thinly sourced to say anything about upbringing. Nothing here
bears on the essay's actual claim, which is about how early a culture installs a self-referential loop in its
children; that is a developmental and anthropological question, not a bibliometric one.

**What a real study would need.** (1) A concept-based rather than term-based corpus: a hand-coded sample of hits to
estimate what share concerns loops of meaning, and search terms in Chinese, Japanese, German and Spanish. (2)
Normalization by field (humanities and theoretical physics output per country), not by all works. (3) Fractional
author counting and first-author country. (4) A religiosity measure matched to the authors' generation and place of
upbringing, not today's national average. (5) For the people table, full biographies rather than encyclopedia pages,
and a list chosen by a measurable criterion (citations to a defined set of works, or appearance in a defined set of
reference entries) rather than by the agent's judgement. (6) A pre-registered prediction before any of it is run,
under the programme's own rules.

## Rerun

The four JSON responses were saved in the agent's scratchpad and are not part of the repository; the URLs above
reproduce them. OpenAlex's counts change as the index grows, so a rerun on another day will differ in the last digits.
Requests without an API key share a small daily budget per network; a free key (https://openalex.org/settings/api)
removes the limit.

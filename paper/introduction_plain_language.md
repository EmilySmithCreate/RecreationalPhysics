# Where does "where" come from?

*A plain-language introduction. Draft 2 (2026-09-20). It describes an idea and how we are testing it, not what we have found. There are no findings yet; the current state is in the README.*

*What changed from Draft 1: the author pointed out that the picture of the "before" given there (anyone can call anyone, no geometry, mess without limit) is the simplest published model's picture, not hers. Draft 2 says whose picture is whose, gives hers, and describes the question the project now asks. Draft 1's own question, about contact lists, is parked and summarised near the end.*

## The stage nobody questions

Almost every picture of the universe starts with a stage. Things happen *somewhere*. One place is near another place and far from a third. Even Einstein's general relativity, which lets the stage bend and stretch, still begins with a stage: space and time are the raw material, and physics describes what they do.

The standard history of the universe is told on that stage. About 13.8 billion years ago space was hot and dense, it expanded, and it cooled. Most cosmologists add an earlier chapter called inflation, a burst of extremely fast expansion that smoothed everything out. That story is well supported by evidence and nothing in this project disputes it.

What the standard story leaves alone is the stage itself. Why is there such a thing as "near" and "far" at all?

## A different starting point

A number of physicists take seriously the idea that space is not a basic ingredient. It may be something that *forms*, the way ice forms from water. This is a research direction, not an accepted fact, and nobody has made it work completely. Our project sits inside one small, concrete corner of it.

## The simplest published picture

Imagine a very large crowd of people, each holding a phone. At the start anyone can call anyone. There is no such thing as a neighbour, because everybody is one call away from everybody else. Asking "how far apart are these two people?" has no useful answer. In this picture the world before space has lots of relationships and no geometry.

Now suppose calls cost effort, and small closed loops of friends (you call her, she calls him, he calls you) are rewarding. As the crowd calms down, people keep only a few contacts, and the rewarding loops knit together into something like a net. In the net, some people are two steps away and others are two hundred. Distance has appeared. Nobody put it in. It came from the pattern of who is connected to whom.

The physicists who proposed this kind of model in 2006 gave the moment of knitting-together a name: **geometrogenesis**, the birth of geometry. In this picture the Big Bang is less like an explosion in space and more like a change of state, as when steam becomes water.

This simplest version has a difficulty that its own authors found. Think about seating a party. With ten guests there are a manageable number of ways to be disorganised. With ten thousand guests who may each talk to *anyone*, the number of messy arrangements explodes far faster than the crowd grows, and disorder wins by sheer weight of numbers. In the model, the bigger the universe, the colder it must get before space can form, and for an endlessly large universe it never forms at all. Remedies have been suggested (a finite universe, rules that strengthen as the universe grows, long-range forces that discourage mess), each with a cost.

## The picture this project starts from

The author's picture of the "before" is different, and the difference is the point of the project. We call the "before" **X**.

X is not a free-for-all. Think of a club with rules, not an endless crowd: a fixed number of members; each may make only so many calls a day; only so many of those may be repeat calls; an unanswered call costs more than a completed call earns, so everyone answers. Under rules like these there is a best way to arrange the calls, and the club settles into it. That settled arrangement is X. It is specific and stable. It may well have a shape of its own, its own kind of near and far, perhaps with a different number of dimensions from ours. The ingredients need not be endless, and they need not be free.

Then something in the arrangement gives way. A member leaves, two calling circles merge into one, a newcomer arrives, and the old best arrangement is no longer the best. The club reorganises into a new arrangement that is more stable than the old one, and the reorganisation brings a kind of reward that did not exist before. In the analogy, that new kind of reward is spacetime.

So the ingredients can be few and bound by rules. They can stretch, combine or collapse, and each such change alters what is best for all the others. The hypothesis is that a change of that kind can produce the geometry we live in. The nearest everyday comparison is a chemical reaction: something that is stable for now, but not the most stable thing available, rearranges into something more stable and gives off energy as it does.

This is a hobbyist's hypothesis. No physicist has reviewed it. It is written out, claim by claim, in `VISION.md`.

## The part that can be checked

One part of the picture can be tested on a computer today. Changes of state come in two kinds. Some are abrupt, like water freezing: the two states are distinct, and a definite lump of energy is given off at the changeover. Others are gradual, like butter softening: no sharp moment, no lump of energy.

The hypothesis needs the abrupt kind, because the lump of energy is its candidate for where matter and radiation came from. If the change that forms geometry turns out to be gradual in every model where it can be measured, that part of the hypothesis has nowhere to live.

We have not built a model of X. We start with a published model by Carlo Trugenberger and colleagues, in which the energy is a network version of the quantity that general relativity is built on. Its published results say the change is gradual in the full model, and abrupt in a simplified one, where the network breaks into small closed pieces instead of forming a space. Our first job is to reproduce those published results. That is a matter of respect for the people who did the work first, and it is the only way to show that we understand their mathematics before we say anything of our own. Only then do we ask our question: which ingredients of the energy make the change abrupt, which make it gradual, and can any setting give an abrupt change *and* a connected space?

One limitation is stated up front. In that model the "before" is a random network, which is a closer relative of the free-for-all than of the club with rules. So it can tell us whether geometry can form abruptly out of randomness. It cannot, as it stands, tell us whether a rule-bound X would do so.

## An earlier version of the question (parked)

Draft 1 of this page asked something else: what if each person's phone only ever held a short contact list? We expected random short lists to tame the mess but leave nothing to knit with, and lists with local pattern to let the net form at an ordinary temperature however large the crowd. If so, **you cannot get geometry from nothing; you can get it from a richer, more tangled geometry that settles into a simpler one.** That is an expectation from an argument, never simulated by us, and the study is parked (`docs/parked/`). Its spirit carries over: the "before" has structure.

## What this is and is not

This is a toy model on a computer, with a few hundred to a few thousand points. It does not contain time as we experience it, or quantum behaviour, or matter. It cannot tell us whether the real universe began this way. What it can do is show whether a mechanism is possible or impossible inside a family of models, in a setting small enough that anyone can rerun every number.

That is why all of the code, every assumption and its source, and the predictions written down *before* the runs that test them are published alongside this text. Results that go against the hypothesis are reported as prominently as results that favour it.

---

*Sources. The hypothesis, claim by claim, with its published ancestors: `VISION.md`. Every assumption and how far it has been checked: `ASSUMPTIONS.md`; bibliography: `REFERENCES.bib`. "Geometrogenesis" and the phone-network-like model: Konopka, Markopoulou and Smolin (2006). The disorder problem and the suggested remedies: Konopka (2008); Chen and Plotkin (2013). The model now used and its published results: Kelly, Trugenberger and Biancalana (2019); Trugenberger (2025). The contact-list argument: `ASSUMPTIONS.md` B1–B5, C1–C4. Age of the universe: Planck Collaboration 2018 results, still to be added to the bibliography. The club-with-rules analogy is the author's, tidied by the assistant.*

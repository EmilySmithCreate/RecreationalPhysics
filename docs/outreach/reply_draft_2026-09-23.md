# Draft reply to Carlo Trugenberger, updated 2026-09-23 (not sent)

Replaces `reply_draft_2026-09-22.md`, which was never sent. Written after his postscript arrived, after
N = 196 finished in both protocols, and after the Fig. 3 check. Everything to attach is in
`for_carlo_2026-09-22/` (pictures 1, 2 and 4, the table); `email_reply_2026-09-23.txt` there is this
letter as plain text. The repository is public, so the zip link works. Nothing here is about the
hypothesis, the loop or the public pages, and his email stays private.

---

**Subject:** Re: Reproducing your model: your postscript reproduced at N = 196, pictures attached, and one question about Fig. 3

Dear Carlo,

Thank you for the reply and for the postscript, which turned out to be exactly what our runs show. I
should say plainly what I am: a software engineer doing this as a hobby, keeping to the reproduction
of your model, where I can be useful to you. Pictures are attached this time rather than links, and my
home-made words are translated into yours below.

**Your postscript, at N = 196 (p = 7).** Two protocols have finished at this size, on the full
Hamiltonian with only the hard-core restriction (picture 4). The first is your procedure as you
described it: 40 couplings from g = 12 to 1.5, each starting from the previous coupling's final graph,
240 sweeps of warm-up and 10,000 measured sweeps per coupling, cooling from a random graph and then
heating from the lattice torus, four independent chains each way. The second is replica exchange from a
random graph, 20 couplings from g = 9 to 2.2, 100,000 sweeps, with every replica making 5 to 15 round
trips between the hot and cold ends. The result is what you suggested: on heating, the lattice survives
past the transition and collapses between g ≈ 3.5 and 2.7, in three chains of four, with the heating
curve up to 0.16 above the cooling curve there; the cooling curve agrees with replica exchange to 0.004
at every coupling; replica exchange gives one smooth curve and no jump anywhere. So at this size the
jump is the metastable lattice branch, and it appears in a faithful copy of your procedure. I will send
484 and 676 as pictures when they finish.

**One question about Fig. 3 of the review, in case it is useful to you.** Fig. 3 sits above Fig. 8a of
the 2019 paper in *both* directions, cooling from random as well as heating from the lattice, by up to
0.4 across the whole transition, and its rise is at g ≈ 6 where Fig. 8a's is at g ≈ 5. Trapping on
descent would keep the random phase and put the cooling curve *below* equilibrium, and our copy of your
procedure shows no departure on descent at all. Our runs match Fig. 8a to 0.005 and Fig. 3 at both ends
(picture 2), so the difference is confined to the middle stretch. Could Fig. 3 have been made at a
different size, or with the coupling normalised differently?

**A difficulty at the larger sizes, and a question about your code.** At N = 484 (p = 11) replica
exchange with single edge switches, 30 couplings from g = 7.5 to 2.0 and 128,000 sweeps, makes no round
trips at all: the cold end freezes. From a random start the coldest replica reaches S/N = 0.955; from
the lattice torus it stays at 0.999; the two never meet. Do you use the neighbourhood-swap move of
Fig. 8 of the review at N = 1024, and did you find single switches insufficient at low coupling? If so
I will build that move before trusting anything at 484 and 676.

**What I meant by my words.** "Flat sheet" is the lattice torus. "A torus with one side curled to
length 4" is the 4 × L lattice torus (picture 1): its short direction is a 4-cycle, so every
wrap-around loop of four is itself a square and the edges along it lie in three squares instead of two.
"Hard cap" was my reading of Sec. 4 of the 2019 paper, that the simulations ran on the space with no
edge carrying more than d − 2 squares; if that restriction was never in the code, I misread the
sentence, and everything I compare with your figures uses the full Hamiltonian with the hard-core
restriction, as in yours. The 14-vertex graph was a remark about the global-term-only case, where the
network breaks into pieces with three squares on every edge as in Gorsky and Valba's simulations, and
where the incidence graph of the 7-point biplane ties with the 4-cube per vertex; it says nothing about
the lattice ground state.

**Something that may be useful for your new code.** At N = 18 we listed every valid graph exhaustively
(about 1.8 × 10¹² labelled graphs in 26 classes), so the averages there are exact sums. The attached
table gives ⟨S⟩/N at seven couplings for the full Hamiltonian, with the assumptions stated; any code
sampling the same ensemble should land on those numbers, and ours does to 0.03 %. The whole code and
every result file can be downloaded as one zip without a GitHub account:
https://github.com/EmilySmithCreate/RecreationalPhysics/archive/refs/heads/main.zip

**One observation about the 4 × L torus, offered in case it touches your allotropes.** With the local
term's coefficient raised to 1.25 and g = 1.5, the 4 × L torus is metastable: it sits for thousands of
sweeps and then opens into the lattice torus, releasing exactly 1 per vertex. In almost every run one
column stays curled: a 4-cycle whose four edges still carry three squares, at 4, 9 or 14 units above
the lattice depending on how many neighbouring edges keep a third square, and it never anneals away at
this coupling. If that object is close to what you call an allotrope, I would be glad to know; if it is
not, please ignore this paragraph.

On my second question, sorry for the confusion: I was asking whether anyone had measured how the
transition moves with N, since the curves in Fig. 8a for N = 100 to 200 do not lie on top of one
another. Your answer, that no finite-size scaling has been derived, answers it.

With thanks, and with real appreciation for your time,

Emily Smith

---

## For Emily: what changed since the 22 September draft, and why each paragraph is there

Read this before sending. If any line is not something you would say yourself, cut it.

- **The postscript paragraph** is the most useful thing we have: his own guess, confirmed in a faithful
  copy of his method, with the numbers. It replaces the 22 September draft's two questions about his
  1024-node runs, which his postscript has already answered.
- **The Fig. 3 paragraph** asks the one question the check left open (ASSUMPTIONS O27). It says where
  we agree with him first, so it reads as help rather than complaint. Cut it if the letter feels long;
  it can wait for his next reply.
- **The 484 question** is new and honest: our sampler is stuck at 484, and he may have solved exactly
  this. "Round trips" are graphs that travelled from the hottest coupling to the coldest and back. If he
  says the neighbourhood-swap move is needed, that decides our next piece of work.
- **The vocabulary paragraph** is the 22 September content compressed: his words for ours, the cap
  admission, the 14-vertex clarification. Picture 1 is the one that shows the tube.
- **The benchmark table** is unchanged: a check that costs him nothing.
- **The allotrope paragraph** is optional and is the only new thing that touches our own track. It is
  about his concept applied to his model, not about the hypothesis, and it is phrased so that "ignore
  this" is a fine answer. Cut it if you would rather keep the first exchange purely to reproduction.
- **Not in the letter:** anything about the hypothesis, the loop, rung 0 or the public pages. His email
  is private and is paraphrased in `correspondence_2026-09-22_trugenberger.md`; never quote it publicly.

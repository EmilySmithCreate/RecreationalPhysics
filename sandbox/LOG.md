# Sandbox log

One line per look: the date, the question, what was seen. Nothing here is cited, scored or evidence (CLAUDE.md rule
16). A look can narrow or withdraw a claim at once; to support one it has to be promoted onto fresh data.

- 2026-10-11. Is a replica that reads OPENS by the count wide flat space? Read saved end states of T48, T53, T56 by
  their distance shells (`scripts/read_open_shells.py`). About a third are the start glued together differently.
  Made before this lane existed and recorded as O116.
- 2026-10-11. How wide is the flat torus a tube ends on? Read saved end states of T8, T23, T24, T60
  (`scripts/read_endpoint_width.py`). Six around in 9,858 of 9,865; the tube with its seam shifted by two. Narrowed
  piece 1's picture at once (O116). To be claimed in paper 1 it stands as an exact count with a tested script.
- 2026-10-11. Of all the flat tori of N points, how many are six around? Counted (`sandbox/flat_torus_widths.py`,
  checked against built graphs at 64 points): 17 % at 64 points, 8.5 % at 192, 5 % at 288, 0.8 % at 1,024, 0.2 % at
  4,096; the median width grows like the square root of N. Six around is the nearest flat state, not the usual one.
- 2026-10-11. Does a six-around torus widen if kept warm? (`sandbox/warm_width.py`; 96 points, 40,000 sweeps, 4
  replicas.) At g = 2.0 and 2.5 it stays six around. At 3.0 and 3.5 it is damaged, and a fast cool does not give
  back a flat torus.
- 2026-10-11. Disordered at g = 3.5, then cooled slowly (`sandbox/anneal_width.py`; 96 points, 8 replicas, cooled
  over 4,000 and over 40,000 sweeps). None ends exactly flat (32 to 97 units left). The most points at one distance
  is 10 to 20, against 8 for a tube: wider than a tube, with flaws. Flaws inflate that number, so it is not a width.
- 2026-10-11. Are the big "sheets" tubes too? Saved end states of T37 and T51 (256 to 4,096 points, opened from
  several places): in most, 9 points at one distance and the far end half the tube's length away. Tubes six around.
  Some T37 tubes of 1,024 points and more have far larger shells (far links or melting; O88, O95).
- 2026-10-11. What does the three-direction slab become when its curled direction is opened everywhere by T54's
  construction? Exactly flat, every point at d = 3, and its shells are the slab's, one step fatter: a slab six thick.
- 2026-10-11. If the burp's heat stays, does the tube end wider? Sealed tubes of 96 points at lambda = 1.25 with 2
  down to a quarter of a store per point, then drained and cooled (`sandbox/burp_heat_width.py`, 8 replicas each).
  With one store per point or more: clean tubes six around, most with one column left curled. With fewer: a few
  end with flaws and more points at one distance. No clean flat end state wider than six.
- 2026-10-11. The same at lambda = 1.40 and 1.50, at 192 points, and with a slower drain. More heat per point
  leaves 16 to 108 units of flaws and none exactly flat.
- 2026-10-11. Those flawed end states read point by point (`sandbox/burp_heat_room.py`): at lambda = 1.40 with a
  third of a store per point, 12 to 45 % of points see an endless sheet out to three steps; in a tube none does.
  A patchwork, wider in places. Promoted the same day as T61, on fresh seeds and with a held-out size.
- 2026-10-11. Disordered and cooled ten times more slowly than before (400,000 sweeps; started before T61 was
  registered, finished after). Still none exactly flat: 26 to 61 units of flaws stay. Not a tube any more, and not
  a clean wide torus either.
- 2026-10-11. Energy comes in and cannot leave (`sandbox/feed_energy.py`; sealed tube of 96 points, one store per
  point, energy added to a random store every 100 sweeps for 40,000 sweeps, then drained and cooled to be read;
  4 replicas each). Slow feed (2 units per point in all): three of four end as the tube six around with one curled
  column or a small flaw, one as a patchwork. Faster feeds (8 and 33 per point in all): the graph melts while it is
  fed (0.2 to 0.7 squares per point) and ends as a patchwork, 28 to 64 % of points seeing a sheet to three steps,
  none exactly flat. The same at lambda = 1.40.
- 2026-10-11. The owner's question: what if the energy can only curl and uncurl? The same feed with every move that
  only breaks squares refused (mode "curl"). Slow feed: two of four end exactly flat and six around, two with one
  curled column. Faster feeds: it still melts (moves that change the curl break squares too) and ends as a
  patchwork, 23 to 54 %, none exactly flat. No wider clean torus either way.
- 2026-10-11. What is a patchwork made of? (`sandbox/patchwork_census.py`, on T61's stage-1 end states at
  lambda = 1.40, read point by point.) About nine points in ten sit in flat surroundings (d = 2). The rest are a
  few points still curled (d = 1, in fours) and a few "too open" (d = 3, in fours and eights). Away from those, a
  point sees the space as six, eight, ten or more around depending on where it stands. Points near a too-open
  flaw see more points than a flat sheet has, so the larger numbers overstate the width.
- 2026-10-11. A NEW RULE, not the toy's: a price mu on every loop of six beyond the 2N a wide flat sheet has
  (`sandbox/six_loop_cost.py`). Priced exactly at 48 points: the tube six around then sits 2.5 mu per point above
  a wide torus, and its cheapest way out costs 20 at mu = 0, 16 at mu = 1.5, nothing at mu = 2. Run at 96 points
  (mu = 1.5 to 2, g = 0.5 to 1.5, with and without slow cooling): it leaves six around every time and ends flawed,
  never flat, with 5 to 18 % of its squares missing. This form pays for having fewer six-loops than a sheet, so
  it pays for breaking squares.
- 2026-10-11. The same idea link by link, saturating as the toy's own rule does: mu times (six-loops through a
  link, less 6) where positive (`sandbox/six_loop_edge.py`). A torus eight around costs nothing and is stuck;
  six around costs 15 mu per point. At mu = 0.25, g = 1.5 it stays six around for 6,000 sweeps (5 of 5). At
  mu = 0.30, g = 1.2 it leaves in 6 of 7 and ends with 32 to 117 units of flaws, 29 to 69 % of points seeing a
  sheet to three steps: a patchwork again, none flat. Where the way out is cheap enough to find (about 12), the
  release is 4.5 per point, four times the tube's at lambda = 1.25 and past where the tube itself breaks up.
- 2026-10-11. An end state of T61 that was flat and still uneven turned out to be two separate pieces, one of them
  one-sided (a Klein bottle). Promoted the same day as an exact reading by a tested script
  (`scripts/read_flat_kind.py`; ASSUMPTIONS O116, last addendum).
- 2026-10-11. Can a patchwork become flat? (`sandbox/heal_patchwork.py`: the 24 WIDE end states of T61's stage 1
  at lambda = 1.40, 96 points, held at g = 2.0 for 100,000 sweeps and cooled over 100,000.) Three end exactly
  flat, and those are six around again (one) or uneven (two: separate pieces or one-sided). The other 21 keep 16
  to 50 units of flaws; about as many see less sheet afterwards as see more. Healing leads back to six around,
  not on to a wide torus.
- 2026-10-11. The second heal look, held at g = 2.5 (100,000 sweeps, cooled over 200,000): the same. None of the
  24 ends as a wide flat torus.
- 2026-10-11. Does supplied energy curl flat fabric back up? (`sandbox/feed_energy.py`, START twist: the tube
  already re-glued, flat and six around, 96 points, fed for 40,000 sweeps, 4 replicas each.) Energy that can only
  curl or uncurl, 2 units per point in all, twice the price of curling the whole tube: nothing moves at all, in 4
  of 4; the energy sits in the stores. Four times as much: the fabric melts (0.77 squares per point) and the curl
  it gains is 1 to 6 % of a curled tube's. With every move allowed: the same. Supplied energy breaks; it does not
  curl.
- 2026-10-11. NEW RULE (`sandbox/six_loop_push.py`): a gentle price on loops of six, link by link, with the first
  move made by hand. Exact at 48 points: after that push (4 squares broken, cost 64 − 176 mu) there are moves
  that keep every square and remove six-loops, all downhill, and ten times as many ways forward as back. Run at 96
  points, mu = 0.10, g = 0.8, 3,000 sweeps, 6 replicas: none fell back; never more than 5 squares missing at a
  time, so a moving defect and not a melt; one finished exactly flat with no six-loop left and every point seeing
  a sheet to three steps, and it is one-sided (a Klein bottle); one more flat and one-sided with a quarter of its
  six-loops left; four still under way. Colder (g = 0.4) none finished. At mu = 0.15 five of six ended flawed.
- 2026-10-11. The same push, run five times longer (15,000 sweeps, 8 replicas each; `sandbox/out/push_long_*`).
  mu = 0.10, g = 1.0: one fell back at once; **one finished as an exactly flat torus twelve around** (no six-loop
  excess left by sweep 755, every point seeing a sheet out to five steps, never more than 5 squares missing on
  the way); six still held 8 to 79 units of flaws. g = 0.8: one finished flat and one-sided, eight or more around;
  one flat and one-sided with a quarter of its six-loops left; six with 32 to 63 units of flaws. mu = 0.05,
  g = 0.8: none finished; one fell back; the others sat at 28 to 48 units. One state, 8 units left and three
  quarters of its points seeing a sheet, turned up three times. Two clean finishes in sixteen at mu = 0.10: the
  first clean wide shape the toy has made from a tube by any route. One replica; a new rule; pushed by hand.
- 2026-10-11. The explainer page "Patches and melting" was drawn from five real states (`sandbox/patches_page.py`).
  Reading their numbers corrected an explanation of ours: T61's patchworks were never melted. The fewest squares
  per point in the sealed spell was 0.92 to 0.99. Warm fabric with flaws in it, not a melt that froze. Yet most
  of their links join dots that started far apart: the dots trade neighbors while the squares stay.
- 2026-10-12. Can part of a patchwork be flat on its own? (`sandbox/no_melt.py pieces`, on T61's end states at all
  three sizes, all read.) Of 213 end states that are not flat as a whole and are in two or more pieces, 124 have
  at least one piece that is exactly flat by itself: 117 such pieces are tori six around, 2 are tori eight
  around, and 16 are one-sided. So parts of a patchwork do close up as clean small tori, nearly always narrow.
- 2026-10-12. "What if melted isn't a thing?" (`sandbox/no_melt.py heal`: the 24 mostly-wide end states of T61 at
  lambda = 1.40, 96 points, run with a ceiling on the energy so that flaws can wander and cancel and the fabric
  can never gain more than about one flaw; 200,000 sweeps.) Still running when this was written; of the first six
  at each of three settings, one or two healed to exactly flat, as separate small pieces (tori six around, one
  eight around, and one-sided ones). Promoted the same day in a different form: the exact floor on squares in a
  sealed run (O123).
- 2026-10-12. The no-melt look finished (`sandbox/out/nomelt_*`; 24 mostly-wide patchworks each). With a ceiling
  of 16 above the lowest energy reached, at g = 2.0: 2 of 24 healed to exactly flat, both as separate small pieces.
  With a ceiling of 32: 3 of 24, and **one of them is a single clean torus eight around** (96 points); the other
  two are pieces. With a ceiling of 32 at g = 3.0: 1 of 24, in pieces, one of them a torus eight around. The
  rest kept their flaws through 200,000 sweeps. So with melting ruled out a patchwork usually stays a patchwork;
  now and then its flaws cancel, and what is left can be wider than six.
- 2026-10-12. **A correction to the push looks of 11 October.** The "push" there was the switch that removes
  the most six-loops, and listed exactly it turns out to join two links seven steps apart: a long-range re-link,
  not a local nudge (ASSUMPTIONS O124). So "one push and the change ran on" was a tube re-linked across a
  distance and then healing, which is why its clean end states were odd ones: a torus twelve around, one-sided
  surfaces. Local pushes exist (two or three steps apart) and also have square-keeping moves onward. They are
  being looked at with the tested kernel (`sandbox/six_loop_scan.py`, which names its push).
- 2026-10-12. Local pushes and no push, with the tested kernel (`sandbox/six_loop_scan.py`; 96 points,
  lambda = 1.25; `sandbox/out/scan2_*`). (a) A local push that breaks two squares, mu = 0.10, g = 1.0: 7 of 10
  fell straight back; 3 ran on, never with more than two squares missing, and ended exactly flat and one-sided
  with a quarter of the six-loop excess left. (b) A local push that breaks two squares and makes two surplus,
  same settings, 40,000 sweeps: none fell back and none finished; two ended flat and still six around with 40 %
  of the excess left; eight kept 20 to 90 units of flaws, with 32 to 92 % of their points seeing a sheet. (c) The
  same at mu = 0.20: all ten kept 32 to 106 units of flaws. (d) **No push at all, mu = 0.20, g = 2.0, 60,000
  sweeps: all eight left six around by themselves and ended mostly wide**, 50 to 83 % of points seeing a sheet,
  with 16 to 64 units of flaws and never fewer than 0.84 squares per point. None exactly flat. For comparison,
  with no price and trapped heat one end state in five was mostly wide at this size (T61).
- 2026-10-12. No push, held warm and then cooled slowly (`sandbox/out/scan3_*`; 96 points unless said). mu = 0.20,
  g = 1.5: all eight stayed six around through 100,000 sweeps. mu = 0.20, g = 2.0, then cooled over 60,000 sweeps:
  all eight left and ended mostly wide (50 to 83 % of points seeing a sheet) with 16 to 64 units of flaws; at 192
  points six of six, 57 to 66 %, with 85 to 112 units. mu = 0.25, g = 1.5: eight of eight left, 47 to 71 %. The
  slow cooling did not remove the flaws; none is exactly flat. Promoted the same day as T62, on fresh seeds, with
  a control at no price and a held-out size.
- 2026-10-12. The same price from the curled tube itself (`sandbox/six_loop_from_tube.py`; 96 points, g = 1.5, six
  replicas a setting; `sandbox/out/fromtube_*`). No price: the tube waits and ends as the clean tube six around,
  6 of 6, as in paper 1. mu = 0.05: it waits about as long, and then does not stop at six around; 4 to 10 % of its
  six-loop excess is left after the warm spell, and it ends with 42 to 78 % of points seeing a sheet and 32 to 64
  units of flaws. mu = 0.10, 0.20 and 0.25: the same, 45 to 83 %, 16 to 74 units. Never fewer than 0.75 squares
  per point. None exactly flat. So with even a small price the curled tube opens straight to mostly wide and
  never visits the narrow tube. Promoted the same day as T63, with the no-price run as its control.
- 2026-10-12. Seen in T63's control (no price; eight end states; a registered run whose gate failed, so nothing
  here is evidence): the burps that end on a leftover are not six around. 33 to 92 % of their points see a sheet,
  and one at 96 points sees 92 % with 20 units of energy left (not read from its wiring). Paper 1's "ends six around" was read from exactly flat
  end states only. To do: a tested reading of paper 1's saved end states that are not flat (T60 keeps them).
- 2026-10-12. The same question on paper 1's own saved end states (`sandbox/leftover_width.py`; T60 at lambda = 1.25,
  120 a size; `sandbox/out/leftover_width.txt`). Exactly flat: every one six around (109, 102, 107, 98, 98 at 64
  to 288 points). With a leftover (11, 18, 13, 22, 22): mostly wide at the two small sizes (10 of 11; 13 of 18),
  mostly patchwork at the larger (9 of 13; 14 of 22; 15 of 22, and none wide at 288). By the medians, 27 to 64
  points see a sheet at every size, so the share falls as the tube gets longer. It looks as if a leftover sits in
  a wider stretch of roughly fixed size. Not read from positions. Promoted the same day as an exact reading with a tested script (`scripts/read_leftover_width.py`; O116, addendum of 12 October), which reads width only from points clear of flaws: about half of those end states do hold a wider stretch. It narrows one sentence: "the
  tube ends six around" is true of the exactly flat end states, eight or nine in ten, and not shown for the rest.
- 2026-10-12. The owner's idea, "what if melting isnt allowed": a rule against bare links (a link on no square,
  so its ends are not otherwise close), hard, or soft at a cost of 8 or 32 (`sandbox/no_far_links.py`; 96 points,
  lambda = 1.25; `sandbox/out/no_far_links_BC.txt`). Exact, by listing every switch: the hard rule forbids about
  nine switches in ten, all the long-reach ones, and none of the cheap ones; paper 1's ways out of the curled tube
  (12, 14) and the local moves out of flat tubes (20, 31, 32, 42) all stay. Runs, 12 a rule: the burp still
  starts, but it ends exactly flat in 5 of 12 under the hard rule against 11 of 12 with none (9 and 10 under the
  soft ones); the rest keep a leftover. A flat tube heated and cooled, 6 a setting: at g = 3 nothing happens with
  or without. At g = 5 and 8 with no rule it melts (0.46 to 0.73 squares per point, up to 89 bare links at once);
  with a rule it keeps more (0.65 to 0.89), and under the hard one it never has a bare link. After cooling none
  comes back flat either way, and the ruled ones keep about twice the energy in flaws (116 to 156 against 67 to
  78). So in this look the rule stops melting, as built, and does not bring the fabric back: it heals worse. One
  cooling time; the owner has not yet said which reading of the rule she means. Not promoted.
- 2026-10-13. Is T51's slow fall a power law, or a floor plus one exponential? (`sandbox/t51_shape.py`: arithmetic
  on the numbers already written in O104, no result file opened.) The seven recorded frozen shares, from the
  quench to 300,000 fair sweeps, fit a floor of 0.012 plus 0.031 × exp(−t/80,000) to the rounding (rms 0.0004;
  three numbers chosen after seeing seven). The four recorded column ratios each give a time of 80,000 to 106,000
  fair sweeps. So the fitted exponents −0.82 and −0.34 may be apparent ones over 1.5 decades, and the
  extrapolation to 10¹⁸ sweeps would not follow: the share would level off near 0.012, about the energy of the
  knots that do not anneal. The two readings part at a million fair sweeps (0.012 against 0.008) and in between
  the cells already run. Not promoted.
- 2026-10-13. From inside, when does a wrapping grid stop looking endless? Counted the points within r steps on
  grids 4, 8 and 12 around and on the tube with its seam shifted by two, two ways (the record's `shells`, and the
  square lattice with the gluing vectors identified). The count first falls short at r = half the way around: 12
  of 13 at two steps on the tube, 40 of 41 at four steps eight around, 84 of 85 at six steps twelve around, 22 of
  25 at three steps on the shifted seam. Exact, and pinned in `tests/test_read_shapes.py`; a table in the
  plain-language edition of paper 1, Chapter 3.
- 2026-10-14. Does a relic seed a fold (the owner's (a), NOTEBOOK same day)? (`sandbox/relic_seed.py`; a 4 x 48 tube
  burps sealed at lambda = 1.25, is cooled, and is kept if it ends with exactly one curled column and no damage: 6
  starts from 10 burps. Then E units packed into one store, one store per point (T26's local spark), next to the
  column or as far from it as possible, 20,000 sweeps, sealed.) No fold grows. Of 192 points the most ever curled
  at once is 23, the largest curled piece 12, at any energy from 16 to 512 (2.7 times the price of curling the whole
  space). Near and far read alike. A small push next to the relic moves or dissolves it (16 units: the column is
  gone in 1 of 6 and moved in the other 5; the same push far away leaves it untouched in 6 of 6); larger pushes break space as in T57 (a third of the points damaged at 512, near or
  far) and the relic does not survive. Narrows (a) in two directions at this curling cost: a relic plus energy
  delivered beside it does not grow a curled region. Not tried: energy that may only curl (feed_energy.py's mode
  "curl") delivered at a relic, which is (a) and (b) together.
- 2026-10-15. Does a relic seed a fold when the energy beside it may only curl (the owner's (a) and (b) together,
  NOTEBOOK 14 and 15 October)? (`sandbox/relic_curl_seed.py`: relic_seed's protocol, 6 one-column starts from 10
  burps of a 4 x 48 tube at lambda = 1.25, E = 16, 64, 256 packed into one store beside the column or far from it,
  20,000 sweeps sealed; two rules for what a store may pay.) Rule "curl" (11 October's: refuse only moves that
  break without changing the curl): the same as ordinary energy. At 64 and 256 the fabric breaks (20 to 37 damaged
  points at the end at 256, peaks 39 to 48), the relic is gone in 12 of 12, and the largest curled piece is 12 points
  once. Rule "strict" (pay only for a move that adds surplus squares and loses none): nothing breaks at any energy
  (damage 0 at the end everywhere; transient peaks of 1 to 12), and most of the energy is never spent: of 256 units
  at most 42 left the stores, in steps of 14, each a new column of the 24 lambda - 16 kind forming in the fabric. So
  curl-only energy curls space only in column-sized bites. The end states hold 1 to 6 curled pieces, almost all
  separate columns of 4; in 2 of 6 near-relic runs at 256 a curled piece of 14 to 16 points persisted (worth about
  three columns of energy, so touching columns rather than a stretch of re-curled tube, unread). Near and far read
  alike in what forms; the relic itself moves or dissolves under a push beside it in both rules (kept whole in 0 to
  3 of 6 near, 6 of 6 far). Narrows (a) + (b) at this curling cost and size: a kind of energy that can only curl does
  not break space, and does not grow a fold from a relic either; it sits, or buys isolated columns. Not tried: a
  cluster of relics; longer runs; the owner's question (4), whether the fold's size tracks the energy, cannot be read
  from a fold that does not grow.
- 2026-10-15. Does the rod's opening leave a stuck relic, as the tube leaves a column (the owner's question whether
  the rod, one open direction, is the three-direction equivalent of the tube)? (`sandbox/rod_relic_dip.py` on saved
  end states: T48's rod cells, four, and T53's rod at L = 18, lambda = 1.25, the two coldest baths; the method checked
  first on T48's two-direction control, where it finds the 14-unit column STUCK, and its local dS, dX checked equal to
  the global recount on 200 random moves. For every connected piece of points still at d <= 1, every single switch
  with a point in the piece is priced at the run's lambda; STUCK means all cost more than zero. Exact per graph; the
  states are sealed or in a bath, not cooled; `sandbox/out/rod_relic_dip.txt`.) In the rod's product, which is the
  slab rung (d = 2), stuck curled pieces are common: of 107 pieces listed over 48 end states, 105 are STUCK and 2 FALL
  (both large unopened stretches whose cheapest move costs exactly 0; counted again from the output file after a
  first rough count of 90 and 88). The 91 small ones (1 to 15 points; 8 to 84 units at lambda = 1.25, 13 to 130 at
  1.40; cheapest exits 11 to 28 at 1.25, 1.6 to 30 at 1.40) are all STUCK and are the three-direction counterpart of
  the column; the 16 large ones (17 to 160 points) are the unopened rod itself. Read from the wiring, the four
  two-point pieces of 14 units in one state at lambda = 1.25 are each a pair of adjacent points still at d = 1 with
  four links on five squares and two on four, a two-point stub of rod inside the slab, cheapest move out 28, more
  stuck than the four-point column (6). So in "stringified" space, one direction still curled, stuck relics exist; in
  flat six-link space (d = 3 everywhere) none is found (O56, O58), and these pieces have not been tried there. Also:
  the 14-unit column's cheapest exit in a tube six around at lambda = 1.25 is 6 (dS -1, dX -2; 16 - 8 lambda, so it is
  a dip for 1 < lambda < 2), not the 12 that O107 guessed ("ours, unverified") and the 13 October note repeated; O107's
  comparison of the column's and the knots' walls needs that number. Not promoted.
- 2026-10-15, late. PREDICTIONS WRITTEN BEFORE READING (the owner's instruction of this hour: log predictions from
  the full story before reading results). Two looks are running. (1) `sandbox/slab_patch_sealed.py`: the tied slab
  4 x 8 x 8, sealed with empty stores, from a patch opened by hand (T54's helix patch) of k columns, lambda 1.25 with
  k = 2, 3 and lambda 1.20 with k = 3, 4, room C = N and 4N stores, 20,000 sweeps, three replicas. Disclosed: the
  control cells k = 0 (sits for ever, as it must) and k = 1 at lambda 1.25 (below the peak; grew a little and damaged
  a little, 160 to 208 of 256 points still on the slab rung) had printed and were seen before this was written; the
  past-peak cells had not. *Ours:* at lambda 1.25, k = 2 and 3 with C = 4N, the opening spreads to most of the slab
  (over 200 of 256 points at d = 3) and the stores end near 0.7 per store, with a few curled pieces and some damage;
  with C = N the release warms the box past what flat space bears and the end state is mostly damaged (over 50 points
  at d > 3). At lambda 1.20, k = 3 and 4, the same in kind, slower. *The owner's (inferred from her picture of 15
  October, "the 3 pop together creating a full new 3 d space"):* the whole slab opens into one flat space. Her word is
  owed. (2) `scripts/exact_relic_search_d.py` at lambda 1.25 (O58's one- and two-switch search, which found no dip at
  1.02): *ours:* no dip at 1.25 either; a dip is hardest at the higher curling cost because every move that sheds a
  surplus square gains more there. *Hers:* not asked; the flat-space relic is her dark-matter candidate, so her
  picture needs a dip to exist.
- 2026-10-16, 00:05 UTC. READ: the sealed slab from a hand-opened patch (`sandbox/slab_patch_sealed.py`; predictions
  above, written before). Every past-peak patch state sat exactly still for 20,000 sweeps with empty stores: k = 2 and
  3 at lambda 1.25, k = 3 and 4 at 1.20, with C = N and 4N stores alike (d-census unchanged, nothing left the stores,
  drift 0). Only the below-peak control, k = 1 at 1.25 (24 above the slab), moved: it grew a little and damaged a
  little. So T54's completed patches of two columns and more are dips of their own: no single switch out of them
  goes downhill, which is O118's correction seen in a run (the states between completed patches lie higher). Our
  prediction (OPENS IN ROOM at C = 4N) fails; the owner's "Opens in room" would fail on this protocol. What it
  narrows: a hand-opened patch with no energy is not a push, and T65 as drafted cannot run that way; an opening of
  the slab needs energy in the stores to cross the single-move walls between patches (the slab's own is 4 at 1.25
  under the tie, O106), which is a spark run, not a patch run. Not promoted; the T65 draft is revised to a spark.
- 2026-10-16, 00:58 UTC. READ: the relic search at lambda = 1.25 (prediction above, written before). O58's one- and
  two-switch search in flat 6 x 6 x 6 listed two candidate kinds, (dS, dX) = (-4, 4) at 84 units and (-7, 4) at 132,
  the same two O58 flagged at 1.02; rebuilt and tested on the full move list (`scripts/exact_relic_confirm_d.py 1.25`;
  `sandbox/out/relic_confirm_lam125.txt`) every arrangement of both kinds has a move downhill (by 84, 68 or 48):
  NO DIP at 1.25, as at 1.02. Ours held. Bookkeeping only: the owner set the flat-space dip aside on 16 October.
- 2026-10-16. Does an unequal flat torus curl its shortest side first (the owner: "first curl will be the 6 dropping
  to 4")? (`sandbox/which_side_curls.py`, `which_side_curls2.py`, `which_side_curls3.py`; the two-direction rehearsal
  at lambda = 0.5, where the sheet gives way to a tube 2 per point lower; flat 6 x 16, 8 x 12, 6 x 24 tori of 96 and
  144 points, each also with its axes swapped as a control for slot bias; `sandbox/out/which_side_curls*.txt`.)
  Pass 1 at g = 3.0 was too hot: the sheets went past the tube to knots and most links were rewired on both axes, so
  no direction could be named. Pass 2 at g = 2.5, stopped at the first tube: the links along the LONG side (16) were
  replaced more than those along the short side in 12 of 12 for 6 x 16 and 16 x 6 (survival 0.36 to 0.53 long against
  0.17 to 0.58 short, with the swap control agreeing), the opposite of the owner's expectation; at g = 2.0 nothing
  moved in 40,000 sweeps and 8 x 12 stayed flat at both. Pass 3, the product's own rings (the links on three squares)
  traced to their origin in the clean tubes (d = 1 at 90 % of points, none at d = 0): about equal numbers come from
  the original x and y links, with a third to a half new (6 x 16: 32/29/35, 32/40/24, 37/37/22, 33/29/34, 25/26/45;
  6 x 24: 50/51/43; 24 x 6: 49/47/40), so the new rings run across both original directions, not along the short one.
  Reading: at this curling cost and size the curl does not choose the shortest side; the energy and the moves are
  local and see no length, and the rings the chain builds are diagonal to the original axes, as the seam-shifted
  tube of O116 is. Her prediction, read as "the short side's links become the rings", does not hold here. One lambda,
  one coupling, two directions, small sizes. Not promoted.
- 2026-10-16. **Does three-direction space heal damage in fewer sweeps than two-direction space untied?** (The owner's
  prediction, notebook, same day; `sandbox/heal_time.py` → `sandbox/out/heal_time.txt`.) N = 216 both (12 × 18 against
  6 × 6 × 6), λ = 1.25, E = 192, 384, 768 packed into one store of 4N empty stores, sealed, 4,000 sweeps, 8 replicas,
  damaged = points with d above flat. **Yes.** The sheet never returned to the scar level (≤ 2 damaged) at any energy
  (0 of 24; end medians 26, 37, 54 damaged); the cube did in 8, 6, 5 of 8 at the three energies, median 1,250, 1,629,
  2,462 sweeps after the peak (end medians 12, 17, 20, the warm stores re-breaking a little). Matched by breaks bought
  (2D at 192 against 3D at 384) the same. The tie "all at the last" made no difference at all: tied and untied 3D
  cells are identical draw for draw, since a damaged point pays no tie and healing never passes a half-curled state.
  Reason, ours: at one store temperature a break costs 64 in 3D against 32 in 2D, so the bath re-breaks the sheet and
  leaves the cube alone. Her prediction holds; ours held on the tie and failed on the time. One size, one λ, one bath,
  a look. **Promoted the same day on the owner's word (rule 16 (c)): PREREGISTRATION T66, fresh seeds, 16 replicas, a held-out size; one look came before it.**
- 2026-10-16. **A feed instead of a spark** (the owner: "a flow with various rates based on what black hole eats and
  so it's one spot per seed"; `sandbox/slab_feed.py` → `sandbox/out/slab_feed.txt`). Untied slab 4 × 8 × 8, λ = 1.25,
  4N empty stores, r units a sweep into one shared store or one point's own store. First try (rates 2, 8, 32 over
  10,000 sweeps; `slab_feed_try1.txt`): the two rows that finished had every point broken and 12 units a store, so the
  rates were far too high; lowered to 0.25 to 16 with a damage stop. **Read:** at every rate, shared store or one point's store, the slab
  moved and then broke: every one of 24 runs stopped on damage (a tenth of the points) with a third of the points
  open (31 to 92 of 256) and none past half. The first move came at the slowest rate after about 250 to 400 sweeps
  (60 to 100 units fed) and was an opening of 8 to 18 points in 4 to 9 separate regions with 4 points damaged; by
  the stop there were 8 to 23 separate open regions, a sprinkle and not a front, about two points opened for every
  one broken, after 275 to 1,600 units fed (slow feeds broke it on less energy than fast ones). Her prediction
  (opens, one spot per seed): half holds, it opens from many spots at once and from the slowest feed on; half
  fails, it never gets past a third open before a tenth is broken. Ours (no rate opens it cleanly; the fast feed
  breaks it, the slow one sits): the clean half holds, the "slow one sits" half fails, the slowest feed moved it
  too. Reason, ours: each completed patch is a dip (O118), so every extension has to be paid for again, and the
  feed pays for breaks as readily. One size, one λ, three replicas, a look. Not promoted.
- 2026-10-17. What happens to one 64-point knot given lots of energy (the owner's question, NOTEBOOK same day)?
  (`scripts/run_sealed_curled_d.py` on a scratchpad config: one 6-cube, lambda = 1.25, sealed, named points, a spark of
  0, 64, 192, 512 or 1024 in one store of a shared bath of 2N, 4 replicas, 5,000 sweeps; output in the scratchpad, not
  in `results/`.) It opens at once at every energy (the way downhill, O41), and what it ends as is set by the energy.
  With nothing added: 1 of 4 fully open (64 at d = 3), 3 of 4 rest at 48 open and 16 still two-curled, the T49 picture.
  At 64 added (one direction's worth): the same, with 8 broken points in 2 of 4. At 192 (the knot's whole release again):
  20 to 27 open, 13 to 35 half-curled, 3 to 15 broken: a mess, neither open nor curled. At 512: 12 to 16 open, 45 to 50
  broken. At 1024: 4 to 7 open, 56 to 58 broken, the random phase. So more energy never helps a knot open: past about
  one direction's worth it breaks instead, as flat space does (T57) and the slab does under a feed (T67). One lambda, one
  size, four replicas, named points; a look. Not promoted.
- 2026-10-18. The owner: "maybe we should be pricing cubes not squares." `sandbox/cube_price.py` counts 3-cubes (eight
  points wired as Q3) on the built six-link ladder and for every valid single switch from the slab 4×6×6 and from flat
  6×6×6 (`sandbox/out/cube_price_2026-10-18.txt`). Ladder, cubes per point: flat 1.0, slab 1.5, rod 2.0, 6-cube 2.5, so a
  curled direction adds half a cube a point as it adds a quarter square and one surplus square: the same ladder, and
  opening a direction loses N/2 cubes as it loses N/4 squares. Single switches: the opening move of the slab (36 units,
  dS −6, dX −12) destroys 14 or 16 cubes; the pure breaking move (64 units, dS −4, dX 0) destroys 8 cubes in the slab and 6
  in flat space. So under a cube count the opening move is about twice as destructive as a break, not less: a price on
  cubes does not make opening cheap and breaking dear, and it does not remove the loss of small loops that opening is.
  One size each, exact, a look. Not promoted.
- 2026-10-18. The owner: "Yes let's look" at her picture run as a rule: the slab fed at every point, with only closed
  and open allowed (no point ever broken). `sandbox/clean_feed.py`: the untied slab 4 × L × L at λ = 1.25, a store at
  every point fed r/N a sweep (T68's "all" place), moves of two switches at once (the second within two steps of the
  first) accepted only if no point is left broken (d ≤ 3 everywhere), paid from the pooled stores of the moved points;
  dH checked exact against the full Hamiltonian, energy conserved to the unit. Rates 2, 8, 32 a sweep, two seeds, 6,000
  sweeps; then r = 32 for 60,000 sweeps at L = 8 and 30,000 at L = 12 (`sandbox/out/clean_feed_*2026-10-18.txt`,
  `clean_feed_long_l8.txt`, `clean_feed_long_l12.txt`). Seen: (1) clean moves are rare under random proposal (two in
  40,000 attempts with unlimited stores), so the clock is the proposal's, not T68's, and the stores are never the
  limit (they bank hundreds of thousands of units unused). (2) The slab opens in clean steps of 16 or 8 points, first
  as 1 to 4 separate patches, which merge into ONE open region by about a third open: at L = 8 one region of 184 of
  256 at its largest (72 %), then back and forth between 164 and 184 for the last 20,000 sweeps; at L = 12 one region
  of 316 of 576 (55 %) at 28,000 sweeps and still rising. The first growing open region larger than one cube that a
  three-direction run of the slab has shown, T48 at λ = 1.40 aside. (3) It climbs: H − H₀ = 4 × (points open), to the
  unit at L = 8 and within 2 % at L = 12, so every opened point costs the seam 4 units and nothing is released on the
  way; the release of 1 per point could come only at completion. At L = 8 it did not complete (no flat six-link
  torus has 256 points, so the clean end state there, if any, is not a torus). (4) The control with breaking allowed,
  same moves and stores: every point broken by sweep 2,000 at every rate (the random phase), as T68. Two seeds, one
  λ, L = 8 and 12; the move set and the pooled payment are choices made for the look. Not promoted.
- 2026-10-18. The owner: "A no-break store could, if the reshaping seams leave no point broken, which nobody has
  checked. Check this?" `sandbox/clean_moves_census.py`: every pair of switches (the first through one point, the second
  within two steps of its ends) from flat 6 × 6 × 6 and 6 × 6 × 8 and from the slab 4 × 6 × 6, kept if no point is left
  at d > 3 (`sandbox/out/clean_moves_census_2026-10-18.txt`). Flat space: 563,670 and 607,384 pairs tried, and the only
  clean ones are the 102 in which the second switch undoes the first (dS 0, dX 0, nothing changed). The slab: 303,580
  pairs, 80 undo pairs, and 24 real clean moves, all the known first opening (dS −4, dX 0, 64 units, 16 points to d = 3).
  So within two switches flat six-link space has no clean move at all: it cannot curl, narrow or reshape without a
  point passing through broken, and the reshaping of a flat torus toward the slab cannot even start under the no-break
  rule at this move size. Three or more switches at once not checked. Exact within its reach; a look. Not promoted.
- 2026-10-18. The owner's compaction move made exact (`sandbox/pair_moves.py`; `sandbox/out/pair_moves_2026-10-18.txt`):
  a linked pair of the two kinds is removed and its ten other neighbours spliced five to five. The whole layer
  (x = 0, 1 removed, x = −1 spliced to x = 2) takes 6 × 6 × 6 to 4 × 6 × 6 and 6 × 6 × 8 to 4 × 6 × 8 and is the built
  slab exactly (N, S, X, H, every point d = 2, valid). One pair removed from flat 6 × 6 × 6: 5 of 120 splicings valid, all
  leaving broken points (dH 176 with 24 broken, or 191 with 26); from the slab 4 × 6 × 6 none valid. Exact; a look.
- 2026-10-18. A part of a layer contracted (`sandbox/partial_contraction.py`; `sandbox/out/partial_contraction_2026-10-18.txt`
  and `_L8_`): patches of 1, 4 and 6 positions with every side-respecting re-linking of the rim tried (the 1 × 2 patch has
  none valid), strips of 1 to 4 rows with canonical re-linkings, and the whole layer; λ = 1.25, L = 6 and 8. Every partial
  contraction leaves 26 to 80 points broken and sits above the finished slab (191 to 432 against 144 at L = 6, 256 at L = 8);
  the blocks cost the same at both sizes, so the seam's cost is local; only the whole layer is clean. Read backward, the
  slab is separated from flat space on these paths by a seam of about 230 to 280 units, the size of T54's completed patch.
  Not tried: re-linkings that move the x = −1 to x = 2 splice, patches of 3 × 3 or more, L above 8. Exact within reach; a
  look. Not promoted. Written up in `docs/design/contraction_model_brief.md`, section 2.5.
- 2026-10-18. The owner's spiral (`sandbox/spiral_contraction.py`; `sandbox/out/spiral_contraction_2026-10-18.txt`): the
  layer contraction of flat 6 × L × L with the splice shifted s steps along y, so the seam of the curled direction runs
  as a spiral with s/L turns per circuit. Every even shift above zero gives a valid state with X = 0, H = 0 and every
  point d = 3 (L = 6: s = 2, 4; L = 8: s = 2, 4, 6); only s = 0 is the slab (X = N, H = 4(λ − 1) N, d = 2). The spiral
  stores no curling cost in this toy; it is O116's flat product (the seam shifted by two) reached from the other side.
  Exact; a look. Not promoted.
- 2026-10-18. The ladder of whole-layer contractions (`sandbox/out/ladder_contraction_2026-10-18.txt`, from
  `sandbox/pair_moves.layer_contraction`): flat 10 × L × L → 8 → 6 → 4 at L = 6 and 8, λ = 1.25. Every step above six
  leaves H = 0, X = 0, every point open and the graph valid; the step 6 → 4 gives X = N, H = 4(λ − 1) N exactly (144 at
  L = 6, 256 at L = 8), every point closed. Exact; the brief's test E2 for the layer form. A look.
- 2026-10-18. Two kernels built with rule-6 tests (`src/graphity/contraction.py`, `src/graphity/clean_move.py`; tests
  `tests/test_contraction.py`, `tests/test_clean_move.py`). Exact facts met on the way, none a result: (a) under the
  layer form the split of the slab is downhill, so with no gate it fires at the first proposal, and the lump then
  sitting in the stores pays the contraction back at the next; a uniform leak holds the product open only once the
  steady store per point, about r/ℓ, falls below the curling cost 4(λ − 1) (arithmetic in T71). (b) With layer moves
  alone the width's stationary distribution is exactly Boltzmann in μ_N N (a test checks the chain against the sum). (c)
  The first clean two-switch move out of the slab costs exactly 64 and opens 16 points, T69's first clean state, at
  λ = 1.25 as at 1.10; one seed hit it after 1.2 × 10⁵ attempts at L = 6 and 2.2 × 10⁵ at L = 8
  (`scratchpad/clean_rate.py`, not kept). (d) The sandbox script `clean_feed.py` counted a second switch that exactly
  undid the first as an accepted move; the kernel refuses that null move. Its census numbers (open points, regions)
  were read from the wiring and are unaffected; its `acc` column was inflated.

- 2026-10-18. Where do T51's knots sit along the sheet (`sandbox/knot_positions.py`; `sandbox/out/knot_positions_2026-10-18.txt`;
  the owner's "scraps as the seeds of structure", notebook 18 October)? Over the 600 saved end states, 1,456 knots (1,142
  columns, 96 double columns, 136 knots of two kinds, 82 groups that are two or more knots within two steps of each other).
  **Clustered, not random:** 23.5 % of knots have another within four columns of the 128 to 512 along the ring, against 7.7 %
  for uniform random positions with the same count per sheet; the smallest-gap bin holds 228 gaps where uniform gives 134;
  the median nearest-neighbour distance is 0.36 of the mean spacing against 0.43. The clustering is on the scale of a few
  columns; beyond it the gaps look uniform (the upper p-value bins sit near their expectation). **Set at the opening:** of
  the knots that survive a slower cooling, 88 % lie within two columns of a knot after the next faster cooling of the same
  opened sheet (random positions: 4 %), which fits O107's reading that the number is set at the opening and the cooling
  only removes. Kinds sit beside kinds: a double column's nearest neighbour is a knot of two kinds 77 times in 96 and never
  a column. A look; it supports nothing. What it kills: a sprinkle of fixed-energy knots, clustered on a few columns and
  random beyond, is white noise at larger scales (density spectrum flat in k, n_s = 0 in the cosmologist's convention),
  while the sky's seeds are nearly scale-invariant (n_s ≈ 0.965; Planck 2018, general knowledge, to verify); so the scraps'
  own layout cannot be the seed spectrum in this toy. Untouched: scraps as dark matter falling into seeds laid by something
  else.
- 2026-10-18, evening. Under the per-universe reading (Update 68), what brings "when we are" forward from [LBS16]'s
  trillions of years? `sandbox/when_we_are_shorteners.py` on the Stage E population model
  (`sandbox/out/when_we_are_shorteners_2026-10-18.txt`). Seen: with every inhabited planet weighted by how long its
  observers last and all stars counted, the share before today is 0.002 (Loeb et al.'s thousandth); her window as a hard cut
  at 100 Gyr gives 0.083; a rip at 30 or 50 Gyr 0.33 or 0.18 (the same arithmetic as a window at that time); excluding
  red dwarfs 0.16, Sun-like only 0.77; a factor multiplying every time alike (an interaction term, company helps or hurts)
  moves nothing (0.002, 0.001); counting each inhabited planet once at its origin, or observers lasting 1 Gyr per planet,
  0.92 with the peak near 5 Gyr. A look; it supports nothing. What it kills: "no interaction between planets" as a
  shortening of the habitable era (a uniform factor); it survives only as a rule for who counts (each civilization once),
  piece 14's lever, which then makes us late rather than early.
- 2026-10-19. Does the parent hold "a little more" than it hands to daughters, and can the toy hold an excess of one
  kind of point? (`sandbox/curl_uncurl_ledger.py`, out `sandbox/out/curl_uncurl_ledger_2026-10-19.txt`; layer moves only,
  g1, daughter mode, one seed, 3,000 sweeps.) Every daughter carries exactly a N_slab (144 at L = 6, 256 at L = 8,
  λ = 1.25). The parent's excess over its starting curl is whatever the stores hold at the moment of reading: 0.3 % of all
  it released at λ = 1.25 (both sizes), 28 % at λ = 1.10 (the torus wandered to width 8 and the feed piled up). So the
  excess is set by the gate, the rate and when one looks, not by the burp. The two kinds of point are equal at every
  sweep (108 and 108; 192 and 192): exact, by the degree rule, so no excess of one kind can exist in the toy. A look.
- 2026-10-19, evening, the owner's question whether the toy's curvature obeys the handle count of Gauss-Bonnet
  (`sandbox/handle_bound.py`, out `sandbox/out/handle_bound_2026-10-19.txt`). *Exact, ours, by Euler's formula, unreviewed:*
  draw a four-link two-sided graph on a closed orientable surface with g handles; every face is an even cycle of length
  at least 4, so 2 - 2g = F - N = -(1/4) x (sum over faces of length k > 4 of k - 4); each such face has k - 4 >= k/3,
  and each edge with fewer than two squares borders at least that many sides of such faces, so D = sum over edges of
  max(0, 2 - S_e), which is H/4 at lambda = 1, obeys D <= 24 (g - 1): **g >= 1 + D/24**. Corollaries: a graph drawn on
  a torus has every face a square, so any edge with fewer than two squares forces at least two handles; and at a fixed
  share of missing squares the handles grow in proportion to the size, as Gauss-Bonnet gives handles in proportion to
  area for a fixed negative curvature. It is a bound, not an equality, and the positive side (a curl, an edge on three
  squares) is not counted by it. The check: the flat 8 x 8 torus drawn naturally has g = 1 and D = 0 (equality); graphs
  made by 1 to 128 random switches from it never broke the bound in 1,000 random drawings each. Random drawings have far
  more handles than the fewest possible (slack 19 at least), so the check is weak and the proof carries the claim. Four
  links only: six- and eight-link networks are not surfaces. A look; an exact test in `tests/` before anything cites it.
- 2026-10-20, the owner's "Proceed" on a look for a balancing halo round the burp's knots (her gravity idea of the same
  night): `sandbox/knot_halo.py` and `sandbox/knot_halo_ring.py`, on T51's saved states at N = 512 (length 128, 10k cooling;
  33 of 39 connected states with knots) and 1,024 (length 256, 300k cooling; 14 of 40), the held-out 2,048 not read. Exact
  for each state; a look. **No halo beyond the first ring:** at two or more steps from a knot every link has exactly two
  squares and every point's share of the energy is zero (at N = 512 a handful, 0.4 % of points at two to five steps,
  carry other small irregularities). **In the first ring** a point is either exactly flat or has exactly one link with
  three squares and one with one (223 of 530 at 512; 60 of 336 at 1,024), never anything else: curl and anti-curl
  cancel point by point. *Ours:* that balance is forced by the counting, not a response: a point with two open directions
  has exactly four squares (with the hard-core rule each pair of its links closes at most one), so a curled link must be
  paid for by a short one; the toy has local neutrality built into its count of directions, and it stops at the knot's
  edge. **The ring is softer:** the cheapest flaw costs 15 within two steps of a knot and 20 from three steps on. Read
  with Update 73's expectation: in the toy's stiff space a knot's curling is balanced at its own edge and nothing reaches
  farther; a balance that spreads, as the owner's curve-first gravity needs, needs soft space. Not promoted.
- 2026-10-20, the owner's growth rule (VISION Update 75): can points be added to flat two-direction space in one place
  without a flaw? (`sandbox/pair_insertion_2d.py`; λ = 1.25; exhaustive over every choice of three cut links within R
  steps of one point.) R = 2 (L = 10): 560 choices, 184 simple, none valid (the hard-core rule). R = 3 (L = 10): 7,140,
  2,540 valid, the cheapest adding 42 and leaving 8 points off d = 2. R = 4 (L = 12): 41,664, 23,792 valid, the same 42
  and 8. A whole row is clean and free (O116). So local growth always leaves a flaw and costs energy. Exact within
  reach; a look. Written into `docs/design/growth_rule_brief.md`.
- 2026-10-20. When a linked pair of points is added in one place in flat two-direction space, does it leave one curl
  and one uncurl (the owner's idea: adding space makes a curl knot and an uncurl knot together)?
  (`sandbox/pair_insertion_dipole.py`; λ = 1.25; the insertions of `pair_insertion_2d.py`, read for missing squares D and
  curl X.) None leaves curl alone. At R = 3 (L = 10): 2,540 valid, 1,240 leave both and 1,300 leave missing squares only;
  at R = 4 (L = 12): 23,792 valid, 7,220 both, 16,572 missing only. The cheapest (42) leaves 10 missing squares and 2
  curled links; the cheapest with no curl costs 48 (12 missing). So added points leave mostly the uncurl kind, a
  little curl at most: not a balanced pair. *Ours:* adding material to a flat sheet makes it ruffle like a saddle,
  negative curvature, as in ordinary geometry. Exact within reach; a look.
- 2026-10-21. Does the toy treat a curl and an uncurl as mirror images, as matter and antimatter would need (the
  owner's hypothesis of the same day, curl matter and uncurl antimatter, against their measured equal masses)?
  (`sandbox/curl_uncurl_mirror.py`; output `sandbox/out/curl_uncurl_mirror_2026-10-21.txt`.) No, in two ways. (1)
  Prices: written link by link, a missing square costs 4 and an extra square 4(λ − 1), 1 : 4 at λ = 1.25, equal only at
  λ = 2; and a link can be missing two squares but carry only one extra (four against one with six links), so no λ
  makes the energy symmetric. (2) Objects: of the 4,928 valid one-switch defects of a flat 8 × 8 torus and 4,968 valid
  two-switch defects near one point, none carries curl alone; every curl comes with more missing squares than extra
  ones (the curl-carrying classes run from D = 10, X = 2 upward), while missing squares alone are common (the cheapest
  defect, 32, is D = 8, X = 0). So in flat space a curl appears only inside a larger uncurl, and the two kinds are not
  mirror images by price or by what exists. *Ours:* read as particle and antiparticle, the raw defects would have
  unequal masses; the reading survives only through what binds them (her answer of the same day: most of a particle's
  mass is connecting energy, not the loop), which the toy does not have yet. Exact within reach; a look.
- 2026-10-21. Which closed rings can face diagonals make in the six-link toy's flat space (the owner's twisted rings,
  VISION Updates 85 to 90)? (`sandbox/diagonal_rings.py`, runs in 2 seconds.) Inside one cube, each kind of point has
  four corners that are all one face diagonal apart: a regular tetrahedron of six face diagonals, one kind's tetrahedron
  interlocking with the other's; the cube's four corner-to-corner diagonals all join the two kinds. Through one point,
  rings of face diagonals: 24 of 3 diagonals (equilateral triangles, the tetrahedra's faces, length 3√2 ≈ 4.24), 116 of
  4, 630 of 5, 4,038 of 6. Rings of edges: none of 3, 12 squares of 4 (length 4), none of 5, 132 of 6. So the smallest
  ring of diagonals is a triangle of three, and the smallest ring of edges is the square, slightly shorter (4 against
  4.24). Exact geometry of the flat lattice; no energy is involved.
- 2026-10-22. Is the shape of a curl connected to the golden ratio (the owner's question)? (`sandbox/golden_ratio_look.py`, runs in seconds; output `sandbox/out/golden_ratio_look_2026-10-22.txt`.) Not in the toy as it stands. (1) The flat lattice's lengths are 1, √2 and √3, none golden. (2) A lattice can only turn into itself by 60, 90, 120 or 180 degrees (the crystallographic restriction, listed by brute force), and the golden ratio comes with five-fold turns (72 degrees), so no flat or curled lattice shape of the toy has it. (3) Vibrations: rings of 4, 6, 8 and 12 links, the 3-, 4- and 6-cubes and the 8 × 8 torus have no golden frequency; rings of 10 and 20 links and the 16 × 10 torus do, because their length is a multiple of 5, not because of curling. (4) Shadows: the 6-cube, which is the toy's fully curled three-direction X, cast into three directions along the toy's own axes is a plain cube (8 corners, 6 square faces); cast along the six five-fold axes of an icosahedron it is a 32-corner, 30-face solid whose every face is a rhombus with diagonals in the golden ratio 1.618034 (the rhombic triacontahedron). So the golden ratio is one irrational viewing angle away from the toy's X, and nothing in the toy's energy picks that angle. Exact geometry; a look.
- 2026-10-22. Can the published model's negatively curved finite-coupling background act as our curling cost at bare λ = 1 (the owner's hypothesis, VISION Update 89)? (`sandbox/background_curl_price.py`, 280 s; output `sandbox/out/background_curl_price_2026-10-22.txt`.) At λ = 1 the energy is 4 D exactly (D the missing squares), so a surplus square costs nothing in any background and a background of missing squares makes a curl cheaper, not dearer: the cheapest single switch that adds surplus squares costs 8 in the finite Fig. 7 tiling (three squares and a hexagon at every point, 240 points) against 40 in flat space, with none downhill in either. Any positive price per surplus square at λ = 1 is entropy times g, so it vanishes cold, where our family's curled torus is stuck with a fixed wall; the two cannot agree over a range of g. In the saved T36 equilibrium graphs (λ = 1, N = 196, g = 3.433 and 3.697, 32 read) 2 to 7 % of links carry three squares, almost all isolated, one closed ring of four in 32 graphs, so the warm background makes no curled objects of its own; curl-making switches are 8 to 13 % of all switches, mean price +18 to +30, about one in twenty downhill. A per-link potential of mean force −(g/4) ln[P(3)/P(2)] reads 1.8 to 2.9 but its calibration twin on the deficit side reads 0 to 0.6 where the true price is 1, and short λ = 1.25 chains give the wrong sign for a known price: that route cannot read an effective λ. The exact census at 16 and 18 points gives entropic prices of +0.038 g and −0.036 g per surplus square (named points), a symmetry effect that flips with N and with the ensemble. Kills the hypothesis as a constant λ − 1 set by the background; a g-dependent entropic surcharge on curl in a background at fixed coupling survives, and the owner's question of the same day (why can a background not charge entropy?) gave it its reference: a flat object of the same square content in the same background. Test to register with her prediction: the entropy lost by holding a curled ring against that lost by holding a flat nine-square patch, across couplings, from equilibrium frequencies and conditioned energies (her inferred prediction: the curl loses more and the gap grows with the deficit density; ours: no gap once square content is matched). A lifetime test measures a wall, not a cost. Finding: `docs/outreach/finding_2026-10-22_background_curling_cost.md` (private folder). A look.
- 2026-10-22. How rare are the curled ring (a square whose four links carry three squares) and the flat patch (a 4 × 4 grid, nine squares) in the published model's warm equilibrium graphs? (`sandbox/curl_vs_flat_feasibility.py`, 30 s, on the 32 already-read T36 graphs at N = 196; output `sandbox/out/curl_vs_flat_feasibility_2026-10-22.txt`; checks: the flat 14 × 14 torus gives 0 rings and 196 patches, the curled 16 × 4 torus 16 rings.) At g = 3.433: 1 ring in 16 graphs, 24 patches (1.5 per graph); at g = 3.697: 0 rings, 11 patches (0.7 per graph). Sizing for the curl-against-flat test (PREREGISTRATION T78): about 6,000 snapshots per cell to see of order a hundred rings at 3.433; the warmest coupling may read NOT READ. A look.
- 2026-10-22. After T79 (PENALTY ON CURL, O148): is the curled ring's extra entropy loss the hard-core rule's forbidden volume? (`sandbox/forbidden_volume.py`, about 25 minutes on the ~~672~~ 736 saved warm graphs of T78 and T36 at N = 196 *(corrected 23 October: the script reads all 576 of T78 and 160 of T36, by directory listing)*; output `sandbox/out/forbidden_volume_2026-10-22.txt`.) For each object found (54 curled rings, 2,208 uncurled twins, 2,118 flat 3 × 4 grids, 503 flat 4 × 4 grids, flat ones sampled three per graph), every pair of links within one step of the object and not the object's own was tried as a switch. The share of those switches that the hard-core rule and simplicity allow: curled ring 12 to 13 %, its uncurled twin 34 to 35 %, flat 3 × 4 grid 68 to 69 %, flat 4 × 4 grid 70 to 73 %, the same at all four couplings; of the allowed switches about half leave the object intact for every type. So the surroundings of a curled ring have about one allowed move for every 2.7 of its twin's and one for every five of a flat grid's: a saturated link forbids most of the switches near it (a fourth square, a K_{2,3}). Consistent with the hard-core rule as the mechanism of the penalty on curl; a one-step proxy for the entropy of the surroundings, not the entropy; the flat grids were found in flat regions, so their high share is partly their surroundings' order, which is why the twin is the fair comparison. To register on fresh graphs with her prediction if it is to be cited. A look.
- 2026-10-22 (evening). Does the published bridge from the toy to a mass, Eq. (45) of [T25] (a bubble's free-energy excess over the surrounding network equals its curvature deficit, times a link length and an unspecified factor n(g)), hold in form inside the toy? (Arithmetic on T79's registered estimates, no new run; printed in chat, to be scripted if cited.) For the ten ordered objects of T79 at four couplings, the free energy F_X and the curvature side dD_X = E_X/4 (the mean excess of missing squares when the object is present): every ordered object sits in snapshots with FEWER missing squares than average (dD < 0) while costing free energy (F > 0), so with one positive constant the equation has the wrong sign for ordered objects; and the ratio F/dD is not one constant, spanning −2.1 to −4.3, the curled ring at −3.6 to −4.1 against −2.1 to −2.8 for the large flat grids (F = −2.3 to −2.6 × dD + 1 to 2 over the ten, correlation −0.93). *Ours, unverified:* his equation is written for random-phase bubbles (dD > 0, F > 0) and covers his matter and his deficit-rich allotropes in sign; the owner's curled objects are not deficit and would need the curvature side extended to surplus, which is what the curling cost 4(λ − 1) does in our family. To use the equation for a number needs ℓ, n(g) and an energy unit, none given in the paper. A look.
- 2026-10-22 (night). The owner's question: could the dark-to-ordinary matter ratio (5.36) come out as the ratio of energies stored in two lattice loops of different lengths (edge loops against diagonal loops, "two springs folded into circles")? Rule 13's counting step first (`sandbox/spring_ratio_look.py`, 54 s; output `sandbox/out/spring_ratio_look_2026-10-22.txt`): with the 119 distinct closed-loop lengths the cubic lattice offers up to 12 steps (edges, face and body diagonals), five energy laws (L, L², L³, 1/L, 1/L²) and loop counts ~~1 to 8~~ 1, 2, 3, 4, 6 and 8 *(corrected 23 October, as the script has them)*, 29,101 ratios land within 2 % of 5.36, and ten random targets between 2 and 12 get 26,000 to 33,000 each. So a loop-length formula that hits 5.36 carries no weight on its own; it would count only if the same formula, with nothing refitted, gave a second measured ratio it was not built for. A look.
- 2026-10-23. Two questions of the owner's on saved three-direction graphs, her predictions in the notebook first (`sandbox/slab_edge_and_flaws_3d.py`, 20 s; output `sandbox/out/slab_edge_and_flaws_3d_2026-10-23.txt`). (A) Where curl and uncurl sit after an opening: the T71 control end states are fully refolded slabs (every point at the curled rung), so they hold no opened region to read; in T53's end states (the rod opening one direction in a bath, 24 graphs per cell) no link below four squares lies inside the clean open region or the clean curled region at any coupling (0 of 15,000 and 0 of 10,600 at λ = 1.25, g = 1.5; a handful at the warmest), every missing square touches a damaged point: the uncurl sits at the seams and joints, not inside the mother. Surplus links inside the open region are the rung's own still-curled direction, so "curl to the daughter" cannot be read from a rod that never reached the open rung; it needs an end state with a fully open region (T56's slabs, unread). (B) Damage per seed in three directions, from T53's logs and end states: at the coldest bath (g = 1.5) 38 to 122 damaged points per seed at λ = 1.25 and 72 to 229 at 1.40, in connected pieces of recurring sizes (6, 14, 16, 32 to 34 at λ = 1.25), against two directions' one knot of a few points per three seeds (O107). Her prediction (fewer per seed in three directions) fails on this reading, with the caveat that T53 is a warm bath holding a half-opened rod and O107 a cooled, fully opened sheet, so the protocols differ; the recurring piece sizes are unread from the wiring. A look.
- 2026-10-23. Where the curl and the uncurl sit once a slab has an open region (the owner's prediction, recorded first: closed curled rings inside the open space, the uncurl at the lip on a tiny fraction of flaws). (`sandbox/curl_in_open_space.py`, 7 s, on T56's 68 cells of saved end states, the slab 4 × L × L and the rod 4 × 4 × L under "all at the last" in a bath, 8 replicas each; output `sandbox/out/curl_in_open_space_2026-10-23.txt`.) Slabs with a fully open region (d = 3) exist only at λ = 1.25 and at 1.20 for g ≥ 2.5, with 25 to 49 % of points open; the untied controls never opened. In every such cell: closed rings of four five-square links with all four points open, 0 per seed everywhere (0 rings in all 64 opened slab end states); isolated surplus links inside the open space 4 to 15 per seed; missing squares inside the open space 0 to 9 of thousands, inside the curled region 0, at clean seams 0; every other missing square (hundreds to thousands per cell) touches a damaged point. So the uncurl does sit at the joints and seams and not in the mother or the open space (her half holds), and the curl does not form closed rings inside the open space at these settings (her half fails); what the open space holds is scattered single five-square links. Caveats: warm-bath end states, not cooled; the open regions are at most half the slab; in two directions the knots were read after a full opening and a cold hold (T51, O107). Kills the ring form at these settings; a cooled, fully opened slab is the test the picture needs and does not exist. A look.
- 2026-10-23: sandbox/torus_counting_two_ways.py, exact; the lattice tori at N = 144, 160, 192, 196 weighed under named and interchangeable points; out/torus_counting_two_ways_2026-10-23.txt; read in NOTEBOOK.md the same day.
- 2026-10-23: sandbox/torus_free_energy_one_switch.py, exact; every valid single switch out of each lattice torus at N = 144, 160, 192 at λ = 1, one-switch free energies; out/torus_free_energy_one_switch_2026-10-23.txt; her prediction (the tube wins at every finite coupling) recorded first and held; read in NOTEBOOK.md. *(Promoted the same day: O150; the zero-cost part is g ln 4, not g ln(2L + 1).)*
- 2026-10-23. Is the Sec. IV.2 geometrization of [T25] well defined on the toy's built graphs, and what does it read (design of the Eq. (45) ratio test, handoff item 2.3)? (`sandbox/eq45_geometrize_check.py`, 5 s, built graphs only, nothing from results/; output `sandbox/out/eq45_geometrize_check_2026-10-23.txt`.) With faces chosen point by point as the rotation of four corners with the smallest angle sum (Eq. 25) and K from Eq. (27): the review's own Fig. 7 tiling reads one type (4,4,4,6), K = −0.486 per square link length; the flat 14 × 14 torus, the tubes 4 × 36 and 16 × 4 and a curled ring spliced into a flat torus read (4,4,4,4), K = 0, at every point of the tube and at the ring's own points (on the tube the four between-ring squares are the faces and the ring square is a cycle round the tube, not a face); the review's Fig. 9 allotrope region reads (4,4,6,6), K = −0.926; summed over a closed surface the excess angle is fixed by its topology (a handle carries 4π, whatever its length). The rule ties on the 4-cube (three rotations of four squares). So under the review's own construction a curl is a handle, not a curvature, and the toy's curling cost has no counterpart on Eq. (45)'s curvature side. A look; nothing here is cited until `graphity.geometrize` pins it with tests.
- 2026-10-23. Is the Eq. (45) brief's first background nonempty, and what is the 2 × 2 grid's free energy in the warm cells? (`sandbox/eq45_background_support.py` and `sandbox/eq45_f2x2_fresh.py`, fresh chains with new seeds, not T78's; N = 196, λ = 1; nothing saved opened.) About 1.6 and 0.25 points per snapshot (of 196) lie at distance ≥ 2 from every 2 × 2 sighting at g = 3.300 and 3.697, so that background is nearly empty and was replaced in the brief by the plain mean; n_2×2/N ≈ 0.55 and 0.51, so F_2×2 ≈ +2.0 and +2.5. A look.
- 2026-10-23. The owner's idea: "without movement space has just 2 degrees of freedom, and that is what happens in the cold flat end." What do the toy's still, cold, perfect lattices read as a random-walk dimension? (`sandbox/cold_flat_dimension_look.py`, seconds, built shapes only; output `sandbox/out/cold_flat_dimension_look_2026-10-23.txt`.) Discrete walk inside T80's draft window, first step excluded: wide flat sheet 24 × 24, 1.89 to 1.97; narrow flat torus 6 × 96 (like the burp's product), 1.57 then 1.00 beyond its width; tube 4 × 96, 1.00; six-link cubic lattice 12³, 2.84 to 2.91. So a still lattice reads what its wiring builds in, and the burp's narrow product reads 1 at large scales, not 2 (corrects one clause of VISION Update 95 in place). A look.
- 2026-10-23. What does the stiff toy carry of a twist by its wiring alone (handoff item 2.2; definition proposed for her to confirm)? (`sandbox/twist_character_check.py`, about 30 s, built graphs only, nothing from results/; output `sandbox/out/twist_character_check_2026-10-23.txt`; revised twice after two adversarial checks.) Under the curvature brief's face rule, with ties completed every way and read region by region: the tube, its half-turn closure and the 4-cube are two-sided; the tube's zero-cost neighbour closed through a reflection is a Klein bottle (flipped cycles run along the tube, never round the curl); flat Klein grids exist in two families at zero energy (the odd-row family carries its flip on a diagonal zigzag, not a straight line); the curvature brief's built "handle" is a cross-handle (one-sided as built, two-sided mirrored); a hand-built lip of our own shape has no surface across its joint, all 32 local failures on or beside it. The seam shift of a lattice torus (O116's "shifted by two") is a second quantity the wiring fixes: a count with no sign. One-sided flat end states were already read (O116: 39 of 9,865 hold a one-sided piece, 5 whole Klein bottles; O122's 2 are two of those 5). No saved state is opened until she confirms the definition and gives her prediction. A look; full text `docs/design/twist_definition_2026-10-23.md`.
- 2026-10-23. After her decision to keep the six-link track (VISION Update 95): the held-out numbers that rule 14 requires before T71's and T74's L = 16 runs, fitted only on their read stage-1 files (L = 8 and 12), and a first design for the cooled, fully opened slab (handoff item 2.7). Drafts, each corrected after an adversarial check; nothing launched; her word owed on each. Scripts and the two amendment drafts in `sandbox/heldout_2026-10-23/`; the slab design in `docs/design/cooled_slab_design_2026-10-23.md`. Seen: both held-out runs test a prediction of hers that equals ours, so L = 16 checks the kernel's scaling, with one informative cell in T71 (λ = 1.10, r = 1/16); T71's control was fed 1/N_slab as much per point (now an O144 addendum); T74's largest jobs may approach the 24-hour Batch ceiling. For the slab, exact on built graphs: the planted opened patch is not past its barrier along its own construction (a single step of +40.8 at λ = 1.40 and +45 at 1.25 on the way to the next size), and no single switch grows it without breaking a point, so the design is not ready for her prediction; cheap exact checks come first. A look.
- 2026-10-23. Her picture of matter and antimatter as the two diagonals of one square, "sides of the same coin", "so energy does both at the same time": what does one square's geometry say? (`sandbox/square_diagonals_check.py`, instant, arithmetic; output `sandbox/out/square_diagonals_check_2026-10-23.txt`.) Euler's quadrilateral theorem, checked on 10,000 random quadrilaterals to 3e-14: with every side 1, the diagonals' squared lengths add to 4 minus four times the squared gap between their midpoints. Flat (a rhombus), d1² + d2² = 4 exactly: one diagonal shortens by just as much as the other lengthens (90°: 1.414 and 1.414; 60°: 1.000 and 1.732). Folded out of its plane along one diagonal, that diagonal keeps √2 and the other shortens (60° fold: 1.225). So in stage B's lengths a square's two diagonals are tied by one equation, which is her coin in the flat case; a fold is a different move. The two diagonals cross at the square's centre, which is not a point of the network. A look.
- 2026-10-23. The owner: "Let's start by observing the 1 column and 2 column?", with her expectation that above a few g anything lasts only a few sweeps. (`sandbox/column_look.py`, about four minutes, built graphs only, nothing from results/; output `sandbox/out/column_look_2026-10-23.txt`, write-up `.md` beside it; corrected after a fresh check before this line was written.) The 14-unit column, built as the six-around torus with three switches read off the chain's own column (isomorphic to it; O126's pattern, O107's census), is a square with two opposite curled sides whose ends tie to four collar points; all 14 units sit on those eight points; it lies in the tube's wall, its long side pointing half way round the tube; its exit is 6 (six moves), a dip, and the check found that exit is its whole barrier back to flat (0, 20, 20, 14 units from flat). The double column, a Q3 cap with a clean collar, comes either as a pair of caps of a cylinder eight around (built here as the "pill", the tube with six seam switches) or alone beside a knot of two kinds (the check's scan; the first version's "cannot sit alone" is withdrawn); per cap 8 units, all curl, zero at lambda = 1; exit 11, a dip. Under the face rule the column's negative curvature sits at the four collar points holding its energy; the rule closes no surface at either lip, and it gives K <= 0 on any graph of two kinds of point, so it cannot show her two signs. At lambda = 1.25, N = 64, 8 replicas: the first exit comes at a median of 14 to 37 sweeps for the column and 45 to 271 for the double column at g = 2.5 to 3.5 (1 to 4 in some replicas), but both mostly come back, and staying away for 1,000 sweeps takes a median of 446 to 1,370 for the column at g = 1.5 to 2.5 (half still there at 20,000 at g = 1.0) and 2,323 to more than 20,000 for the double column at g <= 2.5; from g = 3 the narrow host torus itself comes apart (its cheapest move costs 20, a wide sheet's 32). The column heals to exact flatness; the pill at g = 2.0 often ends with 20 units the detector cannot see. Her expectation fits the first trip out above g = 2.5 and fails if "lasts" means gone for good; which she means is hers. A look.
- 2026-10-24. The owner's particle handoff: the six immediate looks it asks for, on built lattices (`sandbox/particle_handoff_looks.py`, about 20 s; output `sandbox/out/particle_handoff_looks_2026-10-24.txt`; nothing from results/). The published lattice photon on the toy's flat tori: one polarisation with four links, two with six, frequencies 2 √(Σ sin²(kᵢ/2)) to 1e-14, group speed never above one link per tick (a choice of couplings). Half-curl under one energy: a 180° bend is undefinable on fixed links (holonomy U U⁻¹ = 1); a half turn round a square is its most expensive state, and a pulse launched with that holonomy kept 99 % of its energy where it started (links spinning over the top); a half-wave pulse travels at 0.90 and its energy is exactly amplitude squared times 9.806, so "half" fixes no unit. Charges on closed graphs add to zero (real, and mod 3; brute force over all 531,441 three-valued labellings of a 2 × 3 grid: exactly the 243 total-zero patterns occur); smallest allowed sets a pair and a same-way triple. Four quarter turns return every link with its orientation, so link-label states give +1 at 2π. Every observed particle in the handoff's table has 3Q + t ≡ 0 mod 3, so one quark-third cannot make charge −1 and three can. The 1 × 1 × 4 line is √18 = 3√2, same kind, primitive. Three equal twists have one placement, one odd twist three. A look.
- 2026-10-24. Why did Gate U1 fail at β = 8 (`results/gate_u1_2d.csv`)? (`sandbox/u1_gate_topology.py`, about two minutes, fresh seeds; output `sandbox/out/u1_gate_topology_2026-10-24.txt`.) The winding number Q (holonomies wrapped and summed with the alternating square signs; a whole number every time, asserted) never left 0 in 40 blocks of 500 single-link sweeps at β = 8 on 6 × 6 or 10 × 10, and took 5 to 8 values at β = 2. The exact zero-winding value, 0.93711 and 0.93591, is what the gate read (0.93716, 0.93607). With the winding move on, fresh seeds give 0.93688 ± 0.00019 and 0.93530 ± 0.00012 against the all-sector 0.93661 and 0.93526. A first version of this look summed the holonomies without the signs and counted wrong windings; corrected before this line. A look.
- 2026-10-24. The owner's answers (matter on body diagonals, dark on face diagonals; thirds and halves; the electron a 360° band; charge from signed thirds): what the lattice says (`sandbox/strand_answers_look.py`, seconds; output `sandbox/out/strand_answers_look_2026-10-24.txt`). Rings through a point: body diagonals 0 of three, 48 of four, 888 of six (they alternate kinds, so even only); face diagonals 24 triangles, 132 of four. Planes through a body diagonal holding a cube edge: 60° apart. The cube turns into itself every 120° about a body diagonal, 180° about a face diagonal, 90° about an edge (rotations tested against the lattice; a first version returned the trivial full turn for every axis and printed a fixed sentence, fixed before this line). Charge = −(signed thirds)/3 fits all eleven observed rows with the two quark assignments chosen to fit. A look.
- 2026-10-24. Gate U1′'s one failing point (10 × 10, β = 8): `sandbox/u1_gate_autocorr.py`, about ten minutes, four fresh chains of 40,000 sweeps with the winding move. Winding autocorrelation about 36 to 56 sweeps; time at Q = 0 about 66 % (rough expectation 71 %); ⟨cos φ⟩ uncorrelated (τ about 1 sweep), block errors equal autocorrelation errors; chains 0.93522, 0.93511, 0.93523, 0.93523 against the exact 0.93526 (0.4 to 1.7 errors each). Neither freezing nor small errors explains the gate's 3.65. A look.
- 2026-10-24. Light in curled space, after the owner's prediction ("same speed through curved space"): Bloch spectra of the photon field on 8 × 8 × 8, 6 × 8 × 8 and 4 × 8 × 8 (`sandbox/light_in_curled_space.py`, about a minute; output `sandbox/out/light_in_curled_space_2026-10-24.txt`). Flat and side 6 identical; side 4 keeps one massless polarisation at the flat speed and lifts the other to ω² = 4 + 4 sin²(k/2). Promoted the same day by an exact test (O151). A look.
- 2026-10-24. The owner's 1 × 1 × 2 diagonals (`sandbox/diagonal_112_look.py`, seconds; output `sandbox/out/diagonal_112_look_2026-10-24.txt`). In a 2 × 2 × 2 block of cubes 48, all same colour (face diagonals 72, body diagonals 32, all two-colour); in a 2 × 2 × 3 block 80 (104; 48); 12 per point unbounded. Shortest same-colour line off the coordinate planes, √6. No lattice turn about it short of 360°. Rings through a point: 24 triangles, 624 of four. A look.
- 2026-10-24. Strip positions at a corner and the energy of a ring by length (`sandbox/strip_corner_and_ring_energy.py`, instant; output `sandbox/out/strip_corner_and_ring_energy_2026-10-24.txt`). Planes through the line holding one cube edge: body diagonal 3 at 60° each; 1 × 1 × 2 diagonal 3 at 50.77°, 50.77°, 78.46°; face diagonal 2 distinct (the script's third is a repeat, angle 0) at 90°. Bending a strip into a circle of its own length, 2π²B/L: √2 13.958 B, √5 8.828 B, √6 8.058 B. A look.
- 2026-10-24. Correction to the light-in-curled-space line above: the polarisation along the curl is the Wilson-line scalar, not light; light keeps the flat speed (O151, corrected). The generalisation (`sandbox/u1_curl_mass_general.py`, written by an assistant agent, about 20 s, ten tori in two, three and four directions, Bloch formula equal to the full spectrum to 2e-13, independently rebuilt by a second agent) is promoted by `tests/test_u1.py::test_bloch_formula_with_side_four_rings_gives_the_whole_spectrum`. A look, then a test.
- 2026-10-24. The field's free energy by graph, for the rewiring-graph brief (`sandbox/u1_graph_free_energy.py`, seconds; output `sandbox/out/u1_graph_free_energy_2026-10-24.txt`). N = 64: sheet 8 × 8 has 64 squares, rank B 63, one closed square surface; tube 4 × 16 has 80 squares, rank 64, 16 closed surfaces. N = 144: sheet and 6 × 24 torus 144 squares, one surface each; tube 4 × 36 180 squares, 36 surfaces. Leading reward ln I₀(β) per square: tube over sheet +0.985, +3.775, +13.184 in ln(weight) at β = 0.5, 1, 2 (N = 64), equal to the tube's curling cost at λ = 1.25 when g = 65.0, 17.0, 4.85. A look.
- 2026-10-24. Correction to the free-energy line above (the audit, Update 102): the reward of ln I₀(β) per square holds under the Wilson weight only; under Q29's own energy each square gives e^(−β) I₀(β), a penalty (`sandbox/u1_normalisation_look.py`, instant, reading the exact output below). The counts stand.
- 2026-10-24. The exact field free energy, every surface term included (`sandbox/u1_exact_free_energy.py`, written by an assistant agent, about 20 s; output `sandbox/out/u1_exact_free_energy_2026-10-24.txt`; restored from the agent's transcript after the session that wrote it ended, rerun and identical; checked by an independent rebuild). Under the Wilson weight, tube minus sheet at N = 64: 4.033 at β = 1 (leading 3.775), 16.733 at β = 2 (13.184); Monte Carlo 4.032 ± 0.022 and 16.740 ± 0.034; per point the same at N = 144 to five decimals; the curling cost reaches zero at β = 3.59 exactly (4.28 at leading order). Under Q29's energy the effect reverses (λ_eff − 1 = 0.320 at β = 1, 0.339 at β = 2). A look.
- 2026-10-24. Light at a boundary between curled and flat space (`sandbox/u1_boundary_look.py`, written by an assistant agent, about three minutes; output `sandbox/out/u1_boundary_look_2026-10-24.txt`; restored from the transcript, rerun, identical but for timings; checked by an independent rebuild). A hand-built cylinder splitting into two tubes (side 4, and side 6 as control), four and six links, nothing read from results/. Field along the curl into side-4 tubes: reflected entirely at k = 0.6 and 1.2, 0.87 at k = 2.0, 0.99 at 2.6; what gets through converts into the first mode running round the tube; side 6 passes 72 to 92 %. Field along the open third direction with no pattern round the tube: passes entirely, both sides. No charge appears anywhere (it cannot, by Gauss's law, so her "no charge" is not tested by this). Her prediction neither killed nor supported. The checking agent found one set of numbers (pol z with a pattern round the tube) depends on the pattern's phase, which the output does not state. A look.
- 2026-10-25 `cube_sixty_degree_look.py`: the owner's 60-degree pieces and 12 squares at a point; exact (finite geometry); output `out/cube_sixty_degree_look.txt`. Kills nothing; crowns nothing.
- 2026-10-25 `opened_space_curvature_sign.py`: net curl minus uncurl in T51's 600 saved opened sheets; out `out/opened_space_curvature_sign.txt`. Kills the toy reason for C1's "ours negative"; crowns nothing.
- 2026-10-25 `zero_total_rule_reach_n18.py`: exact; the hard zero-total rule's moves join all 9 allowed classes at N = 18; out `out/zero_total_rule_reach_n18.txt`.
- 2026-10-25 `front_push_step.py`: push on a curled-flat front from light arriving from the curled side, continuum mass-step model; out `out/front_push_step.txt`. Never toward the open side. Kills light's push as the hold-back; crowns nothing.
- 2026-10-25 `local_pair_insertion_look.py`: every one-pair insertion with minimal rewiring (cut four links, or three with the new pair joined) near one point of a 10 x 10 flat torus, links within distance 4 (407,371 tried): none flat and valid; out `out/local_pair_insertion_look.txt`. Fits her "whole rows"; does not cover insertions with further rewiring.
- 2026-10-25 `soft_front_look.py` (run with PYTHONPATH=src): term 7's resting profile across a band of sources spreads over the whole gap (10-90 % width about L/3 at L = 24 and 48, whatever the band); with an added double well the wall is 2 to 6 links wide at any chain length and its tension approaches (4/3) sqrt(2 kappa a); out `out/soft_front_look.txt`. Kills a sharp front from term 7 as built; crowns nothing.
- 2026-10-25 `switch_influence_cone.py`: one switch's cone of influence on a flat 32 x 32 torus, lambda = 1.25, g = 2 to 8, 100 sweeps to settle and 200 followed; out `out/switch_influence_cone.txt`. JUMPS: at g = 2, 4, 5 the flat sheet takes 0, 1 and 12 switches in 305 sweeps (frozen, no spread); from g = 6 it melts (450 to 1,230 switches a sweep) and influence reaches all 1,024 points within 1 to 10 sweeps, with jumps of up to 7 links in one sweep, the reach stopping at about 7, the width of the melted graph. Kills a steady speed from the published move; crowns nothing.
- 2026-10-25 correction to the `switch_influence_cone.py` line above (the rule-22 audit, O157): JUMPS is withdrawn. No coupling had both motion and a flat sheet, and the reach was read once per chain sweep, which holds hundreds of switches in sequence; no test. The published move's non-locality is exact from its definition, not shown by the look. `soft_front_look.py`: the duplicated band at L = 24 removed.
- 2026-10-25 pair tie walls (`scripts/exact_walls_tie_shape_d.py --f=0,0,a,0`, exact, the existing script; out `out/pair_tie_walls.txt`): the rod 4 x 4 x 18 and the slab 4 x 12 x 12 both sit 2a per point above flat; cheapest single switch out, rod against slab: 30.4 / 36.8 (lambda 1.10), 29.6 / 31.2 (1.15), 28.8 / 25.6 (1.20), 28.0 / 20.0 (1.25), 25.6 / 3.2 (1.40); untied 25.6 / 43.2, 22.4 / 40.8, 19.2 / 38.4, 16.0 / 36.0, 4.8 / 28.8. Flat 64 throughout. Single moves only, not the true barrier (T54).
- 2026-10-25 `pair_tie_patch_look.py`: exact patch energies (T54's method) for the second opening (slab 4 x 12 x 12, k x k helix patch) and the first (rod 4 x 4 x 18, k whole rows of one curled direction opened), untied, "all at the last" and the pair tie; out `out/pair_tie_patch_look.txt`. Pair tie, slab peak 154 / 102 / 72 / 26 at lambda 1.15 / 1.20 / 1.25 / 1.40 (untied 488+ / 387 / 286 / 128, still rising at the largest patch below 1.40); rod: a seam of about 176 to 192, then a level plateau (each row releases nothing) until the last row. Second below first at every lambda tried under the pair tie. Two different patch shapes; neither shown to be the cheapest path.
- 2026-10-25 `pair_tie_bath_look.py`: the rod under the pair tie in T56's tied bath, lambda 1.20, 1.25, 1.40, g = 1.5, 2.0, 2.5, 4 replicas, 20,000 sweeps; out `out/pair_tie_bath/`. STAYS in 35 replicas of 36 (blips of up to 20 points that heal; acceptance a few in a million at g = 2.5). One BREAKS, lambda 1.40, g = 2.5, replica 3: still at sweep 15,000, then within 3,000 sweeps 68 points at d = 3, 26 at d = 2, 74 broken (largest open region 26), and resting there to 20,000. Where it started, the second direction followed, and the breakage kept pace.
- 2026-10-26 `pair_tie_push_look.py`: one concentrated push into the rod 4 x 4 x 18, sealed, packed into one point under the per-vertex bath (`run_sealed_curled_d.py`, unchanged); pair tie at lambda 1.20, 1.25, 1.40, untied at 1.25 and 1.40; E = 32, 64, 128, 256, 512; 4 replicas, 10,000 sweeps; out `out/pair_tie_push/`. Words declared in the script before the run. No BOTH OPEN in 100 replicas. Pair tie: STAYS at lambda 1.20 (20 of 20) and 1.25 (19 of 20; one BREAKS at E = 512); at 1.40 STAYS to E = 64, one BREAKS at 128, BREAKS 8 of 8 at 256 and 512 (21 to 34 % of points broken, 41 to 71 % of opened points at d = 3). Untied: BREAKS 20 of 20 at 1.40 from E = 32 (26 to 31 % broken, about a third of opened points at d = 3); mixed at 1.25, BREAKS 4 of 4 at E = 512. Drift at most 7e-13; every replica left its start.
- 2026-10-26 `breakage_anticurl_look.py`: the push look's 100 saved end states read for curl (S_e > 4) and anticurl (S_e < 4), no new run. 85 to 100 % of the anticurl sits on links touching a broken point (d > 3). Curl falls from 576 toward about 200 and anticurl rises from 0 to about 200 in the most broken runs, so curl minus anticurl goes from 576 to between -20 and 40 there (432 in the least broken). The remaining curl is not gathered beside the broken points: its share within one link of one is below the share of links there in every replica checked (0.88 against 0.95, 0.28 against 0.68).
- 2026-10-26 `hard_rule_moves_look.py`: every single switch from one point of the flat 6 x 6 x 8 torus and of the rod 4 x 4 x 18, by change in squares. None keeps the count: flat loses 4 to 8 (3,514 valid switches), the rod 4 to 10 (3,946).
- 2026-10-26 `hard_rule_pairs_look.py`: pairs of switches out of the flat torus, the second within 1 or 2 links of the first, restoring the count: 3,514 pairs at either radius, and every one returns the starting graph exactly (checked by edge set). In three damaged end states of the push look (curl 202 / anticurl 206; 185 / 205; 493 / 61), 84, 114 and 28 of about 550,000 valid single switches keep the count.
- 2026-10-26 correction (O159; Codex F21, F22): `hard_rule_pairs_look.py` missed the undo written from the other side; every "restoring pair" above was the undo, and "checked by edge set" was a scratch check, not the script. Fixed (both forms excluded; edge sets now compared) and rerun: 0 restoring pairs at radius 1 and 2. The damaged-state counts above counted each switch twice; now in the script (`damaged`), once: 42 of 274,248; 57 of 272,560; 14 of 282,861.
- 2026-10-26 correction (O159; Codex F15, F16, F17) to the `breakage_anticurl_look.py` line: "85 to 100 %" holds in 79 of 100 end states (below 0.85 in 16, minimum 0.27; four with anticurl and no broken point); the curl beside broken points is at chance untied at 1.40 and below it otherwise, against a baseline of 63 to 99 % of links; the least-moved runs end at 552, not 432.
- 2026-10-26 note (O159; Codex F12): the bath look's seed formula gave lam 1.20, g 2.5 and lam 1.40, g 1.5 the same seed, 20261165; both STAY.


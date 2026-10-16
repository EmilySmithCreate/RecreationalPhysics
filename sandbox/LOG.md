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
  a look. Not promoted.
- 2026-10-16. **A feed instead of a spark** (the owner: "a flow with various rates based on what black hole eats and
  so it's one spot per seed"; `sandbox/slab_feed.py` → `sandbox/out/slab_feed.txt`). Untied slab 4 × 8 × 8, λ = 1.25,
  4N empty stores, r units a sweep into one shared store or one point's own store. First try (rates 2, 8, 32 over
  10,000 sweeps; `slab_feed_try1.txt`): the two rows that finished had every point broken and 12 units a store, so the
  rates were far too high; lowered to 0.25 to 16 with a damage stop, rows unread as this line is written. Reading
  appended when it finishes.

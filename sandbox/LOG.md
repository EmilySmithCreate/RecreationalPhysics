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

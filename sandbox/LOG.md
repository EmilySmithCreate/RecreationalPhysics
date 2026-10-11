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

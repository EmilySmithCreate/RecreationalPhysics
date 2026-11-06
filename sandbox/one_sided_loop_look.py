"""A look (sandbox lane; the owner's picture of 31 October: dark matter is a one-sided loop, the neutrino a two-sided one
made of two half-twist loops of opposite hand; "a one sided structure can hold half a loop, so a curl held in 1/2 the
length that a neutrino has"). Exact arithmetic on the twist term as built (E4 per loop, elastic + mismatch, eps = 1,
flat loop): a closed band is one-sided exactly when its total twist is an odd multiple of one half (a Mobius band).

Predictions (ours, written before running):
  1. Box diagonals carry twist in thirds, and no multiple of 1/3 is an odd multiple of 1/2, so NO loop of box diagonals is
     one-sided as built. One-sidedness forces the dark loop onto the face diagonals (halves), where her 30 October
     assignment already put it.
  2. On face diagonals the cheapest one-sided loop is (1/2, 0, ..., 0): elastic 1/4, mismatch 2 * 1/4 = 1/2, total 3/4,
     the same at every length from the triangle up (no size selected).
  3. The two-sided neutrino (+1/2, -1/2, net 0) costs 3/2 at four or more (recorded 30 October). So the one-sided loop costs
     exactly HALF the neutrino under this term: her "half" appears as a cost, not as a length, since neither selects a length.
  4. Under charge = net twist (her decision of 30 October) the one-sided loop has charge +-1/2, which `check_whole_charge`
     refuses for a lone particle. So her one-sided dark loop and that rule cannot both stand unless face twist is a dark
     charge of its own (her decision of 26 September, Update 34) that light does not see.
Crowns nothing.
"""
from fractions import Fraction as F
from itertools import product


def cost(taus):
    n = len(taus)
    return sum(t * t for t in taus) + sum((taus[(i + 1) % n] - taus[i]) ** 2 for i in range(n))


def cheapest(n, inc, one_sided):
    vals = [F(k, inc) for k in range(-inc, inc + 1)]
    best = None
    for taus in product(vals, repeat=n):
        T = sum(taus, F(0))
        if one_sided:
            ok = (2 * T).denominator == 1 and (2 * T).numerator % 2 == 1
        else:
            ok = T == 0 and any(t != 0 for t in taus)
        if ok:
            c = cost(taus)
            if best is None or c < best[0]:
                best = (c, taus)
    return best


print("box diagonals (thirds), one-sided loops at n = 3..6:", [cheapest(n, 3, True) for n in (3, 4, 5, 6)])
for n in (3, 4, 5, 6):
    print("face (halves), n = %d: one-sided %s ; two-sided neutrino %s" % (n, cheapest(n, 2, True), cheapest(n, 2, False)))

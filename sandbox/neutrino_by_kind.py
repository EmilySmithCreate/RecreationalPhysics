"""A look (sandbox lane; the owner's decision of 30 October, 21:5x UTC: "agreed, proceed" on letting the twist constant
differ by kind of diagonal, and her "proceed" on the two-loop neutrino under signed curl, box against face). Predictions
first, written before the enumeration ran.

The term: E4 per loop, elastic + mismatch, with its own constant per kind: eps_box on box diagonals (thirds), eps_face on
face diagonals (halves); flat loops, writhe 0; curl is signed and E4 does not price it, so the two loops' curls +1 and -1
cost nothing and only let the particle net zero. The particle: two loops, net twist 0 over the particle, twist present
on at least one loop (spin 1/2 needs it), curl net 0.

Two ways the twist can cancel: (W) within each loop (each loop nets 0, twist present); (A) across the loops (one loop
nets +inc, the other -inc: her "2 half twist loops cancel").

Predictions (ours, arithmetic, written before running):
  (A) is cheaper than (W) for both kinds. A loop with one non-zero diagonal t costs t^2 + 2 t^2 = 3 t^2 at every length:
      box (t = 1/3) 1/3 per loop, 2/3 the pair; face (t = 1/2) 3/4 per loop, 3/2 the pair. No length is selected (n >= 3).
  (W): box 2/3 per loop at n >= 4 (4/3 the pair); face 3/2 per loop at n >= 4 (3 the pair). Known from the earlier look.
  The dark (face) pair wins when eps_face * 3/2 < eps_box * 2/3 under (A), i.e. eps_face / eps_box < 4/9; and under (W)
      when eps_face * 3 < eps_box * 4/3, the SAME threshold 4/9. So one number decides, whichever way the twist cancels.
  Can eps differ by kind so that the dark loop wins? Yes, exactly when eps_face < (4/9) eps_box. It is a second constant,
      pinned by nothing yet; with the electron pinning eps_box, the neutrino's own cost would pin eps_face.
Crowns nothing.
"""
from fractions import Fraction as F
from itertools import product


def cheapest(n, inc, net, need_twist):
    vals = [F(k, inc) for k in range(-inc, inc + 1)]
    best = None
    for taus in product(vals, repeat=n):
        if sum(taus) != net or (need_twist and not any(taus)):
            continue
        e = sum(t * t for t in taus) + sum((taus[(i + 1) % n] - taus[i]) ** 2 for i in range(n))
        if best is None or e < best[0]:
            best = (e, taus)
    return best


if __name__ == "__main__":
    for kind, inc in (("box (thirds)", 3), ("face (halves)", 2)):
        print(kind)
        for n in (3, 4, 5, 6):
            w = cheapest(n, inc, F(0), True)
            a = cheapest(n, inc, F(1, inc), False)
            print("  n = %d: (W) one loop netting 0, twist present: %s %s | (A) one loop netting +1/%d: %s %s | pair (W) %s, pair (A) %s"
                  % (n, w[0], w[1], inc, a[0], a[1], 2 * w[0], 2 * a[0]))
    print("threshold: the face pair is cheaper than the box pair iff eps_face/eps_box < (2/3)/(3/2) = 4/9 under (A) and < (4/3)/3 = 4/9 under (W)")

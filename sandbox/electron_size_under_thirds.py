"""A look (sandbox lane; her agreement of 30 October, "proceed"). Expectation first.

Question: under the working twist term E4 (elastic + mismatch; writhe zero on a flat loop) what is the cheapest loop of n
diagonals holding charge -1, when each diagonal's twist must be a multiple of a third (the state as built), against
when it may be any real number (her continuous picture)?
Expectation (ours, arithmetic): continuous, the minimum is T^2/n, falling with n, so no size is selected. In thirds, any
set of multiples of 1/3 summing to -1 has sum of squares at least 1/3 (equality: three diagonals at -1/3, the rest 0),
so the elastic piece does not fall with n; the mismatch piece is 0 on the triangle and at least 2/9 for n >= 4 (the
three thirds adjacent). So in thirds the triangle is the unique cheapest loop: the electron's size n = 3 is selected by
the term with nothing added. Checked by enumeration below for n = 3 to 8 with twists in {-1, -2/3, ..., 1}.
Crowns nothing.
"""
from fractions import Fraction as F
from itertools import product

if __name__ == "__main__":
    vals = [F(k, 3) for k in range(-3, 4)]
    print(" n  min E4 in thirds (elastic, mismatch)   continuous T^2/n")
    for n in range(3, 9):
        best = None
        for taus in product(vals, repeat=n):
            if sum(taus) != -1:
                continue
            el = sum(t * t for t in taus)
            mm = sum((taus[(i + 1) % n] - taus[i]) ** 2 for i in range(n))
            e = el + mm
            if best is None or e < best[0]:
                best = (e, el, mm, taus)
        e, el, mm, taus = best
        print("%2d  %-8s (%s, %s)  example %s   %s" % (n, e, el, mm, tuple(str(t) for t in taus), F(1, n)))
    print("Crowns nothing.")

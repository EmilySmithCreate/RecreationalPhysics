"""A look (sandbox lane; the owner's question of 30 October: is charge as the linking number, Lk = Tw + Wr, consistent
with the other rules?). Exact arithmetic on the built state, expectations first.

The published theorem (Calugareanu-White-Fuller; general knowledge, to verify): for a CLOSED ribbon, Lk = Tw + Wr with Lk a
whole number. So if charge were Lk, (a) a closed loop could not carry a third alone, and (b) on a loop whose polygon
writhes, the twist held would have to be a whole number minus that writhe, which is not a third unless the writhe is.
Expectation (ours): the triangle (three points) is always planar, so Wr = 0 and Tw = Lk there: the electron is safe under
either reading. A loop of four or more box diagonals can be non-planar, and its writhe is a generic real, not a third,
so under charge = Lk its twist could not be in thirds. The look computes the writhe of every closed quadrilateral and
pentagon of box diagonals from the origin on an 8-torus (non-winding) and reports the writhes and whether any non-zero
one is a multiple of 1/3 to 1e-6. Crowns nothing.
"""
from itertools import product
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from graphity.twist import BOX_STEPS, Loop, writhe  # noqa: E402

if __name__ == "__main__":
    steps = sorted(BOX_STEPS)
    for n in (4, 5):
        seen, values = set(), []
        for combo in product(steps, repeat=n):
            if tuple(sum(s[k] for s in combo) for k in range(3)) != (0, 0, 0):
                continue
            key = tuple(sorted(combo))
            try:
                w = writhe(Loop(8, (0, 0, 0), list(combo), [0] * n))
            except ValueError:
                continue
            if w is None or w != w:   # winding, or coincident segments
                continue
            values.append(w)
        nz = [abs(w) for w in values if abs(w) > 1e-6]
        thirds = [w for w in nz if abs(w * 3 - round(w * 3)) < 1e-6]
        print("n = %d: %d closed loops, %d with non-zero writhe; |Wr| ranges %.3f to %.3f; multiples of 1/3 among them: %d" % (
            n, len(values), len(nz), min(nz) if nz else 0, max(nz) if nz else 0, len(thirds)))
        print("   examples:", ", ".join("%.3f" % w for w in sorted(set(round(w, 3) for w in nz))[:8]))
    print("Crowns nothing.")

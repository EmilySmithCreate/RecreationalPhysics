"""Sandbox look, 27 October 2026: is a row segment inserted between two existing flaws clean? (Rule 16: a look can kill,
never crown. Words declared here before anything ran.)

The owner's idea (20 October, VISION Update 75, her words): growth is by whole rows, and "a smaller segment ... will only
work if there's two existing flaws lined up so that the two row additions can take advantage of as the end points of the
line segment otherwise it has to go across all of space." Her prediction for this look, 27 October, 03:02 UTC: CLEAN
SEGMENT. The counts of 26 and 27 October (three and four switches among existing points) found only relabelings; this
look adds points, which those counts never did.

What is built, exactly. On a flat torus a double row (two new points per position, one of each kind, so the two kinds
stay equal) is inserted along one axis between coordinates y0 and y0 + 1 over a set P of positions in the other axes:
the old link A_p-B_p is cut, r1_p and r2_p are added with A_p-r1_p, r1_p-r2_p, r2_p-B_p, and r1 (r2) points at adjacent
positions are linked. Over every position (P = everything) this is the whole row of the record: flat, every link back on
its proper number of squares, cost zero (exact, O116 and the 20 October looks). Over a segment, each position q just
outside P beside one position p of P closes the segment's end the one way that keeps every point on 2D links and the two
kinds apart: A_q-B_q is cut and A_q-r2_p, B_q-r1_p are added (the canonical closure; a segment's end is then a dislocation,
a flaw). A q beside two positions of P (a segment one short of the whole row) takes the only closure left, A_q-r2_p,
B_q-r1_p' and r1_p-r2_p', and is reported apart.

What is read, exactly, for segments of every length k on the 16 x 10 and 24 x 12 four-link tori (the hard rule S = N) and
for strips on the 6 x 6 x 8 and 12 x 6 x 8 six-link tori and rectangular patches on 6 x 6 x 8 (S = 3N; the longer torus
added after the first run showed the two ends of a strip meeting round a side of 6, as the census of 26 October found): the hard-core validity; the energy H at
lambda 1.25 (cqg_d.hamiltonian, checked against cqg.hamiltonian at four links); the increment H(k) - H(k - 1), which is
the cost of lengthening a segment by one position between its two existing end flaws; the off-flat census (points at a
local dimension other than D); and the end flaw read from its wiring (squares on each link at the end). Then, at one
end of a k = 5 segment on 16 x 10, every single-cut closure within R = 3 steps of the end is tried in place of the
canonical one, to see whether the canonical closure is the cheapest and by how much (scope: one cut link and the two
links it frees, nothing wider; the 20 October pair look's 42 at k = 1 is the comparison).

Words. CLEAN SEGMENT: for every k from k0 up to L - 2 the increment H(k) - H(k - 1) is exactly zero and the off-flat
census does not change, so lengthening a segment between its two existing flaws costs nothing and makes no new flaw,
and the whole row has H = 0; k0 is reported (the ends interact below it). FLAWED: the increment is nonzero at some
k >= k0 < L - 2, or new off-flat points appear away from the ends. The same words for the six-link strip; for the
six-link patch the cost against the perimeter is reported with no word (nothing was predicted for it). Starting states
obey the hard rule (flat tori, curl 0, anticurl 0). Ours, before running: CLEAN SEGMENT by the locality of H (a sum of
per-link terms that see two steps), with k0 about 3; the number to learn is the end flaw's cost and shape.
"""
import itertools
import sys
from collections import Counter
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from graphity import cqg, cqg_d  # noqa: E402
from graphity.dimension import local_dimension, local_dimension_d  # noqa: E402

LAM = 1.25


def strides_of(dims):
    return [int(np.prod(dims[a + 1:])) for a in range(len(dims))]


def idx(c, dims):
    return int(sum(int(ci) * s for ci, s in zip(c, strides_of(dims))))


def insert_segment(dims, axis, y0, P):
    """Returns (adj, part, info) or None if the result is not 2D-regular and simple. P: set of tuples over the other
    axes (in axis order, `axis` left out)."""
    adj0, part0 = cqg_d.torus(dims)
    n, deg = adj0.shape
    D = len(dims)
    oth = [b for b in range(D) if b != axis]
    nb = [set(int(x) for x in adj0[i]) for i in range(n)]
    part = list(int(x) for x in part0)
    P = set(tuple(int(x) for x in p) for p in P)

    def full(p, yv):
        c = [0] * D
        c[axis] = yv % dims[axis]
        for b, v in zip(oth, p):
            c[b] = v % dims[b]
        return idx(c, dims)

    r1, r2 = {}, {}
    for p in P:
        A, B = full(p, y0), full(p, y0 + 1)
        assert B in nb[A]
        nb[A].discard(B); nb[B].discard(A)
        u, v = len(nb), len(nb) + 1
        nb.append(set()); nb.append(set())
        part += [part[B], part[A]]
        r1[p], r2[p] = u, v
        nb[A].add(u); nb[u].add(A)
        nb[u].add(v); nb[v].add(u)
        nb[v].add(B); nb[B].add(v)
    boundary = {}
    for p in P:
        for j, b in enumerate(oth):
            for step in (1, -1):
                q = list(p)
                q[j] = (q[j] + step) % dims[b]
                q = tuple(q)
                if q in P:
                    nb[r1[p]].add(r1[q]); nb[r1[q]].add(r1[p])
                    nb[r2[p]].add(r2[q]); nb[r2[q]].add(r2[p])
                else:
                    boundary.setdefault(q, []).append(p)
    special = 0
    for q, ps in boundary.items():
        A, B = full(q, y0), full(q, y0 + 1)
        assert B in nb[A]
        nb[A].discard(B); nb[B].discard(A)
        if len(ps) == 1:
            p = ps[0]
            nb[A].add(r2[p]); nb[r2[p]].add(A)
            nb[B].add(r1[p]); nb[r1[p]].add(B)
        elif len(ps) == 2:
            p, pp = ps
            nb[A].add(r2[p]); nb[r2[p]].add(A)
            nb[B].add(r1[pp]); nb[r1[pp]].add(B)
            nb[r1[p]].add(r2[pp]); nb[r2[pp]].add(r1[p])
            special += 1
        else:
            return None
    if any(len(s) != deg for s in nb):
        return None
    adj = np.array([sorted(s) for s in nb], dtype=np.int64)
    part = np.array(part, dtype=np.int64)
    for u in range(len(nb)):
        for v in nb[u]:
            if part[u] == part[v]:
                return None
    ends = sorted(set(r1.values()) | set(r2.values()))
    return adj, part, dict(special=special, new=ends, boundary=boundary, r1=r1, r2=r2)


def read(adj, part, D, lam=LAM):
    valid = bool(cqg_d.is_valid(adj))
    h = float(cqg_d.hamiltonian(adj, lam))
    if D == 2:
        h2 = float(cqg.hamiltonian(adj, lam))
        assert abs(h - h2) < 1e-9, (h, h2)
        d = local_dimension(adj)
    else:
        d = local_dimension_d(adj)
    off = int((d != D).sum())
    squares = Counter()
    mins = 10 ** 9
    for u in range(adj.shape[0]):
        for v in adj[u]:
            if u < int(v):
                s = int(cqg_d.squares_on_edge(adj, u, int(v)))
                squares[s] += 1
                mins = min(mins, s)
    return dict(valid=valid, H=h, off=off, squares=dict(sorted(squares.items())), min_sq=mins, dim=d)


def flaw_wiring(adj, d, info, D):
    """The end flaw read from its wiring: for each point at a local dimension other than D, its links' square counts."""
    out = []
    for u in np.flatnonzero(d != D):
        out.append((int(u), int(d[u]), tuple(sorted(int(cqg_d.squares_on_edge(adj, int(u), int(v))) for v in adj[u]))))
    return out


def segment_table(dims, axis, k_max, label, strip_axes=None):
    D = len(dims)
    flat = 2 * (D - 1)
    print(f"\n== {label}: flat torus {dims}, H = {float(cqg_d.hamiltonian(cqg_d.torus(dims)[0], LAM)):.1f}, "
          f"flat links carry {flat} squares; insertion along axis {axis} between {0} and {1}")
    prev = None
    rows = []
    for k in range(1, k_max + 1):
        if strip_axes is None:
            P = [(x,) for x in range(k)]
        else:
            P = [(x, y) for x in range(k) for y in range(dims[strip_axes])]
        res = insert_segment(dims, axis, 0, P)
        if res is None:
            print(f"  k = {k}: no 2D-regular bipartite closure built")
            prev = None
            continue
        adj, part, info = res
        r = read(adj, part, D)
        inc = None if prev is None else r["H"] - prev
        tag = " (one short of the whole row: the special closure)" if info["special"] else ""
        tag = " (the whole row)" if k == k_max else tag
        print(f"  k = {k:2d}: N = {adj.shape[0]}, valid {r['valid']}, H = {r['H']:7.1f}, increment "
              f"{'   -  ' if inc is None else f'{inc:+6.1f}'}, off-flat points {r['off']:3d}, squares per link "
              f"{r['squares']}{tag}")
        rows.append((k, r["H"], inc, r["off"], info["special"], r["valid"]))
        if k in (1, 2, 5) or (k == k_max - 1):
            fw = flaw_wiring(adj, r["dim"], info, D)
            if fw:
                kinds = Counter((dd, sq) for _, dd, sq in fw)
                print(f"      off-flat points by (local dimension, squares on their links): {dict(kinds)}")
        prev = r["H"]
    return rows


def zero_run(rows):
    """A plain fact beside the word: the longest run of consecutive k with increment exactly 0 and the off-flat census
    unchanged (the canonical closures only), as (first k, last k, H, off-flat points)."""
    best, cur = None, None
    for (k, h, inc, off, sp, ok) in rows:
        if inc is not None and abs(inc) < 1e-9 and not sp and cur is not None and cur[3] == off:
            cur = (cur[0], k, h, off)
        else:
            cur = (k, k, h, off) if (ok and not sp) else None
        if cur and (best is None or cur[1] - cur[0] > best[1] - best[0]):
            best = cur
    return best


def word_for(rows, k_max):
    """CLEAN SEGMENT / FLAWED by the docstring, with k0."""
    plain = [(k, h, inc, off, sp, ok) for (k, h, inc, off, sp, ok) in rows if not sp and k < k_max]
    if any(not ok for *_, ok in rows):
        return "FLAWED (an invalid state)", None
    k0 = None
    for i in range(1, len(plain)):
        k, h, inc, off, sp, ok = plain[i]
        if abs(inc) < 1e-9 and plain[i - 1][3] == off:
            tail = plain[i:]
            if all(abs(t[2]) < 1e-9 and t[3] == off for t in tail):
                k0 = plain[i - 1][0]
                break
    whole = [h for (k, h, *_rest) in rows if k == k_max]
    if k0 is None or not whole or abs(whole[0]) > 1e-9:
        return "FLAWED", k0
    return "CLEAN SEGMENT", k0


def closure_search(dims, k, R):
    """At the left end of a k-segment on the four-link torus, replace the canonical cut (A_q-B_q) by any single link
    within R steps of the end whose two ends have the parities r2_p and r1_p need; keep the right end canonical."""
    D = 2
    P = [(x,) for x in range(k)]
    adj0, part0 = cqg_d.torus(dims)
    n0 = adj0.shape[0]
    base = insert_segment(dims, 1, 0, P)
    adj_c, part_c, info = base
    h_c = read(adj_c, part_c, D)["H"]
    p = (0,)
    A_p, B_p = idx((0, 0), dims), idx((0, 1), dims)
    q = ((-1) % dims[0],)
    A_q, B_q = idx((q[0], 0), dims), idx((q[0], 1), dims)
    u1, u2 = info["r1"][p], info["r2"][p]
    # distances in the original torus from the end's two old points
    dist = {A_p: 0, B_p: 0}
    frontier = [A_p, B_p]
    for step in range(1, R + 1):
        nxt = []
        for s in frontier:
            for t in adj0[s]:
                t = int(t)
                if t not in dist:
                    dist[t] = step; nxt.append(t)
        frontier = nxt
    near = set(dist)
    # the canonical graph with the left closure undone: remove A_q-r2_p, B_q-r1_p, restore A_q-B_q
    nb = [set(int(x) for x in adj_c[i]) for i in range(adj_c.shape[0])]
    nb[A_q].discard(u2); nb[u2].discard(A_q); nb[B_q].discard(u1); nb[u1].discard(B_q)
    nb[A_q].add(B_q); nb[B_q].add(A_q)
    touched = {idx((x, 0), dims) for x in range(k)} | {idx((x, 1), dims) for x in range(k)}
    results = []
    tried = 0
    for s in sorted(near):
        for t in sorted(nb[s]):
            if t < n0 and s < t and s in near and t in near and s not in touched and t not in touched:
                for (ss, tt) in ((s, t), (t, s)):
                    if part_c[ss] == part_c[B_p] and part_c[tt] == part_c[A_p]:
                        tried += 1
                        nb2 = [set(x) for x in nb]
                        nb2[ss].discard(tt); nb2[tt].discard(ss)
                        nb2[ss].add(u2); nb2[u2].add(ss); nb2[tt].add(u1); nb2[u1].add(tt)
                        if any(len(x) != 4 for x in nb2):
                            continue
                        adj = np.array([sorted(x) for x in nb2], dtype=np.int64)
                        if not cqg_d.is_valid(adj):
                            continue
                        h = float(cqg_d.hamiltonian(adj, LAM))
                        canon = (ss, tt) == (A_q, B_q)
                        results.append((h, ss, tt, canon))
    results.sort()
    print(f"\n== closure search, {dims}, k = {k}, left end, single cut within R = {R}: {tried} candidate cuts, "
          f"{len(results)} valid; canonical H = {h_c:.1f}")
    for h, ss, tt, canon in results[:6]:
        print(f"    H = {h:6.1f} cut ({ss}, {tt}){' <- canonical' if canon else ''}")
    best = results[0][0] if results else None
    print(f"    cheapest {best}; canonical is {'the cheapest' if best is not None and abs(best - h_c) < 1e-9 else 'NOT the cheapest'}")


def patch_table(dims, axis):
    D = len(dims)
    print(f"\n== six-link rectangular patches on {dims}, insertion along axis {axis}: cost against perimeter")
    for a, b in ((1, 1), (2, 1), (2, 2), (3, 2), (3, 3), (4, 3), (4, 4), (4, 2)):
        P = [(x, y) for x in range(a) for y in range(b)]
        res = insert_segment(dims, axis, 0, P)
        if res is None:
            print(f"  patch {a} x {b}: not built")
            continue
        adj, part, info = res
        r = read(adj, part, D)
        per = 2 * (a + b)
        print(f"  patch {a} x {b}: valid {r['valid']}, H = {r['H']:7.1f}, perimeter {per}, H / perimeter "
              f"{r['H'] / per:6.2f}, off-flat points {r['off']}, squares per link {r['squares']}")


if __name__ == "__main__":
    rows = segment_table((16, 10), 1, 16, "four links, 16 x 10 (segment along x, two rows added along y)")
    w, k0 = word_for(rows, 16)
    print(f"  WORD (four links, 16 x 10): {w}, k0 = {k0}; zero-increment run (first k, last k, H, off-flat) {zero_run(rows)}")
    rows = segment_table((24, 12), 1, 24, "four links, 24 x 12")
    w, k0 = word_for(rows, 24)
    print(f"  WORD (four links, 24 x 12): {w}, k0 = {k0}; zero-increment run {zero_run(rows)}")
    closure_search((16, 10), 5, 3)
    for dims in ((6, 6, 8), (12, 6, 8)):
        rows = segment_table(dims, 2, dims[0], f"six links, {dims[0]} x {dims[1]} x {dims[2]} strip (full in y, a segment "
                             f"in x; two planes added along z)", strip_axes=1)
        w, k0 = word_for(rows, dims[0])
        print(f"  WORD (six links, strip {dims}): {w}, k0 = {k0}; zero-increment run {zero_run(rows)}")
    patch_table((6, 6, 8), 2)

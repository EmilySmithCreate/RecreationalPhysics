"""Sandbox look, 23 October 2026 (CLAUDE.md rule 16: a look; it can kill, not crown). BUILT GRAPHS ONLY: nothing
is read from results/ (the T51, T55 and tube end states are held for the twist test's registered version).

The owner asked (sandbox/NOTEBOOK.md, 23 October): "Let's start by observing the 1 column and 2 column?" Her
expectation, recorded before this ran: "Typically anything only lasts a few sweeps higher than a few g."

WHAT THE RECORD SAYS THE TWO OBJECTS ARE, BY THEIR WIRING (read first; quoted in sandbox/out/column_look_2026-10-23.md)
  * The column (paper 2's relic; O16's "four-point remnant", O28's "closed loop of four", O107's "column"): a connected
    piece of exactly four points, all at d = 1 (analyse_t37.leftovers; analyse_t55.is_column). O126 read 2,045 of
    them: the common 14-unit kind has two OPPOSITE sides of the loop on three squares, the other two on two, and at
    each point one link out on three and one on two (X = 6, S = N + 1, 24 lambda - 16); the 4-unit kind has all four
    sides on three and every link out on two (X = 4). Removing its four points never cuts the tube: it lies IN the
    wall of the six-around torus, not round it (O16's correction, confirmed by O126). "4 units at its points, 14
    within one step" (O107).
  * The double column (O107; the "3-cube" of O28): eight points at d = 1 with twelve links among them, each point
    three inside and one out, "8 units at their points and nothing more within one step": the wiring of a 4 x 2
    segment of the tube left curled (X = 8, S = N + 2, 8 units at lambda = 1.25).
  * Where they live: in the burp's product, which is the 4 x L tube re-glued with its ring seam shifted by two, six
    around, exactly flat (O116; run_sixloop_widen.seam_shifted(L, 2)); and in T51's 1,024-point sheets of the same kind.

HOW EACH WAS BUILT HERE (the record's text does not say how the collar is sewn, so the text alone was not enough)
  The toy's own chain was run on a BUILT 4 x 16 tube (cqg.torus, lambda = 1.25, g = 1.5, Metropolis) with a snapshot
  every five sweeps; the first snapshot holding exactly one piece of four points at d = 1 with every other point at
  d = 2 and H = 14 was kept (scratch script, this session; no saved state). Its wiring was read: O126's pattern to
  the letter. A breadth-first search over the chain's own switches found that it is THREE switches from a flat graph,
  and that flat graph is isomorphic (networkx) to seam_shifted(16, 2), the six-around torus, and not to the tube.
  The three switches, mapped through the isomorphism onto the torus's (x, y) coordinates, are the recipe below:
  column() applies them to seam_shifted(L, 2) and the result is isomorphic to the chain's column.
  The double column was built as the pair the chain made in two of sixty seeds: two Q3 caps of a cylinder of
  squares eight around, with nothing else in the graph (H = 16 = 8 + 8). double_column() builds that pair by hand
  (the "pill": the tube with six seam switches) and the cap at rings (8, 9) is observed; its neighbourhood matches
  the chain's cap out to three steps (induced subgraphs isomorphic); the whole graphs differ in how the cylinder
  between the caps is glued. *Corrected 23 October, by the check:* this look first said a clean-collared Q3 "cannot
  sit alone". That is withdrawn. In the check's own scan (150 seeds, same setting) the chain made a single Q3 with a
  clean collar in two seeds, beside four pieces of two three to four steps away (H = 38; in kind O107's knot of two
  kinds), lasting about 17,800 sweeps in one. So a clean-collared Q3 comes either with a second cap or beside a knot
  of two kinds; the layer argument in double_column's docstring is ours, unverified. Only the pill form is timed here.

WHAT IS LOOKED AT (all on the built graphs; lambda = 1.25 unless said)
  (a) energy at lambda = 1 and 1.25 split into missing squares, 16 (N - S), and surplus squares, 4 lambda X (the
      curl energy, 4 (lambda - 1) X, is the part the hypothesis charges beyond the published model);
  (b) is it a dip: EVERY valid single switch of the chain's move set out of it, its cost, the cheapest and how many
      have it (full enumeration over all pairs of links, not the NEAR = 4 shortcut of analyse_t55); also the
      cheapest among switches touching the object, and analyse_t55.one_move's own class;
  (c) under the face rule of docs/design/eq45_ratio_brief.md (imported from sandbox/eq45_geometrize_check.py): the
      vertex types and the excess angle eps / pi summed over the object, over the object plus its collar, and over
      the whole graph (which Gauss-Bonnet fixes at -2 chi); and the region-based reading of
      sandbox/twist_character_check.report_bands: two-sided or one-sided, with its outcome words;
  (d) survival in the toy's own chain (graphity.cqg.run_chain, Metropolis, no cap) at g = 1.0 ... 3.5, 8 replicas per
      coupling with fixed seeds, cap 20,000 sweeps, three times per replica (see survival()): the FIRST EXIT, read
      every sweep (the first sweep at which the record's detector finds fewer such objects than at the start; for the
      pill, the first of its two caps lost); GONE FOR GOOD, the start of an absence lasting at least 1,000 sweeps, read
      every 10 sweeps after the first exit; and the share of those later readings at which the object was back. Also
      the energy at the end, since a graph can hold energy the detector does not see. *Corrected 23 October, by the
      check:* the first version timed only the first exit and called it "gone"; the objects mostly come back.

Usage: python3 sandbox/column_look.py  (writes sandbox/out/column_look_2026-10-23.txt; the write-up beside it, .md,
is written by hand from it)
"""
import contextlib
import io
import math
import os
import statistics
import sys
import time
from collections import Counter

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
for p in (os.path.join(ROOT, "src"), os.path.join(ROOT, "scripts"), HERE):
    if p not in sys.path:
        sys.path.insert(0, p)

from graphity.cqg import NO_CAP, torus, run_chain, hamiltonian, is_valid, total_squares, surplus, _switch, has_edge  # noqa: E402
from graphity.squares import squares_on_edge                                      # noqa: E402
from graphity.dimension import local_dimension, piece_labels                      # noqa: E402
from graphity.objects import count_rings                                          # noqa: E402
from run_sixloop_widen import seam_shifted                                        # noqa: E402
from analyse_t37 import leftovers                                                 # noqa: E402
import analyse_t55 as t55                                                         # noqa: E402
from read_column_wiring import pattern as column_pattern, groups as column_groups   # noqa: E402
from eq45_geometrize_check import INF, geometrize, two_colour, angle_term          # noqa: E402
from twist_character_check import report_bands, regions                           # noqa: E402
import networkx as nx                                                             # noqa: E402

LAM = 1.25
L = 16                       # paper 1's tube length; N = 64
N = 4 * L
COUPLINGS = (1.0, 1.5, 2.0, 2.5, 3.0, 3.5)
REPLICAS = 8
CAP_SWEEPS = 20000
BLOCK = 10
OUT_DIR = os.path.join(HERE, "out")
DATE = "2026-10-23"


# ------------------------------------------------------------------------------------------------- builders

def idx(x, y, length=L):
    """seam_shifted's label of the point x round (0..3), y along."""
    return (x % 4) * length + (y % length)


def rewire(adj, removed, added):
    nb = [list(map(int, adj[v])) for v in range(adj.shape[0])]
    for p, q in removed:
        nb[p].remove(q)
        nb[q].remove(p)
    for p, q in added:
        nb[p].append(q)
        nb[q].append(p)
    out = np.array(nb, dtype=np.int64)
    assert out.shape == adj.shape, "a point lost or gained a link"
    return out


# The column's recipe, read off the chain's own column (see the module docstring). Coordinates are those of
# seam_shifted(L, 2): x round the tube (a step past x = 3 arrives at (0, y - 2)), y along it; y0 places it.
COLUMN_REMOVED = [((0, -1), (0, 0)), ((0, 1), (0, 2)), ((0, 1), (1, 1)), ((2, 0), (2, 1)), ((3, 1), (3, 2))]
COLUMN_ADDED = [((0, -1), (1, 1)), ((0, 0), (2, 1)), ((0, 1), (2, 0)), ((0, 1), (3, 1)), ((0, 2), (3, 2))]
# (The first version also listed the three switches as a path; its first switch named links that are absent, so it
# was removed. The check found a three-switch path from flat: 0 -> 20 -> 20 -> 14 units, so the column's barrier back
# to flat is its 6-unit exit, then a free move, then a fall of 20.)


def column(length=L, y0=8):
    """The six-around torus with one 14-unit column: five links removed and five added (three switches)."""
    adj, side = seam_shifted(length, 2)
    part = np.ones(4 * length, dtype=np.int64)
    part[side] = 0
    rem = [(idx(a[0], a[1] + y0, length), idx(b[0], b[1] + y0, length)) for a, b in COLUMN_REMOVED]
    add = [(idx(a[0], a[1] + y0, length), idx(b[0], b[1] + y0, length)) for a, b in COLUMN_ADDED]
    return rewire(adj, rem, add), part


def double_column(length=L, a=8):
    """The double column as the toy's chain makes it: as one of TWO caps of a cylinder of squares eight around.

    The chain, run on the built 4 x 16 tube (lambda = 1.25, g = 1.5; 60 seeds, snapshots every 5 sweeps), produced
    eight-point pieces at d = 1 with twelve inside links (O107's Q3 wiring) in two seeds, and in both the state held
    two of them at once, with every other point at d = 2 and nothing but their 8 + 8 units in the whole graph
    (S - N = 4, X = 16, H = 16). Read from the wiring: each is an original 4 x 2 segment of the tube (rings a, a + 1)
    whose eight points keep three links among themselves and one out; the eight outside neighbours form an 8-cycle
    (the two old rings beside the segment, opened at their seams and joined end to end by two "bypass" links); the
    next layer is an 8-cycle too, and so on, so the sheet between the two caps is a cylinder eight around.

    Why a clean collar forces a cylinder (ours, unverified; *corrected 23 October: the conclusion first drawn here,
    that such a cap cannot sit alone, is withdrawn*, see the module docstring): with the cap's collar clean (every
    collar link on exactly two squares, which O107's "nothing more within one step" requires), each collar link's
    second square forces the next layer to be another 8-cycle of points on two squares, and so on layer by layer;
    the layers can end only at another cap (another Q3 on three-square links) or at a layer that is not clean, which
    is where the chain's lone clean-collared Q3 ends (beside a knot of two kinds, H = 38).

    This builder is the regular form of that pair: the 4 x `length` tube, anchors (caps) at rings (a, a + 1) and at
    the two rings opposite; every other ring y is paired with 2a + 1 - y and the two seam links (3, y)-(0, y) and
    (3, y')-(0, y') are switched to (3, y)-(3, y') and (0, y)-(0, y'): six switches at length 16. It is valid, has
    the exact signature above, and its caps' neighbourhoods match the chain's caps (induced subgraphs isomorphic out
    to the radius reported in the output); the chain's cylinder between the caps is glued with a twist, so the whole
    graphs are not isomorphic. The cap at rings (a, a + 1) is the object observed."""
    adj, part = torus(4, length, NO_CAP)            # index = x * length + y, x round (0..3), y along
    nb = [list(map(int, adj[v])) for v in range(4 * length)]
    pairs = []
    for y in range(length):
        yp = (2 * a + 1 - y) % length
        if y in (a, a + 1) or yp in (a, a + 1) or y >= yp or (yp - y) % length == 1 or (y - yp) % length == 1:
            continue
        pairs.append((y, yp))
    rem = [(idx(3, y, length), idx(0, y, length)) for pair in pairs for y in pair]
    add = [(idx(3, y, length), idx(3, yp, length)) for y, yp in pairs] + \
          [(idx(0, y, length), idx(0, yp, length)) for y, yp in pairs]
    return rewire(adj, rem, add), part


# ------------------------------------------------------------------------------------------------- readers

def xy(i, length=L):
    return (i // length, i % length)


def pieces(adj):
    d = local_dimension(adj)
    lab = piece_labels(adj, d != 2)
    out = []
    for k in range(int(lab.max()) + 1):
        pts = tuple(int(v) for v in np.flatnonzero(lab == k))
        out.append((pts, tuple(int(d[v]) for v in pts)))
    return out, d


def inside_links(adj, pts):
    s = set(pts)
    return sum(1 for v in pts for w in adj[v] if int(w) in s) // 2


def ball(adj, pts, r):
    seen = set(int(v) for v in pts)
    edge = set(seen)
    for _ in range(r):
        edge = {int(w) for v in edge for w in adj[v]} - seen
        seen |= edge
    return seen


def energy_split(adj, lam):
    s, x = int(total_squares(adj)), int(surplus(adj))
    return dict(S_minus_N=s - adj.shape[0], X=x, missing=16.0 * (adj.shape[0] - s), surplus=4.0 * lam * x,
                curl=4.0 * (lam - 1.0) * x, H=hamiltonian(adj, lam))


def all_switches(adj, part):
    """Every distinct switch of the chain's move set: links (u1, v1), (u2, v2) with u on side 0, to (u1, v2), (u2, v1)."""
    n = adj.shape[0]
    edges = [(u, int(v)) for u in range(n) if part[u] == 0 for v in adj[u]]
    for i in range(len(edges)):
        u1, v1 = edges[i]
        for j in range(i + 1, len(edges)):
            u2, v2 = edges[j]
            if u1 == u2 or v1 == v2 or has_edge(adj, u1, v2) or has_edge(adj, u2, v1):
                continue
            yield u1, v1, u2, v2


def switch_census(adj, part, obj, lam):
    """Costs of every valid single switch out of adj at lam; those touching the object (a point of it among the
    four) counted separately."""
    h0 = hamiltonian(adj, lam)
    costs, touching = Counter(), Counter()
    obj = set(obj)
    tried = valid = 0
    for sw in all_switches(adj, part):
        tried += 1
        t = adj.copy()
        _switch(t, *sw)
        if not is_valid(t, NO_CAP):
            continue
        valid += 1
        dh = round(float(hamiltonian(t, lam) - h0), 6)
        costs[dh] += 1
        if obj & set(sw):
            touching[dh] += 1
    return dict(tried=tried, valid=valid, costs=costs, touching=touching)


def object_count(adj, kind):
    """How many such objects the record's detector finds anywhere in the graph."""
    if kind == "column":
        return leftovers(adj)[0]
    pcs, d = pieces(adj)
    return sum(1 for p, ds in pcs if len(p) == 8 and all(x == 1 for x in ds) and inside_links(adj, p) == 12)


START_COUNT = {"column": 1, "double column": 2}      # the pill holds two caps; losing either counts as gone


def is_object_present(adj, kind):
    return object_count(adj, kind) >= START_COUNT[kind]


def describe_state(adj, lam):
    pcs, d = pieces(adj)
    e = energy_split(adj, lam)
    flat_share = float((d == 2).mean())
    sizes = Counter((len(p), tuple(sorted(set(ds)))) for p, ds in pcs)
    return dict(H=e["H"], S_minus_N=e["S_minus_N"], X=e["X"], flat_share=flat_share,
                pieces=sorted(sizes.items(), key=lambda kv: -kv[0][0]), columns=leftovers(adj)[0])


WINDOW = 1000                # an absence this long counts as gone for good


def survival(adj0, part, kind, lam, g, seeds):
    """Per replica: the first exit, read every sweep (the first sweep at which the detector finds fewer such objects
    than at the start; for the pill, the first of its two caps lost); gone for good, the sweep at which an absence
    began that lasted at least WINDOW sweeps (read every BLOCK sweeps after the first exit; None if the object was
    present at the cap); the share of those later readings at which the object was back; and H at the end. An
    object can leave and come back: the first exit is the first trip over its cheapest wall, not its death. The
    first replica's state at the end is described from its wiring."""
    side = np.flatnonzero(part == 0).astype(np.int64)
    rows, first_state = [], None
    for k, seed in enumerate(seeds):
        adj = adj0.copy()
        t, first, first_exit = 0, True, None
        while t < CAP_SWEEPS:
            run_chain(adj, side, 1.0 / g, 0, 1, seed if first else -1, lam, NO_CAP, False, None)
            first = False
            t += 1
            if not is_object_present(adj, kind):
                first_exit = t
                break
        for_good, back, reads = None, 0, 0
        if first_exit is not None:
            absent_since = first_exit
            while True:
                run_chain(adj, side, 1.0 / g, 0, BLOCK, -1, lam, NO_CAP, False, None)
                t += BLOCK
                reads += 1
                if is_object_present(adj, kind):
                    back += 1
                    absent_since = None
                    if t >= CAP_SWEEPS:
                        break
                else:
                    if absent_since is None:
                        absent_since = t
                    if t - absent_since >= WINDOW:
                        for_good = absent_since
                        break
        rows.append(dict(first_exit=first_exit, for_good=for_good, share_back=(back / reads) if reads else None,
                         H_end=float(hamiltonian(adj, lam))))
        if k == 0:
            first_state = describe_state(adj, lam)
    return rows, first_state


def median_or_more(xs, cap):
    """The median, counting a missing time as later than any; '> cap' when that median is missing."""
    padded = sorted(x if x is not None else math.inf for x in xs)
    m = statistics.median(padded)
    return "> %d" % cap if math.isinf(m) else "%g" % m


# ------------------------------------------------------------------------------------------------- the face rule

def face_rule_reading(adj, obj, lam):
    geo = geometrize(adj)
    n = adj.shape[0]
    obj = sorted(obj)
    collar = sorted(ball(adj, obj, 1) - set(obj))
    two = sorted(ball(adj, obj, 2))
    def types(pts):
        return dict(Counter(tuple("inf" if k >= INF else k for k in geo["types"][p]) for p in pts))
    out = dict(
        types_object=types(obj), types_collar=types(collar),
        eps_object=float(geo["eps"][obj].sum() / math.pi), eps_one_step=float(geo["eps"][obj + collar].sum() / math.pi),
        eps_two_steps=float(geo["eps"][two].sum() / math.pi), eps_total=float(geo["eps"].sum() / math.pi),
        K_object=float(geo["K"][obj].mean()), K_collar=float(geo["K"][collar].mean()) if collar else float("nan"),
        ties=int(geo["ties"].sum()),
        chi_from_eps=-float(geo["eps"].sum() / math.pi) / 2.0)
    curled, opened, flawed, lip = regions(adj)
    out["regions"] = dict(curled=len(curled), opened=len(opened), flawed=len(flawed), lip=len(lip),
                          curled_points=sorted(curled), flawed_points=sorted(flawed))
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        report_bands(adj, "the built graph")
    out["bands_text"] = buf.getvalue()
    return out


# ------------------------------------------------------------------------------------------------- main

def main():
    t0 = time.time()
    os.makedirs(OUT_DIR, exist_ok=True)
    lines = []
    def say(s=""):
        print(s, flush=True)
        lines.append(s)

    say("# The column and the double column, observed on built graphs (sandbox look, %s)" % DATE)
    say()
    say("Rule 16: a look; it can kill, not crown. Nothing read from results/. Kinds of statement: exact (a count or")
    say("arithmetic on a built graph), sandbox (the chains run here), hers (her expectation), ours (our reading).")
    say()
    objects = [("column", column(L)), ("double column", double_column(L))]

    results = {}
    for kind, (adj, part) in objects:
        host = ("the six-around torus seam_shifted(%d, 2) with three switches" % L if kind == "column" else
                "the pill: the 4 x %d tube with six seam switches, a cylinder eight around between two caps" % L)
        say("## %s (built on %s; N = %d)" % (kind, host, N))
        say()
        ok = bool(is_valid(adj, NO_CAP))
        bip = two_colour(adj) is not None
        reg = all(len(set(int(w) for w in adj[v])) == 4 and (adj[v] >= 0).all() for v in range(N))
        pcs, d = pieces(adj)
        say("Validity (exact): is_valid(no cap) = %s; bipartite = %s; 4-regular simple = %s" % (ok, bip, reg))
        say("Pieces of points not at d = 2 (the record's detector, piece_labels on d != 2): %s"
            % [(len(p), ds) for p, ds in pcs])
        if kind == "double column":
            obj = next(p for p, _ in pcs if idx(0, 8) in p)      # the cap at rings (8, 9); the other cap is its twin
            say("The pill holds two caps; the one at rings (8, 9) is observed below. Its twin at rings (0, 1) is the same by symmetry.")
        else:
            obj = pcs[0][0] if pcs else ()
        say("Object's points (labels and (x, y)): %s" % [(v, xy(v)) for v in obj])
        say("analyse_t37.leftovers (columns, other) = %s; objects.count_rings (squares with all four links on three) = %d"
            % (leftovers(adj), int(count_rings(adj))))
        if kind == "column":
            pat = column_pattern(adj, obj)
            say("read_column_wiring.pattern (inside links' squares; out links' squares; three-sides opposite) = %s"
                % (pat,))
            say("read_column_wiring.groups (outside neighbours' groups with the ring removed; 1 = does not cut the tube) = %d"
                % column_groups(adj, obj))
            say("  O126's 14-unit kind reads ((2, 2, 3, 3), (2, 2, 2, 2, 3, 3, 3, 3), True) and groups 1.")
        else:
            say("inside links among the eight points = %d (O107: twelve); each point's inside links: %s"
                % (inside_links(adj, obj), sorted(Counter(sum(1 for w in adj[v] if int(w) in set(obj)) for v in obj).items())))
            sub = nx.Graph([(v, int(w)) for v in obj for w in adj[v] if int(w) in set(obj)])
            say("  induced subgraph isomorphic to the 3-cube Q3: %s" % nx.is_isomorphic(sub, nx.hypercube_graph(3)))
        cen = t55.census(adj, obj, LAM, d)
        e1 = sum(t55.point_energy(adj, v, LAM) for v in ball(adj, obj, 1))
        e2 = sum(t55.point_energy(adj, v, LAM) for v in ball(adj, obj, 2))
        say("analyse_t55.census at lambda = 1.25: size %d, d %s, squares on links %s, energy at its points %.1f; within one step %.1f; within two %.1f"
            % (cen["size"], cen["ds"], cen["squares"], cen["energy"], e1, e2))
        say("  (O107: the column 4 at its points and 14 within one step; the double column 8 at its points and nothing more within one step)")
        far_max, far_n = t55.far_links(adj, obj)
        say("analyse_t55.far_links: largest way round %d, FAR links %d (O107: none)" % (far_max, far_n))
        move, dh, sw = t55.one_move(adj, part, obj, LAM, d)
        say("analyse_t55.one_move (switches within NEAR = 4): %s, cheapest %.2f via %s" % (move, dh, sw))
        for v in obj:
            say("  point %s (x, y) = %s: links %s" % (v, xy(v), [(xy(int(w)), int(squares_on_edge(adj, v, int(w)))) for w in adj[v]]))
        collar = sorted(ball(adj, obj, 1) - set(obj))
        for v in collar:
            say("  collar %s (x, y) = %s, d = %d, e = %.1f: links %s"
                % (v, xy(v), int(d[v]), t55.point_energy(adj, v, LAM), [(xy(int(w)), int(squares_on_edge(adj, v, int(w)))) for w in adj[v]]))
        say()
        # (a) energies
        say("### (a) energy, split (exact)")
        for lam in (1.0, 1.25):
            e = energy_split(adj, lam)
            say("  lambda = %.2f: S - N = %d, X = %d; missing squares 16 (N - S) = %+.1f; surplus squares 4 lambda X = %+.1f; "
                "H = %.1f; the curl energy 4 (lambda - 1) X = %.1f" % (lam, e["S_minus_N"], e["X"], e["missing"], e["surplus"], e["H"], e["curl"]))
        say()
        # (b) dip
        say("### (b) every valid single switch out of it (exact, full enumeration)")
        for lam in (1.25, 1.0):
            c = switch_census(adj, part, obj, lam)
            cheapest = min(c["costs"])
            say("  lambda = %.2f: %d switches tried, %d valid; cheapest cost %.2f, %d switch(es) have it; costs <= 20: %s"
                % (lam, c["tried"], c["valid"], cheapest, c["costs"][cheapest],
                   sorted((k, v) for k, v in c["costs"].items() if k <= 20)))
            if c["touching"]:
                ch_t = min(c["touching"])
                say("    switches touching the object: %d valid; cheapest %.2f (%d of them); their costs <= 20: %s"
                    % (sum(c["touching"].values()), ch_t, c["touching"][ch_t],
                       sorted((k, v) for k, v in c["touching"].items() if k <= 20)))
            say("    a dip (every move out costs): %s" % (cheapest > 1e-9))
        say()
        # (c) face rule
        say("### (c) the face rule (eq45 brief; sandbox/eq45_geometrize_check.py; twist_character_check.report_bands)")
        fr = face_rule_reading(adj, obj, LAM)
        say("  vertex types at the object's points: %s; at the collar: %s" % (fr["types_object"], fr["types_collar"]))
        say("  mean K (1/l^2) at the object %.4f, at the collar %.4f; ties in the rotation choice %d"
            % (fr["K_object"], fr["K_collar"], fr["ties"]))
        say("  excess angle, sum eps / pi: at the object %.4f; object + collar %.4f; within two steps %.4f; whole graph %.4f (-2 chi => chi = %.2f)"
            % (fr["eps_object"], fr["eps_one_step"], fr["eps_two_steps"], fr["eps_total"], fr["chi_from_eps"]))
        say("  regions (twist_character_check.regions): curled %d, opened %d, flawed %d, lip links %d; curled points %s; flawed points %s"
            % (fr["regions"]["curled"], fr["regions"]["opened"], fr["regions"]["flawed"], fr["regions"]["lip"],
               [xy(v) for v in fr["regions"]["curled_points"]], [xy(v) for v in fr["regions"]["flawed_points"]]))
        say("  report_bands:")
        for ln in fr["bands_text"].rstrip().splitlines():
            say("  " + ln)
        say()
        results[kind] = dict(adj=adj, part=part, obj=obj)

    # (d) survival
    say("## (d) survival in the toy's own chain (sandbox; lambda = 1.25, Metropolis, no cap, L = %d, cap %d sweeps)"
        % (L, CAP_SWEEPS))
    say()
    say("First exit = the first sweep (read every sweep) at which the record's detector finds fewer such objects than at")
    say("the start (column: analyse_t37.leftovers()[0] == 0; double column: fewer than the pill's two pieces of eight points")
    say("all at d = 1 with twelve inside links, so the first of its two caps lost). Gone for good = the start of an absence")
    say("lasting at least %d sweeps (read every %d sweeps after the first exit). Back = the share of those later readings at" % (WINDOW, BLOCK))
    say("which the object was there again. H at the end shows energy the detector may not see.")
    say('Her expectation, recorded first: "Typically anything only lasts a few sweeps higher than a few g."')
    say()
    say("| object | g | first exit, median | first exit, per replica | gone for good, median | gone for good, per replica | back, median share | H at the end, per replica | first replica at the end |")
    say("|---|---|---|---|---|---|---|---|---|")
    for kind, r in results.items():
        for g in COUPLINGS:
            seeds = [20261023 + 100 * int(round(10 * g)) + k for k in range(REPLICAS)]
            rows, st = survival(r["adj"], r["part"], kind, LAM, g, seeds)
            fe = [x["first_exit"] for x in rows]
            fg = [x["for_good"] for x in rows]
            sb = [x["share_back"] for x in rows if x["share_back"] is not None]
            say("| %s | %.1f | %s | %s | %s | %s | %s | %s | H = %.1f, S - N = %d, X = %d, share at d = 2 %.2f, pieces off d = 2 (size, d values) %s |"
                % (kind, g, median_or_more(fe, CAP_SWEEPS), [x if x is not None else ">%d" % CAP_SWEEPS for x in fe],
                   median_or_more(fg, CAP_SWEEPS), [x if x is not None else ">%d" % CAP_SWEEPS for x in fg],
                   ("%.2f" % statistics.median(sb)) if sb else "-", ["%g" % x["H_end"] for x in rows],
                   st["H"], st["S_minus_N"], st["X"], st["flat_share"], st["pieces"]))
            print("   ... g = %.1f done for %s (%.0fs)" % (g, kind, time.time() - t0), flush=True)
    say()
    flat0, side0 = seam_shifted(L, 2)
    part0 = np.ones(N, dtype=np.int64)
    part0[side0] = 0
    cc = switch_census(flat0, part0, (), LAM)
    cheapest0 = min(cc["costs"])
    say("Control, the column's host alone: the narrow six-around torus seam_shifted(%d, 2), whose cheapest single switch costs" % L)
    say("%g (%d switches; exact, full enumeration; a wide flat sheet's costs 32), in the same chain, 4 replicas per g: the first" % (cheapest0, cc["costs"][cheapest0]))
    say("sweep at which fewer than 90 %%, and fewer than 50 %%, of its points are still at d = 2 (cap %d, read every %d sweeps)." % (CAP_SWEEPS, BLOCK))
    say("The pill's host (a cylinder eight around between two caps) has no control here.")
    say()
    say("| g | first sweep below 90 % flat, per replica | first sweep below 50 % flat, per replica | share at d = 2 at the end |")
    say("|---|---|---|---|")
    for g in COUPLINGS:
        below90, below50, ends = [], [], []
        for k in range(4):
            adj = flat0.copy()
            first, b90, b50 = True, None, None
            for b in range(CAP_SWEEPS // BLOCK):
                run_chain(adj, side0, 1.0 / g, 0, BLOCK, 20261024 + 100 * int(round(10 * g)) + k if first else -1, LAM, NO_CAP, False, None)
                first = False
                share = float((local_dimension(adj) == 2).mean())
                if b90 is None and share < 0.9:
                    b90 = (b + 1) * BLOCK
                if b50 is None and share < 0.5:
                    b50 = (b + 1) * BLOCK
                    break
            below90.append(b90)
            below50.append(b50)
            ends.append(float((local_dimension(adj) == 2).mean()))
        say("| %.1f | %s | %s | %s |" % (g, [x if x is not None else ">%d" % CAP_SWEEPS for x in below90],
                                        [x if x is not None else ">%d" % CAP_SWEEPS for x in below50],
                                        ["%.2f" % e for e in ends]))
        print("   ... control g = %.1f done (%.0fs)" % (g, time.time() - t0), flush=True)
    say()
    say("Run time %.0f s." % (time.time() - t0))
    with open(os.path.join(OUT_DIR, "column_look_%s.txt" % DATE), "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    return lines


if __name__ == "__main__":
    main()

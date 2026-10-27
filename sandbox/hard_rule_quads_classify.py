"""Classify the count-keeping four-switch sequences found by `hard_rule_quads_look.py` (a look; rule 16).

The counter FOUND in that script means "keeps the square count and leaves the start edge set". That admits renamings,
as the four-link census found (448 of its 480 forms were renamings). This reader replays each found sequence on the
same flat torus and says what its end state is, in this order of tests:

  BACK            the start edge set (should not occur among FOUND rows);
  TRANSPOSITION   the start with two points' names exchanged (one transposition): every point's neighbor set equals the
                  start's with the two names swapped. Exact, no isomorphism search.
  RENAMING        isomorphic to the start by networkx `is_isomorphic` but not by one transposition;
  REAL            none of the above: a count-keeping move that changes the arrangement. Its curl and anticurl change and
                  the smallest number of squares on any link are printed.

Words declared before running: the four-switch count's restricted word is ZERO REAL MOVES if every found form is BACK,
TRANSPOSITION or RENAMING, and FOUND REAL otherwise, with the real sequences listed. The words are about the restricted
count (every switch's points within one link of the first switch's four), not the exhaustive one.

Inputs: `--seq <slice_*.txt ...>` reads the SEQ lines printed by the look (six per kind per slice, representatives);
`--rows <rows_*.npy ...>` reads the saved rows (22 columns: 16 switch ends, 4 dS, curl, anticurl), which hold every
FOUND form when the look ran with `--rows`. `--dims 6,6,8` names the torus (default 6 x 6 x 8).

Usage:
    PYTHONPATH="src;scripts" python sandbox/hard_rule_quads_classify.py --seq sandbox/out/hard_rule_quads/restricted/slice_*.txt
    PYTHONPATH="src;scripts" python sandbox/hard_rule_quads_classify.py --rows sandbox/out/hard_rule_quads/restricted_rows/rows_*.npy

Starting state: the flat torus, which obeys the owner's hard rule (S = 3N, curl 0, anticurl 0). A look: it can kill
"a four-switch move exists within the restricted word" and cannot crown anything.
"""
import glob
import re
import sys
from collections import Counter
from pathlib import Path

import networkx as nx
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "sandbox"))
import hard_rule_quads_look as Q  # noqa: E402

SEQ_RE = re.compile(r"SEQ switches \((\d+),(\d+),(\d+),(\d+)\) \((\d+),(\d+),(\d+),(\d+)\) \((\d+),(\d+),(\d+),(\d+)\) "
                    r"\((\d+),(\d+),(\d+),(\d+)\)")


def read_seqs(files):
    out = []
    for f in files:
        for line in open(f, encoding="utf-8", errors="replace"):
            m = SEQ_RE.match(line.strip())
            if m:
                out.append(tuple(int(x) for x in m.groups()))
    return out


def read_rows(files):
    out = []
    for f in files:
        rows = np.load(f)
        for r in rows:
            out.append(tuple(int(x) for x in r[:16]))
    return out


def classify(dims, seqs):
    adj0, part = Q.torus(dims)
    adj0 = np.asarray(adj0, dtype=np.int64)
    n, deg = adj0.shape
    flat = deg - 2
    s0 = int(Q.total_squares(adj0))
    c0, a0 = Q.curl_anti(adj0, flat)
    print(f"flat torus {dims}: N = {n}, deg = {deg}, S = {s0}, curl {c0}, anticurl {a0}; obeys the hard rule: "
          f"{s0 == flat * deg * n // 8 and c0 == 0 and a0 == 0}")
    nbr0 = [frozenset(int(v) for v in adj0[u]) for u in range(n)]
    g0 = nx.Graph()
    for u in range(n):
        for v in adj0[u]:
            g0.add_edge(u, int(v))
    tally = Counter()
    pairs = Counter()
    reals = []
    end_keys = {}
    for s in seqs:
        adj = adj0.copy()
        ds = []
        for k in range(4):
            u1, v1, u2, v2 = s[4 * k:4 * k + 4]
            ok, d = Q.try_switch(adj, u1, v1, u2, v2)
            if not ok:
                tally["ILLEGAL (replay failed)"] += 1
                break
            ds.append(int(d))
        else:
            if sum(ds) != 0 or int(Q.total_squares(adj)) != s0:
                tally["NOT COUNT-KEEPING (replay)"] += 1
                continue
            nbr = [frozenset(int(v) for v in adj[u]) for u in range(n)]
            changed = [u for u in range(n) if nbr[u] != nbr0[u]]
            if not changed:
                tally["BACK"] += 1
                continue
            kind = None
            for i, p in enumerate(changed):
                for q in changed[i + 1:]:
                    sw = {p: q, q: p}
                    if all(nbr[u] == frozenset(sw.get(int(v), int(v)) for v in nbr0[sw.get(u, u)]) for u in range(n)):
                        kind = "TRANSPOSITION"
                        pairs[(p, q)] += 1
                        break
                if kind:
                    break
            if kind is None:
                key = frozenset((u, int(v)) for u in range(n) for v in adj[u] if u < int(v))
                if key in end_keys:
                    kind = end_keys[key]
                else:
                    g = nx.Graph()
                    for u in range(n):
                        for v in adj[u]:
                            g.add_edge(u, int(v))
                    kind = "RENAMING" if nx.is_isomorphic(g0, g) else "REAL"
                    end_keys[key] = kind
                if kind == "REAL":
                    c, a = Q.curl_anti(adj, flat)
                    mins = min(int(Q.squares_on_edge(adj, u, int(v))) for u in range(n) for v in adj[u])
                    reals.append((s, ds, int(c - c0), int(a - a0), mins))
            tally[kind] += 1
    return tally, pairs, reals, dims


def main(argv):
    dims = (6, 6, 8)
    if "--dims" in argv:
        dims = tuple(int(x) for x in argv[argv.index("--dims") + 1].split(","))
    seqs = []
    if "--seq" in argv:
        i = argv.index("--seq")
        files = []
        for a in argv[i + 1:]:
            if a.startswith("--"):
                break
            files += glob.glob(a)
        seqs += read_seqs(sorted(files))
        print(f"SEQ lines read: {len(seqs)} from {len(files)} files")
    if "--rows" in argv:
        i = argv.index("--rows")
        files = []
        for a in argv[i + 1:]:
            if a.startswith("--"):
                break
            files += glob.glob(a)
        rows = read_rows(sorted(files))
        print(f"rows read: {len(rows)} from {len(files)} files")
        seqs += rows
    print(f"sequences to classify: {len(seqs)} ({len(set(seqs))} distinct)")
    tally, pairs, reals, dims = classify(dims, seqs)
    print("tally:", dict(tally))
    strides = [int(np.prod(dims[a + 1:])) for a in range(len(dims))]

    def coords(i):
        return tuple((i // st) % L for st, L in zip(strides, dims))

    if pairs:
        offs = Counter()
        for (p, q), cnt in pairs.items():
            cp, cq = coords(p), coords(q)
            offs[tuple(sorted(min((a - b) % L, (b - a) % L) for a, b, L in zip(cp, cq, dims)))] += cnt
        print(f"transpositions: {len(pairs)} distinct pairs of points; forms by offset (sorted) {dict(offs)}")
    for s, ds, dc, da, mins in reals[:40]:
        print(f"REAL {s} dS {ds} curl {dc:+d} anticurl {da:+d} min squares on a link {mins}")
    real = tally.get("REAL", 0)
    print("WORD (restricted count):", "FOUND REAL" if real else "ZERO REAL MOVES",
          f"({real} real of {sum(tally.values())} forms)")


if __name__ == "__main__":
    main(sys.argv[1:])

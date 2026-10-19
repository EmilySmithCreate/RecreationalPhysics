"""Sandbox look (rule 16): where do T51's knots sit along the sheet? Random (shot noise) or clustered?

    python sandbox/knot_positions.py            # writes sandbox/out/knot_positions_<date>.txt

The owner's idea of 18 October (`sandbox/NOTEBOOK.md`): the scraps as the seeds of structure. One way it can be wrong:
knots of equal energy scattered at random are shot noise. This look reads the positions of the knots in the 600 saved T51
end states (`results/t51_*_adj/*.npz`, 4 x L tubes opened and cooled; T55 read what the knots are, O107) and asks three
things, none of them evidence for anything:

  1. Along the long direction (column x = index // 4, L columns on a ring), are the gaps between knots what uniform
     random positions give?  For a sheet with n knots the fraction of the ring in one gap has P(gap/L <= s) =
     1 - (1 - s)^(n-1) under the null, so each gap gives a p-value; pooled over sheets they should be uniform (gaps in
     one sheet are dependent, so this is a look, not a test). And the nearest-neighbour distance per knot, pooled,
     against a Monte Carlo with the same n per sheet.
  2. Do knots of different kinds sit together (a column next to a knot of two kinds, say)?
  3. Across cooling times the opened sheets are the same (T51: replicas of one seeded set), so do the knots that survive
     a slower cooling sit where knots sat after a faster one?  If their number is set at the opening (O107), yes.

A knot is a connected group of pieces off d = 2 within graph distance 2 of each other (T55's grouping, which joined the
pieces of two into the eight-point knot of two kinds). Its position is the circular mean of its points' columns.
"""
import sys
from collections import Counter, defaultdict
from glob import glob
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from graphity.dimension import local_dimension, piece_labels   # noqa: E402

LY = 4
rng = np.random.default_rng(2026_10_18)


def knots_of(adj):
    """[(points, kind)] for one sheet. kind: COLUMN (4 at d=1), DOUBLE (8 at d=1), TWO-KINDS (8, d in {1,3}), OTHER."""
    d = local_dimension(adj)
    labels = piece_labels(adj, d != 2)
    n_pieces = int(labels.max()) + 1
    pieces = [set(int(v) for v in np.flatnonzero(labels == k)) for k in range(n_pieces)]
    # group pieces within graph distance 2
    owner = list(range(n_pieces))

    def find(a):
        while owner[a] != a:
            owner[a] = owner[owner[a]]
            a = owner[a]
        return a

    where = {}
    for k, pc in enumerate(pieces):
        for v in pc:
            where[v] = k
    for k, pc in enumerate(pieces):
        ball = set(pc)
        for _ in range(2):
            ball |= {int(w) for v in ball for w in adj[v]}
        for v in ball:
            if v in where and where[v] != k:
                a, b = find(k), find(where[v])
                if a != b:
                    owner[a] = b
    groups = defaultdict(set)
    for k, pc in enumerate(pieces):
        groups[find(k)] |= pc
    out = []
    for pts in groups.values():
        ds = sorted(int(d[v]) for v in pts)
        if len(pts) == 4 and ds == [1] * 4:
            kind = "COLUMN"
        elif len(pts) == 8 and ds == [1] * 8:
            kind = "DOUBLE"
        elif len(pts) == 8 and ds == [1] * 4 + [3] * 4:
            kind = "TWO-KINDS"
        else:
            kind = "OTHER(%d)" % len(pts)
        out.append((sorted(pts), kind))
    return out


def column_of(points, L):
    ang = np.array([v // LY for v in points]) * 2 * np.pi / L
    return (np.arctan2(np.sin(ang).mean(), np.cos(ang).mean()) * L / (2 * np.pi)) % L


def ring_gaps(xs, L):
    xs = np.sort(np.asarray(xs))
    return np.diff(np.concatenate([xs, [xs[0] + L]]))


def nn_dist(xs, L):
    xs = np.asarray(xs)
    dd = np.abs(xs[:, None] - xs[None, :])
    dd = np.minimum(dd, L - dd)
    np.fill_diagonal(dd, np.inf)
    return dd.min(axis=1)


def main():
    files = sorted(glob("results/t51_*_adj/*.npz"))
    per_sheet = []
    for f in files:
        z = np.load(f)
        adj = z["adj"]
        L = adj.shape[0] // LY
        ks = knots_of(adj)
        rows = [(column_of(p, L), kind) for p, kind in ks]
        per_sheet.append(dict(file=f, L=L, t_cool=int(z["t_cool"]), replica=int(z["replica"]),
                              run=Path(f).parent.name, knots=rows))
    lines = []
    P = lines.append
    P("Knot positions in the %d saved T51 sheets (sandbox look, %s)" % (len(per_sheet), Path(__file__).name))
    kinds = Counter(k for s in per_sheet for _, k in s["knots"])
    P("kinds: %s" % dict(kinds))
    P("knots per sheet: %s" % dict(sorted(Counter(len(s["knots"]) for s in per_sheet).items())))
    P("(a DOUBLE is one connected piece of eight; a TWO-KINDS is T55's four pieces of two within two steps; OTHER(n) groups are mostly two or more knots sitting within two steps of each other, i.e. already clustered)")

    # 1. gaps and nearest neighbours against uniform random positions
    pvals, nn_obs, nn_null = [], [], []
    near4 = near4_null = 0.0
    for s in per_sheet:
        xs = [x for x, _ in s["knots"]]
        n, L = len(xs), s["L"]
        if n < 2:
            continue
        for g in ring_gaps(xs, L):
            pvals.append(1 - (1 - g / L) ** (n - 1))
        nn = nn_dist(xs, L)
        nn_obs.extend(nn / L * n)                     # in units of the mean spacing L/n
        near4 += int((nn <= 4).sum())
        for _ in range(200):
            nn0 = nn_dist(rng.uniform(0, L, n), L)
            nn_null.extend(nn0 / L * n)
            near4_null += int((nn0 <= 4).sum()) / 200.0
    pvals = np.array(pvals)
    nn_obs, nn_null = np.array(nn_obs), np.array(nn_null)
    P("")
    P("1. gaps along the ring, sheets with >= 2 knots: %d gaps" % len(pvals))
    edges = np.linspace(0, 1, 11)
    hist = np.histogram(pvals, edges)[0]
    P("   p-value histogram (uniform under the null; each bin expects %.1f): %s" % (len(pvals) / 10, hist.tolist()))
    ks_stat = np.max(np.abs(np.sort(pvals) - np.arange(1, len(pvals) + 1) / len(pvals)))
    P("   KS distance from uniform %.3f (1.36/sqrt(n) = %.3f would be the 5 %% line if the gaps were independent)"
      % (ks_stat, 1.36 / np.sqrt(len(pvals))))
    P("   nearest-neighbour distance in units of the mean spacing: observed mean %.3f, median %.3f; null mean %.3f, median %.3f"
      % (nn_obs.mean(), np.median(nn_obs), nn_null.mean(), np.median(nn_null)))
    P("   share of knots with another knot within 4 columns: observed %.3f, null (same n per sheet, 200 draws) %.3f"
      % (near4 / len(nn_obs), near4_null / len(nn_obs)))
    q = [0.05, 0.25, 0.5, 0.75, 0.95]
    P("   quantiles of nn/spacing, observed %s, null %s"
      % (np.round(np.quantile(nn_obs, q), 3).tolist(), np.round(np.quantile(nn_null, q), 3).tolist()))

    # 2. kinds beside each other
    P("")
    P("2. nearest neighbour's kind, for each knot (sheets with >= 2 knots):")
    pair = Counter()
    for s in per_sheet:
        if len(s["knots"]) < 2:
            continue
        xs = np.array([x for x, _ in s["knots"]])
        kinds_s = [k for _, k in s["knots"]]
        L = s["L"]
        dd = np.abs(xs[:, None] - xs[None, :])
        dd = np.minimum(dd, L - dd)
        np.fill_diagonal(dd, np.inf)
        for i, j in enumerate(dd.argmin(axis=1)):
            pair[(kinds_s[i], kinds_s[j])] += 1
    for k, v in sorted(pair.items()):
        P("   %-12s -> %-12s %d" % (k[0], k[1], v))

    # 3. persistence of positions across cooling times, same (run family, L, replica)
    P("")
    P("3. do the knots that survive a slower cooling sit where knots sat after a faster one?  (same L and replica)")
    by_key = defaultdict(dict)
    for s in per_sheet:
        fam = s["run"].split("_")[1]                   # l128 / l256 / l512
        by_key[(fam, s["replica"])][s["t_cool"]] = s
    matched = total = 0
    rand_matched = 0
    detail = Counter()
    for key, d_ in by_key.items():
        ts = sorted(d_)
        for a, b in zip(ts[:-1], ts[1:]):
            fast, slow = d_[a], d_[b]
            xf = np.array([x for x, _ in fast["knots"]])
            L = slow["L"]
            for x, kind in slow["knots"]:
                total += 1
                if len(xf) and np.min(np.minimum(np.abs(xf - x), L - np.abs(xf - x))) <= 2:
                    matched += 1
                    detail[kind] += 1
                xr = rng.uniform(0, L, len(xf))
                if len(xf) and np.min(np.minimum(np.abs(xr - x), L - np.abs(xr - x))) <= 2:
                    rand_matched += 1
    P("   knots after the slower cooling that lie within 2 columns of a knot after the next faster cooling: %d of %d (%.2f); random positions would give %.2f"
      % (matched, total, matched / max(total, 1), rand_matched / max(total, 1)))
    P("   matched, by kind: %s" % dict(detail))
    P("   (the T51 runs' replica indices across cooling times are taken to name the same opened sheet, as the config says; if they do not, item 3 reads as random)")

    out = Path("sandbox/out"); out.mkdir(exist_ok=True)
    path = out / "knot_positions_2026-10-18.txt"
    path.write_text("\n".join(lines) + "\n")
    print("\n".join(lines))
    print("wrote", path)


if __name__ == "__main__":
    main()

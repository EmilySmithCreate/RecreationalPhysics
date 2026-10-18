"""T71 (draft): read the slab-under-the-layer-form runs by the rules of PREREGISTRATION.md section T71. Usage:

    python scripts/analyse_t71.py [results/t71_*.csv ...]

Per replica: the sweep of the first split, of the first paid clean switch move and of the first contraction; whether
a clean move came before any split (SPENT FIRST); the release at the first split (the fall in F between the row
before it and the row at it; exact only when rows are logged every sweep) against a N_slab; the number of refolds
(contractions after the first split); the open share (the fraction of the logged sweeps after the first split spent
at width >= 6); the end width and the end energy above flat. Words per replica: OPENS AND STAYS (a split and open
share >= 0.9), OSCILLATES (a split, at least one refold, open share < 0.9), NEVER SPLITS. Per cell (lam, L, rate,
gate, leak, move_set, feed_stops_at_split): the majority word, the count of each word, the median first split with
its range, the median release against a N_slab, the median end energy above flat, and how many replicas were SPENT
FIRST. Nothing here scores the held-out size; that is done against the dated amendment once it exists.
"""
import csv
import sys
from collections import Counter, defaultdict
from pathlib import Path

import numpy as np

OPEN_SHARE = 0.9


def width_of(dims):
    return int(str(dims).split("x")[0])


def read_replica(rows):
    """rows: the logged rows of one replica, as dicts with the runner's columns, in sweep order."""
    rows = sorted(rows, key=lambda r: int(r["sweep"]))
    a_n = 4.0 * (float(rows[0]["lam"]) - 1.0) * int(rows[0]["N_slab"])
    first_split = rows[0]["first_split"]
    first_split = int(first_split) if str(first_split) not in ("", "None") else None
    first_clean = rows[0]["first_clean"]
    first_clean = int(first_clean) if str(first_clean) not in ("", "None") else None
    out = dict(first_split=first_split, first_clean=first_clean,
               spent_first=bool(first_clean is not None and (first_split is None or first_clean < first_split)),
               end_width=width_of(rows[-1]["dims"]), end_F=float(rows[-1]["F"]), a_n=a_n, release=None,
               refolds=None, open_share=None)
    if first_split is None:
        out["word"] = "NEVER SPLITS"
        return out
    by_sweep = {int(r["sweep"]): r for r in rows}
    if first_split in by_sweep and (first_split - 1) in by_sweep:
        out["release"] = float(by_sweep[first_split - 1]["F"]) - float(by_sweep[first_split]["F"])
    elif first_split in by_sweep and first_split == 1:
        out["release"] = a_n - float(by_sweep[1]["F"])
    after = [r for r in rows if int(r["sweep"]) >= first_split]
    n_contract_at = int(by_sweep[first_split]["n_contract"]) if first_split in by_sweep else 0
    out["refolds"] = int(rows[-1]["n_contract"]) - n_contract_at
    out["open_share"] = float(np.mean([width_of(r["dims"]) >= 6 for r in after])) if after else 0.0
    # the share decides the word; the refolds are reported beside it (a refold undone again still counts as open)
    out["word"] = "OPENS AND STAYS" if out["open_share"] >= OPEN_SHARE else "OSCILLATES"
    return out


def read_cells(rows):
    """rows: every row of one or more result files. Returns {cell key: dict} with the per-cell reading."""
    groups = defaultdict(lambda: defaultdict(list))
    for r in rows:
        key = (float(r["lam"]), int(r["L"]), float(r["rate"]), float(r["gate"]), float(r["leak"]), r["move_set"],
               int(r["feed_stops_at_split"]))
        groups[key][int(r["replica"])].append(r)
    cells = {}
    for key, reps in sorted(groups.items()):
        reads = [read_replica(rs) for _, rs in sorted(reps.items())]
        words = Counter(x["word"] for x in reads)
        splits = [x["first_split"] for x in reads if x["first_split"] is not None]
        releases = [x["release"] for x in reads if x["release"] is not None]
        cells[key] = dict(
            n=len(reads), words=dict(words), majority=words.most_common(1)[0][0],
            median_first_split=float(np.median(splits)) if splits else None,
            range_first_split=(min(splits), max(splits)) if splits else None,
            median_release=float(np.median(releases)) if releases else None, a_n=reads[0]["a_n"],
            median_end_F=float(np.median([x["end_F"] for x in reads])),
            spent_first=sum(x["spent_first"] for x in reads), replicas=reads)
    return cells


def main(paths):
    rows = []
    for p in paths:
        rows.extend(csv.DictReader(open(p, newline="")))
    cells = read_cells(rows)
    for key, c in cells.items():
        lam, L, rate, gate, leak, move_set, stops = key
        print("lam=%.2f L=%2d r=%-7g gate=%-7.1f leak=%-7g %-8s feed stops=%d | %-15s %s | first split median %s range %s | release median %s vs a N_slab %.1f | end F median %.1f | spent first %d/%d"
              % (lam, L, rate, gate, leak, move_set, stops, c["majority"], c["words"], c["median_first_split"],
                 c["range_first_split"], c["median_release"], c["a_n"], c["median_end_F"], c["spent_first"], c["n"]))
    return cells


if __name__ == "__main__":
    paths = sys.argv[1:] or sorted(str(p) for p in Path("results").glob("t71_*.csv"))
    main(paths)

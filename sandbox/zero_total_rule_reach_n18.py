"""Exact check (sandbox; exploratory), 25 October 2026: under the owner's hard zero-total rule, can the toy's moves
reach every allowed arrangement at 18 points?

The hard rule (VISION Update 105; owner confirmed 25 October) keeps curl minus uncurl at zero, which with four links is
S = N. At N = 18 the complete listing (T4, ASSUMPTIONS Q9) has 26 classes up to renaming, 9 of them with S = 18. A chain
under the hard rule may only make switches that leave S unchanged, so it walks on the 9 classes using only the class
links between two of them. This lists the classes, the links between them, and the pieces the 9 fall into.
"""
from collections import defaultdict

from graphity.small_graphs import count_labelled_states, explore
from graphity.cqg import total_squares, surplus

n = 9  # vertices a side; N = 18
_, start = count_labelled_states(n)
classes, joined = explore(start)
S = {k: int(total_squares(adj)) for k, (adj, _) in enumerate(classes.reps)}
X = {k: int(surplus(adj)) for k, (adj, _) in enumerate(classes.reps)}
keep = sorted(k for k in S if S[k] == 2 * n)
print(f"classes: {len(S)}; keeping the rule (S = {2 * n}): {len(keep)}")
for k in keep:
    inside = sorted(j for j in joined[k] if j in keep)
    print(f"  class {k:2d}  surplus X = {X[k]:2d}  links to rule-keeping classes: {inside}  to others: {len(joined[k]) - len(inside)}")

# pieces of the rule-keeping classes under rule-keeping links only
seen, pieces = set(), []
for k in keep:
    if k in seen:
        continue
    stack, piece = [k], []
    seen.add(k)
    while stack:
        a = stack.pop()
        piece.append(a)
        for b in joined[a]:
            if b in keep and b not in seen:
                seen.add(b)
                stack.append(b)
    pieces.append(sorted(piece))
print(f"pieces under the hard rule: {len(pieces)}")
for p in pieces:
    print("  ", p, " surplus:", [X[k] for k in p])

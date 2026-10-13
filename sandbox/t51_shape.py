"""A look, not a result: is T51's recorded fall one exponential plus a floor?

Uses only numbers already written in ASSUMPTIONS O104 (no result file is opened).
Frozen share (energy left per point over the release), L = 256, against cooling time in fair sweeps.
"""
import math

T = [0, 1_000, 3_000, 10_000, 30_000, 100_000, 300_000]
SHARE = [0.043, 0.044, 0.042, 0.040, 0.034, 0.021, 0.013]

# column ratios recorded in O104: (t_short, t_long, ratio, standard error)
RATIOS = [(1_000, 10_000, 0.91, 0.03), (10_000, 30_000, 0.78, 0.05),
          (10_000, 100_000, 0.347, 0.040), (30_000, 300_000, 0.079, 0.035)]

print("Columns: characteristic time implied by each recorded ratio, if survival = exp(-t/tau)")
for t0, t1, r, se in RATIOS:
    tau = (t1 - t0) / math.log(1 / r)
    lo = (t1 - t0) / math.log(1 / max(r - se, 1e-9))
    hi = (t1 - t0) / math.log(1 / min(r + se, 0.999))
    print(f"  C({t1:>7,})/C({t0:>6,}) = {r:5.3f} +- {se:.3f}  ->  tau = {tau:9,.0f}   (range {lo:9,.0f} to {hi:9,.0f})")

print()
print("Frozen share: least squares of  a + b * exp(-t/tau)  over the seven cells")
best = None
for tau in range(40_000, 200_001, 1_000):
    e = [math.exp(-t / tau) for t in T]
    n = len(T)
    se_, sy = sum(e), sum(SHARE)
    see = sum(x * x for x in e)
    sey = sum(x * y for x, y in zip(e, SHARE))
    b = (n * sey - se_ * sy) / (n * see - se_ * se_)
    a = (sy - b * se_) / n
    sse = sum((a + b * x - y) ** 2 for x, y in zip(e, SHARE))
    if best is None or sse < best[0]:
        best = (sse, tau, a, b)
sse, tau, a, b = best
print(f"  best tau = {tau:,} fair sweeps, floor a = {a:.4f}, dying part b = {b:.4f}, rms = {math.sqrt(sse / len(T)):.4f}")
for t, y in zip(T, SHARE):
    print(f"  t = {t:>7,}: recorded {y:.3f}   exponential + floor {a + b * math.exp(-t / tau):.4f}")

print()
print("Same seven cells, power law fitted from 10,000 upward as recorded (t^-0.34 through 0.040 at 10,000):")
for t, y in zip(T, SHARE):
    if t >= 10_000:
        print(f"  t = {t:>7,}: recorded {y:.3f}   power law {0.040 * (t / 10_000) ** -0.34:.4f}")

print()
print("Where the two descriptions part (not run):")
for t in (1_000_000, 3_000_000):
    print(f"  t = {t:>9,}: exponential + floor {a + b * math.exp(-t / tau):.4f}   power law {0.040 * (t / 10_000) ** -0.34:.4f}")

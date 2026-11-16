"""Q7 - Diagnose and redesign Q6 plain recursion (ways_naive).
Diagnosis: work = number of calls, grows ~1.618**n because the same sub-problem
is solved again and again. Redesign: build up from the bottom, keeping only the
last two answers (each sub-problem solved once; O(n) time, O(1) space, no stack)."""
import sys
import time
sys.path.insert(0, "../Q6")
import temple_steps as t


def ways_bottom_up(n, counter):
    a, b = 1, 1
    for _ in range(n - 1):
        counter[0] += 1                 # one addition per step
        a, b = b, a + b
    return b if n >= 1 else 1


print("A. repeated work in the original (n = 25): how often each w(k) is computed")
seen = {}
orig = t.ways_naive


def counting(n):
    seen[n] = seen.get(n, 0) + 1
    return 1 if n <= 1 else counting(n - 1) + counting(n - 2)


counting(25)
print("   ", {k: seen[k] for k in (25, 20, 15, 10, 5, 1)})
print("D. prediction: calls ~ 1.618^n -> ~n operations; n=30 time drops from ~0.3 s to < 0.01 ms")
print(f"E. {'n':>4} | {'original calls':>14} | {'orig time s':>11} | {'new ops':>7} | {'new time s':>10} | same")
for n in (10, 20, 25, 30, 1000):
    if n <= 30:
        t.calls = 0; s = time.perf_counter(); w1 = t.ways_naive(n); to = time.perf_counter() - s
        oc, ot = f"{t.calls}", f"{to:.6f}"
    else:
        w1, oc, ot = None, "~7e208", "infeasible"
    c = [0]; s = time.perf_counter(); w2 = ways_bottom_up(n, c); tn = time.perf_counter() - s
    print(f"   {n:>4} | {oc:>14} | {ot:>11} | {c[0]:>7} | {tn:10.6f} | {w1 == w2 if w1 else '-'}")

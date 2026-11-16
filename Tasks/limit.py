"""Q6 - Deployment: ways_memo(1000), recursion limit, and the loop version."""
import sys
import time
import temple_steps as t


def ways_loop(n):
    a, b = 1, 1                       # ways(0), ways(1): only two values kept
    for _ in range(n - 1):
        a, b = b, a + b
    return b


print("sys.getrecursionlimit() =", sys.getrecursionlimit())
try:
    t.ways_memo(1000)
except RecursionError as e:
    print("ways_memo(1000) ->", type(e).__name__ + ":", e)
t.ways_memo.cache_clear()
sys.setrecursionlimit(3000)
s = time.perf_counter(); m = t.ways_memo(1000); tm = time.perf_counter() - s
s = time.perf_counter(); l = ways_loop(1000); tl = time.perf_counter() - s
print(f"memo (limit raised to 3000): {tm * 1e3:.3f} ms, cache size {t.ways_memo.cache_info().currsize}")
print(f"loop                        : {tl * 1e3:.3f} ms, 2 variables")
print("same answer:", m == l, "| digits in ways(1000):", len(str(l)))
print("plain recursion for n = 1000: about 7e208 calls - not runnable")

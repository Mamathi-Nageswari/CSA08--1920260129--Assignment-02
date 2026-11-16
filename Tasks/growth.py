"""Q6 - Hand check n=1..6, call tree for n=5, call counts for n=10,20,25,30."""
import temple_steps as t

print("n :", *range(1, 7))
print("by hand :", 1, 2, 3, 5, 8, 13)
print("program :", *[t.ways_naive(n) for n in range(1, 7)])


def tree(n, depth=0):
    print("  " * depth + f"w({n})")
    if n > 1:
        tree(n - 1, depth + 1); tree(n - 2, depth + 1)


print("call tree for n = 5 (w(3) appears 2 times, w(2) 3 times):")
tree(5)
print(f"{'n':>3} | {'ways':>8} | {'naive calls':>11} | {'memo calls':>10}")
for n in (10, 20, 25, 30):
    t.calls = 0; w = t.ways_naive(n); naive = t.calls
    t.ways_memo.cache_clear(); t.calls = 0; t.ways_memo(n); memo = t.calls
    print(f"{n:>3} | {w:>8} | {naive:>11} | {memo:>10}")

"""Q4 - (a) +=  (b) list + join  (c) f-string per line, at 1,000 / 10,000 / 200,000 lines,
run three times and averaged. Also shows why join is safer than relying on the += optimisation."""
import time


def lines(n):
    return [(i, i % 50) for i in range(n)]


def build_plus(rows):
    text = ""
    for i, r in rows:
        text += "Item" + str(i) + ":Rs" + str(r) + ";"
    return text


def build_join(rows):
    parts = []
    for i, r in rows:
        parts.append("Item" + str(i) + ":Rs" + str(r) + ";")
    return "".join(parts)


def build_fstring(rows):
    return "".join([f"Item{i}:Rs{r};" for i, r in rows])


def build_plus_shared(rows):
    """A second reference to text defeats CPython's in-place += optimisation."""
    text = ""
    for i, r in rows:
        keep = text
        text += f"Item{i}:Rs{r};"
    return text


def avg(f, rows, runs=3):
    total = 0
    for _ in range(runs):
        s = time.perf_counter(); f(rows); total += time.perf_counter() - s
    return total / runs


print(f"{'lines':>8} | {'+=':>8} | {'join':>8} | {'f-string':>8} | {'+= shared ref':>13}  (avg of 3, seconds)")
for n in (1_000, 10_000, 50_000, 200_000):
    rows = lines(n)
    assert build_plus(rows) == build_join(rows) == build_fstring(rows)
    shared = f"{avg(build_plus_shared, rows):13.4f}" if n <= 50_000 else f"{'too slow':>13}"
    print(f"{n:>8} | {avg(build_plus, rows):8.4f} | {avg(build_join, rows):8.4f} | "
          f"{avg(build_fstring, rows):8.4f} | {shared}")

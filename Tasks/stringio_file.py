"""Q4 - Alternative concept: io.StringIO and writing line by line to a file."""
import io
import os
import time
import tracemalloc

rows = [(i, i % 50) for i in range(200_000)]


def by_join():
    return "".join([f"Item{i}:Rs{r};" for i, r in rows])


def by_stringio():
    buf = io.StringIO()
    for i, r in rows:
        buf.write(f"Item{i}:Rs{r};")
    return buf.getvalue()


def by_file():
    with open("statement.txt", "w") as f:
        for i, r in rows:
            f.write(f"Item{i}:Rs{r};")
    return os.path.getsize("statement.txt")


for f in (by_join, by_stringio, by_file):
    tracemalloc.start()
    s = time.perf_counter(); out = f(); t = time.perf_counter() - s
    peak = tracemalloc.get_traced_memory()[1]; tracemalloc.stop()
    size = out if isinstance(out, int) else len(out)
    print(f"{f.__name__:12}: {t:.4f} s, peak memory {peak / 1e6:6.2f} MB, output {size} chars")
os.remove("statement.txt")

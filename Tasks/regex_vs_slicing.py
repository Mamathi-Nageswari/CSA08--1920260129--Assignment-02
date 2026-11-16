"""Q3 - Alternative concept: re.fullmatch vs slicing + string methods."""
import re
import timeit
from plate import normalise, is_valid

PATTERN = re.compile(r"[A-Z]{2}[0-9]{2}[A-Z]{1,2}[0-9]{4}")


def is_valid_regex(reg):
    return PATTERN.fullmatch(reg) is not None


tests = ["TN09AB1234", "KA01M0007", "TN9AB1234", "TN221234AB", "TN09ABC1234", "TN09A?1234"]
for t in tests:
    assert is_valid(t) == is_valid_regex(t), t
print("slicing and regex agree on", len(tests), "inputs")
for f in (is_valid, is_valid_regex):
    t = timeit.timeit(lambda: f("TN09AB1234"), number=500_000) / 500_000
    print(f"{f.__name__:15}: {t * 1e9:5.0f} ns per check")

"""Q1 - Alternative concept: match-case and a lookup list of (upper limit, decision)."""
import timeit
from subsidy import subsidy, houses


def subsidy_match(units, ration_card, senior):
    match units:
        case u if u <= 100:
            return "full"
        case u if u <= 200:
            return "partial" if ration_card else "none"
        case _:
            return "senior" if senior else "none"


SLABS = [(100, lambda r, s: "full"), (200, lambda r, s: "partial" if r else "none"),
         (float("inf"), lambda r, s: "senior" if s else "none")]


def subsidy_lookup(units, ration_card, senior):
    for limit, decide in SLABS:          # linear search: O(k) for k slabs
        if units <= limit:
            return decide(ration_card, senior)


for h in houses:
    assert subsidy(*h) == subsidy_match(*h) == subsidy_lookup(*h)
print("match-case and lookup list agree with if-elif-else")
for f in (subsidy, subsidy_match, subsidy_lookup):
    t = timeit.timeit(lambda: f(350, True, True), number=300_000) / 300_000
    print(f"{f.__name__:15}: {t * 1e9:5.0f} ns per decision (worst case, last slab)")

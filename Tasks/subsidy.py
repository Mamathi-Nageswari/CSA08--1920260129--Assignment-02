"""Q1 - Electricity subsidy: separate if statements vs if-elif-else."""

def subsidy_separate_ifs(units, ration_card, senior):
    """The developer's version: separate ifs, so more than one can match."""
    results = []
    if units <= 100:
        results.append("full")
    if units <= 200 and ration_card:          # 'units <= 200' also matches 50 units
        results.append("partial")
    if units > 200 and senior or senior:      # wrong grouping: any senior matches
        results.append("senior")
    return results or ["none"]


def subsidy(units, ration_card, senior):
    """Correct version: if-elif-else with chained comparisons gives exactly one result."""
    if 0 <= units <= 100:
        return "full"
    elif 101 <= units <= 200:
        return "partial" if ration_card else "none"
    elif units > 200 and senior:
        return "senior"
    else:
        return "none"


houses = [(50, False, False), (100, True, False), (101, True, False), (101, False, False),
          (200, True, True), (201, False, False), (201, False, True), (350, True, True)]
predicted = ["full", "full", "partial", "none", "partial", "none", "senior", "senior"]
if __name__ == "__main__":
    print(f"{'units':>5} {'ration':>6} {'80+':>5} | {'predicted':>9} | {'if-elif-else':>12} | separate ifs")
    for (u, r, s), p in zip(houses, predicted):
        good = subsidy(u, r, s)
        print(f"{u:>5} {str(r):>6} {str(s):>5} | {p:>9} | {good:>12} | {subsidy_separate_ifs(u, r, s)}")
        assert good == p
    print("All predictions match the if-elif-else version.")

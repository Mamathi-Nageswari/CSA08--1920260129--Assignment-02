"""Q1 - Design decision: nested if vs combined Boolean conditions (same answers)."""
from subsidy import subsidy, houses


def subsidy_nested(units, ration_card, senior):
    if units <= 100:
        return "full"
    else:
        if units <= 200:
            if ration_card:
                return "partial"
            else:
                return "none"
        else:
            if senior:
                return "senior"
            else:
                return "none"


def subsidy_combined(units, ration_card, senior):
    if units <= 100:
        return "full"
    if 101 <= units <= 200 and ration_card:
        return "partial"
    if units > 200 and senior:
        return "senior"
    return "none"


for h in houses:
    assert subsidy(*h) == subsidy_nested(*h) == subsidy_combined(*h)
print("nested, combined and if-elif-else agree for all 8 households")

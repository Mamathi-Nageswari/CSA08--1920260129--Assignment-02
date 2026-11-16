"""Q3 - Vehicle registration number: normalise, validate, format (no regex)."""


def normalise(text):
    """'tn 09 ab 1234' -> 'TN09AB1234' (spaces and hyphens removed, upper case)."""
    # TODO 1
    return text.strip().replace(" ", "").replace("-", "").upper()


def is_valid(reg):
    """Valid form: 2 letters, 2 digits, 1 or 2 letters, 4 digits (e.g. TN09AB1234)."""
    # TODO 2
    if len(reg) not in (9, 10):
        return False
    state, district, series, number = reg[:2], reg[2:4], reg[4:-4], reg[-4:]
    return state.isalpha() and district.isdigit() and series.isalpha() and number.isdigit()


def format_plate(reg):
    """'TN09AB1234' -> 'TN 09 AB 1234' using slicing and join."""
    return " ".join([reg[:2], reg[2:4], reg[4:-4], reg[-4:]])


if __name__ == "__main__":
    for raw in ["tn 09 ab 1234", "KA-01-M-0007", "TN9AB1234", "TN 22 1234 AB"]:
        reg = normalise(raw)
        print(f"{raw:15} -> {reg:11} {'valid' if is_valid(reg) else 'INVALID'}")
    print()
    predicted = {"tn 09 ab 1234": "TN 09 AB 1234", "TN-09-AB-1234": "TN 09 AB 1234",
                 "Tn09Ab1234": "TN 09 AB 1234", " ka 01 m 0007 ": "KA 01 M 0007",
                 "TN 9 AB 1234": "REJECT", "TN09ABC1234": "REJECT"}
    for raw, pred in predicted.items():
        reg = normalise(raw)
        got = format_plate(reg) if is_valid(reg) else "REJECT"
        print(f"{raw!r:17} predicted {pred:14} got {got:14} {'OK' if got == pred else 'MISMATCH'}")

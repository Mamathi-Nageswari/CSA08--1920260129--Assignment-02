"""Q2 - OTP attempts with while and with for range(3); blank entries are not counted."""
OTP = "4821"
MAX_ATTEMPTS = 3


def verify_while(entries, max_attempts=MAX_ATTEMPTS):
    """while loop: the counter only grows on a real (non-blank) wrong attempt."""
    entries = iter(entries)
    attempts = 0
    while attempts < max_attempts:
        typed = next(entries, "").strip()
        if typed == "":
            print("   blank - not counted")
            continue                     # skip the rest, do not count
        attempts += 1
        if typed == OTP:
            print(f"   attempt {attempts}: correct")
            break                        # stop the loop, else is skipped
        print(f"   attempt {attempts}: wrong")
    else:
        print("   3 wrong attempts - account locked for 30 minutes")
        return "locked"
    return "verified"


def verify_for(entries):
    """for range(3): a blank must be re-read inside, so it does not use up an attempt."""
    entries = iter(entries)
    for attempt in range(1, MAX_ATTEMPTS + 1):
        typed = next(entries, "x").strip()
        while typed == "":
            print("   blank - not counted")
            typed = next(entries, "x").strip()
        if typed == OTP:
            print(f"   attempt {attempt}: correct")
            break
        else:
            pass                         # placeholder: nothing extra to do on a wrong OTP
        print(f"   attempt {attempt}: wrong")
    else:                                # runs only if the loop was not broken
        print("   3 wrong attempts - account locked for 30 minutes")
        return "locked"
    return "verified"


def verify_buggy(entries):
    """Bug: counter updated before the blank check, so blanks use up attempts."""
    entries = iter(entries)
    attempts = 0
    while attempts < MAX_ATTEMPTS:
        attempts += 1
        typed = next(entries, "").strip()
        if typed == "":
            continue
        if typed == OTP:
            return "verified"
    return "locked"


if __name__ == "__main__":
    cases = {"right on 2nd try": ["1111", "4821"], "blank then right": ["", " ", "4821"],
             "three wrong": ["1", "2", "3"]}
    for name, entries in cases.items():
        print(f"{name} {entries}")
        print("  while ->", verify_while(entries))
        print("  for   ->", verify_for(entries))
    print("buggy counter, input ['', '', '', '4821'] ->", verify_buggy(["", "", "", "4821"]),
          "(should be verified)")

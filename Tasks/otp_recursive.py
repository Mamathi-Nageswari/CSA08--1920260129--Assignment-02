"""Q2 - Alternative concept: recursion instead of a loop."""
import inspect
from otp import OTP


def verify_rec(entries, attempts=0, limit=3):
    """Each attempt is a new call; depth grows with attempts (O(a) stack)."""
    depth = len(inspect.stack())
    if attempts == limit:
        return "locked", depth
    typed = entries[0].strip() if entries else "x"
    if typed == "":
        return verify_rec(entries[1:], attempts, limit)
    if typed == OTP:
        return "verified", depth
    return verify_rec(entries[1:], attempts + 1, limit)


base = len(inspect.stack())
for a in (3, 5, 50):
    result, depth = verify_rec(["0"] * a, limit=a)
    print(f"limit {a:>2}: {result}, stack frames used = {depth - base}")

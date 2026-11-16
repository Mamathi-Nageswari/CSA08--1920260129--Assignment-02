"""Q2 - Changed condition: 2 extra attempts after a correct security answer."""
from otp import OTP, verify_while


def verify_with_security(entries, security_ok):
    """Reuse the while design: only max_attempts changes (3, then 2 more)."""
    entries = list(entries)
    result = verify_while(entries[:3])
    if result == "locked" and security_ok:
        print("   security question correct - 2 extra attempts")
        result = verify_while(entries[3:], max_attempts=2)
    return result


print("3 wrong, security ok, then right ->", verify_with_security(["1", "2", "3", "9", OTP], True))
print("3 wrong, security wrong          ->", verify_with_security(["1", "2", "3", OTP], False))

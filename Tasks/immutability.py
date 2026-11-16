"""Q3 - Inquiry: immutability, upper() returns a new string, s[-4:] and s[4:-4]."""
text = "tn09ab1234"
before = id(text)
text.upper()
print("after text.upper()        :", text, "(unchanged)")
text = text.upper()
print("after text = text.upper() :", text, "| same object?", id(text) == before)
try:
    text[0] = "K"
except TypeError as e:
    print("text[0] = 'K' ->", e)
for s in ("TN09A1234", "TN09AB1234"):
    print(f"{s:10} len={len(s):2}  s[-4:]={s[-4:]!r}  s[4:-4]={s[4:-4]!r}")

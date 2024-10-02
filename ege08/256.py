import itertools
b = set()
for a in (itertools.product("0123456789abcdef",repeat=6)):
    if a[0] != "0" and a[0] != "1" and (a[-2] == "a") and (a[-1] == "b"):
        b.add(a)
print(len(b))
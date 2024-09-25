import itertools
b = set()
for a in itertools.product("КЛЕЙ",repeat=6):
    if a.count("Й") < 2 and a[0] != "Й" and a[-1] != "Й" and "ЕЙ" not in "".join(a) and "ЙЕ" not in "".join(a):
        b.add(a)

print(len(b),b)
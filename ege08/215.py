import itertools
b = set()
for a in itertools.product("ПСКАЛЬ",repeat=4):
    if "Ь" != a[0] and "ЬЬ" not in "".join(a):
        b.add(a)

print(len(b),b)
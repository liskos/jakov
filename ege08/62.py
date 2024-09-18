import itertools
b = set()
for a in itertools.product("АБВГДЯ",repeat=3):
    if (((a[0] in "Я") or (a[-1] in "Я")) and (a.count("Я") == 1)) or a.count("Я") == 0:
        b.add(a)
print(len(b),b)


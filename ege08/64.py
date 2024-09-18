import itertools
b = set()
for a in itertools.product("АБВГДЯ",repeat=4):
    if (((a[0] in "Я") or (a[-1] in "Я")) and (a.count("Я") == 1)):
        b.add(a)
print(len(b),b)


import itertools
b = set()
for a in itertools.product("ОБЪЕМ",repeat=4):
    if a.count("О") == 1 and a[0] != "Ъ" and a[-1] != "Ъ":
        b.add(a)

print(len(b),b)
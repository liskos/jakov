import itertools
b = set()
for a in itertools.product("САЛЬСА",repeat=6):
    if a.count("А") < 3:
        b.add(a)
print(len(b),b)
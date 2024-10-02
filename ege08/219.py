import itertools
b = set()
for a in itertools.product("ИНФА",repeat=6):
    if a.count("Ф") == 2:
        b.add(a)

print(len(b),b)
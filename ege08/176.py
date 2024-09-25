import itertools
b = set()
for a in itertools.product("СЧИТАЙ",repeat=4):
    if a.count("А") < 2:
        b.add(a)

print(len(b),b)
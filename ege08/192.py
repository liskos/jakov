import itertools
b = set()
for a in itertools.product("МАРИНА",repeat=6):
    if a.count("А") < 3:
        b.add(a)
print(len(b),b)
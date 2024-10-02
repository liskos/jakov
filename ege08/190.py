import itertools
b = set()
for a in itertools.product("КАЛЬКА",repeat=5):
    if a.count("А") < 3:
        b.add(a)
print(len(b),b)
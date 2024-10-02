import itertools
b = set()
for a in itertools.product("КОРНЕТ",repeat=5):
    if a.count("О") < 2 and a.count("Е") < 2:
        b.add(a)
print(len(b),b)
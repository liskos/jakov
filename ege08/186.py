import itertools
b = set()
for a in itertools.product("БАЛОН",repeat=6):
    if a.count("А") < 2 and a.count("О") < 2:
        b.add(a)
print(len(b),b)
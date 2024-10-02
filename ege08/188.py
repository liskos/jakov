import itertools
b = set()
for a in itertools.product("САКУРА",repeat=5):
    if a.count("А") < 3 and a.count("У") < 2:
        b.add(a)
print(len(b),b)
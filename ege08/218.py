import itertools
b = set()
for a in itertools.product("ПИКАЧУ",repeat=5):
    if a.count("У") > 1:
        b.add(a)

print(len(b),b)
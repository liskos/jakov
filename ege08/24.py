import itertools
b = set()
for i,a in enumerate(itertools.product("МАРТ",repeat=6),1):
    if a.count("Р") == 2:
        b.add(a)
        print(a)
print(len(b))
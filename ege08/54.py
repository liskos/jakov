import itertools
b = set()
for a in itertools.product("СЛОН",repeat=5):
    if 0 < "".join(a).count("О") < 4  :
        b.add(a)
print(len(b))



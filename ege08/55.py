import itertools
b = set()
for a in itertools.product("ЖИРАФ",repeat=6):
    if 0< "".join(a).count("А") < 5:
        b.add(a)
print(len(b))



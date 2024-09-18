import itertools
b = set()
for a in itertools.product("ЖИРАФ",repeat=6):
    if "".join(a).count("А") < 5:
        b.add(a)
print(len(b))



import itertools
b = set()
for a in itertools.product("КОМАР",repeat=4):
    if "".join(a).count("А") < 4:
        b.add(a)
print(len(b))



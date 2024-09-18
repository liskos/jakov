import itertools
b = set()
for a in itertools.product("КРАН",repeat=3):
    if "".join(a).count("А") > 0:
        b.add(a)
print(len(b))
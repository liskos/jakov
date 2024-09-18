import itertools
b = set()
for a in itertools.product("БАЛКОН",repeat=3):
    if "".join(a).count("Б") > 0:
        b.add(a)
print(len(b))
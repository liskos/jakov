import itertools
b = set()
for a in itertools.product("БАЛКОН",repeat=5):
    if "".join(a).count("Б") > 0:
        b.add(a)
print(len(b))
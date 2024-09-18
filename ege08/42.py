import itertools
b = set()
for a in itertools.product("ЛЕТО",repeat=4):
    if "".join(a).count("Е") > 0:
        b.add(a)
print(len(b))
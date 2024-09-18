import itertools
b = set()
for a in itertools.product("МУХА",repeat=5):
    if "".join(a).count("У") < 4:
        b.add(a)
print(len(b))



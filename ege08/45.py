import itertools
b = set()
for a in itertools.product("КЛОУН",repeat=5):
    if "".join(a).count("У") > 0:
        b.add(a)
print(len(b))
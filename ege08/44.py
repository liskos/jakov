import itertools
b = set()
for a in itertools.product("КЛОУН",repeat=4):
    if "".join(a).count("У") > 0:
        b.add(a)
print(len(b))
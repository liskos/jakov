import itertools
b = set()
for i,a in enumerate(itertools.product("ABCX",repeat=5),1):
    if "X" not in "".join(a)[:-1]:
        b.add(a)
print(len(b))
import itertools
b = set()
for i,a in enumerate(itertools.product("ABCX",repeat=5),1):
    if "".join(a).count("X") == 0 or a[-1] == "X":
        b.add(a)
print(len(b))
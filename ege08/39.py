import itertools
b = set()
s = set()
for i,a in enumerate(itertools.product("ABCDX",repeat=4),1):
    if "".join(a).count("X") == 1:
        b.add(a)

print(len(b))
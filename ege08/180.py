import itertools
b = set()
for i,a in enumerate(itertools.product("МЕЧТА",repeat=6),1):
    if a.count("А") > 2:
        b.add(a)

print(len(b))
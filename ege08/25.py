import itertools
b = set()
for i,a in enumerate(itertools.product("ТОК",repeat=6),1):
    if a[0] in "ТК":
        b.add(a)
        print(a)
print(len(b))
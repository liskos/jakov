import itertools
b = set()
for i,a in enumerate(itertools.product("ЛЕТО",repeat=4),1):
    if a[0] in "ЛТ":
        b.add(a)
        print(a)
print(len(b))
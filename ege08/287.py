import itertools
b = set()
n = "AEIOUY"
for a in (itertools.product("POLYGON",repeat=5)):
    if a[2] in n:
        if a == a[::-1]:
            b.add(a)
print(len(b),b)

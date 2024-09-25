import itertools
b = set()
for a in itertools.product("1234",repeat=4):
    if a[0] != "1" and a[1] != a[2]:
        b.add(a)

print(len(b))
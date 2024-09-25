import itertools
b = set()
for a in itertools.product("1234",repeat=5):
    if a[0] != "1" and a[1] != a[3] and a[0] != a[2] and a[2] != a[4]:
        b.add(a)

print(len(b))
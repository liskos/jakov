import itertools
b = set()
for a in itertools.product("1234",repeat=5):
    if a[0] != "1" and a != a[::-1]:
        b.add(a)

print(len(b))
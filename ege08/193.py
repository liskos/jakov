import itertools
b = set()
for a in itertools.product("01234",repeat=6):
    if a[0] == "3":
        b.add(a)
print(len(b),b)
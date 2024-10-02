import itertools
b = set()
for a in itertools.product("0123456789abcdef",repeat=5):
    if a[0] <= a[1] and a[1] <= a[2] and a[2] <= a[3] and a[3] <= a[4] and a[0] != "0":
        b.add(a)
print(len(b))
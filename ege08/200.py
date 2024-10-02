import itertools
b = set()
for a in itertools.product("0123456789",repeat=3):
    if a[0] <= a[1] and a[1] <= a[2] and a[0] != "0":
        b.add(a)
print(len(b))                                                       #or a[1] > a[2] and a[0] <= a[1] or a[0] >= a[1]
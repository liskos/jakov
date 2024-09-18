import itertools
b = set()
k = 0
for a in (itertools.product("АЕС",repeat=6)):
    if a[0] in "АЕ":
        k = k+1
        print(a,k)


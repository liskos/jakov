import itertools

b = set()
k = 0
for a in (itertools.product("АЕСГ", repeat=6)):
    if a[0] in "АЕ" and a[-1] in "Г":
        k = k + 1
        print(a, k)


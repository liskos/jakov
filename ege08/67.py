import itertools
b = set()
for i in itertools.product("ABCDEFGHIJKLMNOPQRSTUVWXYZ", repeat=6):
    if i == i[::-1]:
        b.add(i)
print(len(b), b)
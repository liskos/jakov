import itertools
b = set()
for i in itertools.product("ABCDEFGHIJKLMNOPQRSTUVWXYZ", repeat=3):
        b.add(i)
print(len(b))
print(26**3)
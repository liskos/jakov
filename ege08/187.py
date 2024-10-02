import itertools
b = set()
for a in itertools.product("БАНКИР",repeat=6):
    if a.count("А") < 2 and a.count("И") < 2:
        b.add(a)
print(len(b),b)
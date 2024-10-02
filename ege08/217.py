import itertools
b = set()
for d in range(4,7):
    for a in itertools.product("ЧОАНИМЕ",repeat=d):
        if a.count("М") == 3:
            b.add(a)

print(len(b),b)
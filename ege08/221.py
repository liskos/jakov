import itertools
b = set()
for d in range(4,7):
    for a in itertools.product("ОНИКС",repeat=d):
        ss = "".join(a).replace("О","А")
        if a.count("С") == 3 and a.count("О") == 1:
            b.add(a)

print(len(b),b)
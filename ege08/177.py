import itertools
b = set()
for a in itertools.product("ДЖОБС",repeat=4):
    if a.count("Д") == 1 and a.count("О") == 1 and a.count("С") == 1 and a.count("Ж") < 2:
        b.add(a)

print(len(b),b)
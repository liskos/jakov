import itertools
b = set()
for a in itertools.product("ДЖОБС",repeat=6):
    if a.count("Д") == 1 and a.count("О") == 1 and a.count("С") == 1 and a.count("Ж") < 3:
        b.add(a)

print(len(b),b)
import itertools
b = set()
for a in itertools.product("КОРАБЛИК",repeat = 6):
    if a[0] == "К" or a[0] == "Р" or a[0] == "Б" or a[0] == "Л" and "ОАИ" in a and ("".join(set(a) - set("КОРАБЛИК")==2)):
        b.add(a)
print(len(b))

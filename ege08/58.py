import itertools
b = set()
for a in itertools.product("ПИРОГ",repeat=4):
    if ("".join(a).count("О") < 3) and "ИО" not in "".join(a) and a[0] != "О" :
        b.add(a)
print(len(b),b)



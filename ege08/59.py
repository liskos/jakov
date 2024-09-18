import itertools
b = set()
for a in itertools.product("ПИРОГ",repeat=5):
    ss = "".join(a).replace("О","И").replace("РИ","ХХ")
    if (a.count("Р") < 3) and "Р" not in ss:
        b.add(a)
print(len(b),b)



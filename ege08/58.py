import itertools
b = set()
for a in itertools.product("ПИРОГ",repeat=4):
    ss = "".join(a).replace("Р","П").replace("Г","П")
    ss = ss.replace("ПО","ХХ")
    if (a.count("О") < 3) and ("О" not in ss):
        b.add(a)
print(len(b),b)



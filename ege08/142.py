import itertools
b = set()
for a in itertools.product("ВАЯЮЩИЙ",repeat=4):
    ss = "".join(a).replace("А","И").replace("Я","И").replace("Ю","И")
    if a[0] != "Й" and ss.count("И") > 0:
        b.add("".join(a))
print(len(b),b)
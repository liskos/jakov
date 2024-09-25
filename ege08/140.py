import itertools
b = set()
for a in itertools.product("АРСЕНИЙ",repeat=4):
    ss = "".join(a).replace("А","И").replace("Е","И")
    if a[0] != "Й" and ss.count("И") > 0:
        b.add("".join(a))
print(len(b),b)
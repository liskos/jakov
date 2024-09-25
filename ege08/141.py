import itertools
b = set()
for a in itertools.product("БЕРКЛИЙ",repeat=4):
    ss = "".join(a).replace("Е","И")
    if a[0] != "Й" and ss.count("И") > 0:
        b.add("".join(a))
print(len(b),b)
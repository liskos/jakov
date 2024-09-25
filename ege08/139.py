import itertools
b = set()
for a in itertools.product("ЕНИСЕЙ",repeat=4):
    ss = "".join(a).replace("И","Е")
    if a[0] != "Й" and ss.count("Е") > 0:
        b.add("".join(a))
print(len(b),b)
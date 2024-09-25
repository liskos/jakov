import itertools
b = set()
for a in itertools.product("МОИСЕЙ",repeat=4):
    ss = "".join(a).replace("О","Е").replace("И","Е")
    if a[0] != "Й" and ss.count("Е") > 0:
        b.add("".join(a))
print(len(b),b)
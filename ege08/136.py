import itertools
b = set()
for a in itertools.product("ГЕРОЙ",repeat=4):
    ss = "".join(a).replace("Е","О")
    if a[0] != "Й" and ss.count("О") > 0:
        b.add("".join(a))
print(len(b),b)
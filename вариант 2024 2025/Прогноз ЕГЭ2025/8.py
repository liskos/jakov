import itertools
b = set()
for a in itertools.product("01234567",repeat=7):
    if a[0] != "0":
        if a.count("0") == 2:
            r = "".join(a).replace("2","0").replace("4","0").replace("6","0")
            r = r.replace("3","1").replace("5","1").replace("7","1")
            if ("00" not in r) and ("11" not in r):
                b.add(a)

print(len(b),b)
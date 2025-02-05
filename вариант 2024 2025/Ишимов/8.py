import itertools
s = set()
for a in itertools.product("0123456789ab",repeat=5):
    if a[0] != "0":
        b = "".join(a).replace("2","0").replace("4","0").replace("6","0").replace("8","0").replace("a","0")
        b = b.replace("3","1").replace("5","1").replace("7","1").replace("9","1").replace("b","1")
        if a.count("3") == 1 and ("11" not in b) and ("00" not in b):
            s.add(a)

print(len(s))

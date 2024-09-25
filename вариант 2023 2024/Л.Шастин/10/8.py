import itertools
b = set()
for a in itertools.product("0123456789ab",repeat=5):
    if a[0] != "0":
        ss = "".join(a).replace("2","0").replace("4","0").replace("6","0").replace("8","0").replace("a","0")
        if a.count("a") == 2 and ("07" not in ss) and ("70" not in ss):
            b.add(a)
print(len(b))
import itertools
b = set()
for a in itertools.product("0123456789ab",repeat = 6):
    if a[0] != "0":
        s = "".join(a).replace("2","0").replace("4","0").replace("6","0").replace("8","0").replace("a","0")
        s = s.replace("3","1").replace("5","1").replace("7","1").replace("9","1").replace("b","1")
        if a.count("b") == 1 and s.count("0") == s.count("1"):
            b.add(a)


print(len(b))
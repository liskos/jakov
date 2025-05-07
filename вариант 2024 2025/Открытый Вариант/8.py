import itertools
b = set()
for a in itertools.product("0123456789",repeat=4):
    if a[0] != "0":
        s = "".join(a).replace("2","0").replace("4","0").replace("6","0").replace("8","0")
        s = s.replace("3","1").replace("5","1").replace("7","1").replace("9","1")
        if (len("".join(a)) == len(set("".join(a)))) and ("00" not in s) and ("11" not in s):
            b.add(a)

print(b,
      len(b))
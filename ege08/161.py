import itertools
z = set()
for a in itertools.permutations("01234567",r=6):
    s = "".join(a)
    if a[0] != "0":
        m = s.replace("3", "1").replace("5", "1").replace("7", "1")
        m = m.replace("2","0").replace("4","0").replace("6","0")
        if ("00" not in m) and ("11" not in m):
            z.add(s)

print(len(z))
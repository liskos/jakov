import itertools
z = set()
for a in itertools.permutations("0123456789abcdef",r=3):
    s = "".join(a)
    if a[0] != "0":
        m = s.replace("3", "1").replace("5", "1").replace("7", "1").replace("9", "1").replace("b", "1").replace("d", "1").replace("f","1")
        m = m.replace("2","0").replace("4","0").replace("6","0").replace("8","0").replace("a","0").replace("c","0").replace("e","0")
        if ("00" not in m) and ("11" not in m):
            z.add(s)

print(len(z))
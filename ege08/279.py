import itertools
b = set()
for a in (itertools.permutations("ЭФФЕКТ",r=5)):
    ss = "".join(a).replace("Ф","3").replace("К","1").replace("Т","2")

    if "".join(a).find("Е") < "".join(a).find("Э") and ss.rfind("1") > ss.rfind("2") > ss.rfind("3"):
        b.add(a)
print(len(b),b)

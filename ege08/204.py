import itertools
b = set()
for a in itertools.permutations("0123456789",r=6):
    ss = "".join(a).replace("2","0").replace("4","0").replace("6","0").replace("8","0")
    ss = ss.replace("3","1").replace("5","1").replace("7","1").replace("9","1")
    if "11" not in ss and "00" not in ss and a[0] != "0":
        b.add(a)
print(len(b),b)



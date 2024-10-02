import itertools
b = set()
for w in range(3,6):
    for a in itertools.product("ЛИДА",repeat=w):
        ss = "".join(a).replace("Л","Д")
        if a.count("И") < 3 and a.count("А") < 3 and "Д" not in ss[1:]:
             b.add(a)
print(len(b),b)
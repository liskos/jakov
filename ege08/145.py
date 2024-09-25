import itertools
b = set()
for a in itertools.product("РАДУГА",repeat=6):
    ss = "".join(a).replace("Р","Г").replace("Д","Г")
    if ss.count("Г") > 2:
        b.add("".join(a))
print(len(b),b)
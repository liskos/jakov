import itertools
b = set()
for a in itertools.product("0123456789АБ",repeat=5):
    ss = "".join(a).replace("2","0").replace("4","0").replace("6","0").replace("8","0").replace("А","0")
    if a.count("А") == 2 and ("07" not in ss) and ("70" not in ss):
        b.add(a)
print(len(b))
import itertools
b = set()
for a in itertools.product("АКЛОШ",repeat=5):
    ss = "".join(a).replace("А","О")
    if ss.count("О") > 0:
        b.add(a)

print(len(b),b)
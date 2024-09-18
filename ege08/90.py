import itertools
b = set()
for i,a in enumerate(itertools.product("КРОЙ",repeat=4),1):
    if "".join(a).count("К")==1 and "".join(a).count("Р")==1 and "".join(a).count("О")==1 and "".join(a).count("Й")==1 and a[0] != "Й" and "ОЙ" not in "".join(a):
        b.add("".join(a))
print(len(b))


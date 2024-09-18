import itertools
b = set()
for i,a in enumerate(itertools.product("КОМБАЙН",repeat=7),1):
    if "".join(a).count("К")==1 and "".join(a).count("О")==1 and "".join(a).count("М")==1 and "".join(a).count("Б")==1 and "".join(a).count("А")==1 and "".join(a).count("Й")==1 and "".join(a).count("Н")==1 and a[0] != "Й" and "АЙ" not in "".join(a):
        b.add("".join(a))
print(len(b))


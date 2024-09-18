import itertools
b = set()
for i,a in enumerate(itertools.product("КАБИНЕТ",repeat=7),1):
    if "".join(a).count("К")==1 and "".join(a).count("А")==1 and "".join(a).count("Б")==1 and "".join(a).count("И")==1 and "".join(a).count("Н")==1 and "".join(a).count("Е")==1 and "".join(a).count("Т")==1 and a[0] != "Б" and "ЕА" not in "".join(a):
        b.add("".join(a))
print(len(b))


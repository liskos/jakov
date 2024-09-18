import itertools
b = set()
for i,a in enumerate(itertools.product("ПАЙЩИК",repeat=6),1):
    if "".join(a).count("П")==1 and "".join(a).count("А")==1 and "".join(a).count("Й")==1 and "".join(a).count("Щ")==1 and "".join(a).count("И")==1 and "".join(a).count("К")==1 and a[0] != "Й" and "ТА" not in "".join(a):
        b.add("".join(a))
print(len(b))


import itertools
b = set()
for i,a in enumerate(itertools.product("НИЧЬЯ",repeat=5),1):
    if "".join(a).count("Н")==1 and "".join(a).count("И")==1 and "".join(a).count("Ч")==1 and "".join(a).count("Ь")==1 and "".join(a).count("Я")==1 and a[0] != "Ь" and "ЬИЯ" not in "".join(a):
        b.add("".join(a))
print(len(b))


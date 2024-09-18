import itertools
b = set()
for i,a in enumerate(itertools.product("ПАНЕЛЬ",repeat=6),1):
    if "".join(a).count("П")==1 and "".join(a).count("А")==1 and "".join(a).count("Н")==1 and "".join(a).count("Е")==1 and "".join(a).count("Л")==1 and "".join(a).count("Ь")==1 and a[0] != "Ь" and "ЕЬ" not in "".join(a):
        b.add("".join(a))
print(len(b))


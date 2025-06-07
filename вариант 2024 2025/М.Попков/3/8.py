import itertools

for i,a in enumerate(itertools.product("АКМС",repeat=6),1):
    if a.count("С") == 0 and a.count("М") == 0 and ("КК" not in ("".join(a))):
        print(i,a)
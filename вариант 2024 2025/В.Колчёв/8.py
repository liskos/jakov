import itertools

for i,a in enumerate(itertools.product("ДИКМО",repeat=5),1):
    if ("ММ" not in ("".join(a))) and a.count("М") == 2:
        print(i,a)
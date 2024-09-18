import itertools
b = set()
for i,a in enumerate(itertools.product("ВЕКНО",repeat=5),1):
    if "".join(a).count("Н")==2 and "".join(a).count("К")==2:
        print(a,i)


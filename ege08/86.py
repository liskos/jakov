import itertools
b = set()
for i,a in enumerate(itertools.product("ВЕКНО",repeat=5),1):
    if "".join(a).count("О")==1 and "".join(a).count("Е")==1:
        print(a,i)


import itertools
b = set()
for i,a in enumerate(itertools.product("АВГДИНОР",repeat=4),1):
    if a[0] == "И" and a[1] == "Р":
        print(a,i)



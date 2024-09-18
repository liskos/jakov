import itertools
b = set()
for i,a in enumerate(itertools.product("АВГДИНОР",repeat=4),1):
    if a[0] == "Г" and a[1] == "О":
        print(a,i)



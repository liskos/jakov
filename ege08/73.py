import itertools
b = set()
for i,a in enumerate(itertools.product("АРТФ",repeat = 5),1):
    if a[0] == "Т":
        print(i,a)

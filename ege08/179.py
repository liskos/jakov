import itertools
b = set()
for i,a in enumerate(itertools.product("ЩОГБА",repeat=6),1):
    if "".join(a) == "ОБЩАГА":
        print(i)


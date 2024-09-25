import itertools
b = set()
for i,a in enumerate(itertools.product("АВИКНСТ",repeat=4),1):
    if a[0] not in "АИ" and a[-1] in "АИ":
        if "".join(a) == "НИКА":
            print(i)


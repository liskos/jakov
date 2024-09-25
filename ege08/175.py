import itertools
b = set()
k=0
for a in itertools.product("АВИКНСТ",repeat=4):
    if a[0] not in "АИ" and a[-1] in "АИ":
        k += 1
    if "".join(a) == "НИКА":
            print(k)

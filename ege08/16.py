import itertools
for i,a in enumerate(itertools.product("АКРУ",repeat=5),1):
    if "".join(a) == "УКАРА":
        print(i,"".join(a))
import itertools
for i,a in enumerate(itertools.product("АКРУ",repeat=5),1):
    if "".join(a) == "РУКАА":
        print(i,"".join(a))
import itertools
for i,a in enumerate(itertools.product("АКРУ",repeat=5),1):
    if a[0] == "К":
        print(i,"".join(a))
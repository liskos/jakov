import itertools
b = set()
for i,a in enumerate(itertools.product("АВГЕН",repeat=4),1):
    if "".join(a).count("А") == 0:
        print(a,i)



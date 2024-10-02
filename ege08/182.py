import itertools
b = set()
for i,a in enumerate(itertools.product("АВДПР",repeat=4),1):
    if a.count("А") == 0 and a.count("В") == 1 and a.count("Д") == 1 and a.count("П") == 1:
            print(i,a)

import itertools
for i,a in enumerate(itertools.product("ЬСОНЕ",repeat=4),1):
    if i == 100:
        print(i,"".join(a))
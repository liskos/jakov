import itertools
for i,a in enumerate(itertools.product("КОР",repeat=5),1):
    if i == 182:
        print(i,"".join(a))
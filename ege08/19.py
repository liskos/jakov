import itertools
for i,a in enumerate(itertools.product("АМРТ",repeat=4),1):
    if i == 250:
        print(i,"".join(a))
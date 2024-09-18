import itertools
b = set()
for i,a in enumerate(itertools.product("АГИЛМОРТ",repeat=4),1):
    if a[-2] == "И" and a[-1] == "М":
        print(a,i)


import itertools
for i,a in enumerate(itertools.product("АОУ",repeat=5),1):
    if "".join(a) == "ОАОАО":
        print(i,"".join(a))
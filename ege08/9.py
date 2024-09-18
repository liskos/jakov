import itertools
for i,a in enumerate(itertools.product("АОУ",repeat=5),1):
    if a[0] == "У":
        print(i,"".join(a))
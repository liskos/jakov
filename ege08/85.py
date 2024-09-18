import itertools
b = set()
for i,a in enumerate(itertools.product("АОУ",repeat=5),1):
    if a[2] == "У":
        print(a,i)


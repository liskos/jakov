import itertools

for i,a in enumerate(itertools.product("АОУ",repeat=5),1):
    if i == 170:
        print("".join(a))

import itertools

s = set()
for i,a in enumerate(itertools.product("АОУ",repeat=5),1):
    if "".join(a) == "УАУАУ" or "".join(a) == "ОУОУА":
        print(i,a)

print(183-151+1)
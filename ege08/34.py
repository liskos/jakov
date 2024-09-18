import itertools

s = set()
for i,a in enumerate(itertools.product("АЗНС",repeat=5),1):
    if "".join(a) == "САЗАН" or "".join(a) == "ЗАНАС":
        print(i,a)

print(787-292)
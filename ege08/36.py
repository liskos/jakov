import itertools

s = set()
for i,a in enumerate(itertools.product("АМРТ",repeat=4),1):
    if "".join(a) == "МАРТ" or "".join(a) == "РАМТ":
        print(i,a)

print(136-76)
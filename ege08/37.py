import itertools

s = set()
for i,a in enumerate(itertools.product("АКРУ",repeat=5),1):
    if "".join(a) == "РУКАА" or "".join(a) == "УКАРА":
        print(i,a)

print(841-721+1)
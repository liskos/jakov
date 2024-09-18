import itertools

s = set()
for i,a in enumerate(itertools.product("ОПРТ",repeat=5),1):
    if "".join(a) == "ТОПОР" or "".join(a) == "РОПОТ":
        print(i,a)

print(787-532+1)
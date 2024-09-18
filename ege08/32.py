import itertools

s = set()
for a in itertools.product("ABCD",repeat=3):
    if "BC" not in "".join(a) and "CB" not in "".join(a):
        if a.count("A") == 0:
            s.add(a)
        elif (a.count("A") == 1) and ("AD" in "".join(a) or "DA" in "".join(a)):
            s.add(a)
        elif a.count("A") == 2 and ("ADA" in "".join(a)):
            s.add(a)
print(len(s),s)
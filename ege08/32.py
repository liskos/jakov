import itertools

s = set()
for a in itertools.product("ABCD",repeat=3):

    if "BC" not in "".join(a) and "AD" in "".join(a) or "DA" in "".join(a):
        s.add(a)
print(len(s),s)
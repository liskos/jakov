import itertools

s = set()
for a in itertools.product("КАНТ",repeat=6):

    if "".join(a).count("К") == 2:
        s.add(a)
print(len(s))
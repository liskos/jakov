import itertools

s = set()
for a in itertools.product("КРАНТ",repeat=5):

    if "".join(a).count("К") == 2:
        s.add(a)
print(len(s))
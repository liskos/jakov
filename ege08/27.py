import itertools

s = set()
for a in itertools.product("КРОТ",repeat=6):

    if "".join(a).count("О") == 1:
        s.add(a)
print(len(s))
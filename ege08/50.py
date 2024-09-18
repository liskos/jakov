import itertools
b = set()
for a in itertools.product("КАТЕР",repeat=4):
    if "".join(a).count("Р") > 1:
        b.add(a)
print(len(b))
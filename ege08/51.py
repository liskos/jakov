import itertools
b = set()
for a in itertools.product("КАТЕР",repeat=5):
    if "".join(a).count("Р") > 1:
        b.add(a)
print(len(b))



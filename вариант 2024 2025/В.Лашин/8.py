import itertools
b = set()
for a in itertools.product("КОТБУС",repeat=8):
    if (a[0] not in "УО") and ("".join(a).count("КОТ") > 0):
        b.add(a)

print(len(b))
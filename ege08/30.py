import itertools

s = set()
for a in itertools.product("ГОД",repeat=6):

    if a[0] in "ГД" and a[-1] in "ГД":
        s.add(a)
print(len(s))
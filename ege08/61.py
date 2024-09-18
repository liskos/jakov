import itertools
b = set()
for a in itertools.product("АБВГДЭЮЯ",repeat=5):
    if (a[0] in "ЭЮЯ") and (a[-1] in "ЭЮЯ") and all(x not in a[1:-1] for x in "ЭЮЯ"):
        b.add(a)
print(len(b),b)


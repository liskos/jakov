import itertools

s = set()
for a in itertools.product("КУМА",repeat=5):

    if (a[0] in "КМ") and (a[-1] in "УА"):
        s.add(a)
print(len(s),s)
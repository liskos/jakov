import itertools
b = set()
for a in itertools.product("КАЛИЙ",repeat=6):
    if a.count("Й") < 2 and a[0] != "Й" and a[-1] != "Й" and "ИЙ" not in "".join(a) and "ЙИ" not in "".join(a):
        b.add(a)

print(len(b),b)
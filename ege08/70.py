import itertools
b = set()
for a in itertools.product("АБВГ",repeat = 5):
    if (a.count("Г") == 1 and a[-1] == "Г") or a.count("Г") == 0:
        b.add(a)
print(len(b),b)

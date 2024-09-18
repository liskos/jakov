import itertools
b = set()
for a in itertools.product("АБВГДЕ",repeat = 4):
    if a.count("Г") == 1 and (a[0] == "Г" or a[-1] == "Г"):
        b.add(a)
print(len(b),b)

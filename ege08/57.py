import itertools
b = set()
for a in itertools.product("ПИРОГ",repeat=6):
    if ("".join(a).count("Р") == 1) and ("РИ" or "РО") in "".join(a):
        b.add(a)
print(len(b),b)



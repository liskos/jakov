import itertools
b = set()
for a in itertools.product("ПИРОГ",repeat=6):
    if ("".join(a).count("Р") == 1) and ("РИ" in "".join(a)  or "РО" in "".join(a)):
        b.add(a)
print(len(b),b)



import itertools
b = set()
for a in itertools.product("ПИРОГ",repeat=5):
    if ("".join(a).count("Р") < 3) and "РП" not in "".join(a) and "РГ" not in "".join(a):
        b.add(a)
print(len(b),b)



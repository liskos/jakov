import itertools
b = set()
for a in itertools.product("АБВГДЯ",repeat=3):
    if a[0] == "Я" or a[-1] == "Я" and "".join(a).count("Я") < 2:
        b.add(a)
print(len(b),b)



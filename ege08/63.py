import itertools
b = set()
for a in itertools.product("АБВГДЯ",repeat=4):
    if a.count("Я") < 2:
        if a.count("Я")== 1:
            a[0] == "Я" or a[-1] == "Я"
            b.add(a)
print(len(b),b)



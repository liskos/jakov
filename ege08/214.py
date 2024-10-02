import itertools
b = set()
for a in itertools.permutations("ВАЙФУ",r=4):
    if "Й" != a[0] and "ВФ" not in "".join(a) and "ФВ" not in "".join(a):
        b.add(a)

print(len(b),b)
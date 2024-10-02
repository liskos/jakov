import itertools
b = set()
for a in itertools.permutations("ТЬЮРИНГ",r=6):
    ss = "".join(a).replace("Ю","И")
    if "Ь" != a[0] and "ИЬ" not in ss:
        b.add(a)

print(len(b),b)
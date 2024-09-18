import itertools
b = set()
for a in (itertools.permutations("ШАНЕЛЬ",r=6)):
    if (a[0] != "Ь") and ("ЕАЬ" not in "".join(a)):
        b.add("".join(a))
print(len(b))


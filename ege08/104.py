import itertools
b = set()
for a in (itertools.permutations("НАДПИСЬ",r=7)):
    if (a[0] != "Ь") and ("ЬИА" not in "".join(a)):
        b.add("".join(a))
print(len(b))


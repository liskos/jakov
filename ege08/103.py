import itertools
b = set()
for a in (itertools.permutations("КУПЧИХА",r=7)):
    if (a[0] != "Ч") and ("ИАУ" not in "".join(a)):
        b.add("".join(a))
print(len(b))


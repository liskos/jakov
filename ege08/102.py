import itertools
b = set()
for a in (itertools.permutations("НИГРОЛ",r=6)):
    if (a[0] != "О") and ("ОИГ" not in "".join(a)):
        b.add("".join(a))
print(len(b))


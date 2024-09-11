import itertools
s = set()
for a in itertools.permutations("КУПЧИХА",r=7):
    if (a[0] != "Ч") and ("ИУА" not in "".join(a)):
        s.add(a)
print(len(s))
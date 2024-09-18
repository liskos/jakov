import itertools
b = set()
for a in itertools.permutations("ПАЙЩИК",r=6):
    if a[0] != "Й" and "ИА" not in "".join(a):
        b.add("".join(a))
print(len(b))


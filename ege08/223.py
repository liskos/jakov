import itertools
b = set()
for a in itertools.permutations("ОДЕКОЛОН",r=6):
    if "ОО" not in "".join(a):
        b.add(a)

print(len(b))
import itertools
b = set()
for a in (itertools.permutations("СПОРТЛОТО",r=9)):
    if a[0] == "О":
        b.add(a)
print(len(b))

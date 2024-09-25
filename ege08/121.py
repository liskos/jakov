import itertools
b = set()
for a in (itertools.permutations("ТАРТАР",r=6)):
        b.add("".join(a))
print(len(b),b)


import itertools
b = set()
for a in (itertools.permutations("ТРАТАТА",r=7)):
        b.add("".join(a))
print(len(b),b)


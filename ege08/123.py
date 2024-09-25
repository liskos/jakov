import itertools
b = set()
for a in (itertools.permutations("АССАСИН",r=7)):
        b.add("".join(a))
print(len(b),b)


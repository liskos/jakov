import itertools
b = set()
for a in (itertools.permutations("СПОРТЛОТО",r=9)):
    if "ООО" in "".join(a):
        b.add(a)
print(len(b),b)

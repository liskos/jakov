import itertools
b = set()
for a in (itertools.permutations("СПОРТЛОТО",r=9)):
    if a[0] == a[-1]:
        b.add(a)
print(len(b),b)

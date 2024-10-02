import itertools
b = set()
for a in itertools.permutations("МИМИКРИЯ",r=8):
        b.add(a)


print(len(b),b)
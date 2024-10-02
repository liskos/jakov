import itertools
b = set()
for a in (itertools.permutations("СПОРТЛОТО",r=9)):
    if a[-1] != "О":
        b.add(a)
print(len(b))

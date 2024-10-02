import itertools
b = set()
for a in itertools.permutations("КЛАБХАУС",r=8):
    if "АА" not in "".join(a):
        b.add(a)

print(len(b),b)
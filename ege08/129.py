import itertools
b = set()
for a in itertools.permutations("ВОРОН",r=5):
    if "ОО" not in "".join(a):
        b.add("".join(a))
print(len(b),b)
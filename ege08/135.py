import itertools
b = set()
for a in itertools.permutations("КАБАЛА",r=6):
    if "АА" not in "".join(a):
        b.add("".join(a))
print(len(b),b)
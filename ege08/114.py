import itertools
b = set()
for a in (itertools.permutations("АБАК",r=4)):
    if ("АА" not in "".join(a)) and ("ББ" not in "".join(a)) and ("КК "not in "".join(a)):
        b.add("".join(a))
print(len(b),b)


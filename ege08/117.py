import itertools
b = set()
for a in (itertools.permutations("КАБАЛА",r=6)):
    if ("КК" not in "".join(a)) and ("АА" not in "".join(a)) and ("ББ" not in "".join(a)) and ("ЛЛ" not in "".join(a)):
        b.add("".join(a))
print(len(b),b)


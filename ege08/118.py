import itertools
b = set()
for a in (itertools.permutations("АВРОРА",r=6)):
    if ("АА" not in "".join(a)) and ("ВВ" not in "".join(a)) and ("РР" not in "".join(a)) and ("ОО" not in "".join(a)):
        b.add("".join(a))
print(len(b),b)


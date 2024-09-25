import itertools
b = set()
for a in (itertools.permutations("АДЖИКА",r=6)):
    if ("АА" not in "".join(a)) and ("ДД" not in "".join(a)) and ("ЖЖ" not in "".join(a)) and ("ИИ" not in "".join(a)) and ("КК" not in "".join(a)):
        b.add("".join(a))
print(len(b),b)


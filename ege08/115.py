import itertools
b = set()
for a in (itertools.permutations("МАРТА",r=5)):
    if ("АА" not in "".join(a)) and ("ММ" not in "".join(a)) and ("РР" not in "".join(a)) and ("ТТ" not in "".join(a)):
        b.add("".join(a))
print(len(b),b)


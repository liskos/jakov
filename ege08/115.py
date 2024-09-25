import itertools
b = set()
for a in (itertools.permutations("МАРТА",r=5)):
    if ("АА" not in "".join(a)):
        b.add("".join(a))
print(len(b),b)


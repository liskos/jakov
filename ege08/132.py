import itertools
b = set()
for a in itertools.permutations("АСПЕКТ",r=6):
    ss = "".join(a).replace("Е","А")
    if "АА" not in ss:
        b.add("".join(a))
print(len(b),b)
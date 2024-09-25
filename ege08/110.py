import itertools
b = set()
for a in (itertools.permutations("РУЛЬКА",r=6)):
    ss = "".join(a).replace("У","А")
    if a[0] != "О" and ("АЬ" not in ss):
        b.add("".join(a))
print(len(b),b)


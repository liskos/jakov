import itertools
b = set()
for a in (itertools.permutations("АБРИКОС",r=6)):
    ss = "".join(a).replace("Б","С").replace("А","О").replace("Р","С").replace("И","О").replace("К","С")
    if ("СС" not in ss)and("ОО" not in ss):
        b.add("".join(a))
print(len(b),b)


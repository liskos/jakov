import itertools
b = set()
for a in (itertools.permutations("ПЕСКАРЬ",r=7)):
    ss = "".join(a).replace("Е","А").replace("Р","А")
    if a[0] != "Ь" and ("ЬА" not in ss):
        b.add("".join(a))
print(len(b),b)


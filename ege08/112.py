import itertools
b = set()
for a in (itertools.permutations("ВЕНТИЛЬ",r=7)):
    ss = "".join(a).replace("Е","И")
    if a[-1] != "Ь" and ("ИЬИ" not in ss):
        b.add(a)
print(len(b),b)


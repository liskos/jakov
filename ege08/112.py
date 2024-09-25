import itertools
b = set()
for a in (itertools.permutations("ВЕНТИЛЬ",r=7)):
    ss = "".join(a).replace("Е","И")
    if a[-1] != "Ь" and ("ИЬИ" not in ss) and ("ЬЕ" not in ss) and ("ЕЬ" not in ss) and ("ИЬ" not in ss) and ("ЬИ" not in ss):
        b.add("".join(a))
print(len(b),b)


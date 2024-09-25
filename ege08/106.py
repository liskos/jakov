import itertools
b = set()
for a in (itertools.permutations("НОДА",r=4)):
    ss = "".join(a).replace("Н","Д").replace("О","Я")
    if ("ДД" not in ss)and("ЯЯ" not in ss):
        b.add("".join(a))
print(len(b))


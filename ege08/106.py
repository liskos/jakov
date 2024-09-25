import itertools
b = set()
for a in (itertools.permutations("НОДА",r=4)):
    ss = "".join(a).replace("Н","Д").replace("О","А")
    if ("ДД" not in ss)and("АА" not in ss):
        b.add("".join(a))
print(len(b))


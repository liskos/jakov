import itertools
b = set()
for a in (itertools.permutations("КОЛУН",r=5)):
    ss = "".join(a).replace("К","Н").replace("О","У").replace("Л","Н")
    if ("НН" not in ss)and("УУ" not in ss):
        b.add("".join(a))
print(len(b),b)


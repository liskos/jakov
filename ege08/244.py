import itertools
b = set()
for a in itertools.permutations("ШАРЛАТАН",r=8):
    ss = "".join(a).replace("Ш","Н").replace("Р","Н").replace("Л","Н").replace("Т","Н")
    if ("АА" in ss) or ("ВВ" in ss):
        b.add(a)

print(len(b),b)
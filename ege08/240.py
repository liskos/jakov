import itertools
b = set()
for a in itertools.permutations("АКАРИДА",r=7):
    ss = "".join(a).replace("К","Д").replace("Р","Д")
    ss = ss.replace("И","А")
    if ("АА" not in ss) and ("ДД" not in ss):
        b.add(a)

print(len(b))
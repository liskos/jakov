import itertools
b = set()
for a in itertools.permutations("АББАТИСА",r=8):
    ss = "".join(a).replace("И","А")
    ss = ss.replace("Т","Б").replace("С","Б")
    if "АА" not in ss and "ББ" not in ss:
        b.add(a)

print(len(b))
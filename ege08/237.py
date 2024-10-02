import itertools
b = set()
for a in itertools.permutations("БАРХАТКА",r=8):
    ss = "".join(a).replace("Б","К").replace("Р","К").replace("Х","К").replace("Т","К")
    if ("АА" not in ss) and ("КК" not in ss):
        b.add(a)

print(len(b))
import itertools
b = set()
for a in itertools.permutations("ВЕРЕТЕНО",r=8):
    ss = "".join(a).replace("В","Н").replace("Р","Н").replace("Т","Н")
    ss = ss.replace("О","Е")
    if ("ЕЕ" not in ss) and ("НН" not in ss):
        b.add(a)

print(len(b))
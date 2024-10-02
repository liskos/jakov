import itertools
b = set()
for a in itertools.permutations("ПРЕПАРАТ",r=8):
    ss = "".join(a).replace("Р","П").replace("Т","П")
    ss = ss.replace("Е","А")
    if ("АА" in ss) or ("ПП" in ss):
        b.add(a)

print(len(b),b)
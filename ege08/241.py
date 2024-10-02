import itertools
b = set()
for a in itertools.permutations("АММИАКАТ",r=8):
    ss = "".join(a).replace("Т","М").replace("К","М")
    ss = ss.replace("И","А")
    if ("АА" in ss) or ("ММ" in ss):
        b.add(a)

print(len(b),b)
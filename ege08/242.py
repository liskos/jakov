import itertools
b = set()
for a in itertools.permutations("АТТЕСТАТ",r=8):
    ss = "".join(a).replace("С","Т")
    ss = ss.replace("Т","А")
    if ("АА" in ss) or ("ТТ" in ss):
        b.add(a)

print(len(b),b)
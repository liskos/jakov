import itertools
b = set()
for a in itertools.permutations("ЗАПИСЬ",r=6):
    ss = "".join(a).replace("А","И")
    if a[0] != "Ь" and ("ИЬ" not in ss):
        b.add(a)

print(len(b),b)
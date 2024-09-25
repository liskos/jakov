import itertools
b = set()
for a in itertools.permutations("ВОРОТА",r=6):
    ss = "".join(a).replace("А","О")
    if "ОО" not in ss:
        b.add("".join(a))
print(len(b),b)
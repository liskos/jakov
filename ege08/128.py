import itertools
b = set()
for a in itertools.permutations("АПОРТ",r=5):
    ss = "".join(a).replace("А","О")
    if "ОО" not in ss:
        b.add("".join(a))
print(len(b),b)
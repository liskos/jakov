import itertools
b = set()
for a in (itertools.permutations("ПРИКАЗ",r=4)):
    ss = "".join(a).replace("И","А")
    if ss.count("А") < 2:
        b.add("".join(a))
print(len(b),b)


import itertools
b = set()
for a in (itertools.permutations("ABCDEFGHIKLMNOPQRSTVXYZ",r=5)):
    ss = "".join(a).replace("E","A").replace("I","A").replace("O","A").replace("Y","A")
    if ss.count("A") > 0:
        b.add(a)
print(len(b))

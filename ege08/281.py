import itertools
b = 0
for a in (itertools.permutations("ABCDEFGHIKLMNOPQRSTVXYZ",r=5)):
    ss = "".join(a).replace("E","A").replace("I","A").replace("O","A").replace("Y","A")
    b += ss.count("A")
print(b)

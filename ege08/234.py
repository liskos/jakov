import itertools
b = set()
for a in itertools.permutations("АКАДЕМИК",r=8):
    ss = "".join(a).replace("Е","И").replace("А","И")
    ss = ss.replace("Д","К").replace("М","К")
    if "КК" not in ss and "ИИ" not in ss:
        b.add(a)

print(len(b))
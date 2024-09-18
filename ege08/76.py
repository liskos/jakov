import itertools
b = set()
for a in itertools.permutations("КОРАБЛИ",r = 5):
    s =  ''.join(a)
    ss = s.replace("Р","К").replace("Б","К").replace("Л","К")
    ss = ss.replace("А","О").replace("И","О")
    if ss[0] == "О" and ("КК" not in ss) and ("ОО" not in ss):
        b.add(a)
print(len(b))

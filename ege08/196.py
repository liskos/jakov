import itertools
b = set()
for w in range(3,12):
    for a in itertools.product("КРЫША",repeat=w):
        ss = "".join(a).replace("К","Ш").replace("Р","Ш")
        if a.count("Ы") < 3 and a.count("А") < 3 and "Ш" not in ss[1:]:
             b.add(a)
print(len(b),b)
import itertools
b = set()
for w in range(3,11):
    for a in itertools.product("КСЕНИЯ",repeat=w):
        ss = "".join(a).replace("К","Н").replace("С","Н")
        if a.count("Е") < 3 and a.count("И") < 3 and a.count("Я") < 3 and "Н" not in ss[1:]:
             b.add(a)
print(len(b),b)
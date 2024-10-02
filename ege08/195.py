import itertools
b = set()
for w in range(3,10):
    for a in itertools.product("СЕПИЯ",repeat=w):
        ss = "".join(a).replace("С","П")
        if a.count("Е") < 3 and a.count("И") < 3 and a.count("Я") < 3 and "П" not in ss[1:]:
             b.add(a)
print(len(b),b)
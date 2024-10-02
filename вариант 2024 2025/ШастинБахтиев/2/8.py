import itertools
b = set()
for a in itertools.product("ЛЮСТРА",repeat=5):
    ss = "".join(a).replace("Ю","А")
    if a.count("Ю") < 3 and ss[-1] == "А":
        b.add(a)
print(len(b),b)
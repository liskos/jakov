import itertools
b = set()
for i,a in enumerate(itertools.product("01234567",repeat=5),1):
    ss = "".join(a).replace("65","l").replace("56","d")
    if a[0] == "7" and (ss.count("l") == 1 or ss.count("d") == 1) and int(a[-1]) % 2 == 0:
        b.add(a)
print(len(b),b)
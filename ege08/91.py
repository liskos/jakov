import itertools
b = set()
for i,a in enumerate(itertools.product("КАЛИЙ",repeat=5),1):
    if "".join(a).count("К")==1 and "".join(a).count("А")==1 and "".join(a).count("Л")==1 and "".join(a).count("И")==1 and "".join(a).count("И")==1 and a[0] != "Й" and "ИА" not in "".join(a):
        b.add("".join(a))
print(len(b))


import itertools
b = set()
for i,a in enumerate(itertools.product("ГЕЛИЙ",repeat=5),1):
    if "".join(a).count("Г")==1 and "".join(a).count("Е")==1 and "".join(a).count("Л")==1 and "".join(a).count("И")==1 and "".join(a).count("Й")==1 and a[0] != "Й" and "ИЕЙ" not in "".join(a):
        b.add("".join(a))
print(len(b))


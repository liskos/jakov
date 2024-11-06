import itertools
b = set()
for a in itertools.product("01234567",repeat=5):
    if a[0] != "0":
        ss = "".join(a).replace("3","1").replace("5","1").replace("7","1")
        if ss[0] != "1" and a[-1] not in "26" and a.count("7") < 3:
            b.add(a)

print(len(b),b)
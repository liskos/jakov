import itertools
b = set()
f = []
for a in itertools.permutations("0123456789abcdef", r=15):
    if a[0] != "0":
        ss = "".join(a).replace("2", "0").replace("4", "0").replace("6", "0").replace("8", "0").replace("a", "0").replace("c", "0").replace("e", "0")
        ss = ss.replace("3","1").replace("5","1").replace("7","1").replace("9","1").replace("b","1").replace("d","1").replace("f","1")
        if ("00" not in ss) and ("11" not in ss):
            f.append("".join(a))
f.sort(reverse=True)
for item in f:
    if f == item:
        b.add(item)
print(len(b), b)
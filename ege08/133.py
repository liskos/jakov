import itertools
b = set()
for a in itertools.permutations("ЗДАНИЕ",r=6):
    ss = "".join(a).replace("А","Е").replace("И","Е")
    if "ЕЕ" not in ss:
        b.add("".join(a))
print(len(b),b)
import itertools
b = set()
for a in itertools.product("РАЗМАХ",repeat=6):
    ss = "".join(a).replace("Р","М").replace("З","М").replace("Х","М")
    if ss.count("М") > 2:
        b.add("".join(a))
print(len(b),b)
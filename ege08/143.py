import itertools
b = set()
for a in itertools.product("РУСТАМ",repeat=6):
    ss = "".join(a).replace("Р","М").replace("С","М").replace("Т","М")
    if ss.count("М") > 2:
        b.add("".join(a))
print(len(b),b)
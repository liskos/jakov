import itertools
b = set()
for a in itertools.product("КАРКАС",repeat=6):
    ss = "".join(a).replace("Р","К").replace("С","К")
    if ss.count("К") > 2:
        b.add("".join(a))
print(len(b),b)
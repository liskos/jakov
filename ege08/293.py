import itertools
b = set()
for a in (itertools.product("ТИМАШЕВСК",repeat=6)):
    v = "".join(a).replace("Т","К").replace("М","К").replace("В","К").replace("С","К")
    ss = "".join(a).replace("И","Е").replace("А","Е")
    ss = ss.replace("Т","К").replace("М","К").replace("Ш","К").replace("В","К").replace("С","К")
    if ss.count("К") > ss.count("Е") and ("КШ" not in v) and ("ШК" not in v):
        b.add(a)
print(len(b))

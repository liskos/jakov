import itertools
b = set()
for a in (itertools.product("ТИМАШЕВСК",repeat=5)):
    v = "".join(a).replace("И","Е").replace("А","Е")
    ss = "".join(a).replace("И","Е").replace("А","Е")
    ss = ss.replace("Т","К").replace("М","К").replace("Ш","К").replace("В","К").replace("С","К")
    if ("ЕШ" not in v) and ("ШЕ" not in v) and ("ШВ" not in v) and ("ВШ" not in v):
        b.add(a)
print(len(b))

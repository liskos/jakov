import itertools
b = set()
for a in (itertools.product("ТИМАШЕВСК",repeat=4)):
    v = "".join(a).replace("И","Е").replace("А","Е")
    ss = "".join(a).replace("И","Е").replace("А","Е")
    ss = ss.replace("Т","К").replace("М","К").replace("Ш","К").replace("В","К").replace("С","К")
    if ss[0] != "Е" and a[0] != "Ш":
            b.add(a)
print(len(b),b)

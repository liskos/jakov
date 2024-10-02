import itertools
b = set()
for i,a in enumerate(itertools.product("ШТСМКИЕВА",repeat=5),1):
    g = "".join(a).replace("И","А").replace("Е","А")
    s = "".join(a).replace("Т","К").replace("М","К").replace("Ш","К").replace("В","К").replace("С","К")
    if ("".join(a) == "".join(a)[::-1]) and s[2] == "К" and g.count("А") == 4:
            print(i,a)

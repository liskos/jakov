import itertools
b = set()
for a in itertools.product("АЗИМУТ",repeat=6):
    ss = "".join(a).replace("З","Т").replace("М","Т")
    if ss.count("Т") > 2:
        b.add("".join(a))
print(len(b),b)
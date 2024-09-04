import itertools
v = []
for a in itertools.product("0123456789abcd",repeat=5):
    if a[0] != "0" and a.count("9") == 1 and a.count("b")+a.count("c")+a.count("d") <=3:
        v.append(a)
print(len(v))
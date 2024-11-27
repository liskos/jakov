import itertools
k = 0
for a in itertools.product("012345678",repeat=5):
    if a[0] != "0":
        if a.count("5") == 1 and "".join(a).count("00") == 0 and "".join(a).count("11") == 0 and "".join(a).count("22") == 0 and "".join(a).count("33") == 0 and "".join(a).count("44") == 0 and "".join(a).count("66") == 0 and "".join(a).count("77") == 0 and "".join(a).count("88") == 0:
            k+=1

print(k)
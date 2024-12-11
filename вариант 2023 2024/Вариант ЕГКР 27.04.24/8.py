import itertools
k = 0
for a in itertools.product("0123456",repeat=7):
    if a[0]!= "0":
        ss = "".join(a).replace("2","0").replace("4","0").replace("6","0")
        if ss.count("0") == 2:
            k+=1
            print(a)


print(k)
import itertools
b = set()
for a in (itertools.product("САМОКАТ",repeat=7)):
    ss = "".join(a).replace("САМ","hjk")
    if ss.count("hjk") == 1 and ss.find("k") != 6:
        if ss[int(ss.find("h"))-1] == ss[int(ss.find("k"))+1]:
            b.add(a)
print(len(b),b)

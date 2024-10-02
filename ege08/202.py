import itertools
b = set()
for a in itertools.product("ПИТОН",repeat=4):
    ss = "".join(a).replace("П","Н").replace("Т","Н")
    ss = ss.replace("И","О")
    if "НН" not in ss and "ОО" not in ss:
        b.add(a)
print(len(b),b)



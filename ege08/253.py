import itertools
b = set()
for i,a in enumerate(itertools.product("ОГЭИНФ",repeat=6),1):
    ss = "".join(a).replace("ИГ","Р")
    if (a[0] == "О" or a[-1] == "Э") and a[-1] == "Ф" and a[-2] == "Н" and ss.count("Р") > 0 and "ОГЭ" not in ss:
        b.add(a)
print(len(b),b)
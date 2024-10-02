import itertools
b = set()
for i,a in enumerate(itertools.product("ЕГЭИНФ",repeat=6),1):
    ss = "".join(a).replace("ФИ","Т")
    if a[0] == "Е" and (a[-1] == "Э" or a[-1] == "И") and ss.count("Т") > 1 and "ЕГЭ" not in ss:
        b.add(a)
print(len(b),b)
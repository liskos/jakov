import itertools
b = set()
for i,a in enumerate(itertools.product("ОБЩЕСТВ",repeat=5),1):
    if a[0] != "Щ" and a[0] != "Б" and "ЕВ" not in "".join(a) and "ВЕ" not in "".join(a) and "ТБ" in "".join(a) and a[-2] == "В" and a[-1] == "В":
        b.add(a)
print(len(b),b)
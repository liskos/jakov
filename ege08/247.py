import itertools
b = set()
for a in itertools.product("ГОЛ",repeat=20):
    if ("ЛЛ" not in "".join(a)) and ("ГГ" not in "".join(a)) and ("ОО" not in "".join(a)) and ("ЛГЛ" not in "".join(a)) and ("ОГО" not in "".join(a)) and (a[0] != "Г") and (a[-1] != "Г"):
        b.add(a)

print(len(b))
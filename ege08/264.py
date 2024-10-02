import itertools
b = set()
for i,a in enumerate(itertools.product("ГЕКЭ023",repeat=4),1):
    if (a[0] == "0" or a[0] == "2" or a[0] == "3") and "ГГ" not in "".join(a) and "ЕЕ" not in "".join(a) and "КК" not in "".join(a):
        print(a,i)

import itertools
b = set()
for i,a in enumerate(itertools.product("ЕКЛОСТ",repeat=5),1):
    if a[0] == "С" and "ОО"  in "".join(a):
        print(a,i)

import itertools
for i,a in enumerate(itertools.product("АПРСУ",repeat=5),1):
    if "".join(a).count("У") <2 and "".join(a).count("АА") == 0:
        print(a,i)

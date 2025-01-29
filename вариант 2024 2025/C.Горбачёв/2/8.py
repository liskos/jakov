import itertools

for i,a in enumerate(itertools.product("АИКМНОРТФ",repeat = 6),1):
    if a.count("И") == 0 and a.count("Р") == 3 and a[0] != "А":
        print(i,a)

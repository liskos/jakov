import itertools
b = set()
for i,a in enumerate(itertools.product("КОТ",repeat=6),1):
    if a.count("К") == 2:
        b.add(a)
        print(a)
print(len(b))
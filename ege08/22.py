import itertools
b = set()
for i,a in enumerate(itertools.product("КОТ",repeat=5),1):
    if a.count("О") == 2:
        b.add(a)
        print(a)
print(len(b))
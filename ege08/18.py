import itertools
for i,a in enumerate(itertools.product("ИОУ",repeat=5),1):
    if i == 240:
        print(i,"".join(a))